---
id: "concept:double-spending"
type: concept
title: Double Spending
title_zh: 双重支付
title_en: Double Spending
aliases:
  - 双重支付
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
related:
  - id: "concept:ledger"
    rel: risk-of
    note: 数字资产可复制 — 无共识的数字账本的根本威胁
  - id: "concept:consensus"
    rel: mitigated-by
    note: PoW/PoS 使重写交易历史在经济上昂贵
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# Double Spending | 双重支付

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

同一份数字资产被尝试花两次的问题。

## Why This Matters | 为什么重要

纯数字文件可复制，因此数字货币必须确定唯一有效交易历史。

## Concrete Example | 例子

Alice同时把同一BTC发给Bob和Carol。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Double Spending。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
