---
id: "concept:forward-contract"
type: concept
title: Forward
title_zh: 远期合约
title_en: Forward
aliases:
  - Forward
  - 远期合约
status: reviewed
importance: tier-2
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
related:
  - id: "concept:derivative"
    rel: special-case-of
  - id: "concept:counterparty-risk"
    rel: see-also
    note: "定制双边 OTC 合同, 无 CCP 介入, 违约风险双边裸露"
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Forward | 远期合约

## Executive Definition / Chinese Explanation | 定义与解释

**Forward Contract | 远期合约** = 双方私下约定未来某时点按某价格交易的合约。它是[[futures-contract|期货]]的**场外、非标准化**版本。

一句话区分：**期货是在交易所买的标准品，远期是和对手方谈出来的定制品。**

## Why This Matters | 为什么重要

远期与期货的对比，正好演示了金融基础设施的全部价值：

| | 远期（场外） | 期货（交易所） |
|---|---|---|
| 条款 | 定制 | 标准化 |
| 对手方 | 特定一家 | 中央对手方 |
| 违约风险 | **完全承担** | 被清算所吸收 |
| 提前退出 | 难（需对手方同意） | 随时平仓 |
| 价格透明 | 无 | 公开 |

**标准化 + 中央对手方 = 可流通。** 这就是交易所存在的理由。

**事件市场目前的位置很微妙**：合约在同一平台内是标准化的（像期货），跨平台却不可互换（像远期）—— 因为语义不等价（见 [[contract-equivalence]]）。

## How It Works | 机制怎么运转

远期存在的理由是**定制**：

- 期货只有固定的交割月，你的敞口未必对得上。
- 期货的合约乘数固定，你的规模未必是整数倍。
- 有些标的根本没有期货市场。

**代价是三件事**：承担对手方信用风险、难以提前退出、没有公开价格参考。

**2008 年之后，监管把大量场外衍生品推向中央清算**，正是为了消除第一条 —— 代价是把风险集中到少数几家清算所（见 [[clearinghouse]]）。

## Concrete Example | 具体例子

事件市场里的"远期"形态：**大额 RFQ 成交**（见 [[request-for-quote]]）。

一笔 $2M 的定制事件敞口通过 RFQ 私下与做市商成交：
- **条款可定制** —— 规模、甚至某些边界条件可谈。
- **对手方特定** —— 你面对的是那一家做市商。
- **提前退出难** —— 要平仓通常得回到同一家。

**结构与远期完全一致。** 区别在于这类交易通常仍在平台的托管框架内清算，所以对手方风险被削弱了。

**理解这一点，就理解了为什么事件市场的机构化必然伴随场外结构的出现** —— 公开盘口装不下机构规模。

## Common Misconceptions | 常见误解

- **误解一："远期已经过时了。"** 场外衍生品名义规模仍远超交易所品种。定制需求永远存在。
- **误解二："远期比期货更危险。"** 更危险的是**对手方风险**，不是合约本身。有抵押安排的远期可以很安全。
- **误解三："事件合约都是标准化的。"** 同一平台内是，跨平台不是 —— 语义差异让它们不可互换。

## In Practice | 实战里怎么用

区分你面对的是标准品还是定制品，问三件事：

1. **这份合约能不能转给别人？** 不能 = 远期性质。
2. **谁是我的对手方？** 中央对手方还是特定一家？
3. **有没有公开价格？** 没有 = 你无法独立验证成交价是否合理。

**第 3 条在事件市场的 RFQ 里尤其重要**：私下成交没有公开参考价，你只能靠同时问几家来形成价格竞争。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 远期与期货的三个核心差别是什么？
  A: 条款定制 vs 标准化、特定对手方 vs 中央对手方、难以提前退出 vs 随时平仓。
- Q: 为什么说事件合约的位置很微妙？
  A: 同一平台内是标准化的（像期货），跨平台却因语义不等价而不可互换（像远期）。
- Q: 事件市场里最接近远期的形态是什么？
  A: 大额 RFQ 成交：条款可定制、对手方特定、提前退出通常要回到同一家做市商。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
