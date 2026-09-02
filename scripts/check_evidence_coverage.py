#!/usr/bin/env python3
"""Report which verified notes reach preserved evidence.

A preserved path shows that hashed content exists, not that it supports every claim.
"""
from __future__ import annotations

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root


def evidence_kinds(note_id: str, by_id: dict, seen: set[str] | None = None) -> set[str]:
    seen = set(seen or ())
    if note_id in seen:
        return {"cycle"}
    seen.add(note_id)
    note = by_id.get(note_id)
    if not note:
        return {"missing"}
    if note.ntype == "source":
        if note.frontmatter.get("content_hash"):
            return {"preserved"}
        if note.frontmatter.get("archive_path"):
            return {"archive-unhashed"}
        if note.frontmatter.get("url"):
            return {"live-url-only"}
        return {"no-locator"}
    refs = note.frontmatter.get("sources") or []
    if not refs:
        return {"unsourced-intermediary"}
    result = set()
    for ref in refs:
        result.update(evidence_kinds(str(ref), by_id, seen))
    return result


def main() -> int:
    root = vault_root()
    notes = [note for note in iter_notes() if note.id]
    by_id = {note.id: note for note in notes}
    verified = [note for note in notes if note.ntype != "source" and note.frontmatter.get("status") == "verified"]
    no_preserved = []
    for note in verified:
        kinds = set()
        for ref in note.frontmatter.get("sources") or []:
            kinds.update(evidence_kinds(str(ref), by_id))
        if "preserved" not in kinds:
            no_preserved.append((note, kinds or {"no-sources"}))
    url_only = [note for note in notes if note.ntype == "source"
                and note.frontmatter.get("url") and not note.frontmatter.get("content_hash")]
    print("check_evidence_coverage: report-only; preserved path is not claim entailment")
    print(f"  verified non-source notes: {len(verified)}")
    print(f"  without any hashed evidence path: {len(no_preserved)}")
    print(f"  live URL sources without content hash: {len(url_only)}")
    for note, kinds in no_preserved[:40]:
        print(f"  {note.path.relative_to(root)} -> {', '.join(sorted(kinds))}")
    if len(no_preserved) > 40:
        print(f"  ... {len(no_preserved) - 40} more")
    return 0


if __name__ == "__main__":
    sys.exit(main())
