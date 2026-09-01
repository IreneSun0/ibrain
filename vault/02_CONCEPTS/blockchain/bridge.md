---
id: "concept:bridge"
type: concept
title: Bridge
title_zh: 跨链桥
title_en: Bridge
aliases:
  - 跨链桥
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
# Bridge | 跨链桥

## Executive Definition / Chinese Explanation | 定义与解释

**Bridge | 跨链桥** = 让资产在两条互不相识的链之间移动的机制。

严格说资产并不"移动"：**原链锁定，目标链铸造一个凭证。** 你在目标链上拿到的不是原资产，是一张"原链上锁着等量资产"的欠条。

## Why This Matters | 为什么重要

桥是链上世界**历史上最集中的攻击面**。原因结构性：

- 它必须在两条链上都持有权限（锁定与铸造）。
- 它通常由一组验证者或多签控制，而**那组人的安全性往往远低于两条链本身**。
- 桥里锁着的资产是集中的、公开的、金额巨大的 —— 攻击性价比极高。

**对事件市场的直接含义**：你的抵押品要从 L1 桥到结算链，**那段路上的风险不属于任何一条链，属于桥**（见 [[layer-2]]）。

## How It Works | 机制怎么运转

桥的三种信任模型，安全性递增：

| 模型 | 谁保证 | 风险 |
|---|---|---|
| **托管式** | 一家公司 | 完全信任该公司 |
| **多签/验证者集** | N 选 M 的一组实体 | **阈值被攻破即全失** |
| **轻客户端 / ZK 证明** | 密码学 | 实现复杂，仍可能有 bug |

**绝大多数已发生的桥攻击属于第二类**：拿到足够的签名权限（通过私钥泄露、社工、或治理攻击），然后铸造凭空的资产。

**判断一座桥，核心问一句**：**"要偷走里面的钱，需要攻破什么？"** 答案是"几把私钥"就要非常谨慎。

## Concrete Example | 具体例子

一笔资金进入链上事件市场的完整风险路径：

```
法币 → 交易所 → L1 上的 USDC → 桥 → 结算链上的 USDC → 事件合约
                                 ↑
                          风险不属于任何一条链
```

**注意每一段的风险归属**：
- 交易所段 → 平台托管风险
- L1 段 → 稳定币发行方风险（见 [[stablecoin]]）
- **桥段 → 桥的验证者集/多签风险**
- 结算链段 → 该链的共识安全
- 合约段 → 智能合约风险

**"我的钱在链上很安全"这句话，掩盖了这条路径上至少五种不同的风险。**

## Common Misconceptions | 常见误解

- **误解一："跨链就是转账。"** 是锁定+铸造。你持有的是凭证，不是原资产。
- **误解二："大桥更安全。"** 锁的钱越多，攻击性价比越高。规模不等于安全。
- **误解三："桥出事了原资产还在。"** 原资产确实还锁着 —— **但可能已经被攻击者取走了**，你手里的凭证就此无锚。

## In Practice | 实战里怎么用

跨链把资金送进任何事件市场前，问三件事：

1. **这座桥的信任模型是什么？** 托管 / 多签 / 密码学？
2. **攻破需要什么？** 几把私钥？多签阈值多少？谁持有？
3. **有没有替代路径？** 有些结算链可以直接出入金，不必经过桥。

**第 3 问最实用**：**能不桥就不桥。** 少一段路径就少一类风险。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 跨链桥的本质机制是什么？
  A: 原链锁定、目标链铸造凭证。你持有的是'原链上锁着等量资产'的欠条，而非原资产本身。
- Q: 为什么桥是链上历史上最集中的攻击面？
  A: 它在两条链上都持有权限，通常由一组验证者或多签控制，其安全性远低于两条链本身，且锁着的资产集中巨大。
- Q: 判断一座桥安全性的核心问题是什么？
  A: 要偷走里面的钱需要攻破什么 —— 如果答案是'几把私钥'，就要非常谨慎。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = blockchain; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
