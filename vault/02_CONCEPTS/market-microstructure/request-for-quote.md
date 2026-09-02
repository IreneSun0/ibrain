---
id: "concept:request-for-quote"
type: concept
title: RFQ
title_zh: 询价交易
title_en: RFQ
aliases:
  - RFQ
  - Request for Quote
  - 询价交易
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
  - id: "concept:central-limit-order-book"
    rel: contrasts-with
    note: 定向询价保护大单意图 vs 公开盘口透明但暴露
prerequisites:
  - "concept:market-maker"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# RFQ | 询价交易

## Executive Definition / Chinese Explanation | 定义与解释

**RFQ (Request for Quote) | 询价** = 不在公开盘口下单，而是私下向一个或几个做市商问："这个规模你给我什么价？"

它是大额交易的标准做法，因为**在公开盘口下大单等于先告诉全市场你要买什么**（见 [[price-impact]]）。

## Why This Matters | 为什么重要

公开订单簿对大额交易有一个结构性缺陷：**暴露即成本。**

你挂一个 $5M 的买单，所有人都看见了；价格在你成交前就已经跑掉。RFQ 把这个过程私有化：只有被问的做市商知道，成交完成后才公开（或根本不公开）。

**在事件市场，RFQ 的价值被放大**，因为长尾合约的公开盘口极薄 —— 一笔机构规模的单子在公开簿上根本装不下（见 [[liquidity]]）。

## How It Works | 机制怎么运转

RFQ 的流程与权衡：

```
1. 你发出询价：标的 + 规模 + 方向（有时隐藏方向）
2. 若干做市商各自报价
3. 你选一个成交，或全部拒绝
```

**核心权衡**：
- **问得越多** → 价格竞争越充分，但**信息泄漏越广**（每个被问的人都知道有人要买）。
- **问得越少** → 泄漏少，但可能拿不到最好的价。

**隐藏方向（two-way RFQ）** 是常见对策：让对方同时报买价和卖价，你再选边。代价是报价会更宽。

## Concrete Example | 具体例子

一笔 $2M 的事件合约需求，两条路径：

| | 公开盘口 | RFQ |
|---|---|---|
| 可见性 | 全市场立刻可见 | 仅被询价方 |
| 预期成交价 | 吃穿多档，均价 0.68 | 单一价格 0.655 |
| 价格冲击 | +8 分，且不会完全恢复 | 接近零（若不公开） |
| 确定性 | 部分成交风险 | 全额或不成交 |

**RFQ 省下的 2.5 分（约 $50k）就是"不暴露"的价值。**

代价是：你把执行交给了少数几个对手方，**而他们知道你想做什么**。RFQ 不是没有信息泄漏，是把泄漏范围从"全市场"缩小到"被问的几家"。

## Common Misconceptions | 常见误解

- **误解一："RFQ 一定比公开盘口便宜。"** 在深度充足的盘口上，公开成交往往更便宜（竞争更充分）。RFQ 的优势只在盘口装不下你的时候。
- **误解二："RFQ 没有信息泄漏。"** 有 —— 只是范围小。被问的做市商可以据此调整自己的头寸。
- **误解三："RFQ 是机构专属。"** 越来越多平台把 RFQ 做进散户界面（"报价成交"模式）。

## In Practice | 实战里怎么用

决定走公开盘口还是 RFQ，一条判据：

> **你的规模相对这个盘口的 ±1% 深度是多少？**

- **< 1 倍** → 走公开盘口，更便宜。
- **1–5 倍** → 拆单或 RFQ 都行，比一下。
- **> 5 倍** → **公开盘口装不下你**，RFQ 或分批。

再加一条纪律：**做 RFQ 时问 3–5 家，不要问 10 家。** 超过 5 家，泄漏的边际成本通常已经超过价格竞争的边际收益。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么大额交易要走 RFQ 而不是公开盘口？
  A: 公开挂大单等于先告诉全市场你的意图，价格在成交前就跑掉；RFQ 把可见范围限制在被询价的少数做市商。
- Q: RFQ 的核心权衡是什么？
  A: 问得越多价格竞争越充分但信息泄漏越广；问得越少泄漏小但可能拿不到最好的价。通常 3-5 家是平衡点。
- Q: 怎么判断该走公开盘口还是 RFQ？
  A: 看你的规模相对该盘口 ±1% 深度的倍数：小于 1 倍走公开簿，大于 5 倍公开簿装不下，应走 RFQ 或分批。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
