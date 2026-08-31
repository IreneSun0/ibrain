#!/usr/bin/env python3
"""compute_score.py — T2049 bootcamp quantified scores, fully reproducible.

Model (documented in 10_LEARNING/plan/master-plan.md §1), speedrun edition:
  industry = mainline_clear_rate*0.50 + quiz*0.25 + mock*0.25
  pm       = pm_mainline_clear_rate*0.40 + pm_quiz*0.30 + pm_mock*0.30

  mainline clear rate: cleared / total over the 81 main-quest concepts
    (mainline.yaml; cleared = status reviewed/verified, draft counts 0.4).
    Side-quest concepts do not count — skipping them is the strategy, not a gap.
  pm mainline = mainline ∩ (stage-7 domain ∪ schedule pm_core_concepts)
  quiz: mean of the most recent 5 `kind: quiz` records (pm: scope=pm only)
  mock: weighted mean of most recent 3 `kind: mock` (50/30/20; pm: scope=pm)

Inputs: vault concept frontmatter + 10_LEARNING/plan/{schedule,assessments,mainline}.yaml
Output: 90_META/dashboards/scoreboard.md; --json prints machine-readable dict.
"""
from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

import yaml

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

MASTERY = {"reviewed": 1.0, "verified": 1.0, "draft": 0.4}
PM_STAGE_DOMAIN = "prediction-outcome-markets"


def load_yaml(p: Path):
    return yaml.safe_load(p.read_text(encoding="utf-8")) if p.exists() else {}


def concept_score(concepts) -> tuple[float, int, int]:
    """Mainline clear rate: every quest counts 1 (draft = 0.4 partial credit)."""
    total = len(concepts)
    sw = 0.0
    done = 0
    for n in concepts:
        m = MASTERY.get(str(n.frontmatter.get("status")), 0.0)
        sw += m
        if m >= 1.0:
            done += 1
    return (100.0 * sw / total if total else 0.0), done, total


def quiz_score(records, scope=None) -> float | None:
    q = [r for r in records if r.get("kind") == "quiz" and (scope is None or r.get("scope") == scope)]
    q.sort(key=lambda r: str(r.get("date")))
    last = q[-5:]
    return sum(float(r["score"]) for r in last) / len(last) if last else None


def mock_score(records, scope=None) -> float | None:
    m = [r for r in records if r.get("kind") == "mock" and (scope is None or r.get("scope") == scope)]
    m.sort(key=lambda r: str(r.get("date")))
    last = list(reversed(m[-3:]))  # newest first
    if not last:
        return None
    weights = [0.5, 0.3, 0.2][: len(last)]
    total_w = sum(weights)
    return sum(float(r["score"]) * w for r, w in zip(last, weights)) / total_w


