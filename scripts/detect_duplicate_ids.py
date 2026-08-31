#!/usr/bin/env python3
"""detect_duplicate_ids.py — no two notes may share a canonical frontmatter id.
Also flags duplicate filenames (basenames) across the vault, which break
shortest-path wikilinks in Obsidian. Exit 1 on duplicates."""
from __future__ import annotations

import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root


def main() -> int:
    by_id: dict[str, list[str]] = defaultdict(list)
    by_name: dict[str, list[str]] = defaultdict(list)
    root = vault_root()
    for n in iter_notes():
        rel = str(n.path.relative_to(root))
        if n.id:
            by_id[n.id].append(rel)
        by_name[n.path.name].append(rel)
    bad = False
    for nid, paths in sorted(by_id.items()):
        if len(paths) > 1:
            bad = True
            print(f"DUPLICATE ID `{nid}`:")
            for p in paths:
                print(f"    {p}")
    for name, paths in sorted(by_name.items()):
        if len(paths) > 1:
            bad = True
            print(f"DUPLICATE FILENAME `{name}` (breaks shortest-path links):")
            for p in paths:
                print(f"    {p}")
    if bad:
        return 1
    print("detect_duplicate_ids: OK (all ids and filenames unique)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
