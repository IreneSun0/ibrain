---
id: "concept:know-your-transaction"
type: concept
title: KYT
title_zh: 了解交易/链上交易监控
title_en: KYT
aliases:
  - KYT
  - Know Your Transaction
  - 了解交易
status: reviewed
importance: tier-2
domains:
  - regulation-compliance
  - crypto-market-structure
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
  - id: "concept:know-your-customer"
    rel: contrasts-with
    note: "KYC 看人, KYT 看钱 — crypto AML 必须两者都有"
  - id: "concept:anti-money-laundering"
    rel: mechanism-of
    note: 资金来源与链上关联分析
  - id: "org:chainalysis"
    rel: instantiated-by
    note: 链上 KYT/情报供应商
prerequisites:
  - "concept:know-your-customer"
import_origin: xlsx-learning-map+manual
import_category: Crypto合规
---
# KYT | 了解交易/链上交易监控

## Executive Definition / Chinese Explanation | 定义与解释

**KYT (Know Your Transaction) | 交易链上尽调** = 对链上资金流动做实时分析：这笔钱从哪来、经过了什么、有没有碰过被制裁的地址。

它是[[know-your-customer|KYC]] 在链上的补充：**KYC 认人，KYT 认钱。**

## Why This Matters | 为什么重要

链上有一个传统金融没有的性质：**钱是有历史的。**

一笔 USDC 在到你手里之前的完整路径是公开的。如果它经过了被制裁的地址或混币器，**那段历史会跟着它** —— 而接收方可能因此被冻结或被要求解释。

**对事件市场用户的实际影响**：你在链上事件市场收到的赔付，其资金来源是一个合约池，而池子里的钱来自所有参与者。**理论上，池子被污染的风险是共享的。**

这是链上市场特有的一类风险，传统账户体系里不存在。

## How It Works | 机制怎么运转

KYT 的三层分析：

1. **地址标签** —— 这个地址属于交易所、混币器、还是已知的非法实体？
2. **路径追踪** —— 资金经过了几跳？中间有没有高风险节点？
3. **风险评分** —— 综合给出一个可操作的分数，供机构决定是否接受。

**加密特有的难点是地址聚类**：一个人可以有无数地址，KYT 要判断哪些地址属于同一实体 —— 这本身是概率判断，可能出错。

**误判的代价是真实的**：正常用户的资金被标记为高风险而遭冻结，申诉困难。

## Concrete Example | 具体例子

为什么这对链上事件市场用户是真实风险：

```
你在链上事件市场赢了 $10,000
从合约池领取赔付
提现到交易所
交易所的 KYT 系统标记: 该笔资金路径含高风险节点
资金被冻结, 要求你说明来源
```

**你什么都没做错** —— 但池子里的钱来自所有参与者，而链上事件市场通常不做参与者 KYC。

**实用应对**：
- 大额资金出金前，先小额试探。
- 保留完整的交易记录以备说明。
- **优先选择有 KYC 的持牌平台** —— 它的资金池被污染的概率低得多。

**这是"持牌平台流动性差但资金更干净"这个取舍的一个具体维度。**

## Common Misconceptions | 常见误解

- **误解一："链上匿名所以 KYT 没用。"** 链上是假名，行为可被分析聚类（见 [[public-key]]）。
- **误解二："我的钱来源合法就没事。"** 风险来自**资金路径**，不只是你自己的行为。
- **误解三："KYT 是机构的事。"** 出金时你就会撞上它 —— 它直接决定你能不能把钱拿出来。

## In Practice | 实战里怎么用

在链上事件市场活动，三条实用纪律：

1. **地址分层** —— 交互地址与主仓位分开（见 [[private-key]]），限制污染传播。
2. **大额分批出金** —— 先小额试探目标交易所是否放行。
3. **留痕** —— 保存交易哈希与时间线，被问及时能说清楚。

**再加一条选平台的判据**：**平台做不做参与者 KYC，直接影响你收到的钱有多"干净"** —— 这是持牌平台被低估的一个实际好处。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: KYT 与 KYC 的分工是什么？
  A: KYC 认人（客户身份），KYT 认钱（链上资金路径与来源）。
- Q: 为什么链上事件市场用户会承担共享的资金污染风险？
  A: 赔付来自合约池，池子里的钱来自所有参与者，而多数链上平台不做参与者 KYC，路径污染风险是共享的。
- Q: KYT 的加密特有难点是什么？误判代价是什么？
  A: 地址聚类（判断哪些地址属于同一实体）本身是概率判断；误判会导致正常用户资金被冻结且申诉困难。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
