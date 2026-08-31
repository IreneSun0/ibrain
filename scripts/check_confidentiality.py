#!/usr/bin/env python3
"""Prevent confidentiality downgrades and unprotected raw conversation files."""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

RANK = {"public-source": 0, "internal": 1, "confidential": 2, "strictly-private": 3}
RAW_PREFIXES = (("01_INBOX", "transcripts"), ("01_INBOX", "unprocessed"))


def findings():
    root = vault_root()
    notes = list(iter_notes())
    by_id = {n.id: n for n in notes if n.id}
    errors = []
    for note in notes:
        rel = note.path.relative_to(root)
        level = str(note.frontmatter.get("confidentiality") or "")
        if rel.parts[:2] in RAW_PREFIXES and level != "strictly-private":
            errors.append(f"{rel}: raw conversation artifact must be strictly-private")
        for source_id in note.frontmatter.get("sources") or []:
            source = by_id.get(str(source_id))
            if not source:
                continue  # referential integrity is handled by validate_frontmatter
            source_level = str(source.frontmatter.get("confidentiality") or "")
            if RANK.get(level, -1) < RANK.get(source_level, -1):
                errors.append(
                    f"{rel}: confidentiality `{level}` is lower than source `{source_id}` ({source_level})")
    return errors


def main() -> int:
    errors = findings()
    if errors:
        print(f"check_confidentiality: {len(errors)} violation(s)")
        for error in errors:
            print(f"  {error}")
        return 1
    print("check_confidentiality: OK (no source downgrade; raw conversations protected)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
