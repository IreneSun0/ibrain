---
id: "concept:margin"
type: concept
title: Margin
title_zh: 保证金
title_en: Margin
aliases:
  - 保证金
status: seed
importance: tier-1
domains:
  - derivatives
  - institutional-risk
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
  - id: "concept:collateral"
    rel: special-case-of
    note: 制度化、按风险动态计算的抵押品
  - id: "concept:clearing"
    rel: mechanism-of
    note: 清算体系用保证金吸收价格波动、压低违约概率
prerequisites:
  - "concept:leverage"
import_origin: xlsx-learning-map+manual
import_category: 风险管理
---

# Margin | 保证金

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

为了支持杠杆和确保履约而必须存入的风险缓冲资产，不等于交易总价值。

## Why This Matters | 为什么重要

保证金太低会扩大违约/清算风险；太高会降低资本效率。

## Concrete Example | 例子

用$10k保证金控制$50k头寸。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Margin。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-cftc-2026-05105-html]] — <https://www.cftc.gov/LawRegulation/FederalRegister/proposedrules/2026-05105.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = leverage; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
