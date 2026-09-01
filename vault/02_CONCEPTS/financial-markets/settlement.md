---
id: "concept:settlement"
type: concept
title: Settlement
title_zh: 结算/交割
title_en: Settlement
aliases:
  - 结算
status: reviewed
importance: tier-1
domains:
  - financial-markets
  - institutional-risk
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
related: []
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 交易后基础设施
---
# Settlement | 结算/交割

## Executive Definition / Chinese Explanation | 定义与解释

**Settlement | 结算 / 交割** = 钱和资产真正易手、义务彻底消灭的那一刻。在此之前一切都还是"应收应付"，在此之后交易才算真的结束。

事件合约的结算有一个价格类衍生品没有的额外步骤：**先要判定"那件事到底发生了没有"**。这一步叫 resolution（裁决），它才是事件市场真正的风险所在。

## Why This Matters | 为什么重要

**结算是唯一一个"错了无法撤销"的环节。** 前面所有环节出错都还有补救余地，钱一旦按错误结果分出去，实践中基本追不回来。

这也是为什么事件市场的核心竞争力不在撮合速度，而在**裁决质量**：合约条款写得够不够严密、数据源够不够权威、有争议时有没有可信的申诉路径。撮合引擎可以买，裁决可信度买不到。

## How It Works | 机制怎么运转

事件合约的结算链条比价格衍生品多两环：

| 步骤 | 价格类衍生品 | 事件合约 |
|---|---|---|
| 1 | 到期 | 到期 |
| 2 | 读取结算价（可观测） | **判定事件是否发生（需解释）** |
| 3 | — | **争议 / 申诉窗口** |
| 4 | 计算盈亏 | 计算盈亏（$1 或 $0） |
| 5 | 转移资金 | 转移资金 |

第 2、3 步就是全部难点。价格是客观可读的数字；"某事是否发生"要靠合约文本 + 指定数据源 + 人的解释，**三者中任何一个有歧义，结算就有争议**。

## Concrete Example | 具体例子

**Kalshi 的 Khamenei 合约**是这类风险的教科书案例：合约问"哈梅内伊是否会在某日期前卸任伊朗最高领袖"。真实世界的状态并不总能被清晰归入"是/否" —— 什么算"卸任"？由谁宣布才算数？信息不透明的政权尤其如此。合约文本必须提前把这些边界写死，否则裁决就变成解释之争。

**UMA 的争议三部曲**则展示了另一种失败模式：Polymarket 使用 UMA 的乐观预言机做裁决，而 UMA 的争议解决靠代币持有者投票。**当投票权可以被购买时，"事实"就变成了可以被资本影响的东西** —— 曾发生过持有大量投票权的一方推动出与多数人理解相悖的裁决结果的争议。

两个案例指向同一个结论：**裁决是事件市场的攻击面**。

## Common Misconceptions | 常见误解

- **误解一："结算就是转账。"** 转账是最后一步，也是最简单的一步。真正的难点在它前面的判定与争议。
- **误解二："上链就客观了。"** 链保证的是"记录不可篡改"，不保证"输入是对的"。**链上写着的错误结果，同样不可篡改。**
- **误解三："权威数据源能解决一切。"** 数据源会改口径、会停更、会在关键时刻不可用。合约必须预先规定"主数据源失效时怎么办"，否则就是裸奔。

## In Practice | 实战里怎么用

看一份事件合约，只看这五行就能判断它靠不靠谱：

1. **结算触发条件**是否写成了可机械判定的句子（有明确主体、明确阈值、明确时点）？
2. **指定数据源**是谁？如果它停更或改口径，备用方案是什么？
3. **争议窗口**有多长？争议期间资金是锁定还是已分配？
4. **最终裁定权**在谁手上？是平台、委员会，还是代币投票？
5. **历史争议记录**能不能查到？平台肯不肯公开自己判错过的案例？

**第 5 条最能看出一个平台的诚意。** 敢公开争议历史的，通常裁决质量也更经得起看。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 事件合约的结算比价格衍生品多了哪两步？
  A: 多了'判定事件是否发生'（裁决）和'争议/申诉窗口'两步，这两步是事件市场的主要风险来源。
- Q: 为什么说'上链'不能解决裁决问题？
  A: 链保证记录不可篡改，不保证输入正确。错误的裁决结果上链后同样不可篡改，反而更难纠正。
- Q: UMA 争议案例暴露了哪种结构性风险？
  A: 当裁决靠代币投票且投票权可购买时，'事实'成为资本可影响的对象，裁决的可信度取决于投票权分布而非证据。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 交易后基础设施)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
