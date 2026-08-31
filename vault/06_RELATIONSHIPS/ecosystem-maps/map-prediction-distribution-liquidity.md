---
id: "moc:map-prediction-distribution-liquidity"
type: moc
title: Prediction Market Distribution & Liquidity
title_zh: 预测市场分发与底层流动性
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

# 预测市场: 谁拥有用户, 谁供流动性 (2026-08)

```mermaid
flowchart TD
    subgraph 分发层
    RH[Robinhood/Webull<br/>券商] ; BW[Binance Wallet 2亿] ; CT[Cantor→3000 机构] ; MD[CNN/CNBC/Fox 内容]
    end
    subgraph Venue
    K[Kalshi] ; P[Polymarket] ; PF[Predict.fun] ; H4[HIP-4]
    end
    subgraph 流动性层
    SIG[SIG] ; WM[Wintermute] ; DRW[DRW desk] ; KT[Kalshi Trading 自营 MM] ; LP32[~32 小 LP]
    end
    RH -->|"part (SEC filing 实证)"| K
    CT -->|part| K
    MD -->|part| K
    BW -->|part| PF
    SIG -->|liq| K
    KT -->|"liq (own!)"| K
    WM -->|liq| K & P
    DRW -->|"liq (desk 报道)"| K & P
    LP32 -->|"liq (中位 400bps)"| P
```

**结构判断**: 分发被传统入口 (券商/钱包/投行/媒体) 快速接管, 流动性专业化刚开始 (Polymarket 中位报价仍 400bps) — 需求主流化 × 流动性早期 = MM 工具需求的窗口期 (Wintermute 自己的原话)。**venue 自营 MM (Kalshi Trading) 的利益冲突**已被集体诉讼点名 — market-integrity 情报的现成议题。
