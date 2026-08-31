---
id: "concept:event-var"
type: concept
title: Event VaR
title_zh: 事件风险价值
title_en: Event VaR
aliases:
  - 事件风险价值
status: seed
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-27
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "concept:value-at-risk"
    rel: special-case-of
    note: 按具体事件情景聚合跨 venue/跨工具头寸的 VaR
prerequisites:
  - "concept:value-at-risk"
  - "concept:event-risk"
import_origin: xlsx-learning-map+manual
import_category: 事件市场候选概念
---

# Event VaR | 事件风险价值

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

针对具体事件情景，把预测市场、现货、perp、options、RWA等相关头寸映射后估计组合潜在损失。

## Why This Matters | 为什么重要

把“一个事件”从孤立合约提升到全portfolio视角。

## Concrete Example | 例子

Fed意外加息对BTC、rates、event contracts的联合冲击。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Event VaR。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 事件市场候选概念)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = value-at-risk, event-risk; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
