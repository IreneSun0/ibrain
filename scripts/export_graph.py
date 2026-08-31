#!/usr/bin/env python3
"""export_graph.py — deterministic vault → JSON graph export.

Produces a single JSON document describing every structured note, its quality
metadata, its resolved outgoing links, and every typed relationship edge.

Two consumers:
  1. the visual dashboard artifact (human overview)
  2. a future GBrain/PGLite indexer (see GBRAIN-INTEGRATION.md)

Confidentiality: the export carries each note's `confidentiality` value so a
downstream consumer can filter. `--max-confidentiality LEVEL` drops anything
ranked above LEVEL. Note that `internal` is NOT publishable — for anything that
leaves the machine, use `--max-confidentiality public-source`.

No LLM. No network. Deterministic ordering throughout.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import WIKILINK_RE, iter_notes, vault_root

FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")

CONFIDENTIALITY_RANK = {
    "public-source": 0,
    "internal": 1,
    "confidential": 2,
    "strictly-private": 3,
}

# Types that represent a "thing in the world" rather than an artifact about it.
ENTITY_TYPES = {
    "person", "organization", "exchange-venue", "protocol-network",
    "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset",
}


def first_heading(body: str) -> str:
    for line in body.split("\n"):
        if line.startswith("# "):
            return line[2:].strip()
    return ""


DEF_RE = re.compile(r"## Executive Definition[^\n]*\n+(.*?)(?:\n\n#|\n#|\Z)", re.DOTALL)


def definition_excerpt(body: str, limit: int = 320) -> str:
    """First definition paragraph of a concept page (importer template layout)."""
    m = DEF_RE.search(body)
    if not m:
        return ""
    text = " ".join(m.group(1).split())
    return text[:limit]


def _section(body: str, head_prefix: str, limit: int = 700) -> str:
    m = re.search(rf"## {head_prefix}[^\n]*\n+(.*?)(?=\n## |\n<!-- timeline -->|\Z)", body, re.DOTALL)
    if not m:
        return ""
    text = m.group(1).strip()
    text = re.sub(r"\n{3,}", "\n\n", text)
    return text[:limit]


# A private vault may carry the applied section under a different heading; name it
# with $IBRAIN_PRACTICE_SECTION so the public tooling stays domain-agnostic.
_PRACTICE_FALLBACK = os.environ.get("IBRAIN_PRACTICE_SECTION", "")

RECALL_RE = re.compile(r"- Q: (.*?)\n\s+A: (.*?)(?=\n- Q:|\n\n|\Z)", re.DOTALL)


def concept_content(body: str) -> dict:
    """Full inline content of a concept page for the human learning view."""
    recall = [{"q": " ".join(q.split()), "a": " ".join(a.split())}
              for q, a in RECALL_RE.findall(_section(body, "Active-Recall", 2000))]
    return {
        "why": _section(body, "Why This Matters"),
        "how": _section(body, "How It Works", 1400),
        "example": _section(body, "Concrete Example", 1200),
        "misconceptions": _section(body, "Common Misconceptions", 1200),
        "practice": _section(body, "In Practice") or (
            _section(body, _PRACTICE_FALLBACK) if _PRACTICE_FALLBACK else ""),
        "recall": recall,
    }


def build(public_only: bool = False, max_confidentiality: str = "internal") -> dict:
    """`public_only` is a deprecated alias for max_confidentiality="internal"."""
    max_rank = CONFIDENTIALITY_RANK.get(max_confidentiality, 1)
    root = vault_root()
    notes = [n for n in iter_notes() if n.id]

    # source-note locator index (concept pages reference sources by id)
    src_index = {n.id: {"title": str(n.frontmatter.get("title") or n.path.stem),
                        "url": str(n.frontmatter.get("url") or "")}
                 for n in notes if n.ntype == "source"}

    # ── resolve link targets the way Obsidian does: filename / path / alias ──
    target: dict[str, str] = {}
    for n in notes:
        rel_no_ext = str(n.path.relative_to(root).with_suffix(""))
        for key in (n.path.stem, rel_no_ext, *(str(a) for a in (n.frontmatter.get("aliases") or []) if a)):
            target.setdefault(key.strip().lower(), n.id)

    nodes = []
    edges: list[dict] = []
    seen_edges: set[tuple] = set()

    for n in notes:
        fm = n.frontmatter
        conf_level = str(fm.get("confidentiality") or "internal")
        if public_only and CONFIDENTIALITY_RANK.get(conf_level, 3) > max_rank:
            continue

        srcs = [str(s) for s in (fm.get("sources") or []) if s]
        nodes.append({
            "id": n.id,
            "type": n.ntype or "unknown",
            "isEntity": (n.ntype in ENTITY_TYPES),
            "title": str(fm.get("title") or n.path.stem),
            "titleZh": str(fm.get("title_zh") or ""),
            "path": str(n.path.relative_to(root)),
            "stem": n.path.stem,
            "status": str(fm.get("status") or "unknown"),
            "importance": str(fm.get("importance") or ""),
            "confidence": str(fm.get("confidence") or "unknown"),
            "epistemic": str(fm.get("epistemic_status") or "unknown"),
            "confidentiality": conf_level,
            "domains": [str(d) for d in (fm.get("domains") or [])],
            "sourceCount": len(srcs),
            "lastVerified": str(fm.get("last_verified") or ""),
            "reviewAfter": str(fm.get("review_after") or ""),
            # source-note specific: does the evidence actually exist locally?
            "hasHash": bool(fm.get("content_hash")) if n.ntype == "source" else None,
            "url": str(fm.get("url") or "") if n.ntype == "source" else "",
            "approval": str(fm.get("approval_status") or ""),
            "deadline": str(fm.get("deadline") or ""),
        })

        # concept semantic layer: hard prerequisites + typed relations (frontmatter)
        if n.ntype == "concept":
            prereqs = [str(p) for p in (fm.get("prerequisites") or []) if p]
            crels = []
            for item in (fm.get("related") or []):
                if isinstance(item, dict) and item.get("id") and item.get("rel"):
                    crels.append({"target": str(item["id"]), "rel": str(item["rel"]),
                                  "note": str(item.get("note") or "")})
                elif not isinstance(item, dict) and item:
                    crels.append({"target": str(item), "rel": "", "note": ""})
            nodes[-1]["prerequisites"] = prereqs
            nodes[-1]["relations"] = crels
            nodes[-1]["definition"] = definition_excerpt(n.body)
            nodes[-1]["content"] = concept_content(n.body)
            nodes[-1]["resources"] = [
                {"title": src_index[s]["title"], "url": src_index[s]["url"]}
                for s in srcs if s in src_index and src_index[s]["url"]]
            for p in prereqs:
                key = (p, n.id, "prereq")
                if key not in seen_edges:
                    seen_edges.add(key)
                    # source = prerequisite (learn first), target = dependent (unlocked)
                    edges.append({"source": p, "target": n.id, "kind": "prereq"})
            for c in crels:
                key = (n.id, c["target"], "crel:" + c["rel"])
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"source": n.id, "target": c["target"], "kind": "crel",
                                  "relType": c["rel"], "note": c["note"]})

        # typed relationship edges (the authoritative relationship model)
        if n.ntype == "relationship":
            a, b = str(fm.get("entity_a") or ""), str(fm.get("entity_b") or "")
            if a and b:
                key = (a, b, str(fm.get("relationship_type") or ""))
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({
                        "source": a, "target": b, "kind": "typed",
                        "relType": str(fm.get("relationship_type") or ""),
                        "relStatus": str(fm.get("relationship_status") or "unknown"),
                        "note": n.id,
                    })

        # body wikilinks (weak association edges)
        body = INLINE_CODE_RE.sub("", FENCE_RE.sub("", n.body))
        for m in WIKILINK_RE.finditer(body):
            tid = target.get(m.group(1).strip().lower())
            if tid and tid != n.id:
                key = (n.id, tid, "link")
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"source": n.id, "target": tid, "kind": "link"})

    node_ids = {x["id"] for x in nodes}
    edges = [e for e in edges if e["source"] in node_ids and e["target"] in node_ids]

    by_type = Counter(x["type"] for x in nodes)
    by_status = Counter(x["status"] for x in nodes)
    by_domain: Counter = Counter()
    for x in nodes:
        for d in x["domains"] or ["(none)"]:
            by_domain[d] += 1

    src_nodes = [x for x in nodes if x["type"] == "source"]
    return {
        "generated": date.today().isoformat(),
        "vault": str(root),
        "publicOnly": public_only,
        "counts": {
            "notes": len(nodes),
            "edges": len(edges),
            "typedEdges": sum(1 for e in edges if e["kind"] == "typed"),
            "prereqEdges": sum(1 for e in edges if e["kind"] == "prereq"),
            "conceptRelEdges": sum(1 for e in edges if e["kind"] == "crel"),
            "entities": sum(1 for x in nodes if x["isEntity"]),
            "byType": dict(sorted(by_type.items(), key=lambda kv: -kv[1])),
            "byStatus": dict(sorted(by_status.items(), key=lambda kv: -kv[1])),
            "byDomain": dict(sorted(by_domain.items(), key=lambda kv: -kv[1])),
            "sources": len(src_nodes),
            "sourcesWithHash": sum(1 for x in src_nodes if x["hasHash"]),
            "sourcesWithUrlNoHash": sum(1 for x in src_nodes if x["url"] and not x["hasHash"]),
        },
        "nodes": sorted(nodes, key=lambda x: x["id"]),
        "edges": sorted(edges, key=lambda e: (e["source"], e["target"], e["kind"])),
    }


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None, help="output path (default: stdout)")
    ap.add_argument("--public-only", action="store_true",
                    help="apply the confidentiality ceiling set by --max-confidentiality")
    ap.add_argument("--max-confidentiality", default="internal",
                    choices=list(CONFIDENTIALITY_RANK),
                    help="highest tier to include when --public-only is set "
                         "(use `public-source` for anything that leaves this machine)")
    args = ap.parse_args()

    data = build(public_only=args.public_only, max_confidentiality=args.max_confidentiality)
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        c = data["counts"]
        print(f"export_graph: {c['notes']} nodes / {c['edges']} edges "
              f"({c['typedEdges']} typed) → {args.out}"
              + (f" [≤{args.max_confidentiality}]" if args.public_only else ""))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
