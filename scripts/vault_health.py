#!/usr/bin/env python3
"""vault_health.py — one-shot health report combining all checks.

Runs: frontmatter validation, duplicate ids, wikilinks, duplicate entities,
orphans, source freshness, counts by type/status. Writes
90_META/health-reports/vault-health-YYYY-MM-DD.md and VAULT-HEALTH-REPORT.md
(latest pointer copy at vault root). Exit 1 if any HARD check fails
(frontmatter/dup-ids/wikilinks); soft findings don't fail the run.
"""
from __future__ import annotations

import io
import subprocess
import sys
from collections import Counter
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

SCRIPTS = Path(__file__).resolve().parent


def run(script: str, *args: str) -> tuple[int, str]:
    p = subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                       capture_output=True, text=True)
    return p.returncode, (p.stdout + p.stderr).strip()


def main() -> int:
    root = vault_root()
    today = date.today().isoformat()
    hard, soft = {}, {}
    hard["validate_frontmatter"] = run("validate_frontmatter.py")
    hard["detect_duplicate_ids"] = run("detect_duplicate_ids.py")
    hard["check_wikilinks"] = run("check_wikilinks.py")
    hard["check_confidentiality"] = run("check_confidentiality.py")
    soft["detect_duplicate_entities"] = run("detect_duplicate_entities.py", "--report")
    soft["find_orphan_notes"] = run("find_orphan_notes.py")
    soft["check_source_freshness"] = run("check_source_freshness.py")
    soft["check_evidence_coverage"] = run("check_evidence_coverage.py")
    soft["secret_scan"] = run("secret_scan.py")

    notes = [n for n in iter_notes() if n.id]
    by_type = Counter(n.ntype for n in notes)
    by_status = Counter(str(n.frontmatter.get("status")) for n in notes)
    no_src_verified = [n for n in notes if n.ntype != "source"
                       and n.frontmatter.get("status") == "verified"
                       and not (n.frontmatter.get("sources") or [])]
    unhashed_sources = [n for n in notes if n.ntype == "source"
                        and n.frontmatter.get("url") and not n.frontmatter.get("content_hash")]

    hard_fail = any(rc != 0 for rc, _ in hard.values())
    secret_fail = soft["secret_scan"][0] != 0

    out = io.StringIO()
    w = out.write
    w(f"# Vault Health Report | 知识库健康报告\n\n")
    w(f"- 日期: {today}\n- 结构化笔记: {len(notes)}\n")
    w(f"- 硬检查: {'❌ FAIL' if hard_fail else '✅ PASS'} · 秘密扫描: {'❌ FAIL' if secret_fail else '✅ PASS'}\n\n")
    w("## 数量分布\n\n| type | count |\n|---|---|\n")
    for t, c in sorted(by_type.items(), key=lambda x: -x[1]):
        w(f"| {t} | {c} |\n")
    w("\n| status | count |\n|---|---|\n")
    for t, c in sorted(by_status.items(), key=lambda x: -x[1]):
        w(f"| {t} | {c} |\n")
    w("\n## 硬检查 (fail = 必须修)\n\n")
    for name, (rc, txt) in hard.items():
        w(f"### {name} — {'FAIL' if rc else 'PASS'}\n\n```\n{txt[:3000]}\n```\n\n")
    w("## 软检查 (发现 = 排进维护队列)\n\n")
    for name, (rc, txt) in soft.items():
        w(f"### {name}\n\n```\n{txt[:3000]}\n```\n\n")
    if no_src_verified:
        w("## verified 但无来源 (违规)\n\n")
        for n in no_src_verified:
            w(f"- {n.path.relative_to(root)}\n")
    if unhashed_sources:
        w("## URL source 无内容快照 (证据漂移风险)\n\n")
        for n in unhashed_sources:
            w(f"- {n.path.relative_to(root)}\n")
    report = out.getvalue()

    hr = root / "90_META" / "health-reports"
    hr.mkdir(parents=True, exist_ok=True)
    (hr / f"vault-health-{today}.md").write_text(report, encoding="utf-8")
    (root / "VAULT-HEALTH-REPORT.md").write_text(report, encoding="utf-8")
    print(f"vault_health: {'FAIL' if (hard_fail or secret_fail) else 'PASS'} → 90_META/health-reports/vault-health-{today}.md")
    return 1 if (hard_fail or secret_fail) else 0


if __name__ == "__main__":
    sys.exit(main())
