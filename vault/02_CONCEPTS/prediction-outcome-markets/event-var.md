---
id: "concept:event-var"
type: concept
title: Event VaR
title_zh: 事件风险价值
title_en: Event VaR
aliases:
  - 事件风险价值
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
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
    rel: special-case-of
    note: 按具体事件情景聚合跨 venue/跨工具头寸的 VaR
prerequisites:
  - "concept:value-at-risk"
  - "concept:event-risk"
import_origin: xlsx-learning-map+manual
import_category: 事件市场候选概念
---
# Event VaR | 事件风险价值

## Executive Definition / Chinese Explanation | 定义与解释

**Event VaR | 事件风险价值** = 把 VaR 的思路搬到事件维度：**不问"价格波动多少"，而问"如果这件事以相反方式发生，我的整个组合会损失多少"。**

它不是一个新的统计量，是一个**换轴**：传统 VaR 沿资产类别切，Event VaR 沿事件切。

## Why This Matters | 为什么重要

因为机构的事件敞口是**跨资产、跨账户散落**的（见 [[event-risk]]），任何按资产类别组织的风险系统都看不到它的总和。

一家机构可能在股票、外汇、供应链假设、和事件合约上同时暴露于同一场选举，**而没有任何一张报表会把这四个数字加起来。** Event VaR 就是那张缺失的报表。

## How It Works | 机制怎么运转

算 Event VaR 的三步，每一步的难点都不在数学上：

1. **识别** —— 把组合里所有对同一事件敞口的头寸找出来。**这一步需要一个跨平台、跨资产的事件主键**（见 [[canonical-event-id]]），而它目前不存在。
2. **情景化** —— 对每个可能结果，重估整个组合。二元事件只有两个情景，比连续分布好算得多。
3. **加总与聚合** —— 按事件、按事件族（相关事件）、按时间窗口汇总，找出隐藏的集中度。

**难的是第 1 步。** 第 2、3 步是标准的情景分析，任何风控系统都会做。**整个问题的瓶颈是数据关联，不是数学。**

## Concrete Example | 具体例子

一家基金在"某国大选"上的真实 Event VaR：

| 头寸 | 若 A 当选 | 若 B 当选 |
|---|---|---|
| 政策敏感板块超配 $50M | +$4M | −$6M |
| 该国货币多头 $30M | +$2M | −$5M |
| 事件合约（押 A）$5M | +$7M | −$5M |
| 供应链关税假设 | 0 | −$3M |
| **合计** | **+$13M** | **−$19M** |

**这只基金以为自己"有一点选举敞口"，实际上它在单一事件上押了 $19M 的下行。**

而且注意：事件合约那一行看起来只有 $5M，占比很小 —— **真正的敞口在其他三行里，它们从来没被归类为"选举风险"。**

## Common Misconceptions | 常见误解

- **误解一："Event VaR 是一种新的统计模型。"** 它是情景分析加一个正确的分组键。数学是现成的。
- **误解二："只要买了事件合约就是事件敞口。"** 恰恰相反 —— **大部分事件敞口藏在没有被标记为事件敞口的头寸里。**
- **误解三："事件之间独立，可以简单相加。"** 事件常常高度相关（同一场选举影响多个市场；同一次议息影响整条曲线）。**需要按事件族聚合，不能只按单个事件。**

## In Practice | 实战里怎么用

做一次 Event VaR，用一张表，不需要任何系统：

```
事件: ____________________  日期: ______

头寸/暴露          结果 A      结果 B      结果 C
_______________    ______      ______      ______
_______________    ______      ______      ______
_______________    ______      ______      ______
合计               ______      ______      ______
```

三条纪律：
1. **每一行都要问"这是不是也暴露于同一事件"** —— 包括不在交易账户里的（预算假设、供应链、合规成本）。
2. **按事件族做第二张表** —— 把相关事件放一起，看总敞口。
3. **对每个事件记下"我最不希望的那个结果"** —— 那一列的合计就是你要盯的数字。

**做完你几乎一定会发现一个自己没意识到的集中度。** 这就是这个练习的全部价值。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: Event VaR 相对传统 VaR 的核心变化是什么？
  A: 换轴：不沿资产类别切，而沿事件切 —— 问'如果这件事反向发生，整个组合损失多少'。
- Q: 计算 Event VaR 的瓶颈在哪一步？为什么？
  A: 第一步识别 —— 需要跨平台跨资产的事件主键把散落的敞口关联起来，而这个主键目前不存在。瓶颈是数据关联而非数学。
- Q: 为什么说大部分事件敞口藏在'没被标记为事件敞口'的头寸里？
  A: 事件风险横穿资产类别，藏在板块超配、货币头寸、供应链假设、合规预算里，没有任何按资产分类的报表会把它们加总。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 事件市场候选概念)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = value-at-risk, event-risk; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
