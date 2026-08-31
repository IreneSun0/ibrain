---
id: "concept:basis-risk"
type: concept
title: Basis Risk
title_zh: 基差风险/不完美对冲风险
title_en: Basis Risk
aliases:
  - 基差风险
status: seed
importance: tier-1
domains:
  - derivatives
  - institutional-risk
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
  - id: "concept:hedging"
    rel: risk-of
    note: "对冲工具与被对冲风险不完全相同, 抵消不完全"
prerequisites:
  - "concept:hedging"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---

# Basis Risk | 基差风险/不完美对冲风险

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

对冲工具和被对冲风险并非完全相同，导致两者不会一比一抵消。

## Why This Matters | 为什么重要

这是跨venue prediction contract最大的隐形风险之一。

## Concrete Example | 例子

Kalshi和Polymarket同题但时间区间/来源/措辞不同。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Basis Risk。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = hedging; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
