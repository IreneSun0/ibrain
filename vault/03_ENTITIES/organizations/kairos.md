---
id: "org:kairos"
type: organization
title: Kairos (kairos.trade)
title_zh: Kairos 预测市场终端
aliases:
  - kairos.trade
  - kairoslive
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
tags:
  - organization
  - competitor
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2026-11-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-27-pm-data-vendors"
related:
  - id: "venue:kalshi"
    rel: integrates-with
    note: canonical 跨场馆 ID + 实盘路由覆盖
  - id: "venue:polymarket"
    rel: integrates-with
    note: 同上
  - id: "venue:predict-fun"
    rel: integrates-with
    note: 同上
  - id: "venue:hyperliquid-hip4"
    rel: integrates-with
    note: Tier B 中少数覆盖 HIP-4 的供应商
---

# Kairos (kairos.trade)

> ⚠ **认域名**: 「Kairos」撞名极多 (Kairos Power 核电 / Kairos 人脸识别 / 多个同名 crypto 基金 / GitHub 上一个同名开源 Polymarket 策略引擎)。本页只指 **kairos.trade / kairoslive.com** — a16z crypto 投的预测市场交易终端。法律实体名未公开。

## Executive Summary

Tier B 里**唯一同时具备 canonical 跨场馆 ID + 实盘路由**的供应商, 覆盖场馆最全 (Kalshi / Polymarket / Predict.fun / **Hyperliquid**)。团队来自 Cboe (交易所技术+量化), 2026-02 拿 a16z crypto 领投的 **$2.5M seed**, 2026-06-26 公开上线 — **入市仅两个月**。

## Key Facts (CONFIRMED)

- **融资**: $2.5M seed, a16z crypto 领投, Geneva Trading / University of Illinois / @tier10k + 20 余名天使跟投, 2026-02-03 公布。(双源: a16zcrypto.com + Fortune)
- **创始人**: Jay Malavia (Cboe 量化研究, 含早期预测市场项目; Geneva Trading 数据科学; NASA ML) · Zayd Alzein (Cboe 低延迟数据流与订单簿重建; Solana 交易平台执行基础设施)。公布时**团队仅两位联创**。
- **canonical ID (一手原话)**: 「Cross-venue matching and identifier resolution mean the same event is addressable through **one canonical Kairos market id on every venue**.」
- **执行**: `POST /orders` + **NBBO 路由** (「order sent to the NBBO endpoint routes to whichever venue is actually showing that price」) + **EIP-712 外部签名通道** (机构账户可非托管签名) + 费用预估端点。
- **结算原语**: CTF split (mint YES/NO 各 $0.50) / CTF merge / 程序化 redeem / NegRisk 自动 unwrap。
- **机构化配置**: scoped API key (`trade:execute` / `trade:read` / `position:read`) + IP 白名单。无公开 SOC2/审计背书。
- **定价**: 企业 API **按量报价不公开** (原话: 按 credential、场馆组合、taker/maker 定价)。
- **规模**: 无公开用户/成交数字。「比原生界面快 2-3 秒」为一手营销未验。


## Open Questions

法律实体与注册地? 私测客户是谁? 两人团队如何维持四场馆覆盖 (是否有未披露的上游供应商)?

<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (一手 docs 核验, 证据见 [[report-2026-08-27-pm-data-vendors]])。
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 4 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
