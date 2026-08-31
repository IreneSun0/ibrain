---
id: "report:ecosystem-roles-map"
type: report
title: Ecosystem Roles Map (workbook)
title_zh: 生态游戏版图 · workbook 原文
aliases: []
status: seed
importance: tier-1
domains:
  - industry-strategy
  - crypto-market-structure
tags:
  - xlsx-import
created: 2026-08-26
updated: 2026-08-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related: []
import_origin: xlsx-learning-map
---

# 生态游戏版图 · workbook 原文

> 13 个生态角色: 钱在哪、最怕什么、怎么结算、以及一个中立数据层应当如何与其相处。

| 角色 | 游戏比喻 | 现实中做什么 | 钱在哪里 | 最怕什么 | 典型例子 |
|---|---|---|---|---|---|---|
| Stablecoin issuer | 铸造全城通用金币的央行/钱庄 | 发行和赎回稳定币、管理储备 | 稳定币储备与流通量 | depeg、挤兑、监管、储备问题 | Tether/Circle | 作为现金与collateral风险输入，不必自己发行 |
| Blockchain / L1 | 城市道路+公共总账 | 记录所有权、执行交易和合约 | native token/staked capital | 拥堵、攻击、治理、finality | Ethereum/TRON/Hyperliquid | 读取结算与链状态，做chain risk |
| Wallet | 钥匙包+银行App+App Store入口 | 管理key、账户、签名、发现和分发金融应用 | 用户资产控制权/订单入口 | key安全、恶意签名、distribution lock-in | OKX Wallet/Bitget Wallet | 嵌入式risk API优于和wallet抢用户 |
| Exchange / Venue | 中央交易市场/拍卖行 | 列出产品、撮合订单、管理规则和市场 | 订单流、手续费、collateral（视架构） | 流动性、系统、监管、托管 | Binance/OKX/Kalshi/Polymarket | venue-neutral risk/semantics layer |
| Market Maker | 随时开门收货和卖货的批发商 | 持续双边报价、用资本吸收订单并对冲 | inventory/credit/collateral | adverse selection、库存、gap、counterparty | Wintermute/GSR | 优先做design partner；他们最能指出真实风险痛点 |
| Broker / Prime Broker | 帮大客户进各个市场的总管家 | 准入、路由、融资、信用、净额和机构工作流 | 客户资金、credit lines | counterparty、settlement、credit | FalconX/传统prime brokers | 潜在渠道和高价值买家 |
| Oracle / Resolution | 裁判+官方记分牌 | 把外部事实/价格输入合约并决定结果 | bond/incentives（视机制） | 错误、操纵、来源冲突、治理争议 | UMA/WINkLink/validator votes | 独立监控其证据与状态 |
| Clearinghouse | 全城统一结账与违约消防队 | 净额、保证金、保证履约、处理违约 | default fund/margin | 极端行情、模型失效、member default | CME Clearing | 可消费 event-risk 输入用于 margin/cross-margin |
| Custodian | 金库 | 保管资产和密钥、权限控制 | 客户资产 | hack、内部控制、破产、混同 | 合规托管商 | 初期不要承担custody风险 |
| Quant Fund | 有算法和资本的职业战队 | 把模型、数据、执行和风险预算变成收益 | fund NAV/collateral | model/execution/drawdown/correlation | systematic funds | 需要可集成 API 而非漂亮 dashboard |
| Regulator | 城规+警察+法院 | 决定谁能做什么、监督公平和稳定、执法 | 无交易资金；控制准入和规则 | 系统性风险、欺诈、消费者/市场损害 | CFTC/MAS | 监管元数据与可审计性是价值所在 |
| Data / Risk Provider | 雷达站+地图+情报中心 | 把跨市场原始数据变成可比较、可审计、可决策的信号 | 订阅/API/机构合同 | 数据错、模型错、缺信任与distribution | Bloomberg/Chainalysis/Barra式角色 | 中立数据层最值得争夺的位置 |

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]]

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 原文导入。
