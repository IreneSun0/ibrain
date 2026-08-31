---
id: "concept:event-risk"
type: concept
title: Event Risk
title_zh: 事件风险
title_en: Event Risk
aliases:
  - 事件风险
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - id: "concept:event-var"
    rel: measured-by
  - id: "concept:event-contract"
    rel: see-also
    note: event risk 被合约化之后才可持有、交易、对冲
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Event Risk | 事件风险

## Executive Definition / Chinese Explanation | 定义与解释

**Event Risk | 事件风险** = 由某个离散事件是否发生所带来的损益不确定性 —— 选举结果、监管裁定、并购成败、关税落地、临床试验读数。

它和价格风险的区别是形状：**价格风险是连续扩散的，事件风险是跳跃的。** 一个消息落地，概率从 0.3 直接跳到 0.95，中间没有路径。这个区别让几乎所有基于连续假设的风险模型在这里失效。

## Why This Matters | 为什么重要

机构**早就持有大量事件风险**，只是它没有名字、没有账户、散落在各处：

- 一家跨国公司的关税敞口，藏在采购成本假设里。
- 一只基金的选举敞口，藏在"政策相关板块"的持仓里。
- 一家交易所的监管敞口，藏在"合规费用预算"里。

传统风控按**资产类别**切分（股票风险 / 利率风险 / 汇率风险），而事件风险**横着穿过所有类别**，于是没有任何一张桌子认领它，它散落在各桌的"残差"里。

**事件市场做的事不是创造了这个风险，而是把它显性化并可交易化。**

## How It Works | 机制怎么运转

事件风险的四个特征，每一个都让传统工具失灵：

1. **跳跃而非扩散** —— 波动率模型假设价格连续变动。事件价格直接跳，历史波动率对它几乎无预测力。
2. **二元或离散** —— 没有"部分发生"。VaR 这类基于分位数的指标，在二元分布上给出的数字意义很弱。
3. **相关性在事件时刻突变** —— 平时不相关的持仓，在同一个事件上可能高度同向。
4. **裁决风险叠加** —— 你可能对世界的判断完全正确，却因为合约语义或预言机问题而亏钱（见 [[resolution-risk]]）。

**第 4 条是传统风险分类里完全没有对应物的一项**，也是事件风险真正的特殊之处。

## Concrete Example | 具体例子

同一个"美国大选结果"事件，一家机构的真实敞口可能同时躺在四个地方：

| 位置 | 敞口形式 | 传统风控里归为 |
|---|---|---|
| 股票组合 | 政策敏感板块超配 | 市场风险 |
| 外汇 | 某货币对头寸 | 汇率风险 |
| 供应链 | 关税假设 | 运营预算 |
| 事件合约 | 直接押注 | ——（无归类） |

**没有任何一个系统会告诉它："你在这一个事件上的总敞口是 X。"**

这就是"事件维度的敞口聚合"为什么是个真问题：不是因为数据难拿，而是因为**没有一个把它们串起来的主键**（见 [[canonical-event-id]]）。

## Common Misconceptions | 常见误解

- **误解一："事件风险是新出现的风险。"** 它一直存在，只是以前没有名字和市场。显性化不等于新增。
- **误解二："买事件合约就是投机。"** 对真实持有该敞口的人，它是对冲；对没有敞口的人，它才是投机。**同一笔交易的性质取决于持有者的其他头寸。**
- **误解三："用 VaR 就能管事件风险。"** VaR 基于连续分布的分位数。二元跳跃分布上，VaR 会系统性低估尾部（见 [[event-var]]）。

## In Practice | 实战里怎么用

给自己或机构做一次事件敞口盘点，三步：

1. **列出未来 12 个月内可能发生的离散事件** —— 选举、议息、监管裁定、财报、并购交割日。
2. **对每个事件，问"如果它以相反方式发生，我的组合会怎样"** —— 不要只看直接持仓，要看间接暴露（供应链、板块、货币）。
3. **把跨账户、跨资产的同一事件敞口加总** —— 这一步几乎总是会发现意料之外的集中度。

**第 3 步做不出来，说明你缺的不是数据，是把不同表述指向同一现实事件的能力。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件风险与价格风险在形状上的根本区别是什么？
  A: 价格风险连续扩散，事件风险跳跃 —— 消息落地时概率直接跳变，中间没有路径，使连续假设的模型失效。
- Q: 为什么传统风控框架里没有事件风险的位置？
  A: 传统风控按资产类别切分，而事件风险横穿所有类别，散落在各类的残差里，没有一张桌子认领它。
- Q: 同一笔事件合约交易，什么时候是对冲、什么时候是投机？
  A: 取决于持有者的其他头寸：对真实持有该事件敞口的人是对冲，对没有敞口的人是投机。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
