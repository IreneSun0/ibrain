---
id: "concept:credit-risk"
type: concept
title: Credit Risk
title_zh: 信用风险
title_en: Credit Risk
aliases:
  - 信用风险
status: reviewed
importance: tier-2
domains:
  - institutional-risk
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
  - id: "concept:prime-brokerage"
    rel: risk-of
    note: PB/OTC/margin 体系引入信用敞口
  - id: "concept:counterparty-risk"
    rel: contrasts-with
    note: 借贷偿付能力 vs 交易/托管/清算链条的履约 — 常被混用
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Credit Risk | 信用风险

## Executive Definition / Chinese Explanation | 定义与解释

**Credit Risk | 信用风险** = 对方欠你钱但还不上的风险。它是[[counterparty-risk|对手方风险]]在借贷语境下的名字。

核心是三个量：**违约概率**（PD）、**违约时敞口**（EAD）、**违约后损失率**（LGD）。三者相乘就是预期损失。

## Why This Matters | 为什么重要

事件市场对信用风险做了一件很彻底的事：**用全额抵押把它压到零**（见 [[fully-collateralized-market]]）。

这在传统金融里几乎不可能 —— 那里没有任何一方能承受把全部名义价值锁死的资金成本。加密市场之所以能这么做，是因为它默认了极低的资本效率。

**但风险守恒**：信用风险归零，换来的是资金效率归零，以及一个传统信用框架完全没有的新风险 —— **裁决风险**（见 [[resolution-risk]]）。

## How It Works | 机制怎么运转

```
预期损失 = PD × EAD × LGD
```

传统上控制这三项的手段：
- **降 PD** —— 信用评估、授信额度、财务契约。
- **降 EAD** —— 净额结算、限额、逐日盯市。
- **降 LGD** —— 抵押品、担保、优先受偿顺位。

**全额抵押是一个极端解**：直接把 LGD 打到 0，于是 PD 和 EAD 无论多大都不重要 —— 因此**不需要做信用评估**。

**这是加密市场能对匿名对手方开放的根本原因**：它不需要知道你是谁，因为它不承担你的信用。

## Concrete Example | 具体例子

同一笔 $1M 的敞口，三种信用安排：

| 安排 | PD | LGD | 预期损失 | 需要知道对方是谁吗 |
|---|---|---|---|---|
| 无抵押授信 | 1% | 60% | $6,000 | **必须** |
| 部分抵押（50%） | 1% | 20% | $2,000 | 需要 |
| **全额抵押** | 1% | **0%** | **$0** | **不需要** |

**第三行的最后一格是加密市场的全部设计哲学**：用抵押替代身份。

**代价写在第二列之外**：那 $1M 在整个合约期内不能做别的事。对一个 6 个月的事件合约，按 5% 无风险利率算，机会成本是 **$25,000** —— **是无抵押授信预期损失的 4 倍。**

**所以"全额抵押更安全"是对的，"全额抵押更划算"通常是错的。**

## Common Misconceptions | 常见误解

- **误解一："全额抵押消除了所有风险。"** 消除的是信用风险。合约风险、裁决风险、抵押品本身的风险一个都没消除。
- **误解二："信用风险只在借贷里有。"** 任何"我先给、你后还"的结构都有 —— 包括未结算的交易。
- **误解三："有抵押就不用看对手方。"** 要看**谁保管抵押品**。抵押品在对手方手里等于没有抵押。

## In Practice | 实战里怎么用

评估任何敞口的信用安排，三问：

1. **LGD 是多少？** 有抵押吗？抵押品由谁保管、能否被挪用（见 [[custody-segregation]]）？
2. **EAD 会怎么变？** 敞口是固定的还是随价格波动？有没有净额安排？
3. **省下的信用风险，代价是什么？** 全额抵押的代价是资金占用，把它算成年化成本再比。

**第 3 问最常被跳过**：很多人把"零信用风险"当成免费的，而它的价格就写在资金成本里。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 预期损失的三个组成部分是什么？
  A: 违约概率 PD、违约时敞口 EAD、违约后损失率 LGD，三者相乘。
- Q: 为什么全额抵押让加密市场可以对匿名对手方开放？
  A: 全额抵押把 LGD 打到 0，PD 与 EAD 再大也不产生损失，因此不需要做信用评估、不需要知道对方是谁。
- Q: '全额抵押更划算'为什么通常是错的？
  A: 它消除了信用风险，但资金占用的机会成本往往数倍于无抵押授信的预期损失。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
