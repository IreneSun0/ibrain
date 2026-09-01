---
id: "curr:main-curriculum"
type: curriculum
title: Prediction Market Industry Curriculum
title_zh: 行业主课程 · 8 阶段
aliases:
  - curriculum
  - 主课程
status: reviewed
importance: tier-1
domains:
  - learning
tags:
  - curriculum
created: 2026-08-26
updated: 2026-08-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related: []
---

# 行业主课程 · 8 阶段

> 阅读顺序（每一阶段是下一阶段的前置，见 [[curriculum-source-map]]）：
> **金融市场 → 交易所 → 微观结构 → 衍生品 → 区块链 → Crypto 市场结构 → 预测市场 → 机构风险** (→ 第 9 步: Event Risk Infrastructure 综合)
>
> 读法: 每个阶段都能用同样四个问题检验是否读懂 —— 钱在哪里、谁承担风险、怎么结算、该问什么。四个都答得上来，再进下一阶段。

## Stage 1 — Financial Markets 金融市场

- **前置**: 无。
- **概念**: [[financial-markets]] ⭐ · [[equity]] · [[debt]] · [[price-discovery]] ⭐ · [[broker]] · [[dealer]] · [[market-maker]] ⭐ · [[liquidity-provider]] · [[clearinghouse]] ⭐ · [[clearing]] · [[settlement]] ⭐ · [[order-flow]]
- **必读**: [[book-trading-and-exchanges|Harris《Trading and Exchanges》]] ch.1-3; CFTC LearnAndProtect derivatives basics (workbook 源 URL)。
- **专家问题**: 为什么这个市场存在? 谁需要它? (学习地图 §1)

## Stage 2 — Exchanges 交易所

- **前置**: Stage 1。
- **概念**: [[exchange]] ⭐ · [[venue]] · [[centralized-exchange]] · [[decentralized-exchange]] · [[custody]] ⭐ · [[distribution]] ⭐ · [[exchange-vertical-integration]] · [[order-flow-network-effect]]
- **必读**: 生态版图 Exchange/Wallet/Custodian 行 ([[ecosystem-roles-map]]); Binance/OKX/Kalshi 实体页 (建成后)。
- **专家问题**: 谁能交易? 谁托管? 谁是最终对手方? (学习地图 §2)

## Stage 3 — Market Microstructure 微观结构

- **前置**: Stage 2。
- **概念**: [[order-book]] ⭐ · [[central-limit-order-book]] ⭐ · [[maker]] · [[taker]] · [[bid]] · [[ask]] · [[spread]] ⭐ · [[depth]] ⭐ · [[slippage]] ⭐ · [[price-impact]] · [[adverse-selection]] ⭐ · [[inventory-risk]] · [[execution-risk]] · [[automated-market-maker]] · [[request-for-quote]] · [[smart-order-routing]]
- **必读**: Harris ch.4-14 选读; Polymarket docs prices-orderbook (workbook 源 URL)。
- **专家问题**: 我能以这个价格成交多少? 大单会把价格推多远? (学习地图 §3)

## Stage 4 — Derivatives 衍生品

- **前置**: Stage 3。
- **概念**: [[derivative]] ⭐ · [[underlying]] · [[forward-contract]] · [[futures-contract]] · [[option]] · [[call-option]] · [[put-option]] · [[binary-option]] ⭐ · [[swap]] · [[perpetual-futures]] · [[funding-rate]] · [[margin]] ⭐ · [[initial-margin]] · [[maintenance-margin]] · [[variation-margin]] · [[cross-margin]] ⭐ · [[portfolio-margin]] · [[collateral]] · [[leverage]] · [[liquidation]] · [[hedging]] ⭐ · [[basis-risk]] ⭐ · [[counterparty-risk]] ⭐ · [[value-at-risk]] · [[expected-shortfall]]
- **必读**: [[book-options-futures-hull|Hull《Options, Futures, and Other Derivatives》]] ch.1-5; CME futures 入门课 (workbook 源 URL)。
- **专家问题**: 我真正暴露于哪个 underlying? 最坏要付多少? (学习地图 §4)

## Stage 5 — Blockchain 区块链

