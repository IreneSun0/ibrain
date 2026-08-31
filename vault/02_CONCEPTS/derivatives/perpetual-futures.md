---
id: "concept:perpetual-futures"
type: concept
title: Perpetual Futures / Perp
title_zh: 永续合约
title_en: Perpetual Futures / Perp
aliases:
  - Perpetual Futures / Perp
  - 永续合约
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
  - id: "concept:futures-contract"
    rel: special-case-of
    note: "去掉到期日, 用资金费率锚定现货"
prerequisites:
  - "concept:futures-contract"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---

# Perpetual Futures / Perp | 永续合约

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

没有固定到期日、通过资金费率等机制让合约价格贴近现货的杠杆衍生品。

## Why This Matters | 为什么重要

让用户长期做多/做空而无需滚动到期合约。

## Concrete Example | 例子

BTC-PERP on Binance/OKX/Hyperliquid。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Perpetual Futures / Perp。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = futures-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
