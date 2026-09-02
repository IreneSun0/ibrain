---
id: "org:metaculus"
type: organization
title: Metaculus
title_zh: Metaculus (预测聚合平台)
aliases: []
status: reviewed
importance: tier-3
domains:
  - prediction-outcome-markets
tags:
  - organization
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-prediction-venues"
related: []
---
# Metaculus

## Executive Summary

**不是市场，是声誉制预测征集平台** —— 没有真钱，用积分与社区聚合算法产生预测，由平台行政判定结果。2015 年创立，公益性质法人。

Metaculus 提供了一个非金钱激励的对照样本，可用于比较声誉激励与交易激励下的预测表现。

## What It Actually Is | 它到底是什么

Metaculus 与预测市场的机制差别，决定了它们各自的强项：

| | 预测市场 | Metaculus |
|---|---|---|
| 激励 | 金钱 | 声誉/积分 |
| 聚合方式 | 价格（见 [[price-discovery]]） | 加权算法 |
| 谁能参与 | 有钱就行 | 有时间就行 |
| 长期限问题 | **资金占用成本压价**（见 [[implied-probability]]） | **不受影响** |
| 抗操纵 | 靠资本成本 | 靠声誉与算法 |

**倒数第二行是它的结构性优势**：一个"十年后某事是否发生"的问题，在预测市场里会因为资金占用而系统性低估，在 Metaculus 上不会。

## How It Works | 运作方式

它的聚合不是简单平均：按预测者的历史表现加权，并随时间更新。这让它能在**没有金钱信号**的情况下仍产生有区分度的预测。

2024–2026 年的主线是 **AI 预测的基准化**：持续对比 AI 与人类预测者的表现，并设有专门的 bot 锦标赛。

**这条线值得关注的原因**：如果 AI 预测者在校准上稳定超过人类，那么"谁在预测市场里提供信息"这个问题的答案会改变 —— 而 [[adverse-selection|逆向选择]] 的形态会随之改变。

## Position in the Market | 它在市场里的位置

Metaculus 在这个领域的位置是**校准基准**，不是竞争者。

它的价值在于回答一个预测市场自己回答不了的问题：**某个概率估计到底准不准？** 市场只给你价格，不给你校准记录；Metaculus 的整套设计就是为了产生可审计的校准历史。

**所以它是评估"预测市场是否真的更准"时最常被用到的对照组。**

## What Could Break It | 什么会让它出问题

- **无金钱激励** —— 参与者没有承担错误的成本，可能降低认真程度。
- **依赖资助** —— 非商业模式，可持续性取决于捐助。
- **人群偏差** —— 参与者高度自选择，未必代表更广泛的判断。

## What To Watch | 该盯什么

- **AI vs 人类的校准对比结果** —— 这是当前最有信息量的输出。
- **其历史校准数据是否被用于评价真钱市场。**
- **是否与持牌场馆建立数据合作** —— 校准基准 + 真钱市场是一个自然的组合。
