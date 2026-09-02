---
id: "concept:policy-engine"
type: concept
title: Policy Engine
title_zh: 策略/政策控制引擎
title_en: Policy Engine
aliases:
  - 策略
status: reviewed
importance: tier-1
domains:
  - industry-strategy
  - crypto-market-structure
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "concept:risk-engine"
    rel: contrasts-with
    note: "风险引擎算出风险, 政策引擎决定放不放行"
prerequisites:
  - "concept:risk-engine"
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Policy Engine | 策略/政策控制引擎

## Executive Definition / Chinese Explanation | 定义与解释

**Policy Engine | 政策引擎** = 持有规则、并把风险读数转换成**动作**的系统：拦截、限额、路由、审批。

## Why This Matters | 为什么重要

风险读数本身不改变交易或合规动作。政策引擎记录阈值与处置方式，使同一读数能够稳定触发警告、审批或拦截。不同机构可以使用同一读数，但保留各自的风险阈值。

## How It Works | 机制怎么运转

风险引擎与政策引擎的接力关系：

```
风险引擎          政策引擎
输出读数    →     持有规则      →     执行动作
风险读数           超过机构阈值          执行限制
```

三层的归属完全不同：

| 层 | 谁拥有 | 能不能外购 |
|---|---|---|
| **读数** | 数据供应商 | **可以** |
| **规则** | 机构自己 | **不能**（风险偏好是主权） |
| **执行** | 嵌进交易与合规流程 | 机构自建或系统集成 |

动作可以分为 `WARN`（警告但放行）、`REVIEW`（转人工审批）和 `BLOCK`（直接拦截）。

## Concrete Example | 具体例子

一条完整的规则链，从数据到动作：

```
IF   合约.语义分 < 机构阈值
AND  头寸.名义 > 审批阈值
THEN REVIEW（转风控人工审批）

IF   裁决机制.当前争议数 > 争议阈值
OR   合约.判定日 距今 < 临近判定阈值
THEN WARN + 禁止加仓

IF   单一裁决机制敞口 > 集中度阈值
THEN BLOCK 新开仓
```

## Common Misconceptions | 常见误解

- **误解一："政策引擎就是风控系统。"** 它是风控系统里"规则与执行"的那一半；读数那一半是风险引擎。
- **误解二："规则越多越安全。"** 规则冲突和误报会让人绕过系统。**少而准的规则胜过多而吵的规则。**

## In Practice | 实战里怎么用

用于自动规则的数据字段需要可量化，并带有时间范围与适用对象：

> **"这个字段能不能直接写进一条 `if` 语句？"**

- "该市场存在裁决不确定性" —— **不能**（不可量化）。
- "该合约语义分低于机构设定阈值" —— **能**。
- "UMA 上有争议" —— **不能**（无时间、无数量）。
- "该裁决机制在观察期内的未决争议数超过阈值" —— **能**。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 风险引擎和政策引擎分别负责什么？
  A: 风险引擎输出读数；政策引擎持有阈值并把读数转换为动作。
- Q: 读数、规则、执行三层各自能否外购？
  A: 读数可外购；规则必须机构自持（风险偏好是主权）；执行嵌进机构自己的交易与合规流程。
- Q: 自动规则需要怎样的数据字段？
  A: 可量化，并带有时间范围、适用对象和明确阈值。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
