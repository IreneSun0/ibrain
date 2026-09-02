---
id: "mmf:jane-street"
type: market-maker-fund
title: Jane Street
title_zh: Jane Street
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - financial-markets
  - crypto-market-structure
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
# Jane Street

## Executive Summary

全球顶级量化做市商之一，加密领域最著名的传统金融参与者。它是 BlackRock 比特币 ETF（IBIT）的原始授权参与者（AP）之一。

**但在事件市场上，截至 2026-08 的专项检索找不到它的任何公开记录** —— 这个空白本身是信息：最有能力做市的机构之一还没有公开进场。

## What It Actually Is | 它到底是什么

Jane Street 是**纯交易公司**：不建协议、不做托管、不发产品，只做市与自营。

它的核心能力恰好是事件合约最需要的：
- 极强的**离散支付定价**能力（期权与结构化产品出身）；
- 跨市场对冲与库存管理（见 [[inventory-risk]]）；
- 巨大的资本承受力。

**它没有进场，说明的不是能力问题，而是这个市场目前不满足它的进场条件** —— 规模、合规确定性、以及可对冲性（见 [[contract-equivalence]]）。

## How It Works | 运作方式

传统做市巨头进入一个新市场，通常要三个条件同时成立：

| 条件 | 事件市场现状 |
|---|---|
| 规模足够摊薄固定成本 | **接近但仍偏小** |
| 监管地位清晰 | **正在成型**（州诉讼未决） |
| 头寸可对冲 | **不成立**（跨场所语义不等价） |

**第三行是最硬的门槛**：一家纯做市公司不会长期持有无法对冲的方向性敞口（见 [[dealer]]）。

**所以"Jane Street 什么时候进场"是一个有信息量的指标** —— 它进场意味着上面三个条件同时被满足了。

## Position in the Market | 它在市场里的位置

在事件市场的地图上，Jane Street 目前是一个**空位**。

对比：[[susquehanna]] 已是 [[kalshi]] 的旗舰做市商，[[wintermute]] 服务 [[polymarket]]，[[cumberland-drw]] 被报道正在建台。**Jane Street 的缺席在这一组里格外显眼。**

它的诉讼记录（印度 SEBI 案、Terraform 清算管理人指控）也提示：这类机构对新市场的监管不确定性极度敏感。

## What Could Break It | 什么会让它出问题

对**这个市场**而言，风险不是 Jane Street 出问题，而是它**继续不来**：

- 缺少最顶级的做市能力 → 价差与深度长期低于传统市场水平；
- 机构资金因此更难进场（见 [[regulatory-access]]）。

**做市能力的缺席，最终以更差的价格由每一个用户承担**（见 [[adverse-selection]]）。

## What To Watch | 该盯什么

- **是否公开出现在任何持牌事件交易所的做市商名单里** —— 这是最直接的信号。
- **是否招聘事件合约相关岗位。**
- **它对可对冲性的表态** —— 一家纯做市公司公开谈论某个市场的对冲工具，通常是进场的前奏。
