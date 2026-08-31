---
id: "concept:oracle"
type: concept
title: Oracle
title_zh: 预言机/外部事实输入层
title_en: Oracle
aliases:
  - 预言机
status: seed
importance: tier-1
domains:
  - blockchain
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-27
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "protocol:chainlink"
    rel: instantiated-by
    note: 价格类结算主流选择; Polymarket 2026 起价格市场采用
  - id: "protocol:pyth-network"
    rel: instantiated-by
    note: 第一方金融数据 oracle (交易公司/交易所直发)
  - id: "protocol:winklink"
    rel: instantiated-by
    note: TRON 生态 oracle
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---

# Oracle | 预言机/外部事实输入层

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

把链外价格、天气、比赛结果、新闻或其他事实输入智能合约的机制。

## Why This Matters | 为什么重要

链本身只知道链内状态，无法天然知道“总统是否辞职”。

## Concrete Example | 例子

Chainlink、WINkLink、UMA。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Oracle。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = smart-contract; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
