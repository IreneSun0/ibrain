---
id: "concept:value-at-risk"
type: concept
title: VaR
title_zh: 风险价值
title_en: VaR
aliases:
  - VaR
  - Value at Risk
  - 风险价值
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
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# VaR | 风险价值

## Executive Definition / Chinese Explanation | 定义与解释

**VaR (Value at Risk) | 风险价值** = 在给定的置信水平和时间窗口下，预期不会被超过的最大损失。

"1 天 99% VaR = $2M" 的意思是：**100 个交易日里大约有 1 天，亏损会超过 $2M。** 注意它说的不是"最多亏 $2M"，而是"超过 $2M 的情况大约百分之一"。这两句话的差别，是历次风控事故的常见起点。

## Why This Matters | 为什么重要

VaR 是机构风险对话的**通用语**。监管资本、内部限额、董事会报告，全都建立在它之上。不会说 VaR，就无法和风控部门对话。

但对事件市场来说，更重要的是知道**它在这里为什么会失灵** —— 因为几乎所有机构会先用他们熟悉的 VaR 去量事件敞口，然后得到一个系统性偏低的数字。

## How It Works | 机制怎么运转

三种主流算法，假设各不相同：

| 方法 | 怎么算 | 隐含假设 |
|---|---|---|
| **参数法 / 方差-协方差** | 假设收益服从正态分布，用均值和标准差算分位数 | 收益连续、近似正态 |
| **历史模拟** | 直接用过去 N 天的真实收益分布取分位数 | 未来像过去 |
| **蒙特卡洛** | 按设定的随机过程模拟大量路径 | 你设的过程是对的 |

**三种方法在事件合约上都会出问题**：前两种依赖连续分布和历史，而事件价格是跳跃的、且往往没有可用历史（这个事件只发生一次）；第三种依赖你能正确设定跳跃过程 —— 而"这件事会不会发生"的概率恰恰是市场正在试图发现的东西。

## Concrete Example | 具体例子

一个 $1M 的事件合约头寸，以 0.30 买入：

- **历史模拟 VaR** —— 过去 30 天该合约价格在 0.28–0.32 之间波动，日波动率很低。算出的 1 天 99% VaR 可能只有 **$40k**。
- **真实的风险** —— 事件揭晓那天，价格要么到 1.00 要么到 0.00。**最大损失是 $1M（全部本金），概率 70%。**

**VaR 给出的 $40k 和真实的 $1M 差了 25 倍**，而且它在"平静期"看起来完全合理。这就是为什么直接把事件敞口塞进标准 VaR 框架是危险的：**它在事件揭晓前一直给你安全的读数。**

## Common Misconceptions | 常见误解

- **误解一："VaR 是最大损失。"** 它是一个分位数，**明确不覆盖尾部**。超过 VaR 之后能亏多少，VaR 一个字都没说（那是 [[expected-shortfall]] 回答的）。
- **误解二："VaR 低就是安全。"** 在跳跃型风险上，平静期的 VaR 低恰恰是危险信号 —— 它说明模型没有看见即将到来的跳跃。
- **误解三："置信水平越高越保守。"** 99% VaR 比 95% VaR 大，但它同时把"关注范围"推得更窄 —— **两者都不告诉你尾部里发生了什么。**

## In Practice | 实战里怎么用

在事件市场上用 VaR，必须做三件事：

1. **把二元敞口单独出账**，不要混进连续资产的 VaR 池 —— 混进去只会稀释掉它的真实形状。
2. **对每个事件直接算"结果矩阵"** —— 事件发生时组合值多少、不发生时多少。**这比任何分位数都有信息量。**
3. **用 [[expected-shortfall]] 而不是 VaR 做限额** —— ES 至少看进了尾部内部。

**最实用的一条：对事件敞口，把"最坏情况全额损失"直接写进报告，和 VaR 并列。** 这一行数字通常比整页统计更能改变决策。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: '1 天 99% VaR = $2M' 精确的含义是什么？
  A: 在 100 个交易日里约有 1 天，损失会超过 $2M。它不是最大损失，而是一个分位数。
- Q: 为什么标准 VaR 在事件合约上会系统性低估风险？
  A: 它依赖连续分布与历史波动，而事件价格是跳跃的且常无可用历史；平静期波动低会给出安全读数，直到揭晓日跳变。
- Q: 对事件敞口比 VaR 更有信息量的做法是什么？
  A: 直接列出结果矩阵（事件发生/不发生时组合分别值多少），并把最坏情况全额损失与 VaR 并列报告。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
