---
id: "protocol:sunpump"
type: protocol-network
title: SunPump
title_zh: TRON meme公平发行平台
title_en: SunPump
aliases:
  - TRON meme公平发行平台
status: reviewed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
tags:
  - protocol-network
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
  - "source:2026-08-26-tron-dao-tron-network"
related:
  - id: "protocol:tron"
    rel: built-on
    note: TRON 生态的 meme token fair-launch 平台
prerequisites: []
import_origin: xlsx-learning-map
import_category: TRON生态
---
# SunPump | TRON meme公平发行平台

## Executive Summary

[[tron]] 生态的 meme 代币公平发射平台，承担代币发行与用户/流动性增长入口的角色。

**它与事件市场没有直接关系，但它演示了一个相关机制**：如何用极低的门槛把长尾资产批量上线 —— 而事件市场面对的正是同一个问题（见 [[order-flow-network-effect]]）。

## What It Actually Is | 它到底是什么

公平发射平台的核心设计是**把上线成本压到接近零**：任何人都能发一个资产，由曲线自动提供初始流动性。

**这与事件市场的长尾困境高度同构**：

| | meme 发射 | 长尾事件合约 |
|---|---|---|
| 数量 | 无限 | 无限 |
| 单个流动性 | 极薄 | 极薄 |
| 解法 | **曲线自动做市** | **AMM 兜底**（见 [[automated-market-maker]]） |

**两者的解法是同一个**：无人做市时，用公式保证总有报价。

**两者的代价也是同一个**：曲线做市方承担被套利的损失，而在事件市场里这个损失是永久的（见 [[liquidity-provider]]）。

## How It Works | 运作方式

这类平台的经济学建立在**量而非质**上：绝大多数发行归零，少数产生流量，平台按交易额抽成。

**把这个逻辑套到事件市场上会得到一个不舒服的结论**：如果一个事件市场平台的收入模式是"上尽可能多的合约、按成交抽成"，那么它**没有动力保证合约质量**（见 [[contract-semantics]]）。

**上市审查与收入模式在这里是直接冲突的。**

## Position in the Market | 它在市场里的位置

SunPump 不是事件市场参与者，此处仅用于比较长尾资产的批量上线机制。

长尾资产可以批量上线，但批量化不能同时保证资产质量；事件市场采用相同机制时也会继承这一取舍。

## What Could Break It | 什么会让它出问题

- **绝大多数发行归零** —— 对用户是高损失率环境。
- **监管定性不明** —— 各辖区对此类平台态度不一。

## What To Watch | 该盯什么

- **事件市场是否出现"任何人可开盘"的平台** —— 若出现，看它怎么解决合约质量。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
- [[src-2026-08-26-tron-dao-tron-network]] — <https://tron.network/>
