---
id: "concept:anti-money-laundering"
type: concept
title: AML
title_zh: 反洗钱
title_en: AML
aliases:
  - AML
  - Anti-Money Laundering
  - 反洗钱
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
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# AML | 反洗钱

## Executive Definition / Chinese Explanation | 定义与解释

**AML (Anti-Money Laundering) | 反洗钱** = 一整套法定义务，用来防止金融体系被用来清洗犯罪所得。

[[know-your-customer|KYC]] 是它的入口环节；AML 还包括交易监控、可疑活动上报、制裁名单筛查、以及记录保存。

## Why This Matters | 为什么重要

AML 对事件市场有一个特别的敏感点：**这类市场天然适合价值转移。**

两个账户可以在同一个事件上对赌，一方故意输 —— 资金就完成了转移，表面上看是"交易亏损"。这在传统市场也存在，但事件市场的**长尾合约深度极薄**，两个人就能构成一个完整的市场，不需要第三方参与。

**这是监管对预测市场最实质的担忧之一**，也是长尾合约面临更严格审查的原因。

## How It Works | 机制怎么运转

AML 的四个支柱：

| 支柱 | 内容 |
|---|---|
| **KYC / CDD** | 知道客户是谁、钱从哪来 |
| **交易监控** | 识别异常模式（对倒、拆分、异常路径） |
| **制裁筛查** | 对照 OFAC 等名单 |
| **上报与留痕** | 可疑活动报告、记录保存 |

**加密特有的一层是链上分析**：地址聚类、资金溯源、混币器识别（见 [[know-your-transaction]]）。

**事件市场特有的监控难点**：如何区分"故意输钱转移价值"和"判断失误"？在薄盘口上，两者的链上痕迹几乎一样 —— **这需要事件维度的跨市场监测能力，而那一层目前空着**（见 [[market-integrity]]）。

## Concrete Example | 具体例子

一个薄盘口上的可疑模式：

```
账户 A 在某长尾合约挂买单 0.90 (真实概率约 0.10)
账户 B 全部吃掉, 成交 $200,000
事件揭晓, A 亏 $180,000, B 赚 $180,000
```

**表面上**：A 判断失误，B 判断正确。
**实质上**：可能是一次 $180,000 的价值转移。

**区分两者需要的证据**：账户关联性、历史行为模式、下单时机、以及该盘口是否只有这两方参与。

**这些证据分散在链上数据、平台数据和跨市场数据里，目前没有任何一方能看全** —— 场馆有利益冲突，监管看不到链上与跨境。

## Common Misconceptions | 常见误解

- **误解一："AML 就是 KYC。"** KYC 是入口环节，AML 还包括持续监控、筛查和上报。
- **误解二："链上透明所以 AML 更容易。"** 透明的是交易，不是身份和意图。**看得见资金流动，不等于看得懂它为什么流动。**
- **误解三："小平台不用做 AML。"** 义务通常按业务性质而非规模确定；且出入金环节的银行/发行方会把义务传导下来。

## In Practice | 实战里怎么用

评估一个事件市场平台的 AML 成熟度，看四件事：

1. **有没有交易监控？** 不是只有 KYC。
2. **监控覆盖跨市场吗？** 单平台监控看不到跨场所的对倒。
3. **制裁筛查怎么做？** 链上地址也筛吗？
4. **出过案例吗？** 公开过执法或自查结果的平台，通常能力更实。

**对做基础设施的人**：**事件维度的跨市场监测层是当前明确空着的位置** —— 场馆不能自我监管，监管机构看不全，而这一层需要的正是主键 + 等价性 + 全场数据。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: AML 的四个支柱是什么？
  A: KYC/CDD、交易监控、制裁筛查、可疑活动上报与记录保存。
- Q: 为什么事件市场天然适合价值转移？
  A: 两个账户可在薄盘口上对赌，一方故意输即完成转移，表面看只是交易亏损，且不需要第三方参与。
- Q: 区分'故意输钱'和'判断失误'需要什么证据？为什么难？
  A: 需要账户关联性、历史行为、下单时机与盘口参与者构成；难在证据分散于链上、平台与跨市场数据，无人看全。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
