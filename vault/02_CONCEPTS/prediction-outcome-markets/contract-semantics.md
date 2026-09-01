---
id: "concept:contract-semantics"
type: concept
title: Contract Semantics
title_zh: 合约语义
title_en: Contract Semantics
aliases:
  - 合约语义
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
related: []
prerequisites:
  - "concept:event-contract"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Contract Semantics | 合约语义

## Executive Definition / Chinese Explanation | 定义与解释

**Contract Semantics | 合约语义** = 一份事件合约的文本到底把"什么算发生"定义得有多严密。

它是**可以在开盘前度量的风险因子**，而不是事后才知道的运气。同一个事件，语义写得好的合约和写得差的合约，裁决争议概率差一个数量级。

## Why This Matters | 为什么重要

语义缝隙是事件市场最廉价的攻击面。**攻击者不需要操纵市场，也不需要买通任何人 —— 只需要找到条款里那个没定义清楚的词，然后押在"技术上可辩护但违背常识"的那一边。**

而且这种攻击的防御成本极低：多写一句话就能堵上。**问题从来不是难，是没人在开盘前认真读一遍文本。**

## How It Works | 机制怎么运转

语义缺陷有四种典型形态，按出现频率排：

1. **未定义的谓词** — "卸任"、"正式宣布"、"实质控制"、"穿西装"。日常语言里清楚，法律判定上全是缝。
2. **缺失的边界条件** — 死亡算不算卸任？部分满足算不算满足？同时满足两个互斥条件怎么办？
3. **数据源未指定或未兜底** — 以谁公布的为准？它停更、改口径、延迟发布怎么办？
4. **时点与时区含糊** — "6 月底前"是哪个时区的 6 月 30 日 23:59？以事件发生时间还是以报道时间为准？

**一份合格的合约要能被改写成一段无歧义的 `if` 条件。** 改写不出来，就是有缝。

## Concrete Example | 具体例子

**Zelenskyy 西装案（2025-07）** 是语义缝隙的标本（见 [[case-uma-dispute-trilogy]] Case 2）：

合约问"Zelenskyy 在 6 月底前是否穿西装"。在有着装证据的情况下，巨鲸投票裁定为 **No**。争议的本质是 —— **"suit" 的语义边界在哪？** 军装式正装算不算西装？

**这个裁决"技术上可辩护"**（可以论证那不是传统意义的西装），**但违背了绝大多数参与者的常识理解**。受影响交易被报道至 **$215M** 量级。

**教训很直接**：如果合约文本里加一句"以是否包含配套西装外套与领带为准"，这场争议根本不会发生。**一句话的成本，$215M 的争议。**

## Common Misconceptions | 常见误解

- **误解一："语义问题是罕见的边缘案例。"** 三大公开争议案里有两起的直接成因就是语义（Zelenskyy 西装、Khamenei 卸任）。
- **误解二："用词严谨会让合约变得难懂，影响交易量。"** 交易量来自流动性，不来自文本简短。**含糊的文本换来的成交量，会在裁决日以争议和赔付的形式还回去。**
- **误解三："语义质量没法量化。"** 可以。未定义谓词的数量、边界条件的覆盖率、数据源是否有兜底方案 —— 这些都是开盘前就能打分的客观指标。

## In Practice | 实战里怎么用

开盘前给一份合约的语义质量打分，一张表就够：

| 检查项 | 满分条件 |
|---|---|
| 主体唯一性 | 主体有唯一标识，无同名歧义 |
| 谓词可判定 | 每个动词都能改写成可机械判定的条件 |
| 边界条件 | 死亡/部分满足/互斥情形均有明文规定 |
| 数据源 | 指定了主源，且写明失效时的备用方案 |
| 时点时区 | 精确到时区与时刻，说明按发生还是按报道 |

**任何一项不满分，就是一条已知的争议入口。** 把这张表跑一遍只要几分钟，但它能筛掉这个市场里绝大部分可预防的损失。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 语义缺陷的四种典型形态是什么？
  A: 未定义的谓词、缺失的边界条件、数据源未指定或未兜底、时点与时区含糊。
- Q: Zelenskyy 西装案的教训是什么？
  A: '技术上可辩护但违背常识'的裁决源于语义缝隙。一句定义就能避免 $215M 量级的争议。
- Q: 为什么说语义质量是开盘前可度量的风险因子？
  A: 未定义谓词数量、边界条件覆盖率、数据源兜底方案都是客观可检查的指标，不需要等到裁决日。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = event-contract; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
