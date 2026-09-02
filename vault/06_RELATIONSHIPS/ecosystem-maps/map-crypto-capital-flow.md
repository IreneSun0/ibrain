---
id: "moc:map-crypto-capital-flow"
type: moc
title: Crypto Capital Flow
title_zh: 加密资本流 (stablecoin→chain→exchange→MM→OTC)
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

# 加密资本流: Stablecoin → Chain → Exchange → MM → OTC

```mermaid
flowchart LR
    F[法币/银行] -->|"铸造 (integ)"| T[Tether USDT $189B<br/>Circle USDC $73B]
    T -->|"结算轨 (infra)"| CH[TRON 48.7% USDT · $2.1T/季<br/>Ethereum/Polygon/Solana/Arc]
    CH -->|"充值 (infra)"| EX[CEX: Binance/OKX/Bybit/Bitget/HTX<br/>DEX: Hyperliquid/Uniswap]
    MM[做市商 Wintermute/GSR/SIG] -->|"liq"| EX
    EX -->|"大额外溢 (liq)"| OTC[OTC/Prime: Cumberland/B2C2/FalconX]
    OTC -->|"信用+净额 (infra)"| INST[机构资金]
    EV[事件市场 Polymarket/Kalshi] -->|"USDC/USD 抵押 (infra)"| CH
    MM -->|"liq (2026 起)"| EV
```

关键实测数字 (2026-08 核验): USDT $189B (TRON 占 48.67%) · USDC $73.3B · 事件市场月成交 $44.8B。冻结权/挤兑风险沿 T→CH→EX 每一跳都在: 见 [[stablecoin]] / [[settlement-rail]] / [[custody]]。

