---
id: "concept:clearinghouse"
type: concept
title: Clearinghouse
title_zh: 清算所/中央对手方
title_en: Clearinghouse
aliases:
  - CCP
  - Central Counterparty
  - 清算所
status: reviewed
importance: tier-1
domains:
  - financial-markets
  - institutional-risk
tags:
  - concept
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources: []
related:
  - id: "venue:kalshi"
    rel: instantiated-by
    note: Kalshi Klear = 自有 DCO 清算所 (2024-08)
prerequisites:
  - "concept:clearing"
---
# Clearinghouse | 清算所

## Executive Definition / Chinese Explanation | 定义与解释

**Clearinghouse / CCP | 清算所 / 中央对手方** = 通过"合约更替（novation）"把自己插进每一笔交易中间的机构：原本 A 和 B 的一份合约，被换成 A 对 CCP、CCP 对 B 的两份合约。

结果是**所有人只需要评估一个对手方的信用**，而不是市场上每一个交易对手。这是 20 世纪金融基础设施最重要的发明之一。

## Why This Matters | 为什么重要

它同时解决了两个问题：

- **信用问题** — 你不需要调查对手是谁，只需要相信 CCP。
- **规模问题** — 所有人对同一个对手方，净额可以在全市场范围内做，资金效率再上一个台阶。

代价是**风险高度集中**：CCP 自己成了系统性单点。2008 年后监管把大量场外衍生品强制推向中央清算，同时也就把风险集中到了少数几家 CCP 身上 —— 这是当前全球金融监管公认的核心难题之一。

## How It Works | 机制怎么运转

CCP 靠一套分层的**违约瀑布（default waterfall）**吸收损失，顺序不可乱：

1. **违约方的保证金** — 先烧违约者自己的钱。
2. **违约方缴纳的违约基金份额** — 还是违约者的钱。
3. **CCP 自有资本（skin in the game）** — CCP 自己出一部分，确保它有动力把风控做好。
4. **其他会员的违约基金** — 幸存者共同分担。
5. **追加摊派 / 减记** — 最后手段，实际动用意味着市场已处于危机。

**"skin in the game"放在会员资金之前是刻意设计**：如果 CCP 亏的永远是别人的钱，它就没有动力严格风控。

## Concrete Example | 具体例子

**Kalshi** 的架构是理解这件事最直接的样本：它既有 CFTC 持牌的交易所（DCM），又有自己的清算机构 **Kalshi Klear**（DCO）。这意味着上市、撮合、清算在同一个集团内闭环。

**Polymarket** 走了另一条路：2025 年 7 月以约 $112M 收购 QCEX，一次拿到 **QCX（DCM，交易所牌照）+ QC Clearing（DCO，清算牌照）**，用以合规重返美国市场。

对比之下，纯链上的事件市场**没有 CCP**：没有违约瀑布，也不需要 —— 因为全额抵押让"违约"这件事在机制上不可能发生。它把对手方风险换成了智能合约风险与预言机风险。

## Common Misconceptions | 常见误解

- **误解一："有 CCP 就没有风险了。"** 风险被转移和集中，没有消失。CCP 自己倒下是尾部风险中最严重的一种。
- **误解二："CCP 是监管机构。"** 它是商业机构（通常是交易所集团的一部分），受监管但不是监管者。
- **误解三："链上全额抵押等于有了 CCP。"** 全额抵押消除了信用风险，但没有提供 CCP 的另一半价值 —— **跨产品净额**。这正是链上市场资金效率上不去的结构性原因。

## In Practice | 实战里怎么用

看到"我们有清算"这句话时，追问四件事：

1. **是不是真的 CCP** —— 有没有做合约更替（novation）？还是只是内部记账？
2. **违约瀑布怎么排** —— 自有资本排在会员资金之前吗？
3. **保证金模型是什么** —— SPAN 类还是 VaR 类？极端行情下的压力测试假设是什么？
4. **谁是会员，集中度多高** —— 前三大会员占多少？集中度高时，一家违约就可能击穿整个瀑布。

第 4 条在加密市场尤其关键，因为会员数量通常远少于传统市场。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: novation（合约更替）具体做了什么？
  A: 把 A-B 的一份合约替换为 A-CCP 与 CCP-B 两份，使所有参与者只需评估 CCP 一个对手方的信用。
- Q: 违约瀑布的顺序是什么？为什么 CCP 自有资本要排在其他会员的钱前面？
  A: 违约方保证金→违约方违约基金→CCP 自有资本→其他会员违约基金→摊派/减记。CCP 先出钱才有动力严格风控。
- Q: 纯链上全额抵押市场相比 CCP 少了什么能力？
  A: 少了跨产品净额。全额抵押消除信用风险，但资金无法在不同头寸间轧差，资金效率结构性偏低。


## Sources
