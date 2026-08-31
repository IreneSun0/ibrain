---
id: "concept:public-key"
type: concept
title: Public Key
title_zh: 公钥
title_en: Public Key
aliases:
  - 公钥
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
  - id: "concept:wallet"
    rel: component-of
prerequisites:
  - "concept:private-key"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# Public Key | 公钥

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

由私钥推导、可公开用于验证签名的密码学信息；地址通常进一步由它推导。

## Why This Matters | 为什么重要

让别人验证“这笔交易确实由私钥控制者授权”而无需知道私钥。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Public Key。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = private-key; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
