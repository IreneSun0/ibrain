---
id: "concept:request-for-quote"
type: concept
title: RFQ
title_zh: 询价交易
title_en: RFQ
aliases:
  - RFQ
  - Request for Quote
  - 询价交易
status: seed
importance: tier-2
domains:
  - market-microstructure
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
  - id: "concept:central-limit-order-book"
    rel: contrasts-with
    note: 定向询价保护大单意图 vs 公开盘口透明但暴露
prerequisites:
  - "concept:market-maker"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---

# RFQ | 询价交易

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

Request for Quote。大客户先询问若干做市商“这笔大单你给什么价格”，再选择成交。

## Why This Matters | 为什么重要

机构大单不一定适合直接扫公开订单簿。

## Concrete Example | 例子

基金向3家dealer询价买$5m事件风险。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 RFQ。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = market-maker; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
