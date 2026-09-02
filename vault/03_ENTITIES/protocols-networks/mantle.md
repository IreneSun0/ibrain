---
id: "protocol:mantle"
type: protocol-network
title: Mantle
title_zh: Mantle
aliases:
  - MNT
  - BitDAO
status: reviewed
importance: tier-3
domains:
  - blockchain
tags:
  - protocol-network
created: 2026-08-27
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-cex-lineage"
related:
  - id: "protocol:ethereum"
    rel: built-on
    note: "Ethereum L2"
  - id: "venue:bybit"
    rel: backed-by
    note: "前身 BitDAO 由 Bybit 生态孵化, 金库主要来自 Bybit; MNT 是其事实生态代币"
---
# Mantle

## Executive Summary

以太坊 L2，前身是由 [[bybit]] 生态孵化的 DAO（金库主要来自 Bybit），2023 年完成代币转换并上线主网。**MNT 事实上承担了 Bybit 生态代币的位置。**

它是"交易所 + 自有链"这一模式的另一个样本（对照 [[x-layer]] 与 [[bnb-chain]]）。

## What It Actually Is | 它到底是什么

三家头部交易所、三条自有链，模式一致：

| 交易所 | 链 | 事件市场状态 |
|---|---|---|
| Binance 生态 | [[bnb-chain]] | **已有两家场馆** |
| OKX | [[x-layer]] | 计划中（单源） |
| Bybit 生态 | **Mantle** | **无公开部署** |

**这张表本身就是一个预测**：如果"交易所 + 自有链 + 内嵌预测市场"是可复制的组合，那么第二、三行迟早会被填上。

**BNB Chain 已经走完了这条路，其余两家有全部条件。**

## How It Works | 运作方式

L2 的技术选择决定安全模型（见 [[layer-2]]）：Rollup 继承以太坊的安全，侧链不继承。

**对事件市场用户，这一条比 TPS 重要得多**：你的抵押品的安全来源是哪条链的验证者集？

**交易所系 L2 还有一层特殊风险**：链与交易所的命运高度相关。交易所出问题（如 2025-02 的被盗事件），生态代币与链上活动都会受冲击 —— **这是普通 L2 没有的相关性**（见 [[concentration-risk]]）。

## Position in the Market | 它在市场里的位置

在事件市场版图上，Mantle 目前是**空位**：有链、有生态代币、有交易所用户池，但没有已知的事件市场部署。

**它的价值在于让"交易所系链会不会都上预测市场"这个问题变得可检验** —— 这不是猜测，是一个有明确观察指标的假设。

## What Could Break It | 什么会让它出问题

- **与交易所命运绑定** —— 相关性风险高于独立 L2。
- **生态代币的治理与价值捕获路径复杂。**
- **截至 2026-08 没有公开的事件市场部署。**

## What To Watch | 该盯什么

- **是否出现建在 Mantle 上的事件市场。**
- **Bybit 钱包是否内嵌预测市场入口。**
