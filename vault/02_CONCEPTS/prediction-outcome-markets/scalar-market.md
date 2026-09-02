---
id: "concept:scalar-market"
type: concept
title: Scalar Market
title_zh: 标量市场
title_en: Scalar Market
aliases:
  - 标量市场
  - Range Market
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
    note: "结算值为连续数值, 支付线性映射"
  - id: "concept:binary-option"
    rel: contrasts-with
    note: 连续线性支付 vs 0/1 支付
prerequisites:
  - "concept:outcome-market"
---
# Scalar Market | 标量市场

## Executive Definition / Chinese Explanation | 定义与解释

**Scalar Market | 标量市场** = 结算值落在一个**连续区间**上的合约，而不是二元的 $1 / $0。

问的不是"会不会发生"，而是"会是多少"：CPI 是多少、得票率多少、气温多少度。结算按实际数值在区间内线性插值。

## Why This Matters | 为什么重要

二元合约把世界压成"是/否"，很多真实敞口不是这个形状。

一家公司关心的不是"关税会不会加"，而是"加多少个百分点" —— 因为成本是连续函数。**用一串二元合约去逼近一个连续量，需要开很多个盘口，而每一个都更薄**（见 [[multi-outcome-market]]）。标量市场用一份合约解决这个问题。

代价是：**它比二元合约更难定价、更难做市、也更难写清楚条款。**

## How It Works | 机制怎么运转

标量合约的结算：

```
结算值 = clamp(实际数值, 下界, 上界)
每份合约赔付 = (结算值 − 下界) / (上界 − 下界)
```

例：区间 [2%, 4%] 的 CPI 合约，实际 CPI = 3.2% → 每份赔付 (3.2−2)/(4−2) = **0.60**。

**三个必须写死的东西**：
1. **区间上下界** —— 超出区间怎么办（截断还是作废）？
2. **精度** —— 保留几位小数？四舍五入还是截断？
3. **数据修正** —— 官方数据事后修正了，按初值还是修正值？

**第 3 条在标量市场比在二元市场严重得多**，因为修正 0.1 个百分点就直接改变赔付。

## Concrete Example | 具体例子

同一个"美联储会降息多少"的问题，三种市场形态的对比：

| 形态 | 合约数 | 流动性 | 表达精度 |
|---|---|---|---|
| 二元（"会不会降"） | 1 | 集中 | 最粗 |
| 多结果（0 / 25bp / 50bp） | 3 | 切成三份 | 中 |
| **标量（降息幅度 0–75bp）** | **1** | **集中** | **最细** |

**标量市场在理论上是最优的**：一份合约、集中的流动性、连续的表达。

**它在实践中稀少，原因是做市**：做市商要对整个区间报价，风险敞口是连续的，对冲和存货管理都比二元难一个量级。这是一个"理论最优、工程未解"的位置。

## Common Misconceptions | 常见误解

- **误解一："标量市场就是很多个二元合约。"** 经济上近似，但流动性完全不同：一份标量合约的深度集中，一串二元合约的深度被切碎。
- **误解二："价格还是概率。"** 标量合约的价格是**期望值的归一化**，不是概率。读法完全不同。
- **误解三："区间设宽一点更安全。"** 区间越宽，单位价格变动对应的实际数值变动越大，精度越低；且极端值被截断的概率上升。

## In Practice | 实战里怎么用

看一份标量合约，先算三个数：

1. **当前价格对应的隐含数值** = 下界 + 价格 × (上界 − 下界)。
2. **你的观点对应的价格** —— 再和市场价比。
3. **截断风险** —— 你认为实际值落在区间外的概率有多大？落外面你就拿边界值，可能与你的判断严重不符。

**再查一条条款：数据修正怎么处理。** 这是标量合约最容易被忽略、也最容易吃亏的地方。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 标量市场与二元市场的根本区别是什么？
  A: 结算值落在连续区间上并线性插值，而不是二元的 $1/$0；问的是'会是多少'而非'会不会发生'。
- Q: 标量合约必须写死哪三件事？
  A: 区间上下界（超出怎么办）、精度（小数位与舍入）、数据修正（按初值还是修正值）。
- Q: 标量市场理论最优却实践稀少，原因是什么？
  A: 做市商要对整个连续区间报价，风险敞口连续，对冲与存货管理比二元难一个量级。


## Sources
