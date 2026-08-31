---
id: "moc:map-tron-htx-chainup"
type: moc
title: TRON / HTX / ChainUp Ecosystem
title_zh: TRON·HTX·ChainUp 生态
aliases: []
status: reviewed
importance: tier-1
domains:
  - crypto-market-structure
  - people-networks
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

# TRON / HTX / ChainUp 生态 (含 disputed 标注)

```mermaid
flowchart TD
    JS[Justin Sun] -->|"founded"| TR[TRON<br/>48.7% USDT·$2.1T/季]
    JS -.->|"advises (自述)<br/>own = DISPUTED (报道)"| HT[HTX]
    HT ---|"深绑 (part, HTX DAO)"| TR
    TR -->|infra| JL[JustLend<br/>Energy Rental] & SP[SunPump] & BT[BTTC]
    CLK[Chainlink] -->|"infra (2025-05 取代 WINkLink)"| TR
    WK[WINkLink 已废黜] -.->|"史 (ended)"| TR
    UK[UK/EU 制裁 2026] -.->|reg| HT
    DJ[杜均] -->|co-founded| CU[ChainUp<br/>Hermes 白标预测市场]
    DJ -->|"co-founded (史)"| HB[Huobi→HTX 前身]
    LL[Leon Li] -->|"founded (史)·2022 售出"| HB
    TT[Tether] -->|"结算共生 (infra)"| TR
```

三个要点: ① TRON 是 USDT 主轨但制裁暴露经 HTX 传导 (Binance 已切割 UK/EU HTX 交易); ② WINkLink 被自家生态废黜 = oracle 层无忠诚; ③ ChainUp 与 HTX 无直接股权证据 — 连接只在杜均的人脉层 (`emp/inv` 级, 非 `own`)。
