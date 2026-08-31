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

> 因果链 (workbook 学习地图原文骨架, 见 [[curriculum-source-map]]):
> **金融市场 → 交易所 → 微观结构 → 衍生品 → 区块链 → Crypto 市场结构 → 预测市场 → 机构风险** (→ 第 9 步: Event Risk Infrastructure 综合)
>
> 用法: 每阶段过四关 — ① 读概念页并答对 Active-Recall; ② 把该阶段「学习地图行」的四个问题 (钱在哪/谁担风险/怎么结算/必问问题) 脱稿讲一遍; ③ 做实战应用练习; ④ 完成判据自查通过 → 把该阶段概念页 status 升 reviewed。
> 每日入口: `make study` 生成 next-session; 队列看 [[study-queue]]。

## Stage 1 — Financial Markets 金融市场

- **前置**: 无。
- **概念**: [[financial-markets]] ⭐ · [[equity]] · [[debt]] · [[price-discovery]] ⭐ · [[broker]] · [[dealer]] · [[market-maker]] ⭐ · [[liquidity-provider]] · [[clearinghouse]] ⭐ · [[clearing]] · [[settlement]] ⭐ · [[order-flow]]
- **必读**: [[book-trading-and-exchanges|Harris《Trading and Exchanges》]] ch.1-3; CFTC LearnAndProtect derivatives basics (workbook 源 URL)。
- **练习**: 拿任意一条本周金融新闻, 指出: 谁在配置资本、谁在转移风险、结算走哪条轨。
- **实战应用**: 用一段话向机构解释「事件风险为什么属于金融市场而不是博彩」。
- **专家问题**: 为什么这个市场存在? 谁需要它? (学习地图 §1)
- **完成判据**: 能脱稿画出「资本 → 中介 → venue → 清算 → 结算」链并标出每环的钱与风险。

## Stage 2 — Exchanges 交易所

- **前置**: Stage 1。
- **概念**: [[exchange]] ⭐ · [[venue]] · [[centralized-exchange]] · [[decentralized-exchange]] · [[custody]] ⭐ · [[distribution]] ⭐ · [[exchange-vertical-integration]] · [[order-flow-network-effect]]
- **必读**: 生态版图 Exchange/Wallet/Custodian 行 ([[ecosystem-roles-map]]); Binance/OKX/Kalshi 实体页 (建成后)。
- **练习**: 对比 Kalshi (监管 CLOB) 与 Polymarket (hybrid 链上结算) 的「谁托管、谁是对手方、谁能冻结」。
- **实战应用**: 写出「场所中立的数据层」相对「自建交易场所」的三个理由。
- **专家问题**: 谁能交易? 谁托管? 谁是最终对手方? (学习地图 §2)
- **完成判据**: 给任一 venue 能在 5 分钟内讲清其市场模型/托管/结算/监管四件套。

## Stage 3 — Market Microstructure 微观结构

- **前置**: Stage 2。
- **概念**: [[order-book]] ⭐ · [[central-limit-order-book]] ⭐ · [[maker]] · [[taker]] · [[bid]] · [[ask]] · [[spread]] ⭐ · [[depth]] ⭐ · [[slippage]] ⭐ · [[price-impact]] · [[adverse-selection]] ⭐ · [[inventory-risk]] · [[execution-risk]] · [[automated-market-maker]] · [[request-for-quote]] · [[smart-order-routing]]
- **必读**: Harris ch.4-14 选读; Polymarket docs prices-orderbook (workbook 源 URL)。
- **练习**: 打开任一 Polymarket 盘口, 手算: $10k 买单的滑点、吃几档、冲击多远。
- **实战应用**: 解释为什么专业报价应给「liquidity-adjusted price」而不是 mid。
- **专家问题**: 我能以这个价格成交多少? 大单会把价格推多远? (学习地图 §3)
- **完成判据**: 能用 maker/taker/逆向选择三个词把「spread 为什么存在」讲给外行。

## Stage 4 — Derivatives 衍生品

- **前置**: Stage 3。
- **概念**: [[derivative]] ⭐ · [[underlying]] · [[forward-contract]] · [[futures-contract]] · [[option]] · [[call-option]] · [[put-option]] · [[binary-option]] ⭐ · [[swap]] · [[perpetual-futures]] · [[funding-rate]] · [[margin]] ⭐ · [[initial-margin]] · [[maintenance-margin]] · [[variation-margin]] · [[cross-margin]] ⭐ · [[portfolio-margin]] · [[collateral]] · [[leverage]] · [[liquidation]] · [[hedging]] ⭐ · [[basis-risk]] ⭐ · [[counterparty-risk]] ⭐ · [[value-at-risk]] · [[expected-shortfall]]
- **必读**: [[book-options-futures-hull|Hull《Options, Futures, and Other Derivatives》]] ch.1-5; CME futures 入门课 (workbook 源 URL)。
- **练习**: 把一张 event contract 摊开成 binary option 的 payoff 图; 标出它与真期权的法律分类差异。
- **实战应用**: 用 [[basis-risk]] 解释「Kalshi 与 Polymarket 同题合约为什么不是完美对冲」。
- **专家问题**: 我真正暴露于哪个 underlying? 最坏要付多少? (学习地图 §4)
- **完成判据**: 能给「事件合约 margin 化」(CFTC 2026 提案) 写出三条机构影响。

## Stage 5 — Blockchain 区块链

