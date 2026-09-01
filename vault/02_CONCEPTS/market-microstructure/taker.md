---
id: "concept:taker"
type: concept
title: Taker
title_zh: 吃单方/消耗流动性者
title_en: Taker
aliases:
  - 吃单方
status: reviewed
importance: tier-2
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
related: []
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Taker | 吃单方/消耗流动性者

## Executive Definition / Chinese Explanation | 定义与解释

**Taker | 吃单方** = 主动吃掉订单簿上已有挂单的一方。它消耗流动性，因此通常付更高的费率。

taker 买的是**确定性**：立刻成交，不用等。价差和 taker 费就是这份确定性的价格。

## Why This Matters | 为什么重要

绝大多数用户默认就是 taker —— 界面上那个"买入"按钮通常就是市价单。**这意味着大多数人在毫无察觉的情况下，一直在支付市场上最贵的那种成本。**

搞清楚自己什么时候该做 taker、什么时候该做 maker，是从"用户"变成"交易者"的第一个分水岭。

## How It Works | 机制怎么运转

什么时候当 taker 是理性的：

| 情境 | 该做 taker 吗 | 为什么 |
|---|---|---|
| 你有时效性信息 | **是** | 慢一秒信息就没价值了，价差是小钱 |
| 你要对冲一个正在扩大的风险 | **是** | 不成交的风险大于价差成本 |
| 你在建长期头寸，不急 | **否** | 挂限价单，让别人来找你 |
| 盘口很薄 | **否** | 滑点会远超价差，应该拆单慢慢挂 |

**核心判断：你付出的立即性成本，是否小于等待的成本。**

## Concrete Example | 具体例子

同一笔"买 10,000 份 YES"的需求：

- **做 taker**：市价打进去，均价 0.6502，加 taker 费 0.2%，**总成本约 $6,515**。
- **做 maker**：在 0.63 挂限价单分批。若两小时内全部成交，均价 0.63，扣返佣，**总成本约 $6,296**。省下约 **$219（3.4%）**。
- **但**：若这两小时里出了利好，价格直接跳到 0.72，你的挂单一份没成交，**踏空的损失是 $900 以上**。

**省下的 3.4% 和踏空的 14%，就是 maker 与 taker 的真实取舍。** 没有普适答案，只有"你这笔交易到底在赌什么"。

## Common Misconceptions | 常见误解

- **误解一："taker 费高，所以永远该挂单。"** 挂单的隐性成本是不成交，在快速行情里这个成本远超价差。
- **误解二："市价单保证成交。"** 在薄盘口上市价单会吃穿整个簿子，成交价可能离谱到你不能接受。**永远设价格上限。**
- **误解三："taker 一定是散户。"** 有信息优势的专业玩家几乎总是 taker —— 因为信息有时效，他们要的正是立即性。

## In Practice | 实战里怎么用

下单前用一句话回答："我付这个价差，是在买什么？"

- 买**信息时效** → 值，做 taker。
- 买**风险对冲的确定性** → 值，做 taker。
- 什么都没买，只是不想等 → **不值**，改挂限价单。

再加一条硬纪律：**永远不用无价格上限的市价单**。在薄盘口上，那等于给市场开了一张空白支票。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: taker 付出的额外成本买到的是什么？
  A: 立即性（确定立刻成交）。价差和 taker 费就是这份确定性的价格。
- Q: 什么情况下做 taker 是理性的？
  A: 有时效性信息、或需要对冲正在扩大的风险时 —— 不成交的代价大于价差成本。
- Q: 为什么有信息优势的专业玩家往往是 taker 而非 maker？
  A: 信息有时效，他们要的正是立即成交；等待挂单成交会让信息优势消失。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = order-book; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
