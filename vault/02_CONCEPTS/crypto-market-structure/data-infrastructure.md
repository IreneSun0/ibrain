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

在事件市场里它比在价格市场里难得多，因为**价格数据天然统一（都是数字），而事件数据必须先被建构出来**。

## Why This Matters | 为什么重要

价格市场的数据层是"采集 + 分发"：交易所给出价格，标准化几乎是免费的 —— 所有人对"BTC 的价格"没有歧义。

事件市场的数据层要做三件价格市场不需要做的事：

1. **建构** —— 判断哪些合约指向同一个现实事件（见 [[canonical-event-id]]）。
2. **判断** —— 标注判定状态与争议状态，这需要读懂规则文本。
3. **跨域合流** —— 行情 + 链上 + 语义 + 监管四类来源必须对齐到同一个主键上。

**所以事件数据不是"采集来的"，是"构造出来的"** —— 而构造需要领域判断，这是它难以被快速复制的原因。

## How It Works | 机制怎么运转

一个可用的事件数据层至少要有四层：

| 层 | 内容 | 难点 |
|---|---|---|
| **标识层** | 事件主键 + 合约到事件的映射 | 需要等价性判断，不是哈希 |
| **状态层** | 判定进度、争议状态、终局与否 | 需要读多个平台的不同流程 |
| **语义层** | 条款结构化：主体/谓词/阈值/时点/数据源 | 需要读懂法律文本 |
| **市场层** | 行情、深度、持仓分布 | 相对标准，但跨平台口径不一 |

**前三层是护城河，第四层是商品。** 大多数团队从第四层开始做，因为它最容易 —— 也因此最容易被复制。

## Concrete Example | 具体例子

为什么"生成式 AI 让数据层不再值钱"的说法在这里不成立：

生成式 AI 压塌了**应用层**的复制成本 —— 界面、报表、摘要现在人人可做。但它**消费**数据，不能**无中生有**数据：

- 采集需要接入（API 权限、链上索引、文档抓取）；
- 清洗需要领域判断（这两份合约是不是同一件事？）；
- **积累需要时间**（争议历史、判定记录、语义演化只能一天天攒）。

**结果是价值向数据层集中**：应用可以一夜复制，三年的争议历史库不能。

## Common Misconceptions | 常见误解

- **误解一："数据就是 API 聚合。"** 聚合是最容易的一层。难的是让不同来源的数据**指向同一个主键**。
- **误解二："AI 能自动做语义结构化。"** 能做初筛，但**边界条件的等价判定必须逐条比对** —— 那是确定性工作，不是相似度判断。
- **误解三："先做规模，标准后补。"** 主键设计错了，后面所有数据都要重建。**标识层是第一天就要定下来的事。**

## In Practice | 实战里怎么用

评估任何一个事件数据产品，按四层逐层问：

1. **标识层** —— 它有事件主键吗？一对多映射怎么建模？合约条款差异保留了吗？
2. **状态层** —— 争议状态是实时的还是事后的？覆盖几个平台？
3. **语义层** —— 条款是结构化字段还是原文？五要素齐吗？
4. **市场层** —— 深度数据有吗（不只是价格和成交量）？

**只有第 4 层的产品是行情终端，不是风险数据。** 而机构付费的理由通常在前三层。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件数据层比价格数据层多做哪三件事？
  A: 建构（判断哪些合约指向同一现实事件）、判断（标注判定与争议状态）、跨域合流（行情+链上+语义+监管对齐到同一主键）。
- Q: 为什么生成式 AI 没有让事件数据层贬值？
  A: AI 压塌了应用层复制成本，但它消费数据而不能无中生有：接入、领域判断和时间积累（争议历史）都无法被快速复制。
- Q: 事件数据的四层里哪三层是护城河、哪一层是商品？
  A: 标识层、状态层、语义层是护城河；市场层（行情与深度）相对标准，是商品。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 产业战略)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
