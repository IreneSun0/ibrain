---
id: "concept:know-your-transaction"
type: concept
title: KYT
title_zh: 了解交易/链上交易监控
title_en: KYT
aliases:
  - KYT
  - Know Your Transaction
  - 了解交易
status: seed
importance: tier-2
domains:
  - regulation-compliance
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
  - id: "concept:know-your-customer"
    rel: contrasts-with
    note: "KYC 看人, KYT 看钱 — crypto AML 必须两者都有"
  - id: "concept:anti-money-laundering"
    rel: mechanism-of
    note: 资金来源与链上关联分析
  - id: "org:chainalysis"
    rel: instantiated-by
    note: 链上 KYT/情报供应商
prerequisites:
  - "concept:know-your-customer"
import_origin: xlsx-learning-map+manual
import_category: Crypto合规
---

# KYT | 了解交易/链上交易监控

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

Know Your Transaction。分析资金来源、链上地址关联和交易风险。

## Why This Matters | 为什么重要

Crypto AML不能只知道客户是谁，还要知道资金从哪里来。

## Concrete Example | 例子

Chainalysis类链上监控。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 KYT。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto合规)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = know-your-customer; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
