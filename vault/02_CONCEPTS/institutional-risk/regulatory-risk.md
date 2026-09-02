---
id: "concept:regulatory-risk"
type: concept
title: Regulatory Risk
title_zh: 监管风险
title_en: Regulatory Risk
aliases:
  - 监管风险
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
  - id: "concept:regulatory-access"
    rel: mitigated-by
    note: "持牌是一级缓解, 但牌照本身可变可撤"
prerequisites:
  - "concept:jurisdiction"
import_origin: xlsx-learning-map+manual
import_category: 机构风险
---
# Regulatory Risk | 监管风险

## Executive Definition / Chinese Explanation | 定义与解释

**Regulatory Risk | 监管风险** = 规则本身改变，从而改变你的业务能不能做、成本多高、甚至已成交的交易还算不算数的风险。

它和其他风险有一个本质区别：**它不服从任何统计规律。** 你无法从历史数据推断下一个规则变化，因为它由少数人的决定产生，而不是由市场过程产生。

## Why This Matters | 为什么重要

对事件市场，监管风险不是外部变量，**它就是市场结构本身**。

这个行业的形态在过去两年主要由监管动作塑造，而不是由技术或需求塑造：CFTC 从"禁止路线"转向"逐案公共利益认定 + 保证金化探索"、选举合约的合法性经法院落定、州与联邦的管辖权之争、首例预测市场内幕交易执法。

**每一步规则动作都直接改写市场结构** —— 谁能开业、能上什么合约、用户从哪来。

## How It Works | 机制怎么运转

监管风险有四种形态，影响面依次扩大：

1. **准入变化** —— 牌照要求变了，你还能不能做。
2. **产品变化** —— 某类合约被禁或被要求改条款。
3. **运营变化** —— KYC / 报告 / 资本要求提高，成本上升。
4. **溯及力** —— **最严重的一种：已成交的交易被要求取消或强制平仓。**

第 4 种在传统金融中罕见，但在这个赛道已经出现：CFTC 曾使用紧急权力阻止州政府强制取消已成交交易。**"我的头寸会不会因为规则变化而被强制作废"，在这里是一个真实的问题。**

## Concrete Example | 具体例子

**监管态度的转向如何直接改变商业模型**：

[[polymarket]] 的路径就是一条监管风险曲线：
- 2022：CFTC 罚款 $1.4M，退出美国市场
- 2024-11：FBI 搜查创始人住所
- 2025-07：DOJ 与 CFTC 双双撤案不起诉
- 2025-07：以 $112M 收购 QCEX 取得牌照
- 2025-11：获得 Amended Order of Designation

**三年之内，同一个业务从"被执法对象"变成"持牌经营者"** —— 而这中间公司的产品几乎没变，变的是规则和执法态度。

**这就是监管风险的形状：它不是渐变，是状态切换。**

## Common Misconceptions | 常见误解

- **误解一："监管风险可以用概率建模。"** 它由少数人的决定产生，历史频率对它几乎无预测力。**能做的是情景分析，不是概率分布。**
- **误解二："合规了就没有监管风险。"** 合规针对现行规则。规则改变时，合规状态本身可能失效。
- **误解三："监管只会越来越严。"** 也可能放松（CFTC 近年的转向就是例子）。**方向不确定性本身就是风险。**

## In Practice | 实战里怎么用

管理监管风险靠情景，不靠模型：

1. **列出 2–3 个可能的规则变化情景**（收紧 / 放松 / 管辖权重划）。
2. **对每个情景问"我的头寸和业务会怎样"** —— 特别问第 4 种形态：**已成交交易会不会被作废。**
3. **识别单点依赖** —— 你的全部业务是否依赖一个法域、一张牌照、一条监管解释？
4. **跟踪先行指标** —— 规则征询（ANPRM/comment）、诉讼进展、执法案例。**这些通常比正式规则早 6–18 个月出现。**

**第 4 条是最实用的**：公开的规则征询文件里，谁提交了意见、说了什么，往往能提前很久看出行业结构的走向。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 监管风险与其他风险的本质区别是什么？
  A: 它不服从统计规律 —— 由少数人的决定产生而非市场过程产生，历史数据对它几乎无预测力，只能做情景分析。
- Q: 监管风险的四种形态里，哪一种最严重、为什么？
  A: 溯及力 —— 已成交交易被要求取消或强制平仓。它让'我已经建好的头寸'本身变得不确定，传统金融中罕见。
- Q: 追踪监管风险最实用的先行指标是什么？
  A: 规则征询文件（谁提交意见、说了什么）、诉讼进展、执法案例 —— 通常比正式规则早 6-18 个月出现。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
