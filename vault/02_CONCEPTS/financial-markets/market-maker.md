---
id: "concept:market-maker"
type: concept
title: Market Maker
title_zh: 做市商
title_en: Market Maker
aliases:
  - 做市商
status: reviewed
importance: tier-1
domains:
  - financial-markets
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
  - id: "concept:liquidity-provider"
    rel: special-case-of
    note: "最专业的一类流动性提供者: 持续双边报价+管理库存与信息风险"
  - id: "mmf:wintermute"
    rel: instantiated-by
    note: 2026-05 官宣进入预测市场做市 (Polymarket+Kalshi 双场馆)
  - id: "mmf:susquehanna"
    rel: instantiated-by
    note: Kalshi 首个旗舰机构做市商 (2024-04 起)
  - id: "mmf:jane-street"
    rel: instantiated-by
    note: 顶级量化做市商
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 市场结构
---
# Market Maker | 做市商

## Executive Definition / Chinese Explanation | 定义与解释

**Market Maker | 做市商** = 同时挂出买价和卖价、随时准备用自有资金接下对手盘的交易者。

它赚的是**价差**（买低卖高的那一点点），承担的是**存货风险**（接了单之后价格反向跑）和**逆向选择**（跟你成交的人可能知道你不知道的事）。

一句话：做市商卖的是"立刻能成交"这个服务，价差就是这个服务的价格。

## Why This Matters | 为什么重要

没有做市商，市场就只剩下"恰好有对手方在同一时刻想做反向交易"的偶然成交 —— 这在事件市场里几乎不会发生，因为大部分事件是长尾的、冷门的。

**预测市场的核心难题是：事件数量以万计，每个事件都需要有人报价，但绝大多数事件没有自然的双向需求。** 谁来给"某国 12 月 CPI 超过 3%"报价？只有做市商。所以做市商激励设计（返佣、库存补贴、做市商专属费率）是这类平台能不能活的关键，不是附加功能。

## How It Works | 机制怎么运转

做市商的一天基本是三件事的循环：

1. **报价** — 围绕自己估计的"公允价值"上下各挂一个价，中间是价差。公允价越不确定，价差挂得越宽。
2. **管库存** — 成交后手上有了头寸，要么在别的场所对冲掉，要么调整报价把库存推回中性（比如手上多了 YES，就把两边报价整体下移，鼓励别人来买你的 YES）。
3. **防逆向选择** — 如果一直被同一个方向吃单，说明对手方可能有信息。此时正确反应是**拉宽价差或撤单**，而不是继续报。

**信息不对称越严重的市场，价差必然越宽** —— 这不是做市商贪，是它在为承担信息劣势定价。

## Concrete Example | 具体例子

一个"美联储 12 月降息"合约，做市商估计公允价 0.62：

- 挂 **买 0.60 / 卖 0.64**，价差 4 分。
- 有人按 0.64 买走 1000 份，做市商现在**空** 1000 份 YES，成本 0.64。
- 它立刻在另一个场所以 0.625 买回 800 份对冲，锁定 1.5 分利润；剩 200 份敞口。
- 十分钟后美联储官员讲话偏鸽，公允价跳到 0.71 —— 剩下那 200 份亏 1.4 分/份。

**这次它靠价差赚的钱被存货风险吃掉了一半。** 做市不是无风险套利，是靠大量重复交易让价差收益的期望值盖过存货和逆向选择的损失。

## Common Misconceptions | 常见误解

- **误解一："做市商在操纵价格。"** 它的常态是**被动接单**并尽快回到中性，方向性观点不是它的收入来源。真要操纵，反而得放弃对冲、承担巨大敞口。
- **误解二："价差宽是平台黑。"** 价差反映的是做市商面对的不确定性与库存成本。冷门长尾事件价差宽是必然的，逼窄只会让做市商撤走。
- **误解三："有做市商就有流动性。"** 做市商随时可以撤单。**恰恰在最需要流动性的时刻（消息冲击、临近裁决）它撤得最快** —— 这就是所谓"流动性在你最需要时消失"。

## In Practice | 实战里怎么用

评估一个事件市场的做市质量，看四个指标，缺一不可：

1. **价差** — 中间价附近买卖差多少分？
2. **深度** — 价差之内两侧各挂了多少钱？
3. **韧性** — 大单吃掉之后，多久恢复到原来的价差和深度？
4. **消息时刻的在场率** — 重大消息发生后 5 分钟内，报价还在不在？

第 4 条最能区分"真做市"和"平时刷个样子"。绝大多数平台的公开数据只给你前两条，第 3、4 条要自己抓时序数据算。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 做市商赚什么钱，承担什么风险？
  A: 赚买卖价差；承担存货风险（成交后价格反向）和逆向选择（对手方有信息优势）。
- Q: 为什么信息不对称越严重的市场价差越宽？
  A: 价差是做市商为承担信息劣势定的价。被有信息的人反复吃单会亏钱，只能靠拉宽价差补偿或直接撤单。
- Q: 为什么说'有做市商'不等于'有流动性'？
  A: 做市商可随时撤单，且在消息冲击和临近裁决时撤得最快，流动性恰在最需要时消失。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 市场结构)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = 无硬前置 (判断过的空); typed 关系 4 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
