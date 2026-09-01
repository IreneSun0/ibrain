---
id: "concept:over-the-counter"
type: concept
title: OTC
title_zh: 场外交易
title_en: OTC
aliases:
  - Institutional OTC
  - OTC
  - 场外交易
status: reviewed
importance: tier-2
domains:
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
  - id: "concept:order-book"
    rel: contrasts-with
    note: 双边协商避免公开盘口冲击 vs 集中透明但暴露交易意图
  - id: "mmf:b2c2"
    rel: instantiated-by
    note: 机构 OTC 流动性商
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# OTC | 场外交易

## Executive Definition / Chinese Explanation | 定义与解释

**OTC (Over-the-Counter) | 场外交易** = 不在公开交易所撮合，而是双方（或经中介）私下议价成交。

它存在的唯一理由是**规模**：公开盘口装不下的单子，只能到场外去谈。

## Why This Matters | 为什么重要

OTC 在事件市场的重要性被低估了，原因是一个简单的数学事实：

**长尾事件合约的公开盘口深度通常只有几千美元，而机构的最小配置规模是几十万起。** 两者差两三个数量级 —— **公开盘口在结构上无法服务机构。**

**所以事件市场的机构化必然伴随 OTC/RFQ 结构的出现**（见 [[request-for-quote]]），这不是选择，是算术。

## How It Works | 机制怎么运转

OTC 成交的三种形态：

| 形态 | 机制 | 适用 |
|---|---|---|
| **双边议价** | 直接找对手方谈 | 关系型、超大额 |
| **RFQ** | 同时问几家做市商报价 | 主流 |
| **大宗交易（block trade）** | 场外谈定、交易所过户清算 | **兼顾私密与清算保障** |

**第三种最值得注意**：它把"价格发现在场外、清算在场内"分开，**既避免了盘口冲击，又保留了中央对手方的保护**。

传统衍生品市场大量使用这种结构，而事件市场刚开始出现（有持牌场馆已在推进机构大宗交易通道）。

## Concrete Example | 具体例子

一笔 $2M 的事件合约需求，三条路的真实成本：

| 路径 | 价格 | 冲击 | 对手方风险 |
|---|---|---|---|
| 公开盘口打进去 | 均价 0.68 | +8 分，不完全恢复 | 无（有清算） |
| 纯 OTC 双边 | 0.655 | 近零 | **承担对手方** |
| **大宗交易** | 0.66 | 近零 | **无（场内清算）** |

**第三行是结构最优的**：价格接近 OTC，风险接近场内。

**它的前提是场馆提供这条通道** —— 而这需要清算能力和机构关系，是持牌场馆的结构性优势。

## Common Misconceptions | 常见误解

- **误解一："OTC 就是不透明。"** 成交后通常要上报；不透明的是**成交前**的意图，而那正是它的价值。
- **误解二："OTC 价格一定更差。"** 对大额通常更好 —— 因为避免了价格冲击（见 [[price-impact]]）。
- **误解三："OTC 只有机构能用。"** 越来越多平台把 RFQ 做进散户界面。

## In Practice | 实战里怎么用

决定走公开盘口还是场外，一条判据（见 [[request-for-quote]]）：

> **你的规模 ÷ 该盘口 ±1% 深度**

- **< 1** → 公开盘口更便宜。
- **1–5** → 拆单或 RFQ，比一比。
- **> 5** → **公开盘口装不下你**。

**再问一条**：这个场馆有没有大宗交易通道？有 → 可以同时拿到 OTC 的价格和场内的清算保护，那通常是最优解。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说事件市场的机构化必然伴随 OTC 结构？
  A: 长尾合约公开盘口深度只有几千美元，而机构最小配置规模是几十万起，差两三个数量级，公开盘口结构上服务不了机构。
- Q: 大宗交易（block trade）的结构优势是什么？
  A: 价格发现在场外（避免冲击），清算在场内（保留中央对手方保护）—— 兼顾私密与风险保障。
- Q: OTC 不透明的到底是什么？
  A: 成交前的意图。成交后通常要上报；隐藏意图正是它相对公开盘口的价值所在。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = order-book; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
