---
id: "concept:put-option"
type: concept
title: Put Option
title_zh: 看跌期权
title_en: Put Option
aliases:
  - 看跌期权
status: reviewed
importance: tier-2
domains:
  - derivatives
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
  - id: "concept:option"
    rel: special-case-of
prerequisites:
  - "concept:option"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Put Option | 看跌期权

## Executive Definition / Chinese Explanation | 定义与解释

**Put Option | 看跌期权** = 给你**在到期日以约定价格卖出**标的的权利，但没有义务。

它是市场上最直接的**保险工具**：付一笔权利金，把下跌风险的尾部截断。

## Why This Matters | 为什么重要

看跌期权把"保险"这个概念在金融里讲清楚了：**你付保费，把最坏情况的损失封顶。**

这正是[[resolution-insurance|裁决保险]]目前缺失的那种东西 —— 事件市场里"合约被判错"的风险，没有任何对应的看跌期权可买（见 [[resolution-risk]]）。

**理解 put 的定价逻辑，就理解了为什么裁决保险难做**：保险需要可度量的违约率来定费率，而裁决出错的历史数据至今无人系统性收集。

## How It Works | 机制怎么运转

```
到期收益 = max(行权价 − 标的价, 0) − 权利金
```

put 的两种典型用法：

| 用法 | 你的其他头寸 | 目的 |
|---|---|---|
| **保护性看跌** | 持有标的现货 | **保险** —— 封住下跌 |
| **裸买看跌** | 无 | **投机** —— 押注下跌 |

**同一份合约，两种完全不同的性质。** 这与事件合约完全同构：对真实持有该事件敞口的人是对冲，对没有敞口的人是投机（见 [[event-risk]]）。

**"是不是对冲"从来不是合约的属性，而是持有人整体头寸的属性。**

## Concrete Example | 具体例子

一家基金持有 $10M 政策敏感板块，担心某项监管落地：

| 方案 | 成本 | 保护 | 问题 |
|---|---|---|---|
| 卖掉持仓 | 放弃上行 | 完全 | 若监管没来，踏空 |
| 买板块看跌期权 | 权利金约 $300k | 部分（板块相关性不完美） | **基差风险** |
| 买"监管落地"事件合约 | 全额抵押占用 | **精确对准事件** | 资金效率低 + 裁决风险 |

**第三行是事件合约的理论优势**：它对准的是**事件本身**，没有基差风险 —— 前提是合约语义写得准（见 [[contract-equivalence]]）。

**这就是事件市场的核心价值主张，也是它成败的关键点：语义精度换来了对冲精度。**

## Common Misconceptions | 常见误解

- **误解一："买 put 是看空。"** 保护性看跌的持有人通常看多 —— 他只是想封住尾部。
- **误解二："保险总是划算的。"** 权利金是确定成本，保护是概率收益。长期无脑买保险会持续亏损。
- **误解三："事件合约可以完全替代 put。"** 只在合约语义精确对准你的敞口时成立；语义有缝就退化成基差头寸。

## In Practice | 实战里怎么用

任何"我要对冲"的需求，按三步走：

1. **写下敞口** —— 事件 X 反向发生时我损失多少？
2. **找工具并算基差** —— 这个工具与我的敞口有多贴合？差在哪？
3. **算全成本** —— 权利金或资金占用，占敞口的百分比。

**超过敞口的 30% 就该重新考虑**：那说明市场认为这个风险很可能发生，你也许该直接调整业务而不是买保险。

**对事件合约多问一条**：合约条款的五要素是否精确对准了你的敞口？对不上就不是对冲。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 同一份看跌期权，什么时候是保险、什么时候是投机？
  A: 取决于持有人的其他头寸：持有标的时是保险（封住下跌），无敞口时是投机。事件合约完全同构。
- Q: 事件合约相对板块看跌期权的理论优势是什么？前提是什么？
  A: 它对准事件本身，没有基差风险。前提是合约语义精确对准你的敞口，否则退化成基差头寸。
- Q: 理解 put 的定价为什么有助于理解裁决保险为何难做？
  A: 保险需要可度量的违约率来定费率，而'裁决出错'的历史数据至今无人系统性收集，因而无法定价。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = option; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
