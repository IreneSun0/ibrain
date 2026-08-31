#!/usr/bin/env python3
"""Convert frontmatter-id wikilinks to native Obsidian filename targets.

Dry-run by default. Pass --write to update files. Frontmatter is never changed,
links in fenced code are ignored, and 09_ORIGINALS/irene is always excluded.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
LINK_RE = re.compile(r"\[\[([^\]|#]+)(#[^\]|]*)?(\|[^\]]*)?\]\]")
FM_RE = re.compile(r"\A---\s*\n.*?\n---\s*\n?", re.DOTALL)


def rewrite_segment(text: str, id_to_stem: dict[str, str]) -> tuple[str, int]:
    count = 0

    def replace(match: re.Match[str]) -> str:
        nonlocal count
        target = match.group(1).strip()
        stem = id_to_stem.get(target.lower())
        if not stem:
            return match.group(0)
        count += 1
        return f"[[{stem}{match.group(2) or ''}{match.group(3) or ''}]]"

    return LINK_RE.sub(replace, text), count


def rewrite_body(body: str, id_to_stem: dict[str, str]) -> tuple[str, int]:
    parts, total, cursor = [], 0, 0
    for fence in FENCE_RE.finditer(body):
        rewritten, count = rewrite_segment(body[cursor:fence.start()], id_to_stem)
        parts.extend((rewritten, fence.group(0)))
        total += count
        cursor = fence.end()
    rewritten, count = rewrite_segment(body[cursor:], id_to_stem)
    parts.append(rewritten)
    return "".join(parts), total + count


def main(argv: list[str]) -> int:
    write = "--write" in argv
    root = vault_root()
    notes = list(iter_notes())
    id_to_stem = {n.id.lower(): n.path.stem for n in notes if n.id}
    changed_files, changed_links = 0, 0
    for note in notes:
        rel = note.path.relative_to(root)
        if rel.parts[:2] == ("09_ORIGINALS", "irene"):
            continue
        raw = note.path.read_text(encoding="utf-8")
        fm = FM_RE.match(raw)
        prefix = fm.group(0) if fm else ""
        body = raw[fm.end():] if fm else raw
        new_body, count = rewrite_body(body, id_to_stem)
        if not count:
            continue
        changed_files += 1
        changed_links += count
        print(f"  {rel}: {count}")
        if write:
            note.path.write_text(prefix + new_body, encoding="utf-8")
    mode = "updated" if write else "would update"
    print(f"normalize_wikilinks: {mode} {changed_links} link(s) in {changed_files} file(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
