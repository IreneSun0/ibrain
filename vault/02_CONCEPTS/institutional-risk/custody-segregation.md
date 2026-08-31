---
id: "concept:custody-segregation"
type: concept
title: Custody Segregation
title_zh: 客户资产隔离托管
title_en: Custody Segregation
aliases:
  - 客户资产隔离托管
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
  - id: "concept:custody"
    rel: component-of
    note: 客户资产与公司资产的账务与保管隔离
prerequisites:
  - "concept:custody"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---

# Custody Segregation | 客户资产隔离托管

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

客户资产与平台自己的公司资产分开记录和保管。

## Why This Matters | 为什么重要

平台破产时降低客户资产被当作公司财产处理的风险。

## Concrete Example | 例子

segregated accounts/wallet structures。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Custody Segregation。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = custody; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
