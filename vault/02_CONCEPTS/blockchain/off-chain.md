---
id: "concept:off-chain"
type: concept
title: Off-chain
title_zh: 链下
title_en: Off-chain
aliases:
  - Off-chain
  - 链下
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
  - id: "concept:on-chain"
    rel: contrasts-with
    note: 快而便宜但信任假设强 vs 可验证可组合但受链的速度与成本限制
prerequisites:
  - "concept:blockchain"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Off-chain | 链下

## Executive Definition / Chinese Explanation | 定义与解释

**Off-chain | 链下** = 不写进区块链共识状态的部分：撮合引擎、用户数据库、风控系统、以及大多数计算。

链下不是"不安全"的同义词。**关键问题从来不是"在哪里算"，而是"谁能作恶、作恶了能不能被发现"。**

## Why This Matters | 为什么重要

事件市场的主流架构（hybrid）就是一次刻意的链下/链上切分（见 [[hybrid-exchange-architecture]]）：

| 在链下 | 为什么 |
|---|---|
| 撮合 | 需要毫秒级延迟，上链太慢太贵 |
| 用户身份 / KYC | 隐私，且无需共享 |
| 风控计算 | 计算量大，无需他人验证 |

| 在链上 | 为什么 |
|---|---|
| 资金托管 | 必须不可挪用 |
| 结算执行 | 必须可验证、可自动执行 |

**这个切分不是妥协，是对每个组件分别问"多方互不信任 + 需要共享状态吗"的结果。**

## How It Works | 机制怎么运转

链下部分的风险有一个共同特征：**难以被外部验证。**

| 链下组件 | 风险 | 能验证吗 |
|---|---|---|
| 撮合引擎 | 不公平排序、抢跑 | **很难** |
| 报价分发 | 给不同用户不同数据 | 很难 |
| 风控执行 | 选择性执行规则 | 很难 |

**这就是 hybrid 架构诚实的说法**：它把"平台会不会卷款"这个**容易验证**的问题解决了，把"撮合公不公平"这个**难以验证**的问题留下了。

**一个平台如果只强调"资金在链上"而回避撮合公平性，它回答的是较容易的那一半。**

## Concrete Example | 具体例子

判断一个平台的链下部分值不值得信，看它愿不愿意做这三件事：

1. **公布订单承诺（order commitment）** —— 撮合前先把订单哈希上链，事后可验证排序未被篡改。
2. **接受第三方审计** —— 撮合日志由独立方定期抽查。
3. **公开延迟与拒单统计** —— 谁的单被拒了、延迟分布如何。

**目前这三件事在整个行业都很少见。** 这不是指责，是现状描述 —— **撮合公平性是这个赛道尚未被解决的问题之一。**

对比：资金托管的可验证性已经解决了（区块浏览器一查便知）。**两个问题的成熟度差得很远。**

## Common Misconceptions | 常见误解

- **误解一："链下 = 中心化 = 不安全。"** 安全的关键问题是**钱在哪**。链下撮合 + 链上托管，平台无法挪用资金。
- **误解二："全部上链最安全。"** 全上链的系统在延迟和成本上通常不可用，**而不可用的系统也是一种风险。**
- **误解三："链下部分不重要。"** 撮合公平性直接影响你的成交价格。**它只是更难验证，不是更不重要。**

## In Practice | 实战里怎么用

对任何 hybrid 平台，把两个问题分开问 —— 很多人把它们混为一谈：

| 问题 | 决定什么 | 怎么验证 |
|---|---|---|
| **钱在哪？** | 平台能否卷款跑路 | 区块浏览器（**容易**） |
| **撮合在哪、公不公平？** | 你的成交价格 | 几乎无法（**难**） |

**第一个问题有明确答案的平台已经比多数强。**
**第二个问题愿意主动提供证据的平台，目前极少 —— 遇到了值得记下来。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 判断链下组件是否可接受的关键问题是什么？
  A: 不是'在哪里算'，而是'谁能作恶、作恶了能不能被发现'。
- Q: hybrid 架构解决了哪个问题、留下了哪个问题？
  A: 解决了'平台会不会卷款'（容易验证），留下了'撮合公不公平'（难以验证）。
- Q: 能提升链下撮合可信度的三件事是什么？
  A: 订单承诺上链（事后可验证排序）、接受第三方审计、公开延迟与拒单统计。目前行业内都很少见。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
