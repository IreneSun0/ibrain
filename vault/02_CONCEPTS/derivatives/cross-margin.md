---
id: "concept:cross-margin"
type: concept
title: Cross Margin
title_zh: 跨品种/跨头寸保证金
title_en: Cross Margin
aliases:
  - 跨品种
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
  - id: "concept:margin"
    rel: special-case-of
    note: 允许相关头寸风险互抵的保证金模式
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---

# Cross Margin | 跨品种/跨头寸保证金

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

允许相关头寸的风险相互抵消，从而减少总保证金。

## Why This Matters | 为什么重要

显著提高资本效率，但要求正确识别相关性和极端情况下的失效。

## Concrete Example | 例子

BTC spot + short perp；未来Fed event + rate product。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Cross Margin。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = margin; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
