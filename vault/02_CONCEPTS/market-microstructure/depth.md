---
id: "concept:depth"
type: concept
title: Depth
title_zh: 盘口深度
title_en: Depth
aliases:
  - 盘口深度
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
related: []
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Depth | 盘口深度

## Executive Definition / Chinese Explanation | 定义与解释

**Depth | 市场深度** = 在偏离当前价格一定范围内，订单簿两侧总共挂了多少钱。

价差告诉你"一手的成本"，深度告诉你"**多大的单子能进去而不把价格推走**"。对任何有规模的资金来说，深度比价格重要。

## Why This Matters | 为什么重要

深度是"这个市场能不能承载机构"的直接判据。

一个日成交额 100 万美元的事件合约，如果深度只有几千美元，那它对一个想配置 50 万的基金就是不可用的 —— **不是价格不合适，是根本进不去，进去也出不来。**

预测市场想拿到机构资金，深度是绕不过去的门槛，而它恰恰是这类市场最稀缺的东西。

## How It Works | 机制怎么运转

深度通常按"距中间价 X%"分档统计：

```
±0.5%  →  $1,200
±1%    →  $3,500
±2%    →  $9,000
±5%    →  $31,000
```

读法：你想成交 $3,500，大约会把价格推动 1%。想成交 $31,000，会推动 5%。

**深度的三个维度都要看：**
- **静态深度** — 此刻挂了多少；
- **韧性（resilience）** — 被大单吃掉后多久恢复；
- **在场率** — 消息冲击时报价还在不在。

只报第一个的平台数据，参考价值有限。

## Concrete Example | 具体例子

两个都显示"日成交 $2M"的事件合约：

- **A**：±1% 深度 $40,000，大单吃穿后 30 秒恢复，消息后仍有报价。
- **B**：±1% 深度 $800，成交量主要来自少数账户高频对倒，消息一出报价全撤。

**成交量相同，可用性天差地别。** A 能接一笔 $50k 的机构单，B 连 $5k 都会明显推动价格。

这就是为什么"成交量"是事件市场最容易被包装的指标 —— 而深度和韧性很难伪造。

## Common Misconceptions | 常见误解

- **误解一："成交量大 = 深度好。"** 对倒和刷量能造出成交量，造不出深度。
- **误解二："深度是静态属性。"** 它随时间、消息、临近裁决剧烈变化，且在你最需要时最薄。
- **误解三："看总挂单量就够了。"** 挂在离盘口 20 分之外的单不构成可用深度，必须按距中间价的档位统计。

## In Practice | 实战里怎么用

判断一个盘口能不能接你的单，只需要一个动作：**按你的实际下单规模，把订单簿逐层吃一遍，算加权成交均价。**

```
预期滑点 = (加权成交均价 − 中间价) / 中间价
```

超过 1% 就该拆单或换场所；超过 3% 基本说明这个盘口装不下你。

再叠加一次时序采样：抓一周的深度数据，看它在消息时刻的最低点 —— **那个最低点才是你真正能依赖的深度。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 深度的三个维度是什么？只看哪一个会误判？
  A: 静态深度、韧性（恢复速度）、在场率（消息时是否还报价）。只看静态深度会严重高估可用流动性。
- Q: 为什么成交量是容易被包装的指标，而深度不是？
  A: 对倒和刷量能制造成交量却造不出真实挂单深度，深度需要真金白银持续暴露在被吃单的风险中。
- Q: 怎么量化'这个盘口能不能接我的单'？
  A: 按实际规模逐层吃订单簿算加权均价，得出预期滑点；再看消息时刻的深度最低点。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = order-book; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
