---
id: "deck:exercises-stage-2"
type: flashcard-deck
title: Exercises Stage 2 Exchanges
title_zh: 练习题 · Stage 2 交易所
aliases: []
status: seed
importance: tier-1
domains:
  - learning
  - exchanges
tags:
  - exercises
  - bootcamp
created: 2026-08-27
updated: 2026-08-27
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related: []
---

# 练习题 · Stage 2 交易所 (v1, 2026-08-27)

## Q1 [忆] exchange 的本质
交易所到底卖什么? 为什么说「交易所通常不是你交易的对手方」? 那谁是?
> **参考**: 交易所卖的是规则+撮合+准入+行情 (市场基础设施), 不是资产本身。你的对手方是另一侧的交易者 (或做市商); 成交后在成熟市场里 CCP 介入成为法律对手方。
> **给分点**: 基础设施定位 0.5; 对手方链条 (交易者→CCP) 0.5。

## Q2 [忆] 四件套
给任一 venue 做尽调的四件套是什么? 每件用一个问题表述。
> **参考**: ① 市场模型 — 怎么撮合定价 (CLOB/AMM/RFQ)? ② 托管 — 钱和资产在谁手里, 谁能冻结? ③ 结算 — 赢了怎么真正拿到钱, 走哪条轨, 多快? ④ 监管 — 谁发的牌照, 覆盖谁, 出事找谁?
> **给分点**: 四件各 0.25。这是 Stage 2 完成判据的骨架。

## Q3 [判] Kalshi vs Polymarket 四件套 (curriculum 原题)
用四件套对比 Kalshi 与 Polymarket (美国合规实体): 谁托管、谁是最终对手方、谁能冻结、监管归谁。
> **参考**: Kalshi — CFTC DCM + 自有 DCO (Kalshi Klear): 法币入金托管在受监管清算体系, CCP 是对手方, 监管冻结路径经 CFTC/法院; Polymarket — hybrid: 链下 CLOB 撮合 + Polygon 链上 USDC 全额抵押结算 (ERC-1155 outcome token), 托管在智能合约 (自托管钱包持仓), 对手方是合约池/对侧持仓者, 冻结面在合约权限与美国实体 (QCX DCM/QC Clearing) 的合规层。
> **给分点**: 每平台四件各 0.125。答不出说明 Stage 2+5 还没通, 记回炉。

## Q4 [忆] CEX vs DEX 一刀
中心化与去中心化交易所的**一刀切分标准**是什么? (不是「有没有公司」)
> **参考**: 资产托管与结算发生在哪 — CEX: 内部账本记账、平台托管、提现才上链; DEX: 链上合约结算、用户自托管、成交即链上状态变更。
> **给分点**: 托管+结算位置 1.0; 答「有没有中介」这类模糊标准 ≤0.3。

## Q5 [判] 谁能冻结
三个场景各答「谁能冻结你的钱」: ① Binance 现货账户; ② Polymarket (Polygon USDC 持仓); ③ Kalshi 账户。
> **参考**: ① Binance 平台自身 (内部账本) + 其接受的执法辖区; ② 没有平台单方冻结你钱包的通道, 但 USDC 发行方 Circle 可以冻结地址上的 USDC, 合约权限内的暂停是另一层; ③ Kalshi/清算体系依监管指令。
> **给分点**: 每场景 0.33; ② 里说出「Circle 能冻 USDC」是关键分。

## Q6 [忆] 垂直整合栈
默写头部 CEX 垂直整合的典型栈 (至少 5 环), 并指出其中一个内生利益冲突。
> **参考**: 撮合 + 托管 + 钱包 + 自有公链 + 平台币 + launchpad + 支付/卡。冲突例: 既当 venue 又当托管方 (FTX 教训 — 客户资产与自营边界); 平台币做保证金 (自我抵押的反身性); launchpad 上币与撮合方的利益一致性。
> **给分点**: 栈 ≥5 环 0.6; 冲突说清一个 0.4。(关系考察: exchange-vertical-integration instantiated-by binance)

## Q7 [忆] 飞轮
订单流网络效应的链条是什么? 它解释了什么行业现象?
> **参考**: 更多用户 → 更多订单流 → 吸引做市商 → 更深流动性 → 更好价格 → 再吸引用户。解释: 交易所赢家通吃/头部集中, 以及新 venue 冷启动必须买流动性 (做市激励)。
> **给分点**: 链条完整 0.6; 现象连接 0.4。

## Q8 [英] Venue-neutral, 60 秒
用英语说出「场所中立的数据层」的三个理由 (curriculum 实战应用题, 英文版)。
> **参考骨架**: "First, institutions don't live on one venue — their event exposure is scattered across Kalshi, Polymarket and whatever launches next quarter, so risk tooling has to aggregate. Second, a venue can't neutrally referee markets it profits from — surveillance and risk assessment need to sit outside the exchange stack. Third, neutrality is what makes market makers and funds willing to share data with us — we don't compete with their execution."
> **给分点**: 三理由各 0.3, 流畅 0.1。

## Q9 [话] custody 追问
机构风控问: "你们读链上数据, 那你们碰客户资产吗? 你们的数据供应商能挪用什么?" 回答, 并主动区分 custody / data access 两层。
> **参考骨架**: 中立数据层不托管任何客户资产 (read-only, 链上公开状态 + venue API 只读授权); 数据访问权 ≠ 资产控制权 — 没有私钥、没有提现权限。风险面在数据完整性 (我们要证明读到的是真的), 不在资产挪用。这正是 auditability 设计的一部分。
> **给分点**: 「不托管」立场清晰 0.4; 两层区分 0.4; 落到 auditability 0.2。

## Q10 [英] 口径卡产出
写 custody 与 distribution 各两版英文一句话 (外行版/机构版), 记入你的口径卡。
> **参考**: custody 机构版示例: "Custody is about who controls the keys and the withdrawal path — in crypto market structure, it's the single biggest counterparty question." distribution 机构版: "Distribution is who owns the end user and the default trading entry point — in this industry, wallets and exchanges are fighting for exactly that."
> **给分点**: 四句各 0.25, 语域对。
