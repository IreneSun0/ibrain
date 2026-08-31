#!/usr/bin/env python3
"""build_query_eval.py — check the retrieval benchmark against the vault.

Reads 90_META/coverage/query-eval-benchmark.md, which lists benchmark questions
with machine-readable expectation lines:
    expects: note-stem-1, note-stem-2, ...
For each question reports which expected notes exist / are missing (existence +
linkage smoke test — answer QUALITY is judged by a human/agent, not here).
Writes 90_META/coverage/query-eval-latest.md. Exit 0 always (informational).
"""
from __future__ import annotations

import re
import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

Q_RE = re.compile(r"^###\s+Q(\d+)[.:]?\s*(.+)$")
EXPECT_RE = re.compile(r"^\s*expects:\s*(.+)$")


def main() -> int:
    root = vault_root()
    bench = root / "90_META" / "coverage" / "query-eval-benchmark.md"
    if not bench.exists():
        print("build_query_eval: benchmark file missing — create 90_META/coverage/query-eval-benchmark.md")
        return 0
    stems = {n.path.stem for n in iter_notes()}
    lines = bench.read_text(encoding="utf-8").split("\n")
    results, cur_q = [], None
    for ln in lines:
        qm = Q_RE.match(ln)
        if qm:
            cur_q = (qm.group(1), qm.group(2).strip())
            continue
        em = EXPECT_RE.match(ln)
        if em and cur_q:
            expected = [s.strip() for s in em.group(1).split(",") if s.strip()]
            missing = [e for e in expected if e not in stems]
            results.append((cur_q[0], cur_q[1], expected, missing))
    today = date.today().isoformat()
    out = [f"# Query Eval — 存在性检查结果", "", f"> 生成: {today} · `build_query_eval.py`",
           "> 只检查 expected notes 是否存在; 答案质量由人工/agent 评。", ""]
    ok = 0
    for qid, qtext, expected, missing in results:
        status = "✅" if not missing else "❌"
        if not missing:
            ok += 1
        out.append(f"- {status} **Q{qid}** {qtext}")
        if missing:
            out.append(f"  - 缺: {', '.join(f'`{m}`' for m in missing)}")
    out.insert(3, f"**{ok}/{len(results)}** 问题的 expected-note 文件集合存在。该数字不代表答案正确、完整、最新或有证据。\n")
    (root / "90_META" / "coverage" / "query-eval-latest.md").write_text("\n".join(out) + "\n", encoding="utf-8")
    print(f"build_query_eval: {ok}/{len(results)} expected-note sets present (presence only) → 90_META/coverage/query-eval-latest.md")
    return 0


if __name__ == "__main__":
    sys.exit(main())
