---
id: "concept:centralized-exchange"
type: concept
title: CEX
title_zh: 中心化加密交易所
title_en: CEX
aliases:
  - CEX
  - Centralized Exchange
  - 中心化加密交易所
status: reviewed
importance: tier-2
domains:
  - crypto-market-structure
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
  - id: "concept:exchange"
    rel: special-case-of
  - id: "concept:decentralized-exchange"
    rel: contrasts-with
    note: 内部账本+托管撮合 vs 链上合约+自托管结算 — 谁托管、谁能冻结完全不同
  - id: "venue:binance"
    rel: instantiated-by
  - id: "venue:okx"
    rel: instantiated-by
prerequisites:
  - "concept:exchange"
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# CEX | 中心化加密交易所

## Executive Definition / Chinese Explanation | 定义与解释

**CEX (Centralized Exchange) | 中心化交易所** = 由一家公司运营撮合、托管和结算的交易平台。用户把资产存进去，在平台的账本上交易。

它的效率来自集中：撮合快、体验好、无需理解链上机制。**代价是你的资产在别人手里。**

## Why This Matters | 为什么重要

CEX 与 DEX 的对比，是理解事件市场架构选择的基础。

**核心问题从来不是"中心化好还是去中心化好"，而是"哪些环节需要信任，那份信任由什么保证"。**

- CEX：撮合、托管、结算全在一家公司 → 信任由**声誉与监管**保证。
- DEX：托管与结算在合约 → 信任由**代码与经济激励**保证。
- **hybrid（事件市场主流）**：撮合在链下，托管结算在链上 → 各取所长（见 [[hybrid-exchange-architecture]]）。

## How It Works | 机制怎么运转

CEX 承担的四项功能，每一项都是一个信任点：

| 功能 | 风险 |
|---|---|
| **撮合** | 不公平排序、抢跑（难以外部验证） |
| **托管** | 挪用、被盗、破产时资产归属不明 |
| **结算** | 内部记账，外部无法核验 |
| **上市** | 决定挂什么、什么时候下架 |

**托管是唯一一个已经有成熟解法的**：链上全额抵押让平台无法挪用（见 [[custody]]）。

**撮合公平性至今没有好答案** —— 这也是 hybrid 架构诚实的边界：它解决了容易验证的一半（钱），留下了难验证的一半（撮合）。

## Concrete Example | 具体例子

三种事件市场架构下"平台倒闭"的后果：

| 架构 | 平台倒闭时 | 你的钱 |
|---|---|---|
| 纯 CEX（离岸） | 资产在平台钱包 | **进破产财产** |
| 持牌 CEX | 法定隔离账户 | **可取回** |
| hybrid（链上托管） | 合约与平台存续无关 | **合约照常结算** |

**第三行的特殊之处**：即使团队全部消失，链上合约仍会按预言机结果执行 —— **不需要任何机构继续存在。**

代价是：如果预言机也停摆，资金可能永久锁死。**自治性与救济渠道是一对取舍。**

## Common Misconceptions | 常见误解

- **误解一："CEX 一定不安全。"** 持牌 CEX 有法定隔离与监管救济，安全性可能高于一个有升级权限的"去中心化"合约。
- **误解二："CEX 就是中心化的全部。"** 关键要拆开看四项功能各在哪里 —— hybrid 就是把它们拆开的结果。
- **误解三："用户体验只有 CEX 能做好。"** 体验取决于产品设计，不取决于托管模式。hybrid 可以同时有好体验和链上托管。

## In Practice | 实战里怎么用

看任何交易平台，把四项功能逐个定位：

```
撮合  在哪? ______   能否验证? ______
托管  在哪? ______   平台能单方转出吗? ______
结算  在哪? ______   外部可核验吗? ______
上市  谁决定? ______  有规则手册吗? ______
```

**填完这张表，"中心化还是去中心化"这个问题就不需要问了** —— 你已经知道每一项的信任来自哪里。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: CEX 承担的四项功能是什么？哪一项已有成熟解法？
  A: 撮合、托管、结算、上市。托管已有成熟解法：链上全额抵押让平台无法挪用。
- Q: hybrid 架构诚实的边界在哪里？
  A: 它解决了容易验证的一半（资金托管），留下了难以外部验证的一半（撮合公平性）。
- Q: 链上托管在平台倒闭时的特殊之处是什么？代价是什么？
  A: 即使团队消失合约仍按预言机结果结算，不需任何机构存续；代价是预言机停摆时资金可能永久锁死。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: Crypto市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = exchange; typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
