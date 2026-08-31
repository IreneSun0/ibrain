#!/usr/bin/env python3
"""generate_mocs.py — maintain the GENERATED sections inside Maps of Content.

MOC pages are hand-authored (curation is judgment), but each may contain a
generated inventory block delimited by:
    <!-- moc:auto domain=<domain> type=<type> -->
    ...regenerated content...
    <!-- /moc:auto -->
This script rewrites only what is inside the markers — hand-written prose
around them is preserved. Filters: domain=X, type=Y (both optional, AND-ed).
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

BLOCK_RE = re.compile(r"(<!-- moc:auto([^>]*)-->)(.*?)(<!-- /moc:auto -->)", re.DOTALL)
ARG_RE = re.compile(r"(domain|type|folder)=([a-z0-9_/-]+)")


def render(notes, args: dict) -> str:
    sel = []
    for n in notes:
        if not n.id:
            continue
        if "type" in args and n.ntype != args["type"]:
            continue
        if "domain" in args and args["domain"] not in [str(d) for d in (n.frontmatter.get("domains") or [])]:
            continue
        if "folder" in args and not str(n.path).replace("\\", "/").find("/" + args["folder"]) >= 0:
            continue
        sel.append(n)
    sel.sort(key=lambda n: (({"tier-1": 0, "tier-2": 1, "tier-3": 2}).get(str(n.frontmatter.get("importance")), 3), n.path.stem))
    lines = ["\n"]
    for n in sel:
        zh = n.frontmatter.get("title_zh")
        tier = n.frontmatter.get("importance") or ""
        status = n.frontmatter.get("status") or ""
        extra = f" · {zh}" if zh and zh != n.frontmatter.get("title") else ""
        badge = " ⭐" if tier == "tier-1" else ""
        lines.append(f"- [[{n.path.stem}|{n.frontmatter.get('title') or n.path.stem}]]{extra}{badge} `{status}`")
    lines.append("\n")
    return "\n".join(lines)


def main() -> int:
    root = vault_root()
    notes = list(iter_notes())
    changed = 0
    for n in notes:
        text = n.path.read_text(encoding="utf-8")
        if "moc:auto" not in text:
            continue

        def sub(m):
            args = dict(ARG_RE.findall(m.group(2)))
            return m.group(1) + render(notes, args) + m.group(4)

        new = BLOCK_RE.sub(sub, text)
        if new != text:
            n.path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"generate_mocs: refreshed auto-blocks in {changed} MOC file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
