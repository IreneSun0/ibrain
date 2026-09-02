#!/usr/bin/env python3
"""build_learning_view.py — the whole vault as one self-contained HTML page.

The landing view is the graph of every note. The reading view walks a 81-step
reading path from 10_LEARNING/plan/mainline.yaml (the prerequisite closure of the
core concepts), with the other 62 concepts kept alongside it as side entries. All
concept content is inlined, so the page needs neither Obsidian nor a server.

Pipeline: export_graph.build() + mainline.yaml → learning_view_template.html → docs/index.html.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import export_graph
import yaml
from brainlib import OPS_ROOT, vault_root

PLACEHOLDER = "/*__DATA__*/{}"
EX_Q_RE = re.compile(r"^## (Q\d+) \[(.+?)\] (.*)$")
QUEST_RE = re.compile(r"^## quest: (concept:[a-z0-9._-]+)\s*$")
SUB_RE = re.compile(r"^### (hook|card|mechanism|traps|ammo|drill)\s*$")



def parse_exercises(path: Path) -> list[dict]:
    """Parse a deck file's `## Qn [type] title` blocks; quoted lines = answer.

    A `concept: concept:<slug>` line directly under the heading attaches the
    question to that concept. Exercises and a concept's own recall questions are
    the same object — a prompt with a hidden answer — so they end up in one list.
    """
    items: list[dict] = []
    cur: dict | None = None
    body_lines: list[str] = []
    ans_lines: list[str] = []

    def flush():
        if cur is not None:
            cur["body"] = "\n".join(body_lines).strip()
            cur["answer"] = "\n".join(ans_lines).strip()
            items.append(cur)

    for line in path.read_text(encoding="utf-8").split("\n"):
        m = EX_Q_RE.match(line)
        if m:
            flush()
            cur = {"n": m.group(1), "kind": m.group(2), "title": m.group(3).strip()}
            body_lines, ans_lines = [], []
            continue
        if cur is None:
            continue
        if line.startswith("concept:") and not cur.get("concept"):
            cur["concept"] = line.split(":", 1)[1].strip()
            continue
        if line.startswith(">"):
            ans_lines.append(line.lstrip("> ").rstrip())
        elif line.startswith("## ") or line.startswith("# "):
            flush()
            cur = None
        else:
            body_lines.append(line.rstrip())
    flush()
    return items


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--out", default=None)
    args = ap.parse_args(argv)

    tpl_path = OPS_ROOT / "scripts" / "learning_view_template.html"
    tpl = tpl_path.read_text(encoding="utf-8")
    if PLACEHOLDER not in tpl:
        print(f"ERROR: placeholder missing from {tpl_path}", file=sys.stderr)
        return 1

    root = vault_root()
    plan_dir = root / "10_LEARNING" / "plan"
    mainline = yaml.safe_load((plan_dir / "mainline.yaml").read_text(encoding="utf-8")) or {}
    chapters = mainline.get("chapters") or []
    side_map = {str(k): int(v) for k, v in (mainline.get("side_domain_chapter") or {}).items()}

    graph = export_graph.build()
    concepts = {n["id"]: n for n in graph["nodes"] if n["type"] == "concept"}

    # ── mainline integrity: every quest exists, prerequisites appear earlier ──
    order: dict[str, int] = {}
    errors = []
    for ch in chapters:
        for cid in ch.get("concepts") or []:
            if cid not in concepts:
                errors.append(f"mainline quest `{cid}` is not a vault concept")
                continue
            if cid in order:
                errors.append(f"mainline quest `{cid}` listed twice")
            order[cid] = len(order) + 1
    for cid, idx in order.items():
        for p in concepts[cid].get("prerequisites") or []:
            if p in order and order[p] >= idx:
                errors.append(f"topology: `{p}` must come before `{cid}`")
            # prerequisites outside the mainline would break the closure promise
            if p not in order:
                errors.append(f"closure: `{cid}` needs `{p}` which is not on the mainline")
    if errors:
        for e in errors:
            print("ERROR:", e, file=sys.stderr)
        return 1

    # ── side quests fold into chapters by domain ──
    side_of: dict[int, list[str]] = {int(ch["n"]): [] for ch in chapters}
    unmapped = []
    for cid, node in sorted(concepts.items()):
        if cid in order:
            continue
        dom = (node.get("domains") or ["(none)"])[0]
        chn = side_map.get(dom)
        if chn is None:
            unmapped.append(f"{cid} (domain {dom})")
            chn = max(side_of)
        side_of[chn].append(cid)
    if unmapped:
        print(f"WARNING: side quests without domain mapping → last chapter: {unmapped}")

    # ── per-chapter mechanism diagrams ──
    svgs: dict[int, str] = {}
    for ch in chapters:
        p = OPS_ROOT / "scripts" / "assets" / f"chapter-{ch['n']}.svg"
        if p.exists():
            svgs[int(ch["n"])] = p.read_text(encoding="utf-8")

    # ── exercises: same shape as recall, so they merge into the same list ──
    ex_of: dict[str, list[dict]] = {}
    ex_dir = root / "10_LEARNING" / "exercises"
    if ex_dir.exists():
        for p in sorted(ex_dir.glob("*.md")):
            for ex in parse_exercises(p):
                cid = ex.get("concept")
                if not cid:
                    print(f"WARNING: {p.name} {ex['n']} has no concept: marker; skipped")
                    continue
                ex_of.setdefault(cid, []).append(
                    {"q": "\n".join(x for x in (ex["title"], ex["body"]) if x),
                     "a": ex["answer"], "kind": ex["kind"]})

    # The landing graph is the whole knowledge base, not a slice of it: every note
    # and every edge, so the picture actually shows what the vault contains.
    ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                    "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset"}
    nodes = graph["nodes"]
    edges = graph["edges"]

    # One self-test list per concept: its own recall prompts, then the exercises
    # written against it. Same object, so they are not shown as two sections.
    unattached = set(ex_of)
    for n in nodes:
        extra = ex_of.get(n["id"])
        if not extra:
            continue
        unattached.discard(n["id"])
        c = n.setdefault("content", {})
        c["recall"] = [dict(q, kind=q.get("kind", "\u5fc6")) for q in (c.get("recall") or [])] + extra
    for cid in sorted(unattached):
        print(f"WARNING: exercises reference unknown concept {cid}")

    data = {
        "generated": graph["generated"],
        "chapters": [{"n": int(ch["n"]), "title": str(ch["title"]),
                      "titleEn": str(ch.get("title_en") or ""),
                      "question": str(ch.get("question") or ""),
                      "questionEn": str(ch.get("question_en") or ""),
                      "concepts": list(ch.get("concepts") or []),
                      "side": side_of.get(int(ch["n"]), []),
                      "svg": svgs.get(int(ch["n"]), "")} for ch in chapters],
        "mainOrder": order,
        "entityTypes": sorted(ENTITY_TYPES),
        "nodes": nodes,
        "edges": edges,
    }

    html = tpl.replace(PLACEHOLDER, json.dumps(data, ensure_ascii=False, separators=(",", ":")))
    out = Path(args.out) if args.out else OPS_ROOT / "dist" / "ibrain-learning.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html, encoding="utf-8")

    # A syntax error in the template silently ships a blank page, so fail the build
    # instead. Skipped (with a warning) where node is unavailable.
    import shutil, subprocess, tempfile
    node = shutil.which("node")
    if node:
        m = re.search(r"<script>\n(.*)\n</script>", html, re.S)
        if m:
            with tempfile.NamedTemporaryFile("w", suffix=".js", delete=False,
                                             encoding="utf-8") as fh:
                fh.write(m.group(1))
                probe = fh.name
            r = subprocess.run([node, "--check", probe], capture_output=True, text=True)
            Path(probe).unlink(missing_ok=True)
            if r.returncode != 0:
                print("build_learning_view: template JS does not parse\n" + r.stderr,
                      file=sys.stderr)
                return 1
    else:
        print("build_learning_view: node not found — skipping JS syntax check")
    kb = round(len(html.encode("utf-8")) / 1024)
    n_ex = sum(len(v) for v in ex_of.values())
    print(f"build_learning_view: mainline {len(order)} quests / {len(chapters)} chapters / "
          f"side {sum(len(v) for v in side_of.values())} / "
          f"{len(svgs)} diagrams / {n_ex} exercises → {out} ({kb} KB)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
