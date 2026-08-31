---
id: "concept:stablecoin"
type: concept
title: Stablecoin
title_zh: 稳定币
title_en: Stablecoin
aliases:
  - 稳定币
status: seed
importance: tier-1
domains:
  - stablecoins-wallets-payments
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
  - id: "concept:token"
    rel: special-case-of
    note: 锚定稳定价值的 token
  - id: "org:tether"
    rel: instantiated-by
    note: USDT — 约六成稳定币供应
  - id: "org:circle"
    rel: instantiated-by
    note: USDC 发行方
  - id: "concept:settlement-rail"
    rel: see-also
    note: 稳定币+公链共同构成 crypto 的事实结算轨
prerequisites:
  - "concept:token"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# Stablecoin | 稳定币

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

目标是维持相对稳定价值（通常锚定美元）的链上token。

## Why This Matters | 为什么重要

在crypto里承担现金、抵押品、结算货币和跨境支付媒介的角色。

## Concrete Example | 例子

USDT、USDC。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Stablecoin。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = token; typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
