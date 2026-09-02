---
id: "concept:settlement-methodology"
type: concept
title: Settlement Methodology
title_zh: 结算方法论
title_en: Settlement Methodology
aliases:
  - 结算方法论
status: reviewed
importance: tier-2
domains:
  - prediction-outcome-markets
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
related:
  - id: "concept:settlement-rail"
    rel: see-also
    note: 规则链第四层「通过什么轨道支付」即结算轨选择
prerequisites:
  - "concept:resolution"
  - "concept:settlement"
---
# Settlement Methodology | 结算方法论

## Executive Definition / Chinese Explanation | 定义与解释

**Settlement Methodology | 结算方法学** = 一个平台把"事件发生了"变成"钱到账"的**完整规程**，而不只是"谁来判定"这一个问题。

它有五层，每一层都能单独出错：判定什么、按什么价格、在什么时点、走什么轨道、以及 —— 最被忽视的 —— **生效后发现判错了怎么办**。

## Why This Matters | 为什么重要

大多数关于事件市场的讨论只停在第一层（预言机/裁决方是谁），但**钱是从第五层出去的**。

一个平台可以有完美的裁决机制，却在"多结果盘部分结算的价格规则"或"判定到支付之间的时滞"上让你亏钱。**只问"谁裁决"，等于只检查了五分之一。**

## How It Works | 机制怎么运转

五层规程，逐层问：

| 层 | 问题 | 典型出错方式 |
|---|---|---|
| 1 **判定** | 事件发生了吗？ | 语义歧义、预言机被操纵 |
| 2 **价格** | 按什么价格结算？多结果盘部分结算怎么算？ | 部分结算规则不明 |
| 3 **时点** | 判定到支付之间隔多久？ | 时滞期间的敞口无人计量 |
| 4 **轨道** | 钱走哪条路？谁能冻结？ | 稳定币冻结、银行环节 |
| 5 **回滚** | 生效后发现判错了怎么办？ | **链上兑付不可逆 —— 技术上不存在回滚** |

**第 5 层是最关键的**：链上支付一旦执行不可撤销，意味着"纠错"的唯一防线被完全压缩到了**生效前的争议窗口**。争议窗口的长度和门槛，因此不是行政细节，而是整个方法学里最重要的参数。

## Concrete Example | 具体例子

**同一个品牌，两套方法学** —— [[polymarket]] 需要分轨维护：

| | 离岸主平台 | 美国 QCX（DCM） |
|---|---|---|
| 判定 | [[uma]] 乐观预言机（价格类 2025-09 起走 [[chainlink]]） | DCM 自认证合约流程 |
| 轨道 | Polygon 链上 USDC | 受监管清算 |
| 回滚 | 链上不可逆 | 监管框架内有救济路径 |

**[[kalshi]]** 则把方法学写进条款：Source Agencies + 判定日钉死，内部 markets team 判定，异议依 Rule 7.1 送 Outcome Review Committee，24 小时终局。Khamenei 案后还把一条 "death settlement rule" 补进 CFTC 备案（见 [[case-kalshi-khamenei-settlement]]）。

**结论：判定层的差异只是表面，五层加起来才是你真正承担的风险画像。**

## Common Misconceptions | 常见误解

- **误解一："结算方法学 = 预言机选型。"** 预言机只是第一层。价格规则、时滞、轨道、回滚各有独立风险。
- **误解二："同一个平台的方法学是统一的。"** 不一定 —— 同一品牌的不同法律实体可能用完全不同的方法学。
- **误解三："链上不可逆是优点。"** 对防篡改是优点，**对纠错是致命缺陷**。它把全部纠错能力压缩进了争议窗口。

## In Practice | 实战里怎么用

建立一张跨平台的方法学对照表，五行五列，每个平台一列：

```
              平台 A    平台 B    平台 C
判定方         ______    ______    ______
价格规则       ______    ______    ______
判定→支付时滞  ______    ______    ______
资金轨道       ______    ______    ______
争议窗口/回滚  ______    ______    ______
```

**填完这张表，你才第一次能说"我知道自己在哪个平台承担什么"。**

更进一步：把它做成结构化数据、跨平台可比 —— 这就是 settlement intelligence 这个词组的字面工程含义。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 结算方法学的五层分别是什么？
  A: 判定（事件是否发生）、价格（按什么价结算）、时点（判定到支付的时滞）、轨道（资金走哪条路、谁能冻结）、回滚（生效后发现判错怎么办）。
- Q: 为什么第五层（回滚）在链上市场特别关键？
  A: 链上兑付不可逆，技术上不存在回滚，唯一的纠错防线被压缩到生效前的争议窗口，因此争议窗口参数至关重要。
- Q: 为什么只问'谁来裁决'不够？
  A: 那只是五层里的第一层。价格规则、时滞、资金轨道、回滚机制各有独立的失效方式，钱是从第五层出去的。


## Sources
