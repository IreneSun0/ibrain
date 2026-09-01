---
id: "concept:tron-power"
type: concept
title: TRON Power
title_zh: TRON投票权资源
title_en: TRON Power
aliases:
  - TRON投票权资源
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
  - "source:2026-08-26-tron-dao-resource-model"
related:
  - id: "concept:delegated-proof-of-stake"
    rel: mechanism-of
    note: "TRON DPoS 的投票权载体, 用于选 SR"
prerequisites:
  - "concept:delegated-proof-of-stake"
import_origin: xlsx-learning-map+manual
import_category: TRON
---
# TRON Power | TRON投票权资源

## Executive Definition / Chinese Explanation | 定义与解释

**TRON Power (TP) | 投票权** = 质押 TRX 后获得的治理投票权，用来在 [[delegated-proof-of-stake|DPoS]] 中选举超级代表。

**质押一次，得到两样东西**：[[tron-energy|Energy]]/[[tron-bandwidth|Bandwidth]] 的资源额度，以及 TRON Power 的投票权。

## Why This Matters | 为什么重要

这个"一次质押、两种用途"的设计，把**资源需求**和**治理权力**捆在了一起 —— 而这带来一个值得注意的后果：

**大量质押 TRX 的实体，是为了获得 Energy（做业务），却顺带获得了治理权。**

典型的例子是交易所：它们为用户代持大量 TRX，因此在超级代表选举中拥有巨大话语权 —— **而它们的初衷通常只是运营需求，不是治理意图。**

**结果是治理权力集中在一批"并不特别想要它"的实体手里** —— 这是 DPoS 集中度问题的一个具体机制（见 [[delegated-proof-of-stake]]）。

## How It Works | 机制怎么运转

```
质押 TRX → 同时获得: 资源额度 + TRON Power
TRON Power → 投票给超级代表 → 可获投票奖励
```

**投票权的两个性质**：
1. **与质押量成正比** —— 钱多话语权大。
2. **可以委托** —— 但委托的是投票，不是资源。

**关键的集中度问题**：**用户把币存在交易所时，投票权实际由交易所行使，而用户通常不知情。** 这形成了一层看不见的权力集中。

## Concrete Example | 具体例子

为什么这对事件市场用户不是无关的技术细节：

```
你的抵押品是 TRC-20 USDT
   ↓ 依赖
TRON 链的共识安全
   ↓ 依赖
几十个超级代表不合谋
   ↓ 由谁选出
TRON Power 持有者, 其中很大比例是交易所代持
```

**所以你的资金安全，最终链接到"交易所用用户的币投了谁"这件事上** —— 而这条链路上没有任何一环是你能控制或通常会去查的。

**这不是危言耸听，是一条应该被明确写进风险清单的依赖链。**

## Common Misconceptions | 常见误解

- **误解一："投票权与我无关。"** 它决定谁验证你的交易、你的抵押品有多安全。
- **误解二："质押就是理财。"** 你同时获得了治理权并承担了锁定期风险。
- **误解三："交易所代持不影响去中心化。"** 恰恰是它造成了最主要的隐性集中。

## In Practice | 实战里怎么用

如果你的事件市场资金经过 TRON 轨道，把这条依赖链写下来：

```
我的抵押品 → TRC-20 USDT → TRON 共识 → N 个超级代表 → TP 持有者分布
```

然后查两个数（见 [[delegated-proof-of-stake]]）：
1. **超级代表数量**。
2. **前 1/3 由谁控制，其中交易所占多少。**

**查完你会对"我的钱在链上很安全"这句话有一个更准确的估计** —— 它安全到什么程度，取决于这条链路上最弱的一环。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 质押 TRX 同时获得哪两样东西？这个捆绑带来什么后果？
  A: 资源额度（Energy/Bandwidth）与治理投票权 TRON Power。后果是为业务需求质押的实体顺带获得治理权，造成权力集中。
- Q: 交易所代持如何造成隐性权力集中？
  A: 用户把币存在交易所后，投票权实际由交易所行使，而用户通常不知情，形成看不见的集中。
- Q: 事件市场用户为什么该关心 TRON Power 的分布？
  A: 抵押品安全依赖 TRON 共识，共识依赖超级代表不合谋，而超级代表由 TRON Power 持有者选出 —— 这是一条完整的依赖链。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-tron-dao-resource-model]] — <https://developers.tron.network/docs/resource-model>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: TRON)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = delegated-proof-of-stake; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
