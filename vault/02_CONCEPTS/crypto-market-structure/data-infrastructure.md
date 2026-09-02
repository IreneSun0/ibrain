---
id: "concept:data-infrastructure"
type: concept
title: Data Infrastructure
title_zh: 数据基础设施
title_en: Data Infrastructure
aliases:
  - 数据基础设施
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
  - id: "org:predexon"
    rel: instantiated-by
    note: 预测市场数据层; 独特资产 = UMA 裁决/争议数据
  - id: "org:finfeedapi"
    rel: instantiated-by
    note: 把交易所行情 schema 套到事件市场的跨资产数据商
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Data Infrastructure | 数据基础设施

## Executive Definition / Chinese Explanation | 定义与解释

**Data Infrastructure | 数据基础设施** = 把散落、异构、不可比的原始数据，变成可以被机器消费的结构化事实的那一层。

## Why This Matters | 为什么重要

事件市场的数据层除采集与分发外，还需要：

1. **建构** —— 判断哪些合约指向同一个现实事件（见 [[canonical-event-id]]）。
2. **判断** —— 标注判定状态与争议状态，这需要读懂规则文本。
3. **跨域合流** —— 行情 + 链上 + 语义 + 监管四类来源必须对齐到同一个主键上。

## How It Works | 机制怎么运转

一个可用的事件数据层至少要有四层：

| 层 | 内容 | 难点 |
|---|---|---|
| **标识层** | 事件主键 + 合约到事件的映射 | 需要等价性判断，不是哈希 |
| **状态层** | 判定进度、争议状态、终局与否 | 需要读多个平台的不同流程 |
| **语义层** | 条款结构化：主体/谓词/阈值/时点/数据源 | 需要读懂法律文本 |
| **市场层** | 行情、深度、持仓分布 | 相对标准，但跨平台口径不一 |

## Concrete Example | 具体例子

两个场馆的合约可能指向同一现实事件，但截止时间、判定来源或例外条款不同。数据层需要把它们映射到同一个 `canonical-event-id`，同时保留各自的合约语义与判定状态。

## Common Misconceptions | 常见误解

- **误解一："数据就是 API 聚合。"** 聚合是最容易的一层。难的是让不同来源的数据**指向同一个主键**。
- **误解二："先做规模，标准后补。"** 主键设计错误会使后续数据无法稳定合并。

## In Practice | 实战里怎么用

评估任何一个事件数据产品，按四层逐层问：

1. **标识层** —— 它有事件主键吗？一对多映射怎么建模？合约条款差异保留了吗？
2. **状态层** —— 争议状态是实时的还是事后的？覆盖几个平台？
3. **语义层** —— 条款是结构化字段还是原文？五要素齐吗？
4. **市场层** —— 深度数据有吗（不只是价格和成交量）？

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件数据层比价格数据层多做哪三件事？
  A: 建构（判断哪些合约指向同一现实事件）、判断（标注判定与争议状态）、跨域合流（行情+链上+语义+监管对齐到同一主键）。
- Q: 为什么同一事件的合约仍需分别保留语义？
  A: 截止时间、判定来源和例外条款可能不同，事件主键相同不代表合约等价。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
