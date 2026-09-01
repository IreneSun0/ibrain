---
id: "mmf:wintermute"
type: market-maker-fund
title: Wintermute
title_zh: Wintermute
aliases:
  []
status: reviewed
importance: tier-1
domains:
  - crypto-market-structure
  - market-microstructure
  - prediction-outcome-markets
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
# Wintermute

## Executive Summary

加密原生的算法做市商，是**目前公开确认为 [[polymarket]] 提供流动性的机构**，也在 2025-02 [[bybit]] 被盗事件中参与了 72 小时储备补足。

它与 [[susquehanna]] 构成事件市场做市的两条路线：**加密原生 vs 传统自营。**

## What It Actually Is | 它到底是什么

两条路线的差别不是规模，是**风险处理方式**：

| | 加密原生（Wintermute） | 传统自营（SIG） |
|---|---|---|
| 主战场 | 链上 + CEX | 持牌交易所 |
| 对冲工具 | 加密现货、永续 | 期货、期权、跨资产 |
| 监管暴露 | 较低 | 高（受严格约束） |
| 进入新市场 | **快** | **慢但稳** |

**"快"是加密原生做市商的核心优势**：它可以在一个监管地位尚未明朗的市场里先报价，而传统机构不行。

**Polymarket 长期在离岸运营，能为它做市的必然是这一类。**

## How It Works | 运作方式

算法做市的经济学在事件市场上有一个特殊困难：**存货无处可去。**

在加密现货上，Wintermute 接了货可以去永续或其他所对冲；在长尾事件合约上，**没有对冲工具**（见 [[inventory-risk]]）。

**所以它在事件市场的报价必然集中在头部合约** —— 那些有足够双向需求、可以自然轧平的市场。

**这解释了事件市场深度分布的极端长尾形态**：不是做市商偷懒，是长尾根本无法被算法做市（见 [[liquidity]]）。

## Position in the Market | 它在市场里的位置

在事件市场，Wintermute 的位置是**链上侧的主要流动性来源**。

它出现在两个不同的场景里：常态做市（Polymarket），以及危机流动性（Bybit 被盗后的储备补足）。**后者说明它的资产负债表足以在极端时刻起作用** —— 这在评估做市商时是一个被低估的维度。

**它的缺席或撤出，会是链上事件市场流动性的直接预警。**

## What Could Break It | 什么会让它出问题

- **无做市义务** —— 可随时撤退，尤其在裁决临近时。
- **集中度** —— 链上侧的公开做市方选择极少。
- **监管环境变化** —— 若链上平台的合规压力上升，其参与成本会变。

## What To Watch | 该盯什么

- **是否扩展到持牌场馆** —— 从链上走向持牌是能力与合规的双重升级。
- **在重大事件裁决窗口是否仍在报价** —— 这是检验做市质量的真实时刻。
- **是否有第二家链上做市商公开进场** —— 单一来源是结构性脆弱。


## Sources

[[report-2026-08-26-infra-mm-stablecoins]] (一手: wintermute.com 官宣)

<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验)。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
