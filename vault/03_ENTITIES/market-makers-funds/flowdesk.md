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

**这个模式对事件市场理论上很对口**：长尾事件合约无人愿意自担风险做市（见 [[inventory-risk]]），但如果场馆愿意付费买流动性，外包做市就成立。

**它把"没人愿意承担风险"的问题，转化成"谁来付这个钱"的问题** —— 后者至少是可谈判的。

## How It Works | 运作方式

做市即服务的核心是**技术平台 + 多场所接入 + 合规**，而不是资本规模。

它的客户通常是需要在多个场所维持流动性的代币项目或场馆。

**对事件市场的启示**：一个新场馆冷启动时（见 [[order-flow-network-effect]]），与其等专业做市商自愿进场，不如**直接购买流动性服务** —— 前提是算清楚这笔钱值不值（见 [[market-maker-incentive]]）。

## Position in the Market | 它在市场里的位置

Flowdesk 在事件市场的公开关联为 **UNKNOWN**。

它在这个知识库里的价值是**提供一个尚未被采用的解法**：事件市场的长尾流动性问题，可能不需要等到专业自营愿意进场，而可以通过服务化的方式解决。

**目前没有公开案例说明有场馆在这样做** —— 这既是空白，也是一个可验证的假设。

## What Could Break It | 什么会让它出问题

- **模式依赖客户付费意愿** —— 场馆预算有限时首先砍这项。
- **公开信息稀薄** —— 高管在任状态等基本信息缺少近期时间戳源，标 UNVERIFIED。
- **事件市场关联未证实。**

## What To Watch | 该盯什么

- **是否有事件市场场馆采购做市服务** —— 第一个案例会定义这个模式的定价。
- **欧洲监管框架下的做市服务合规路径。**


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
