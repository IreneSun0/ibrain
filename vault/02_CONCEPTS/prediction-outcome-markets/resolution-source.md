---
id: "concept:resolution-source"
type: concept
title: Resolution Source
title_zh: 指定结果来源
title_en: Resolution Source
aliases:
  - 指定结果来源
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - id: "concept:contract-semantics"
    rel: component-of
    note: 语义五要素 (谓词/阈值/时间窗/来源/例外) 之一
prerequisites:
  - "concept:resolution"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Resolution Source | 指定结果来源

## Executive Definition / Chinese Explanation | 定义与解释

**Resolution Source | 裁决数据源** = 合约文本里指定的、用来判定事件是否发生的权威信息来源。

它是合约语义中**最容易写清楚、也最常被写含糊**的一项。一份合约可以对"什么算发生"定义得很精确，却在"以谁公布的为准"上留白 —— 那么争议照样会来。

## Why This Matters | 为什么重要

数据源决定了裁决的**可验证性**。指定了具体来源，任何人都能自己去查、自己判断裁决对不对；没指定，裁决就变成平台或投票者的自由裁量。

这也是中心化持牌平台相对链上平台的一个真实优势：[[kalshi]] 把 **Source Agencies（指定机构）和判定日直接钉进合约条款**，这是监管框架下的强制要求，不是可选项。

## How It Works | 机制怎么运转

一个合格的数据源条款要回答四件事：

1. **主源是谁** — 具体到机构名和发布物（不是"权威媒体"这种废话）。
2. **读哪个字段** — 同一份报告里可能有初值、修正值、季调值，必须指明。
3. **什么时点的版本** — 数据会被修正。以首发值还是以修正后为准？
4. **主源失效怎么办** — 停更、改口径、延迟发布、机构被撤销时的备用方案。

**第 4 条是绝大多数合约的裸奔位置。** 而它恰恰是最容易发生的：政府停摆导致统计数据延迟发布，在美国已经发生过多次。

## Concrete Example | 具体例子

2025–2026 年，部分平台开始按数据源的可自动化程度分流裁决方式：

- **可量化 / 有权威喂价的**（加密价格、指数点位）→ [[polymarket]] 自 **2025-09** 起把价格类合约的裁决改走 [[chainlink]]，**完全绕开人工投票**。
- **需要解释的**（政治、人事、语义性事件）→ 仍走 [[uma]] 乐观预言机或平台内部团队。

这类分流把可自动核验的合约交给数据源处理，把需要解释的合约留给人工或投票机制；后者仍是主要的裁决难题。

## Common Misconceptions | 常见误解

- **误解一："权威机构的数据不会有问题。"** 会停更、会改口径、会延迟、会修正。合约必须为这些情况预留规则。
- **误解二："多写几个备用源就安全了。"** 备用源之间**冲突时以谁为准**也必须写明，否则只是把一个歧义换成了另一个。
- **误解三："数据源是技术细节。"** 它是合约的核心条款，和价格、期限同等重要。

## In Practice | 实战里怎么用

读任何一份事件合约的数据源条款，逐项对照：

| 检查 | 合格的样子 |
|---|---|
| 主源具名 | "美国劳工统计局发布的 CPI-U 月度报告"，而非"官方数据" |
| 字段明确 | 指明用初值还是修正值、季调还是非季调 |
| 版本时点 | 说明以哪一次发布为准 |
| 失效兜底 | 明文规定停更/延迟/改口径时的处理 |
| 冲突规则 | 多源并列时的优先级 |

**五项里缺任何一项，就在合约里记一笔已知风险。** 这张表跑一遍不到两分钟。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 一个合格的数据源条款要回答哪四件事？
  A: 主源具名、读哪个字段、以哪个版本时点为准、主源失效时的备用方案。
- Q: 行业按什么标准把裁决方式分流？这说明了什么？
  A: 按数据源可自动化程度：可量化的走自动化喂价（如 Chainlink），需解释的仍走预言机或人工。说明能自动化的部分就不该留给人和投票。
- Q: 为什么'主源失效怎么办'是最常见的裸奔位置？
  A: 它最容易发生（政府停摆、口径变更、延迟发布）却最常被略过，一旦发生就无规则可依。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
