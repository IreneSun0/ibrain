#!/usr/bin/env python3
"""build_learning_view.py — Irene 的主线通关地图 (self-contained HTML).

Speedrun edition: the view renders the 81-quest mainline from
10_LEARNING/plan/mainline.yaml (prerequisite closure of the target skill set),
with the other 62 concepts folded away as skippable side quests. All concept
content (definition / why / how / example / misconceptions / practice / recall) is
inlined — no jumping out to Obsidian. Exercises are embedded per chapter.

Pipeline: export_graph.build() + mainline.yaml + schedule.yaml + compute_score
→ scripts/learning_view_template.html → dist/ibrain-learning.html.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import compute_score
import export_graph
from brainlib import OPS_ROOT, vault_root

PLACEHOLDER = "/*__DATA__*/{}"
EX_Q_RE = re.compile(r"^## (Q\d+) \[(.+?)\] (.*)$")
QUEST_RE = re.compile(r"^## quest: (concept:[a-z0-9._-]+)\s*$")
SUB_RE = re.compile(r"^### (hook|card|mechanism|traps|ammo|drill)\s*$")



def parse_exercises(path: Path) -> list[dict]:
    """Parse a deck file's `## Qn [type] title` blocks; quoted lines = answer."""
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
    mainline = compute_score.load_yaml(plan_dir / "mainline.yaml")
    chapters = mainline.get("chapters") or []
    side_map = {str(k): int(v) for k, v in (mainline.get("side_domain_chapter") or {}).items()}
    ex_map = {str(k): int(v) for k, v in (mainline.get("exercise_chapter") or {}).items()}

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

    # ── exercises embedded per chapter ──
    ex_of: dict[int, list[dict]] = {}
    ex_dir = root / "10_LEARNING" / "exercises"
    if ex_dir.exists():
        for p in sorted(ex_dir.glob("*.md")):
            chn = ex_map.get(p.stem)
            if chn is None:
                m = re.match(r"chapter-(\d+)", p.stem)
                chn = int(m.group(1)) if m else None
            if chn is None:
                print(f"WARNING: exercises file {p.name} has no chapter mapping; skipped")
                continue
            ex_of.setdefault(chn, []).extend(parse_exercises(p))

    # ── training layer: personal bootcamp state, absent from any public build ──
    training = None
    sched_path = plan_dir / "schedule.yaml"
    if False and sched_path.exists():
        sched = compute_score.load_yaml(sched_path)
        score = compute_score.build()
        training = {
            "deadline": str(sched.get("deadline") or ""),
            "event": {"name": (sched.get("event") or {}).get("name", ""),
                      "date": str(((sched.get("event") or {}).get("dates") or [""])[0])},
            "industry": score["industry"], "pm": score["pm"],
            "mainDone": score["concepts"]["all"],
            "nextTarget": None if not score["nextTarget"] else
                {k: str(v) for k, v in score["nextTarget"].items()},
            "weeks": [{"n": w["n"], "start": str(w["start"]), "end": str(w["end"]),
                       "chapters": w.get("chapters") or []} for w in (sched.get("weeks") or [])],
        }

    # The landing graph is the whole knowledge base, not a slice of it: every note
    # and every edge, so the picture actually shows what the vault contains.
    ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                    "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset"}
    nodes = graph["nodes"]
    edges = graph["edges"]

    data = {
        "generated": graph["generated"],
        "chapters": [{"n": int(ch["n"]), "title": str(ch["title"]),
                      "titleEn": str(ch.get("title_en") or ""),
                      "question": str(ch.get("question") or ""),
                      "questionEn": str(ch.get("question_en") or ""),
                      "concepts": list(ch.get("concepts") or []),
                      "side": side_of.get(int(ch["n"]), []),
                      "exercises": ex_of.get(int(ch["n"]), []),
                      "svg": svgs.get(int(ch["n"]), "")} for ch in chapters],
        "mainOrder": order,
        "entityTypes": sorted(ENTITY_TYPES),
        "nodes": nodes,
        "edges": edges,
        "training": training,
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
