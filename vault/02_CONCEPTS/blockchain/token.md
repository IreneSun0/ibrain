---
id: "concept:token"
type: concept
title: Token
title_zh: 代币/链上资产单位
title_en: Token
aliases:
  - 代币
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
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Token | 代币/链上资产单位

## Executive Definition / Chinese Explanation | 定义与解释

**Token | 代币 / 链上资产单位** = 记录在链上的一份**可编程的权利**。

关键词是**权利**：token 本身没有内在价值，它的价值完全来自它代表的那份权利 —— 一份索赔权、一份投票权、一份使用权，或者（在事件市场里）**一份对某个结果的赔付索赔权**。

## Why This Matters | 为什么重要

把"头寸"变成"token"，改变的不是记账方式，是**资产的性质**（见 [[outcome-token]]）：

- **可转移** —— 不必等结果揭晓就能退出。
- **可组合** —— 能进钱包、进 DeFi、做抵押品。
- **可审计** —— 谁持有多少，链上全透明。

**这三条合起来，让事件敞口第一次接入了更大的金融体系。** 在此之前，一个"我押注 X 会发生"的头寸只能待在开仓的那个平台里。

## How It Works | 机制怎么运转

token 标准决定了它能做什么。事件市场用的是 **ERC-1155**，原因很具体：

| 标准 | 结构 | 用在事件市场 |
|---|---|---|
| [[erc-20]] | 一个合约一种同质代币 | 每个结果部署一个合约 —— 太贵 |
| [[erc-721]] | 一个合约多个**唯一**代币 | 结果份额需要可分割互换 —— 不匹配 |
| **[[erc-1155]]** | 一个合约多个 id；**id 间异质、id 内同质**，支持批量转移 | **正好** |

**"id 间异质、id 内同质"** 翻译过来就是：不同事件不同结果互不相同，但同一结果的每一份完全等价可互换。**一个标准选型，决定了整个市场的可组合性与可审计性。**

## Concrete Example | 具体例子

一份事件合约在链上的实际形态：

```
合约地址 0xABC…（条件代币框架）
 ├─ token id 0x1f3a…  = "候选人 A 当选 → YES"
 └─ token id 0x9c72…  = "候选人 A 当选 → NO"
```

- 存 $1 → 各得 1 份 YES 和 1 份 NO（铸造）。
- 卖掉 NO 得 $0.37 → 净成本 $0.63，持有 1 份 YES。
- **想提前退出 → 直接把 YES 转给别人，不必等选举结束。**
- 集齐一份 YES + 一份 NO → 可换回 $1（合并）。

**铸造与合并这一对操作，就是"YES 价格 + NO 价格 ≈ $1"这个恒等式的执行机制**（见 [[fully-collateralized-market]]）。

## Common Misconceptions | 常见误解

- **误解一："token 有内在价值。"** 它的价值完全来自它代表的权利。**合约裁决出错，token 一文不值** —— 它是索赔权，不是资产。
- **误解二："token 化只是技术选型。"** 它决定了敞口能不能提前转让、能不能进 DeFi、能不能被第三方审计。**这些是产品能力。**
- **误解三："所有 token 都一样。"** 标准不同能力完全不同；同一标准下，发行合约的权限设计也决定了它有多可信。

## In Practice | 实战里怎么用

拿到任何一个 token，问三件事：

1. **它代表什么权利？** 对谁的索赔？在什么条件下兑现？
2. **谁能改变这份权利？** 合约有升级权限吗？（见 [[smart-contract]]）
3. **它依赖什么？** 结果代币依赖预言机；稳定币依赖发行方储备。

**第 3 问是最容易被跳过的**：你持有的 outcome token，其价值链条是
`token → 合约 → 预言机 → 现实`。**链条上任何一环断了，token 就归零** —— 而多数人只检查了第一环。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: token 的价值来自哪里？
  A: 它所代表的那份权利，而非 token 本身。事件市场里它是一份对某个结果的赔付索赔权。
- Q: 为什么 ERC-1155 适合结果代币？
  A: 一个合约容纳多个 id，id 间异质（不同结果）、id 内同质（份额可互换），并支持批量转移。
- Q: 持有 outcome token 的价值链条是什么？
  A: token → 合约 → 预言机 → 现实。任何一环断了 token 就归零，而多数人只检查第一环。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
