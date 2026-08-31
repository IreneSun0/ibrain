#!/usr/bin/env python3
"""find_orphan_notes.py — notes with NO incoming wikilinks (reachability by links,
not folders). MOCs/dashboards/policies are roots and never orphans; generated
index pages count as link sources only if they are real notes. Report-only, exit 0."""
from __future__ import annotations

import re
import sys
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import WIKILINK_RE, iter_notes, vault_root

ROOT_TYPES = {"moc", "dashboard", "policy", "taxonomy", "template", "curriculum", "report"}
ROOT_DIRS = ("00_HOME", "90_META", "10_LEARNING/curriculum", "11_OUTPUTS")
FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def main() -> int:
    root = vault_root()
    notes = list(iter_notes())
    incoming: dict[str, int] = defaultdict(int)
    keys: dict[str, list[str]] = {}
    for n in notes:
        ks = [n.path.stem.lower()]
        if n.id:
            ks.append(n.id.lower())
        for a in (n.frontmatter.get("aliases") or []):
            if a:
                ks.append(str(a).lower())
        keys[str(n.path)] = ks
    target_owner: dict[str, str] = {}
    for pth, ks in keys.items():
        for k in ks:
            target_owner.setdefault(k, pth)
    for n in notes:
        body = INLINE_CODE_RE.sub("", FENCE_RE.sub("", n.body))
        for m in WIKILINK_RE.finditer(body):
            t = m.group(1).strip().lower()
            owner = target_owner.get(t)
            if owner and owner != str(n.path):
                incoming[owner] += 1
    orphans = []
    for n in notes:
        rel = str(n.path.relative_to(root))
        if n.ntype in ROOT_TYPES or any(rel.startswith(d) for d in ROOT_DIRS):
            continue
        if incoming.get(str(n.path), 0) == 0:
            orphans.append(rel)
    if orphans:
        print(f"find_orphan_notes: {len(orphans)} orphan(s) — no incoming links:")
        for o in orphans:
            print(f"  {o}")
    else:
        print("find_orphan_notes: OK (no orphans)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
