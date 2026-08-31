---
id: "concept:delegated-proof-of-stake"
type: concept
title: DPoS
title_zh: 委托权益证明
title_en: DPoS
aliases:
  - DPoS
  - Delegated Proof of Stake
  - 委托权益证明
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
  - "source:2026-08-26-tron-dao-how-tron-works"
related:
  - id: "concept:proof-of-stake"
    rel: special-case-of
    note: 持币者投票选出有限验证节点集合
  - id: "protocol:tron"
    rel: instantiated-by
    note: 27 个 Super Representatives 由 TRX 质押投票选出
prerequisites:
  - "concept:proof-of-stake"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# DPoS | 委托权益证明

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

持币者用权益投票选出有限数量的验证/出块节点。

## Why This Matters | 为什么重要

提高性能和治理效率，但验证者集合更集中。

## Concrete Example | 例子

TRON由Super Representatives参与共识。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 DPoS。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-tron-dao-how-tron-works]] — <https://developers.tron.network/docs/how-tron-works>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = proof-of-stake; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
