---
id: "concept:policy-engine"
type: concept
title: Policy Engine
title_zh: 策略/政策控制引擎
title_en: Policy Engine
aliases:
  - 策略
status: reviewed
importance: tier-1
domains:
  - industry-strategy
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
  - id: "concept:risk-engine"
    rel: contrasts-with
    note: "风险引擎算出风险, 政策引擎决定放不放行"
prerequisites:
  - "concept:risk-engine"
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Policy Engine | 策略/政策控制引擎

## Executive Definition / Chinese Explanation | 定义与解释

**Policy Engine | 政策引擎** = 持有规则、并把风险读数转换成**动作**的系统：拦截、限额、路由、审批。

它是风险数据真正产生付费意愿的地方。**机构采购风险数据的最终理由不是"想知道"，而是"要照办"。**

## Why This Matters | 为什么重要

这是理解风险信息商业价值的关键：

一份"这个市场的裁决风险偏高"的报告，如果只是被人读一遍，它的价值接近零。
同一份数据，如果进入了一条 `if 争议概率 > 10% then 禁止新开仓` 的规则，它就变成了业务流程的一部分 —— **而业务流程的依赖是会付费的。**

**所以风险数据的产品终局是成为政策引擎的标准输入源**：每个数据字段都应该为"能写进一条 if 语句"而设计。

## How It Works | 机制怎么运转

风险引擎与政策引擎的接力关系：

```
风险引擎          政策引擎
输出读数    →     持有规则      →     执行动作
"争议概率 12%"    ">10% 禁新开"       拦截这笔单
```

三层的归属完全不同：

| 层 | 谁拥有 | 能不能外购 |
|---|---|---|
| **读数** | 数据供应商 | **可以** |
| **规则** | 机构自己 | **不能**（风险偏好是主权） |
| **执行** | 嵌进交易与合规流程 | 机构自建或系统集成 |

**动作分级通常是三档**：`WARN`（警告但放行）/ `REVIEW`（转人工审批）/ `BLOCK`（直接拦截）。分级存在的意义是让规则可以先以低强度上线，积累信任后再收紧。

## Concrete Example | 具体例子

一条完整的规则链，从数据到动作：

```
IF   合约.语义分 < 0.6
AND  头寸.名义 > $500k
THEN REVIEW（转风控人工审批）

IF   裁决机制.当前争议数 > 3
OR   合约.判定日 距今 < 48h
THEN WARN + 禁止加仓

IF   单一裁决机制敞口 > 30%
THEN BLOCK 新开仓
```

**注意每一条规则里的数据字段**：语义分、争议数、判定日、裁决机制敞口。**这四个字段在今天的任何标准市场数据源里都不存在。**

**这就是为什么"能写进 if 语句的字段"是一个真实的产品设计目标**，而不是漂亮话。

## Common Misconceptions | 常见误解

- **误解一："政策引擎就是风控系统。"** 它是风控系统里"规则与执行"的那一半；读数那一半是风险引擎。
- **误解二："规则越多越安全。"** 规则冲突和误报会让人绕过系统。**少而准的规则胜过多而吵的规则。**
- **误解三："数据卖给分析师就够了。"** 分析师读完就忘；进了 if 语句的数据才会被持续付费。

## In Practice | 实战里怎么用

如果你在设计风险数据产品，用一个测试检验每个字段：

> **"这个字段能不能直接写进一条 `if` 语句？"**

- "该市场存在裁决不确定性" —— **不能**（不可量化）。
- "该合约语义分 = 0.42，低于阈值 0.6" —— **能**。
- "UMA 上有争议" —— **不能**（无时间、无数量）。
- "该裁决机制当前未决争议数 = 3，7 日内新增 2" —— **能**。

**能通过这个测试的字段才有商业价值。** 剩下的是内容，不是产品。

如果你是采购方：**要求供应商给出可机读的字段定义和阈值建议**，而不是 PDF 报告。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说风险数据的产品终局是成为政策引擎的输入源？
  A: 机构付费的理由不是'想知道'而是'要照办'。数据只有进入准入/额度/路由/审批的自动化流程才产生持续付费意愿。
- Q: 读数、规则、执行三层各自能否外购？
  A: 读数可外购；规则必须机构自持（风险偏好是主权）；执行嵌进机构自己的交易与合规流程。
- Q: 检验一个风险数据字段是否有商业价值的测试是什么？
  A: 它能不能直接写进一条 if 语句 —— 需要可量化、有阈值、有时间维度，而不是定性描述。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
