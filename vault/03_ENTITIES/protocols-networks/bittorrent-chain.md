---
id: "protocol:bittorrent-chain"
type: protocol-network
title: BTTC
title_zh: BitTorrent Chain
title_en: BTTC
aliases:
  - BTTC
  - BitTorrent Chain
status: reviewed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
tags:
  - protocol-network
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
  - "source:2026-08-26-bittorrent-chain-bittorrent-chainwhitepaper-en-pdf"
related:
  - id: "protocol:tron"
    rel: integrates-with
    note: 跨链/执行基础设施, 连接 TRON 与其他生态
  - id: "protocol:ethereum"
    rel: integrates-with
    note: 同上
  - id: "protocol:bnb-chain"
    rel: integrates-with
    note: 同上
prerequisites: []
import_origin: xlsx-learning-map
import_category: TRON生态
---
# BTTC | BitTorrent Chain

## Executive Summary

多链资产与消息互通的跨链基础设施，连接 [[tron]]、[[ethereum]]、[[bnb-chain]] 等生态。

BitTorrent Chain 的相关风险主要来自跨链桥（见 [[bridge]]）；跨链事件市场的资金进出依赖这类桥接设施。

## What It Actually Is | 它到底是什么

跨链设施做的事是"锁定 + 铸造"，不是真正的转移：

```
原链锁定资产 → 目标链铸造凭证 → 你持有的是欠条
```

**它的安全性取决于谁掌握锁定与铸造的权限** —— 通常是一组验证者或多签，**其安全预算往往远低于它连接的任何一条链**。

**判断任何一座桥，核心只有一问**：要偷走里面的钱，需要攻破什么？

## How It Works | 运作方式

跨链设施的价值主张是**流动性统一**：让资产在多个生态间自由流动。

**对事件市场的具体含义**：如果一个事件市场部署在多条链上（见 [[bnb-chain]] 与 [[polygon]] 的双轨格局），那么跨链能力决定了流动性能否被合并 —— **否则同一个事件在不同链上就是两个互不相通的盘口**（见 [[liquidity]]）。

**但合并流动性的代价，是把桥的风险引入结算路径。**

## Position in the Market | 它在市场里的位置

在事件市场的基础设施图谱上，跨链层是一个**必要但危险**的环节。

目前主流事件市场都是单链结算，因此桥的风险主要出现在**用户资金进出**这一段，而不在结算本身。

**若未来出现跨链的事件市场，桥就会从"路径风险"升级为"结算风险"** —— 那是一个数量级的变化。

## What Could Break It | 什么会让它出问题

- **桥是历史上最集中的攻击面。**
- **凭证无锚风险** —— 原链资产被盗后，目标链的凭证失去支撑。
- **验证者集中度。**

## What To Watch | 该盯什么

- **是否出现跨链结算的事件市场** —— 那会显著改变风险画像。
- **主要桥的安全模型演进**（多签 → 轻客户端/证明）。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
- [[src-2026-08-26-bittorrent-chain-bittorrent-chainwhitepaper-en-pdf]] — <https://bt.io/doc/BitTorrent-ChainWhitepaper_EN.pdf>
