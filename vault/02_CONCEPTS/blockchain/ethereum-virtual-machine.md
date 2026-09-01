---
id: "concept:ethereum-virtual-machine"
type: concept
title: EVM
title_zh: 以太坊虚拟机
title_en: EVM
aliases:
  - EVM
  - Ethereum Virtual Machine
  - 以太坊虚拟机
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
  - id: "protocol:ethereum"
    rel: instantiated-by
    note: EVM 标准的母体; 众多兼容链复用其字节码与工具生态
prerequisites:
  - "concept:smart-contract"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# EVM | 以太坊虚拟机

## Executive Definition / Chinese Explanation | 定义与解释

**EVM (Ethereum Virtual Machine) | 以太坊虚拟机** = 执行[[smart-contract|智能合约]]字节码的运行环境。每个节点都跑同一个 EVM，因此对同一笔交易得到同一个结果 —— 这就是链上"确定性执行"的来源。

**EVM 已经成为事实标准**：大量非以太坊的链选择"EVM 兼容"，为的是直接复用现成的工具、钱包和合约。

## Why This Matters | 为什么重要

EVM 兼容性对事件市场是一个**分发问题**，不是技术偏好：

- 合约用 [[solidity|Solidity]] 写一次，可以部署到任何 EVM 链。
- 用户的钱包、区块浏览器、审计工具全部通用。
- **[[erc-1155]] 这类标准也随之通用** —— 结果代币在任何 EVM 链上都能被钱包识别（见 [[outcome-token]]）。

**这意味着一个事件市场协议可以低成本地铺到多条链上** —— 也意味着**碎片化更容易发生**（见 [[liquidity]]）。

**兼容性同时是扩张的加速器和流动性的稀释器。**

## How It Works | 机制怎么运转

EVM 的三个关键性质：

1. **确定性** —— 相同输入必得相同输出，否则节点无法达成共识。**因此合约里不能有真随机数、不能直接读外部数据**（那正是需要[[oracle|预言机]]的原因）。
2. **计量执行** —— 每个操作码有固定 gas 成本，跑得越久越贵（见 [[gas]]）。
3. **沙箱隔离** —— 合约只能访问链上状态，不能碰文件系统或网络。

**第 1 条直接解释了事件市场最核心的架构约束**：合约无法自己知道"选举结果是什么"，**这个信息必须由外部送进来 —— 于是预言机成为不可消除的信任点。**

## Concrete Example | 具体例子

EVM 的确定性要求如何塑造了事件市场的结构：

```
合约能做:  锁定抵押品 · 铸造结果代币 · 按给定结果分配资金
合约不能:  知道选举结果 · 判断新闻真假 · 访问任何链外数据
                    ↑
              必须由预言机送入
```

**这条边界不是实现限制，是共识的数学要求**：如果合约能读外部数据，不同节点在不同时刻读到的可能不同，共识就崩了。

**所以"链上事件市场"永远是"链上结算 + 链外判定"的组合** —— 判定这一环无法被密码学消除，只能被机制设计约束（见 [[oracle-risk]]）。

## Common Misconceptions | 常见误解

- **误解一："EVM 是以太坊专有的。"** 它已是跨链的事实标准，大量链选择兼容。
- **误解二："合约能自动获取现实信息。"** 不能 —— 确定性要求禁止它。所有外部数据必须由预言机推入。
- **误解三："EVM 兼容 = 安全性相同。"** 兼容的是执行环境，**不是共识安全**。同一份合约在不同链上的安全性天差地别（见 [[layer-1]]）。

## In Practice | 实战里怎么用

理解 EVM 的确定性约束，对判断事件市场产品有两个直接用处：

1. **任何声称"合约自动判定现实事件"的说法都是错的** —— 一定有一个外部输入点，找出它，那就是信任点。
2. **"EVM 兼容"不代表安全等价** —— 同一个协议部署在不同链上，你要分别评估那条链的共识安全（见 [[proof-of-stake]]）。

**一句话检验**：**这份合约的现实数据从哪里进来？** 答不出来说明你还没找到真正的风险所在。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: EVM 的确定性要求带来了什么核心约束？
  A: 合约不能有真随机数、不能直接读外部数据 —— 否则不同节点结果不同、共识崩溃。所以外部数据必须由预言机推入。
- Q: 为什么'链上事件市场'永远是'链上结算 + 链外判定'？
  A: 确定性要求禁止合约自己获取现实信息，判定这一环无法被密码学消除，只能被机制设计约束。
- Q: 'EVM 兼容'保证了什么、没保证什么？
  A: 保证了执行环境与工具生态通用；不保证共识安全 —— 同一份合约在不同链上的安全性可能天差地别。

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = smart-contract; typed 关系 1 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
