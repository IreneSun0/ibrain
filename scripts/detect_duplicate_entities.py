#!/usr/bin/env python3
"""Report distinct ids that share a normalized title or alias.

Never edits files. Exits 1 on matches, or 0 in --report mode.
"""
from __future__ import annotations

import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset", "concept"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKC", str(s)).lower().strip()
    return "".join(ch for ch in s if ch.isalnum())


def main(argv: list[str]) -> int:
    report_mode = "--report" in argv
    claims: dict[str, set[str]] = defaultdict(set)
    root = vault_root()
    for n in iter_notes():
        if n.ntype not in ENTITY_TYPES or not n.id:
            continue
        names = [n.frontmatter.get("title"), n.frontmatter.get("title_zh"),
                 n.frontmatter.get("title_en")] + list(n.frontmatter.get("aliases") or [])
        for name in names:
            if name and norm(name):
                claims[norm(name)].add(n.id)
    suspects = {k: v for k, v in claims.items() if len(v) > 1}
    if suspects:
        print(f"detect_duplicate_entities: {len(suspects)} shared name(s) across distinct ids")
        for k, ids in sorted(suspects.items()):
            print(f"  `{k}` claimed by: {', '.join(sorted(ids))}")
        return 0 if report_mode else 1
    print("detect_duplicate_entities: OK (no shared names across entity ids)")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
