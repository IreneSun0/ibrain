---
id: "concept:price-impact"
type: concept
title: Price Impact
title_zh: 价格冲击
title_en: Price Impact
aliases:
  - 价格冲击
status: reviewed
importance: tier-2
domains:
  - market-microstructure
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
related: []
prerequisites:
  - "concept:depth"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Price Impact | 价格冲击

## Executive Definition / Chinese Explanation | 定义与解释

**Price Impact | 价格冲击** = 你的这笔单子本身把价格推动了多少。

它和[[slippage|滑点]]是同一件事的两个视角：滑点是"我多付了多少"，价格冲击是"我把市场推了多远"。**下单规模越大，你越不是价格的接受者，而是价格的制造者。**

## Why This Matters | 为什么重要

在薄盘口上，价格冲击有一个特别恶劣的性质：**它会泄漏你的意图。**

你把价格从 0.60 推到 0.68，等于告诉全市场"有人在大举买入"。跟单者和抢跑者随之出现，你剩下的单子成交更贵，而你想平仓时价格又会向下冲击。

**事件市场的长尾合约深度极薄，几千美元就能造成可见的价格冲击** —— 这也是为什么这些盘口的"概率"很容易被少量资金操纵（见 [[market-integrity]]）。

## How It Works | 机制怎么运转

价格冲击分两部分，恢复行为完全不同：

| 成分 | 含义 | 会不会恢复 |
|---|---|---|
| **临时冲击** | 消耗了盘口深度 | **会** —— 做市商补单后价格回落 |
| **永久冲击** | 市场认为你的交易含信息 | **不会** —— 价格永久重定 |

**永久冲击的大小取决于市场认为你有多可能知情。** 同样规模的单子，来自一个匿名新地址和来自一个已知的被动指数基金，永久冲击完全不同。

**恢复时间是最实用的指标**：大单之后价格多久回到原位？恢复慢的盘口，进去容易出来难。

## Concrete Example | 具体例子

在一个 ±1% 深度只有 $8,000 的事件合约上买入 $40,000：

```
下单前   中间价 0.60
吃穿五档 成交均价 0.653      ← 滑点 8.8%
成交后   中间价 0.67          ← 价格冲击 +7 分
5 分钟后 中间价 0.64          ← 临时冲击恢复了 3 分
稳定在   0.64                 ← 永久冲击 = 4 分
```

**你付出了两次代价**：成交时的滑点 8.8%，以及把市场永久推高 4 分 —— 后者意味着你如果想再买，起点已经变差；想卖出，则要向下冲击。

**大资金在事件市场的真实成本，通常是账面手续费的十倍以上。**

## Common Misconceptions | 常见误解

- **误解一："价格冲击等于滑点。"** 滑点是你的成交价偏离，价格冲击是市场价格的位移。一笔单子两者都产生，但后者影响的是你之后的每一笔。
- **误解二："拆单就没有冲击了。"** 拆单降低瞬时冲击，但拉长了暴露时间，且规律性的拆单会被识别和抢跑。
- **误解三："冲击只影响我自己。"** 它把"概率"推走了，而别人正在引用那个概率。**薄盘口上的价格冲击是市场诚信问题，不只是执行成本问题。**

## In Practice | 实战里怎么用

下大单前，先做一次冲击预算：

1. **算预期冲击** —— 逐层吃穿订单簿，得出成交后的中间价位移。
2. **设冲击上限** —— 超过 2–3% 就应拆单或换场所。
3. **测恢复** —— 抓几次历史大单前后的时序，看深度和价差多久恢复。
4. **考虑反向** —— 你退出时会造成反向冲击，把它计入总成本。

**第 4 条最常被忽略**：很多人只算进场成本，忘了出场时还要再付一次。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 价格冲击和滑点的区别是什么？
  A: 滑点是你的成交价偏离下单时价格；价格冲击是你的单子对市场价格造成的位移，它影响你之后的每一笔交易。
- Q: 临时冲击与永久冲击的差别是什么？
  A: 临时冲击是消耗盘口深度造成的，做市商补单后会恢复；永久冲击是市场认为你的交易含信息而重定价格，不会恢复。
- Q: 为什么薄盘口上的价格冲击是市场诚信问题？
  A: 它把被外界引用的'概率'推走了，几千美元就能造成可见位移，使价格容易被少量资金操纵。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
