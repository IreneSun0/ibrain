---
id: "concept:expected-shortfall"
type: concept
title: Expected Shortfall
title_zh: 预期损失/尾部期望损失
title_en: Expected Shortfall
aliases:
  - 预期损失
status: seed
importance: tier-2
domains:
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
  - id: "concept:value-at-risk"
    rel: contrasts-with
    note: 尾部平均损失 vs 阈值损失概率 — 监管从 VaR 转向 ES 的原因
prerequisites:
  - "concept:value-at-risk"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---

# Expected Shortfall | 预期损失/尾部期望损失

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

在最坏那一小部分情形里，平均会亏多少。比VaR更关注尾部严重程度。

## Why This Matters | 为什么重要

适合描述极端风险和流动性崩塌。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Expected Shortfall。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = value-at-risk; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
