---
id: "concept:hedging"
type: concept
title: Hedging
title_zh: 对冲
title_en: Hedging
aliases:
  - 对冲
status: reviewed
importance: tier-1
domains:
  - derivatives
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
import_category: 风险管理
---
# Hedging | 对冲

## Executive Definition / Chinese Explanation | 定义与解释

**Hedging | 对冲** = 建立一个反向头寸，让你原有的风险敞口减小。

对冲的目的不是赚钱，是**把不想承担的不确定性转移出去**。判断一次对冲成不成功，不看它赚没赚，看它**有没有让你的结果分布变窄**。

## Why This Matters | 为什么重要

事件市场存在的经济学理由就是对冲：

- 一家航空公司对冲油价，用期货。
- 一家跨国公司对冲汇率，用远期。
- **一家公司对冲"关税会不会落地"，用什么？**

在事件合约出现之前，第三个问题**没有工具**。企业只能在预算里放一个假设，然后祈祷。

**"存在真实的对冲需求"正是事件合约被划入衍生品监管而非博彩的法律论证核心。**

## How It Works | 机制怎么运转

对冲的四个步骤，每一步都可能出错：

1. **识别敞口** —— 我到底暴露于什么？多少？（见 [[event-var]]）
2. **选工具** —— 哪个合约的支付函数最贴合我的敞口？
3. **定规模** —— 对冲比率是多少？全额还是部分？
4. **持续监控** —— 敞口和对冲工具的关系会变吗？

**在事件市场，第 2 步的失败方式是独有的**：两张看起来对应的合约可能语义不等价（见 [[basis-risk]]），于是你建了一个**自以为是对冲、实际是两个独立头寸**的组合。

**这比不对冲更危险** —— 因为它会让你误以为可以加大规模。

## Concrete Example | 具体例子

一家进口商对冲关税风险的完整算式：

- **敞口**：若某项关税落地，年成本增加约 $2M。
- **工具**：一份"该关税在 Q4 前生效"的事件合约，现价 0.35。
- **规模**：要对冲 $2M 的损失，需买入 $2M / (1 − 0.35) ≈ **307 万份**（每份赢时净赚 0.65）。
- **成本**：307 万 × 0.35 ≈ **$107 万**。

**注意这个数字**：为了对冲 $2M 的风险，前期要付 $107 万，占用到 Q4。

**这就是全额抵押对冲的真实代价** —— 对很多企业，这笔钱的机会成本高到让对冲不值得做。**它不是需求不存在，是当前的资金效率让需求无法转化为交易**（见 [[fully-collateralized-market]]）。

## Common Misconceptions | 常见误解

- **误解一："对冲亏了就是对冲失败。"** 对冲亏钱通常意味着你原来的敞口赚钱了 —— **那正是它该有的样子。**
- **误解二："对冲要做满。"** 部分对冲往往更优：全额对冲要付全额成本，而你未必想消除全部不确定性。
- **误解三："买了反向合约就中性了。"** 只有在语义等价时才成立。**先做五维对照检查**（见 [[contract-equivalence]]）。

## In Practice | 实战里怎么用

做任何对冲前，把这四行写清楚：

```
1. 我的敞口:  事件 ______ 反向发生时损失 $______
2. 对冲工具:  合约 ______ 现价 ______
3. 语义对齐:  五维检查通过? □
4. 全成本:    权利金/占用资金 $______ , 占敞口的 ____%
```

**第 4 行超过敞口的 30%，就该重新考虑** —— 那说明市场认为这个风险很可能发生，你可能该直接调整业务而不是对冲它。

**第 3 行不通过就不是对冲**，别在风险系统里做抵扣。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 判断一次对冲成功的标准是什么？
  A: 不看赚没赚，看有没有让结果分布变窄。对冲亏钱通常意味着原有敞口赚钱了，那正是它该有的样子。
- Q: 为什么'存在真实对冲需求'对事件市场很重要？
  A: 它是事件合约被划入衍生品监管而非博彩的法律论证核心。
- Q: 事件市场对冲第二步（选工具）独有的失败方式是什么？
  A: 两张看似对应的合约语义不等价，建成了自以为是对冲、实际是两个独立头寸的组合 —— 这比不对冲更危险，因为会让人误以为可以加大规模。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 风险管理)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
