---
id: "concept:funding-rate"
type: concept
title: Funding Rate
title_zh: 资金费率
title_en: Funding Rate
aliases:
  - 资金费率
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
  - id: "concept:perpetual-futures"
    rel: mechanism-of
    note: "多空定期互付, 把 perp 价格拉回现货"
prerequisites:
  - "concept:perpetual-futures"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---

# Funding Rate | 资金费率

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

永续合约多空双方定期互相支付的费用，用来把perp价格拉回现货附近。

## Why This Matters | 为什么重要

防止永续合约长期脱离现货。

## Concrete Example | 例子

perp高于spot时通常多头付空头。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Funding Rate。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = perpetual-futures; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
