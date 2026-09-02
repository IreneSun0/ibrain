---
id: "concept:outcome-market"
type: concept
title: Outcome Market
title_zh: 结果市场/结果型合约市场
title_en: Outcome Market
aliases:
  - 结果市场
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - "source:2026-08-26-hyperliquid-asset-ids"
related:
  - id: "venue:hyperliquid-hip4"
    rel: instantiated-by
    note: 链上 CLOB venue 的 outcome-market 扩展 (HIP-4)
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Outcome Market | 结果市场/结果型合约市场

## Executive Definition / Chinese Explanation | 定义与解释

**Outcome Market | 结果市场** = 交易标的是"某个结果是否成立"的市场。它是 [[prediction-market]] 更中性的技术叫法。

这个词的存在有实际意义：**"prediction market"（预测市场）这个名字强调预测，容易被理解成算命或博彩；"outcome market"（结果市场）强调的是可交割的结果，更接近它在法律和金融上的实际性质。**

## Why This Matters | 为什么重要

命名在这个行业不是文字游戏，**它直接影响法律定性**。

- 叫"预测"→ 听起来像猜测 → 容易被归入博彩。
- 叫"结果合约"或"事件合约"→ 强调有明确交割条件的合约 → 落入衍生品框架。

美国的监管论证正是沿着后一条路：这是转移事件风险的**衍生品**（event contract），因此归 CFTC 而非博彩监管。**这场命名之争至今仍在多个州的法庭上进行。**

## How It Works | 机制怎么运转

结果市场的最小构成要素只有四个：

1. **一个可判定的命题** —— "X 在 T 之前发生"。
2. **一个赔付函数** —— 通常是二元（$1 / $0），也可以是多结果或区间。
3. **一个抵押机制** —— 保证赔付可兑现（多为全额抵押）。
4. **一个裁决机制** —— 判定命题是否成立。

**去掉任何一个，它就不是结果市场**：
- 没有 (1)，是赌局；
- 没有 (2)，是意见调查；
- 没有 (3)，是承诺；
- 没有 (4)，是无法结算的合约。

**这四要素也是评估任何一个"预测市场"平台的最小检查表。**

## Concrete Example | 具体例子

同一件事的四种市场形态，法律与经济性质各不相同：

| 形态 | 例子 | 性质 |
|---|---|---|
| **意见调查** | 民调"你认为谁会赢" | 无金钱，无交割 |
| **博彩投注** | 体育博彩的固定赔率 | 与庄家对赌，赔率由庄家定，不可转让 |
| **结果市场** | Kalshi / Polymarket 的事件合约 | **双向可交易、价格由市场决定、可提前转让** |
| **传统衍生品** | CME 联邦基金期货 | 标的是价格，不是事件 |

**第 2 与第 3 行的区别是关键**：博彩是**你对庄家**，赔率固定；结果市场是**你对其他参与者**，价格连续变动，且你可以在结果揭晓前随时退出。

**"能否在结果揭晓前以市场价退出"是区分二者最实用的一条线。**

## Common Misconceptions | 常见误解

- **误解一："结果市场就是换个说法的赌博。"** 关键区别在于是否存在真实的经济对冲需求、是否双向可交易、是否可提前退出。这三条也是法律论证的支点。
- **误解二："这只是命名问题。"** 命名决定归入哪个监管框架，而框架决定了你有没有法律救济。
- **误解三："所有结果市场都一样。"** 二元 / 多结果 / 区间的定价约束和风险形状差别很大（见 [[multi-outcome-market]]）。

## In Practice | 实战里怎么用

用四要素检查表评估任何自称"预测市场"的产品：

| 要素 | 检查 |
|---|---|
| 可判定命题 | 能否改写成一个无歧义的 `if` 条件？ |
| 赔付函数 | 二元 / 多结果 / 区间？部分满足怎么算？ |
| 抵押机制 | 全额还是保证金？钱锁在哪？ |
| 裁决机制 | 谁判、能否申诉、历史争议查得到吗？ |

**再加一条判别线**：**能不能在结果揭晓前按市场价退出？** 不能，那它更接近投注票而非市场，价格也不该被读作概率。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么 'outcome market' 这个叫法在法律上更有利？
  A: 它强调可交割的结果合约而非'预测'，更容易落入衍生品框架（CFTC）而非博彩监管。
- Q: 结果市场的四个最小构成要素是什么？
  A: 可判定的命题、赔付函数、抵押机制、裁决机制。缺任何一个它就分别退化为赌局/意见调查/承诺/无法结算的合约。
- Q: 区分结果市场与博彩投注最实用的一条线是什么？
  A: 能否在结果揭晓前按市场价双向交易并退出 —— 博彩是与庄家对赌、赔率固定、不可转让。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
- [[src-2026-08-26-hyperliquid-asset-ids]] — <https://hyperliquid.gitbook.io/hyperliquid-docs/for-developers/api/asset-ids>
