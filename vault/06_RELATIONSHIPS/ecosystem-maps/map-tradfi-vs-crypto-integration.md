---
id: "moc:map-tradfi-vs-crypto-integration"
type: moc
title: TradFi vs Crypto Vertical Integration
title_zh: 传统金融 vs Crypto 纵向一体化
aliases: []
status: reviewed
importance: tier-1
domains:
  - crypto-market-structure
tags:
  - moc
  - ecosystem-map
created: 2026-08-27
updated: 2026-08-27
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related: []
---

> **边类型图例** (受控词表 [[relationship-types]]): `own` 所有权 · `emp` 雇佣史 · `inv` 投资 · `part` 合作 · `integ` 集成 · `liq` 流动性 · `infra` 基础设施依赖 · `comp` 竞争 · `reg` 监管 · `inf` 推断 (标注) · `?` unknown。**无标签的线不允许存在。**

# 传统金融 vs Crypto 纵向一体化 (2026 快照)

| 功能 | TradFi (强制分离) | Crypto (自然全栈) | 2026 融合动作 |
|---|---|---|---|
| 交易 | NYSE/CME | CEX 自营撮合 | ICE→inv→Polymarket+OKX(单源); Cantor 分发 Kalshi |
| 清算 | 独立 CCP (CME Clearing) | 交易所内部 / Kalshi Klear 自有 DCO | CFTC ANPRM 问事件合约 margin/清算 |
| 托管 | 独立托管行 | 交易所自托管 / Fireblocks | Circle OCC 信托银行; Anchorage 发 USA₮ |
| 结算货币 | 央行货币 | USDT/USDC/USDH | GENIUS Act 双轨制 (USA₮) |
| 数据/指数 | Bloomberg/S&P (独立) | venue 自报 (利益冲突) | **空位** |
| 风控 | 独立 (Barra/RiskMetrics) | venue margin engine | **空位** |

**结构论点** (inference): TradFi 的分离是监管强制的信任分工; crypto 正被拉向同一形态 (清算/托管/稳定币逐件被拆出去持牌)。**数据与风控的独立化是下一件** — 这就是 BLUEPRINT 的彭博/晨星位。反向融合同样在发生: ICE/Cantor/Morgan Stanley 系资本进 venue 层。
