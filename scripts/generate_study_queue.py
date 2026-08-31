#!/usr/bin/env python3
"""generate_study_queue.py — adaptive study queue + one study-session sheet.

Deterministic selection (no LLM):
  - overdue reviews: review_after < today, ordered by importance then date
  - weak concepts: confidence in (low, unknown) or status=stub
  - never-reviewed tier-1 concepts (status=seed)
Session sheet composition (from curriculum stage inferred as the lowest stage
with unfinished tier-1 concepts):
  3 prerequisite recalls + 3 new concepts + 2 relationship questions +
  1 case + 1 applied exercise + 1 expert question.
Writes 10_LEARNING/study-sessions/next-session.md and 90_META/dashboards/study-queue.md.
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from brainlib import iter_notes, vault_root

STAGE_DOMAINS = [
    ("1 Financial Markets", "financial-markets"),
    ("2 Exchanges", "exchanges"),
    ("3 Market Microstructure", "market-microstructure"),
    ("4 Derivatives", "derivatives"),
    ("5 Blockchain", "blockchain"),
    ("6 Crypto Market Structure", "crypto-market-structure"),
    ("7 Prediction & Outcome Markets", "prediction-outcome-markets"),
    ("8 Institutional Risk", "institutional-risk"),
]


def select_prereqs(concepts, stage_dom, stage_new):
    """Choose recall notes without duplicating the session's new concepts."""
    domains = [domain for _, domain in STAGE_DOMAINS]
    prior = set(domains[:max(0, domains.index(stage_dom))])
    pool = [n for n in concepts if set(str(d) for d in (n.frontmatter.get("domains") or [])) & prior]
    if not pool:
        pool = [n for n in concepts
                if stage_dom in set(str(d) for d in (n.frontmatter.get("domains") or []))
                and n not in stage_new
                and n.frontmatter.get("status") in ("reviewed", "verified")]
    tiers = {"tier-1": 0, "tier-2": 1, "tier-3": 2}
    pool.sort(key=lambda n: (tiers.get(str(n.frontmatter.get("importance")), 3), n.path.stem))
    return pool[:3]


def main() -> int:
    root = vault_root()
    today = date.today()
    concepts = [n for n in iter_notes() if n.ntype == "concept"]
    tiers = {"tier-1": 0, "tier-2": 1, "tier-3": 2}

    def dom_of(n):
        return set(str(d) for d in (n.frontmatter.get("domains") or []))

    overdue = [n for n in concepts if str(n.frontmatter.get("review_after") or "9999") < str(today)]
    weak = [n for n in concepts if str(n.frontmatter.get("confidence")) in ("low", "unknown")
            or n.frontmatter.get("status") == "stub"]
    fresh_t1 = [n for n in concepts if n.frontmatter.get("importance") == "tier-1"
                and n.frontmatter.get("status") == "seed"]
    fresh_t1.sort(key=lambda n: n.path.stem)

    # current stage = first stage that still has seed tier-1 concepts
    stage_name, stage_dom = STAGE_DOMAINS[0]
    for name, dom in STAGE_DOMAINS:
        if any(dom in dom_of(n) for n in fresh_t1):
            stage_name, stage_dom = name, dom
            break

    stage_new = [n for n in fresh_t1 if stage_dom in dom_of(n)][:3]
    prereqs = select_prereqs(concepts, stage_dom, stage_new)

    def L(n):
        zh = n.frontmatter.get("title_zh") or ""
        return f"[[{n.path.stem}|{n.frontmatter.get('title') or n.path.stem}]] {zh}"

    ses = [
        "# 下一次学习 session | Study Session",
        "",
        f"> 生成: {today} · `generate_study_queue.py` · 当前推断阶段: **{stage_name}**",
        "> 标准配方: 最多 3 个前置回忆 + 3 新概念 + 2 关系题 + 1 真实案例 + 1 实战应用 + 1 专家问题。",
        "",
        "## 1) 前置回忆 (不看笔记, 先答再对)",
        *(f"- {L(n)} — 用两三句话讲清: 它是什么、钱在哪里、谁担风险。" for n in prereqs),
        *(["- 首个阶段暂无已复核前置概念; 先用自己的话写下对本阶段的基线理解。"] if not prereqs else []),
        "",
        "## 2) 新概念 (读页面, 然后合上做主动回忆)",
        *(f"- {L(n)} — 读完后回答页内 Active-Recall Questions。" for n in stage_new),
        "",
        "## 3) 关系题",
        "- 上面两个新概念之间是什么关系? 谁依赖谁? 钱怎么从一个流到另一个?",
        "- 挑一个新概念, 说出它在 [[ecosystem-roles-map|生态游戏版图]] 里属于哪个角色的日常。",
        "",
        "## 4) 真实市场案例",
        "- 在 05_CASES/ 里挑一个 (或回忆最近一条行业新闻), 用今天的新概念解释它的机制。",
        "",
        "## 5) 实战应用",
        "- 今天的概念在真实交易/尽调场景里怎么用? 写三句话留在本次 study-session 笔记; 不写入 09_ORIGINALS/。",
        "",
        "## 6) 专家问题",
        "- 从 [[institutional-conversation-cheatsheet|机构对话速查]] 挑一个对象, 用今天的概念设计一个能问出信息增量的问题。",
        "",
        "## Feynman 提示",
        "- 不用术语本身解释它 / 钱坐在哪里 / 谁最终亏 / 结算如何完成 / 它为什么存在 / 什么会弄坏它 / 在真实交易或尽调里怎么用。",
    ]
    sp = root / "10_LEARNING" / "study-sessions" / "next-session.md"
    sp.parent.mkdir(parents=True, exist_ok=True)
    sp.write_text("\n".join(ses) + "\n", encoding="utf-8")

    q = [
        "# Study Queue | 学习队列",
        "",
        f"> 生成: {today} · `generate_study_queue.py` · 手改会被覆盖",
        "",
        f"当前阶段 (推断): **{stage_name}** — 该阶段还有 {len([n for n in fresh_t1 if stage_dom in dom_of(n)])} 个 tier-1 概念未复核。",
        "",
        f"## 逾期复核 — {len(overdue)}",
        *(f"- {L(n)}" for n in sorted(overdue, key=lambda n: str(n.frontmatter.get('review_after')))[:20]),
        "",
        f"## 薄弱概念 (confidence low/unknown 或 stub) — {len(weak)}",
        *(f"- {L(n)}" for n in sorted(weak, key=lambda n: n.path.stem)[:20]),
        "",
        f"## 未消化的 tier-1 (status: seed) — {len(fresh_t1)}",
        *(f"- {L(n)}" for n in fresh_t1[:30]),
        "",
        "> 消化一个概念 = 读页 + 答对 Active-Recall + 把 status 升为 reviewed。",
    ]
    qp = root / "90_META" / "dashboards" / "study-queue.md"
    qp.write_text("\n".join(q) + "\n", encoding="utf-8")
    print(f"generate_study_queue: stage={stage_name} overdue={len(overdue)} weak={len(weak)} fresh-t1={len(fresh_t1)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
