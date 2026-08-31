---
id: "moc:map-event-risk-cross-asset"
type: moc
title: Event Risk → Cross-Asset Portfolio Map
title_zh: 事件风险跨资产传导图
aliases: []
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
  - institutional-risk
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

# 事件风险 → 跨资产组合传导

```mermaid
flowchart TD
    EV[单一事件<br/>例: Fed 意外加息 / 选举翻盘 / 制裁令] --> EC[事件合约价格<br/>P: 0→1 跳变]
    EV --> RT[利率/债市<br/>期货·掉期重定价]
    EV --> EQ[股票<br/>板块β + 个股暴露]
    EV --> CR[Crypto<br/>BTC/ETH + 清算连锁]
    EV --> FX[汇率]
    EC -.->|"同一 underlying 的<br/>不同 venue 合约 (basis)"| EC2[跨 venue 等价合约]
    CR --> LQ[连锁清算<br/>实证: 2025-10-10 风暴, Hyperliquid $10B/日清算]
    RT & EQ & CR & FX --> PF[组合 P&L]
    EC --> PF
```

组合级问题 (机构对话速查 §8): 「看对方向以后, 还有什么让我拿不到钱?」— 答案沿三轴: [[basis-risk]] (等价性) · [[liquidity-risk]] (退出深度) · [[settlement-risk]] (裁决与支付)。

**Event VaR 的构造** ([[event-var]]): 把同一 [[canonical-event-id]] 下的全部头寸 (事件合约 + 相关资产) 映射到共同情景; 条件市场价差 P(B|A)−P(B) 是市场自己报出的传导系数 ([[combinatorial-market]])。2025-10-10 清算风暴与 2026 世界杯脉冲是现成的校准样本。
