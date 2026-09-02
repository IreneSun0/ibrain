---
id: "concept:smart-order-routing"
type: concept
title: Smart Order Routing
title_zh: 智能订单路由
title_en: Smart Order Routing
aliases:
  - 智能订单路由
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
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
  - "concept:venue"
  - "concept:depth"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# Smart Order Routing | 智能订单路由

## Executive Definition / Chinese Explanation | 定义与解释

**SOR (Smart Order Routing) | 智能订单路由** = 自动把一笔单子拆开、送到多个场所，以拿到更好的综合成交结果。

它优化的通常是三件事的组合：**价格、成交概率、和冲击成本**。

## Why This Matters | 为什么重要

事件市场的流动性天然碎片化：同一个事件在多个平台各有盘口，每个都不够深（见 [[liquidity]]）。**SOR 是把碎片重新拼起来的技术。**

**但它有一个事件市场特有的前置条件**：路由的前提是这些盘口**真的是同一个东西**。

在股票市场，同一只股票在不同交易所是完全等价的，路由是纯技术问题。
**在事件市场，不同平台的"同题"合约可能语义不等价**（见 [[contract-equivalence]]）—— **把单子路由过去，你买到的可能是另一个东西。**

**所以事件市场的 SOR 首先是语义问题，其次才是技术问题。**

## How It Works | 机制怎么运转

SOR 的决策要素：

| 要素 | 考虑 |
|---|---|
| **价格** | 各场所的可实现价（含费用与滑点） |
| **深度** | 每个场所能吃多少 |
| **确定性** | 成交概率、拒单率 |
| **成本** | 手续费、提现费、跨链成本 |
| **语义** | **这些合约真的等价吗** ← 事件市场专属 |

**最后一行没有对应物的原因**：股票不需要问"这只股票和那只股票是不是同一只"。

**而在事件市场，这一问必须逐条比对五个维度**，而且是确定性判断，不是相似度匹配。

## Concrete Example | 具体例子

一笔 $500k 的事件合约需求，SOR 面对的实际决策：

```
平台 A: 0.62 × $120k 可成交  · 判定日 12/31 · 源 = 机构 X
平台 B: 0.60 × $200k 可成交  · 判定日 12/28 · 源 = 机构 Y
平台 C: 0.64 × $400k 可成交  · 判定日 12/31 · 源 = 机构 X
```

**纯价格路由会选 B（最便宜）**。

**但 B 的判定日和数据源都不同** —— 它是另一份合约。把 $200k 路由过去，你建的不是同一个头寸，而是一个带基差的头寸（见 [[basis-risk]]）。

**正确的路由是 A + C（语义相同），代价是均价更高。**

**这个例子说明：事件市场的最优路由不是最低价格，是"语义正确前提下的最低价格"。**

## Common Misconceptions | 常见误解

- **误解一："SOR 就是找最低价。"** 还要权衡深度、成交确定性、总成本，在事件市场还要先过语义关。
- **误解二："路由到更多场所总是更好。"** 每多一个场所就多一份运营与语义风险；跨链路由还有资金移动成本。
- **误解三："股票市场的 SOR 技术可以直接搬过来。"** 缺的那一层正是最难的：**判断这些合约是不是同一个东西。**

## In Practice | 实战里怎么用

评估任何跨场所路由方案，按顺序问：

1. **它怎么判断合约等价？** 有五维对照吗？还是只匹配标题？
2. **不等价时怎么办？** 拒绝路由，还是照样路由？**照样路由的方案不要用。**
3. **总成本算全了吗？** 含手续费、提现、跨链、以及资金在途时间。

**第 1 问是分辨严肃方案与玩具的最快方式**：只按标题匹配的路由，在极端情形下会把你的对冲变成裸奔。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件市场的 SOR 相比股票市场多了哪一层前置问题？
  A: 语义等价判定 —— 不同平台的'同题'合约可能不是同一个东西，路由过去买到的可能是另一份合约。
- Q: 为什么纯价格路由在事件市场可能是错的？
  A: 最便宜的那个盘口可能判定日或数据源不同，路由过去建的是带基差的头寸而非同一个头寸。
- Q: 分辨严肃路由方案与玩具的最快问题是什么？
  A: 它怎么判断合约等价 —— 只按标题匹配的路由会在极端情形下把对冲变成裸奔。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
