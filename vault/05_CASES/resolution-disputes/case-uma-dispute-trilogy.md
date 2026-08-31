---
id: "case:uma-dispute-trilogy"
type: case-study
title: "UMA Dispute Trilogy 2025-2026"
title_zh: UMA 裁决争议三连案
aliases: []
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
tags:
  - case-study
created: 2026-08-26
updated: 2026-08-26
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-infra-mm-stablecoins"
related:
  - "protocol:uma"
  - "concept:dispute-mechanism"
  - "concept:resolution-risk"
---

# UMA 裁决争议三连案 (2025-2026)

## The Question This Case Answers

乐观预言机的三个结构缺陷 (投票权可买 / 小盘挑战激励不足 / 语义缝隙) 在真金白银里如何逐一兑现? — 这是 [[resolution-risk]] 从概念变成实测的最佳案例组。

## Case 1 — Ukraine 矿产协议 (2025-03-25): 投票权可买

~$7M 市场 "Ukraine 是否与 Trump 签矿产协议"。单一行为人以 3 个账户投 5M UMA = 该轮 25% 投票权, 把**未发生**的事裁成 Yes; 价格 24h 内 9%→100%。Polymarket 定性 "unprecedented governance attack", **但拒绝退款** (称非 market failure)。 (CONFIRMED)

**机制教训**: DVM 的 Schelling 均衡假设投票人分散且激励对齐; 集中持币人 + 自持仓 = 均衡破产。「代币投票终裁」的安全边界 = 攻击成本 vs 可操纵市场规模 — 盘口越大, 攻击越划算。

## Case 2 — Zelenskyy 西装 (2025-07): 语义缝隙

「Zelenskyy 在 6 月底前是否穿西装」— 有着装证据情况下巨鲸投票裁 No; 争议本质是 "suit" 的语义边界 (军装式正装算不算)。受影响交易报道至 $215M 量级。 (CONFIRMED)

**机制教训**: 规则文本的语义缝隙让「技术上可辩护但违背常识」的裁决成为可能; 语义质量 ([[contract-semantics]]) 是可以在开盘前度量的风险因子。

## Case 3 — Clavicular 怀孕盘 (2026-04): 小盘挑战拉锯

主播怀孕声明市场, 终身成交 $16.46M; 两轮 proposed→disputed, UMA 终裁维持; 交易员公开抨击 oracle 是 "rogue traders" 运营的 "disinformation engine" (Forbes: "inmates taking the asylum")。 (CONFIRMED)

## What Broke / What Worked

坏: 三个缺陷全部兑现且无赔付先例 (受害者零追索 — [[resolution-insurance]] 的需求实证)。
成: 争议状态机全程链上可读 — 提议/挑战/投票每步可监控, **这也正是争议监控可以直接消费的数据**。

## Generalizable Lesson

结算风险不是尾部想象而是年度级频发事件; oracle 层因此开始分化 (价格类→Chainlink 自动化, 主观类→EigenLayer 研究)。「谁裁决」= 预测市场的核心基础设施竞争位。


## Sources

[[report-2026-08-26-infra-mm-stablecoins]] (一手: theblock.co 348171 / cryptopolitan / Forbes 2026-04-30)

<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验)。
