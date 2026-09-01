---
id: "concept:derivative"
type: concept
title: Derivative
title_zh: 衍生品
title_en: Derivative
aliases:
  - 衍生品
status: reviewed
importance: tier-1
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
  - "source:2026-08-26-cftc-derivatives-basics-html"
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Derivative | 衍生品

## Executive Definition / Chinese Explanation | 定义与解释

**Derivative | 衍生品** = 一张自己一文不值、却可能值一百万的合约 —— 因为它的价值**衍生**自别的东西（价格、指数、利率、或某个事件的结果）。

金融最重要的发明不是钱，是**"指向"**：你可以在不持有一样东西的情况下，精确地承担或转移它带来的风险。

## Why This Matters | 为什么重要

衍生品干的事只有一件：**把风险从"和资产绑死"变成"可以单独拿出来交易"。**

- 你不必买下整片油田，就能承担（或对冲）油价风险。
- 你不必持有那家公司，就能对冲它财报不及预期的风险。
- **你不必参与选举，就能转移选举结果带来的风险。**

事件合约就是衍生品家族的一员 —— **这一点法律归属是它能被 CFTC 而非博彩监管的前提**，也是整个赛道合法性论证的基石。

## How It Works | 机制怎么运转

理解任何衍生品，拆四件事：

1. **标的（underlying）** —— 价值指向什么？
2. **支付函数（payoff）** —— 标的取不同值时，我收到多少钱？
3. **抵押与保证金** —— 谁保证到时候赔得出？
4. **结算方式** —— 现金结算还是实物交割？何时？

**事件合约的特别之处全在第 1 和第 2 项**：
- 标的不是价格，是**一个命题的真假**；
- 支付函数不是连续曲线，是**台阶函数**（$1 或 $0，没有中间态）。

这两点让所有基于连续假设的定价与风控工具在这里失效。

## Concrete Example | 具体例子

同一个"油价上涨"的风险，四种衍生品形态：

| 形态 | 支付 | 最坏情况 |
|---|---|---|
| **期货** | 线性，价格每涨 $1 赚 $1 | 理论上无限（做空时） |
| **期权** | 非线性，有权不买 | 买方最多亏权利金 |
| **掉期** | 交换现金流 | 视条款 |
| **事件合约** | "油价年底超 $100" → $1 / $0 | **开仓即知：最多亏本金** |

**最后一行的性质是事件合约最被低估的优点**：0.30 买入，赢 +0.70 / 输 −0.30，**开仓那一刻就知道最坏情况**。没有爆仓、没有追保、没有意外。

代价是资金效率（见 [[fully-collateralized-market]]）—— 但对很多机构，**"最坏情况可知"本身就值那个代价。**

## Common Misconceptions | 常见误解

- **误解一："衍生品 = 高杠杆 = 危险。"** 杠杆是保证金制度带来的，不是衍生品本身。**全额抵押的事件合约杠杆为 1，比现货还保守。**
- **误解二："衍生品是零和的所以没有价值。"** 交易层面零和，但**风险转移创造了实际价值** —— 农民不再担心秋天价格，这是真实的效用。
- **误解三："事件合约不算真正的衍生品。"** 它满足全部四要素（标的、支付函数、抵押、结算）。**争议不在金融定义上，在法律归类上。**

## In Practice | 实战里怎么用

看到任何衍生品，用四问拆解，尤其注意第 2 问的形状：

1. **标的是什么？** 是可观测的价格，还是需要判定的命题？
2. **支付函数长什么样？** 线性 / 非线性 / **台阶**？画出来。
3. **最坏情况是多少？** 有界还是无界？
4. **谁保证赔付？** CCP / 全额抵押 / 对手方信用？

**第 2 问画出来最有用。** 台阶函数意味着风险不能用波动率描述 —— 而这正是机构现有工具的盲区。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 衍生品做的唯一一件事是什么？
  A: 把风险从'和资产绑死'变成'可以单独拿出来交易' —— 让人在不持有资产的前提下承担或转移它带来的风险。
- Q: 事件合约与传统衍生品在哪两个要素上不同？
  A: 标的（不是价格而是一个命题的真假）与支付函数（不是连续曲线而是 $1/$0 的台阶函数）。
- Q: 为什么说全额抵押的事件合约比现货还保守？
  A: 杠杆为 1，且开仓那一刻就锁定了最坏情况（最多亏本金），没有爆仓与追保。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-derivatives-basics-html]] — <https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/derivatives_basics.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
