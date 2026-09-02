---
id: "mmf:jump-crypto"
type: market-maker-fund
title: Jump Crypto
title_zh: Jump Crypto
aliases:
  - Jump Trading
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
  - blockchain
tags:
  - market-maker-fund
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related: []
---
# Jump Crypto

## Executive Summary

芝加哥自营交易巨头 Jump Trading 的加密部门，同时是**做市商、基础设施投资方与协议孵化者** —— 三个身份叠加，是理解它在这个行业分量的关键。

它孵化了 [[pyth-network]]（第一方金融数据 oracle），并在 2026-02 参与投资了 BNB Chain 上的事件市场 [[opinion-labs]]。

## What It Actually Is | 它到底是什么

Jump 与纯做市商的区别在于**它同时是基础设施的建造者**：

| 身份 | 表现 |
|---|---|
| 做市商 | 多个加密场所的流动性提供方 |
| 投资方 | 事件市场与基础设施项目的早期资本 |
| **孵化者** | **Pyth 出自 Jump 团队；Douro Labs 由前 Jump 人员组建** |

**第三行是它与 [[jane-street]]、[[susquehanna]] 最大的差别**：后者是交易公司，Jump 还建协议。

这意味着它在事件市场的利益不只是交易收益，还包括**它所建基础设施被采用**的收益 —— 这两者未必总是一致。

## How It Works | 运作方式

Jump 的加密业务横跨三层：

1. **交易层** —— 自营做市，赚价差与结构性机会（见 [[market-maker]]）。
2. **基础设施层** —— 数据 oracle、跨链设施。
3. **资本层** —— 对场馆与工具的股权投资。

**这种纵向布局在事件市场里有一个具体后果**：它可以同时是某个场馆的做市商、该场馆所用 oracle 的建造方、以及该场馆的股东。**三个角色的利益并不天然一致**（见 [[exchange-vertical-integration]]）。

## Position in the Market | 它在市场里的位置

在事件市场，Jump 的位置是**通过基础设施与资本参与，而不是通过品牌**。

普通用户在 Polymarket 或 Kalshi 上看不到它的名字，但它可能同时在报价、在提供价格数据、在持有股权。

**这正是这个行业最容易被低估的一层**：真正决定市场结构的往往不是台前的场馆，而是背后同时占据多个位置的交易公司。

## What Could Break It | 什么会让它出问题

- **监管注意** —— 历史上大型加密做市商反复出现在执法与诉讼叙事里（Terraform 相关指控波及多家）。
- **角色冲突** —— 做市 + 建基础设施 + 持股，任何一环出问题都会传导到其余两环。
- **信息优势的争议** —— 同时看到订单流与 oracle 数据，会引发公平性质疑（见 [[inside-information]]）。

## What To Watch | 该盯什么

- **它是否设立事件市场专门做市台** —— 可作为机构参与度的观察指标之一（对照 [[cumberland-drw]] 的报道级消息）。
- **Pyth 是否被事件市场用于价格类裁决** —— 那会把 Jump 从"投资方"变成"裁决基础设施提供方"。
- **它的投资组合里出现哪些新的事件市场项目。**
