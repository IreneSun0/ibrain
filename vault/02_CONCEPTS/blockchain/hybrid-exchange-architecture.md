---
id: "concept:hybrid-exchange-architecture"
type: concept
title: Hybrid Exchange
title_zh: 混合式交易架构
title_en: Hybrid Exchange
aliases:
  - Hybrid Exchange
  - 混合式交易架构
status: seed
importance: tier-2
domains:
  - blockchain
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
  - "source:2026-08-26-polymarket-prices-orderbook"
related:
  - id: "venue:polymarket"
    rel: instantiated-by
    note: 链下 CLOB 撮合 + Polygon 链上 USDC 全额抵押结算
prerequisites:
  - "concept:on-chain"
  - "concept:off-chain"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# Hybrid Exchange | 混合式交易架构

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

把高频/低延迟部分放链下，把签名、托管或最终结算放链上。

## Why This Matters | 为什么重要

兼顾传统交易速度和链上可验证/非托管结算。

## Concrete Example | 例子

Polymarket off-chain matching + on-chain settlement。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Hybrid Exchange。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-polymarket-prices-orderbook]] — <https://docs.polymarket.com/concepts/prices-orderbook>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = on-chain, off-chain; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
