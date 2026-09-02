---
id: "concept:on-chain"
type: concept
title: On-chain
title_zh: 链上
title_en: On-chain
aliases:
  - On-chain
  - 链上
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
  - "concept:blockchain"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# On-chain | 链上

## Executive Definition / Chinese Explanation | 定义与解释

**On-chain | 链上** = 状态被写进区块链的共识状态，因此不可篡改、任何人可验证、任何合约可组合调用。

"上链"不是一个技术标签，是一种**公开承诺的强度**：写进共识状态 = 向全世界开放审计权。

## Why This Matters | 为什么重要

对机构，这件事的意义远超技术：

- **传统场馆说**："相信我们的账。"
- **链上场馆说**："**自己去查。**"

**审计从特权变成了公共品。** 这是事件市场少数几个结构性优于传统市场的地方 —— 在传统市场里，核验一家交易所的结算历史需要它配合、需要监管权限；在链上，一个区块浏览器就够了。

**代价是隐私**：可审计与可监视是同一件事的两面。大户持仓无法隐藏，这会反过来改变他们的下单行为。

## How It Works | 机制怎么运转

链上能带来三重承诺，缺一不可：

1. **任何人可验证** —— 无需许可即可核对。
2. **任何合约可组合调用** —— 资产能被其他协议使用（DeFi 抵押、钱包展示）。
3. **没有单点能删改** —— 历史不可被单方重写。

**第 2 条常被低估**：outcome token 上链意味着事件敞口**天生可组合**进 EVM 生态（见 [[outcome-token]]）。这是"资产"和"账户余额"的本质区别 —— 前者能进入更大的金融体系，后者只能待在一个平台里。

## Concrete Example | 具体例子

链上可读性带来的三种真实分析能力，传统市场都做不到：

| 分析 | 传统市场 | 链上事件市场 |
|---|---|---|
| **持仓集中度** | 需监管权限 | **任何人可查** |
| **大户建仓时序** | 不可见 | **精确到区块** |
| **平台历史结算行为** | 需平台配合 | **完全公开** |

**第二项特别有价值**：能看到一个大额头寸是在什么消息**之前**建立的 —— 这是识别可能的信息优势最直接的线索（见 [[inside-information]]）。

**在传统市场里，这类分析是监管机构的专属能力。**

## Common Misconceptions | 常见误解

- **误解一："上链 = 去中心化。"** 数据上链但控制权在一个多签手里，依然是中心化的。**看权限，不看数据位置。**
- **误解二："链上的都是真的。"** 不可篡改 ≠ 正确。错误的裁决结果上链后同样不可篡改，**而且更难纠正。**
- **误解三："链上没有隐私就是缺点。"** 对用户是代价，对市场诚信是能力。**这是一个取舍，不是纯粹的缺陷。**

## In Practice | 实战里怎么用

看到"链上"两个字，先分清是哪一种：

| 说法 | 实际含义 | 价值 |
|---|---|---|
| "资金链上托管" | 钱锁在合约，平台无私钥 | **高** |
| "结算链上执行" | 分配逻辑由合约执行 | **高** |
| "数据上链存证" | 存了个哈希 | **低**（只证明数据没被改，不证明数据对） |
| "订单簿链上" | 撮合在链上 | 中（可验证但慢） |

**只做第三行的项目，"上链"基本是营销词。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: '上链'对机构的真正意义是什么？
  A: 审计从特权变成公共品 —— 传统场馆说'相信我们的账'，链上场馆说'自己去查'，无需平台配合即可核验。
- Q: 链上的三重承诺是什么？哪一条最常被低估？
  A: 任何人可验证、任何合约可组合调用、没有单点能删改。可组合性最常被低估 —— 它让敞口成为能进入更大金融体系的资产。
- Q: '数据上链存证'和'资金链上托管'的价值差别是什么？
  A: 存证只证明数据未被修改，不证明数据正确，价值低；链上托管意味着平台无私钥无法挪用，价值高。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
