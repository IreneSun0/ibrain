---
id: "concept:distribution"
type: concept
title: Distribution
title_zh: 用户分发/入口
title_en: Distribution
aliases:
  - Wallet Distribution
  - 用户分发
  - 钱包分发
status: reviewed
importance: tier-1
domains:
  - industry-strategy
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
  - id: "venue:binance"
    rel: instantiated-by
    note: ~300M 用户 — 行业最大分发入口 (公司口径)
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 产业战略
---
# Distribution | 用户分发/入口

## Executive Definition / Chinese Explanation | 定义与解释

**Distribution | 分发** = 用户从哪里进入你的产品。在事件市场，它正在成为比撮合技术更重要的竞争维度。

一句话：**撮合引擎可以买，牌照可以买，分发买不到 —— 它是别人已经拥有的用户关系。**

## Why This Matters | 为什么重要

事件市场的产品是**极易复制的**：全额抵押的二元合约、CLOB 或 AMM 撮合、预言机裁决 —— 这些都有成熟方案，白标供应商甚至能把"开一个预测市场"压缩到 30 天上线。

**当产品可复制时，竞争就转移到分发。**

而分发的持有者不是场馆：
- **钱包**（数亿用户，一键进入）
- **券商 App**（已有金融账户与合规关系）
- **交易所**（现成的交易用户与资金）

**场馆做的是产品，钱包和券商做的是入口 —— 入口方的议价权在上升。**

## How It Works | 机制怎么运转

分发关系的三种形态，场馆的位置依次变弱：

| 形态 | 场馆得到 | 场馆失去 |
|---|---|---|
| **自有 App** | 全部关系与数据 | 获客成本极高 |
| **API 接入合作方** | 订单流 | 用户是对方的 |
| **白标输出** | 技术费 | **完全隐形** |

**第二行是当前主流**：券商向零售分发事件合约，场馆拿订单流，券商拿分成。

**这个结构的经济含义**：**场馆变成了后端的"合约工厂"，前端关系归分发方。** 长期看，利润会向掌握用户的一侧转移 —— 这是所有平台生意的共同规律。

## Concrete Example | 具体例子

事件市场分发格局的三条已发生的路径：

1. **钱包内嵌** —— 主流交易所钱包内嵌预测市场，由第三方场馆驱动，2 亿+ 用户入口、一键免 gas。
2. **券商分发** —— 持牌事件交易所通过零售券商 App 分发合约，券商在 10-K 中披露对这条关系的依赖。
3. **白标输出** —— 基础设施商把"开一个预测市场"做成 30 天上线的商品。

**三条路径指向同一个结论**：**venue 的数量会暴增，而每个新 venue 都自带结算与语义质量问题**（见 [[contract-equivalence]]）。

**分发的胜利，同时是碎片化的加速。**

## Common Misconceptions | 常见误解

- **误解一："产品好就会有用户。"** 在可复制的产品上，分发决定份额。
- **误解二："分发就是营销。"** 它是**已有的用户关系与信任**，营销买不到。
- **误解三："被分发方拿走利润是坏事。"** 对场馆是，但对整个市场未必 —— 分发降低了准入门槛，扩大了参与规模。

## In Practice | 实战里怎么用

判断一个事件市场参与者的战略位置，问三件事：

1. **它拥有用户关系吗？** 还是租来的？
2. **如果分发方明天换供应商，它还剩什么？** 剩得越多护城河越硬。
3. **它在这条链上的位置是可替代的吗？** 撮合可替代，牌照较难，**裁决可信度与语义能力最难**。

**一条推论**：在一个分发被别人掌握、产品又可复制的市场里，**唯一稳固的位置是别人做不了或不能可信地做的事** —— 比如中立地评价所有场馆的裁决质量。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么分发在事件市场比撮合技术更重要？
  A: 产品极易复制（白标供应商可 30 天上线），当产品可复制时竞争就转移到分发，而分发是别人已拥有的用户关系。
- Q: 三种分发形态里，场馆的位置如何依次变弱？
  A: 自有 App（全部关系）→ API 接入（拿订单流但用户是对方的）→ 白标输出（完全隐形，只拿技术费）。
- Q: 分发的胜利同时带来了什么副作用？
  A: venue 数量暴增导致碎片化加速，每个新场馆都自带结算与语义质量问题。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
