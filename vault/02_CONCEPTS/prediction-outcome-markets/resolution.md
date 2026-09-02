---
id: "concept:resolution"
type: concept
title: Resolution
title_zh: 结果判定/裁决
title_en: Resolution
aliases:
  - 结果判定
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
  - "source:2026-08-26-polymarket-resolution"
related: []
prerequisites:
  - "concept:event-contract"
import_origin: xlsx-learning-map+manual
import_category: 预测市场
---
# Resolution | 结果判定/裁决

## Executive Definition / Chinese Explanation | 定义与解释

**Resolution | 裁决** = 判定"这个事件到底发生了没有"，从而决定合约按 $1 还是 $0 结算的那个动作。

它是事件市场独有的一步 —— 传统衍生品直接读结算价，事件合约必须先**做出判断**。而任何需要判断的地方，就有可能判错、可能被操纵、可能被争议。

## Why This Matters | 为什么重要

**裁决是事件市场唯一一个"错了就无法撤销"的环节。** 撮合出错可以撤单重来，行情出错可以修正，钱一旦按错误结果分给了赢家，实践中基本追不回来。

这也是为什么"谁来裁决"是这个行业真正的基础设施竞争位。撮合引擎可以买，流动性可以补贴，**裁决可信度买不到，只能靠时间和公开的争议记录积累。**

## How It Works | 机制怎么运转

目前有三种裁决架构，各有各的失效模式：

| 架构 | 代表 | 怎么判 | 主要失效模式 |
|---|---|---|---|
| **中心化团队 + 申诉委员会** | [[kalshi]] | 内部 markets team 判定；条款钉死 Source Agencies 与判定日；异议走 Rule 7.1 送 Outcome Review Committee，24 小时终局 | 平台自身的利益冲突；语义漏洞 |
| **乐观预言机 + 代币投票** | [[uma]]（[[polymarket]] 离岸端） | 有人提议结果 → 挑战窗口 → 有争议则代币持有人投票终裁 | **投票权可购买**；小盘挑战激励不足 |
| **自动化数据喂价** | [[chainlink]]（Polymarket 价格类自 2025-09 起） | 直接读取权威价格源，无需人判断 | 只适用于可量化标的；数据源本身失效 |

部分平台正把可量化事件与需要解释的事件分开处理：价格类合约可以自动化，主观类合约仍依赖人工、委员会或投票机制。

## Concrete Example | 具体例子

**同一个品牌，两套裁决法学** —— [[polymarket]] 的现状最能说明这件事的复杂度：

- **离岸主平台** → [[uma]] 乐观预言机裁决（价格类合约自 2025-09 起改走 [[chainlink]]）。
- **美国 QCX（DCM）** → DCM 自认证合约，走监管框架内的裁决流程，**完全不用 UMA**。

对用户的实际含义：**"我在 Polymarket 上交易"这句话已经不足以说明你承担什么裁决风险了。** 你必须知道自己在哪一侧，因为两侧的争议机制、终裁权、和救济路径完全不同。

这就是为什么裁决方法学需要按平台、按合约类别分轨建档（见 [[settlement-methodology]]）。

## Common Misconceptions | 常见误解

- **误解一："上链就客观了。"** 链保证记录不可篡改，不保证输入正确。**错误的裁决结果上链后同样不可篡改，反而更难纠正。**
- **误解二："去中心化投票比公司裁决公正。"** 取决于投票权分布。当投票权可以购买时，"事实"就变成了资本可以影响的东西（见 [[case-uma-dispute-trilogy]] Case 1）。
- **误解三："裁决争议是罕见的尾部事件。"** 不是。2025–2026 年公开的重大争议按年计频发，涉及金额从数百万到上亿美元。**它是常态风险，不是黑天鹅。**

## In Practice | 实战里怎么用

交易任何事件合约之前，先把裁决链条问清楚 —— 五个问题：

1. **谁做初判？** 平台团队、预言机提议者，还是自动喂价？
2. **挑战/争议窗口多长？** 期间资金是锁定还是已分配？
3. **谁有终裁权？** 委员会、代币投票，还是监管框架内的仲裁？
4. **终裁方有没有利益冲突？** 平台自己既做市又裁决吗？投票权集中在谁手里？
5. **历史争议记录公开吗？** 判错过几次，怎么处理的？

**第 5 条是最快的可信度筛子。** 拿不出争议历史的平台，要么没经历过压力测试，要么不想让你看见。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说裁决是事件市场唯一'错了无法撤销'的环节？
  A: 钱一旦按错误结果分给赢家，实践中追不回来；其他环节出错都还有补救余地。
- Q: 三种裁决架构各自的主要失效模式是什么？
  A: 中心化团队：利益冲突与语义漏洞；乐观预言机+代币投票：投票权可购买、小盘挑战激励不足；自动化喂价：只适用可量化标的且依赖数据源本身。
- Q: 为什么'上链'不能解决裁决问题？
  A: 链只保证记录不可篡改，不保证输入正确；错误结果上链后更难纠正。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
- [[src-2026-08-26-polymarket-resolution]] — <https://docs.polymarket.com/concepts/resolution>
