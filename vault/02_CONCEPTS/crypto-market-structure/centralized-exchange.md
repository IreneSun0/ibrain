---
id: "concept:centralized-exchange"
type: concept
title: CEX
title_zh: 中心化加密交易所
title_en: CEX
aliases:
  - CEX
  - Centralized Exchange
  - 中心化加密交易所
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
  - id: "concept:exchange"
    rel: special-case-of
  - id: "concept:decentralized-exchange"
    rel: contrasts-with
    note: 内部账本+托管撮合 vs 链上合约+自托管结算 — 谁托管、谁能冻结完全不同
  - id: "venue:binance"
    rel: instantiated-by
  - id: "venue:okx"
    rel: instantiated-by
prerequisites:
  - "concept:exchange"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---

# CEX | 中心化加密交易所

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

由公司运营、通常托管用户资产并用内部账本/撮合引擎交易的crypto exchange。

## Why This Matters | 为什么重要

速度高、产品丰富、法币/客服/机构服务强，但存在托管和平台风险。

## Concrete Example | 例子

Binance、OKX、Bybit、Bitget、HTX。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 CEX。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = exchange; typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
