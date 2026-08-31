---
id: "concept:proof-of-stake"
type: concept
title: PoS
title_zh: 权益证明
title_en: PoS
aliases:
  - PoS
  - Proof of Stake
  - 权益证明
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
  - id: "concept:consensus"
    rel: special-case-of
  - id: "concept:proof-of-work"
    rel: contrasts-with
    note: 质押经济惩罚 vs 算力成本竞争
  - id: "protocol:ethereum"
    rel: instantiated-by
    note: 最大 PoS 智能合约链
prerequisites:
  - "concept:consensus"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# PoS | 权益证明

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

Proof of Stake。验证者质押资产参与共识，作恶可能失去收益或被惩罚。

## Why This Matters | 为什么重要

用经济抵押替代PoW的大量计算竞争。

## Concrete Example | 例子

Ethereum PoS。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 PoS。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = consensus; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
