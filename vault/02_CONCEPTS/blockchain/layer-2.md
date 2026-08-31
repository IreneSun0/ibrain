---
id: "concept:layer-2"
type: concept
title: L2
title_zh: 第二层扩容网络
title_en: L2
aliases:
  - L2
  - Layer 2
  - 第二层扩容网络
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
  - id: "protocol:x-layer"
    rel: instantiated-by
    note: OKX 系 Ethereum L2 (OKB 为唯一 gas)
  - id: "protocol:mantle"
    rel: instantiated-by
    note: Bybit 生态系 Ethereum L2
prerequisites:
  - "concept:layer-1"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# L2 | 第二层扩容网络

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

在基础链之上执行/聚合大量交易，再把结果或证明提交到底层链。

## Why This Matters | 为什么重要

降低成本、提高吞吐量，但增加桥接和系统假设。

## Concrete Example | 例子

Ethereum rollups。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 L2。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = layer-1; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
