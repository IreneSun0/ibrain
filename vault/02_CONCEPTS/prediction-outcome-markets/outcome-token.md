---
id: "concept:outcome-token"
type: concept
title: Outcome Token
title_zh: 结果代币
title_en: Outcome Token
aliases:
  - 结果代币
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
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
  - "source:2026-08-26-polymarket-overview"
related:
  - id: "concept:token"
    rel: special-case-of
    note: 代表特定结果支付权的 token
  - id: "concept:outcome-market"
    rel: component-of
    note: outcome market 的可转让构件
  - id: "concept:erc-1155"
    rel: see-also
    note: Polymarket CTF 用 ERC-1155 一约承载多结果 token
prerequisites:
  - "concept:token"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Outcome Token | 结果代币

## Executive Definition / Chinese Explanation | 定义与解释

**Outcome Token | 结果代币** = 把"我持有某个事件的某个结果"这件事，从**账户里的一条记录**变成**一个可转移的链上资产**。

Polymarket 用 ERC-1155 实现：一个合约地址下可以有无数个 token id，每个 id 对应一个具体的"事件 + 结果"组合。

## Why This Matters | 为什么重要

这一步改变的不是交易体验，是**资产的性质**。变成 token 之后，事件敞口获得了三个原本没有的属性：

- **可转移** — 不必等到事件揭晓才能退出，随时可以在二级市场换手。
- **可组合** — 能进钱包、能进 DeFi、能做抵押品，事件敞口第一次接入了更大的金融体系。
- **可审计** — 谁持有多少、什么时候进出，链上全透明。

**第三条是价格类市场做不到的数据条件。** 在传统市场里你无法知道某个参与者的真实持仓；在链上事件市场里，任何人都能重建某个地址的完整事件敞口画像。

## How It Works | 机制怎么运转

ERC-1155 被选中不是偶然，它正好是这个场景需要的形状：

| 标准 | 特性 | 适不适合 |
|---|---|---|
| ERC-20 | 一个合约一种同质代币 | 每个结果都要部署一个合约 —— 太贵 |
| ERC-721 | 一个合约多个**唯一**代币 | 结果份额需要同质可分割 —— 不匹配 |
| **ERC-1155** | 一个合约多个 id，**id 之间异质、id 之内同质**，且支持批量转移 | **正好** |

"id 之间异质"= 不同事件不同结果互不相同；"id 之内同质"= 同一结果的每一份完全等价可互换。**一个标准选型，决定了整个市场的可组合性与可审计性。**

## Concrete Example | 具体例子

一份"某候选人当选"的合约在链上的样子：

```
合约地址 0xABC…（Conditional Tokens 框架）
 ├─ token id 0x1f3a…  = "候选人 A 当选 → YES"
 └─ token id 0x9c72…  = "候选人 A 当选 → NO"
```

- 你存 $1 → 各得 1 份 YES 和 1 份 NO。
- 卖掉 NO 得 $0.37 → 净成本 $0.63，持有 1 份 YES。
- 想提前退出 → 直接把 YES 转给别人，不必等选举结束。
- **任何人都能查到你这个地址持有多少份、什么时候买的。**

最后一条既是透明度的胜利，也是隐私的代价 —— 大户的持仓无法隐藏，这本身会影响市场行为。

## Common Misconceptions | 常见误解

- **误解一："token 化只是技术选型。"** 它决定了敞口能不能提前转让、能不能进 DeFi、能不能被第三方审计。这些都是产品能力，不是实现细节。
- **误解二："链上透明所以更公平。"** 透明是双向的：你能看别人，别人也能看你。**大户建仓会被跟单，这会改变他们的下单行为**（拆单、多地址）。
- **误解三："outcome token 有内在价值。"** 它的价值完全来自那份合约的赔付承诺。合约裁决出错，token 一文不值 —— **它不是一种资产，是一份索赔权。**

## In Practice | 实战里怎么用

把 outcome token 的链上可读性当成一个真实的分析工具：

1. **持仓集中度** — 前 10 个地址占多少？集中度高说明这个价格是少数人的观点。
2. **建仓时序** — 大额头寸是什么时候建的？在什么消息之前？（这是识别可能的信息优势的最直接线索）
3. **跨事件敞口** — 同一地址在多少个相关事件上有头寸？这能看出它是对冲还是单向押注。

**这三项分析在传统市场里需要监管权限才能做，在链上任何人都能做。** 这是事件市场少数几个结构性优于传统市场的地方。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: token 化给事件敞口带来了哪三个新属性？
  A: 可转移（提前退出）、可组合（进钱包与 DeFi）、可审计（链上持仓全透明）。
- Q: 为什么 ERC-1155 比 ERC-20 和 ERC-721 更适合结果代币？
  A: 一个合约容纳多个 id，id 之间异质（不同结果）、id 之内同质（份额可互换），并支持批量转移。
- Q: 链上透明的代价是什么？
  A: 透明是双向的 —— 大户持仓无法隐藏，会被跟单，因而改变其下单行为（拆单、多地址）。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, Irene 提供)
- [[src-2026-08-26-polymarket-overview]] — <https://docs.polymarket.com/developers/CTF/overview>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 预测市场)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = token; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
