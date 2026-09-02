---
id: "concept:double-spending"
type: concept
title: Double Spending
title_zh: 双重支付
title_en: Double Spending
aliases:
  - 双重支付
status: reviewed
importance: tier-2
domains:
  - blockchain
tags:
  - concept
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: high
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
related:
  - id: "concept:ledger"
    rel: risk-of
    note: 数字资产可复制 — 无共识的数字账本的根本威胁
  - id: "concept:consensus"
    rel: mitigated-by
    note: PoW/PoS 使重写交易历史在经济上昂贵
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Double Spending | 双重支付

## Executive Definition / Chinese Explanation | 定义与解释

**Double Spending | 双花** = 同一笔钱被花两次。

这是数字货币在中本聪之前**无解的根本问题**：数字文件可以完美复制，凭什么保证一份数字现金没有被同时发给两个人？

## Why This Matters | 为什么重要

双花问题的解法，就是区块链存在的全部理由。

**传统解法是中心化账本**：银行记账，它说你有多少就有多少，因此不可能双花 —— 代价是你必须信任银行。

**中本聪的解法是让所有人共同记账，并让改写历史变得昂贵**（见 [[consensus]]）。这样就在**没有中心机构**的前提下解决了双花。

**理解这一点，就理解了"什么时候值得上链"**：只有当你需要在互不信任的多方之间维护共享状态时，这套昂贵的机制才划算（见 [[blockchain]]）。

## How It Works | 机制怎么运转

双花攻击的两种形态：

| 形态 | 机制 | 防线 |
|---|---|---|
| **竞态双花** | 同时广播两笔冲突交易，赌哪笔先确认 | **等待确认数** |
| **重组攻击（51%）** | 掌握多数算力/权益，重写已确认的历史 | 攻击成本 > 收益 |

**"等待确认数"是所有交易所提现规则的由来**：确认数越多，交易被重组掉的概率越低。

**对事件市场的直接含义**：**结算的最终性必须早于资金的可提取性**（见 [[consensus]]）。若赢家在最终性达成前就提走并卖掉，一次重组就会制造出无中生有的钱。

## Concrete Example | 具体例子

为什么确认数在事件市场结算里是风险参数而非技术细节：

```
判定完成 → 合约按结果分配 → 赢家提现 → 转到交易所卖出
             ↑                    ↑
        需要 N 个确认         若此时发生重组
                              链上记录变了, 但钱已经离开
```

**平台设置提现等待期，就是在给这个窗口留安全边际。**

**不同链需要的确认数差异巨大**：有明确最终性的链（多数 PoS）几乎立即安全；概率性最终性的链需要等待更久。**这直接影响用户体验与结算风险，是选链时的实质考量。**

## Common Misconceptions | 常见误解

- **误解一："双花已经是历史问题。"** 对主流大链是；对小链和低算力链仍是现实威胁。
- **误解二："交易确认了就绝对安全。"** 概率性最终性的链上，确认只是降低回滚概率，不是消除。
- **误解三："双花只影响转账。"** 任何依赖链上状态的操作都受影响 —— 包括事件合约的结算。

## In Practice | 实战里怎么用

评估一条链能否承载事件市场结算，两问：

1. **最终性是确定的还是概率性的？** 确定性最终性的链，结算风险窗口小得多。
2. **多少确认后可以安全提现？** 拿这个数字对照平台的提现等待期 —— **等待期短于安全确认数的平台，在赌不会发生重组。**

**一条通用判据**：**结算确定性必须早于资金可提取性。** 任何反过来的设计都是在给自己留一个可被利用的窗口。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 双花问题为什么是数字货币的根本问题？
  A: 数字文件可完美复制，在没有中心账本的前提下无法保证同一笔钱不被同时发给两个人。
- Q: 双花攻击的两种形态和对应防线是什么？
  A: 竞态双花（等待确认数）和重组/51% 攻击（攻击成本必须大于收益）。
- Q: 事件市场结算的通用判据是什么？
  A: 结算确定性必须早于资金可提取性；否则赢家可能在最终性达成前提走资金，一次重组就制造出无中生有的钱。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
