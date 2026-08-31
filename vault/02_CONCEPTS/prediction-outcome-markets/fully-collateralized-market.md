---
id: "concept:fully-collateralized-market"
type: concept
title: Fully Collateralized
title_zh: 全额抵押
title_en: Fully Collateralized
aliases:
  - Fully Collateralized
  - Fully Collateralized Market
  - 全额抵押
status: seed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - "source:2026-08-26-cftc-2026-05105-html"
related:
  - id: "concept:margin"
    rel: contrasts-with
    note: 全额抵押无违约链条但资本效率低 — CFTC 2026 保证金化提案的核心权衡
  - id: "venue:polymarket"
    rel: instantiated-by
    note: USDC 全额抵押结算
  - id: "venue:hyperliquid-hip4"
    rel: instantiated-by
    note: HIP-4 全额抵押模型
prerequisites:
  - "concept:collateral"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---

# Fully Collateralized | 全额抵押

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

最坏情况下的支付义务已经由100%所需抵押资产支持。

## Why This Matters | 为什么重要

降低杠杆和违约复杂度，但资本效率较低。

## Concrete Example | 例子

投入$1拆成完整YES+NO组合。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Fully Collateralized。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = collateral; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
