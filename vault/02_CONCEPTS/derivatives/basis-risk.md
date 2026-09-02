---
id: "concept:basis-risk"
type: concept
title: Basis Risk
title_zh: 基差风险/不完美对冲风险
title_en: Basis Risk
aliases:
  - 基差风险
status: reviewed
importance: tier-1
domains:
  - derivatives
  - institutional-risk
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "concept:hedging"
    rel: risk-of
    note: "对冲工具与被对冲风险不完全相同, 抵消不完全"
prerequisites:
  - "concept:hedging"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Basis Risk | 基差风险/不完美对冲风险

## Executive Definition / Chinese Explanation | 定义与解释

**Basis Risk | 基差风险** = 你的对冲工具和你要对冲的风险**不完全一致**，剩下的那部分差异带来的风险。

对冲从来不是完美的。基差就是"完美"和"实际"之间的缝，而**你亏钱的地方永远在缝里。**

## Why This Matters | 为什么重要

在价格市场，基差是**统计问题**：两个相关资产的价差有历史分布，可以建模、可以估计。

在事件市场，基差是**语义问题**：两张合约的条款可能在某些情形下给出相反结果。**统计解决不了它 —— 必须逐条读条款。**

这个区别决定了工具完全不同：价格市场用相关性矩阵，事件市场需要**逐条的语义等价判定**（见 [[contract-equivalence]]）。

## How It Works | 机制怎么运转

事件市场的基差有三个来源，且比价格市场更凶：

1. **标的不同** —— 两张合约的语义有缝（"卸任"的定义、时区、边界条件）。
2. **结算机制不同** —— 一边在 CFTC 框架内由委员会裁定，一边由代币投票裁定。**同样的现实，两套判定程序可能给出不同答案。**
3. **时间不同** —— 判定日差一天，就可能一边 YES 一边 NO。

**第 2 条是价格市场完全没有的**：CME 和 ICE 的同一个标的期货，结算价来自同一个可观测市场。事件市场没有这个共同基准。

## Concrete Example | 具体例子

**教科书级的伪对冲**：

你在 [[kalshi]] 持有"X 当选" YES，去 [[polymarket]] 买"X 当选" NO 来对冲。你以为自己中性了。

选举夜出了意外情形（计票争议、法律挑战、当选人在就职前变故）：
- Kalshi 按其 Source Agencies 与判定日条款裁 **YES**。
- Polymarket 按 UMA 投票裁 **NO**。

**你的"完美对冲"在两边同时亏损。**

这不是假想的极端情况 —— 它正是 [[contract-semantics]] 的语义缝隙在两个不同裁决体系下的必然产物。**两张合约的标题一样，DNA 不一样。**

## Common Misconceptions | 常见误解

- **误解一："同题合约就能对冲。"** 标题相同不代表条款相同。**必须五维对齐**（主体 / 谓词阈值 / 判定时点 / 数据源 / 边界条件）。
- **误解二："基差风险很小可以忽略。"** 它平时确实小 —— **但它恰恰在极端情形下才显现，而那正是你需要对冲生效的时刻。**
- **误解三："基差风险可以用历史相关性估计。"** 在事件市场不行。**语义分叉不是统计现象，它要么发生要么不发生。**

## In Practice | 实战里怎么用

建立任何跨场所对冲前，跑五行对照表（见 [[contract-equivalence]]）：

```
              A 平台      B 平台      一致?
主体          ______      ______      □
谓词/阈值     ______      ______      □
判定时点      ______      ______      □
数据源        ______      ______      □
边界条件      ______      ______      □
```

- **五项全 ✓** → 可视作对冲。
- **有任何一项 ✗** → **这不是对冲，是两个独立头寸。** 分别计量，不要在风险系统里做抵扣。

**最危险的状态不是"我知道有基差"，是"我以为自己中性了"。** 后者会让你在错误的地方加大规模。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 价格市场与事件市场的基差风险在性质上有什么根本不同？
  A: 价格市场的基差是统计问题（有历史分布可建模），事件市场的基差是语义问题（条款可能给出相反结果），必须逐条读条款。
- Q: 事件市场基差的三个来源是什么？哪一个是价格市场没有的？
  A: 标的语义不同、结算机制不同、判定时点不同。结算机制不同是价格市场没有的 —— 价格衍生品共享可观测的结算基准。
- Q: 跨场所对冲前的五维对照检查是哪五项？
  A: 主体、谓词与阈值、判定时点、裁决数据源、边界条件处理。任何一项不一致就不是对冲，而是两个独立头寸。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
