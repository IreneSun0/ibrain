---
id: "protocol:pyth-network"
type: protocol-network
title: Pyth Network
title_zh: Pyth (预言机)
aliases:
  - Pyth
status: reviewed
importance: tier-2
domains:
  - blockchain
  - crypto-market-structure
tags:
  - protocol-network
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related:
  - id: "mmf:jump-crypto"
    rel: backed-by
    note: "由 Jump 孵化; 核心贡献方 Douro Labs 出自前 Jump 团队"
---
# Pyth Network

## Executive Summary

**第一方**金融数据预言机：价格直接由交易公司与交易所发布，而不是由第三方节点去外部抓取。由 [[jump-crypto]] 孵化，核心贡献团队出自前 Jump 人员。

2025-09 起与美国商务部合作，把联邦经济数据（自 GDP 起）上链分发 —— **这是首次有美国机构用去中心化预言机分发官方统计。**

## What It Actually Is | 它到底是什么

"第一方"这三个字是它与 [[chainlink]] 的根本差别：

```
第三方预言机: 节点 → 去交易所抓价 → 聚合 → 上链
第一方预言机: 交易公司/交易所 → 直接发布自己的价格 → 聚合 → 上链
```

**第一方的优势是数据源头更近**（发布者就是价格的产生者）；**代价是发布者集中度**——如果发布者是同一批交易公司，它们的利益未必与用户一致。

**对事件市场，这个差别很具体**：价格类合约的裁决要读价（见 [[resolution-source]]），而"谁提供这个价"直接决定裁决可被谁影响。

## How It Works | 运作方式

与官方统计数据的合作是这条线里最值得关注的一步：

**因为事件市场最需要裁决的一类标的恰恰是官方数据**（CPI、失业率、GDP）—— 如果这些数据本身以可验证的方式上链，那么这一类合约的裁决可以完全自动化，不需要任何人工判断。

```
CPI 合约的裁决:
  今天  → 读官方发布 → 人工/半自动录入 → 争议空间
  可能  → 官方数据直接上链 → 合约自动结算 → 无争议空间
```

**这条路径能消灭一整类裁决风险** —— 那是这个赛道最实在的进步方向之一。

## Position in the Market | 它在市场里的位置

在事件市场的裁决基础设施里，Pyth 目前主要覆盖**价格类**，与 Chainlink 竞争同一片区域。

它的差异化在两处：第一方数据的源头优势，以及**官方统计上链**这条别人没有的线。

**若后者铺开，它会从"另一个喂价预言机"变成"官方数据的链上通道"** —— 那是一个结构性不同的位置。

## What Could Break It | 什么会让它出问题

- **发布者集中度** —— 第一方模式依赖一批交易公司持续诚实发布。
- **规模口径冲突** —— 自报数据与第三方统计存在明显差异，引用时需注明口径。
- **与孵化方的关联** —— Jump 同时是孵化者、发布者与相关市场参与者（见 [[jump-crypto]]）。

## What To Watch | 该盯什么

- **官方数据上链的覆盖范围是否扩大** —— 每多一项，就少一类裁决争议。
- **是否被事件市场用于价格类裁决** —— 目前 Polymarket 与 Predict.fun 走的是 Chainlink。
- **发布者名单的分散程度。**
