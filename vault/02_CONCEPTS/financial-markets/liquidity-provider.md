---
id: "concept:liquidity-provider"
type: concept
title: Liquidity Provider
title_zh: 流动性提供者
title_en: Liquidity Provider
aliases:
  - 流动性提供者
status: reviewed
importance: tier-2
domains:
  - financial-markets
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
import_category: 市场结构
---
# Liquidity Provider | 流动性提供者

## Executive Definition / Chinese Explanation | 定义与解释

**Liquidity Provider (LP) | 流动性提供者** = 任何愿意在市场上挂出可成交报价、承担被动成交风险的一方。

它比"做市商"宽：做市商是有持续报价义务的专业 LP；而向 AMM 池注资的散户也是 LP，只是它的报价由公式代为执行。

## Why This Matters | 为什么重要

区分**主动 LP** 和**被动 LP**，是理解事件市场流动性结构的关键：

| | 主动 LP（做市商） | 被动 LP（AMM 注资者） |
|---|---|---|
| 报价 | 自己决定 | 公式决定 |
| 能否撤退 | **能** | **不能**（资金锁在池里） |
| 消息冲击时 | 撤单保护自己 | **被套利者按旧价吃干** |

**被动 LP 在跳变标的上尤其危险**：事件价格从 0.30 直接跳到 0.90，AMM 曲线还在按 0.30 起报 —— **中间的差价全部由 LP 承担**（见 [[automated-market-maker]]）。

## How It Works | 机制怎么运转

LP 的收益与成本：

```
收益 = 手续费分成 + 流动性激励
成本 = 无常损失 / 逆向选择 + 资金占用
```

**在事件市场，"无常损失"这个词有点误导**：现货 AMM 的无常损失在价格回归后会消失；**事件市场的价格不会回归 —— 它会跳到 0 或 1 并锁定。** 所以对事件 AMM 而言，那不是"无常"损失，是**永久损失**。

**这是很多人把现货 AMM 直觉套到事件 AMM 上时踩的坑。**

## Concrete Example | 具体例子

一个事件 AMM 池在消息冲击下的实际结果：

```
池内初始      $100,000, 报价围绕 0.30
消息公布      真实概率跳到 0.90
套利者持续买入直到池价 = 0.90
LP 最终持有   大量 NO 份额 (将归零) + 少量现金
LP 实际损失   远超已收取的手续费
```

**关键在于"不会回归"**：现货 AMM 里，价格可能回到原位，LP 的浮亏消失；**事件 AMM 里，判定日一到，价格永久停在 0 或 1。**

**所以事件 AMM 的 LP 本质上是在卖一个未定价的期权** —— 而且没有权利金保护。

## Common Misconceptions | 常见误解

- **误解一："提供流动性是被动收租。"** 它是承担逆向选择的风险，在跳变标的上尤其残酷。
- **误解二："无常损失会恢复。"** 在事件市场不会 —— 价格跳到 0/1 后锁定。
- **误解三："LP 和做市商是一回事。"** 做市商能撤退，被动 LP 不能。**这个差别在压力时刻决定生死。**

## In Practice | 实战里怎么用

考虑给任何事件市场提供流动性前，问四件事：

1. **是主动还是被动？** 能不能在消息来临时撤出？
2. **用的什么曲线？** LMSR 类的损失有界（由参数 b 决定），常数乘积没有这个保证。
3. **激励能否覆盖预期逆向选择？** 算一下，不要看年化收益率宣传。
4. **判定日临近时会怎样？** 这是损失集中发生的窗口。

**第 4 条最常被忽略**：很多人在判定日前才发现自己无法退出。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 主动 LP 与被动 LP 的关键区别是什么？
  A: 主动 LP（做市商）能在消息来临时撤单保护自己；被动 LP 的资金锁在池里，会被套利者按旧价吃干。
- Q: 为什么'无常损失'这个词在事件市场有误导性？
  A: 现货 AMM 的浮亏在价格回归后消失；事件价格判定后永久停在 0 或 1，损失是永久的而非无常的。
- Q: 事件 AMM 的 LP 本质上在做什么？
  A: 卖一个未定价的期权，而且没有权利金保护 —— 承担跳变风险却只收手续费分成。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
