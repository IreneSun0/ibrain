---
id: "concept:layer-2"
type: concept
title: L2
title_zh: 第二层扩容网络
title_en: L2
aliases:
  - L2
  - Layer 2
  - 第二层扩容网络
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
  - id: "protocol:x-layer"
    rel: instantiated-by
    note: OKX 系 Ethereum L2 (OKB 为唯一 gas)
  - id: "protocol:mantle"
    rel: instantiated-by
    note: Bybit 生态系 Ethereum L2
prerequisites:
  - "concept:layer-1"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# L2 | 第二层扩容网络

## Executive Definition / Chinese Explanation | 定义与解释

**Layer 2 | 二层网络** = 把交易的执行搬到链下（或旁链）处理，只把结果与证明提交回主链（L1）的扩容方案。

一句话：**L1 负责安全与最终性，L2 负责吞吐与成本。**

## Why This Matters | 为什么重要

L2 是事件市场绕不开的一层，原因是[[gas|成本]]：

主网 L1 上一笔操作可能几美元到几十美元，而事件市场的典型头寸可能只有几十到几百美元 —— **L1 的成本结构直接排除了零售规模。**

**Polymarket 选择 Polygon 结算就是这个逻辑的直接体现**：它需要一个足够便宜、足够快、且有足够安全保证的执行环境。

## How It Works | 机制怎么运转

两大类 L2，安全模型不同：

| 类型 | 机制 | 提现等待 | 安全来源 |
|---|---|---|---|
| **Optimistic Rollup** | 默认相信，留挑战期 | **数天** | 有人会挑战错误状态 |
| **ZK Rollup** | 提交有效性证明 | 分钟到小时 | **数学证明** |
| 侧链 | 独立共识 | 视桥而定 | **自身验证者，不继承 L1 安全** |

**注意第三行**：侧链严格说不是 L2 —— 它有自己的验证者集，**不继承 L1 的安全性**。Polygon PoS 就属于这一类。

**这对事件市场的实际含义**：你的抵押品的安全性取决于该侧链的验证者集，而不是以太坊。**这是一个需要单独评估的风险，而不是"反正在链上"。**

## Concrete Example | 具体例子

同一笔事件合约头寸在三种环境下的属性：

| | L1 | ZK Rollup | 侧链 |
|---|---|---|---|
| 单笔成本 | $2–50 | $0.05 | $0.01 |
| 最终性 | 最强 | 强（继承 L1） | **取决于自身验证者** |
| 拥堵时可用性 | 差 | 较好 | 较好 |
| 桥风险 | 无 | 较低 | **跨链桥是历史上最大的攻击面之一** |

**最后一行值得单独看**：把资金从 L1 桥到侧链，桥本身就是一个攻击面。**"资金在链上"并不说明在哪条链上、经过了什么桥。**

## Common Misconceptions | 常见误解

- **误解一："所有 L2 安全性一样。"** ZK 和 Optimistic 的安全模型不同；侧链根本不继承 L1 安全。
- **误解二："L2 就是更便宜的以太坊。"** 便宜的代价是不同的信任假设，需要单独评估。
- **误解三："在链上就安全。"** 要问**哪条链、什么共识、桥是谁的**（见 [[bridge]]）。

## In Practice | 实战里怎么用

评估一个事件市场的结算环境，四问：

1. **结算在哪条链？** L1、Rollup、还是侧链？
2. **安全从哪来？** 继承 L1，还是自己的验证者集？
3. **验证者集中度多高？** 少数实体控制多数权益 = 单点风险。
4. **资金怎么进出？** 经过什么桥？桥审计过吗？

**第 4 问最容易被跳过，也是历史上损失最集中的地方。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: L1 与 L2 的分工是什么？
  A: L1 负责安全与最终性，L2 负责吞吐与成本。
- Q: 侧链为什么严格说不是 L2？
  A: 它有自己的验证者集，不继承 L1 的安全性；抵押品的安全取决于该侧链自身，需要单独评估。
- Q: 评估结算环境时最容易被跳过、损失却最集中的一问是什么？
  A: 资金经过什么桥、桥是否审计过 —— 跨链桥是历史上最大的攻击面之一。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
