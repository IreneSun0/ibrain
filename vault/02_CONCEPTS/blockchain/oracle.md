---
id: "concept:oracle"
type: concept
title: Oracle
title_zh: 预言机/外部事实输入层
title_en: Oracle
aliases:
  - 预言机
status: reviewed
importance: tier-1
domains:
  - blockchain
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
  - id: "protocol:chainlink"
    rel: instantiated-by
    note: 价格类结算主流选择; Polymarket 2026 起价格市场采用
  - id: "protocol:pyth-network"
    rel: instantiated-by
    note: 第一方金融数据 oracle (交易公司/交易所直发)
  - id: "protocol:winklink"
    rel: instantiated-by
    note: TRON 生态 oracle
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Oracle | 预言机/外部事实输入层

## Executive Definition / Chinese Explanation | 定义与解释

**Oracle | 预言机** = 把链外的事实送进链上合约的那个机制。

链本身不知道任何链外的事：不知道 BTC 的价格，不知道谁赢了选举，不知道哈梅内伊是否还在任。**必须有人告诉它。** 那个"人"就是预言机 —— 也是整个链上系统的**信任奇点**。

## Why This Matters | 为什么重要

这是事件市场最重要的一个概念，因为它是**唯一一个信任无法被消除、只能被转移的位置**。

- 合约可以审计 → 代码风险可控。
- 抵押可以链上验证 → 托管风险可控。
- 撮合可以链上化 → 撮合风险可控。
- **"这件事发生了吗" —— 链自己永远不知道。**

**去中心化把信任从平台转移到了预言机，没有消除它。** 一句话概括：

> **合约的诚实上限 = 预言机的诚实下限。**

## How It Works | 机制怎么运转

按输入类型分两类，成熟度天差地别：

| 类型 | 输入 | 机制 | 成熟度 |
|---|---|---|---|
| **价格类** | 可量化、有权威源 | 多源聚合、中位数、偏离阈值 | **较成熟** |
| **事件类** | 需要解释的命题 | 提议-挑战-投票，或人工判定 | **未解** |

**行业正在按这条线分流**：[[polymarket]] 自 2025-09 起把价格类合约的裁决改走 [[chainlink]]，**完全绕开人工投票**；需要解释的事件仍走 [[uma]] 的乐观预言机或平台内部团队。

**这个分流本身就是行业的判断：能自动化的部分不要留给人和投票。** 剩下不能自动化的那部分，才是真正的未解难题。

## Concrete Example | 具体例子

乐观预言机（optimistic oracle）的工作流程，以及它每一步的攻击面：

```
1. 有人提议结果 + 押金        ← 提议者可能说谎
2. 挑战窗口                   ← 小盘无人挑战 → 错误静默通过
3. 有争议 → 代币持有人投票     ← 投票权可购买
4. 终裁执行                   ← 链上不可逆
```

**三个攻击面在 2025–2026 年全部被兑现**（见 [[case-uma-dispute-trilogy]]）：
- **投票权可买** —— Ukraine 矿产协议案：单一行为人 3 个账户投 5M UMA（约 25% 投票权），把未发生的事裁成 Yes，$7M 市场，**拒绝退款**。
- **语义缝隙** —— Zelenskyy 西装案，影响交易至 $215M 量级。
- **小盘挑战不足** —— Clavicular 案，$16.46M 终身成交，两轮拉锯后维持原判。

**注意：这三条不是 bug，是这类设计的固有权衡。**

## Common Misconceptions | 常见误解

- **误解一："多个数据源就安全。"** 多源解决**单点故障**，不解决**治理攻击**。投票机制被俘获时，数据源再多也没用。
- **误解二："预言机是技术组件。"** 它主要是**经济与治理机制**。技术上一切正常，结果照样可以是错的。
- **误解三："预言机只是数据管道。"** 对价格类接近如此；对事件类，它在做**判断**，而判断可以被影响。

## In Practice | 实战里怎么用

评估一个预言机，算一道题：

```
攻击成本 = 获得关键投票权/影响力所需的成本（含滑点与价格冲击）
攻击收益 = 可被这次裁决影响的最大市场规模 × 可获取比例
```

**收益 > 成本 → 这个市场可攻击。与人品无关，是数学。**

再补三项检查：
1. **投票权/影响力的集中度**（前 10 地址占比）。
2. **历史上有没有已兑现的攻击，平台如何处理**（赔了还是没赔）。
3. **是否已按合约类型分流**（价格类走自动化）—— 这是当前最实际的缓解手段。

**并且：把同一预言机下的所有头寸算作一个集中度桶**（见 [[concentration-risk]]）。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 为什么说预言机是链上系统的信任奇点？
  A: 合约、抵押、撮合的风险都可控，但'这件事发生了吗'链自己永远不知道，必须有人告诉它 —— 信任只能被转移，不能被消除。
- Q: 行业按什么标准把预言机分流？说明了什么判断？
  A: 按输入是否可量化：价格类走自动化喂价，需解释的事件类走乐观预言机或人工。判断是：能自动化的部分不要留给人和投票。
- Q: 乐观预言机的三个攻击面是什么？
  A: 提议者可能说谎、小盘无人挑战使错误静默通过、争议投票的投票权可购买。三者在 2025-2026 年全部被真实兑现。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = smart-contract; typed 关系 3 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
