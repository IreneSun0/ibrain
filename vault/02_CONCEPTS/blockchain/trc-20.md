---
id: "concept:trc-20"
type: concept
title: TRC-20
title_zh: TRON同质化代币标准
title_en: TRC-20
aliases:
  - TRC-20
  - TRON同质化代币标准
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
related:
  - id: "concept:stablecoin"
    rel: see-also
    note: TRON 上 USDT 的载体标准 — 最大稳定币结算流量的技术形态
prerequisites:
  - "concept:erc-20"
import_origin: xlsx-learning-map+manual
import_category: TRON
---
# TRC-20 | TRON同质化代币标准

## Executive Definition / Chinese Explanation | 定义与解释

**TRC-20** = TRON 链上的同质化代币标准，接口设计与 [[erc-20]] 基本一致 —— 名字、余额、转账、授权那一套。

**它值得单独一页，只因为一个事实**：全球流通 USDT 里有相当大比例是 TRC-20 形态，TRON 因此成为稳定币最主要的结算轨道之一。

## Why This Matters | 为什么重要

对事件市场，这件事的意义在于**结算轨道的选择**（见 [[settlement-rail]]）：

事件市场以稳定币计价、在稳定币轨道上流动。而稳定币在哪条链上流通量最大，就意味着：
- 出入金最方便的路径在哪；
- 跨平台转移资金的成本在哪；
- **哪条链的风险与你的资金实际相关。**

**如果你的抵押品要经过 TRON 轨道，那么 TRON 的共识安全（DPoS，见 [[delegated-proof-of-stake]]）就是你的风险清单上的一行** —— 不管你的事件合约本身在哪条链上结算。

## How It Works | 机制怎么运转

TRC-20 与 ERC-20 的实际差异：

| | ERC-20（以太坊） | TRC-20（TRON） |
|---|---|---|
| 接口 | 标准 | **基本一致** |
| 转账成本 | 中到高 | **极低** |
| 共识 | PoS | **DPoS（验证者少）** |
| 最终性 | 明确 | 快 |

**接口一致意味着工具可复用；共识不同意味着安全假设不同。**

**这是一个经典的"看起来一样、底下不一样"的例子**：同一个 USDT，在两条链上的安全性依赖于完全不同的验证者集合。

## Concrete Example | 具体例子

同样是持有 $100,000 USDT，两条轨道的风险构成：

| 风险 | ERC-20 (以太坊) | TRC-20 (TRON) |
|---|---|---|
| 发行方（Tether）风险 | **相同** | **相同** |
| 冻结风险 | **相同**（发行方可冻结地址） | **相同** |
| 链共识风险 | 以太坊 PoS | **TRON DPoS，验证者数十个** |
| 转账成本 | 高 | 极低 |

**前两行相同 —— 发行方风险与链无关。**
**第三行不同 —— 这是选择轨道时唯一实质变化的一项。**

**结论**：**跨链选择改变的是共识风险与成本，不改变发行方风险。** 很多人以为换链能分散稳定币风险，其实不能。

## Common Misconceptions | 常见误解

- **误解一："TRC-20 USDT 和 ERC-20 USDT 是两种币。"** 是同一个发行方的同一种负债，只是在不同链上的表示。
- **误解二："换条链就分散了稳定币风险。"** 发行方风险完全相同 —— 分散的只是链风险。
- **误解三："转账便宜所以更好。"** 便宜的代价是不同的共识安全假设，需要单独评估。

## In Practice | 实战里怎么用

管理你在事件市场的稳定币敞口，分两层看：

1. **发行方层** —— 你持有的稳定币来自几个发行方？全部同一个 = 100% 集中（见 [[concentration-risk]]）。
2. **链层** —— 资金在哪条链上？该链的共识安全如何？

**换链能分散第 2 层，不能分散第 1 层。**

**再查一条**：**你要用的事件市场平台支持哪条轨道出入金？** 如果只支持一条，你就没有选择余地 —— 那本身是一个应该被记下的约束。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: TRC-20 与 ERC-20 的接口和共识分别有什么关系？
  A: 接口基本一致（工具可复用），共识完全不同（TRON 是 DPoS 验证者数十个，以太坊是开放式 PoS）。
- Q: 跨链持有同一种稳定币，能分散哪层风险、不能分散哪层？
  A: 能分散链共识风险，不能分散发行方风险 —— 发行方风险与链无关。
- Q: 为什么 TRC-20 值得单独理解？
  A: 全球流通 USDT 中相当大比例是 TRC-20 形态，TRON 因此是稳定币的主要结算轨道之一，可能是你资金的实际路径。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
