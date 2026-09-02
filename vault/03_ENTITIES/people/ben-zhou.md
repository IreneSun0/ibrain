---
id: "person:ben-zhou"
type: person
title: Ben Zhou
title_zh: 周本
aliases:
  []
status: reviewed
importance: tier-2
domains:
  - people-networks
  - crypto-market-structure
tags:
  - person
created: 2026-08-27
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-cex-lineage"
related:
  - id: "venue:bybit"
    rel: co-founded
    note: 2018 年创立 Bybit
  - id: "venue:bybit"
    rel: executive-of
    note: 现任 CEO; 2025-02 $1.5B 被盗案的危机应对者
---
# Ben Zhou

## Executive Summary

[[bybit]] 联合创始人兼 CEO（2018 年创立）。

2025-02-21 Bybit 被盗约 15 亿美元；官方归因于国家级黑客组织。此后 72 小时内，多家机构协助补足储备，平台持续公开进展。该事件可用于分析[[operational-risk|操作风险]]中的披露、流动性与外部支持。

## What It Actually Is | 它到底是什么

这次事件之所以值得单独记录，是因为它**把操作风险的应对拆解得很清楚**：

| 环节 | 做对了什么 |
|---|---|
| 披露 | **立即公开、持续更新**，而非拖延 |
| 流动性 | 72 小时内经 [[falconx]]、[[wintermute]] 等补足 |
| 储备 | 事前有可验证的储备水平 |
| 结果 | **未发生挤兑破产** |

**关键教训在第三行**：应对能力来自事前准备，不是事后反应。**没有事前的储备透明与机构关系，72 小时是不够的。**

**反面推论同样重要**：如果没有那几家愿意出手的机构，结果会完全不同 —— 这说明危机中的救援依赖关系网络，而关系网络是长期资产。

## How It Works | 运作方式

交易所的操作风险有一个结构性特征：**它不随规模自动下降。**

规模越大，被攻击的价值越高；而托管、密钥管理、内部权限的复杂度也随规模上升（见 [[custody]]）。

**对事件市场的直接含义**：链上全额抵押把托管风险从平台转移到了合约（见 [[fully-collateralized-market]]）—— 这是它相对中心化交易所被低估的优势。

## Position in the Market | 它在市场里的位置

在人物图谱里，Ben Zhou 代表的是**危机处理这条线**，而不是产品或监管创新。

Bybit 截至 2026-08 **没有公开的事件市场业务**，但其生态代币所在的 L2（见 [[mantle]]）与其生态孵化历史，使它具备进入这个品类的条件。

## What Could Break It | 什么会让它出问题

- **持续的安全暴露** —— 大型中心化托管的固有风险。
- **地缘与制裁环境** —— 攻击归因涉及国家级行为体。
- **动态职务** —— 需带 last_verified。

## What To Watch | 该盯什么

- **Bybit 是否进入预测市场品类。**
- **储备证明的持续披露质量** —— 这次危机中它起了决定作用。
