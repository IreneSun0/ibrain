---
id: "mmf:flowdesk"
type: market-maker-fund
title: Flowdesk
title_zh: Flowdesk
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
tags:
  - market-maker-fund
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: medium
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related: []
---
# Flowdesk

## Executive Summary

巴黎的做市与流动性技术商，把做市做成服务（"Market-Making as a Service"）卖给代币发行方与场馆，累计融资约 $2.8 亿。

**它代表一种事件市场目前没有的模式**：做市不是自营，而是**外包服务**。

## What It Actually Is | 它到底是什么

传统做市商用自有资本自负盈亏；Flowdesk 的模式是**为客户做市并收服务费**：

| | 自营做市 | 做市即服务 |
|---|---|---|
| 资本 | 自有 | 客户或混合 |
| 收益 | 价差与库存收益 | **服务费 + 分成** |
| 风险 | 自担 | **部分转移给客户** |

该模式可以用于补充长尾市场的流动性，但成立条件包括场馆预算、做市风险分配与合规安排。

## How It Works | 运作方式

做市即服务的核心是**技术平台 + 多场所接入 + 合规**，而不是资本规模。

它的客户通常是需要在多个场所维持流动性的代币项目或场馆。

新场馆冷启动时，可以比较采购流动性服务与自建做市激励的成本和风险（见 [[order-flow-network-effect]]、[[market-maker-incentive]]）。

## Position in the Market | 它在市场里的位置

Flowdesk 截至 2026-08 **没有公开的事件市场业务记录**。

目前没有公开案例表明事件市场场馆已采用这类服务，因此其适用性仍待验证。

## What Could Break It | 什么会让它出问题

- **依赖场馆预算** —— 采购成本可能限制采用范围。
- **公开信息稀薄** —— 高管在任状态等基本信息缺少近期时间戳源，标 UNVERIFIED。
- **事件市场关联未证实。**

## What To Watch | 该盯什么

- **是否有事件市场场馆采购做市服务** —— 第一个案例会定义这个模式的定价。
- **欧洲监管框架下的做市服务合规路径。**
