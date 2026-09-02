---
id: "concept:spread"
type: concept
title: Spread
title_zh: 买卖价差
title_en: Spread
aliases:
  - 买卖价差
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
related: []
prerequisites:
  - "concept:bid"
  - "concept:ask"
import_origin: xlsx-learning-map+manual
import_category: 市场微观结构
---
# Spread | 买卖价差

## Executive Definition / Chinese Explanation | 定义与解释

**Spread | 买卖价差** = 最优卖价减最优买价。它是你为"立刻成交"支付的价格。

价差不是平台在坑你，它是做市商为承担两种成本收的费：**存货风险**（接了单之后价格反向跑）和**逆向选择**（跟你成交的人可能知道你不知道的事）。

## Why This Matters | 为什么重要

价差是**衡量一个市场健不健康最快的单一指标**，也是所有交易成本里最容易被忽略的一项 —— 因为它不出现在手续费账单上。

事件合约的价格本身就在 0 到 1 之间，所以价差要看**相对值**：0.63 的合约上 2 分价差 = 3.2% 的往返成本，比绝大多数平台的手续费高一个数量级。

## How It Works | 机制怎么运转

价差由三样东西决定，缺一不可：

1. **存货成本** — 做市商接下单后要多久、多大代价才能对冲掉？没有对冲工具的长尾事件，价差必然宽。
2. **逆向选择风险** — 这个市场里有多少人可能比做市商知道得多？内幕信息越可能存在，价差越宽。
3. **竞争** — 有几家做市商在抢同一个盘口？只有一家时，价差里含垄断租金。

**所以价差宽窄不是"平台良心"问题，而是这三个变量的读数。** 想压窄价差，得从这三处下手，光靠补贴只能撑一时。

## Concrete Example | 具体例子

同一时刻，三类事件合约的典型价差：

| 合约 | 中间价 | 价差 | 相对成本 |
|---|---|---|---|
| 美国大选结果（高关注、高流动） | 0.63 | 0.01 | 1.6% |
| 美联储议息（有 CME 期货可对冲） | 0.71 | 0.01–0.02 | 1.4–2.8% |
| 某小国选举（长尾、无对冲工具） | 0.40 | 0.08 | 20% |

第三行才是事件市场的真实常态。**它的价差宽，不是因为没人管，而是因为做市商既对冲不掉，也判断不了对手方是不是当地知情人。**

## Common Misconceptions | 常见误解

- **误解一："零手续费 = 免费交易。"** 价差就是费用，而且通常比手续费高得多。2026 年以前 Polymarket 长期零手续费，但真实交易成本从来不是零。
- **误解二："价差窄说明平台好。"** 也可能是补贴堆出来的。补贴一停就回到真实水平 —— 判断时要看**没有激励时**的价差。
- **误解三："价差是固定的。"** 它在消息前后、临近裁决时会剧烈变化，恰恰在你最想交易的时刻最宽。

## In Practice | 实战里怎么用

比较两个平台的真实成本，别看费率表，做这件事：

1. 挑**同一个事件**在两个平台上的合约。
2. 在同一时刻记录两边的 `bid / ask`。
3. 算 `(ask − bid) / mid`，再加上各自的手续费。
4. **重复采样一周，特别记录重大消息发生后 5 分钟的读数。**

第 4 步是关键。平静时的价差谁都好看，压力下的价差才是你真实要付的。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 价差补偿了做市商的哪两类成本？
  A: 存货风险（成交后价格反向）和逆向选择（对手方可能有信息优势）。
- Q: 为什么长尾事件合约的价差必然更宽？
  A: 做市商既没有对冲工具消化存货，又更可能面对本地知情人，两类成本同时上升。
- Q: 怎样公平比较两个平台的真实交易成本？
  A: 同一事件同一时刻采样双方 bid/ask，算相对价差再加手续费，并特别采集消息冲击后的读数。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
