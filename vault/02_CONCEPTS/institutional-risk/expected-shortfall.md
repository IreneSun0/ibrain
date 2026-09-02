---
id: "concept:expected-shortfall"
type: concept
title: Expected Shortfall
title_zh: 预期损失/尾部期望损失
title_en: Expected Shortfall
aliases:
  - 预期损失
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
    rel: contrasts-with
    note: 尾部平均损失 vs 阈值损失概率 — 监管从 VaR 转向 ES 的原因
prerequisites:
  - "concept:value-at-risk"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Expected Shortfall | 预期损失/尾部期望损失

## Executive Definition / Chinese Explanation | 定义与解释

**Expected Shortfall (ES) | 期望短缺 / CVaR** = 在最坏的那部分情形里，**平均**会亏多少。

[[value-at-risk|VaR]] 说"99% 的日子亏不超过 $2M"，但对剩下那 1% 一个字没说。**ES 回答的正是那 1% 里平均亏多少** —— 它看进了尾部内部。

## Why This Matters | 为什么重要

ES 是巴塞尔框架从 VaR 转向的核心指标，原因很直接：**VaR 对尾部形状完全不敏感。**

两个组合可以有相同的 99% VaR，但一个尾部亏 $2.1M，另一个亏 $50M。VaR 看不出区别，ES 能。

**对事件市场，这个区别是致命的**：二元跳变标的的分布只有两个点，VaR 在判定日之前一直给出温和的读数，而 ES 至少会把"归零"这个情形算进去（见 [[event-var]]）。

## How It Works | 机制怎么运转

```
ES(α) = E[损失 | 损失 > VaR(α)]
```

读法：把最坏的 (1−α) 那部分情形单独拿出来，算它们的平均损失。

ES 相对 VaR 的两个数学优点：
1. **次可加性** —— 组合的 ES 不会超过各部分 ES 之和。**VaR 不满足这条**，意味着按 VaR 管理可能"拆开算比合起来算更安全"，这在数学上是荒谬的。
2. **对尾部敏感** —— 尾部变胖，ES 立刻上升；VaR 可能纹丝不动。

**次可加性对事件市场特别重要**：你的敞口散落在多个事件、多个平台，若风险指标不满足次可加性，聚合出来的数字可能系统性低估。

## Concrete Example | 具体例子

两个组合，相同的 99% VaR：

| | 组合 A | 组合 B |
|---|---|---|
| 99% VaR | $2.0M | $2.0M |
| 尾部情形 | 亏 $2.1M | **亏 $50M** |
| **99% ES** | **$2.1M** | **$50M** |

**VaR 完全看不出差别，ES 相差 24 倍。**

**事件市场的组合几乎总是组合 B 的形状**：平静期波动极小（VaR 低），判定日一次性归零（ES 极高）。

**只看 VaR 管理事件敞口，等于在判定日之前一直觉得自己很安全。**

## Common Misconceptions | 常见误解

- **误解一："ES 只是更保守的 VaR。"** 它是不同的问题：VaR 问"边界在哪"，ES 问"越过边界之后平均多惨"。
- **误解二："ES 更保守所以更好。"** ES 需要估计尾部分布，而尾部数据本来就稀少 —— **估计误差比 VaR 更大**。它更对，但也更难算准。
- **误解三："事件合约用 ES 就够了。"** ES 仍是统计指标。对二元标的，**直接列结果矩阵比任何分位数指标都更有信息量**（见 [[event-var]]）。

## In Practice | 实战里怎么用

在事件市场用风险指标，按这个顺序：

1. **结果矩阵优先** —— 事件正反两种情形下组合分别值多少。**这比任何统计量都直接。**
2. **ES 而非 VaR 做限额** —— 至少它看进了尾部。
3. **把"全额损失"单列一行** —— 二元标的的最坏情况就是本金归零，写出来。

**一条实用纪律**：给任何事件敞口报风险时，**同时给 VaR、ES、和最坏情况全额损失三个数**。三个数放一起，决策者才看得见真实形状。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: ES 与 VaR 回答的问题有什么不同？
  A: VaR 问'损失边界在哪'（一个分位数），ES 问'越过那个边界之后平均亏多少'（尾部内部的均值）。
- Q: 为什么次可加性对事件市场特别重要？
  A: 敞口散落在多个事件和平台，若指标不满足次可加性，聚合出来的风险数字可能系统性低估。
- Q: 为什么对二元标的，结果矩阵比任何分位数指标都好？
  A: 分布只有两个点，分位数指标在判定日之前一直给出温和读数；结果矩阵直接列出两种情形的组合价值。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
