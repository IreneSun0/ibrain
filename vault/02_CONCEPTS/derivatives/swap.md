---
id: "concept:swap"
type: concept
title: Swap
title_zh: 互换
title_en: Swap
aliases:
  - 互换
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
  - "source:2026-08-26-cftc-derivatives-basics-html"
related:
  - id: "concept:derivative"
    rel: special-case-of
prerequisites:
  - "concept:derivative"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Swap | 互换

## Executive Definition / Chinese Explanation | 定义与解释

**Swap | 掉期 / 互换** = 双方约定在未来一段时间里交换现金流的合约：我付固定、你付浮动，或者反过来。

它是场外衍生品里名义规模最大的一类，**也是"事件合约是不是 swap"这个法律问题的核心** —— 因为在美国，DCM 上市的 swap 归 CFTC 排他管辖。

## Why This Matters | 为什么重要

这个分类问题不是学术争论，它决定了整个赛道的监管归属。

**美国的论证链条**：
1. 事件合约是一种 swap（约定基于某个事件发生与否交换现金流）。
2. Swap 在 DCM 上市 → **归 CFTC 排他管辖**。
3. 因此州博彩法不适用。

**CFTC 正是据此对州政府主张联邦优先权**（见 [[regulatory-risk]]）。

**所以"swap"这个词的定义边界，直接决定了预测市场在美国是合法衍生品还是非法赌博。** 这场争论目前在法庭上。

## How It Works | 机制怎么运转

swap 的基本结构：

```
甲方 → 固定现金流 → 乙方
甲方 ← 浮动现金流 ← 乙方
```

常见类型：利率互换（固定换浮动）、货币互换、信用违约互换（CDS）。

**事件合约与 CDS 的结构相似性值得注意**：
- **CDS**：定期付保费；若信用事件发生，收到赔付。
- **事件合约**：一次性付价格；若事件发生，收到 $1。

**两者都是"为某个离散事件是否发生而交换现金流"** —— 这正是把事件合约归入 swap 家族的技术依据。

## Concrete Example | 具体例子

同一个"某公司违约"的风险，两种工具的对照：

| | CDS | 事件合约 |
|---|---|---|
| 付款方式 | 定期保费 | 一次性 |
| 触发 | 信用事件（有 ISDA 定义） | 合约条款定义 |
| 谁判定 | **ISDA 决定委员会** | 平台或预言机 |
| 标准化程度 | **极高**（ISDA 主协议） | 各平台不一 |

**第三、四行是关键差距**：CDS 有一套沉淀了几十年的标准定义与集中裁定机制；**事件合约没有 —— 每个平台自己定义、自己裁定。**

**这正是[[contract-equivalence|合约等价性]]问题的来源，也是这个市场最需要补的基础设施。** ISDA 那套东西，事件市场还没有。

## Common Misconceptions | 常见误解

- **误解一："swap 就是复杂的场外产品。"** 结构可以很简单；复杂的是条款与信用安排。
- **误解二："事件合约是 swap 只是法律技巧。"** 结构上确实同源：都是基于事件交换现金流。
- **误解三："有了监管归属就万事大吉。"** 归属解决的是"谁管"，不解决"条款是否清晰"—— 后者仍是每个平台自己的事。

## In Practice | 实战里怎么用

理解 swap 对事件市场的两个实用推论：

1. **看一份事件合约时，把它当 swap 读**：谁在什么条件下向谁支付多少？条件的定义精确到什么程度？
2. **对照 ISDA 的成熟度**：CDS 花了几十年才把"什么算信用事件"定义清楚。**事件市场目前还在这个过程的起点** —— 这既是风险，也是最明确的基础设施机会（见 [[contract-semantics]]）。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么'事件合约是不是 swap'是个关键法律问题？
  A: DCM 上市的 swap 归 CFTC 排他管辖，若成立则州博彩法不适用；这是联邦优先权论证的基础。
- Q: 事件合约与 CDS 的结构相似性是什么？
  A: 两者都是为某个离散事件是否发生而交换现金流 —— 这是把事件合约归入 swap 家族的技术依据。
- Q: CDS 有而事件合约缺的关键基础设施是什么？
  A: ISDA 式的标准化定义与集中裁定机制 —— 事件合约每个平台自己定义、自己裁定，这正是等价性问题的来源。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cftc-derivatives-basics-html]] — <https://www.cftc.gov/LearnAndProtect/AdvisoriesAndArticles/derivatives_basics.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = derivative; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
