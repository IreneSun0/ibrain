---
id: "concept:exchange-vertical-integration"
type: concept
title: Exchange Vertical Integration
title_zh: 交易所纵向一体化
title_en: Exchange Vertical Integration
aliases:
  - 纵向一体化
status: seed
importance: tier-2
domains:
  - crypto-market-structure
  - industry-strategy
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
  - id: "venue:binance"
    rel: instantiated-by
    note: 撮合+托管+钱包+BNB Chain+平台币+launchpad 全栈
  - id: "concept:distribution"
    rel: see-also
    note: 垂直整合的战略目的 = 把用户资金生命周期每一环收进自己的分发栈
prerequisites:
  - "concept:centralized-exchange"
---
# Exchange Vertical Integration | 交易所纵向一体化

## Executive Definition

头部 crypto 交易所同时拥有: 交易撮合 + 托管 + 钱包 + 自有公链 + 平台币 + 发行平台 (launchpad) + 支付/卡 — 把用户资金生命周期的每一环都收进自己的栈。

## Chinese Explanation | 中文解释

传统金融里交易、清算、托管、经纪被监管强制分离; crypto 交易所则天然长成了全栈: Binance 有 BNB Chain + BNB + 钱包; OKX 有 X Layer + OKB + OKX Wallet; Bitget 有 Morph 关联 + BGB + Bitget Wallet; Bybit 与 Mantle 生态关联。动机: ① 手续费之外的第二增长曲线; ② 用户资金留在自家生态内循环 (提现也提到自家链); ③ 平台币积分/燃烧绑定用户忠诚; ④ 分发入口 (钱包) 控制下一代应用的流量税。

风险面: 利益冲突 (上币定价 vs 自营)、监管对混业的清算 (FTX 之后各辖区盯 custody 分离)、以及"链上模式反噬" — Hyperliquid 用链本身当交易所, 把一体化做到了更彻底的形态。


## Active-Recall Questions

- Q: 交易所做自有链的三个动机?
  A: 第二收入曲线、资金生态内循环、控制钱包分发入口。

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = centralized-exchange; typed 关系 2 条。词表见 [[relationship-types|关系类型受控词表]]。
