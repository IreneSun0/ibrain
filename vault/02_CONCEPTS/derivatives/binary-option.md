---
id: "concept:binary-option"
type: concept
title: Binary/Digital Option
title_zh: 二元/数字期权
title_en: Binary/Digital Option
aliases:
  - Binary/Digital Option
  - 二元
status: seed
importance: tier-1
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
  - id: "concept:option"
    rel: special-case-of
    note: "支付只有固定金额或 0, 无连续 payoff"
prerequisites:
  - "concept:option"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---

# Binary/Digital Option | 二元/数字期权

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

满足条件就支付固定金额，不满足就支付0的期权结构。

## Why This Matters | 为什么重要

与YES/NO事件合约的支付结构非常接近。

## Concrete Example | 例子

BTC到期是否高于$100k；YES赢则$1，否则$0。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Binary/Digital Option。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = option; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
