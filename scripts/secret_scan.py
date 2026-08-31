#!/usr/bin/env python3
"""secret_scan.py — block credentials from entering either repo.

Scans working tree of BOTH repos (vault + ops) for secret-shaped content.
Run manually or from the pre-commit instructions in OPERATIONS.md. Exit 1 on hit.
"""
from __future__ import annotations

import os
import re
import sys
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import OPS_ROOT, vault_root

PATTERNS = [
    ("private-key-block", re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH |PGP )?PRIVATE KEY-----")),
    ("aws-access-key", re.compile(r"\bAKIA[0-9A-Z]{16}\b")),
    ("openai-key", re.compile(r"\bsk-[A-Za-z0-9_-]{20,}\b")),
    ("anthropic-key", re.compile(r"\bsk-ant-[A-Za-z0-9_-]{20,}\b")),
    ("github-token", re.compile(r"\bgh[pousr]_[A-Za-z0-9]{36,}\b")),
    ("telegram-bot-token", re.compile(r"\b\d{8,10}:AA[A-Za-z0-9_-]{33}\b")),
    ("slack-token", re.compile(r"\bxox[baprs]-[A-Za-z0-9-]{10,}\b")),
    ("google-api-key", re.compile(r"\bAIza[0-9A-Za-z_-]{35}\b")),
    ("generic-assignment", re.compile(
        r"(?i)\b(api[_-]?key|secret[_-]?key|access[_-]?token|password|passwd)\b\s*[:=]\s*"
        r"(?:['\"][^'\"\s]{12,}['\"]|[^\s#,'\";]{12,})")),
    ("eth-private-key", re.compile(r"\b0x[0-9a-fA-F]{64}\b")),
    ("jwt", re.compile(r"\beyJ[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\.[A-Za-z0-9_-]{10,}\b")),
]
# BIP-39 mnemonic heuristic: 12+ consecutive lowercase words from a sample set
BIP39_SAMPLE = {
    "abandon", "ability", "able", "about", "absent", "zoo", "wrap", "wolf",
    "toward", "seed", "mnemonic", "phrase",
}
WORDS_RE = re.compile(r"^[a-z]+(?: [a-z]+){11,23}$")

SKIP_DIRS = {".git", ".venv", "venv", "__pycache__", ".obsidian", "node_modules", ".pytest_cache"}
SKIP_SUFFIX = {".png", ".jpg", ".jpeg", ".gif"}
# Files that legitimately DESCRIBE secret patterns (this scanner, policies)
ALLOWLIST_NAMES = {"secret_scan.py", "test_secret_scan.py"}


def scan_text(text: str) -> list[str]:
    hits = []
    for name, rx in PATTERNS:
        if rx.search(text):
            hits.append(name)
    for line in text.splitlines():
        s = line.strip().lower()
        if WORDS_RE.match(s) and len(BIP39_SAMPLE & set(s.split())) >= 2:
            hits.append("possible-mnemonic")
            break
    return hits


def scan_file(p: Path) -> list[str]:
    hits = []
    try:
        if p.suffix.lower() in {".zip", ".xlsx"}:
            with zipfile.ZipFile(p) as archive:
                for member in archive.infolist():
                    if member.is_dir() or member.file_size > 10_000_000:
                        continue
                    member_hits = scan_text(archive.read(member).decode("utf-8", errors="ignore"))
                    hits.extend(f"{hit}@{member.filename}" for hit in member_hits)
            return hits
        data = p.read_bytes()
        return scan_text(data.decode("utf-8", errors="ignore"))
    except Exception:
        return hits


def main() -> int:
    seed_root = Path(os.environ.get("IBRAIN_SEED_PATH", str(OPS_ROOT.parent / "_seed")))
    roots = [vault_root(), OPS_ROOT]
    if seed_root.exists():
        roots.append(seed_root)
    bad = []
    for root in roots:
        for p in sorted(root.rglob("*")):
            if not p.is_file() or p.suffix in SKIP_SUFFIX:
                continue
            if any(part in SKIP_DIRS for part in p.parts):
                continue
            if p.name in ALLOWLIST_NAMES:
                continue
            hits = scan_file(p)
            if hits:
                bad.append((p, hits))
    if bad:
        print(f"secret_scan: {len(bad)} file(s) with secret-shaped content — DO NOT COMMIT")
        for p, hits in bad:
            print(f"  {p}: {', '.join(sorted(set(hits)))}")
        return 1
    print("secret_scan: OK (no secret-shaped content)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
