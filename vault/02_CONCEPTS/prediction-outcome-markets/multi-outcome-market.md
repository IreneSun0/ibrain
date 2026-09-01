---
id: "concept:multi-outcome-market"
type: concept
title: Multi-Outcome Market
title_zh: 多结果市场
title_en: Multi-Outcome Market
aliases:
  - 多结果市场
status: reviewed
importance: tier-2
domains:
  - prediction-outcome-markets
tags:
  - concept
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related:
  - id: "concept:outcome-market"
    rel: special-case-of
    note: "N 个互斥结果, 每结果一个 outcome token"
  - id: "concept:implied-probability"
    rel: see-also
    note: "全部结果价格之和理论 = 1, 偏离即套利空间或费率痕迹"
prerequisites:
  - "concept:outcome-market"
---
# Multi-Outcome Market | 多结果市场

## Executive Definition / Chinese Explanation | 定义与解释

**Multi-Outcome Market | 多结果市场** = 一个事件有三个以上互斥结果的市场（"谁会当选" 而不是 "X 会不会当选"）。

它不是二元市场的简单推广：**结果数从 2 变成 N，流动性被切成 N 份，而定价约束从一条变成一组。**

## Why This Matters | 为什么重要

绝大多数真实世界的问题天生是多结果的（谁当选、降息多少个基点、什么时候完成）。把它们硬塞成一系列二元合约，会产生两个真实问题：

- **流动性碎片化** —— 同一个事件的资金被分散到 N 个盘口，每个都更薄。
- **定价不一致** —— N 个独立盘口的价格之和可能不等于 1，产生套利空间，也让"价格即概率"的读法失效。

**这是事件市场规模化时最先撞上的结构性墙。**

## How It Works | 机制怎么运转

多结果市场的核心约束是：**所有互斥且穷尽的结果，价格之和必须等于 1。**

维持这个约束有两条路：

1. **完备集铸造（complete set）** —— 存 $1 铸出全部 N 个结果各一份；集齐全套可赎回 $1。套利者据此把价格和钉向 1。
2. **统一做市（如 LMSR 类自动做市商）** —— 用一个成本函数在整个结果空间上同时定价，数学上保证价格和恒等于 1。

**还必须处理三种边界情形，否则就是漏洞**：
- **"以上皆非"** —— 结果集是否穷尽？漏了怎么办？
- **并列 / 部分满足** —— 两个结果同时成立时怎么分？
- **事件取消或延期** —— 全部退款还是按某个规则结算？

第三条恰恰属于 [[settlement-methodology]] 的第二层（价格规则），而它在多结果盘上最容易被写含糊。

## Concrete Example | 具体例子

一个"谁会赢得某选举"的四选一市场：

```
候选人 A   0.45
候选人 B   0.38
候选人 C   0.12
其他/无人  0.03
────────────────
合计       0.98   ← 少了 0.02
```

**这 0.02 是什么？** 三种可能，含义完全不同：

- **套利机会** —— 买齐四份成本 $0.98，必得 $1，锁定 2% 无风险收益（若流动性足够）。
- **摩擦成本** —— 费用与资金占用让套利不划算，价格就停在这里。
- **结算不确定性折价** —— 市场怀疑"其他/无人"的定义有漏洞，宁可不碰。

**分不清是哪一种，就不该下这笔单。** 这三种情况的正确应对完全相反。

## Common Misconceptions | 常见误解

- **误解一："多结果市场 = 几个二元市场放一起。"** 少了完备集或统一做市，价格约束就不成立，套利与不一致会持续存在。
- **误解二："价格之和不等于 1 一定是套利。"** 也可能是摩擦或结算不确定性折价。**先分清是哪一种。**
- **误解三："结果集总是穷尽的。"** "以上皆非"是最常被漏掉的一项，也是争议高发区。

## In Practice | 实战里怎么用

看一个多结果盘，四步：

1. **算价格和** —— 偏离 1 多少？
2. **判断偏离来源** —— 套利 / 摩擦 / 折价？看流动性和费用能不能覆盖偏离。
3. **检查结果集是否穷尽** —— 有没有"以上皆非"？它的定义清楚吗？
4. **检查边界条款** —— 并列、取消、延期各自怎么结算？

**第 3、4 步就是这类盘口的主要风险来源**，而它们完全写在合约文本里，开盘前就能读到。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 多结果市场的核心定价约束是什么？靠什么维持？
  A: 所有互斥且穷尽的结果价格之和必须等于 1；靠完备集铸造赎回的套利，或统一做市（如 LMSR 类成本函数）维持。
- Q: 价格之和不等于 1 的三种可能解释是什么？
  A: 套利机会、摩擦成本（费用与资金占用使套利不划算）、结算不确定性折价。三者的正确应对完全不同。
- Q: 多结果盘最常被漏掉的条款是什么？
  A: '以上皆非'（结果集是否穷尽）以及并列/取消/延期的结算规则。


## Sources

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = outcome-market; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
