---
id: "org:circle"
type: organization
title: Circle
title_zh: Circle (USDC 发行方)
aliases:
  - USDC 发行方
  - CRCL
status: reviewed
importance: tier-1
domains:
  - stablecoins-wallets-payments
  - crypto-market-structure
tags:
  - organization
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
# Circle (NYSE: CRCL)

## Executive Summary

USDC 的发行方，是 [[polymarket]] 等链上事件市场抵押品的信用来源之一。

与 [[tether]] 的差别在**透明度取向**：Circle 长期以更强的监管配合与储备披露作为差异化，而 Tether 以流通规模与新兴市场渗透见长。

## What It Actually Is | 它到底是什么

对事件市场，选 USDC 还是 USDT 作为抵押品是一个**风险取向的选择**，不是技术选择：

| | USDC | USDT |
|---|---|---|
| 储备披露 | 较频繁、较规范 | 长期争议焦点 |
| 监管定位 | 主动靠拢 | 相对疏离 |
| 流通规模 | 较小 | **最大** |
| 主要链分布 | 多链均衡 | **近半在单一链** |

**两者共有的性质**：**发行方都能冻结地址。** 这是稳定币抵押品与真正无许可资产的根本差别（见 [[stablecoin]]）。

**"钱锁在链上合约里"不等于"钱一定能动"** —— 这句话对两者都成立。

## How It Works | 运作方式

Circle 的模式与 Tether 相同（发行负债、持有储备、赚利差），差别在于它把**合规配合本身当作产品**：更规范的披露、更主动的立法参与、以及向机构销售的定位。

它也在推进自有的结算网络，把稳定币从"某条链上的代币"变成"自己的结算基础设施"——传统交易所巨头参与其中作为创始验证人（见 [[intercontinental-exchange]]）。

**这条线值得盯**：如果稳定币发行方自己变成结算层，事件市场的链选择逻辑会改变。

## Position in the Market | 它在市场里的位置

在事件市场，Circle 是**抵押品层的可选项之一**，但它的位置正在从"代币发行方"向"结算基础设施"移动。

**对用户的实际含义很直接**：你的事件合约抵押品是 USDC 还是 USDT，决定了你承担的是哪一家的储备风险、哪一套披露质量、以及哪一条链上的集中度（见 [[concentration-risk]]）。

**这是评估链上事件市场时最少被问、却最底层的一个问题。**

## What Could Break It | 什么会让它出问题

- **储备与利率敏感** —— 收入来自利差，利率下行直接影响盈利。
- **冻结能力** —— 与 Tether 同样具备。
- **银行合作方风险** —— 历史上曾因合作银行问题出现短暂脱锚。

## What To Watch | 该盯什么

- **各辖区稳定币立法的落地** —— 决定它能否成为受监管场馆的合规抵押品。
- **自有结算网络的采用情况。**
- **事件市场是否出现多稳定币抵押选项。**


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-infra-mm-stablecoins]])。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
