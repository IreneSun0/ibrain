---
id: "protocol:justlend"
type: protocol-network
title: JUST / JustLend DAO
title_zh: TRON借贷与DeFi体系
title_en: JUST / JustLend DAO
aliases:
  - JUST / JustLend DAO
  - TRON借贷与DeFi体系
status: reviewed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
tags:
  - protocol-network
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
  - "source:2026-08-26-justlend-dao-justlend-whitepaper-en-pdf"
related:
  - id: "protocol:tron"
    rel: built-on
    note: TRON 上的去中心化 money market, 含 Energy 租赁
prerequisites: []
import_origin: xlsx-learning-map
import_category: TRON生态
---
# JUST / JustLend DAO | TRON借贷与DeFi体系

## Executive Summary

[[tron]] 上的去中心化货币市场：存款、借贷、抵押，以及 TRON 特有的**能量租赁**（见 [[tron-energy-delegation]]）。

**它在这个知识库里的意义是"资金效率"的对照**：借贷协议让抵押品可以同时生息，而事件市场的全额抵押完全做不到这一点。

## What It Actually Is | 它到底是什么

把两者并排看，事件市场的资金效率问题就很直观：

| | 借贷协议 | 全额抵押事件合约 |
|---|---|---|
| 抵押品状态 | **生息** | **闲置到判定日** |
| 资金效率 | 高 | **极低** |
| 风险 | 清算风险 | 无清算但有裁决风险 |

**这正是"收益型抵押"这个设计方向的由来**：[[predict-fun]] 的差异化卖点之一就是挂单与持仓资金经借贷协议生息 —— **把闲置的抵押品变成生息资产。**

**这是目前对全额抵押资金效率问题最实际的缓解手段**（见 [[fully-collateralized-market]]）。

## How It Works | 运作方式

借贷协议的基本机制是超额抵押 + 清算：抵押率跌破阈值即被清算（见 [[liquidation]]）。

**把它接到事件市场上会引入一个新问题**：抵押品在生息的同时也在承担借贷协议的风险（合约风险、清算风险、利率风险）。

**"让抵押品生息"不是免费的** —— 它把一种风险（资金闲置）换成了另一种（协议风险）。评估这类设计时要问清楚换到了什么。

## Position in the Market | 它在市场里的位置

在事件市场的价值链上，这类协议是**资金效率层的候选组件**。

它本身不是事件市场的参与者，但它代表了一个明确的方向：**在不牺牲结算确定性的前提下，让锁定的抵押品产生收益。**

**这是全额抵押模式唯一的效率出路** —— 除非保证金化被解决（见 [[margin]]）。

## What Could Break It | 什么会让它出问题

- **合约风险叠加** —— 抵押品多经过一层协议。
- **利率与流动性风险** —— 生息资产在极端行情下可能无法及时赎回。
- **清算风险** —— 若抵押品本身被用作借贷抵押。

## What To Watch | 该盯什么

- **收益型抵押在事件市场的实际采用与事故记录。**
- **是否出现专为事件市场设计的抵押品收益方案。**

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-justlend-dao-justlend-whitepaper-en-pdf]] — <https://justlend.org/docs/justlend_whitepaper_en.pdf>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: TRON生态)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
