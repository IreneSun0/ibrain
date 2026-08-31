---
id: "moc:map-prediction-value-chain"
type: moc
title: Prediction Market Value Chain
title_zh: 预测市场价值链
aliases: []
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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

# 预测市场价值链 (2026-08 实测版)

```mermaid
flowchart LR
    E[事件发生] --> SRC[Resolution Source<br/>官方数据/指定来源]
    SRC -->|"infra"| OR[裁决层<br/>UMA投票 · Kalshi内部 · Chainlink自动 · HIP-4 mark price]
    OR -->|"infra"| VN[Venue<br/>Polymarket · Kalshi · Predict.fun · HIP-4 · Opinion]
    LQ[MM: SIG/Wintermute/DRW/32 小LP] -->|"liq"| VN
    VN -->|"分发 (part)"| DIST[分发层<br/>Robinhood/Webull · Binance Wallet · Cantor机构通道 · CNN/Fox内容]
    DIST --> RU[零售 & 机构用户]
    WL[白标供给 ChainUp Hermes] -->|"infra"| VN
    RG[CFTC/州/各国] -.->|"reg"| VN
```

链上每环的抽水与风险: venue 抽 taker 费 (Polymarket 2026 费率表 / Kalshi 费) · 裁决层出 [[resolution-risk]] (三连争议+Khamenei) · 分发层拿用户 (Robinhood 依赖 Kalshi = SEC filing 实证)。

