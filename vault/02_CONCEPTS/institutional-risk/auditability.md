---
id: "concept:auditability"
type: concept
title: Auditability
title_zh: 可审计性
title_en: Auditability
aliases:
  - 可审计性
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
  - id: "concept:data-infrastructure"
    rel: see-also
    note: 审计能力 = 数据基础设施的输出 — 可重建当时的数据/规则/决定
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Auditability | 可审计性

## Executive Definition / Chinese Explanation | 定义与解释

**Auditability | 可审计性** = 事后能够独立重建"当时发生了什么、依据什么做的决定"的能力。

关键词是**独立** —— 不需要相信任何一方的说法，就能自己把过程复原一遍。

## Why This Matters | 为什么重要

它是三条线的汇合点：

- **对机构** —— 尽调的硬门槛。**无法审计的服务进不了采购流程**，这不是偏好问题，是合规要求。
- **对监管** —— 合规的通行证。
- **对争议** —— 唯一的事实依据。争议发生时，说不清"当时依据什么"的一方通常直接输。

**而且它有一个残酷的性质：可审计性必须在事前设计进系统，事后无法补建。** 就像历史数据不能事后补录一样。

## How It Works | 机制怎么运转

可审计性由四样东西构成，缺一不可：

1. **输入快照** —— 决策时刻看到的原始数据是什么样，原样存下来。
2. **规则版本化** —— 当时生效的是哪一版规则？规则改了要能回溯到旧版。
3. **决策日志** —— 谁在什么时候、依据什么做了什么动作。
4. **输出锚定** —— 结果不可事后篡改（哈希上链是一种低成本增强）。

**第 2 条最常被忽略**：很多系统能查到"当时的数据"和"当时的结论"，但查不到"当时的规则"。规则一改，历史决策就变得无法解释。

## Concrete Example | 具体例子

链上事件市场在这件事上有一个**结构性优势**，值得理解清楚：

传统场馆说"相信我们的账"；链上场馆说"**自己去查**"。

- [[polymarket]] 的持仓与结算全部链上可查。
- 任何第三方**无需场馆授权**就能核验其历史结算行为：哪个合约、什么时候、判成了什么、钱付给了谁。

**审计从特权变成了公共品。** 这重新定义了第三方评价机构的可能性 —— 在传统市场里，评价一家交易所的结算质量需要它配合；在链上，不需要。

**代价是隐私**：可审计与可监视是同一件事的两面。

## Common Misconceptions | 常见误解

- **误解一："上链就等于可审计。"** 链保证记录不可篡改，但如果**规则版本和输入快照没存**，你依然无法解释当时为什么那样判。
- **误解二："可审计性可以事后补。"** 补不了。没记录的输入和规则版本永久丢失。
- **误解三："可审计性只是合规负担。"** 它同时是产品能力 —— **能被审计的服务才进得了机构采购流程**，这直接决定了客户是谁。

## In Practice | 实战里怎么用

给任何一个系统做可审计性体检，四问：

1. **能不能重建任意一个历史时刻的输入？**
2. **能不能查到当时生效的规则版本？**
3. **每个自动化动作有没有留下"为什么"的记录？**
4. **历史记录能不能被事后修改？谁有权限？**

**四问全过，这个系统才能被机构采购。**

对做产品的人还有一条：**既要自身可审计（公信力），也可能在出售审计能力（帮客户重建他们的历史敞口与判定记录）** —— 后者往往是更值钱的那一半。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 可审计性的四个构成要素是什么？哪个最常被忽略？
  A: 输入快照、规则版本化、决策日志、输出锚定。规则版本化最常被忽略 —— 规则一改历史决策就无法解释。
- Q: 链上市场在可审计性上的结构性优势是什么？代价是什么？
  A: 第三方无需场馆授权即可核验其结算历史，审计从特权变成公共品。代价是隐私 —— 可审计与可监视是一体两面。
- Q: 为什么说可审计性必须事前设计？
  A: 没有记录下来的输入快照和规则版本永久丢失，事后无法补建，就像历史数据不能事后补录。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
