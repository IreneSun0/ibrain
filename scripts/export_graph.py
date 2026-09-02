#!/usr/bin/env python3
"""export_graph.py — vault → JSON graph, deterministically ordered.

Every structured note with its quality metadata, its resolved outgoing links and
every typed relationship edge.

`--max-confidentiality LEVEL` drops notes ranked above LEVEL. `internal` is NOT
publishable: anything that leaves this machine needs `public-source`.
"""
from __future__ import annotations

import argparse
import json
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


RECALL_RE = re.compile(r"- Q: (.*?)\n\s+A: (.*?)(?=\n- Q:|\n\n|\Z)", re.DOTALL)


def entity_summary(body: str) -> str:
    """First substantive paragraph of an entity page, for the graph detail panel."""
    for head in ("Executive Summary", "Key Facts", "Mandate",
                 "The Question This Case Answers"):
        s = _section(body, head, 900)
        if s:
            return s
    for para in body.split("\n\n"):
        p = para.strip()
        if p and not p.startswith(("#", ">", "-", "|", "<!--")):
            return p[:900]
    return ""


def concept_content(body: str) -> dict:
    """Full inline content of a concept page for the human learning view."""
    recall = [{"q": " ".join(q.split()), "a": " ".join(a.split())}
              for q, a in RECALL_RE.findall(_section(body, "Active-Recall", 2000))]
    return {
        "why": _section(body, "Why This Matters"),
        "how": _section(body, "How It Works", 1400),
        "example": _section(body, "Concrete Example", 1200),
        "misconceptions": _section(body, "Common Misconceptions", 1200),
        "practice": _section(body, "In Practice"),
        "recall": recall,
    }


def build(max_confidentiality: str | None = None) -> dict:
    max_rank = CONFIDENTIALITY_RANK.get(max_confidentiality) if max_confidentiality else None
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

    # Wikilinks are Obsidian syntax; a browser shows them as literal brackets. Resolve
    # them here, where the target index already exists: to `[[<id>|label]]` when the
    # target is a published note, and to the label alone when it is not.
    WIKI_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(?:\|([^\]]*))?\]\]")

    display = {n.id: str(n.frontmatter.get("title_zh") or n.frontmatter.get("title")
                         or n.path.stem) for n in notes}

    def resolve_wikilinks(text: str) -> str:
        def sub(m):
            raw, label = m.group(1).strip(), (m.group(3) or "").strip()
            tid = target.get(raw.lower()) or target.get(raw.split("/")[-1].lower())
            # a bare [[slug]] shows the target's own name, not its filename
            shown = label or (display.get(tid) if tid else None) or raw.split("/")[-1]
            # U+001F, not `|`: a pipe inside a table cell would split the row
            return f"[[{tid}\u001f{shown}]]" if tid else shown
        return WIKI_RE.sub(sub, text)

    def resolve_deep(v):
        if isinstance(v, str):
            return resolve_wikilinks(v)
        if isinstance(v, list):
            return [resolve_deep(x) for x in v]
        if isinstance(v, dict):
            return {k: resolve_deep(x) for k, x in v.items()}
        return v

    nodes = []
    edges: list[dict] = []
    seen_edges: set[tuple] = set()

    for n in notes:
        fm = n.frontmatter
        conf_level = str(fm.get("confidentiality") or "internal")
        if max_rank is not None and CONFIDENTIALITY_RANK.get(conf_level, 3) > max_rank:
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
            "hasHash": bool(fm.get("content_hash")) if n.ntype == "source" else None,
            "url": str(fm.get("url") or "") if n.ntype == "source" else "",
            "approval": str(fm.get("approval_status") or ""),
            "deadline": str(fm.get("deadline") or ""),
        })

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
            nodes[-1]["definition"] = resolve_wikilinks(definition_excerpt(n.body))
            nodes[-1]["content"] = resolve_deep(concept_content(n.body))
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

        # cases sit on the map beside entities, so they need a summary too
        if n.ntype in ENTITY_TYPES or n.ntype == "case-study":
            nodes[-1]["summary"] = resolve_wikilinks(entity_summary(n.body))

        # entity semantic layer: typed `related` on entity pages — lighter than a
        # relationship note, evidenced by the entity page's own sourced prose
        if n.ntype in ENTITY_TYPES:
            erels = []
            for item in (fm.get("related") or []):
                if isinstance(item, dict) and item.get("id") and item.get("rel"):
                    erels.append({"target": str(item["id"]), "rel": str(item["rel"]),
                                  "note": str(item.get("note") or "")})
            nodes[-1]["relations"] = erels
            for c in erels:
                key = (n.id, c["target"], "erel:" + c["rel"])
                if key not in seen_edges:
                    seen_edges.add(key)
                    edges.append({"source": n.id, "target": c["target"], "kind": "erel",
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
        "maxConfidentiality": max_confidentiality,
        "counts": {
            "notes": len(nodes),
            "edges": len(edges),
            "typedEdges": sum(1 for e in edges if e["kind"] == "typed"),
            "prereqEdges": sum(1 for e in edges if e["kind"] == "prereq"),
            "conceptRelEdges": sum(1 for e in edges if e["kind"] == "crel"),
            "entityRelEdges": sum(1 for e in edges if e["kind"] == "erel"),
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
    ap.add_argument("--max-confidentiality", default=None,
                    choices=list(CONFIDENTIALITY_RANK),
                    help="highest tier to include (use `public-source` for anything "
                         "that leaves this machine); omit to export every note")
    args = ap.parse_args()

    data = build(args.max_confidentiality)
    text = json.dumps(data, ensure_ascii=False, separators=(",", ":"))
    if args.out:
        Path(args.out).write_text(text, encoding="utf-8")
        c = data["counts"]
        print(f"export_graph: {c['notes']} nodes / {c['edges']} edges "
              f"({c['typedEdges']} typed) → {args.out}"
              + (f" [≤{args.max_confidentiality}]" if args.max_confidentiality else ""))
    else:
        print(text)
    return 0


if __name__ == "__main__":
    sys.exit(main())
