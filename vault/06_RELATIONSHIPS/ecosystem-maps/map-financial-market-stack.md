---
id: "moc:map-financial-market-stack"
type: moc
title: Financial Market Stack
title_zh: 金融市场栈
aliases: []
status: reviewed
importance: tier-1
domains:
  - financial-markets
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

# 金融市场栈 (谁在哪一层, 钱怎么沉淀)

```mermaid
flowchart TD
    U[资本所有者: 投资者/企业/基金 LP] -->|"配置资本 (own)"| B[Broker / Prime Broker<br/>准入·路由·信用]
    B -->|"订单流 (infra)"| V[Exchange / Venue<br/>规则·撮合·行情]
    D[Dealer / Market Maker<br/>自有资本双边报价] -->|"流动性 (liq)"| V
    V -->|"成交 (infra)"| C[Clearinghouse CCP<br/>novation·保证金·违约瀑布]
    C -->|"净额义务 (infra)"| S[Settlement 层<br/>CSD·银行·链]
    R[Regulator] -.->|"reg"| V & C & B
    O[Oracle/数据层] -.->|"事实输入 (infra)"| V
```

每层的钱与最怕: 见 [[ecosystem-roles-map]] (workbook 原文 13 角色表)。概念链: [[financial-markets]] → [[exchange]] → [[clearinghouse]] → [[settlement]]。

