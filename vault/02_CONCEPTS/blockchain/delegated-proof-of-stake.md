---
id: "concept:delegated-proof-of-stake"
type: concept
title: DPoS
title_zh: 委托权益证明
title_en: DPoS
aliases:
  - DPoS
  - Delegated Proof of Stake
  - 委托权益证明
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
  - "source:2026-08-26-tron-dao-how-tron-works"
related:
  - id: "concept:proof-of-stake"
    rel: special-case-of
    note: 持币者投票选出有限验证节点集合
  - id: "protocol:tron"
    rel: instantiated-by
    note: 27 个 Super Representatives 由 TRX 质押投票选出
prerequisites:
  - "concept:proof-of-stake"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# DPoS | 委托权益证明

## Executive Definition / Chinese Explanation | 定义与解释

**DPoS (Delegated Proof of Stake) | 委托权益证明** = 代币持有人投票选出**固定数量**的验证者（超级代表）来出块，而不是所有质押者都参与。

它用**更少的验证者**换取更高的吞吐和更快的最终性。

## Why This Matters | 为什么重要

DPoS 的取舍在事件市场语境下很具体：

**好处** —— 出块快、费用极低，让小额事件头寸在经济上成立（见 [[gas]]）。
**代价** —— 验证者数量少（通常几十个），**去中心化程度明显低于开放式 PoS**。

**TRON 是 DPoS 的代表**，也是全球 USDT 的主要结算轨道之一 —— **这意味着大量稳定币的安全性，实际上依赖于几十个超级代表的诚实与可用性。**

**这不是一个可以忽略的假设，而是一个应该被明确写进风险清单的事实。**

## How It Works | 机制怎么运转

```
代币持有人投票 → 选出 N 个超级代表 → 轮流出块 → 定期重新选举
```

**关键参数**：
- **N 的大小** —— 越小越快，越集中。
- **投票权分布** —— 大户能否决定选举结果？
- **轮换频率** —— 多久重选一次？

**DPoS 的中心化风险有一个具体形态**：**投票权与交易所质押高度重合**。交易所代持大量用户代币，因此在选举中拥有巨大话语权 —— 而用户通常不知道自己的币被用来投了谁。

## Concrete Example | 具体例子

评估一条 DPoS 链承载事件市场结算的三个数：

| 指标 | 为什么重要 | 危险信号 |
|---|---|---|
| 超级代表数量 | 抗审查与抗合谋 | **少于 30** |
| 前 1/3 代表的关联度 | 能否阻止最终性 | 由少数实体控制 |
| 交易所投票占比 | 隐性集中 | **过半** |

**第三行最少被查**：交易所用用户的币投票，形成了一层用户看不见的权力集中。

**对事件市场的直接含义**：如果你的抵押品结算在一条 DPoS 链上，**你的资金安全依赖于那几十个实体不合谋、不宕机** —— 这个假设应该被明确评估，而不是默认。

## Common Misconceptions | 常见误解

- **误解一："DPoS 就是中心化的 PoS。"** 它确实更集中，但有选举与轮换机制 —— 程度问题，不是二元。
- **误解二："验证者少所以不安全。"** 快速最终性也是安全属性。**要看具体威胁模型：防审查靠数量，防重组靠最终性。**
- **误解三："我不用那条链就与我无关。"** 若你的稳定币主要在那条链上流转，你已经暴露于它了。

## In Practice | 实战里怎么用

对结算在 DPoS 链上的事件市场，把这条写进风险清单：

> **我的抵押品安全依赖于 N 个超级代表不合谋且保持可用。**

然后查三件事：
1. **N 是多少？**
2. **前 1/3 由谁控制？**（1/3 阈值见 [[proof-of-stake]]）
3. **交易所投票占比多高？**

**这三个数查一次要不到十分钟，但它们决定了你"资金在链上"这句话到底值多少。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: DPoS 用什么换取什么？
  A: 用更少的验证者数量换取更高吞吐与更快最终性 —— 去中心化程度明显低于开放式 PoS。
- Q: DPoS 中心化风险最少被查的一个形态是什么？
  A: 交易所代持用户代币参与投票，形成用户看不见的权力集中，可能占据过半投票权。
- Q: 结算在 DPoS 链上的事件市场，该写进风险清单的一句话是什么？
  A: 我的抵押品安全依赖于 N 个超级代表不合谋且保持可用 —— 这个假设应被明确评估而非默认。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-tron-dao-how-tron-works]] — <https://developers.tron.network/docs/how-tron-works>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = proof-of-stake; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
