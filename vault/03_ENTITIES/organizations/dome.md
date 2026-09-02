---
id: "org:dome"
type: organization
title: Dome (domeapi.io)
title_zh: Dome (已被收购关停)
aliases:
  - domeapi
status: reviewed
importance: tier-2
domains:
  - prediction-outcome-markets
tags:
  - organization
  - defunct
created: 2026-08-27
updated: 2026-08-31
last_verified: 2026-08-27
review_after: 2027-08-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-27-pm-data-vendors"
related:
  - "case:dome-acquisition"
  - "venue:polymarket"
---
# Dome (domeapi.io) — 已停业

## Executive Summary

预测市场数据与执行工具商，**2025 年被 [[polymarket]] 收购** —— 这是这个赛道第一起有代表性的"场馆吞掉工具层"事件。

**它的价值不在于它自己，而在于它被收购这件事说明了什么。**

## What It Actually Is | 它到底是什么

Dome 做的是跨场馆的数据与执行工具：把多个预测市场的行情与下单能力聚合成一个接口。

**这类工具层的处境天然脆弱**：

```
它的价值 = 帮用户跨越多个场馆
但       = 场馆不希望自己被商品化
结果     = 头部场馆可能选择收购并内部化这类能力
```

**这正是发生的事。** 被收购之后，一个"中立聚合层"变成了"某一家场馆的内部工具"。

**对整个市场的含义**：中立性一旦被收购就消失了，而中立性正是聚合层的全部价值（见 [[contract-equivalence]]）。

## How It Works | 运作方式

这起收购给工具层的所有玩家提供了一个明确的教训（见 [[opticodds]] 的策略选择）：

| 定位 | 风险 |
|---|---|
| **做执行 + 路由** | 直接与场馆争夺用户关系 → **被收购或被封杀** |
| **只做数据、不碰执行** | 不威胁场馆 → 可以长期中立 |

**有数据商在这之后明确退出了执行与跨场馆匹配业务**，转做纯数据 —— 那是对这起收购的直接反应。

**这是一次真实的市场结构演化，被记录下来了。**

## Position in the Market | 它在市场里的位置

在事件市场的历史里，Dome 收购案是一个**分水岭事件**：

它标志着场馆开始向上游整合（见 [[exchange-vertical-integration]]），也标志着"中立聚合层"这个位置的商业风险被公开定价。

跨场馆中立服务需要同时管理客户集中度、平台依赖与被纵向整合的风险。

**目前的答案倾向于"不碰客户资金、不做执行"** —— 只做判断与数据，让客户自己路由。

## What Could Break It | 什么会让它出问题

- **被收购后中立性消失** —— 已发生。
- **对其余工具商的示范效应** —— 提高了整个工具层的估值不确定性。
- **场馆整合的持续压力。**

## What To Watch | 该盯什么

- **是否有其他工具商被收购** —— 第二起会确认这是趋势而非个案。
- **纯数据定位的玩家能否维持独立。**
- **场馆是否继续向上游整合**（数据、指数、风控）。
