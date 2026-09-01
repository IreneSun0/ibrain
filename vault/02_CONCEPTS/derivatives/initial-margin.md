---
id: "concept:initial-margin"
type: concept
title: Initial Margin
title_zh: 初始保证金
title_en: Initial Margin
aliases:
  - 初始保证金
status: reviewed
importance: tier-2
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
    rel: component-of
    note: 开仓门槛
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---
# Initial Margin | 初始保证金

## Executive Definition / Chinese Explanation | 定义与解释

**Initial Margin (IM) | 初始保证金** = 开仓时必须存入的抵押品，用来覆盖头寸在正常市况下**一段持有期内的最大可能亏损**。

它回答的问题是：在我们能把这个头寸平掉之前，它最多会亏多少。

## Why This Matters | 为什么重要

IM 是清算所风险模型的**第一道防线**，也是资本效率的主要杠杆：IM 收得越低，同样的资本能支撑越大的敞口 —— 但违约瀑布被击穿的概率越高。

**在事件合约上，IM 的计算方法直接失效**（见 [[margin]]）：常规做法是按历史波动率估一个置信区间，而事件价格不扩散、直接跳。**要覆盖跳变，IM 就得等于全部名义价值**，那就退回全额抵押了。

这就是"事件合约保证金化"这个监管议题的技术核心。

## How It Works | 机制怎么运转

IM 的两类主流模型：

| 模型 | 思路 | 适用 |
|---|---|---|
| **SPAN 类** | 扫描一组预设情景（价格 ±X%、波动率 ±Y%），取最坏 | 期货、期权 |
| **VaR / ES 类** | 按历史或模拟分布取分位数 | 组合、跨品种 |

两者共同的隐含假设：**收益分布是连续的、历史有代表性。**

**对二元跳变标的，两个假设都不成立**：分布只有两个点，历史波动率对判定日的跳变毫无预测力。目前没有公认可用的替代模型 —— 这不是有人偷懒，是真问题。

## Concrete Example | 具体例子

同一个 $100k 名义的头寸，几类标的的 IM 对照：

| 标的 | 日波动率 | IM（99%, 2 日） | IM / 名义 |
|---|---|---|---|
| 主要股指期货 | 1.2% | ~$4,000 | 4% |
| 加密永续 | 4% | ~$13,000 | 13% |
| 事件合约（模型算） | 表面 2% | ~$7,000 | 7% |
| **事件合约（真实需要）** | **跳到 0 或 1** | **$100,000** | **100%** |

**后两行差 14 倍。** 模型给出的 7% 在平静期看起来合理，直到判定日 —— 那一天它一次性穿仓 93%。

**这就是为什么事件市场普遍走全额抵押：不是保守，是模型确实不适用。**

## Common Misconceptions | 常见误解

- **误解一："IM 越低越好。"** 低 IM = 高杠杆 = 高穿仓概率。对跳变标的尤其危险。
- **误解二："IM 是给交易所的钱。"** 它是你的抵押品，平仓后退还（扣除盈亏）。
- **误解三："事件合约不做保证金是监管保守。"** 主要是模型不适用 —— 覆盖跳变所需的 IM 就等于全额。

## In Practice | 实战里怎么用

看到任何"事件合约保证金化"的方案，问三件事：

1. **它怎么处理跳变？** 用什么替代历史波动率？
2. **穿仓谁承担？** 有违约瀑布吗？第一层是谁的钱？
3. **IM 会不会顺周期？** 波动时上调保证金，会不会触发连环强平？

**第 3 问是 2008 年的教训**，而在二元跳变标的上这个效应会更剧烈 —— 因为"波动"不是渐变，是一次性跳到底。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 初始保证金回答的是什么问题？
  A: 在头寸能被平掉之前，它在正常市况下最多会亏多少。
- Q: 为什么 SPAN 和 VaR 类模型对事件合约都失效？
  A: 两者都假设收益分布连续且历史有代表性；而事件分布只有两个点，历史波动率对判定日跳变毫无预测力。
- Q: 为什么事件市场普遍走全额抵押？
  A: 覆盖跳变所需的初始保证金就等于全部名义价值，与全额抵押等价 —— 是模型不适用，不是监管保守。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = margin; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
