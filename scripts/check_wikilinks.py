#!/usr/bin/env python3
"""check_wikilinks.py — validate native Obsidian [[wikilinks]].

A link target resolves if it matches (case-insensitive):
  - a note basename or vault-relative path (without .md), or
  - any alias declared in frontmatter.
Frontmatter ids are intentionally NOT targets: Obsidian does not resolve them unless
they are also a filename, path, or declared alias. Ambiguous aliases are failures.
Unresolved links are reported; exit 1 if any. Links inside code fences are ignored.
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import WIKILINK_RE, iter_notes, vault_root

FENCE_RE = re.compile(r"```.*?```", re.DOTALL)
INLINE_CODE_RE = re.compile(r"`[^`\n]*`")


def main(argv: list[str]) -> int:
    root = vault_root()
    targets: dict[str, set[str]] = {}
    notes = list(iter_notes())
    target_notes = list(iter_notes(include_templates=True))

    def add_target(key: str, path: Path) -> None:
        key = key.strip().lower()
        if key:
            targets.setdefault(key, set()).add(str(path.relative_to(root)))

    for n in target_notes:
        rel_no_ext = str(n.path.relative_to(root).with_suffix(""))
        add_target(n.path.stem, n.path)
        add_target(rel_no_ext, n.path)
        for a in (n.frontmatter.get("aliases") or []):
            if a:
                add_target(str(a), n.path)
    broken: list[tuple[str, str]] = []
    ambiguous: list[tuple[str, str, list[str]]] = []
    total_links = 0
    for n in notes:
        body = INLINE_CODE_RE.sub("", FENCE_RE.sub("", n.body)).replace("\\|", "|")
        for m in WIKILINK_RE.finditer(body):
            t = m.group(1).strip()
            if not t:
                continue
            total_links += 1
            key = t.removesuffix(".md").lower()
            if key.endswith(".canvas") or key.endswith(".png") or key.endswith(".pdf"):
                if (root / t).exists() or any(root.rglob(t)):
                    continue
            matches = targets.get(key, set())
            if not matches:
                broken.append((str(n.path.relative_to(root)), t))
            elif len(matches) > 1:
                ambiguous.append((str(n.path.relative_to(root)), t, sorted(matches)))
    if broken or ambiguous:
        print(f"check_wikilinks: {len(broken)} broken, {len(ambiguous)} ambiguous / {total_links} total")
        for src, t in broken:
            print(f"  {src} -> [[{t}]]")
        for src, t, matches in ambiguous:
            print(f"  {src} -> [[{t}]] is ambiguous: {', '.join(matches)}")
        return 1
    print(f"check_wikilinks: OK ({total_links} links, 0 broken)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
