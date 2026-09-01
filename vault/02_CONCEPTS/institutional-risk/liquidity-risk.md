---
id: "concept:liquidity-risk"
type: concept
title: Liquidity Risk
title_zh: 流动性风险
title_en: Liquidity Risk
aliases:
  - 流动性风险
status: reviewed
importance: tier-1
domains:
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
  - id: "concept:market-risk"
    rel: contrasts-with
    note: 无法按价变现的损失 vs 价格变动的损失 — 账面盈利 ≠ 可兑现
prerequisites:
  - "concept:liquidity"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Liquidity Risk | 流动性风险

## Executive Definition / Chinese Explanation | 定义与解释

**Liquidity Risk | 流动性风险** = 你想平仓时，没法以接近当前价格的价格平掉的风险。

它和市场风险是**正交的两个维度**：市场风险是"价格变了"，流动性风险是"我没法按这个价格出去"。一个头寸可以在账面上盈利，同时在流动性上已经死了。

## Why This Matters | 为什么重要

它是第一章微观结构（[[spread]] / [[depth]] / [[slippage]]）**在组合层的投影**。

单笔交易看三个仪表就够了；机构问的是另一个问题：**"我这整个仓位，按当前盘口读数，要多久、多贵才能清完？"**

在事件市场上这个问题格外尖锐，因为流动性有三个叠加的坏性质：极度长尾（大部分合约常年空盘）、随时可撤（做市商没有义务）、**并且在临近裁决日集中蒸发** —— 而那恰恰是最多人想调整头寸的时刻。

## How It Works | 机制怎么运转

量化流动性风险的标准做法是 **liquidity-adjusted VaR**：在正常 VaR 之上，加一项"在受压深度下清仓的估计滑点"。

```
LVaR ≈ VaR + 清仓成本
清仓成本 = Σ(逐层吃穿订单簿的加权均价偏离) × 头寸规模
```

关键在"受压深度"三个字：**不能用平静时的盘口算**。正确做法是取一段时间里深度的**低分位数**（比如 10 分位），或者直接取历史上重大消息后 5 分钟的深度读数。

**这正是 liquidity-adjusted 思想从定价端延伸到风控端的完整形态** —— 定价时它告诉你"你的规模能实现的价格"，风控时它告诉你"你的仓位能实现的退出"。

## Concrete Example | 具体例子

两个账面完全相同的 $2M 事件合约头寸：

| | 合约 A（大选） | 合约 B（某小国选举） |
|---|---|---|
| 账面价值 | $2M | $2M |
| ±1% 深度 | $180k | $2k |
| 清仓需要 | 约 11 层 / 数小时 | **盘口根本装不下** |
| 估计清仓成本 | ~1.5% | **>20%，或者根本出不来** |

**账面一样，可实现价值差 20% 以上。**

更糟的是：合约 B 的深度在裁决日前一周会进一步萎缩。**如果你打算"看到不对就跑"，那个"跑"在合约 B 上是不存在的选项。**

## Common Misconceptions | 常见误解

- **误解一："流动性风险是市场风险的一种。"** 正交维度。市场风险是价格变了，流动性风险是出不去。
- **误解二："成交量大 = 流动性风险低。"** 成交量是历史，可以刷。要看**此刻的深度**和**受压时的深度**。
- **误解三："我持仓小所以没有流动性风险。"** 相对于**那个盘口**才算小。在一个 ±1% 深度只有 $2k 的合约上，$50k 就是巨仓。

## In Practice | 实战里怎么用

把流动性风险写进每一个仓位决策，三个动作：

1. **开仓前算退出成本** —— 按你的规模逐层吃一遍订单簿，得出预期清仓滑点。**超过 3% 就要重新考虑仓位大小。**
2. **用受压深度，不用当前深度** —— 取历史深度的 10 分位，或消息冲击后的读数。
3. **设"流动性预算"** —— 你的总仓位不应超过某个"能在 N 天内清完"的阈值。

**再加一条事件市场专用纪律：临近裁决日主动降仓。** 那个窗口里流动性最薄、争议风险最高、而你最可能想动。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 流动性风险和市场风险为什么是正交维度？
  A: 市场风险是价格变了，流动性风险是没法按这个价格出去。头寸可以账面盈利而在流动性上已无法退出。
- Q: 计算 liquidity-adjusted VaR 时，为什么必须用'受压深度'？
  A: 平静期的盘口深度会大幅高估可退出规模；应取深度的低分位数或重大消息后的读数。
- Q: 事件市场流动性的三个坏性质是什么？
  A: 极度长尾（多数合约空盘）、可随时撤单（做市商无义务）、临近裁决日集中蒸发 —— 恰在最需要时消失。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = liquidity; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
