#!/usr/bin/env python3
"""apply_concept_relations.py — merge seeds/concept-relations.yaml into concept frontmatter.

One-shot deterministic writer for the 2026-08-27 semantic-relations layer:
  - sets `prerequisites` + typed `related` on every concept page from the seed file;
  - bumps `updated`, locks `import_origin` to `xlsx-learning-map+manual` (importer hand-off);
  - appends one audit entry to the page timeline (idempotent per marker);
  - replaces the importer's "(librarian 待补链)" placeholder in the body.

The seed file is a judgment record; after applying, frontmatter is the single
source of truth (edit pages directly, do not write back into the seed).

Usage:
  apply_concept_relations.py            # dry-run report
  apply_concept_relations.py --write    # apply
Exit 0 = clean, 1 = seed/vault mismatch or coverage error.
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import TIMELINE_MARK, build_frontmatter, iter_notes, vault_root

SEED = Path(__file__).resolve().parent.parent / "seeds" / "concept-relations.yaml"
STAMP = "2026-08-27"
TIMELINE_MARKER = "语义关联层判断"
PLACEHOLDER = "- (librarian 待补链)"
PLACEHOLDER_NEW = ("- 见 frontmatter `prerequisites` / `related` (typed, "
                   f"{STAMP} 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true", help="apply changes (default: dry-run)")
    args = ap.parse_args()

    data = yaml.safe_load(SEED.read_text(encoding="utf-8"))
    seed = data.get("concepts") or {}

    notes = {n.id: n for n in iter_notes() if n.ntype == "concept"}
    known_ids = {n.id for n in iter_notes() if n.id}

    errors = []
    missing_in_seed = sorted(set(notes) - set(seed))
    unknown_in_seed = sorted(set(seed) - set(notes))
    if missing_in_seed:
        errors.append(f"concepts missing from seed (must be explicitly judged): {missing_in_seed}")
    if unknown_in_seed:
        errors.append(f"seed keys not found in vault: {unknown_in_seed}")
    for cid, spec in seed.items():
        for pid in spec.get("prerequisites") or []:
            if pid not in notes:
                errors.append(f"{cid}: prerequisite `{pid}` is not a vault concept")
        for rel in spec.get("relations") or []:
            if not isinstance(rel, dict) or "id" not in rel or "rel" not in rel:
                errors.append(f"{cid}: malformed relation entry {rel!r}")
            elif rel["id"] not in known_ids:
                errors.append(f"{cid}: relation target `{rel['id']}` unknown")
    if errors:
        for e in errors:
            print("ERROR:", e)
        return 1

    changed = unchanged = 0
    n_pre = n_rel = 0
    for cid in sorted(seed):
        n = notes[cid]
        spec = seed[cid]
        pre = [str(x) for x in (spec.get("prerequisites") or [])]
        rels = []
        for r in spec.get("relations") or []:
            entry = {"id": str(r["id"]), "rel": str(r["rel"])}
            if r.get("note"):
                entry["note"] = str(r["note"])
            rels.append(entry)
        n_pre += len(pre)
        n_rel += len(rels)

        fm = dict(n.frontmatter)
        fm["related"] = rels
        fm["prerequisites"] = pre
        fm["updated"] = STAMP
        if fm.get("import_origin") == "xlsx-learning-map":
            fm["import_origin"] = "xlsx-learning-map+manual"

        body = n.body
        if PLACEHOLDER in body:
            body = body.replace(PLACEHOLDER, PLACEHOLDER_NEW)
        if TIMELINE_MARKER not in body:
            pre_txt = ", ".join(p.split(":", 1)[1] for p in pre) if pre else "无硬前置 (判断过的空)"
            entry = (f"- **{STAMP}** — {TIMELINE_MARKER} (Claude seed, 待 Irene 复核): "
                     f"前置 = {pre_txt}; typed 关系 {len(rels)} 条。词表见 "
                     f"[[relationship-types|关系类型受控词表]]。")
            if TIMELINE_MARK in body:
                body = body.rstrip("\n") + "\n" + entry + "\n"
            else:
                body = body.rstrip("\n") + f"\n\n{TIMELINE_MARK}\n\n## Timeline\n\n" + entry + "\n"

        new_text = build_frontmatter(fm) + "\n" + body
        old_text = n.path.read_text(encoding="utf-8")
        if new_text != old_text:
            changed += 1
            if args.write:
                n.path.write_text(new_text, encoding="utf-8")
        else:
            unchanged += 1

    mode = "APPLIED" if args.write else "DRY-RUN"
    print(f"apply_concept_relations [{mode}]: {len(seed)} concepts, "
          f"{n_pre} prerequisite edges, {n_rel} typed relations; "
          f"{changed} files changed, {unchanged} unchanged")
    return 0


if __name__ == "__main__":
    sys.exit(main())
