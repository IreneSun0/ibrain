---
id: "concept:tron-bandwidth"
type: concept
title: Bandwidth (TRON)
title_zh: TRON带宽资源
title_en: Bandwidth (TRON)
aliases:
  - Bandwidth (TRON)
  - TRON带宽资源
status: reviewed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
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
  - "source:2026-08-26-tron-dao-bandwidth-and-energy"
related:
  - id: "concept:tron-energy"
    rel: see-also
    note: "TRON 双资源模型 — 带宽计字节, 能量计算力"
prerequisites:
  - "concept:transaction"
import_origin: xlsx-learning-map+manual
import_category: TRON
---
# Bandwidth (TRON) | TRON带宽资源

## Executive Definition / Chinese Explanation | 定义与解释

**TRON Bandwidth | 带宽** = TRON 上按**交易数据大小**收取的资源，与按计算量收取的 [[tron-energy|Energy]] 是两种独立资源。

简单转账主要消耗 Bandwidth；调用合约同时消耗 Bandwidth 和 Energy。

## Why This Matters | 为什么重要

把"数据大小"和"计算量"分开计价，是 TRON 资源模型的核心设计。

**它的实际效果**：简单转账（数据小、无计算）几乎免费，而复杂合约调用才真正花钱。**这精准补贴了稳定币转账这个最高频的场景** —— 也是 TRON 成为 USDT 主要轨道的技术原因之一。

**对比以太坊**：EVM 只有一种 gas，数据与计算混在一起计价，因此简单转账也要付可观成本。

## How It Works | 机制怎么运转

每个账户每天获得**免费 Bandwidth 额度**；额度不够时：

```
1. 用免费额度        (每日恢复)
2. 质押 TRX 获得更多  (每日恢复)
3. 烧 TRX 直接支付    (兜底)
```

**三层递进的设计意图很清楚**：让轻度用户几乎零成本，让重度用户可以通过质押把成本固定下来，最后才是按次付费。

**这是一个把"用户分层"直接写进协议的资源模型** —— 大多数链没有这一层。

## Concrete Example | 具体例子

三种操作的资源消耗对照：

| 操作 | Bandwidth | Energy | 典型成本 |
|---|---|---|---|
| TRX 转账 | 少 | 无 | **免费额度内** |
| USDT (TRC-20) 转账 | 中 | **有**（合约调用） | 低 |
| 复杂合约交互 | 中 | **高** | 中 |

**注意第二行**：USDT 转账是合约调用，所以要消耗 Energy —— **这就是为什么"TRON 转 USDT 免费"这个说法不准确**：免费的是 Bandwidth 那部分，Energy 那部分仍要付。

**这也解释了 Energy 租赁市场为什么存在**（见 [[tron-energy-delegation]]）：大量用户需要的正是 USDT 转账所需的那一点 Energy。

## Common Misconceptions | 常见误解

- **误解一："Bandwidth 就是网速。"** 它是链上资源配额，与网络带宽无关。
- **误解二："有免费额度就完全免费。"** 额度有限且每日恢复；USDT 转账还要另付 Energy。
- **误解三："资源模型只是技术细节。"** 它直接决定了哪类使用被补贴 —— **这是产品决策，不是工程细节。**

## In Practice | 实战里怎么用

理解 TRON 资源模型对事件市场用户的一个实用推论：

**如果你频繁在 TRON 上转移 USDT 作为事件市场的出入金**，你需要的是 Energy 而不是 Bandwidth。三个选择：

1. **烧 TRX** —— 最简单，成本略高。
2. **质押 TRX** —— 高频划算，但资本被锁定。
3. **租赁 Energy** —— 按需购买，无需长期锁仓（见 [[tron-energy-delegation]]）。

**先算清楚你每月的转账笔数，再选** —— 三者的盈亏平衡点差得很远。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: Bandwidth 与 Energy 的分工是什么？
  A: Bandwidth 按交易数据大小收取，Energy 按计算量收取；简单转账主要消耗 Bandwidth，合约调用两者都要。
- Q: 为什么'TRON 转 USDT 免费'不准确？
  A: USDT 转账是合约调用，Bandwidth 部分可能在免费额度内，但 Energy 部分仍需支付。
- Q: TRON 资源模型的三层递进设计意图是什么？
  A: 免费额度让轻度用户零成本，质押让重度用户固定成本，烧币兜底 —— 把用户分层写进了协议。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
- [[src-2026-08-26-tron-dao-bandwidth-and-energy]] — <https://developers.tron.network/docs/bandwidth-and-energy>
