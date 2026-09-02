---
id: "concept:automated-market-maker"
type: concept
title: AMM
title_zh: 自动做市商
title_en: AMM
aliases:
  - AMM
  - Automated Market Maker
  - 自动做市商
status: reviewed
importance: tier-2
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
related:
  - id: "concept:central-limit-order-book"
    rel: contrasts-with
    note: 公式+资金池定价 vs 订单撮合定价; 无需传统 MM 即可冷启动
  - id: "concept:price-discovery"
    rel: mechanism-of
    note: 与 CLOB 并列的另一条定价机制路线
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# AMM | 自动做市商

## Executive Definition / Chinese Explanation | 定义与解释

**AMM (Automated Market Maker) | 自动做市商** = 用一个数学公式而不是订单簿来决定价格的做市机制。流动性提供者把资金存进池子，公式根据池子里的比例自动报价。

它的关键性质：**总是有报价**，代价是**报价由公式决定，无法在消息来临时保护自己**。

## Why This Matters | 为什么重要

AMM 和 [[central-limit-order-book|CLOB]] 在事件市场上是互补而非竞争关系：

| | CLOB | AMM |
|---|---|---|
| 头部合约（有做市商） | **好** | 一般 |
| 长尾合约（无人做市） | **空盘口，无法成交** | **总能成交（哪怕价差很差）** |
| 消息冲击时 | 做市商可撤单保护自己 | **被套利者按旧价吃干** |
| 资本效率 | 高（只在需要处挂单） | 低（全曲线铺开） |

**事件市场的合约数量以万计，绝大多数是长尾。** 这就是为什么成熟平台往往两者并用：头部走 CLOB，长尾用 AMM 兜底。

## How It Works | 机制怎么运转

事件市场用的 AMM 和加密现货的不太一样：

- **常数乘积（x·y=k）** —— Uniswap 式，适合两种资产互换。
- **LMSR（对数市场评分规则）** —— **专为预测市场设计**，能在整个结果空间上维持一致定价，保证所有结果价格之和为 1。

**LMSR 的关键性质是"有界损失"**：做市商的最大亏损由一个流动性参数 b 控制，可以事先算出来。**这让"我愿意为这个市场补贴多少流动性"变成一个可以预算的数字** —— 对平台来说非常实用。

代价是：b 越大，价格对交易越不敏感（更深但更迟钝）；b 越小，越灵敏但越容易被推动。

## Concrete Example | 具体例子

为什么 AMM 在消息冲击时会被吃干：

一个 AMM 池给某事件报价 0.30。消息公布，真实概率跳到 0.90。

- **CLOB 做市商**：看到消息 → 撤单 → 重新以 0.88/0.92 报价。**损失有限。**
- **AMM**：公式不知道有消息 → 仍按 0.30 起报 → 套利者持续买入，把价格一路推到 0.90。

**这中间被套走的差价，全部由流动性提供者承担。** 这就是 AMM 版本的 [[adverse-selection|逆向选择]]，在事件市场里因为价格是**跳变**的（不是渐变），损失比现货 AMM 严重得多。

**结论：AMM 适合"没人做市总比没有好"的长尾，不适合有信息冲击的头部合约。**

## Common Misconceptions | 常见误解

- **误解一："AMM 比 CLOB 落后。"** 在无人做市的长尾市场，**空的 CLOB 不如报价很差的 AMM** —— 至少后者能成交。
- **误解二："做 AMM 的流动性提供者是被动收租。"** 他们承担的是**无法撤退的逆向选择**，在跳变标的上尤其残酷。
- **误解三："LMSR 和常数乘积差不多。"** LMSR 专为多结果概率市场设计，能保证价格和为 1 且损失有界；常数乘积不能。

## In Practice | 实战里怎么用

看到一个事件市场用 AMM，问三个问题：

1. **用的是哪种曲线？** LMSR 还是常数乘积？多结果盘用常数乘积通常是设计缺陷。
2. **流动性参数是多少？** 它决定了深度和对交易的敏感度，也决定了补贴上限。
3. **有没有做市商保护机制？** 消息冲击时有暂停、有价格带、还是完全裸奔？

**作为流动性提供者，第 3 问决定你会不会被套干。**
**作为交易者，第 2 问决定你的大单会把价格推多远。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: AMM 相对 CLOB 的核心取舍是什么？
  A: AMM 总是有报价（适合无人做市的长尾），但报价由公式决定、无法在消息来临时撤退，会被套利者按旧价吃干。
- Q: LMSR 相对常数乘积的两个关键优势是什么？
  A: 能在整个结果空间维持一致定价（所有结果价格之和为 1），且做市商最大损失由流动性参数 b 界定，可事先预算。
- Q: 为什么 AMM 的逆向选择在事件市场比在现货市场更严重？
  A: 事件价格是跳变的而非渐变的，消息公布后价格从 0.30 直接到 0.90，套利者可持续按旧价吃入，全部差价由流动性提供者承担。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
