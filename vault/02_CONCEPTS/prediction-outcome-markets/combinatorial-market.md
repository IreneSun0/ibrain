---
id: "concept:combinatorial-market"
type: concept
title: Combinatorial Market
title_zh: 组合市场
title_en: Combinatorial Market
aliases:
  - 组合市场
  - Conditional Market
status: seed
importance: tier-2
domains:
  - prediction-outcome-markets
tags:
  - concept
created: 2026-08-26
updated: 2026-08-27
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related:
  - id: "concept:outcome-market"
    rel: special-case-of
    note: 直接为联合/条件概率定价
prerequisites:
  - "concept:multi-outcome-market"
  - "concept:implied-probability"
---
# Combinatorial Market | 组合市场

## Executive Definition

对多个事件的**联合/条件**结果定价的市场: "A 且 B"、"若 A 则 B" — 价格直接给出联合概率或条件概率, 而不只是各自的边际概率。

## Chinese Explanation | 中文解释

独立市场只给边际: P(A)、P(B)。但决策常需要条件量: "若 X 当选, 关税会加吗?" 组合市场直接交易 P(B|A) (常见实现: "A 且 B" 与 "A 且非B" 两个市场, 条件概率 = 前者/(两者之和))。

难点是**流动性组合爆炸**: N 个事件的联合空间是 2^N, 每个角落都需要做市资本, 绝大多数组合盘口为空。学术上 (Hanson 的 LMSR 系) 用自动做市商在整个联合空间上维持一致定价, 实践中真实交易量集中在极少数政治条件对。注意: 这与赌场 parlay (串关) 形似而神异 — parlay 是给定赔率的投注票, 不是可持续双向交易的市场; 务必注意: parlay 结构不适合用作仓位测算的依据。


## Active-Recall Questions

- Q: 怎么从两个"且"市场读出条件概率?
  A: P(B|A) = P(A∧B) / (P(A∧B) + P(A∧¬B))。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = multi-outcome-market, implied-probability; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
