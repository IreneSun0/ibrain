---
id: "curr:curriculum-source-map"
type: report
title: Curriculum Source Map (workbook)
title_zh: 学习地图 · workbook 原文
aliases: []
status: seed
importance: tier-1
domains:
  - learning
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

# 学习地图 · workbook 原文

> 8 阶段学习地图原文。手写 curriculum 以此为骨架; 本页保持与 workbook 一致, 不手改。

| 阶段 | 节点 | 它解决什么 | 钱在哪里 | 主要风险 | 谁承担风险 | 怎么结算 | 必须会问的问题 |
|---|---|---|---|---|---|---|---|
| 1 | Financial Markets 金融市场 | 资本怎么被配置、风险怎么被转移 | 投资者/基金/企业/银行/交易商的现金与资产 | 市场、信用、流动性、政策等 | 不同参与者分别承担 | 银行账本、证券/现金系统 | 为什么这个市场存在？谁需要它？ |
| 2 | Exchange 交易所 | 把买卖双方和统一规则集中起来 | 客户账户、保证金、订单流 | 平台、技术、监管、托管、价格风险（视架构） | 用户、MM、venue、清算方 | 内部账本/清算机构/区块链 | 谁能交易？谁托管？谁是最终对手方？ |
| 3 | Market Microstructure 市场微观结构 | 解释一个订单如何变成成交和价格 | 盘口里的实际可执行资金 | spread、slippage、adverse selection、price impact | maker/taker/MM | 成交后进入clearing/settlement | 我能以这个价格成交多少？大单会把价格推多远？ |
| 4 | Derivatives 衍生品 | 重新塑造、杠杆化和对冲风险 | margin/collateral + notional exposure | basis、leverage、liquidation、counterparty | 买卖双方/clearinghouse | 清算/每日盯市/到期支付 | 我真正暴露于哪个underlying？最坏要付多少？ |
| 5 | Blockchain 区块链 | 多方共享可验证账本并可编程执行 | 链上token、gas、staked capital | key、smart contract、oracle、bridge、consensus | 用户/validator/protocol | on-chain finality | 哪些必须上链？哪些链下更合理？信任假设是什么？ |
| 6 | Crypto Market Structure 加密市场结构 | 把CEX/DEX/wallet/stablecoin/custody/chain连成资本管道 | stablecoin、exchange balances、OTC/prime资金 | custody、counterparty、bridge、funding、regulatory | exchange/MM/custodian/issuer/user | 链上+中心化内部账本+银行 | 钱在哪个平台？能否自由转移？谁能冻结？ |
| 7 | Prediction Markets 预测市场 | 把现实事件不确定性变成可交易合约 | event contract collateral + liquidity | resolution、inside info、liquidity、semantic/basis risk | trader/MM/venue/oracle | 事件判定后$0/$1或多结果支付 | 这个contract到底承诺什么？谁决定事实？ |
| 8 | Institutional Risk 机构风险 | 把单笔交易放回整个portfolio和组织约束 | NAV、collateral、credit lines、capital budget | VaR/ES、concentration、counterparty、regulatory、operational | PM/CRO/risk/compliance/ops | 跨venue、custody、clearing、bank/chains | 看对方向以后，还有什么能让我拿不到钱或被迫退出？ |

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]]

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 原文导入。
