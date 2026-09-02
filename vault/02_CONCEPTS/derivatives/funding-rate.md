---
id: "concept:funding-rate"
type: concept
title: Funding Rate
title_zh: 资金费率
title_en: Funding Rate
aliases:
  - 资金费率
status: reviewed
importance: tier-2
domains:
  - derivatives
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "concept:perpetual-futures"
    rel: mechanism-of
    note: "多空定期互付, 把 perp 价格拉回现货"
prerequisites:
  - "concept:perpetual-futures"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Funding Rate | 资金费率

## Executive Definition / Chinese Explanation | 定义与解释

**Funding Rate | 资金费率** = 永续合约里多空之间的周期性转移支付，用来把永续价格拉回现货。

它不是手续费 —— **平台通常不抽成**，钱是从一方直接流到另一方。它是[[perpetual-futures|永续合约]]用来替代交割日的锚定机制。

## Why This Matters | 为什么重要

资金费率是**加密市场最直接的情绪指标**：它是市场愿意为持有某个方向付多少钱。

长期为正 = 多头拥挤，愿意付钱维持仓位；长期为负 = 空头拥挤。这比任何"看涨看跌指数"都硬，因为它是**用真金白银投出来的**。

对事件市场，它提供一个对照：**事件合约没有资金费率，但有资金占用的机会成本** —— 两者都在给"持有时间"定价，只是一个显性、一个隐性。

## How It Works | 机制怎么运转

```
若 永续价 > 现货价  → 多头付空头  → 抑制做多
若 永续价 < 现货价  → 空头付多头  → 抑制做空
```

每 8 小时（各平台不同）结算一次。费率通常由两部分构成：

1. **溢价指数** —— 永续价与现货价的偏离。
2. **利率项** —— 一个基准利率差，通常固定且很小。

**这个设计不需要交割就能自我锚定** —— 代价是持有成本不确定：它取决于市场情绪，而不是一个事先已知的利率。

## Concrete Example | 具体例子

三种市场状态下的资金费率读数：

| 状态 | 费率 | 含义 | 30 天持有 $100k 的成本 |
|---|---|---|---|
| 平静 | ±0.005% / 8h | 供需平衡 | ±$450 |
| 牛市拥挤 | +0.05% / 8h | 多头愿付高价 | **$4,500** |
| 极端挤压 | +0.3% / 8h | 强制平仓边缘 | **$27,000** |

**第三行是关键**：年化持有成本超过 300%。在那种状态下，**即使方向判断完全正确，持有成本也可能吃掉全部利润。**

这就是为什么专业玩家把资金费率算进策略，而不是当成噪声。

## Common Misconceptions | 常见误解

- **误解一："资金费率是平台的收入。"** 通常是多空之间的转移，平台不抽成。
- **误解二："费率低就说明市场健康。"** 也可能是流动性太差、没人愿意套利。要结合深度一起看。
- **误解三："资金费率只影响永续。"** 它是跨市场的信号：极端费率往往预示强制平仓潮，会传导到现货和相关衍生品。

## In Practice | 实战里怎么用

把资金费率当成两件事用：

**一是成本项** —— 写进持仓成本模型：
```
持有总成本 = 手续费 + 滑点 + Σ(费率 × 名义 × 周期数)
```

**二是仓位信号** —— 极端费率意味着一侧拥挤，反转风险上升。

跨市场比较时，可以把事件合约全额抵押的机会成本（`本金 × 无风险利率 × 期限`）折算到与永续费率相同的时间尺度。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 资金费率的作用是什么？它是平台收入吗？
  A: 把永续价格锚定到现货（替代交割日的机制）。通常不是平台收入，而是多空之间的转移支付。
- Q: 为什么极端资金费率会让正确的方向判断也亏钱？
  A: 年化持有成本可能超过 300%，持有期内的费率支出会吃掉全部方向性利润。
- Q: 怎样公平比较永续的资金费率与事件合约的资金占用成本？
  A: 把事件合约的机会成本（本金×无风险利率×期限）折算成同样的每周期费率，再并排比较。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
