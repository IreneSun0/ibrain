---
id: "protocol:x-layer"
type: protocol-network
title: X Layer
title_zh: X Layer (OKX L2)
aliases:
  - OKB Chain
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
related: []
---
# X Layer

## Executive Summary

[[okx]] 体系内的 L2 网络。它与事件市场的关联目前是间接的：OKX 已公开将预测市场列入扩张计划，同时运营自己的链。

**"交易所 + 自有链 + 预测市场"是一个已经被验证可行的组合**（见 [[bnb-chain]] 与 [[predict-fun]] 的关系）。

## What It Actually Is | 它到底是什么

交易所自建链的战略逻辑很直接：

```
交易所有用户  →  自有链承接这些用户的链上活动
              →  链上活动的价值留在自己生态里
              →  分发与结算两头都拿住 (见 distribution)
```

**这解释了为什么头部交易所都在做自己的链**：它不是技术项目，是把分发优势延伸到链上的手段。

**对事件市场的含义**：如果 OKX 真的上线预测市场，最可能的形态是**建在自己的链上、通过自己的钱包分发** —— 与 BNB Chain 的路径同构。

## How It Works | 运作方式

交易所系 L2 的共同特征是**生态封闭度较高**：验证者、排序器、生态基金多由同一体系控制。

**这带来的是效率与协同，代价是去中心化程度**（见 [[layer-2]]）：抵押品的安全性取决于该体系而非以太坊。

**评估这类链上的事件市场，"链背后是谁"和"平台背后是谁"是同一个答案** —— 风险因此高度相关（见 [[concentration-risk]]）。

## Position in the Market | 它在市场里的位置

目前 X Layer 在事件市场没有已知的直接角色，它的价值是**作为一个待激活的条件**：

OKX 是头部交易所里**第一个公开把预测市场写进扩张计划**的（单源，需持续核）。若落地，它拥有钱包（多链覆盖）、用户规模、以及自有结算链 —— 三样齐备。

**这类"条件齐备但尚未动作"的玩家，是判断格局变化最有价值的观察对象。**

## What Could Break It | 什么会让它出问题

- **生态封闭带来的集中度。**
- **母公司监管处境** —— OKX 有大额认罪和解记录，扩张受合规约束。
- **计划为单源信息** —— 引用前需再核。

## What To Watch | 该盯什么

- **OKX 是否真的上线预测市场品类，以及建在哪条链上。**
- **其钱包是否内嵌第三方或自建场馆。**
