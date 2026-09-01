---
id: "concept:blockchain"
type: concept
title: Blockchain
title_zh: 区块链
title_en: Blockchain
aliases:
  - 区块链
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
related: []
prerequisites:
  - "concept:ledger"
  - "concept:consensus"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Blockchain | 区块链

## Executive Definition / Chinese Explanation | 定义与解释

**Blockchain | 区块链** = 一份由共识机制维护的、不可篡改的共享历史账本。

它把三样东西绑在一起：[[ledger|账本]]（记录谁拥有什么）、[[consensus|共识]]（谁说了算）、以及密码学链接（改历史要重做之后的所有工作）。

## Why This Matters | 为什么重要

对事件市场，区块链提供的不是"去中心化"这个抽象好处，而是**三个具体能力**：

1. **不可挪用的托管** —— 钱锁在合约里，平台没有私钥。
2. **可独立验证的历史** —— 第三方无需授权就能核验结算行为（见 [[auditability]]）。
3. **7×24 的结算轨道** —— 事件不在银行营业时间发生（见 [[settlement-rail]]）。

**这三条都是可验证的属性，不是意识形态。** 它们也正好对应事件市场最需要的三件事。

## How It Works | 机制怎么运转

判断"该不该上链"，一句口诀：

> **多方互不信任 + 需要共享状态 → 上链；否则数据库更快更便宜。**

代入事件市场，答案是分层的：

| 组件 | 上链？ | 为什么 |
|---|---|---|
| 资金托管 | **是** | 多方互不信任，需要不可挪用 |
| 结算执行 | **是** | 需要可验证、可自动执行 |
| 订单簿撮合 | **通常否** | 需要低延迟，参与者可接受平台撮合 |
| 用户身份 KYC | **否** | 隐私 + 无需共享 |

**这就是 hybrid 架构的推导过程**（见 [[hybrid-exchange-architecture]]）—— 它不是妥协，是对每个组件分别回答这个问题的结果。

## Concrete Example | 具体例子

[[polymarket]] 是这套推导的完整实例：

- **链上**：Polygon 上的 USDC 全额抵押、条件代币（ERC-1155）、结算执行。
- **链下**：CLOB 撮合引擎。
- **混合**：裁决 —— 提议与投票在链上可读，但判断由人做出。

**实际效果**：持仓与结算全部链上可查。任何人可以独立核验"这个合约什么时候判成了什么、钱付给了谁"，**无需平台配合**。

**这重新定义了第三方评价的可能性**：在传统市场里，评价一家交易所的结算质量需要它配合；在链上，不需要。

## Common Misconceptions | 常见误解

- **误解一："区块链让一切更快更便宜。"** 相反 —— 它慢得多、贵得多。**买的是不需要信任单一方。**
- **误解二："上链的数据是真的。"** 链保证记录不可篡改，不保证内容正确。**输入靠 [[oracle|预言机]]，而那才是最脆弱的一环。**
- **误解三："全部上链最好。"** 每个组件要单独回答"该不该上链"。**全上链的系统通常在延迟和成本上不可用。**

## In Practice | 实战里怎么用

看到任何"基于区块链的"产品，逐组件拆：

```
组件           上链?    为什么/为什么不
托管           ____     ____________
结算           ____     ____________
撮合           ____     ____________
身份           ____     ____________
裁决           ____     ____________
```

**拆完再问一次那个判据**：如果这个平台明天消失，链上还剩下什么？

**剩下托管和结算 → 上链上得实。**
**只剩一个存证哈希 → 那是营销。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 区块链为事件市场提供的三个具体能力是什么？
  A: 不可挪用的托管、可独立验证的历史、7×24 的结算轨道。
- Q: 判断'该不该上链'的口诀是什么？
  A: 多方互不信任且需要共享状态就上链；否则中心化数据库更快更便宜。要逐组件分别回答。
- Q: 链上可验证的历史重新定义了什么？
  A: 第三方评价的可能性 —— 传统市场里评价交易所结算质量需要它配合，链上不需要。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = ledger, consensus; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
