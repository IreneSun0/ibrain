# Query Eval Benchmark | 检索基准问题集

> 15 问。`expects:` 行是机器可读的存在性断言 (note 文件名), `build_query_eval.py` 检查; 答案质量由人工/agent 评。每问标注: 类型 (fact/synthesis/judgment) + 已知缺口。**不为让基准通过而造答案。**

### Q1. CLOB 怎么运作? Polymarket 哪些在链上哪些在链下?
expects: central-limit-order-book, polymarket, hybrid-exchange-architecture, on-chain, off-chain
类型: fact。缺口: 无 — 页面齐。

### Q2. 预测市场里钱在哪、谁担风险、结算如何完成?
expects: prediction-market, fully-collateralized-market, settlement-methodology, resolution, outcome-token
类型: fact+synthesis。缺口: 无。

### Q3. Binance/OKX/HTX/Bybit/Bitget/Hyperliquid 之间是什么关系?
expects: map-exchange-power, binance, okx, htx, bybit, bitget, hyperliquid-hip4, chinese-exchange-lineage
类型: synthesis。缺口: 无 — 竞争+谱系+对比表齐。

### Q4. OKCoin、CZ、Yi He、Binance、OKX 的历史联系?
expects: chinese-exchange-lineage, changpeng-zhao-cz, yi-he, star-xu, rel-changpeng-zhao-cz--former-executive-of--okx
类型: fact。缺口: Yi He 招募 CZ 单源。

### Q5. Huobi、HTX、杜均、ChainUp、TRON 之间的关系?
expects: chinese-exchange-lineage, htx, du-jun, chainup, tron, map-tron-htx-chainup, leon-li
类型: fact+synthesis。缺口: HTX 所有权 disputed (如实); 杜均-ChainUp 聚合级源。

### Q6. TRON Bandwidth 和 Energy 是什么? 为什么 Energy 是 B2B 生意?
expects: tron-bandwidth, tron-energy, tron-energy-delegation, tron, justlend
类型: fact。缺口: Energy 租赁市场定价深度未研究。

### Q7. 稳定币、链、交易所、做市商、衍生品、OTC 台怎么连成资本管道?
expects: map-crypto-capital-flow, stablecoin, settlement-rail, over-the-counter, tether, circle
类型: synthesis。缺口: 法币通道 (banking rails) 未展开。

### Q8. 预测市场与结果市场的区别?
expects: prediction-market, outcome-market, event-contract, hyperliquid-hip4
类型: fact。缺口: 无。

### Q9. 为什么两个标题相似的事件合约可能对冲失败?
expects: contract-equivalence, contract-semantics, basis-risk, settlement-methodology, case-kalshi-khamenei-settlement
类型: fact+synthesis。缺口: 无 — 四层清单+两案例支撑。

### Q12. 还缺什么证据?
expects: KNOWLEDGE-COVERAGE-MATRIX, RESEARCH-BACKLOG, strategic-risks
类型: synthesis。缺口: 本问的答案就是缺口清单本身。

### Q13. Irene 应该优先见哪些组织、为什么?
expects: hyp-market-maker-design-partner, wintermute, susquehanna, chainup, map-prediction-distribution-liquidity
类型: judgment。缺口: 排序是 assistant 建议, 未经裁定。

### Q14. 一个事件如何跨预测市场、crypto 衍生品和组合传导?
expects: map-event-risk-cross-asset, event-var, combinatorial-market, concentration-risk
类型: synthesis。缺口: 传导系数无实测校准 (2025-10-10 样本待做)。

### Q15. 知识库里哪些断言过期或弱源?
expects: KNOWLEDGE-COVERAGE-MATRIX
类型: fact (由工具回答)。缺口: 无 — `make refresh` 跑 source-freshness + 各页 SINGLE-SOURCE 标注即答案。
