---
id: "concept:model-risk"
type: concept
title: Model Risk
title_zh: 模型风险
title_en: Model Risk
aliases:
  - 模型风险
status: reviewed
importance: tier-2
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
  - id: "concept:value-at-risk"
    rel: risk-of
    note: "VaR/ES 自身是模型 — 模型错则风险容量错, backtest 不是免罪"
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Model Risk | 模型风险

## Executive Definition / Chinese Explanation | 定义与解释

**Model Risk | 模型风险** = 你用来定价或度量风险的模型本身是错的，或被用在了它不适用的地方。

它有两种形态：**模型错了**（假设与现实不符），和**模型用错了**（假设成立的场合之外还在用）。后者更常见，也更隐蔽。

## Why This Matters | 为什么重要

事件市场是模型风险的**教科书现场**，因为几乎所有现成的金融模型都建立在同一个假设上：**价格是连续变动的。**

- Black-Scholes：假设几何布朗运动 → 事件价格跳变，**不适用**。
- 历史波动率：假设过去能预测未来 → 事件只发生一次，**没有历史**。
- VaR / SPAN 保证金：假设连续分布 → 二元分布只有两个点，**读数系统性偏低**。

**把这些模型套到事件合约上，它们不会报错，只会给出一个看起来合理的错误数字。** 这是最危险的失效方式。

## How It Works | 机制怎么运转

管理模型风险的三条标准做法：

1. **明确写下假设** —— 每个模型都有前提。写不出前提，说明你不知道它什么时候会坏。
2. **做适用性检验** —— 数据是否满足假设？分布形状对吗？
3. **备用模型对照** —— 用两个假设不同的方法算同一个量，差得远就说明至少一个错了。

**对事件市场还要加一条**：**当模型给出的读数在判定日前后差一个数量级时，那不是模型在预警，是模型在失效。**

## Concrete Example | 具体例子

同一个 0.30 的事件合约头寸，三个模型给出的日风险读数：

| 方法 | 假设 | 读数 | 判定日实际 |
|---|---|---|---|
| 历史波动率 VaR | 连续、历史有代表性 | $2,000 | **$30,000** |
| 隐含波动率 | 存在连续隐含波动率曲面 | 无法计算 | — |
| **结果矩阵** | **无分布假设** | **两种情形: +$70k / −$30k** | **准确** |

**前两行是模型风险的两种表现**：一个给出错误数字，一个给不出数字。

**第三行不是更聪明的模型，是放弃建模** —— 直接枚举两种情形。**当标的只有两个结果时，枚举永远优于分布假设。**

## Common Misconceptions | 常见误解

- **误解一："模型越复杂越准。"** 复杂度提高了对假设的依赖。**假设错了，复杂只会让错误更难被发现。**
- **误解二："模型经过回测就可靠。"** 回测只能验证历史区间内的表现。事件合约常常没有可比历史。
- **误解三："模型风险是量化团队的事。"** 用模型输出做决策的人同样承担它 —— **不知道模型的假设，就不该引用它的数字。**

## In Practice | 实战里怎么用

引用任何模型给出的风险数字前，问三句话：

1. **这个模型假设了什么？** 说不出来就不要引用。
2. **我的标的满足那些假设吗？** 二元跳变标的通常不满足。
3. **有没有第二种方法算过同一个量？** 两法差一个数量级 = 至少一个是错的。

**对事件敞口的硬规**：**永远把"最坏情况全额损失"和模型读数并排放。** 模型可能错，那个数不会错。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 模型风险的两种形态是什么？哪种更隐蔽？
  A: 模型错了（假设与现实不符）和模型用错了（用在假设不成立的场合）。后者更常见也更隐蔽。
- Q: 为什么现成金融模型套到事件合约上特别危险？
  A: 它们都假设价格连续变动，套用时不会报错，只会给出一个看起来合理的错误数字。
- Q: 为什么对二元标的，枚举优于分布假设？
  A: 只有两个结果时，直接列出两种情形的组合价值是精确的，任何分布假设都是多余且可能错误的。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
