---
id: "concept:forward-contract"
type: concept
title: Forward
title_zh: 远期合约
title_en: Forward
aliases:
  - Forward
  - 远期合约
status: seed
importance: tier-2
domains:
  - derivatives
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
  - id: "concept:derivative"
    rel: special-case-of
  - id: "concept:counterparty-risk"
    rel: see-also
    note: "定制双边 OTC 合同, 无 CCP 介入, 违约风险双边裸露"
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---

# Forward | 远期合约

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

双方今天约定未来某天按约定价格交易某资产，通常是定制的OTC双边合同。

## Why This Matters | 为什么重要

方便定制对冲，但存在较强counterparty risk。

## Concrete Example | 例子

公司锁定3个月后的美元汇率。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Forward。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = derivative; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