- **前置**: 无硬前置 (可与 4 并行)。
- **概念**: [[blockchain]] · [[ledger]] · [[transaction]] · [[block]] · [[consensus]] · [[double-spending]] · [[private-key]] · [[public-key]] · [[wallet]] · [[smart-contract]] · [[token]] · [[gas]] · [[proof-of-work]] · [[proof-of-stake]] · [[delegated-proof-of-stake]] · [[layer-1]] · [[layer-2]] · [[bridge]] · [[oracle]] ⭐ · [[ethereum-virtual-machine]] · [[erc-20]] · [[erc-721]] · [[erc-1155]] · [[on-chain]] · [[off-chain]] · [[hybrid-exchange-architecture]] · [[tron-bandwidth]] · [[tron-energy]]
- **必读**: TRON developers docs (workbook 源 URL); Polymarket CTF overview (ERC-1155 outcome tokens)。
- **练习**: 追一笔真实 Polygon 上的 USDC 转账: 从签名到 finality 每步谁在做什么。
- **实战应用**: 列出「读链但不上链」的三个理由 (速度/成本/审计的取舍)。
- **专家问题**: 哪些必须上链? 哪些链下更合理? 信任假设是什么? (学习地图 §5)
- **完成判据**: 能讲清 Polymarket 哪半在链上哪半在链下、为什么。

## Stage 6 — Crypto Market Structure 加密市场结构

- **前置**: Stage 2 + 5。
- **概念**: [[stablecoin]] ⭐ · [[custody]] · [[prime-brokerage]] · [[over-the-counter]] · [[settlement-rail]] ⭐ · [[token-economy]] · [[regulatory-access]] · [[know-your-transaction]] · [[data-infrastructure]] ⭐ · [[risk-engine]] ⭐ · [[policy-engine]] ⭐
- **必读**: 生态版图全部 13 行; Tether/Circle/TRON 实体页 (建成后)。
- **练习**: 画「stablecoin → chain → exchange → MM → OTC」资金环流图, 每条边标: 谁能冻结、结算多快。
- **实战应用**: 回答: event-market 资本以 USDC 结算, 必须监控哪三类 stablecoin 风险?
- **专家问题**: 钱在哪个平台? 能否自由转移? 谁能冻结? (学习地图 §6)
- **完成判据**: 能对任一大所讲出它的纵向一体化栈与其中的利益冲突。

## Stage 7 — Prediction & Outcome Markets 预测市场 (核心阶段)

- **前置**: Stage 3 + 4 + 6。
- **概念**: [[prediction-market]] ⭐ · [[outcome-market]] ⭐ · [[event-contract]] ⭐ · [[outcome-token]] ⭐ · [[implied-probability]] ⭐ · [[fully-collateralized-market]] ⭐ · [[resolution]] ⭐ · [[resolution-source]] ⭐ · [[settlement-methodology]] · [[oracle-risk]] ⭐ · [[dispute-mechanism]] ⭐ · [[resolution-risk]] ⭐ · [[contract-semantics]] ⭐ · [[contract-equivalence]] ⭐ · [[canonical-event-id]] ⭐ · [[multi-outcome-market]] · [[scalar-market]] · [[combinatorial-market]] · [[resolution-insurance]] ⭐ · [[market-integrity]] ⭐ · [[inside-information]] ⭐ · [[market-maker-incentive]] · [[event-risk]] ⭐ · [[event-var]] ⭐
- **必读**: CFTC PredictionMarkets 专页 + 2026 提案 (workbook 源 URL); Polymarket resolution docs; UMA 机制文档。
- **练习**: 找一对跨 venue 同题合约, 逐层过 [[settlement-methodology]] 四层清单, 写出等价性判决。
- **实战应用**: 从争议历史库口径 (123k 请求/957 争议/7.12% 改判) 推一条产品含义。
- **专家问题**: 这个 contract 到底承诺什么? 谁决定事实? (学习地图 §7)
- **完成判据**: 能независ— 能独立完成一份 contract equivalence 判决书并让 Irene 挑不出漏项。

## Stage 8 — Institutional Risk 机构风险

- **前置**: Stage 4 + 7。
- **概念**: [[market-risk]] · [[liquidity-risk]] ⭐ · [[credit-risk]] · [[counterparty-risk]] · [[settlement-risk]] · [[operational-risk]] · [[model-risk]] · [[concentration-risk]] ⭐ · [[regulatory-risk]] ⭐ · [[anti-money-laundering]] · [[know-your-customer]] · [[jurisdiction]] ⭐ · [[custody-segregation]] · [[capital-requirements]] · [[auditability]]
- **必读**: 机构对话速查 5 行 ([[institutional-conversation-cheatsheet]])。
- **练习**: 给一个假想基金的 event 持仓做风险清单: 按 8 类风险各写一条具体败法。
- **实战应用**: 把 [[event-var]] 讲成 CRO 听得懂的一段话。
- **专家问题**: 看对方向以后, 还有什么能让我拿不到钱或被迫退出? (学习地图 §8)
- **完成判据**: 能用 5 分钟给 CRO 讲完「event exposure 为什么是你的盲区」。

## Stage 9 (综合) — Event Risk Infrastructure

Stage 7+8 的综合: 读 event-risk-infrastructure · settlement-intelligence · friction-not-prediction 三命题, 对每条能复述: 主张 / 已证据 / 反证据 / 证伪条件 / 最小验证。**完成判据 = 能主持一场与 MM 的 design-partner 对话而不需要小抄。**
