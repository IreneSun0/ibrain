---
id: "concept:over-the-counter"
type: concept
title: OTC
title_zh: 场外交易
title_en: OTC
aliases:
  - Institutional OTC
  - OTC
  - 场外交易
status: seed
importance: tier-2
domains:
  - crypto-market-structure
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
  - id: "concept:order-book"
    rel: contrasts-with
    note: 双边协商避免公开盘口冲击 vs 集中透明但暴露交易意图
  - id: "mmf:b2c2"
    rel: instantiated-by
    note: 机构 OTC 流动性商
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---

# OTC | 场外交易

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

不通过公开订单簿、由双方或dealer直接协商的大额/定制交易。

## Why This Matters | 为什么重要

减少公开市场price impact，并支持大额、复杂、信用型交易。

## Concrete Example | 例子

机构向Wintermute询价大额spot/options。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 OTC。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = order-book; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
