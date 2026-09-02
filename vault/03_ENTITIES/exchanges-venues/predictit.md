---
id: "venue:predictit"
type: exchange-venue
title: PredictIt
title_zh: PredictIt
aliases:
  []
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
related:
  - id: "regulator:cftc"
    rel: regulated-by
    note: 长期以 CFTC no-action 状态运行的学术性市场
---
# PredictIt

## Executive Summary

美国最早具备规模的政治预测市场，长期以 **CFTC no-action 状态**运行的学术性市场，由新西兰惠灵顿维多利亚大学发起。

**它的历史意义大于当下体量**：在 [[kalshi]] 打赢监管官司之前，PredictIt 是"美国到底能不能合法交易事件合约"这个问题唯一的活体样本。

## What It Actually Is | 它到底是什么

PredictIt 与今天的持牌场馆有三个根本差别，每一个都塑造了它的形态：

| | PredictIt | 持牌 DCM |
|---|---|---|
| 法律地位 | **no-action letter**（监管容忍，非许可） | 正式牌照 |
| 单市场参与人数 | **有上限** | 无 |
| 单人持仓 | **有金额上限** | 无（受风控约束） |
| 手续费 | 对**盈利**抽成 + 提现费 | 按成交额 |

**"对盈利抽成"是一个很少见的费率结构**，它意味着套利与做市的净收益被系统性削薄 —— 这直接解释了它的价差为什么长期偏宽（见 [[spread]]）。

**上限也不是缺陷而是条件**：no-action 状态换来的正是"规模不得过大"。

## How It Works | 运作方式

它的存在方式本身就是一堂监管课：

```
no-action letter = 监管说"我暂时不追究"
                 ≠ 监管说"这是合法的"
```

这个身份**随时可以被撤回**，而事实上 CFTC 曾一度撤销其 no-action 状态并引发诉讼。

**对比 [[kalshi]] 的路径差异是这个行业最重要的分岔**：
- PredictIt 走"被容忍"，规模受限、随时可被叫停；
- Kalshi 走"拿牌照 + 打官司"，代价高但地位稳固（见 [[regulatory-access]]）。

**后者赢了，也定义了这个行业此后的路。**

## Position in the Market | 它在市场里的位置

在今天的格局里，PredictIt 更多是**参照系**而非竞争者：体量远小于 Polymarket 与 Kalshi，但它的数据序列跨越多个美国选举周期，是研究预测市场准确性最常被引用的样本之一。

**它证明了两件事**：一是政治事件市场有真实需求；二是**规模上限会直接扼杀流动性质量** —— 上限让专业资金无法进场，价差因此长期宽于同期的无上限场馆（见 [[liquidity]]）。

## What Could Break It | 什么会让它出问题

- **监管地位不稳** —— no-action 可撤回，这是它的结构性风险，不是尾部风险。
- **规模上限锁死流动性** —— 无法吸引专业做市（见 [[market-maker-incentive]]）。
- **费率结构不利套利** —— 对盈利抽成削弱了价格纠错的动力。

## What To Watch | 该盯什么

- **no-action 状态的任何变动。**
- **它的历史价格数据是否被持续用于学术校准** —— 那是它长期价值的所在。
- **是否转向正式牌照** —— 若转，说明"被容忍"这条路已经彻底关闭。
