---
id: "concept:tron-energy"
type: concept
title: Energy (TRON)
title_zh: TRON能量/计算资源
title_en: Energy (TRON)
aliases:
  - Energy (TRON)
  - TRON能量
status: seed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
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
  - "source:2026-08-26-tron-dao-resource-model"
related:
  - id: "concept:gas"
    rel: contrasts-with
    note: 质押换配额 vs 逐笔付费 — TRON 与 Ethereum 的资源定价哲学差异
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: TRON
---

# Energy (TRON) | TRON能量/计算资源

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

TRON用于计量TVM执行智能合约指令消耗的计算资源单位。

## Why This Matters | 为什么重要

智能合约越复杂，消耗Energy越多。

## Concrete Example | 例子

TRC-20 USDT转账会调用智能合约，因此消耗Energy。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Energy (TRON)。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-tron-dao-resource-model]] — <https://developers.tron.network/docs/resource-model>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: TRON)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = smart-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
