---
id: "concept:implied-probability"
type: concept
title: Implied Probability
title_zh: 隐含概率
title_en: Implied Probability
aliases:
  - 隐含概率
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
  - id: "concept:price-discovery"
    rel: see-also
    note: 概率读数 = 价格发现的输出; 偏差来自费率、流动性与时间价值
prerequisites:
  - "concept:prediction-market"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Implied Probability | 隐含概率

## Executive Definition / Chinese Explanation | 定义与解释

**Implied Probability | 隐含概率** = 从合约价格反推出的、市场认为事件会发生的概率。

在全额抵押的二元合约里换算极简单：**价格 0.63 = 63%**。但"简单"不等于"准确"—— 这个等式成立需要一串前提条件，而现实中它们经常不成立。

## Why This Matters | 为什么重要

几乎所有关于预测市场的报道都建立在"价格 = 概率"这个等式上。**它成立时，预测市场是强大的信息工具；它不成立时，所有基于它的推论都是错的。**

知道这个等式什么时候会失真，是把预测市场当工具用和把它当新闻看的区别。

## How It Works | 机制怎么运转

价格与真实概率之间有四道楔子：

1. **手续费** — 买卖都要付费，价格必须偏离概率才能覆盖成本。Polymarket 自 **2026-01 结束零费率**，taker 费按品类 0.03%–0.07%，这道楔子从零变成了非零。
2. **资金占用成本** — 全额抵押意味着钱被锁到到期。**期限越长，锁仓的机会成本越高，价格就越向下偏离真实概率。** 一个"一年后某事发生"的合约，价格系统性低于真实概率。
3. **流动性溢价** — 薄盘口上你必须付出滑点，可实现价格远离中间价。
4. **裁决风险折价** — 如果市场怀疑裁决可能出错或被操纵，价格会包含一个折扣。

**所以：`价格 ≈ 概率 − 持有成本 − 裁决风险折价`。** 只有在低费用、短期限、深流动性、裁决可信时，价格才近似等于概率。

## Concrete Example | 具体例子

一个"12 个月后某事件发生"的合约报价 0.40。

- 直觉读法：市场认为 40% 概率。
- **考虑资金成本**：这 $0.40 要锁 12 个月。若无风险利率 5%，机会成本约 0.02。
- **考虑费用**：往返约 0.001。
- **考虑裁决风险**：若这类合约历史争议率不低，市场可能再打 2–3% 折扣。

**风险中性下的真实概率估计约为 0.43–0.44，而不是 0.40。**

**期限越长，这个偏差越大。** 拿长期合约的报价直接当概率引用，是这个领域最常见的错误 —— 媒体几乎每次都犯。

## Common Misconceptions | 常见误解

- **误解一："0.63 就是 63%，没什么好说的。"** 短期、低费、深流动性的合约上近似成立，其他情况都要修正。
- **误解二："多个平台价格不一样，说明有套利。"** 也可能是**合约语义不同**（判定日不同、数据源不同、边界条件不同）。**先确认两份合约真的等价，再谈套利** —— 否则那是伪套利，两边都可能输。
- **误解三："YES + NO 一定等于 1。"** 理论上是，实践中因费用和摩擦有偏离。那个偏离量本身就是衡量平台效率的好指标。

## In Practice | 实战里怎么用

把任何一个预测市场价格转成可用的概率估计，做四步修正：

```
真实概率估计 ≈ 中间价
              + 资金占用成本（无风险利率 × 剩余期限 × 价格）
              + 费用（往返 taker 费）
              + 裁决风险折价（按该平台历史争议率估）
```

并且**永远用你实际能成交的价格**（按规模逐层算），不要用屏幕上的中间价。

在跨平台比较之前，先做一次**合约语义对齐检查**：判定日、数据源、边界条件三者全部一致，才谈得上比较。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 价格与真实概率之间有哪四道楔子？
  A: 手续费、资金占用成本（期限越长越大）、流动性溢价（滑点）、裁决风险折价。
- Q: 为什么长期限合约的价格会系统性低于真实概率？
  A: 全额抵押的资金要锁到到期，机会成本随期限增加，价格必须下偏来补偿这部分成本。
- Q: 看到两个平台同一事件价格不同，第一件该做的事是什么？
  A: 确认两份合约语义是否真的等价（判定日、数据源、边界条件），否则是伪套利。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = prediction-market; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
