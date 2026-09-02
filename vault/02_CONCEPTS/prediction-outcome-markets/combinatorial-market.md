---
id: "concept:combinatorial-market"
type: concept
title: Combinatorial Market
title_zh: 组合市场
title_en: Combinatorial Market
aliases:
  - 组合市场
  - Conditional Market
status: reviewed
importance: tier-2
domains:
  - prediction-outcome-markets
tags:
  - concept
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related:
  - id: "concept:outcome-market"
    rel: special-case-of
    note: 直接为联合/条件概率定价
prerequisites:
  - "concept:multi-outcome-market"
  - "concept:implied-probability"
---
# Combinatorial Market | 组合市场

## Executive Definition / Chinese Explanation | 定义与解释

**Combinatorial Market | 组合市场** = 允许对**多个事件的联合结果**下注的市场："A 当选**且**通胀低于 3%"。

它的表达力远超单事件市场 —— 现实中的风险几乎总是条件性的、组合性的。但它有一个数学上的硬墙。

## Why This Matters | 为什么重要

因为**很多真实敞口是条件敞口**。

一家公司的关税成本取决于"哪个政党执政"**和**"贸易谈判是否达成"的组合；一只基金的风险取决于"降息"**和**"财报季表现"的交互。用单事件合约无法表达这些交互 —— 你只能分别下注，而分别下注不等于对组合下注。

**组合市场是唯一能直接表达条件性风险的形态。**

## How It Works | 机制怎么运转

硬墙在于**流动性的组合爆炸**：

```
N 个事件 → 2^N 个联合结果
```

- 3 个事件 → 8 个角落
- 10 个事件 → **1,024 个角落**
- 20 个事件 → **超过一百万个**

每一个角落都需要有人报价、有人接盘。**绝大多数组合的盘口是空的**，而空盘口意味着无法成交、无法定价。

**学术解法**是用自动做市商（Hanson 的 LMSR 系）在整个联合空间上维持一致定价：不需要每个角落都有人挂单，公式保证任意组合都有价格且不套利（见 [[automated-market-maker]]）。

**实践现实**是：真实交易量集中在极少数政治条件对上，其余角落有价格但无成交。

## Concrete Example | 具体例子

一个 3 事件组合市场的联合空间：

| A | B | C | 联合概率 |
|---|---|---|---|
| ✓ | ✓ | ✓ | 0.08 |
| ✓ | ✓ | ✗ | 0.12 |
| ✓ | ✗ | ✓ | 0.05 |
| … | … | … | … |
| ✗ | ✗ | ✗ | 0.21 |

**8 行必须加起来等于 1**，而且必须和单事件的边际概率一致（P(A) = 含 A 的四行之和）。

**这个一致性约束正是价值所在**：组合市场强制所有相关合约的定价互相自洽，而一堆独立的单事件合约做不到 —— 它们的隐含联合分布可能自相矛盾。

**注意区分 parlay（串关）**：赌场的串关是给定赔率的投注票，不是可持续双向交易的市场，也没有这个一致性保证。**形似而神异。**

## Common Misconceptions | 常见误解

- **误解一："组合市场就是同时买几个合约。"** 分别买 A 和 B 不等于买"A 且 B" —— 前者的收益是两笔独立支付，后者只在两者同时成立时支付。
- **误解二："2^N 的问题可以靠算力解决。"** 这不是计算问题，是**流动性问题**：每个角落都需要资本，而资本有限。
- **误解三："组合市场和串关一样。"** 串关是投注票，赔率给定、不可转让、无一致性约束。**结构不同，不要混用。**

## In Practice | 实战里怎么用

判断一个组合市场是否可用，三问：

1. **联合空间多大？** 事件数 N 决定 2^N。超过 4–5 个事件，实际可用性急剧下降。
2. **用什么维持定价一致？** 有 LMSR 类统一做市，还是靠独立盘口？后者几乎必然出现不一致。
3. **边际概率对得上吗？** 把含 A 的所有联合概率加起来，是否等于 A 的单事件价格？对不上就是套利机会 —— 或者是定价机制有问题。

**第 3 条是一个 30 秒的自洽性检查，也是最容易发现定价缺陷的地方。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 组合市场解决了单事件市场解决不了的什么问题？
  A: 条件性/组合性风险的表达 —— 现实敞口常取决于多个事件的交互，分别下注不等于对组合下注。
- Q: 组合市场的硬墙是什么？为什么算力解决不了？
  A: 流动性的组合爆炸：N 个事件产生 2^N 个联合结果，每个角落都需要资本报价，而资本有限。这是流动性问题不是计算问题。
- Q: 组合市场与赌场串关（parlay）的关键区别是什么？
  A: 串关是给定赔率的投注票，不可转让、无双向交易、无定价一致性约束；组合市场是可交易的市场且强制边际概率自洽。


## Sources
