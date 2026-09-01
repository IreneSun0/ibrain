---
id: "concept:futures-contract"
type: concept
title: Futures
title_zh: 期货
title_en: Futures
aliases:
  - Futures
  - 期货
status: reviewed
importance: tier-2
domains:
  - derivatives
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
  - "source:2026-08-26-cme-group-introduction-to-futures-html"
related:
  - id: "concept:forward-contract"
    rel: special-case-of
    note: "标准化+交易所交易+清算体系管理保证金, 是与 forward 的本质区别"
prerequisites:
  - "concept:forward-contract"
import_origin: xlsx-learning-map+manual
import_category: 衍生品
---
# Futures | 期货

## Executive Definition / Chinese Explanation | 定义与解释

**Futures Contract | 期货合约** = 在交易所标准化交易、约定未来某时点按约定价格交割的合约。

关键词是**标准化**和**交易所**：条款统一（数量、品质、交割日）、有中央对手方担保、可随时反向平仓。这三条把一份私人约定变成了可流通的金融工具。

## Why This Matters | 为什么重要

期货是理解事件合约的**最近参照物**：两者都是"现在定价、未来结算"的衍生品，都在受监管交易所交易，都有清算机构。

**差别只在标的**：期货的结算价是可观测的市场价格，事件合约的结算需要判定一个命题是否成立（见 [[event-contract]]）。

**美国把事件合约划归 CFTC 而非博彩监管，走的正是"它是期货家族一员"这条论证。** 理解期货，就理解了这条法律路径的地基。

## How It Works | 机制怎么运转

期货的三个核心机制：

1. **标准化条款** —— 合约乘数、交割月、最小变动单位全部固定，因此可互换、可净额。
2. **保证金 + 逐日盯市** —— 不必付全款，每日按结算价结清盈亏（见 [[margin]]）。
3. **中央对手方** —— 清算所做合约更替，你只面对它（见 [[clearinghouse]]）。

**绝大多数期货不实物交割** —— 到期前反向平仓，或现金结算。交割机制的存在是为了把期货价格锚定到现货，而不是为了真的交货。

## Concrete Example | 具体例子

同一个"押注美联储降息"的需求，期货与事件合约的对照：

| | CME 联邦基金期货 | 事件合约 |
|---|---|---|
| 标的 | 有效联邦基金利率（可观测） | "是否降息"（需判定） |
| 支付 | 线性 | 台阶（$1 / $0） |
| 抵押 | 保证金（5–15%） | 通常全额 |
| 最坏情况 | 理论上很大 | 开仓即知 |
| 结算争议 | 极罕见 | **常态风险** |

**最后一行是全部差别所在。** 期货的结算价来自公开市场，不需要解释；事件合约的结算需要有人做判断，而判断可能出错、可能被操纵（见 [[resolution-risk]]）。

## Common Misconceptions | 常见误解

- **误解一："期货就是高杠杆赌博。"** 杠杆来自保证金制度，不是期货本身。期货的原始功能是对冲。
- **误解二："买期货就要准备接货。"** 绝大多数在到期前平仓；很多品种本身就是现金结算。
- **误解三："事件合约和期货完全不同。"** 结构上高度同源 —— 不同只在标的是价格还是命题。这一点是它法律地位的基础。

## In Practice | 实战里怎么用

用期货当参照系去看任何一个事件合约，问四件事：

1. **标的是可观测的还是需判定的？** —— 这决定了有没有裁决风险。
2. **抵押是保证金还是全额？** —— 决定资金效率与爆仓风险。
3. **有没有中央对手方？** —— 决定对手方风险怎么被吸收。
4. **结算价怎么来？** —— 期货来自市场，事件合约来自数据源加解释。

**答完这四问，你就知道这份合约比一份期货多承担了什么。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 期货的三个核心机制是什么？
  A: 标准化条款（可互换可净额）、保证金加逐日盯市、中央对手方合约更替。
- Q: 期货与事件合约的唯一结构性差别是什么？
  A: 标的：期货结算价是可观测的市场价格，事件合约需要判定一个命题是否成立，因而多出裁决风险。
- Q: 为什么理解期货对理解事件合约的法律地位很重要？
  A: 美国把事件合约划归 CFTC 而非博彩监管，论证正是'它属于期货/衍生品家族'。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-cme-group-introduction-to-futures-html]] — <https://www.cmegroup.com/education/courses/introduction-to-futures.html>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 衍生品)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = forward-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
