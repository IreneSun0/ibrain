---
id: "concept:automated-market-maker"
type: concept
title: AMM
title_zh: 自动做市商
title_en: AMM
aliases:
  - AMM
  - Automated Market Maker
  - 自动做市商
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
    note: 公式+资金池定价 vs 订单撮合定价; 无需传统 MM 即可冷启动
  - id: "concept:price-discovery"
    rel: mechanism-of
    note: 与 CLOB 并列的另一条定价机制路线
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---

# AMM | 自动做市商

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

用智能合约和公式、资金池自动给出价格，而不是传统订单簿逐单撮合。

## Why This Matters | 为什么重要

能在没有传统MM的情况下启动市场，但有资本效率和无常损失等问题。

## Concrete Example | 例子

Uniswap恒定乘积AMM。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 AMM。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = smart-contract; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
