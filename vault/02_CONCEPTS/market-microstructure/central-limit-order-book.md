---
id: "concept:central-limit-order-book"
type: concept
title: CLOB
title_zh: 中央限价订单簿
title_en: CLOB
aliases:
  - CLOB
  - Central Limit Order Book
  - 中央限价订单簿
status: reviewed
importance: tier-1
domains:
  - market-microstructure
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
  - "source:2026-08-26-polymarket-prices-orderbook"
related:
  - id: "concept:order-book"
    rel: special-case-of
    note: 集中化+价格/时间优先撮合的订单簿
  - id: "concept:price-discovery"
    rel: mechanism-of
    note: 集中限价单竞价是最经典的价格发现机制
  - id: "venue:polymarket"
    rel: instantiated-by
    note: 链下 CLOB 撮合 (hybrid 架构的链下半)
  - id: "venue:kalshi"
    rel: instantiated-by
    note: 受监管 DCM 上的 CLOB
  - id: "venue:hyperliquid-hip4"
    rel: instantiated-by
    note: Hyperliquid L1 链上 CLOB
prerequisites:
  - "concept:order-book"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# CLOB | 中央限价订单簿

## Executive Definition / Chinese Explanation | 定义与解释

**CLOB | 中央限价订单簿** = 把所有限价单集中到**一个**簿子上，按价格优先、时间优先撮合的机制。

"中央"是关键词：所有订单流汇聚一处。这既是它效率的来源（流动性不被切碎），也是它的门槛（冷启动极难）。

## Why This Matters | 为什么重要

CLOB 是传统交易所和绝大多数专业加密场所的默认撮合模型。理解它，就理解了"为什么专业交易者偏好订单簿而不是 AMM"。

核心原因：**CLOB 让做市商可以精确表达价格观点并随时撤回**。AMM 的曲线是被动的，价格由公式决定，做市商无法在消息来临时保护自己 —— 这在事件市场里是致命的，因为事件市场的信息冲击是跳跃式的（消息一出，概率从 0.3 直接到 0.9），而不是连续的。

## How It Works | 机制怎么运转

CLOB 与 AMM 在事件市场上的关键差异：

| | CLOB | AMM |
|---|---|---|
| 价格来源 | 挂单博弈 | 公式（如常数乘积、LMSR） |
| 做市商能否撤退 | **能** | 不能（资金锁在池子里） |
| 消息冲击时 | 价差变宽或撤单 | **被套利者按旧价格吃干** |
| 长尾市场 | 盘口可能空着 | 总有报价（哪怕很差） |
| 资本效率 | 高（只在需要处挂单） | 低（全曲线铺开） |

**结论：CLOB 适合有做市商的头部市场，AMM 适合无人做市的长尾市场。** 成熟的事件平台往往两者并用 —— 头部走 CLOB，长尾用 AMM 兜底。

## Concrete Example | 具体例子

三种实现路径：

- **Polymarket** — **链下 CLOB 撮合 + Polygon 链上结算**的 hybrid 架构：撮合要快，所以放链下；钱要安全不可挪用，所以锁在链上合约里。这是当前加密事件市场的主流选择。
- **Kalshi** — CFTC 持牌 DCM 上的传统 CLOB，全部在受监管的基础设施内运行。
- **Hyperliquid HIP-4** — 把订单簿本身放到 L1 上跑，追求"链上可验证的 CLOB"，代价是对链性能的极高要求。

**三条路线在同一个权衡轴上取了不同的点**：撮合速度 ↔ 可验证性 ↔ 监管合规。

## Common Misconceptions | 常见误解

- **误解一："CLOB 一定比 AMM 好。"** 在没有做市商的长尾市场上，空的 CLOB 不如一个报价很差的 AMM —— 至少后者能成交。
- **误解二："链下撮合 = 中心化 = 不安全。"** 关键看**钱在哪**。链下撮合 + 链上全额抵押结算，平台无法挪用资金，安全模型和纯链上接近。
- **误解三："CLOB 就是技术实现问题。"** 撮合引擎是最容易的部分。难的是把订单流吸引过来 —— **空的 CLOB 一文不值。**

## In Practice | 实战里怎么用

看到一个事件平台，先分清它的**撮合层**和**结算层**各在哪里：

| 组合 | 代表 | 你要关心的风险 |
|---|---|---|
| 链下撮合 + 链上结算 | Polymarket | 撮合公平性（看不见）、合约风险 |
| 链上撮合 + 链上结算 | Hyperliquid HIP-4 | 链性能、拥堵时的可用性 |
| 全链下 + 持牌清算 | Kalshi | 平台信用、监管保护 |

**"钱在哪"和"撮合在哪"是两个独立的问题**，很多人把它们混为一谈。前者决定平台能不能卷款跑路，后者决定撮合是否公平 —— 两者都要单独问。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么专业做市商偏好 CLOB 而非 AMM？
  A: CLOB 允许精确表达价格并随时撤单，AMM 的资金锁在池子里、价格由公式被动决定，消息冲击时会被套利者按旧价吃干。
- Q: hybrid 架构（链下撮合 + 链上结算）解决了什么权衡？
  A: 撮合需要低延迟所以放链下，资金安全需要不可挪用和可验证所以放链上，两者各取所长。
- Q: 在什么情况下 AMM 反而优于 CLOB？
  A: 无人做市的长尾市场 —— 空的 CLOB 无法成交，AMM 至少始终提供（虽然较差的）报价。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-polymarket-prices-orderbook]] — <https://docs.polymarket.com/concepts/prices-orderbook>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场微观结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = order-book; typed 关系 5 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
