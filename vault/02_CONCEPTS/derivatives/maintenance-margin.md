---
id: "concept:maintenance-margin"
type: concept
title: Maintenance Margin
title_zh: 维持保证金
title_en: Maintenance Margin
aliases:
  - 维持保证金
status: seed
importance: tier-2
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
    rel: component-of
    note: 持仓底线
  - id: "concept:initial-margin"
    rel: contrasts-with
    note: 开仓门槛 vs 持仓底线 — 跌破后者触发补仓或强平
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---

# Maintenance Margin | 维持保证金

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

持仓期间必须维持的最低保证金水平。

## Why This Matters | 为什么重要

低于它通常触发补保证金或强平。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Maintenance Margin。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = margin; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