def build() -> dict:
    root = vault_root()
    plan_dir = root / "10_LEARNING" / "plan"
    schedule = load_yaml(plan_dir / "schedule.yaml")
    assessments = load_yaml(plan_dir / "assessments.yaml") or {}
    records = assessments.get("records") or []

    mainline = load_yaml(plan_dir / "mainline.yaml")
    main_ids = [c for ch in (mainline.get("chapters") or []) for c in (ch.get("concepts") or [])]
    main_set = set(main_ids)

    all_concepts = [n for n in iter_notes() if n.ntype == "concept"]
    concepts = [n for n in all_concepts if n.id in main_set] if main_set else all_concepts
    pm_ids = set(schedule.get("pm_core_concepts") or [])
    pm_concepts = [n for n in concepts
                   if n.id in pm_ids or PM_STAGE_DOMAIN in [str(d) for d in (n.frontmatter.get("domains") or [])]]

    c_all, done_all, n_all = concept_score(concepts)
    c_pm, done_pm, n_pm = concept_score(pm_concepts)
    q_all, q_pm = quiz_score(records), quiz_score(records, "pm")
    m_all, m_pm = mock_score(records), mock_score(records, "pm")

    industry = 0.50 * c_all + 0.25 * (q_all or 0.0) + 0.25 * (m_all or 0.0)
    pm = 0.40 * c_pm + 0.30 * (q_pm or 0.0) + 0.30 * (m_pm or 0.0)

    today = date.today().isoformat()
    target = None
    for t in schedule.get("score_targets") or []:
        if str(t["date"]) >= today:
            target = t
            break

    # which training week is today in
    week = None
    for w in schedule.get("weeks") or []:
        if str(w["start"]) <= today <= str(w["end"]):
            week = w
            break

    return {
        "date": today,
        "deadline": str(schedule.get("deadline") or ""),
        "industry": round(industry, 1),
        "pm": round(pm, 1),
        "parts": {
            "conceptAll": round(c_all, 1), "conceptPm": round(c_pm, 1),
            "quizAll": None if q_all is None else round(q_all, 1),
            "quizPm": None if q_pm is None else round(q_pm, 1),
            "mockAll": None if m_all is None else round(m_all, 1),
            "mockPm": None if m_pm is None else round(m_pm, 1),
        },
        "concepts": {"all": [done_all, n_all], "pm": [done_pm, n_pm]},
        "nextTarget": target,
        "week": None if week is None else {"n": week["n"], "chapters": week.get("chapters") or [],
                                           "theme": week.get("theme") or "", "end": str(week["end"])},
        "records": len(records),
    }


def render_md(s: dict) -> str:
    def fmt(v):
        return "—  (无记录)" if v is None else f"{v}"
    t = s["nextTarget"]
    target_line = (f"下一检查点 **{t['date']}**: 行业 {t['industry']} / PM {t['pm']}"
                   if t else "已过全部检查点")
    gap = ""
    if t:
        gi = s["industry"] - float(t["industry"])
        gp = s["pm"] - float(t["pm"])
        gap = f" (当前差距: 行业 {gi:+.1f} / PM {gp:+.1f})"
    week_line = "训练期外"
    if s["week"]:
        chs = s['week']['chapters']
        week_line = f"W{s['week']['n']} ({'第 ' + '+'.join(map(str, chs)) + ' 章' if chs else '冲刺'}) — {s['week']['theme']}"
    return f"""# T2049 训练营记分板

> 生成: {s['date']} · `make score` 重算 · 模型定义: 10_LEARNING/plan/master-plan.md §1 · 数据: assessments.yaml ({s['records']} 条记录)

## 当前分数

| | 分数 | 主线通关 | 测验 | 模拟实战 |
|---|---|---|---|---|
| **行业总分** | **{s['industry']}** / 60 | {s['parts']['conceptAll']} (权重 50%) | {fmt(s['parts']['quizAll'])} (25%) | {fmt(s['parts']['mockAll'])} (25%) |
| **PM 专项** | **{s['pm']}** / 75 | {s['parts']['conceptPm']} (40%) | {fmt(s['parts']['quizPm'])} (30%) | {fmt(s['parts']['mockPm'])} (30%) |

主线进度: {s['concepts']['all'][0]}/{s['concepts']['all'][1]} 关 · 其中 PM 关卡 {s['concepts']['pm'][0]}/{s['concepts']['pm'][1]}。支线不计分 — 跳过它们是策略, 不是欠账。

## 轨迹

当前位置: {week_line}
{target_line}{gap}
Deadline: **{s['deadline']}** (行业 ≥60 / PM ≥75) → TOKEN2049 10/07–08。
"""


def main(argv=None) -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--json", action="store_true", help="print machine-readable scores")
    ap.add_argument("--out", default=None, help="scoreboard md path override")
    args = ap.parse_args(argv)

    s = build()
    if args.json:
        print(json.dumps(s, ensure_ascii=False, default=str))
        return 0
    out = Path(args.out) if args.out else vault_root() / "90_META" / "dashboards" / "scoreboard.md"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(render_md(s), encoding="utf-8")
    print(f"compute_score: industry {s['industry']} / pm {s['pm']} "
          f"(concepts {s['concepts']['all'][0]}/{s['concepts']['all'][1]}) → {out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
