---
id: "concept:maker"
type: concept
title: Maker
title_zh: 挂单方/提供流动性者
title_en: Maker
aliases:
  - 挂单方
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
related:
  - id: "concept:taker"
    rel: contrasts-with
    note: 挂单等待、赚价差/返佣 vs 立即成交、付更高费用与冲击成本
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Maker | 挂单方/提供流动性者

## Executive Definition / Chinese Explanation | 定义与解释

**Maker | 挂单方 / 流动性提供者** = 挂出限价单、等待别人来成交的一方。它"造出"了订单簿上的那一层。

对应的是 taker（吃单方）。区分它们的**唯一标准是谁先挂在簿子上**，跟你是买还是卖无关。

## Why This Matters | 为什么重要

几乎所有交易所都对 maker 收更低的费率，甚至给返佣（负费率）。原因很直接：**maker 提供了流动性这个公共品，交易所要付钱买它。**

在事件市场里这件事被放大了：有几万个长尾合约需要有人报价，而自然的双向需求几乎不存在。**maker 激励设计基本决定了一个事件市场平台的生死** —— 没有人挂单，平台上就只有一片空盘口。

## How It Works | 机制怎么运转

做 maker 的经济学是三项相减：

```
收益 = 价差收入 + maker 返佣
成本 = 存货风险损失 + 逆向选择损失
```

- **价差收入**：每完成一次"低买高卖"的往返，赚一个价差。
- **maker 返佣**：平台为激励挂单支付的补贴。
- **存货风险**：接了单还没对冲掉时价格反向。
- **逆向选择**：被有信息的人专门挑走对他有利的那一边。

**当逆向选择损失长期大于价差收入时，理性的 maker 就撤了** —— 这就是很多新平台"上线时有做市，三个月后盘口全空"的原因。

## Concrete Example | 具体例子

平台给 maker 返佣 0.5 个基点、taker 收 2 个基点，一个做市商在某事件合约上：

- 挂 0.62 买 / 0.64 卖，一天完成 200 次往返，每次 1,000 份。
- **价差收入**：0.02 × 1,000 × 200 = $4,000。
- **返佣**：约 $130。
- 但当天有一次内幕消息，它在消息前被连续吃掉 30,000 份 YES，价格随后从 0.63 跳到 0.78 —— **单次逆向选择损失约 $4,500**。

**这一天净亏损。** 一次信息事件就抹掉了一整天的价差收入 —— 这就是为什么做市商对"这个市场有没有内幕"极度敏感，也是它们在裁决临近时集体撤单的原因。

## Common Misconceptions | 常见误解

- **误解一："maker 是稳赚的。"** 它赚的是概率优势，单次可以巨亏。逆向选择是它的头号杀手。
- **误解二："maker/taker 由买卖方向决定。"** 由**谁先挂在簿子上**决定。挂限价买单是 maker，市价买入是 taker。
- **误解三："提高返佣就能买来流动性。"** 只在逆向选择可控时有效。信息不对称严重的市场，补贴再高做市商也不来 —— 因为亏的比补贴多。

## In Practice | 实战里怎么用

设计或评估一个事件市场的 maker 激励，四个问题按顺序问：

1. **做市商能不能对冲？** 有没有相关的期货/其他场所可以转移存货风险？
2. **逆向选择有多严重？** 这类事件存在内幕的可能性有多高？
3. **返佣够不够覆盖 (2)？** 算清楚，不要拍脑袋。
4. **裁决风险谁承担？** 裁决出错时做市商的头寸怎么处理？

**第 4 条最容易被漏掉，也最容易让做市商在关键时刻集体退出。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: maker 和 taker 的区分标准是什么？
  A: 谁先挂在订单簿上。先挂限价单等成交的是 maker，主动吃掉已有挂单的是 taker，与买卖方向无关。
- Q: 做市商的收益和成本各由哪几项构成？
  A: 收益 = 价差收入 + maker 返佣；成本 = 存货风险损失 + 逆向选择损失。
- Q: 为什么单纯提高 maker 返佣未必能买来流动性？
  A: 返佣只在逆向选择可控时有效。信息不对称严重时做市商的损失远超补贴，理性选择是不来。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = order-book; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
