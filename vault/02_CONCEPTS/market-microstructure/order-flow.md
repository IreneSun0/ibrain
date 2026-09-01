---
id: "concept:order-flow"
type: concept
title: Order Flow
title_zh: 订单流
title_en: Order Flow
aliases:
  - 订单流
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
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Order Flow | 订单流

## Executive Definition / Chinese Explanation | 定义与解释

**Order Flow | 订单流** = 单位时间里进入市场的买卖单序列。

它不是一个数字，是一条**带方向、带规模、带时间戳的流**。交易所真正的资产不是撮合引擎，是订单流；做市商真正在读的也不是价格，是订单流。

## Why This Matters | 为什么重要

价格是订单流的**结果**，订单流是原因。看价格是看结果，看订单流是看过程。

对做市商，订单流的构成决定生死：
- **无信息流**（对冲者、噪音交易者）—— 方向随机，做市商赚它们的价差。
- **知情流** —— 只在报价错时单向成交，做市商必亏。

```
做市盈亏 = 无信息流贡献 − 知情流收割
```

**这个等式是理解做市商一切行为的钥匙**：它拉宽价差、缩小挂单量、在消息前撤退，全都是在调整这两项的比例。

## How It Works | 机制怎么运转

读订单流的三个维度：

1. **方向性（order flow imbalance）** —— 买单量减卖单量。持续单向通常意味着有人在建仓。
2. **规模分布** —— 大量小单 vs 少量大单，含义完全不同。前者像散户，后者像机构或知情人。
3. **时序聚集** —— 成交是均匀分布还是集中爆发？集中爆发常发生在信息事件前后。

**在链上事件市场，订单流有一个传统市场没有的性质：它部分是公开的。** 持仓变化链上可查（见 [[on-chain]]），因此任何人都能做传统上只有交易所能做的流分析。

## Concrete Example | 具体例子

同样是"一小时内成交 $200,000"，两种订单流的含义相反：

| | 流 A | 流 B |
|---|---|---|
| 笔数 | 400 笔 | 6 笔 |
| 方向 | 买卖各半 | 全部买入 |
| 时序 | 均匀 | 集中在 5 分钟内 |
| 读法 | **健康的双向需求** | **有人在抢时间建仓** |

**流 B 是做市商最怕的形态**：单向、大额、集中。理性反应是立刻拉宽价差或撤单。

如果你在流 B 之后看到价格跳涨，那不是巧合 —— **订单流通常领先价格。**

## Common Misconceptions | 常见误解

- **误解一："成交量就是订单流。"** 成交量是标量（总额），订单流是带方向和时序的序列。成交量可以刷，订单流的形态难伪造。
- **误解二："订单流分析需要交易所权限。"** 在链上事件市场不需要 —— 持仓变化公开可读。
- **误解三："订单流不平衡就一定有内幕。"** 也可能是对冲需求、指数再平衡、或一个人的判断。**不平衡是信号，不是结论。**

## In Practice | 实战里怎么用

在事件市场做订单流分析，三步：

1. **抓时序数据** —— 不是快照，是带时间戳的成交序列。
2. **算方向性不平衡** —— 滚动窗口内的买卖差。
3. **对照消息时间线** —— 不平衡是出现在消息**之前**还是之后？

**第 3 步是全部价值所在**：出现在消息之前的单向大额流，是识别可能的信息优势最直接的线索（见 [[inside-information]]）。链上市场让这件事对所有人开放。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 做市商的盈亏等式是什么？
  A: 做市盈亏 = 无信息流贡献 − 知情流收割。它解释了做市商拉宽价差、缩量、消息前撤退的全部行为。
- Q: 为什么说订单流通常领先价格？
  A: 价格是订单流的结果。单向、大额、集中的流出现之后价格才跳动，因此读流比读价格更早。
- Q: 链上事件市场的订单流分析有什么特殊之处？
  A: 持仓变化链上公开可读，任何人都能做传统上只有交易所才能做的流分析，尤其是比对消息时间线。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
