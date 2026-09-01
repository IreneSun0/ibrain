---
id: "concept:market-risk"
type: concept
title: Market Risk
title_zh: 市场风险
title_en: Market Risk
aliases:
  - 市场风险
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
    rel: measured-by
  - id: "concept:expected-shortfall"
    rel: measured-by
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Market Risk | 市场风险

## Executive Definition / Chinese Explanation | 定义与解释

**Market Risk | 市场风险** = 因为价格变动而造成损失的风险。它是四大风险类别里最基础、也最被充分研究的一类。

传统上按驱动因子细分：股价、利率、汇率、商品价格 —— 每个因子一张桌子、一套模型、一个负责人。

## Why This Matters | 为什么重要

市场风险的分类方式，恰恰暴露了[[event-risk|事件风险]]无处安放的原因。

传统风控**按资产类别切分**风险。而事件风险**横着穿过所有类别**：一场选举同时影响股票、汇率、商品和供应链假设。**它不属于任何一张桌子，于是散落在各桌的"残差"里，没有人认领。**

**这不是疏忽，是分类框架的结构性盲区** —— 而事件市场做的事，就是把这层风险显性化并可交易化。

## How It Works | 机制怎么运转

市场风险的度量工具链：

```
敏感度 (delta / duration / beta)
   → 情景分析 (如果因子动 X%)
      → VaR / ES (分布的分位数与尾部)
         → 压力测试 (极端但可信的情景)
```

**这条链的每一环都假设因子是连续变动的。** 对事件标的：

- **敏感度** —— delta 在临近判定时趋于无穷（见 [[binary-option]]）。
- **情景分析** —— 只有两个情景，反而最好用。
- **VaR / ES** —— 分位数在二元分布上意义很弱。
- **压力测试** —— 事件的"压力情景"就是它的正常情景之一。

**结论：整条链里唯一对事件标的仍然好用的是情景分析** —— 也就是结果矩阵。

## Concrete Example | 具体例子

一家基金的风险报表，事件敞口如何"消失"：

| 报表行 | 数字 | 其中的选举敞口 |
|---|---|---|
| 股票市场风险 | $8M | **隐含 $6M** |
| 汇率风险 | $5M | **隐含 $5M** |
| 商品风险 | $3M | 0 |
| 事件合约 | $5M | $5M |
| **合计** | $21M | **真实选举敞口 $16M** |

**报表上只有第四行被标记为"事件"，而真实敞口是它的三倍多。**

**这就是为什么"事件维度的敞口聚合"是个真问题**：不是数据难拿，是**没有一个把它们串起来的主键**（见 [[canonical-event-id]]）。

## Common Misconceptions | 常见误解

- **误解一："市场风险已经被研究透了。"** 对连续因子是的；对跳变型因子，工具链大部分不适用。
- **误解二："事件风险是市场风险的一种。"** 它横穿所有类别，且是二元跳变的。**并入市场风险会让它彻底消失在残差里。**
- **误解三："报表上没有就说明没有敞口。"** 恰恰相反 —— 没有被分类的敞口是最危险的，因为无人管理。

## In Practice | 实战里怎么用

给你的组合做一次"事件维度重切"，三步：

1. **列出未来 12 个月的关键离散事件。**
2. **对每个事件，逐行扫描你的持仓** —— 问"这一行是否也暴露于这个事件"。不要只看被标记为事件的那些。
3. **按事件加总，不按资产类别加总。**

**几乎每次做这个练习，都会发现一个报表上看不见的集中度** —— 那正是它的价值（见 [[event-var]]）。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 传统市场风险的分类方式为什么让事件风险无处安放？
  A: 传统按资产类别切分，而事件风险横穿所有类别，于是散落在各类的残差里，没有任何一张桌子认领。
- Q: 市场风险的度量工具链里，哪一环对事件标的仍然好用？
  A: 情景分析（结果矩阵）—— 因为事件只有两个情景，枚举反而最精确；敏感度、VaR/ES、压力测试都依赖连续性假设。
- Q: 为什么'报表上没有就说明没有敞口'是危险的想法？
  A: 没有被分类的敞口无人管理，而事件敞口恰恰隐含在被标为股票、汇率、商品的行里。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
