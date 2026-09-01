---
id: "protocol:chainlink"
type: protocol-network
title: Chainlink
title_zh: Chainlink (预言机)
aliases:
  - LINK
status: reviewed
importance: tier-1
domains:
  - blockchain
  - prediction-outcome-markets
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
related: []
---
# Chainlink

## Executive Summary

最广泛使用的去中心化预言机网络。在事件市场里，它的角色正在从"喂价"变成**裁决基础设施的一半**。

**标志性变化**：[[polymarket]] 自 2025-09 起把**价格类市场的结算移交 Chainlink**，绕开 [[uma]] 的人工投票；[[predict-fun]] 采用同构双轨（事件类走 UMA，价格类走 Chainlink）。

## What It Actually Is | 它到底是什么

这个转变背后是一条清晰的行业判断：**能自动化的裁决，就不该留给人和投票。**

| 裁决类型 | 特征 | 归谁 |
|---|---|---|
| **价格类**（BTC 收盘价、指数点位） | 可量化、有权威源 | **自动化喂价** |
| **主观类**（某人是否卸任、是否穿西装） | 需要解释 | 预言机投票或人工委员会 |

**这条分流线是当前事件市场最重要的结构性演进**（见 [[resolution-source]]）：它把 [[oracle-risk]] 的暴露面从"所有合约"缩小到"需要解释的那部分"。

**剩下那部分仍然无解** —— 而那正是这个赛道最难也最有价值的位置。

## How It Works | 运作方式

Chainlink 的安全模型与乐观预言机完全不同：

```
乐观预言机: 默认相信提议 → 有人挑战 → 代币投票终裁
Chainlink:  多个独立节点取数 → 聚合 → 上链, 无投票环节
```

**没有投票就没有"投票权可购买"这个攻击面**（见 [[case-uma-dispute-trilogy]] 的 Ukraine 案）。

代价是**它只能处理有权威数据源的问题**：给它一个"某国领导人是否卸任"，它没有可聚合的数据源可读。

**所以它不是 UMA 的替代品，是分工的另一半。**

## Position in the Market | 它在市场里的位置

在事件市场的裁决层，格局正在变成两轨：

| | 覆盖 | 主要风险 |
|---|---|---|
| **Chainlink 类自动化** | 价格与可量化标的 | 数据源本身失效、聚合节点集中度 |
| **UMA 类乐观预言机** | 主观与语义类 | 投票权可购买、挑战激励不足 |

**Chainlink 拿走了容易的一半，且拿得很稳** —— 它在多链上的部署深度和采用量让它成为默认选项（TRON 也在 2025-05 把官方 oracle 切换为它）。

**难的一半仍空着，这是这个知识库反复指向的那个位置。**

## What Could Break It | 什么会让它出问题

- **数据源上游风险** —— 聚合多个节点解决的是节点故障，不解决所有节点读同一个坏源。
- **节点运营方集中度** —— 需要单独评估。
- **只能覆盖可量化标的** —— 对事件市场最棘手的部分无能为力。

## What To Watch | 该盯什么

- **是否有主观类裁决的新方案出现** —— 那会是这个赛道的分水岭。
- **更多场馆采用双轨结算** —— 采用率决定这条分流是否成为标准。
- **合规工作流上链的进展** —— 与情报商的合作方向（见 [[chainalysis]]）。


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
