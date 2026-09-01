---
id: "concept:decentralized-exchange"
type: concept
title: DEX
title_zh: 去中心化交易所
title_en: DEX
aliases:
  - DEX
  - Decentralized Exchange
  - 去中心化交易所
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
  - id: "concept:exchange"
    rel: special-case-of
prerequisites:
  - "concept:exchange"
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# DEX | 去中心化交易所

## Executive Definition / Chinese Explanation | 定义与解释

**DEX (Decentralized Exchange) | 去中心化交易所** = 撮合与/或结算由智能合约执行，用户自持资产、无需把钱交给平台的交易场所。

"去中心化"是个连续谱，不是二元状态：**从"只有结算在链上"到"订单簿也在链上"，中间有很多档。**

## Why This Matters | 为什么重要

DEX 的价值主张只有一条真正硬的：**无需信任托管方。** 其余（抗审查、无需许可）视具体设计而定。

**对事件市场，这条价值主张特别贵重**：事件合约的资金要锁数月到判定日，托管风险的暴露时间远长于现货交易。**全额抵押锁在合约里，是这个市场最自然的选择。**

但要注意：**很多"DEX"的合约带升级权限或管理员密钥** —— 那实质上更接近平台托管，只是伪装成了去信任（见 [[smart-contract]]）。

## How It Works | 机制怎么运转

去中心化程度的四档：

| 档 | 撮合 | 托管 | 例 |
|---|---|---|---|
| 1 | 链下 | 平台 | 就是 CEX |
| 2 | 链下 | **链上** | hybrid（事件市场主流） |
| 3 | **链上 AMM** | 链上 | 现货 DEX 主流 |
| 4 | **链上订单簿** | 链上 | 最难，对链性能要求极高 |

**事件市场主要在第 2 和第 4 档**：
- 第 2 档兼顾速度与资金安全，是当前主流。
- 第 4 档追求完全可验证，代价是性能与成本。

**第 3 档（AMM）在事件市场用于长尾兜底** —— 无人做市时至少有报价（见 [[automated-market-maker]]）。

## Concrete Example | 具体例子

同一个事件合约，两种去中心化程度：

| | 第 2 档（hybrid） | 第 4 档（全链上） |
|---|---|---|
| 下单延迟 | 毫秒 | 受限于出块 |
| 撮合可验证 | **否** | **是** |
| 拥堵时 | 撮合正常 | **可能不可用** |
| 做市商体验 | 好 | 受限 |

**关键权衡出现在"事件揭晓时刻"**：那正是全网最拥堵、所有人同时想动的时候。

**第 4 档在这个时刻的表现，是它能否成立的真正考验** —— 平时够快不算数。

## Common Misconceptions | 常见误解

- **误解一："DEX 一定比 CEX 安全。"** 取决于合约质量与权限设计。有管理员密钥的"DEX"不比持牌 CEX 更安全。
- **误解二："去中心化 = 无人负责。"** 也意味着**出事时无人赔付**。Ukraine 案的先例是零追索（见 [[case-uma-dispute-trilogy]]）。
- **误解三："链上撮合是终局。"** 只有当链的性能与成本能承载高频撮合时才成立；在此之前 hybrid 是工程上的正解。

## In Practice | 实战里怎么用

判断一个"DEX"的真实去中心化程度，三问：

1. **合约有升级权限吗？** 有 → 你信任的是密钥持有者，不是代码。
2. **撮合在哪？** 链下 → 撮合公平性不可验证。
3. **前端谁运营？** 前端被下架时，还能不能直接与合约交互？

**第 3 问最少被问**：很多"去中心化"协议的实际访问入口是一个中心化网站，而那正是最容易被切断的一环。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: DEX 唯一真正硬的价值主张是什么？
  A: 无需信任托管方。抗审查与无需许可视具体设计而定，不是自动获得的。
- Q: 去中心化的四档分别是什么？事件市场主要在哪几档？
  A: 链下撮合+平台托管（CEX）、链下撮合+链上托管（hybrid）、链上 AMM、链上订单簿。事件市场主要在第 2 档和第 4 档。
- Q: 为什么全链上撮合的真正考验是事件揭晓时刻？
  A: 那是全网最拥堵、所有人同时想交易的时候；平时够快不算数。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = exchange, smart-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
