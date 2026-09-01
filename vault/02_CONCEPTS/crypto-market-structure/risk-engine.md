---
id: "concept:risk-engine"
type: concept
title: Risk Engine
title_zh: 风险引擎
title_en: Risk Engine
aliases:
  - 风险引擎
status: reviewed
importance: tier-1
domains:
  - industry-strategy
  - crypto-market-structure
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
prerequisites:
  - "concept:margin"
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Risk Engine | 风险引擎

## Executive Definition / Chinese Explanation | 定义与解释

**Risk Engine | 风险引擎** = 持续读取头寸与市场状态、计算风险指标、并输出**读数**的系统。

注意它输出的是读数，不是动作。"争议概率 12%"是读数；"禁止新开仓"是动作 —— 那是[[policy-engine|政策引擎]]的事。**把这两者分开，是理解机构风控架构的关键。**

## Why This Matters | 为什么重要

因为分工决定了什么能外购、什么必须自持：

- **读数层可以外购** —— 计算方法是通用的，数据可以来自第三方。
- **规则层必须机构自有** —— 风险偏好是各家的主权，没有两家机构的限额一样。

**很多产品搞混了这一点**，试图卖"完整的风控解决方案"，结果撞上机构不肯把风险偏好交给外部系统的天花板。**卖读数比卖规则容易得多。**

## How It Works | 机制怎么运转

事件市场的风险引擎需要计算的，和传统的不一样：

| 传统风险引擎 | 事件风险引擎 |
|---|---|
| VaR / ES（连续分布） | **结果矩阵**（二元/离散） |
| 按资产类别聚合 | **按事件与事件族聚合**（见 [[event-var]]） |
| 保证金充足度 | 全额抵押下不适用 |
| 对手方敞口 | **裁决机制敞口**（见 [[concentration-risk]]） |
| 流动性调整 | 同样需要，但深度数据更难拿 |

**右列有三行在左列里没有对应物。** 这就是为什么把事件敞口塞进现成的风控系统会漏掉最重要的部分 —— 系统里根本没有那几个字段。

## Concrete Example | 具体例子

一个事件风险引擎在一天里该输出的读数：

```
组合事件敞口
  ├─ 按事件:      最大单一事件 12% ✓
  ├─ 按事件族:    "中期选举"族 35% ⚠
  ├─ 按裁决机制:  预言机 A 100% ❌
  └─ 按抵押资产:  USDC 100% ❌

裁决风险
  ├─ 语义分低于阈值的持仓: 3 个, 合计 8%
  ├─ 当前处于争议状态的持仓: 1 个, $240k
  └─ 7 日内到判定日的持仓: 5 个, 合计 22%

流动性
  └─ 按受压深度估计的清仓成本: 2.8%
```

**这十行读数里，有六行在任何现成的风控系统里都算不出来** —— 不是算法难，是缺字段和缺数据。

## Common Misconceptions | 常见误解

- **误解一："风险引擎就是算 VaR。"** 在事件市场，VaR 是最不重要的那个指标（见 [[value-at-risk]]）。
- **误解二："引擎越复杂越好。"** 一个能正确按四个维度聚合集中度的简单引擎，胜过一个模型精巧但看不见裁决敞口的复杂引擎。
- **误解三："读数和动作应该在一个系统里。"** 分开才对：读数可外购，规则必自持。混在一起会让机构无法采购。

## In Practice | 实战里怎么用

搭一个最小可用的事件风险引擎，只需要四个输出：

1. **四维集中度表**（事件 / 事件族 / 裁决机制 / 抵押资产）
2. **结果矩阵**（每个重要事件的正反两种情形下组合值多少）
3. **裁决风险清单**（语义分低的、争议中的、临近判定日的）
4. **受压清仓成本**（按低分位深度算）

**这四项用一张电子表格就能做**，不需要任何系统。而它们比大多数机构现在拥有的事件风险视图都更完整。

**先把这四项手工做一遍，再谈自动化。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 风险引擎与政策引擎的分工是什么？为什么这个分工重要？
  A: 风险引擎输出读数，政策引擎持有规则并执行动作。读数层可外购，规则层必须机构自持（风险偏好是主权）。
- Q: 事件风险引擎相比传统风险引擎多了哪几类计算？
  A: 结果矩阵（二元离散）、按事件与事件族聚合、裁决机制敞口 —— 这三项在传统系统里没有对应字段。
- Q: 最小可用的事件风险引擎需要哪四个输出？
  A: 四维集中度表、结果矩阵、裁决风险清单（语义分低/争议中/临近判定）、受压清仓成本。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 产业战略)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = margin; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