- **前置**: 无硬前置 (可与 4 并行)。
- **概念**: [[blockchain]] · [[ledger]] · [[transaction]] · [[block]] · [[consensus]] · [[double-spending]] · [[private-key]] · [[public-key]] · [[wallet]] · [[smart-contract]] · [[token]] · [[gas]] · [[proof-of-work]] · [[proof-of-stake]] · [[delegated-proof-of-stake]] · [[layer-1]] · [[layer-2]] · [[bridge]] · [[oracle]] ⭐ · [[ethereum-virtual-machine]] · [[erc-20]] · [[erc-721]] · [[erc-1155]] · [[on-chain]] · [[off-chain]] · [[hybrid-exchange-architecture]] · [[tron-bandwidth]] · [[tron-energy]]
- **必读**: TRON developers docs (workbook 源 URL); Polymarket CTF overview (ERC-1155 outcome tokens)。
- **专家问题**: 哪些必须上链? 哪些链下更合理? 信任假设是什么? (学习地图 §5)

## Stage 6 — Crypto Market Structure 加密市场结构

- **前置**: Stage 2 + 5。
- **概念**: [[stablecoin]] ⭐ · [[custody]] · [[prime-brokerage]] · [[over-the-counter]] · [[settlement-rail]] ⭐ · [[token-economy]] · [[regulatory-access]] · [[know-your-transaction]] · [[data-infrastructure]] ⭐ · [[risk-engine]] ⭐ · [[policy-engine]] ⭐
- **必读**: 生态版图全部 13 行; Tether/Circle/TRON 实体页 (建成后)。
- **专家问题**: 钱在哪个平台? 能否自由转移? 谁能冻结? (学习地图 §6)

## Stage 7 — Prediction & Outcome Markets 预测市场

- **前置**: Stage 3 + 4 + 6。
- **概念**: [[prediction-market]] ⭐ · [[outcome-market]] ⭐ · [[event-contract]] ⭐ · [[outcome-token]] ⭐ · [[implied-probability]] ⭐ · [[fully-collateralized-market]] ⭐ · [[resolution]] ⭐ · [[resolution-source]] ⭐ · [[settlement-methodology]] · [[oracle-risk]] ⭐ · [[dispute-mechanism]] ⭐ · [[resolution-risk]] ⭐ · [[contract-semantics]] ⭐ · [[contract-equivalence]] ⭐ · [[canonical-event-id]] ⭐ · [[multi-outcome-market]] · [[scalar-market]] · [[combinatorial-market]] · [[resolution-insurance]] ⭐ · [[market-integrity]] ⭐ · [[inside-information]] ⭐ · [[market-maker-incentive]] · [[event-risk]] ⭐ · [[event-var]] ⭐
- **必读**: CFTC PredictionMarkets 专页 + 2026 提案 (workbook 源 URL); Polymarket resolution docs; UMA 机制文档。
- **专家问题**: 这个 contract 到底承诺什么? 谁决定事实? (学习地图 §7)

## Stage 8 — Institutional Risk 机构风险

- **前置**: Stage 4 + 7。
- **概念**: [[market-risk]] · [[liquidity-risk]] ⭐ · [[credit-risk]] · [[counterparty-risk]] · [[settlement-risk]] · [[operational-risk]] · [[model-risk]] · [[concentration-risk]] ⭐ · [[regulatory-risk]] ⭐ · [[anti-money-laundering]] · [[know-your-customer]] · [[jurisdiction]] ⭐ · [[custody-segregation]] · [[capital-requirements]] · [[auditability]]
- **必读**: 机构对话速查 5 行 ([[institutional-conversation-cheatsheet]])。
- **专家问题**: 看对方向以后, 还有什么能让我拿不到钱或被迫退出? (学习地图 §8)

## Stage 9（综合）— Event Risk Infrastructure

前八个阶段各自回答一个局部问题；第九步是把它们接起来：**一笔事件敞口从下单到拿到钱，中间有多少环可能让你拿不到？**

按顺序重读这四页即可完成综合：[[event-risk]]、[[resolution-risk]]、[[contract-equivalence]]、[[event-var]] —— 它们分别对应敞口的产生、判定的失效、跨场所的不可比、以及组合层的度量。
