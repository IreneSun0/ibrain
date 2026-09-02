---
id: "protocol:uma"
type: protocol-network
title: UMA
title_zh: UMA (乐观预言机)
aliases:
  - Universal Market Access
  - UMA Protocol
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
  - blockchain
tags:
  - protocol-network
created: 2026-08-26
updated: 2026-08-26
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related: []
---

# UMA | 乐观预言机

## Executive Summary

Polymarket 的主裁决层: optimistic oracle + UMA 代币持有人投票终裁 (DVM)。2025-2026 三连争议实证了乐观预言机的结构缺陷 (投票权可买/挑战激励不足/语义缝隙), 导致 Polymarket 把价格类市场结算移交 Chainlink —— 结算情报领域的头号观测标的。

## Mechanism (CONFIRMED)

Risk Labs 开发, 2018 年由前 Goldman 交易员 Hart Lambur 与 Allison Lu 创立。流程: proposer 押 $750 USDC bond 提结果 → 2 小时挑战窗 → 无争议即结算 (通常 2-4 小时); 有争议 → UMA 持币人 DVM 投票终裁 (Schelling point 激励)。Lambur 声明团队禁止在 Polymarket 交易、本人不投票 (利益回避)。

## 2025-2026 三连争议 (CONFIRMED; 详见 [[case-uma-dispute-trilogy]])

1. **2025-03-25 Ukraine 矿产协议** (~$7M): 单一行为人 3 账户投 5M UMA (该轮 25% 投票权) 把未发生的事裁成 Yes; Polymarket 定性 "unprecedented governance attack" 但拒绝退款。
2. **2025-07 Zelenskyy 西装**: 巨鲸投票裁 No (有着装证据情况下); 受影响交易量级报道至 $215M。
3. **2026-04 Clavicular 怀孕盘** ($16.46M): 两轮 proposed→disputed 后维持; Forbes 以 "inmates taking the asylum" 报道。

## 结构性回应 (CONFIRMED)

- 2025-02: EigenLayer × Polymarket × UMA 研究 next-gen oracle (restaking + "intersubjective truth")。
- 2025-09: Polymarket 价格类市场移交 [[chainlink]] (Data Streams + Automation, 降低人为裁决面)。


## Sources

[[report-2026-08-26-infra-mm-stablecoins]] (一手: docs.polymarket.com / theblock / Forbes / blog.uma.xyz)
