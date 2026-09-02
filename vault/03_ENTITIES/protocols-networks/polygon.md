---
id: "protocol:polygon"
type: protocol-network
title: Polygon
title_zh: Polygon
aliases:
  - MATIC
  - POL
status: reviewed
importance: tier-1
domains:
  - blockchain
  - prediction-outcome-markets
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
# Polygon

## Executive Summary

EVM 兼容的 PoS 网络，**全球最大加密预测市场 [[polymarket]] 的执行与结算链**。抵押品是链上 USDC，结果代币是 ERC-1155（conditional tokens framework），裁决由 [[uma]] 适配器写回合约。

选它不是技术偏好，是经济必然：以太坊主网单笔几美元到几十美元的 [[gas]]，会让一个 $50 的事件头寸在开仓那一刻就亏掉 20%（见 [[layer-2]]）。

## What It Actually Is | 它到底是什么

**严格说它不是 L2，是侧链** —— 这一点直接关系到你的抵押品有多安全。

| | 继承以太坊安全 | 自己的验证者集 |
|---|---|---|
| Rollup | ✓ | — |
| **Polygon PoS** | **✗** | **✓** |

它有自己的 PoS 验证者集合，安全预算与以太坊无关。**"我的钱在链上"这句话在这里的准确含义是：你的钱由 Polygon 的验证者集保护，不是由以太坊保护。**

这不是说它不安全，而是说**它是一个需要单独评估的对象**，不能靠"反正在链上"带过（见 [[layer-1]]）。

## How It Works | 运作方式

预测市场在 Polygon 上的完整链路：

```
USDC 存入 → CTF 合约铸造 YES/NO 结果代币 (ERC-1155)
撮合在链下 (CLOB) → 成交后链上转移代币
判定日 → UMA 适配器把结果写入合约 → 持有方赎回
```

**三个必须分开看的信任点**：
1. **抵押品** —— 锁在合约里，平台无法挪用（可链上验证）。
2. **撮合** —— 在链下，公平性**无法外部验证**。
3. **裁决** —— 由预言机写入，链只忠实执行（见 [[oracle-risk]]）。

**链解决的是第 1 点，第 2、3 点不在它的职责范围内。** 混淆这三者，是评估链上事件市场时最常见的错误。

## Position in the Market | 它在市场里的位置

Polygon 在事件市场里的位置是**被选中的结算轨道**，而不是竞争者。

它的价值主张对这个赛道极其对口：EVM 兼容（工具与合约标准可直接复用，见 [[erc-1155]]）、成本足够低（零售规模成立）、生态成熟（USDC 原生流通）。

**但这也构成了一个集中度事实**：全球最大的加密事件市场把执行与结算放在同一条链上。这条链的拥堵、故障或验证者问题，会直接传导为该市场的不可用（见 [[concentration-risk]]）。

## What Could Break It | 什么会让它出问题

三类，按可能性排序：

1. **拥堵与费用尖峰** —— 事件揭晓时全网同时提交交易，正是最需要交易的时刻（见 [[gas]]）。
2. **验证者集中度** —— 少数实体控制多数权益即单点风险；前 1/3 就足以阻止最终性（见 [[proof-of-stake]]）。
3. **跨链桥** —— 资金从以太坊进出要经过桥，而桥是链上历史上最集中的攻击面（见 [[bridge]]）。

**第 3 点常被忽略**：它不属于任何一条链的安全预算，是路径上单独的一段。

## What To Watch | 该盯什么

看 Polygon 作为事件市场结算轨道，四个指标：

1. **重大事件日的费用与延迟** —— 平时便宜不算数，看高峰。
2. **验证者数量与前 5 大质押占比**。
3. **RPC 与索引服务的可用性** —— 读路径故障会让依赖链上状态的系统失效。
4. **Polymarket 是否出现多链结算** —— 一旦分散，集中度风险下降，但流动性碎片化上升（见 [[liquidity]]）。
