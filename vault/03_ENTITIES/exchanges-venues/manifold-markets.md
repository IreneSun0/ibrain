---
id: "venue:manifold-markets"
type: exchange-venue
title: Manifold Markets
title_zh: Manifold (玩钱市场)
aliases:
  - Manifold
status: reviewed
importance: tier-3
domains:
  - prediction-outcome-markets
tags:
  - exchange-venue
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2026-11-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-prediction-venues"
related: []
---
# Manifold Markets

## Executive Summary

玩钱（Mana）预测市场，2021-12 创立、开源，用户可以自建市场、创建者自行判定结算。

**它最有价值的地方是一次失败的实验**：2024-09 上线可兑现的 Sweepcash 模式，**2025-03-28 关停**，退回纯玩钱 —— 合规与客服开销压过了规模。

## What It Actually Is | 它到底是什么

Manifold 用 AMM（"maniswap"，Uniswap 变体）而非订单簿，这是玩钱市场的合理选择：**没有专业做市商，AMM 至少保证任何冷门市场都有报价**（见 [[automated-market-maker]]）。

它的两个设计选择在真钱市场里都不成立：

| 设计 | 玩钱下 | 真钱下会怎样 |
|---|---|---|
| **用户自建市场** | 长尾极丰富 | 语义质量不可控（见 [[contract-semantics]]） |
| **创建者自判结算** | 社区自律即可 | **利益冲突，无法接受**（见 [[resolution]]） |

**第二行是致命的**：让开盘的人来判定结果，在有真钱的情况下等于让庄家自己吹哨。

## How It Works | 运作方式

Sweepcash 实验的失败路径值得完整记下来，因为它是"玩钱转真钱"这条路的实测：

```
2024-09  上线 sweepstakes 模式 (可兑现)
         ↓ 合规义务出现: KYC、反洗钱、州法差异
         ↓ 客服开销出现: 争议、退款、身份核验
2025-03  关停, 退回 Mana-only
```

**教训**：真钱不是给玩钱产品加一个提现按钮。它带来的是一整套 [[know-your-customer|KYC]]、[[anti-money-laundering|AML]]、争议处理与州级合规负担 —— 而这些的固定成本，小平台摊不动（见 [[capital-requirements]]）。

## Position in the Market | 它在市场里的位置

在事件市场版图里，Manifold 占据**低风险实验区**：无监管压力、极长尾、社区驱动。

它的真实用途有两个：
1. **预测能力的测试场** —— 无金钱激励下的校准数据；
2. **产品创意的试验田** —— 新市场类型可以零成本上线。

**但它对"预测市场能不能成为金融基础设施"这个问题不提供证据** —— 玩钱市场没有 [[adverse-selection|逆向选择]] 的经济后果，因此它的价格质量不能外推到真钱市场。

## What Could Break It | 什么会让它出问题

- **玩钱市场的价格不可外推** —— 没有真实损失，就没有真正的纠错压力。
- **创建者自判结算** —— 在任何有价值的场景下都不成立。
- **可持续性依赖资助** —— 无交易收入。

## What To Watch | 该盯什么

- **是否再次尝试真钱路径** —— 若尝试，看它这次怎么解决结算的利益冲突。
- **其校准数据是否被用于对照真钱市场** —— 那是它最有学术价值的输出。
