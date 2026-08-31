---
id: "concept:option"
type: concept
title: Option
title_zh: 期权
title_en: Option
aliases:
  - 期权
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
  - id: "concept:futures-contract"
    rel: contrasts-with
    note: 权利而非义务 — 权利金换非对称收益 vs 双向义务+保证金
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---

# Option | 期权

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

买方支付权利金，获得在未来按条件买/卖或获得特定支付的权利，而不是义务。

## Why This Matters | 为什么重要

提供非对称收益：损失可限定、上涨或下跌暴露可定制。

## Concrete Example | 例子

BTC Call/Put、数字期权。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Option。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = derivative; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
