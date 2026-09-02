---
id: "concept:public-key"
type: concept
title: Public Key
title_zh: 公钥
title_en: Public Key
aliases:
  - 公钥
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
  - id: "concept:wallet"
    rel: component-of
prerequisites:
  - "concept:private-key"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Public Key | 公钥

## Executive Definition / Chinese Explanation | 定义与解释

**Public Key | 公钥** = 从[[private-key|私钥]]单向推导出来、可以公开的那一半。别人用它验证你的签名，但推不回你的私钥。

**地址通常是公钥的哈希** —— 所以"公开地址"不等于"公开公钥"，也不等于泄露任何秘密。

## Why This Matters | 为什么重要

公钥密码学解决了一个看似不可能的问题：**如何在不共享秘密的前提下证明身份。**

传统金融靠"共享秘密"（密码、印鉴、证件号）—— 这意味着验证方也知道你的秘密，因此验证方本身成为攻击面。

**公钥体系里，验证方永远不需要知道你的私钥。** 这是链上"无需信任"的密码学地基：任何人都能独立验证一笔交易确实由某地址的主人发出，而不需要向任何机构查询。

## How It Works | 机制怎么运转

签名与验证的流程：

```
签名:  消息 + 私钥  →  签名
验证:  消息 + 签名 + 公钥  →  真/假
```

**验证者不需要私钥，也无法从签名反推私钥。**

对事件市场的直接含义：
- **你对合约的每一次操作都是一次签名** —— 授权、存入、领取。
- **链上的每一笔头寸变化都可被任何人验证为真** —— 这是[[on-chain|链上可审计性]]的技术来源。
- **这也意味着持仓分析对所有人开放**（见 [[order-flow]]）：既是透明度，也是隐私代价。

## Concrete Example | 具体例子

为什么链上是"假名"而不是"匿名"：

```
地址 0x7a3f… 的所有行为都被永久记录:
  何时开仓、多大规模、在什么消息之前
  资金从哪来、到哪去
```

**地址本身不含身份信息，但行为模式会泄露身份。**

- 出入金环节撞上 [[know-your-customer|KYC]] → 地址与身份绑定。
- 地址之间的资金流动可被聚类 → 一个人的多个地址可能被关联。

**这就是为什么"链上匿名"是个常见误解**：它是**假名 + 完整公开的行为史**，从长期看比传统账户更容易被画像。

## Common Misconceptions | 常见误解

- **误解一："公开地址会泄露私钥。"** 不会 —— 推导是单向的。
- **误解二："链上是匿名的。"** 是**假名**：身份不直接可见，但行为完全公开且永久，可被分析与关联。
- **误解三："公钥就是地址。"** 多数链上地址是公钥的哈希，两者不是一回事。

## In Practice | 实战里怎么用

理解公钥体系对你在事件市场的两个实际影响：

**一是安全** —— 你的每次签名都是不可撤销的授权。签之前看清楚签的是什么（见 [[erc-20]] 的授权风险）。

**二是隐私** —— 你的所有事件敞口都是公开的。如果你不希望自己的持仓被跟单或被分析：
- 用多个地址分散头寸；
- 避免在出入金环节把主仓位地址与身份绑定；
- 明白**这只是提高分析成本，不是消除可分析性。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 公钥密码学解决了什么看似不可能的问题？
  A: 在不共享秘密的前提下证明身份 —— 验证方永远不需要知道你的私钥。
- Q: 为什么说链上是假名而不是匿名？
  A: 地址不含身份信息，但行为史完整公开且永久；出入金的 KYC 与地址聚类都可能把地址与身份关联。
- Q: 公钥与地址是一回事吗？
  A: 不是。多数链上地址是公钥的哈希，公开地址既不泄露公钥也不泄露私钥。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
