---
id: "concept:cross-margin"
type: concept
title: Cross Margin
title_zh: 跨品种/跨头寸保证金
title_en: Cross Margin
aliases:
  - 跨品种
status: reviewed
importance: tier-1
domains:
  - derivatives
  - institutional-risk
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
  - id: "concept:margin"
    rel: special-case-of
    note: 允许相关头寸风险互抵的保证金模式
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Cross Margin | 跨品种/跨头寸保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Cross Margin | 跨品种 / 组合保证金** = 承认多个头寸之间存在风险抵消，按**组合净风险**收保证金，而不是每个头寸各收各的。

逐仓（isolated）保证金把每个头寸当孤岛；cross-margin 承认组合是一张网。

## Why This Matters | 为什么重要

它是资本效率的主要来源之一。一个持有相互对冲头寸的组合，逐仓收保证金会重复收取，组合保证金只收净风险 —— **差别可以到数倍**。对机构而言，这直接决定同样的资本能支撑多大业务规模。

## How It Works | 机制怎么运转

cross-margin 的成立依赖一个假设：**相关性在压力时刻仍然成立。**

这就是它的"地下室"：互抵按平时的相关性算，而**危机时相关性会突变** —— 2008 年、2020 年 3 月都演示过，平时对冲良好的组合在压力下同时亏损。

**事件市场版本的深水区更尖锐**：跨场所的"同题"合约能不能互抵？答案取决于它们**是否真的等价**（见 [[contract-equivalence]]）。于是：

> **资本效率问题被翻译成了语义判定问题。**

**这不是比喻。** 清算机构要允许跨场所净额，就必须能证明两张合约在所有情形下给出相同结果 —— 那是逐条读条款的工作，不是统计工作。

## Concrete Example | 具体例子

一个机构的两个头寸：

- A 平台："某法案在 Q4 前通过" **YES**，$5M
- B 平台："某法案在 2026 年内通过" **NO**，$5M

**看起来高度对冲**，逐仓要收 $10M 抵押，组合保证金理论上可以收很少。

**但两张合约的判定时点不同**（Q4 末 vs 年末）。若法案在 12 月通过：
- A 判 **NO**（Q4 前没通过）→ 你的 YES 亏
- B 判 **YES**（年内通过）→ 你的 NO 也亏

**两边同时亏，$10M 全损。** 而按"高度相关"给的组合保证金可能只收了 $1M —— **穿仓 $9M。**

**这就是为什么跨场所净额需要语义等价证明，而不是相关性估计。**

## Common Misconceptions | 常见误解

- **误解一："互抵省下的钱是免费的。"** 省的是"正常日"的资本，**押上的是"相关性断裂日"的风险。**
- **误解二："同题合约可以互抵。"** 只有五维全部对齐才可以（见 [[contract-equivalence]]）。
- **误解三："相关性可以用历史数据估计。"** 事件市场的分叉是语义性的、二元的 —— **要么发生要么不发生，没有历史频率可用。**

## In Practice | 实战里怎么用

在任何风险系统里做抵扣之前，过一道闸：

```
这两个头寸能互抵吗?
  ├─ 五维语义对照全部一致?  → 可互抵
  ├─ 有一项不一致?          → 记为基差头寸, 不抵扣
  └─ 不确定?                → 按不抵扣处理
```

**默认应该是"不抵扣"，抵扣需要证明。** 反过来做（默认抵扣，出问题再说）是穿仓的标准路径。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: cross-margin 的成立依赖什么假设？它的'地下室'是什么？
  A: 依赖相关性在压力时刻仍成立。地下室是危机时相关性突变，平时对冲良好的组合可能同时亏损。
- Q: 为什么说事件市场的资本效率问题被翻译成了语义判定问题？
  A: 跨场所净额要求证明两张合约在所有情形下给出相同结果，这是逐条读条款的语义工作，不是统计相关性工作。
- Q: 风险系统里做头寸抵扣的正确默认值是什么？
  A: 默认不抵扣，抵扣需要五维语义对照的证明。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
