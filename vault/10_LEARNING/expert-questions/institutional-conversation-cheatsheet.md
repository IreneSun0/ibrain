---
id: "report:institutional-conversation-cheatsheet"
type: report
title: Institutional Conversation Cheatsheet (workbook)
title_zh: 机构对话速查 · workbook 原文
aliases: []
status: seed
importance: tier-1
domains:
  - learning
  - institutional-risk
tags:
  - xlsx-import
created: 2026-08-26
updated: 2026-08-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related: []
import_origin: xlsx-learning-map
---

# 机构对话速查 · workbook 原文

> 见机构人士之前 5 分钟过一遍: 对方的钱在哪里、最怕什么、该问什么。

| 对象 | 钱在哪里 | 他最怕什么 | 谁承担风险 | 如何结算 | 你应该问的第一类问题 |
|---|---|---|---|---|---|
| Exchange CTO | 客户余额、collateral、fee revenue、insurance/default buffers | 撮合/风控宕机、hack、坏账、清算、合规、扩容 | 用户+venue+clearing/custody体系 | 内部账本、清算系统、链/银行 | 哪一类失败会让你们暂停市场或拒绝某个contract？ |
| Market Maker | 自有working capital、inventory、exchange balances、credit lines | adverse selection、inventory、latency、venue/counterparty、hedge失效 | 主要由MM承担即时市场风险 | 多venue净额、链上/交易所/OTC | 你在哪些event contracts上最不愿意做大size，为什么？ |
| Quant PM | 基金NAV、margin、collateral、prime账户 | 模型失效、执行成本、相关性、leverage、drawdown | 基金/LP资本 | broker/exchange/custodian/chain | 你现在最难统一度量的event exposure是什么？ |
| Fund Manager / CIO | 基金资本、LP资金、cash buffer | 最大回撤、流动性、LP赎回、counterparty、合规 | 基金对LP负责 | prime/custody/bank/exchange | 什么风险会阻止你扩大prediction/event-market allocation？ |
| Wallet / Distribution | 用户stablecoin/crypto、交易入口 | 用户流失、签名安全、欺诈、合规、差的execution | 用户+wallet运营方（视结构） | 路由到底层venue后结算 | 你想把event markets内嵌进钱包时，最缺哪一层可信风险信息？ |

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]]

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 原文导入。
