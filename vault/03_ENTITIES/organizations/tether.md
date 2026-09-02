---
id: "org:tether"
type: organization
title: Tether
title_zh: Tether (USDT 发行方)
aliases:
  - USDT 发行方
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
related:
  - id: "protocol:tron"
    rel: settles-on
    note: TRON 承载约 48.67% 流通 USDT (~$89.7B, 2026-07)
---
# Tether

## Executive Summary

全球流通量最大的稳定币 USDT 的发行方。它在事件市场里的角色不是参与者，而是**抵押品本身的信用来源**。

关键事实：**TRON 承载约 48.67% 的流通 USDT（约 $897 亿，2026-07）**，季度结算规模以万亿计 —— 这让 [[tron]] 成为稳定币最主要的结算轨道之一（见 [[trc-20]]）。

## What It Actually Is | 它到底是什么

事件市场用稳定币计价与抵押，这意味着**每一个头寸背后都叠加了一层发行方风险**：

```
你的事件合约头寸
  └─ 抵押品是 USDT
       └─ USDT 的价值取决于 Tether 的储备与兑付能力
            └─ 且 Tether 可以冻结特定地址
```

**最后一行常被忽略**：稳定币发行方保留冻结地址的能力。这意味着"资金锁在链上合约里、平台无法挪用"这句话**并不完整** —— 发行方仍可以让那笔钱不可用（见 [[stablecoin]]）。

**全额抵押消除了平台风险，没有消除发行方风险。**

## How It Works | 运作方式

Tether 的模式是**发行负债、持有储备、赚取利差**：用户交来美元，它买短期国债等资产，利息归它。

**这个模式在高利率环境下极其赚钱**，也决定了它的风险形态：
- 不是信用风险（储备是国债类资产）；
- 而是**兑付与集中度风险**（挤兑时的流动性、以及储备构成的透明度）。

**对事件市场的含义**：你的抵押品的安全性，最终取决于一个非银行机构的资产负债表 —— 而那张表的审计透明度长期是争议焦点。

## Position in the Market | 它在市场里的位置

在事件市场的价值链里，Tether 处在**最底层却最少被评估**的位置。

评估一个事件市场平台时，大家会问撮合、托管、裁决、监管，**很少有人问"抵押品的发行方是谁、它的储备如何"** —— 而那是所有头寸的共同底座。

**这也是一个集中度问题**：如果一个组合里所有事件头寸都以同一种稳定币计价，那么发行方风险是 100% 集中的（见 [[concentration-risk]]）。

## What Could Break It | 什么会让它出问题

- **储备透明度** —— 长期争议焦点。
- **冻结能力** —— 发行方可使特定地址的资金不可用。
- **监管压力** —— 各辖区的稳定币立法会改变其运营条件。
- **链集中度** —— 近半流通量在单一链上（见 [[delegated-proof-of-stake]] 的验证者集中度问题）。

## What To Watch | 该盯什么

- **储备构成与审计报告的频率与质量。**
- **各主要辖区稳定币立法的落地** —— 会直接影响它能在哪里被用作抵押品。
- **事件市场是否出现多稳定币抵押** —— 那是降低这层集中度的唯一实际手段。
