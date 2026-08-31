---
id: "concept:scalar-market"
type: concept
title: Scalar Market
title_zh: 标量市场
title_en: Scalar Market
aliases:
  - 标量市场
  - Range Market
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
    note: "结算值为连续数值, 支付线性映射"
  - id: "concept:binary-option"
    rel: contrasts-with
    note: 连续线性支付 vs 0/1 支付
prerequisites:
  - "concept:outcome-market"
---
# Scalar Market | 标量市场

## Executive Definition

结算值是一个连续数值 (CPI 读数、得票率、某日 BTC 价格) 而非 YES/NO 的结果市场; 支付按结算值在约定区间内线性 (或分段) 映射。

## Chinese Explanation | 中文解释

二元市场只回答"过没过线"; 标量市场回答"落在哪里"。典型实现: 定义区间 [下限, 上限], long token 支付 = (结算值 − 下限)/(上限 − 下限), 封顶封底。这让市场直接交易**期望值**而不只是概率, 信息含量更高。

实践里更常见的替代形态是"桶化": 把连续变量切成一串区间型二元市场 (CPI 在 2.9-3.1%? 3.1-3.3%?) — 本质是离散化的 scalar, 组合起来读出整条隐含分布。

风险点: 区间设计错 (真实值贴边或出界, 市场退化成二元)、结算源的精度与修订 (官方数据初值 vs 修正值用哪个 — 语义必须钉死)。


## Active-Recall Questions

- Q: 桶化二元市场群和真 scalar 市场的关系?
  A: 桶化是离散化的 scalar; 读全部桶价可重构隐含分布, 但跨桶流动性割裂。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = outcome-market; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
