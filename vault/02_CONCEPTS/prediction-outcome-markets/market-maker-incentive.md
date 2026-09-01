---
id: "concept:market-maker-incentive"
type: concept
title: Market Maker Incentive
title_zh: 做市激励计划
title_en: Market Maker Incentive
aliases:
  - Market Maker Incentives
  - 做市商激励
  - 做市激励计划
status: reviewed
importance: tier-2
domains:
  - prediction-outcome-markets
  - regulation-compliance
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
  - "source:2026-08-26-cftc-9282-26"
related:
  - id: "concept:order-flow-network-effect"
    rel: see-also
    note: 无自然流动性时的人工点火 — 用返佣让飞轮先转起来
prerequisites:
  - "concept:market-maker"
import_origin: xlsx-learning-map+manual
import_category: 预测市场监管
---
# Market Maker Incentive | 做市激励计划

## Executive Definition / Chinese Explanation | 定义与解释

**Market Maker Incentive | 做市激励** = 平台为让做市商在无自然双向需求的市场上持续报价而支付的补贴：返佣、库存补贴、专属费率、或直接的做市合同。

它在事件市场不是"增长手段"，而是**基础设施** —— 因为绝大多数事件合约根本没有自然的对手方。

## Why This Matters | 为什么重要

事件市场面对一个死循环：

```
没有做市商 → 盘口空 → 交易者不来 → 更没有做市商
```

价格市场靠自然的双向需求（有人想买有人想卖）打破这个循环。**事件市场大部分合约没有自然双向需求** —— 谁会主动想卖"某国 12 月 CPI 超过 3%"？

**所以平台必须花钱买第一推动**：用返佣与奖励**买断**做市商早期承担的逆向选择与库存成本，让飞轮转过临界点。

## How It Works | 机制怎么运转

激励设计的核心难题：**买行为，不要买刷量。**

| 计费口径 | 买到了什么 | 副作用 |
|---|---|---|
| **按成交量付费** | 成交量 | **会买来对敲刷量** |
| **按有效报价时长 × 规模 × 价差质量付费** | **真深度** | 需要更复杂的度量 |

正确的口径要同时含三个因子：
- **在场时长** —— 报价挂了多久（尤其消息前后）
- **规模** —— 挂了多少钱
- **价差质量** —— 挂得多紧

**只按成交量付费是最常见也最昂贵的错误** —— 它精确地激励了你最不想要的行为。

## Concrete Example | 具体例子

同样 $100k 的激励预算，两种设计的结果：

| | 按成交量付 | 按有效报价付 |
|---|---|---|
| 做市商行为 | 自己和自己对敲 | 真实挂单承担风险 |
| 产生的成交量 | 很高 | 中等 |
| **±1% 真实深度** | **接近 0** | **$40k** |
| 消息冲击时在场率 | 0% | 60% |
| 平台看到的数字 | 漂亮 | 一般 |
| 用户实际体验 | **进不去出不来** | 能交易 |

**第一列的问题是：平台的仪表盘会显示成功。** 成交量指标漂亮，直到有人想真的下一笔大单。

## Common Misconceptions | 常见误解

- **误解一："提高返佣就能买来流动性。"** 只在逆向选择可控时有效。**信息不对称严重的市场，补贴再高做市商也不来** —— 因为亏的比补贴多（见 [[adverse-selection]]）。
- **误解二："有做市商就有流动性。"** 做市商可随时撤单，且在消息与裁决时刻撤得最快。
- **误解三："激励是临时的，飞轮转起来就可以停。"** 头部合约可以，**长尾合约永远需要激励** —— 它们永远没有自然双向需求。

## In Practice | 实战里怎么用

设计或评估一套做市激励，四问按顺序：

1. **做市商能不能对冲？** 有没有其他场所或相关品种转移库存？（见 [[inventory-risk]]）
2. **逆向选择有多严重？** 这类事件存在内幕的可能性多高？
3. **返佣够不够覆盖 (2)？** 算清楚，不要拍脑袋。
4. **裁决出错时做市商的头寸怎么处理？**

**第 4 条最容易被漏掉，也最容易让做市商在关键时刻集体退出。** 做市商能承受市场风险，但不愿承受"我完全正确却因为裁决错误而亏光"的风险。

**一个反直觉的结论**：做市商被激励合同**要求**在自己看不清的市场持续报价 —— 风险工具的需求方就是这么被制度制造出来的。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件市场为什么必须支付做市激励？
  A: 绝大多数事件合约没有自然的双向需求，存在'没做市商→盘口空→交易者不来'的死循环，必须花钱买第一推动。
- Q: 为什么按成交量付费是错误的激励口径？
  A: 它会买来对敲刷量 —— 成交量指标漂亮但真实深度接近零。正确口径是有效报价时长 × 规模 × 价差质量。
- Q: 做市激励设计里最容易被漏掉的一问是什么？
  A: 裁决出错时做市商的头寸怎么处理 —— 做市商能承受市场风险，但不愿承受判定错误导致的归零。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-9282-26]] — <https://www.cftc.gov/PressRoom/PressReleases/9282-26>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场监管)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = market-maker; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
