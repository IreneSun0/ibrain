---
id: "concept:capital-requirements"
type: concept
title: Capital Requirements
title_zh: 资本充足/最低资本要求
title_en: Capital Requirements
aliases:
  - 资本充足
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
# Capital Requirements | 资本充足/最低资本要求

## Executive Definition / Chinese Explanation | 定义与解释

**Capital Requirements | 资本要求** = 监管规定金融机构必须持有的最低自有资本，用来吸收损失而不倒下。

核心逻辑：**你可以用别人的钱做生意，但亏损必须先亏你自己的。** 资本就是那层缓冲。

## Why This Matters | 为什么重要

资本要求是持牌经营的**硬门槛**，也是[[regulatory-access|监管准入]]护城河的组成部分。

对事件市场：
- **持牌交易所（DCM）与清算所（DCO）都有法定资本要求** —— 这筛掉了绝大部分想入场的团队。
- **它是"时间买不到"的护城河的一部分**：即使有钱，资本要求也要配合审批周期与合规履历。

**这解释了为什么收购持牌实体比自建更快** —— 买的不只是牌照，还有已经满足的资本与合规状态。

## How It Works | 机制怎么运转

资本要求的三个层次：

1. **最低净资本** —— 一个绝对下限。
2. **风险加权资本** —— 按业务风险规模调整：做的风险越大，要求的资本越多。
3. **额外缓冲** —— 逆周期缓冲、系统重要性附加等。

**对清算所（CCP）还有一层特殊要求**：**自有资本必须排在会员违约基金之前被消耗**（见 [[clearinghouse]] 的违约瀑布）。

**这条设计的用意是激励对齐**：如果 CCP 亏的永远是会员的钱，它就没有动力严格风控。

## Concrete Example | 具体例子

为什么资本要求让"开一个持牌预测市场"很难：

| 要件 | 时间 | 钱能加速吗 |
|---|---|---|
| 最低资本 | 立刻 | **能** |
| 合规团队与流程 | 数月 | 部分 |
| 监管审批周期 | **以年计** | **不能** |
| 监管信任履历 | **逐案积累** | **不能** |

**只有第一行是钱能解决的。**

**所以 $112M 收购一个持牌实体是理性的**：它买的是后三行 —— 已经走完的时间和已经积累的履历（见 [[regulatory-access]]）。

资本要求还要与审批周期和合规履历一起评估，不能只看账面资金。

## Common Misconceptions | 常见误解

- **误解一："资本要求就是有多少钱。"** 它是**风险加权**的：同样的资本能支撑多大业务，取决于业务的风险特征。
- **误解二："资本要求只影响大机构。"** 它对小机构往往更致命 —— 固定成本摊薄不了。
- **误解三："满足资本要求就安全。"** 资本吸收的是**预期之外的损失**；它不能替代风控，只能在风控失效后争取时间。

## In Practice | 实战里怎么用

看一个持牌场馆的资本状况，问三件事：

1. **它持什么牌？** DCM / DCO / 经纪，各自的资本要求不同。
2. **资本相对业务规模如何？** 绝对数字没意义，要看覆盖倍数。
3. **清算所自有资本排在瀑布哪一层？** 排在会员资金之前 = 激励对齐。

资本要求、审批周期与合规履历共同构成准入门槛，短期内难以仅靠增加技术投入跨越。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 资本要求的核心逻辑是什么？
  A: 可以用别人的钱做生意，但亏损必须先亏自己的；资本就是吸收损失的缓冲层。
- Q: 为什么清算所的自有资本要排在会员违约基金之前？
  A: 激励对齐 —— 如果 CCP 亏的永远是会员的钱，它就没有动力严格风控。
- Q: 为什么收购持牌实体比自建更快？
  A: 钱只能加速最低资本一项；审批周期和监管信任履历都是时间函数，买下已持牌实体等于买下已走完的时间。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
