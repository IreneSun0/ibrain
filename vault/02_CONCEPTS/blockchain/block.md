---
id: "concept:block"
type: concept
title: Block
title_zh: 区块
title_en: Block
aliases:
  - 区块
status: reviewed
importance: tier-2
domains:
  - blockchain
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
  - id: "concept:blockchain"
    rel: component-of
prerequisites:
  - "concept:transaction"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Block | 区块

## Executive Definition / Chinese Explanation | 定义与解释

**Block | 区块** = 一批被打包在一起、一次性写入链的交易，附带指向前一个区块的哈希。

**"指向前一个"这一点是全部**：它把区块串成链，改写任何一个历史区块都会让之后所有区块的哈希失效 —— 这就是不可篡改的技术来源。

## Why This Matters | 为什么重要

区块是链上世界的**时间单位**，而时间单位的长短直接影响事件市场的体验：

- **出块时间** —— 决定你的交易最快多久被处理。
- **区块容量** —— 决定拥堵时谁被挤出去。
- **确认数** —— 结算安全性的度量单位（见 [[double-spending]]）。

**事件揭晓的那一刻，所有人同时提交交易，而区块容量是固定的** —— 于是费用竞价飙升，处理被推迟（见 [[gas]]）。**这是链上事件市场最集中的性能压力点。**

## How It Works | 机制怎么运转

区块的核心结构：

```
区块头:  前一区块哈希 · 时间戳 · 状态根 · 难度/验证者签名
区块体:  交易列表
```

**"前一区块哈希"构成链式结构**：改动区块 N 的任何一个字节 → 区块 N 的哈希变了 → 区块 N+1 里记录的"前一哈希"对不上 → N+1 之后全部失效。

**所以改写历史的成本随深度指数上升** —— 这就是"确认数越多越安全"的原理。

## Concrete Example | 具体例子

事件揭晓时刻的区块争夺：

```
判定完成的那个区块之后:
  数千个地址同时提交 redeem 交易
  区块容量固定 → 只有出价最高的进得去
  gas 价格飙升 5–20 倍
  小额头寸的领取变得不经济
```

**这不是理论**：任何一次高关注度事件的结算窗口都会出现这个形态。

**实用应对**：**领取赔付不必抢在第一分钟。** 判定结果已经确定，等 gas 回落再领，省下的钱可能超过等待的机会成本。

## Common Misconceptions | 常见误解

- **误解一："区块越快越好。"** 出块太快会增加分叉概率，降低最终性质量。**速度与安全是权衡。**
- **误解二："交易一进区块就安全了。"** 进区块 ≠ 最终性。概率性最终性的链上仍可能被重组。
- **误解三："区块容量可以随便加大。"** 容量增加提高节点运行门槛，长期削弱去中心化 —— 这是长期争论的核心。

## In Practice | 实战里怎么用

对链上事件市场的两条实用推论：

1. **判定后不要抢领** —— 等拥堵过去，gas 可能便宜 5–10 倍。
2. **重要操作避开高峰** —— 授权、存入这类不紧急的操作，选在链空闲时做。

**再记一个数**：**你所用链的出块时间 × 平台要求的确认数 = 你的钱最快多久能动。** 这个数字在你需要紧急调仓时才会显出重要性。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 区块链不可篡改的技术来源是什么？
  A: 每个区块头包含前一区块的哈希，改动任一历史区块会让之后所有区块的哈希失效，改写成本随深度指数上升。
- Q: 为什么事件揭晓时刻是链上事件市场最集中的性能压力点？
  A: 所有人同时提交交易而区块容量固定，费用竞价飙升，小额头寸的领取变得不经济。
- Q: 为什么'区块越快越好'是错的？
  A: 出块太快增加分叉概率、降低最终性质量；速度与安全是权衡关系。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
