---
id: "concept:gas"
type: concept
title: Gas
title_zh: 链上计算/资源费
title_en: Gas
aliases:
  - 链上计算
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
    rel: mechanism-of
    note: "计量并定价稀缺计算/存储资源, 防垃圾交易"
prerequisites:
  - "concept:transaction"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Gas | 链上计算/资源费

## Executive Definition / Chinese Explanation | 定义与解释

**Gas | 燃料费** = 在链上执行计算与存储所要付的费用。它给"区块空间"这个稀缺资源定价。

**它不是平台收的手续费**，而是付给验证者/矿工的、用来竞价进入下一个区块的费用。

## Why This Matters | 为什么重要

Gas 是链上事件市场的**隐性成本项**，而且它在最坏的时刻最贵：

**事件揭晓的那一刻，全网最拥堵。** 所有人同时想调整头寸、同时想领取赔付 —— gas 价格飙升，而你正好最需要交易。

**这是选择结算链时的核心考量**（见 [[consensus]]）：一条平时够快够便宜的链，在大选夜可能贵到让小额头寸的领取变得不经济。

## How It Works | 机制怎么运转

```
交易费 = gas 用量 × gas 价格
```

- **gas 用量** —— 由操作复杂度决定（转账便宜，合约交互贵，批量操作更省）。
- **gas 价格** —— 由供需竞价决定，拥堵时飙升。

**事件市场的三个 gas 敏感点**：
1. **授权（approve）** —— 一次性成本。
2. **铸造/合并完备集** —— 需要批量操作，这正是 [[erc-1155]] 批量转移的价值所在。
3. **判定后领取赔付** —— **全网同时发生，最贵。**

**第 3 点是很多小额头寸的实际问题**：赔付 $20，gas 花 $15。

## Concrete Example | 具体例子

同一笔事件合约操作，三条链的成本量级：

| 链 | 平静期 | 拥堵期 | 对 $100 头寸的影响 |
|---|---|---|---|
| Ethereum L1 | $2–10 | **$50+** | **不经济** |
| L2 / 侧链 | $0.01–0.1 | $0.5 | 可接受 |
| 高吞吐 L1 | $0.001 | $0.01 | 可忽略 |

**这就是为什么事件市场几乎都不在以太坊主网结算** —— Polymarket 选 Polygon，不是技术偏好，是**小额头寸在 L1 上根本无法成立**。

**gas 成本直接决定了这个市场能服务多小的用户。**

## Common Misconceptions | 常见误解

- **误解一："gas 是平台收入。"** 它付给验证者，平台通常拿不到。
- **误解二："gas 便宜就没问题。"** 要看**拥堵时**的价格，而拥堵恰好发生在事件揭晓时。
- **误解三："gas 只影响小额用户。"** 它也影响做市商：频繁调整报价在高 gas 环境下不可行，直接导致价差变宽。

## In Practice | 实战里怎么用

评估一个链上事件市场的实际成本，算全四项：

```
总成本 = 价差 + 滑点 + 平台手续费 + gas(开仓 + 平仓 + 领取)
```

**特别测一次拥堵期**：找一个历史上的高峰时刻，看那天的 gas 价格 —— **那才是你在关键时刻要付的钱。**

**对小额头寸的判据**：如果 `gas 总额 / 头寸规模 > 5%`，这个平台对你这个规模是不经济的。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: gas 为什么在最坏的时刻最贵？
  A: 事件揭晓时全网最拥堵，所有人同时调整头寸和领取赔付，gas 竞价飙升，而那正是你最需要交易的时刻。
- Q: 为什么事件市场几乎都不在以太坊主网结算？
  A: L1 的 gas 成本让小额头寸在经济上不成立；Polygon 等低成本链是必要选择而非技术偏好。
- Q: gas 如何影响做市商？
  A: 高 gas 环境下频繁调整报价不可行，做市商只能拉宽价差 —— gas 成本会转化为用户的交易成本。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
