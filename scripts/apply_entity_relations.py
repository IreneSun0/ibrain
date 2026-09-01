#!/usr/bin/env python3
"""apply_entity_relations.py — merge seeds/entity-relations.yaml into entity frontmatter.

The heavy, evidence-bearing edges live as relationship notes under 06_RELATIONSHIPS/.
This applies the lighter ones, whose evidence is the entity page's own sourced prose,
as typed `related` entries — the same shape concepts use.

The seed is a judgment record. Once applied, frontmatter is the single source of
truth: edit the pages, do not write back into the seed.

  apply_entity_relations.py            # dry run
  apply_entity_relations.py --write    # apply
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import TIMELINE_MARK, iter_notes, schema, vault_root

SEED = Path(__file__).resolve().parent.parent / "seeds" / "entity-relations.yaml"
MARKER = "实体语义关联层"



def render(items: list[dict]) -> str:
    out = ["related:"]
    for it in items:
        out.append(f'  - id: "{it["id"]}"')
        out.append(f'    rel: {it["rel"]}')
        if it.get("note"):
            # notes routinely contain ':' — quote so the scalar stays a scalar
            out.append(f'    note: {json.dumps(it["note"], ensure_ascii=False)}')
    return "\n".join(out)


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--stamp", default="", help="date for the timeline entry (YYYY-MM-DD)")
    args = ap.parse_args()

    seed = yaml.safe_load(SEED.read_text(encoding="utf-8"))["entities"]
    notes = {n.id: n for n in iter_notes() if n.id}
    vocab = set(schema().get("allowed_relationship_types") or [])

    errs = []
    for src, items in seed.items():
        if src not in notes:
            errs.append(f"unknown source id `{src}`")
            continue
        for it in items:
            if it["id"] not in notes:
                errs.append(f"{src}: unknown target `{it['id']}`")
            if it["rel"] not in vocab:
                errs.append(f"{src}: rel `{it['rel']}` not in the entity vocabulary")
    if errs:
        print(f"apply_entity_relations: {len(errs)} problem(s)")
        for e in errs:
            print(f"  {e}")
        return 1

    changed = 0
    for src, items in seed.items():
        n = notes[src]
        text = n.path.read_text(encoding="utf-8")
        stamp_marker = f"{MARKER} ({args.stamp})" if args.stamp else MARKER
        if stamp_marker in text:
            continue  # idempotent per batch
        block = render(items)
        if "\nrelated: []" in text:
            text = text.replace("\nrelated: []", "\n" + block, 1)
        elif "\nrelated:\n" in text:
            # append after the existing list rather than replacing it: legacy bare ids
            # are still meaningful and are upgraded separately.
            lines, out, i = text.split("\n"), [], 0
            while i < len(lines):
                out.append(lines[i])
                if lines[i] == "related:":
                    i += 1
                    while i < len(lines) and lines[i].startswith("  "):
                        out.append(lines[i]); i += 1
                    out.extend(block.split("\n")[1:])
                    continue
                i += 1
            text = "\n".join(out)
        else:
            errs.append(f"{src}: no `related` field to merge into")
            continue
        stamp = args.stamp or "(undated)"
        entry = (f"\n- **{stamp}** — {stamp_marker}: 依实体页已有 CONFIRMED 事实补 "
                 f"{len(items)} 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); "
                 f"证据为本页来源, 未新增断言。\n")
        text = text.rstrip() + entry
        if args.write:
            n.path.write_text(text, encoding="utf-8")
        changed += 1

    verb = "wrote" if args.write else "would write"
    print(f"apply_entity_relations: {verb} {changed} page(s), "
          f"{sum(len(v) for v in seed.values())} edge(s)")
    if errs:
        for e in errs:
            print(f"  {e}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
