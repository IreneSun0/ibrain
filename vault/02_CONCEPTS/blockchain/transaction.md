---
id: "concept:transaction"
type: concept
title: Transaction
title_zh: 交易/状态更新指令
title_en: Transaction
aliases:
  - 交易
status: reviewed
importance: tier-2
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
  - id: "concept:block"
    rel: component-of
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Transaction | 交易/状态更新指令

## Executive Definition / Chinese Explanation | 定义与解释

**Transaction | 交易（链上）** = 一条由私钥签名、提交给网络、会改变链上状态的指令。

它不只是转账 —— 授权、下单、铸造、领取赔付，在链上全都是交易。**每一条都要付 [[gas]]，每一条都不可撤销。**

## Why This Matters | 为什么重要

"不可撤销"这四个字是链上世界与传统金融最大的操作差异。

传统银行转错账可以追回、可以撤销、可以申诉；**链上交易一经确认，没有任何人能撤回它** —— 包括链的开发者。

**对事件市场的含义**：
- **好的一面**：结算一旦执行就是终局，没有对手方可以反悔。
- **坏的一面**：**判错了也一样不可撤销**（见 [[resolution]]）。错误的裁决结果上链后，纠错窗口已经关闭。

## How It Works | 机制怎么运转

一笔交易的生命周期：

```
构造 → 签名 → 广播到 mempool → 被打包进区块 → 确认 → 最终性
                    ↑                                    ↑
              这里可能被看见并抢跑                  这里才不可逆
```

**两个关键窗口**：
1. **mempool 阶段** —— 你的交易公开可见但尚未执行。**大额事件市场订单在这里可能被抢跑**（见 [[execution-risk]]）。
2. **确认到最终性之间** —— 理论上仍可能因重组而回滚（见 [[consensus]]）。

**平台设置提现等待期，正是为了跨过第二个窗口。**

## Concrete Example | 具体例子

在链上事件市场做一笔完整交易，实际发生的链上操作：

```
1. approve  授权合约动用你的 USDC     ← 一笔交易, 付 gas
2. deposit  存入抵押品                ← 一笔交易, 付 gas
3. trade    成交 (若撮合在链下, 这步可能不上链)
4. redeem   判定后领取赔付            ← 一笔交易, 付 gas
```

**至少三笔交易，三次 gas。** 对一个 $50 的头寸，这可能占到本金的 20% 以上。

**这就是为什么事件市场普遍走 hybrid 架构**（见 [[hybrid-exchange-architecture]]）：把高频的撮合放链下，只有资金进出上链 —— **交易笔数从"每次下单一笔"降到"每个头寸两三笔"。**

## Common Misconceptions | 常见误解

- **误解一："交易失败就不用付钱。"** 失败的交易通常仍消耗 gas —— 网络已经做了计算。
- **误解二："交易一广播就完成了。"** 广播只是进入候选池；被打包、被确认、达到最终性是三件事。
- **误解三："链上交易是私密的。"** mempool 阶段完全公开 —— 这正是抢跑的技术前提。

## In Practice | 实战里怎么用

在链上事件市场操作时的三条实用纪律：

1. **合并操作** —— 能批量就批量（[[erc-1155]] 支持批量转移，正是为省 gas）。
2. **避开拥堵** —— 判定后领取赔付不必抢在第一分钟，等 gas 回落。
3. **大额拆分或走私密路径** —— mempool 可见意味着大单会被看到。

**再加一条心理准备**：**每一次签名都是终局。** 签之前确认你签的是什么，而不是签完再看。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 链上交易与传统银行转账最大的操作差异是什么？
  A: 不可撤销 —— 一经确认没有任何人能撤回，包括链的开发者。
- Q: 交易生命周期里的两个关键风险窗口是什么？
  A: mempool 阶段（公开可见但未执行，可能被抢跑）和确认到最终性之间（理论上仍可能因重组回滚）。
- Q: 为什么事件市场普遍走 hybrid 架构？
  A: 把高频撮合放链下，只有资金进出上链，交易笔数从每次下单一笔降到每个头寸两三笔，大幅节省 gas。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = 无硬前置 (判断过的空); typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
