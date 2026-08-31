---
id: "concept:counterparty-risk"
type: concept
title: Counterparty Risk
title_zh: 交易对手风险
title_en: Counterparty Risk
aliases:
  - 交易对手风险
status: seed
importance: tier-1
domains:
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
related:
  - id: "concept:over-the-counter"
    rel: risk-of
    note: 无 CCP 的双边交易是对手方风险的裸露形态
  - id: "concept:clearinghouse"
    rel: mitigated-by
    note: CCP 成为所有人的对手方 + 保证金/违约基金瀑布
  - id: "concept:collateral"
    rel: mitigated-by
  - id: "concept:custody-segregation"
    rel: mitigated-by
    note: 平台破产时客户资产不被当作公司财产
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---

# Counterparty Risk | 交易对手风险

> 本页由学习地图 workbook 确定性导入 (status: seed)。原文字段完整保留; enrich 时不删原文, 追加即可。

## Executive Definition / Chinese Explanation | 定义与解释

和你交易、托管、清算或提供信用的一方无法履约、破产、冻结资产或违约的风险。

## Why This Matters | 为什么重要

价格判断正确仍可能因为对手方失败而亏钱。

## Concrete Example | 例子

交易所倒闭、OTC dealer不付款。


## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed, 2026-08-27 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 不看笔记, 用两三句话向一个聪明的外行解释 Counterparty Risk。
  A: 见上文定义。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
