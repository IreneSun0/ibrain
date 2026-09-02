---
id: "concept:layer-1"
type: concept
title: L1
title_zh: 第一层/基础公链
title_en: L1
aliases:
  - L1
  - Layer 1
  - 第一层
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
  - id: "protocol:ethereum"
    rel: instantiated-by
  - id: "protocol:tron"
    rel: instantiated-by
prerequisites:
  - "concept:blockchain"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# L1 | 第一层/基础公链

## Executive Definition / Chinese Explanation | 定义与解释

**Layer 1 | 一层网络** = 拥有自己[[consensus|共识]]与安全性的基础区块链。它是最终的结算与安全来源，其他一切都建在它上面。

判据很简单：**它的安全来自自己的验证者/矿工，而不是继承自别人。**

## Why This Matters | 为什么重要

对事件市场，选哪条 L1 结算是一个**风险决策，不是技术偏好**：

- **抵押品的安全性**最终取决于该 L1 的共识安全（见 [[proof-of-stake]]）。
- **事件揭晓时刻的可用性**取决于该 L1 的吞吐与拥堵表现。
- **最终性类型**决定了结算与提现之间的风险窗口。

**"资金在链上"这句话不说明在哪条链上** —— 而不同 L1 的安全预算可能差几个数量级。

## How It Works | 机制怎么运转

L1 的三难权衡（区块链三元悖论）：

```
        去中心化
         /    \
        /      \
   安全 ------- 可扩展
```

**你只能优先其中两个。** 不同 L1 的选择：

| 取向 | 代价 | 对事件市场 |
|---|---|---|
| 去中心化 + 安全 | 吞吐低、费用高 | **小额头寸不经济** |
| 安全 + 可扩展 | 验证者较少 | 可用，需评估集中度 |
| 去中心化 + 可扩展 | 安全预算较低 | **抵押品风险上升** |

**事件市场的实际选择通常落在第二行**，或者干脆用 L1 做安全锚、L2 做执行（见 [[layer-2]]）。

## Concrete Example | 具体例子

同一份事件合约放在不同 L1 上的属性差异：

| | 高安全低吞吐 L1 | 高吞吐 L1 | L2 / 侧链 |
|---|---|---|---|
| 单笔成本 | $2–50 | $0.001–0.01 | $0.01–0.1 |
| 安全来源 | 自身（最强） | 自身（视质押规模） | **可能不继承 L1** |
| 拥堵时 | **不可用** | 较好 | 较好 |
| 适合规模 | 大额 | 全部 | 全部 |

**注意第二行的第三列**：侧链有自己的验证者集，**抵押品安全取决于它而不是以太坊**。

**这是"在链上"这三个字最常掩盖的一件事。**

## Common Misconceptions | 常见误解

- **误解一："所有 L1 安全性相近。"** 安全预算（质押总额或算力）可能差几个数量级。
- **误解二："L1 越去中心化越好。"** 去中心化是成本，买的是抗审查与抗操纵。**买多少取决于你在防谁。**
- **误解三："选链是技术团队的事。"** 它直接决定你的抵押品有多安全、以及关键时刻能不能动 —— 是风险决策。

## In Practice | 实战里怎么用

评估事件市场的结算 L1，四问：

1. **安全预算多大？** 质押总额或算力，相对链上锁仓价值。
2. **最终性类型？** 确定性还是概率性。
3. **验证者集中度？** 前 5 大占比，注意 1/3 阈值。
4. **历史拥堵表现？** 找一个高峰日看费用与延迟。

**第 4 问用一句话检验**：**上一次全网最忙的那天，这条链上的事件市场还能正常结算吗？**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 判断一条链是不是 L1 的简单判据是什么？
  A: 它的安全来自自己的验证者/矿工，而不是继承自别的链。
- Q: 区块链三元悖论说的是什么？事件市场通常怎么取舍？
  A: 去中心化、安全、可扩展三者只能优先两个。事件市场通常选安全+可扩展（需评估集中度），或用 L1 做安全锚、L2 做执行。
- Q: '资金在链上'这句话最常掩盖什么？
  A: 在哪条链上 —— 侧链有自己的验证者集，抵押品安全取决于它而非以太坊，安全预算可能差几个数量级。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
