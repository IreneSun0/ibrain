---
id: "concept:broker"
type: concept
title: Broker
title_zh: 经纪商
title_en: Broker
aliases:
  - 经纪商
status: reviewed
importance: tier-2
domains:
  - financial-markets
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
  - id: "concept:dealer"
    rel: contrasts-with
    note: 代理传单不担价格风险 vs 用自有资产负债表直接成为对手方
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场结构
---
# Broker | 经纪商

## Executive Definition / Chinese Explanation | 定义与解释

**Broker | 经纪商** = 代客户执行交易的中介。它**不持有头寸**，只赚佣金。

与[[dealer|交易商]]的区别是全部：经纪商是代理（agent），赚佣金，不担方向风险；交易商是自营（principal），用自己的账簿接你的单，赚价差、担风险。

## Why This Matters | 为什么重要

经纪商与交易商的区分，决定了**利益冲突在哪里**。

- **纯经纪商**：它的收入与你交易的方向无关，只与成交量有关 → 冲突较小，但它有动机让你多交易。
- **交易商**：它是你的对手方 → **你亏就是它赚**，冲突直接。

**在事件市场里这条线常常是模糊的**：很多平台既撮合又自营做市（有场馆设有自有做市子公司）。**你需要知道自己对面的是谁。**

## How It Works | 机制怎么运转

经纪商提供的四项功能：

1. **市场接入** —— 连到你自己连不上的场所。
2. **订单路由** —— 决定把你的单送到哪（见 [[smart-order-routing]]）。
3. **托管与清算** —— 代你持有资产、完成结算。
4. **融资** —— 保证金账户。

**第 2 项是最容易产生隐性冲突的地方**：路由决策可以为你优化（最优价格），也可以为经纪商优化（订单流付费、内部撮合）。**"最优执行"义务就是针对这一点设立的。**

## Concrete Example | 具体例子

事件市场的分发格局里，经纪商角色正在成型：

- 持牌事件交易所通过券商 App 向零售分发合约 —— **券商在这里是经纪商**，它把交易所的产品送到用户面前。
- 这条链的经济含义：**交易所拿到订单流，券商拿到分成，用户拿到便利。**
- **风险含义**：用户面对的界面是券商的，但产品规则、裁决机制是交易所的 —— **出了争议，你要找谁？**

**这就是分发链条变长之后的典型问题：便利提升，责任链模糊。**

## Common Misconceptions | 常见误解

- **误解一："经纪商和交易商差不多。"** 一个是代理不担风险，一个是对手方直接与你对赌。**性质完全不同。**
- **误解二："零佣金 = 免费。"** 收入可能来自订单流付费、价差、或利息。**免费的往往在别处收。**
- **误解三："经纪商必然为我争取最优价格。"** 取决于是否有最优执行义务，以及是否被有效监管。

## In Practice | 实战里怎么用

用任何交易入口前，弄清三件事：

1. **我的对手方是谁？** 是市场上的其他人，还是这家机构自己？
2. **它怎么赚钱？** 佣金 / 价差 / 订单流付费 / 利息？
3. **出争议找谁？** 界面提供方还是产品发行方？

**第 3 问在分发链条变长时特别重要** —— 界面是一家，规则是另一家，裁决可能是第三家。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 经纪商与交易商的根本区别是什么？
  A: 经纪商是代理，赚佣金不担方向风险；交易商是自营，用自己的账簿做你的对手方，赚价差担风险。
- Q: 经纪商最容易产生隐性冲突的功能是哪一项？
  A: 订单路由 —— 可以为客户优化最优价格，也可以为自己优化（订单流付费、内部撮合），最优执行义务即针对此。
- Q: 分发链条变长带来的典型问题是什么？
  A: 便利提升但责任链模糊：界面是一家、产品规则是另一家、裁决可能是第三家，出争议时用户不知道找谁。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
