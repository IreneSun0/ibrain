---
id: "concept:erc-standards"
type: concept
title: ERC Standard
title_zh: 以太坊代币/接口标准
title_en: ERC Standard
aliases:
  - ERC Standard
  - 以太坊代币
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
# ERC Standard | 以太坊代币/接口标准

## Executive Definition / Chinese Explanation | 定义与解释

**ERC Standards | 以太坊代币标准** = 一组约定好的接口规范，规定"一个代币合约必须提供哪些函数"。

标准的价值不在技术，在**互操作**：只要你遵守 ERC-20 的接口，全世界的钱包、交易所、DeFi 协议就都能自动识别你的代币，**无需任何一方为你单独适配。**

## Why This Matters | 为什么重要

**标准是产品决策，不是实现细节。** 选哪个标准，直接决定了三件事：

1. **能不能被钱包显示** —— 用户看不看得见自己的持仓。
2. **能不能进 DeFi** —— 敞口能不能被当作抵押品使用。
3. **能不能被第三方审计** —— 外部工具能不能读懂你的持仓结构。

事件市场选择 [[erc-1155]] 而不是 [[erc-20]]，**一个选型就决定了整个市场的可组合性与可审计性**（见 [[outcome-token]]）。

## How It Works | 机制怎么运转

三个主要标准的结构差异：

| 标准 | 一个合约里 | 同质性 | 典型用途 |
|---|---|---|---|
| **ERC-20** | 一种代币 | 完全同质 | 货币、稳定币、治理代币 |
| **ERC-721** | 多个**唯一**代币 | 完全异质 | NFT、单件资产 |
| **ERC-1155** | 多个 id | **id 间异质、id 内同质** | **多结果事件合约** |

**ERC-1155 还支持批量转移**（一次交易转多个 id），这对需要同时操作多个结果的事件市场是实打实的成本节省。

**看懂这张表，就看懂了为什么条件代币框架必须用 1155。**

## Concrete Example | 具体例子

如果事件市场硬用 ERC-20 会怎样：

一个有 10,000 个市场、每个 2 个结果的平台：

| | ERC-20 方案 | ERC-1155 方案 |
|---|---|---|
| 需要部署的合约数 | **20,000 个** | **1 个** |
| 部署成本 | 极高 | 一次性 |
| 批量操作 | 每个合约单独调用 | **一次交易批量转移** |
| 钱包展示 | 20,000 个代币条目 | 按 id 组织 |

**这不只是成本问题，是可行性问题。** ERC-20 方案下，开一个新市场就要部署一个新合约，这让"一天上线几百个市场"在经济上不可能。

**标准选型直接决定了产品能做多大。**

## Common Misconceptions | 常见误解

- **误解一："标准是技术细节，产品经理不用管。"** 它决定了可组合性、可审计性、和开市场的边际成本。**这些全是产品问题。**
- **误解二："遵守标准就安全。"** 标准规定接口，不规定实现。**一个符合 ERC-20 接口的合约照样可以有后门。**
- **误解三："新标准总比旧标准好。"** 选型要看结构是否匹配。用 ERC-721 做可分割的份额就是结构不匹配，无关新旧。

## In Practice | 实战里怎么用

看到一个链上资产，先确认它的标准，再问三件事：

1. **标准和用途匹配吗？** 可互换的份额用 1155/20；唯一资产用 721。
2. **钱包和工具支持吗？** 不被支持的标准 = 用户看不见自己的资产。
3. **合约实现有没有偏离标准？** 有些合约"基本兼容"但在某些函数上有特殊行为 —— **这是集成时踩坑的常见来源。**

**对事件市场特别的一条**：结果代币用 ERC-1155 是行业事实标准。**看到用别的方案的，先问为什么。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: ERC 标准的价值主要在哪里？
  A: 互操作 —— 遵守接口就能被全世界的钱包、交易所、DeFi 协议自动识别，无需逐一适配。
- Q: 为什么事件市场不能用 ERC-20 实现结果代币？
  A: 每个结果都要部署一个独立合约，10,000 个二元市场就是 20,000 个合约，部署成本和批量操作成本让'一天上线数百个市场'在经济上不可行。
- Q: 为什么说标准选型是产品决策？
  A: 它决定了能否被钱包显示、能否进 DeFi 做抵押、能否被第三方审计，以及开新市场的边际成本。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = smart-contract; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
