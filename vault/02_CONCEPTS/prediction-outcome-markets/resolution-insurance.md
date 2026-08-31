---
id: "concept:resolution-insurance"
type: concept
title: Resolution Insurance
title_zh: 结果判定保险
title_en: Resolution Insurance
aliases:
  - 判定保险
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
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
related: []
prerequisites:
  - "concept:resolution-risk"
---
# Resolution Insurance | 结果判定保险

## Executive Definition / Chinese Explanation | 定义与解释

**Resolution Insurance | 裁决保险** = 针对"合约被判错"这一风险的赔付安排 —— 无论它以平台保证金、第三方保险、还是互助资金池的形式存在。

**目前这个市场基本不存在。** 但它的需求已经被多起真实事件证明了。

## Why This Matters | 为什么重要

因为现状是：**判错了，损失全部由用户承担，且通常零追索。**

[[polymarket]] 在 Ukraine 矿产协议案（2025-03）里公开定性该事件为 "unprecedented governance attack"，**但拒绝退款**，理由是不构成 market failure。受害者零补偿。

对比之下，[[kalshi]] 在 Khamenei 案（2026-03）里冻结 $54M、最终赔付约 **$2.2M** 并把新规则备案 CFTC —— **但这是监管框架下的个案处理，不是一个可依赖的制度。**

**没有裁决保险，机构资金就必须把裁决风险全额计入自有风险预算** —— 而这个风险既难度量又是二元的，结果就是机构干脆不来。

## How It Works | 机制怎么运转

要让裁决保险成立，需要三件目前都还缺的基础设施：

1. **可度量的风险定价** — 保险需要费率，费率需要历史违约率。这要求有**结构化的争议历史库**：多少合约、多少争议、多少判错、损失多少。目前这些数据散落在推特和新闻里，没有人系统化地维护。
2. **客观的触发条件** — "判错了"本身需要被裁决。**谁来裁决裁决？** 这是个递归问题，需要一个独立于原裁决方的仲裁层。
3. **资本方** — 有人愿意承接这个风险。前提是 (1) 和 (2) 成立，否则无法定价。

**三件事里，(1) 是唯一可以由第三方独立完成的** —— 这也是为什么"争议历史的结构化归档"是这条链上最先该被做的一环。

## Concrete Example | 具体例子

对照传统金融，这个缺口的性质就很清楚：

| | 传统清算 | 事件市场现状 |
|---|---|---|
| 对手方违约 | 违约瀑布逐层吸收（见 [[clearinghouse]]） | 全额抵押，不会违约 ✓ |
| **结算判错** | 几乎不发生（结算价可观测） | **频发，且无任何吸收机制** ✗ |

**全额抵押解决了"对方赔不起"，但完全没有解决"判错了"。**

而判错的频率并不低：2025–2026 年公开的重大裁决争议按年计频发，单起涉及金额从数百万到 $215M 量级。**这是一个已被验证有需求、但供给为零的市场。**

## Common Misconceptions | 常见误解

- **误解一："全额抵押已经保证安全了。"** 全额抵押保证的是"有钱可赔"，不保证"赔给对的人"。
- **误解二："平台会自己兜底。"** Ukraine 案的先例是不兜。**做决策时应默认零赔付。**
- **误解三："这个风险太主观，没法保。"** 信用违约、地震、政治风险都曾被认为不可保。**可保性的前提是有结构化的历史数据和客观的触发条件** —— 缺的是这两样，不是保险原理。

## In Practice | 实战里怎么用

在裁决保险出现之前，用户只能自己做替代性风控：

1. **把裁决风险计入仓位上限** —— 按 [[resolution-risk]] 的四项来源打分，分低的合约直接降仓。
2. **按预言机/裁决方设集中度桶** —— 同一裁决机制下的所有头寸算一个风险桶。
3. **避开语义分低 + 规模大的组合** —— 这是攻击性价比最高的象限（攻击成本固定，收益随规模增长）。
4. **临近裁决日主动降仓** —— 争议风险集中在这个窗口。

**如果你在建这个行业的基础设施：结构化的争议历史库是这条链上最先该被做、也最容易被独立完成的一环。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说裁决保险是'需求已验证、供给为零'的市场？
  A: 多起事件证明用户承担了判错损失且零追索；但缺少结构化争议历史、客观触发条件和资本方，供给尚未出现。
- Q: 全额抵押解决了什么、没解决什么？
  A: 解决了'对方赔不起'（对手方违约），完全没解决'判错了'（结算判定错误）。
- Q: 让裁决保险成立需要哪三件基础设施？哪一件可由第三方独立完成？
  A: 可度量的风险定价（争议历史库）、客观的触发条件（独立仲裁层）、资本方。争议历史库可由第三方独立完成。


## Sources

<!-- timeline -->

## Timeline

- **2026-08-26** — 手写创建 (补任务清单缺口; 教科书级概念, 行内一手引用待 researcher 回填)。
- **2026-08-27** — 语义关联层判断 (Claude seed, 待 Irene 复核): 前置 = resolution-risk; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
