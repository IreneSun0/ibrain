---
id: "concept:ask"
type: concept
title: Ask
title_zh: 卖一/卖价
title_en: Ask
aliases:
  - 卖一
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
# Ask | 卖一/卖价

## Executive Definition / Chinese Explanation | 定义与解释

**Ask / Offer | 卖价 / 卖单** = 有人愿意**卖出**的最低价格，以及那个价位上的数量。

它是订单簿的上半边。"最优卖价"（best ask）是你**现在立刻买入**要付的价格。

## Why This Matters | 为什么重要

ask 是"进货价"。任何策略回测如果用中间价成交，结果都会系统性偏乐观 —— 因为现实中你买要付 ask，卖只能拿 bid，**每次往返都自动亏掉一个价差**。

在价差 4 分的事件合约上，一次买入再卖出就先亏 4 分。若合约本身价格只有 0.63，这就是 **6% 以上的往返成本** —— 很多看起来有效的策略，扣掉这个就不剩什么了。

## How It Works | 机制怎么运转

事件市场有一个和普通市场不同的地方：**卖 YES 和买 NO 在经济上等价**（因为 YES + NO = $1）。

这意味着 ask 侧的流动性可以从两个来源获得：
- 直接有人挂 YES 的卖单；
- 有人挂 NO 的买单，被系统或套利者转换过来。

**成熟的事件市场会把两侧合并显示**，所以你看到的 YES ask 深度，可能有一半其实来自 NO 的 bid。不合并的平台，表面流动性会比真实流动性差很多。

## Concrete Example | 具体例子

簿子上最优 ask 是 **0.64 × 1,200**，同时 NO 侧最优 bid 是 **0.35 × 5,000**。

- 买 NO 花 0.35，等价于卖 YES 拿 **1 − 0.35 = 0.65**。
- 而 YES 侧最优 bid 只有 0.62。
- **通过 NO 侧卖 YES 能拿 0.65，比直接卖 YES 的 0.62 高 3 分。**

这就是事件市场里最常见的一类结构性机会：**两侧订单簿没有被完全打通时，同一个经济头寸在两条路径上价格不一致。** 专业玩家的第一课就是永远同时看两侧。

## Common Misconceptions | 常见误解

- **误解一："只看 YES 侧就够了。"** 在多数事件市场上，忽略 NO 侧等于只看到一半的流动性和一半的价格。
- **误解二："YES + NO 一定等于 1。"** 理论上是，实践中因为费用、资金成本和撮合摩擦会有偏离 —— 那个偏离就是套利空间，也是判断平台效率的直接指标。

## In Practice | 实战里怎么用

任何时候读一个事件市场的盘口，**同时读两侧**，并算一次 `YES_ask + NO_ask` 和 `YES_bid + NO_bid`：

- `YES_ask + NO_ask` 明显大于 1 → 两边都在收你钱，摩擦成本高。
- `YES_bid + NO_bid` 明显小于 1 → 变现折价大。
- 两个数离 1 越远，这个平台的实际交易成本越高，**跟它宣传的手续费率无关**。

这是一个 30 秒就能做完、但绝大多数人不做的平台体检。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么用中间价回测会系统性高估策略收益？
  A: 现实中买付 ask、卖拿 bid，每次往返自动损失一个价差。中间价成交假设抹掉了这个必然成本。
- Q: 在事件市场里，卖 YES 还有哪条等价路径？为什么必须同时看两侧？
  A: 买 NO 等价于卖 YES（YES+NO=$1）。两侧订单簿未完全打通时，同一头寸在两条路径上价格可能不同。
- Q: 怎么用 30 秒判断一个事件市场的真实交易成本？
  A: 算 YES_ask+NO_ask 与 YES_bid+NO_bid 离 1 的偏离度，偏离越大实际摩擦越高，与宣传费率无关。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
