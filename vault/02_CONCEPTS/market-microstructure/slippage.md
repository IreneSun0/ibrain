---
id: "concept:slippage"
type: concept
title: Slippage
title_zh: 滑点
title_en: Slippage
aliases:
  - 滑点
status: reviewed
importance: tier-1
domains:
  - market-microstructure
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
  - id: "concept:execution-risk"
    rel: component-of
    note: 执行风险清单里最常见的一项
  - id: "concept:price-impact"
    rel: contrasts-with
    note: 你付出的均价与预期之差 vs 你把市场价格推走多远 — 常被混用
prerequisites:
  - "concept:depth"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Slippage | 滑点

## Executive Definition / Chinese Explanation | 定义与解释

**Slippage | 滑点** = 你实际成交的均价，和下单那一刻看到的价格之间的差。

它有两个来源：**吃穿订单簿多层**（规模造成的，可预测），和**下单到成交之间价格已经动了**（延迟造成的，不可预测）。

## Why This Matters | 为什么重要

滑点是从"纸面策略"到"真实收益"之间最大的一道减法，也是几乎所有回测失真的主因。

在事件市场里它尤其致命：合约价格本身在 0–1 之间，**1 分钱的滑点在 0.63 的合约上就是 1.6%**。一个胜率 55% 的策略，扣掉往返滑点可能直接变成负期望。

## How It Works | 机制怎么运转

规模造成的滑点可以精确算：

```
1. 按你的下单量，从最优价逐层吃订单簿
2. 加权平均得到实际成交均价
3. 滑点 = (成交均价 − 下单时中间价) / 中间价
```

延迟造成的滑点则取决于三件事：你的下单到达速度、市场当时的波动、以及**有没有人在抢跑你**。在公开 mempool 的链上市场，大单会被看见并被抢先交易，这是链上事件市场特有的滑点来源。

**降低滑点的四种手段**：拆单（TWAP/VWAP 分批）、挂限价单而非市价单、跨场所路由、择时避开薄流动性时段。每一种都在用时间换价格。

## Concrete Example | 具体例子

用前面的簿子买 5,000 份：

```
0.64 × 1,200 = $  768
0.65 × 2,500 = $1,625
0.66 × 1,300 = $  858
─────────────────────
5,000 份      = $3,251   →  均价 0.6502
```

- 下单时中间价 0.63，成交均价 0.6502。
- **滑点 = (0.6502 − 0.63) / 0.63 = 3.2%**。

若改成拆成 10 笔、每笔 500 份、间隔 5 分钟挂限价单，滑点大概率能压到 1% 以内 —— **代价是这 50 分钟里价格可能已经跑了，那是另一种成本。**

## Common Misconceptions | 常见误解

- **误解一："滑点是意外。"** 规模造成的那一半完全可以事先算出来。算不出来只是因为没去看订单簿。
- **误解二："限价单没有滑点。"** 限价单没有价格滑点，但有**成交不确定性** —— 可能只成交一部分，或者完全不成交，而这本身就是成本。
- **误解三："大平台滑点一定小。"** 取决于**那个具体合约**的深度。大平台上的冷门合约照样很薄。

## In Practice | 实战里怎么用

把滑点当成必须事先申报的成本，写进每一次交易决策：

1. 下单前逐层算一遍预期滑点，**超过策略预期收益的三分之一就不该按市价打进去**。
2. 记录每笔交易的实际滑点，和事前估算对比 —— 差得远说明你的数据延迟或对手方在抢跑。
3. 回测里强制加入基于真实订单簿的滑点模型，**不要用中间价成交**。

第 3 条能筛掉绝大多数看起来有效、实际不能落地的策略。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 滑点的两个来源分别是什么？哪一个可以事先算出来？
  A: 规模吃穿多层（可事先按订单簿精确计算）和下单延迟期间价格变动（不可预测）。
- Q: 为什么滑点在事件市场比在股票市场更致命？
  A: 合约价格在 0-1 之间，1 分钱滑点在 0.63 合约上就是 1.6%，足以把中等胜率策略变成负期望。
- Q: 限价单避免了什么成本，又引入了什么成本？
  A: 避免了价格滑点，引入了成交不确定性 —— 可能部分成交或完全不成交。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = depth; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
