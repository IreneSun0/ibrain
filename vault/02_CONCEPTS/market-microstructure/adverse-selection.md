---
id: "concept:adverse-selection"
type: concept
title: Adverse Selection
title_zh: 逆向选择/被更懂的人交易
title_en: Adverse Selection
aliases:
  - 逆向选择
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
  - id: "concept:market-maker"
    rel: risk-of
    note: "做市两大成本之一: 知情对手只在报价不利时来成交"
  - id: "concept:spread"
    rel: mitigated-by
    note: 做市商拉宽价差为知情流付费
prerequisites:
  - "concept:market-maker"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Adverse Selection | 逆向选择/被更懂的人交易

## Executive Definition / Chinese Explanation | 定义与解释

**Adverse Selection | 逆向选择** = 在信息不对称的市场里，**愿意跟你成交的人，恰恰更可能是知道得比你多的人**。

对做市商而言这是一条铁律：你的挂单只有在对对方有利时才会被吃掉。所以每一笔成交都自带一个坏消息 —— 你可能刚刚接了一个知情人的货。

## Why This Matters | 为什么重要

这是理解事件市场为什么"看起来该很赚但实际很难做"的钥匙。

事件市场的标的是**现实世界会发生的事**，而现实世界里总有人先知道：公司内部的人知道财报，竞选团队知道内部民调，监管机构的人知道下周宣布什么。**信息优势在事件市场里比在股票市场更普遍、更难监管** —— 因为标的不是证券，很多辖区的内幕交易法根本不适用。

做市商知道这一点，所以要么把价差拉宽，要么干脆不报价。**这就是长尾事件盘口常年空着的根本原因。**

## How It Works | 机制怎么运转

逆向选择怎么把一个做市商逼走：

1. 做市商在 0.62/0.64 报价，自认为公允价 0.63。
2. 一个知情人知道真实概率是 0.85，于是持续按 0.64 买入。
3. 做市商连续被单边吃单，库存变成大额空头。
4. 消息公开，价格跳到 0.85。**做市商每份亏 0.21，价差赚的 0.02 完全不够看。**

理性的做市商有三种反应，都对用户不利：
- **拉宽价差**（你的成本上升）
- **减少挂单量**（深度变薄）
- **完全撤出**（盘口消失）

**所以逆向选择的成本最终一定由普通用户承担**，形式是更差的价格。

## Concrete Example | 具体例子

2024 年 Polymarket 大选合约的"Théo"案例通常被当作价格发现的胜利，但从做市商视角看是**教科书级的逆向选择**：

一个掌握了更好信息（自委托的邻居效应民调）的交易者，持续单向建立巨额头寸。跟他成交的每一个人 —— 包括做市商 —— 都在系统性地站在错误一边。他最终盈利数千万美元，**而这笔钱正是从对手方口袋里出来的**。

同一件事，两种读法：
- **对市场**：信息被注入价格，价格发现成功。
- **对做市商**：一次教科书级的逆向选择事件，代价是巨额亏损。

**这两种读法都对，而且必须同时成立** —— 价格发现的收益，正是由承担逆向选择的人支付的。

## Common Misconceptions | 常见误解

- **误解一："逆向选择就是内幕交易。"** 内幕交易是其中一种，但合法的信息优势（更好的模型、更快的数据、更专业的判断）造成的逆向选择同样存在，而且完全合法。
- **误解二："提高手续费能补偿逆向选择。"** 手续费对所有人一视同仁，而逆向选择只来自知情人。加手续费只会赶走没信息的流动性，**让剩下的人里知情人比例更高** —— 反而恶化。
- **误解三："这只是做市商的问题。"** 它最终以更宽的价差和更薄的深度转嫁给每一个用户。

## In Practice | 实战里怎么用

设计或评估一个事件市场，先给它的**信息不对称程度**打分：

| 事件类型 | 信息不对称 | 可做市性 |
|---|---|---|
| 公开数据发布（CPI、失业率） | 低 | 好 |
| 选举结果 | 中（民调可买） | 中 |
| 公司具体决策、人事任免 | **高** | 差 |
| 小圈子内部事件 | **极高** | 基本不可做市 |

**信息不对称高的市场，靠补贴堆不出流动性。** 唯一有效的手段是从机制上降低不对称：更权威的公开数据源、更严格的上市审查、更清晰的合约语义。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说做市商的每一笔成交都自带坏消息？
  A: 挂单只在对对方有利时才被吃掉，所以成交本身就是'对方可能知道得更多'的信号。
- Q: 为什么加手续费不能解决逆向选择？
  A: 手续费对所有人一视同仁，会先赶走无信息的流动性，反而提高剩余交易者中知情人的比例，使问题恶化。
- Q: 为什么事件市场的逆向选择比股票市场更严重？
  A: 标的是现实事件，总有人先知道；且多数辖区的内幕交易法不适用于非证券的事件合约。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = market-maker; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
