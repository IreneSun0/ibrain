---
id: "concept:bid"
type: concept
title: Bid
title_zh: 买一/买价
title_en: Bid
aliases:
  - 买一
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
related:
  - id: "concept:order-book"
    rel: component-of
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Bid | 买一/买价

## Executive Definition / Chinese Explanation | 定义与解释

**Bid | 买价 / 买单** = 有人愿意**买入**的最高价格，以及挂在那个价位上的数量。

它是订单簿的下半边。"最优买价"（best bid）是所有买单里出价最高的那一个 —— 也就是你**现在立刻卖出**能拿到的价格。

## Why This Matters | 为什么重要

bid 是"变现价"。你手上的头寸值多少钱，取决于 bid 而不是你买入的成本，也不是屏幕中间那个数字。

**很多人算浮盈时用中间价，实际平仓时才发现只能按 bid 出** —— 在价差宽的事件市场里，这个差可能吃掉一大截利润。

## How It Works | 机制怎么运转

挂一个 bid 就是在说"我愿意在这个价位接货"。它有两种命运：

- **被吃掉** → 你成交了，付出资金拿到头寸（你是 maker，通常费率更低甚至有返佣）。
- **一直挂着** → 你承担了"如果价格暴跌，你是那个接盘的人"的风险，这就是**逆向选择**成本。

所以 bid 的位置永远是权衡：挂得高，成交快但容易接到坏货；挂得低，安全但可能永远不成交。

## Concrete Example | 具体例子

接上一节的簿子：最优 bid 是 **0.62 × 900**。

- 你手上有 500 份 YES，想立刻卖 → 按 0.62 全部成交。
- 你手上有 3,000 份想立刻卖 → 0.62 只能吃 900 份，剩下 2,100 份要往下砸到 0.61、0.60，**均价约 0.6045**。
- 若你按中间价 0.63 估值，你会以为这 3,000 份值 $1,890；实际立刻变现只有约 **$1,813**，差 4%。

**这 4% 就是流动性的价格，它一直存在，只是不平仓就看不见。**

## Common Misconceptions | 常见误解

- **误解一："bid 和 ask 差不多，用哪个都行。"** 在主流股票上确实差不多；在长尾事件合约上价差可能有 5-10 分，用错一个，估值就错一大截。
- **误解二："挂 bid 没风险，反正不成交就没事。"** 挂单本身就是给了市场一个免费期权：只有在价格对你不利时它才最可能被吃掉。

## In Practice | 实战里怎么用

估算持仓价值时，**永远用 bid 侧的可实现价，不用中间价**，并且按你的实际规模逐层算：

- 小仓位 → 最优 bid 够用。
- 大仓位 → 把 bid 侧逐层吃一遍，算加权均价。

机构风控里这叫 **liquidation-adjusted valuation（考虑变现的估值）**。散户账户界面几乎从不这么显示，所以你得自己算。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么持仓估值该用 bid 而不是中间价？
  A: bid 是你立刻卖出能实际拿到的价格；中间价只是买卖两侧的中点，无法据以成交。价差宽时两者差距可观。
- Q: 挂一个 bid 相当于给了市场什么？
  A: 一个免费期权 —— 它最可能在价格对你不利时被吃掉，这就是挂单的逆向选择成本。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
