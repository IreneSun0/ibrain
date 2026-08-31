---
id: "concept:outcome-token"
type: concept
title: Outcome Token
title_zh: 结果代币
title_en: Outcome Token
aliases:
  - 结果代币
status: seed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - "source:2026-08-26-polymarket-overview"
related:
  - id: "concept:token"
    rel: special-case-of
    note: 代表特定结果支付权的 token
  - id: "concept:outcome-market"
    rel: component-of
    note: outcome market 的可转让构件
  - id: "concept:erc-1155"
    rel: see-also
    note: Polymarket CTF 用 ERC-1155 一约承载多结果 token
prerequisites:
  - "concept:token"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---

# Outcome Token | 结果代币

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

代表某个结果发生时可获得特定支付的token。

## Why This Matters | 为什么重要

把事件的payoff变成链上可转让资产。

## Concrete Example | 例子

Polymarket YES/NO ERC-1155 token。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Outcome Token。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-polymarket-overview]] — <https://docs.polymarket.com/developers/CTF/overview>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = token; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
