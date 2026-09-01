---
id: "concept:concentration-risk"
type: concept
title: Concentration Risk
title_zh: 集中度风险
title_en: Concentration Risk
aliases:
  - 集中度风险
status: reviewed
importance: tier-1
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
  - id: "concept:event-var"
    rel: see-also
    note: "同一事件的跨 venue/跨工具持仓 = 事件维度的集中风险, event-var 正是其度量"
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Concentration Risk | 集中度风险

## Executive Definition / Chinese Explanation | 定义与解释

**Concentration Risk | 集中度风险** = 你以为自己分散了，其实没有。

它不是"押得太多"，而是**"很多看起来不同的头寸，实际上会同时出问题"**。集中度的危险在于它是隐藏的 —— 显性的大仓位每个人都会盯，隐性的共因暴露没人盯。

## Why This Matters | 为什么重要

事件市场有**四种独立的集中度维度**，而绝大多数人只盯第一种：

| 维度 | 隐藏方式 |
|---|---|
| **单一事件** | 同一事件的敞口散落在多个平台、多个资产类别 |
| **事件族** | 同一场选举驱动的十几个不同合约 |
| **裁决机制** | 二十个不同事件，全部由同一个预言机裁决 |
| **资金轨道** | 全部头寸的抵押品都是同一种稳定币 |

**第三种最反直觉，也最危险。** 你在 20 个互不相关的事件上各押 5%，感觉很分散 —— 但如果这 20 个合约全在同一个平台、由同一个预言机裁决，那么**一次治理攻击就能同时打击全部头寸**。这不是分散，这是 100% 集中在一个裁决机制上。

## How It Works | 机制怎么运转

识别隐藏集中度的方法是**按共因分桶**，而不是按标的分桶：

1. **列出所有头寸**。
2. **对每个头寸，标注四个标签**：驱动事件、事件族、裁决机制、抵押资产。
3. **按每个标签分别汇总**，看最大桶占总敞口多少。
4. **对每个桶问一个反事实**："如果这个桶整体失效，我损失多少？"

**第 3 步做出来的四张表，通常有一张会让人吃惊。** 而它们全部可以在开仓前算出来 —— 集中度风险是少数几个完全可预防的风险之一。

## Concrete Example | 具体例子

一个"充分分散"的事件组合：

```
20 个头寸，每个 5%，横跨政治/体育/经济/科技四个类别
```

按标的看：很分散。按共因看：

| 分桶维度 | 最大桶 | 占比 |
|---|---|---|
| 单一事件 | 最大单一事件 | 12% ✓ |
| 事件族 | "2026 美国中期选举"相关 | 35% ⚠ |
| **裁决机制** | **全部走同一个预言机** | **100%** ❌ |
| 抵押资产 | 全部 USDC | 100% ❌ |

**后两行是致命的，而按标的分散的直觉完全看不见它们。**

历史上这不是假想：Ukraine 矿产协议案证明了单一治理攻击可以影响特定预言机下的裁决结果（见 [[case-uma-dispute-trilogy]]）。

## Common Misconceptions | 常见误解

- **误解一："持仓数量多 = 分散。"** 数量与分散无关，共因才决定分散。
- **误解二："不同类别（政治/体育/经济）就是不同风险。"** 如果它们共用裁决机制和结算轨道，在那两个维度上完全相关。
- **误解三："集中度是事后才知道的。"** 恰恰相反 —— **它是最容易事前计算的风险**，只需要给每个头寸打四个标签。

## In Practice | 实战里怎么用

给你的组合做一次四维集中度体检，一张表：

```
头寸    驱动事件    事件族    裁决机制    抵押资产
_____   _________   _______   _________   _________
```

然后对四列分别做 group-by，看最大桶。

**设四条独立的限额**，不是一条：
- 单一事件 ≤ X%
- 单一事件族 ≤ Y%
- **单一裁决机制 ≤ Z%** ← 最容易被忽略、也最该设
- 单一抵押资产 ≤ W%

**只设第一条限额，等于只防了四分之一。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件市场的四种集中度维度是什么？
  A: 单一事件、事件族（相关事件）、裁决机制（同一预言机）、资金轨道（同一抵押资产）。
- Q: 为什么'20 个不同事件各押 5%'可能仍是 100% 集中？
  A: 若这 20 个合约全部由同一个预言机裁决、以同一种稳定币抵押，则在裁决机制和资金轨道两个维度上完全相关。
- Q: 为什么说集中度风险是最容易事前计算的风险？
  A: 只需给每个头寸打上驱动事件/事件族/裁决机制/抵押资产四个标签，再按每个标签汇总即可，开仓前就能算出。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 机构风险)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
