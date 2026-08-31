---
id: "venue:hyperliquid-hip4"
type: exchange-venue
title: Hyperliquid HIP-4
title_zh: Hyperliquid 结果市场
aliases:
  - HIP-4
  - Hyperliquid outcome markets
status: verified
importance: tier-1
domains:
  - prediction-outcome-markets
tags:
  - exchange-venue
created: 2026-08-26
updated: 2026-08-26
last_verified: 2026-08-26
review_after: 2026-11-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-prediction-venues"
related: []
---

# Hyperliquid HIP-4 | 结果市场

## Key Facts (CONFIRMED, 官方文档为主)

- Hyperliquid L1 (链上 CLOB perp DEX, 零 VC, [[jeff-yan]]) 的 outcome-market 扩展: **2026-03-10 testnet → 2026-05-02 mainnet** (validator 白名单模式)。
- 模型: 全额抵押定域结算合约 (价格 = 0-1 隐含概率), 二元 YES/NO 共享订单簿, 与 perp/spot 共用 HyperCore CLOB; **结算货币 USDH** (原生稳定币, 非 USDC)。
- 首市场 BTC daily binary: 对协议**内生 mark price** 结算 (线性插值到精确时点, 无外部 oracle)。
- 费用: 初期 0 费率; 模型 = close/settle 收、open 不收。
- **无许可化路线 (2026-07 公布, preliminary)**: 部署者质押 500k HYPE (~$30M) 锁 6 个月; 市场「定义不清 / 结算错误 / 悬置超 1 周」→ validator 投票可 slash; 部署者最高分 50% 交易费。(旧文 1M HYPE 口径已过时。)
- HIP-3 (builder 自部署 perp, OI $1.43B) 是同模式前身。


<!-- timeline -->

## Timeline

- **2026-08-26** — 建页 (web 核验, 证据见 [[report-2026-08-26-prediction-venues]])。
- **2026-08-27** — R2 补充 (CONFIRMED, 见 [[report-2026-08-26-cex-lineage]]): ① **JELLY 事件坐实** (2025-03-26): 攻击者用 spot 拉盘 + perp 空单武器化清算流打 HLP 金库 (~$12-13M 风险), validators 投票下架并按 $0.0095 强制结算 — 中心化批评的来源, 也是「validator 治理可以覆写市场」的先例; ② **USDH 发行方 = Native Markets** (2025-09-15 validator 投票胜 Paxos/Ethena/Frax); ③ HIP-3 (2025-10-13 mainnet) OI >$1.43B, trade.xyz 占 builder OI 90%+ (美股 perp); ④ 团队 ~11 人 / 年化利润 ~$900M (单源); 2026-05 Bitwise BHYP 首只美国现货 HYPE ETF (单源); ⑤ 2026 起与美国政策层互动 (Hyperliquid Policy Center, 单源)。
