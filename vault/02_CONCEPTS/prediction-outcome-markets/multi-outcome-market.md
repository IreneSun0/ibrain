---
id: "concept:multi-outcome-market"
type: concept
title: Multi-Outcome Market
title_zh: 多结果市场
title_en: Multi-Outcome Market
aliases:
  - 多结果市场
status: seed
importance: tier-2
domains:
  - prediction-outcome-markets
tags:
  - concept
created: 2026-08-26
updated: 2026-08-27
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
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

## Executive Definition

同一事件下有 N 个互斥结果 (谁赢得大选: A/B/C/其他), 每个结果一个 outcome token, 全部结果的价格之和理论上 = 1。

## Chinese Explanation | 中文解释

二元市场是 N=2 的特例。多结果市场把"恰好一个结果发生"的约束编码进合约: 全额抵押下 1 份完整组合 (每个结果各一份) 恒可赎回 $1。因此**价格和偏离 1 就是套利信号** — 和高于 1 可以买入全组合锁定无风险差价 (费前), 和低于 1 反向。实际偏离常存在, 因为吃掉它要跨 N 腿成交, 各腿深度不一、手续费与 gas 磨掉利润。

结构性风险: "其他/Other" 桶的语义 (新候选人冒出来算谁的)、结果列表中途增删的规则、以及各结果盘口流动性极不均匀 (长尾结果盘口常年空)。


## Active-Recall Questions

- Q: 多结果市场价格和为什么理论上等于 1? 实际偏离为什么难吃?
  A: 全额抵押下完整组合恒赎回 $1; 偏离要跨多腿成交, 深度/费用/执行风险磨掉套利。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = outcome-market; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
