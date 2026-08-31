---
id: "concept:consensus"
type: concept
title: Consensus
title_zh: 共识机制
title_en: Consensus
aliases:
  - 共识机制
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
    note: 让互不信任的节点就同一账本历史达成一致
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Consensus | 共识机制

## Executive Definition / Chinese Explanation | 定义与解释

**Consensus | 共识机制** = 一群互不信任的节点，就"账本现在长什么样"达成一致的规则。

它要解决的核心问题只有一个：**谁说了算。** 而它给出的答案是：**让说谎变得昂贵。**

## Why This Matters | 为什么重要

共识决定了链的三个属性，而这三个属性直接决定事件市场能不能用它：

1. **最终性（finality）** —— 一笔交易多久之后不可能被回滚？**结算需要确定性。**
2. **吞吐与延迟** —— 能承载多少交易？**撮合上链需要高吞吐。**
3. **抗审查性** —— 能不能有人阻止你的交易上链？

**事件市场对第 1 条最敏感**：如果结算交易可能被回滚，那"链上结算"的确定性承诺就打了折。这也是为什么大多数事件市场选择在成熟公链上结算，而不是自建链。

## How It Works | 机制怎么运转

两大类共识，成本结构完全不同：

| | PoW（工作量证明） | PoS（权益证明） |
|---|---|---|
| 说谎成本 | 烧电算力 | 质押的代币被罚没 |
| 最终性 | 概率性（等更多确认） | 多数有明确最终性 |
| 能耗 | 高 | 低 |
| 攻击成本 | 获得多数算力 | 获得多数质押 |

**共同点是关键**：两者都不是"技术上不可能作恶"，而是**"作恶的成本大于收益"**。

**这个思路和预言机是同一个** —— [[oracle-risk]] 里的攻击成本计算，本质上是把共识安全性的逻辑搬到了裁决层。**理解了共识，就理解了为什么"投票权可购买"是致命缺陷。**

## Concrete Example | 具体例子

为什么最终性对事件市场是硬要求：

假设一个事件在链上结算，赢家收到 $1M。若该链的最终性是概率性的：

- 6 个确认后：回滚概率极低但非零。
- 赢家提走资金，转到交易所卖掉。
- **若发生深度重组，链上记录改变，但钱已经离开。**

**结算的确定性必须早于资金的可提取性** —— 这就是为什么平台会设提现等待期，也是为什么"确认数"不是技术细节而是风险参数。

在实践中，事件市场倾向使用有明确最终性的链或成熟的 L2，正是为了让这个窗口尽可能短且可预测。

## Common Misconceptions | 常见误解

- **误解一："共识保证数据正确。"** 它保证**大家看到同一份数据**，不保证那份数据反映现实。现实的输入靠 [[oracle|预言机]]。
- **误解二："去中心化程度越高越好。"** 去中心化是成本，买的是抗审查与抗操纵。**买多少取决于你在防谁。**
- **误解三："PoS 比 PoW 更中心化/更不安全。"** 两者的攻击成本模型不同，各有权衡，不存在简单的优劣排序。

## In Practice | 实战里怎么用

评估一条链能不能承载你的结算，三问：

1. **最终性多久？** 多少个区块/多长时间后不可回滚？
2. **拥堵时会怎样？** 高峰期费用和延迟到什么水平？**事件揭晓时刻恰恰是全网最拥堵的时刻之一。**
3. **验证者集中度？** 前几个实体控制多少质押/算力？

**第 2 问最容易被忽略但最实际**：一个平时够快的链，在大选夜可能拥堵到无法及时结算 —— **而那正是所有人同时想动的时候。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 共识机制解决的核心问题和采用的手段是什么？
  A: 解决'谁说了算'，手段是让说谎变得昂贵 —— 作恶成本大于收益，而非技术上不可能作恶。
- Q: 为什么最终性对事件市场是硬要求？
  A: 若结算交易可能被回滚而资金已被提走，链上结算的确定性承诺就打了折。结算确定性必须早于资金可提取性。
- Q: 评估链能否承载结算时最容易被忽略的一问是什么？
  A: 拥堵时的费用与延迟 —— 事件揭晓时刻恰恰是全网最拥堵、所有人同时想动的时候。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
