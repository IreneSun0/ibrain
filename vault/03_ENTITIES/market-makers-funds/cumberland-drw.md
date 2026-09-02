---
id: "mmf:cumberland-drw"
type: market-maker-fund
title: Cumberland / DRW
title_zh: Cumberland (DRW)
aliases:
  - Cumberland
  - DRW
status: reviewed
importance: tier-1
domains:
  - crypto-market-structure
  - prediction-outcome-markets
tags:
  - market-maker-fund
created: 2026-08-26
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related:
  - id: "venue:polymarket"
    rel: provides-liquidity-to
    note: "报道级 (2026-06 CoinDesk): DRW 被点名建 dedicated desk; 做市协议条款未披露"
  - id: "venue:kalshi"
    rel: provides-liquidity-to
    note: "报道级 (2026-06 CoinDesk): 同上"
---
# Cumberland / DRW

## Executive Summary

芝加哥自营交易集团 DRW（Don Wilson 1992 年创立）的加密流动性部门，2014 年成立，7×24 做市。

**它是目前最值得盯的一条线索**：2026-06 有报道点名 DRW 在 [[polymarket]] 与 [[kalshi]] 建立专门的做市台（报道级，做市协议条款未披露）。**这是第一家被公开指认进入事件市场的顶级传统自营机构。**

## What It Actually Is | 它到底是什么

DRW 的背景决定了它为什么会是第一批：Don Wilson 出身芝加哥期权与事件类衍生品结构，**对离散支付的定价是这家公司的本行**（见 [[binary-option]]）。

与 [[jane-street]] 的对照很能说明问题：

| | Jane Street | Cumberland / DRW |
|---|---|---|
| 离散支付定价能力 | 强 | 强 |
| 加密经验 | 有（ETF AP） | **深，做了十余年** |
| 事件市场动作 | **无公开记录** | **被报道已建台** |

**同样有能力，动作不同** —— 差别通常在风险偏好与监管容忍度上，而不在技术。

## How It Works | 运作方式

做市台建立的意义不只是多一个报价方，它改变了市场的**可承载规模**：

专业自营台带来的是自有资本、跨市场对冲能力、以及在压力时刻仍然报价的意愿（见 [[inventory-risk]]）。

**但要注意报道的边界**：公开信息是"建了台"，**做市协议条款、返佣安排、是否负有做市义务，三项都未披露**。有台不等于有承诺 —— 无义务的做市台可以在任何时刻撤出。

## Position in the Market | 它在市场里的位置

在事件市场的做市商版图上，目前的公开格局：

| 场馆 | 已知做市方 |
|---|---|
| [[kalshi]] | [[susquehanna]]（旗舰）、自有子公司、[[wintermute]] |
| [[polymarket]] | [[wintermute]] |
| 两者 | **Cumberland / DRW（报道级）** |

**DRW 同时出现在两侧，是唯一一家** —— 若属实，它就是第一个真正跨场馆做市的机构，而跨场馆做市的前提是能对冲（见 [[contract-equivalence]]）。

**这条线索之所以重要，正是因为它暗示对冲问题被某种方式解决了 —— 或者被承担了。**

## What Could Break It | 什么会让它出问题

- **报道级信息** —— 协议条款未披露，引用时必须标明。
- **监管历史** —— 该集团曾有 SEC 未注册交易商指控（2025-03 SEC 同意撤诉，理由是监管路径重塑，非案情）。
- **无义务的做市可随时撤出** —— 尤其在裁决临近时（见 [[market-maker-incentive]]）。

## What To Watch | 该盯什么

- **是否有任何一方确认做市协议** —— 从报道级升到 CONFIRMED，这条信息的价值会大幅上升。
- **它是否只做头部合约** —— 长尾是否被覆盖，决定这个市场的深度结构（见 [[liquidity]]）。
- **其他顶级自营是否跟进** —— DRW 通常是同类机构的先行指标。
