---
id: "concept:resolution-risk"
type: concept
title: Resolution Risk
title_zh: 结果判定风险
title_en: Resolution Risk
aliases:
  - 结果判定风险
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
  - id: "concept:resolution"
    rel: risk-of
  - id: "concept:oracle-risk"
    rel: contrasts-with
    note: 规则语义歧义 (来源如实也可能裁错) vs 数据管道/机制失效
  - id: "concept:dispute-mechanism"
    rel: mitigated-by
  - id: "concept:resolution-insurance"
    rel: mitigated-by
    note: 候选工具 — 方向对但裁错的风险转移
prerequisites:
  - "concept:resolution"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Resolution Risk | 结果判定风险

## Executive Definition / Chinese Explanation | 定义与解释

**Resolution Risk | 裁决风险** = 合约最终按错误结果结算的风险，无论错误来自语义漏洞、预言机被操纵、数据源失效，还是判定方的自由裁量。

**它是事件市场特有的风险类别** —— 在传统衍生品的风险分类里找不到对应项，因为传统合约的结算触发条件是可观测价格，不需要判断。

## Why This Matters | 为什么重要

这是把预测市场当资产类别看时，**必须单列的一项风险**。

一个机构做风险预算时，会算市场风险、对手方风险、流动性风险 —— 但如果不单列裁决风险，它就会系统性低估自己的敞口。因为裁决风险有个特点：**它与市场风险不相关，且是二元的**。市场风险让你亏 20%，裁决风险让你亏 100%。

**而且它不是尾部事件。** 2025–2026 年公开的重大裁决争议按年计频发，涉及金额从数百万到 $215M 量级。这是常态风险。

## How It Works | 机制怎么运转

裁决风险有四个可分别度量的来源：

| 来源 | 度量方式 | 缓解手段 |
|---|---|---|
| **语义漏洞** | 未定义谓词数、边界条件覆盖率（见 [[contract-semantics]]） | 开盘前文本审查 |
| **预言机操纵** | 攻击成本 vs 可影响市场规模（见 [[oracle-risk]]） | 分流自动化裁决、提高投票分散度 |
| **数据源失效** | 主源是否有兜底条款（见 [[resolution-source]]） | 明文规定备用源与优先级 |
| **裁量偏差** | 判定方独立性、历史争议处理记录 | 独立委员会、公开争议档案 |

**四项都是可以在开盘前打分的**，不需要等到裁决日才知道。这是裁决风险和市场风险最大的区别 —— 市场风险不可预测，裁决风险很大程度上可预判。

## Concrete Example | 具体例子

三个案子，三种来源，同一类损失（见 [[case-uma-dispute-trilogy]] 与 [[case-kalshi-khamenei-settlement]]）：

| 案例 | 时间 | 来源 | 规模 |
|---|---|---|---|
| Ukraine 矿产协议 | 2025-03 | 预言机操纵（投票权可买） | ~$7M 市场，**拒绝退款** |
| Zelenskyy 西装 | 2025-07 | 语义缝隙 | 受影响交易报道至 **$215M** |
| Khamenei 卸任 | 2026-03 | 语义缝隙 | 冻结 **$54M**，赔付 **~$2.2M** |

**关键对比在最后一列**：链上平台（Ukraine 案）**零赔付**，持牌平台（Khamenei 案）**赔了 $2.2M 并修改规则备案 CFTC**。

**这就是监管框架的实际价值** —— 不是它能防止争议，而是它让赔付成为可能。

## Common Misconceptions | 常见误解

- **误解一："裁决风险是小概率黑天鹅。"** 年度级频发，且随市场规模增长而增长（盘口越大，攻击越划算）。
- **误解二："分散到多个市场就能分散裁决风险。"** 如果这些市场共用同一个预言机或同一套合约模板，**风险是完全相关的**，分散无效。
- **误解三："出事平台会赔。"** Ukraine 案的先例是不赔。**做仓位决策时应默认零赔付**，赔付是意外之喜不是权利。

## In Practice | 实战里怎么用

把裁决风险写进你的仓位计算，而不是当成注脚：

```
有效期望收益 = 名义期望收益 × (1 − 裁决出错概率) − 裁决出错时的损失 × 裁决出错概率
```

其中"裁决出错概率"由上面四项来源打分估计。实操上：

1. **语义分低的合约直接降仓或不做** —— 这是最便宜的风控。
2. **同一预言机下的头寸算作一个集中度桶**，设总敞口上限。
3. **临近裁决日主动降仓** —— 争议风险集中爆发在这个窗口。

**第 2 条最容易被忽略。** 很多人以为自己分散在 20 个市场，实际上是 20 个头寸押在同一个预言机上。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么裁决风险必须单列，不能并入市场风险？
  A: 它与市场风险不相关且是二元的：市场风险让你亏部分，裁决风险让你亏全部。不单列会系统性低估敞口。
- Q: 裁决风险的四个可度量来源是什么？
  A: 语义漏洞、预言机操纵、数据源失效、裁量偏差 —— 四项都可在开盘前打分。
- Q: 链上平台与持牌平台在裁决出错后的处理有什么关键差异？
  A: Ukraine 案链上平台零赔付；Khamenei 案持牌平台赔付约 $2.2M 并把新规则备案 CFTC。监管框架让赔付成为可能。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = resolution; typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
