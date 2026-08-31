---
id: "concept:erc-20"
type: concept
title: ERC-20
title_zh: 同质化代币标准
title_en: ERC-20
aliases:
  - ERC-20
  - 同质化代币标准
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
  - id: "concept:erc-standards"
    rel: special-case-of
    note: 同质化 token 接口
prerequisites:
  - "concept:token"
  - "concept:erc-standards"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# ERC-20 | 同质化代币标准

## Executive Definition / Chinese Explanation | 定义与解释

**ERC-20 | 同质化代币标准** = 一个合约代表一种完全同质的代币：每一份和另一份毫无区别，可任意分割和互换。

它是链上金融的基础货币形态 —— **稳定币、治理代币、大部分交易对的两端都是 ERC-20。**

## Why This Matters | 为什么重要

对事件市场，ERC-20 的角色不是结果代币，而是**抵押品**：

- 你的头寸是 [[erc-1155]] 的结果代币；
- **锁在合约里的抵押品是 ERC-20 的稳定币**（通常是 USDC）。

**这意味着 ERC-20 那一层的风险直接传导到你的头寸**：稳定币脱锚、发行方冻结地址、储备质量问题 —— 这些都不是"事件风险"，但它们会让你的赢利变成打折的钱（见 [[stablecoin]]）。

## How It Works | 机制怎么运转

ERC-20 的接口只有几个核心函数，简单是它成功的原因：

```
balanceOf(address)        余额查询
transfer(to, amount)      转账
approve(spender, amount)  授权额度
transferFrom(...)         代扣转账
```

**`approve` 是事件市场用户最该理解的一个**：你要把 USDC 存进事件市场合约，必须先 `approve` 授权它动用你的余额。

**风险点**：很多前端默认申请**无限额度授权**。这意味着那个合约在你撤销之前，可以随时动用你钱包里的全部该代币。**合约若被攻破或有后门，损失不限于你存进去的那部分。**

## Concrete Example | 具体例子

一次事件市场存款的完整链上动作：

```
1. approve(市场合约, 无限额度)   ← 危险的默认值
2. deposit(1000 USDC)            ← 实际只存了 1000
```

**第 1 步之后，那个合约理论上可以动用你钱包里的全部 USDC**，而不只是 1000。

**更好的做法**：
- 授权额度设为**实际需要的数额**，而不是无限；
- 定期检查并撤销不再使用的授权（区块浏览器和多数钱包都提供这个功能）；
- **大额资金用独立地址** —— 交互地址和存储地址分开。

**这三条是链上事件市场用户最实用的安全习惯，而且大多数人从没做过。**

## Common Misconceptions | 常见误解

- **误解一："ERC-20 稳定币就是美元。"** 它是**对发行方的索赔权**（见 [[stablecoin]]），不是美元本身。
- **误解二："授权只是一个技术步骤。"** 无限授权是链上最常见的资金损失路径之一。
- **误解三："我没在用的协议不用管。"** 旧授权一直有效。**协议后来被攻破，你的授权依然可以被利用。**

## In Practice | 实战里怎么用

链上事件市场的三条基本安全纪律：

1. **授权额度按需给，不给无限。** 多数钱包支持自定义额度。
2. **定期清理授权。** 用区块浏览器的 token approval 工具，撤销不再使用的。
3. **地址分层。** 交互地址只放要用的钱，主仓位放在从不签任何授权的地址。

**第 3 条最有效也最少人做。** 它把"某个协议被攻破"的损失上限，从"你的全部资产"降到"交互地址里的余额"。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: ERC-20 在事件市场里扮演什么角色？
  A: 抵押品（通常是 USDC 稳定币）。结果代币是 ERC-1155，抵押品那一层的风险会直接传导到头寸。
- Q: 为什么 approve 无限额度是危险的？
  A: 被授权的合约在撤销前可随时动用你钱包里该代币的全部余额，损失不限于存入的那部分。
- Q: 链上事件市场最有效但最少人做的安全习惯是什么？
  A: 地址分层 —— 交互地址只放要用的钱，主仓位放在从不签任何授权的地址，把被攻破的损失上限压到交互地址余额。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = token, erc-standards; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
