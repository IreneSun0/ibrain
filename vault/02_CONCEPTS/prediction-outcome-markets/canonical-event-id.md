---
id: "concept:canonical-event-id"
type: concept
title: Canonical Event ID
title_zh: 统一事件标识
title_en: Canonical Event ID
aliases:
  - 统一事件标识
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
  - id: "concept:event-var"
    rel: mechanism-of
    note: 跨 venue 敞口聚合的标识基础 — 没有它 exposure 无法可靠汇总
  - id: "org:opticodds"
    rel: instantiated-by
    note: 只返回真正跨平台事件的 canonical 标识符
prerequisites:
  - "concept:contract-equivalence"
import_origin: xlsx-learning-map+manual
import_category: 预测市场数据
---
# Canonical Event ID | 统一事件标识

## Executive Definition / Chinese Explanation | 定义与解释

**Canonical Event ID | 事件规范标识** = 给"现实世界里的同一个事件"分配一个跨平台稳定的唯一标识，使不同场所上指向它的合约能被可靠地关联起来。

它解决的问题很土但很致命：**同一件事，在十个平台上有十个不同的名字。**

## Why This Matters | 为什么重要

没有规范标识，事件市场的数据层就是一堆无法拼接的孤岛。

具体卡住的能力：
- **跨场所行情聚合** — 无法把同一事件的多个盘口合并显示。
- **历史回溯** — 无法追踪同一事件在不同平台的价格演化。
- **风险聚合** — 一个基金在五个平台持有同一事件的头寸，**如果不能识别它们是同一事件，就无法计算真实的集中度**。

**第三条是机构入场的硬门槛。** 风控系统必须能回答"我在这件事上总共押了多少"，答不出来就不能配置。

## How It Works | 机制怎么运转

事件标识的难点不在生成 ID，在**判定"这是不是同一个事件"**：

1. **命名差异** — "Fed cuts rates in December" vs "美联储 12 月降息" vs "FOMC Dec rate cut"。
2. **粒度差异** — 一个平台按"降息与否"开盘，另一个按"降 25bp / 50bp / 不降"开三个盘。**一对多的映射。**
3. **条款差异** — 名字一样但判定日或数据源不同，**这时候恰恰不该给同一个 ID**（见 [[contract-equivalence]]）。
4. **时间演化** — 事件被推迟、被取消、被拆分时，ID 怎么继承？

**关键设计判断：ID 应该标识"现实世界的事件"，而不是"某个合约"。** 一个事件对应多个合约，多个合约共享一个事件 ID 但各有自己的合约 ID —— 这样才能既聚合又不混淆。

## Concrete Example | 具体例子

"2026 年美联储 12 月议息结果"这一个现实事件，在不同场所的形态：

| 场所 | 合约形态 | 与事件的关系 |
|---|---|---|
| A | "是否降息"（二元） | 1 个合约 |
| B | "降 0 / 25bp / 50bp"（三选一） | 3 个合约 |
| C | "降息幅度区间"（多档） | N 个合约 |

**正确的建模**：一个 `event:fomc-2026-12-decision` 事件 ID，下挂 A/B/C 各自的合约 ID，并记录每个合约与事件的映射关系（二元/多档/区间）以及各自的判定条款。

**错误的建模**：给每个合约一个独立 ID 且互不关联 —— 那就回到了孤岛。**也错**：把它们全都当成同一个合约 —— 那就丢失了条款差异。

## Common Misconceptions | 常见误解

- **误解一："用 hash 就能生成稳定 ID。"** hash 只能保证同样的输入得到同样的输出，**不能判断两段不同文本是否指向同一事件**。那需要判断，不是哈希。
- **误解二："ID 一样就能对冲。"** ID 表示"关于同一事件"，等价性还需要五维对齐。**同事件 ≠ 等价合约。**
- **误解三："让平台自己出标准就行。"** 平台自建标识可能与自身流动性策略冲突；中立标识层更便于跨平台采用。

## In Practice | 实战里怎么用

设计一个事件标识体系，四条原则：

1. **ID 标识事件，不标识合约** —— 一对多关系显式建模。
2. **ID 一经分配永不更改** —— 事件被推迟/改期时追加属性，不换 ID（与知识库的 id 纪律同源）。
3. **映射关系带类型** —— 二元 / 多档 / 区间 / 条件复合，各自标注。
4. **合约条款差异单独记录** —— 同 ID 不代表可互换，条款差异是必须保留的字段。

**做完这四条，"我在这件事上总共押了多少"才第一次变成一个可以被计算的问题。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么事件规范标识是机构入场的硬门槛？
  A: 风控必须能计算'在同一事件上的总敞口'。跨平台头寸若不能识别为同一事件，集中度就算不出来，无法配置。
- Q: ID 应该标识事件还是合约？为什么？
  A: 标识事件。一个事件对应多个合约（二元/多档/区间），这样才能既聚合行情与风险，又保留各合约的条款差异。
- Q: 为什么 hash 解决不了事件标识问题？
  A: hash 只保证相同输入得相同输出，无法判断两段不同文本是否指向同一现实事件 —— 那需要判断而非计算。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
