---
id: "protocol:ethereum"
type: protocol-network
title: Ethereum
title_zh: 以太坊
aliases:
  - ETH
status: reviewed
importance: tier-2
domains:
  - blockchain
tags:
  - protocol-network
created: 2026-08-27
updated: 2026-08-31
last_verified: 2026-08-26
review_after: 2027-02-26
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources:
  - "report:2026-08-26-cex-lineage"
related: []
---
# Ethereum

## Executive Summary

最大的智能合约平台，事件市场所有技术标准的**发源地**：ERC-20、ERC-1155、conditional tokens、EVM 字节码 —— 现在跑在各条链上的东西，标准都是这里定的。

**它自己反而很少直接承载事件市场**，原因只有一个：[[gas]] 太贵。

## What It Actually Is | 它到底是什么

对事件市场，以太坊的实际角色是**三重的**：

| 角色 | 说明 |
|---|---|
| **标准制定者** | [[erc-1155]]、[[erc-20]]、CTF —— 结果代币的表示方式来自这里 |
| **安全锚** | Rollup 类 L2 的最终性来自它（见 [[layer-2]]） |
| **价值枢纽** | USDC/USDT 的主要发行与流通地之一，资金从这里出发 |

**但它不是执行层**：一个 $50 的事件头寸在 L1 上光 gas 就要 20%（见 [[block]]）。所以主流事件市场把执行放在 L2 或侧链，把以太坊当作资金的起点和标准的来源。

## How It Works | 运作方式

以太坊 2022 年从 PoW 转为 [[proof-of-stake|PoS]]，并引入了**明确最终性**：区块在达到一定条件后于协议层面不可回滚。

**这一点对事件市场很关键**：结算的确定性必须早于资金的可提取性（见 [[double-spending]]）。有明确最终性的链，这个风险窗口小得多。

其扩容路线是 **rollup-centric**：L1 只做结算与数据可用性，执行交给 L2。事件市场正好落在这条路线的目标场景里 —— 高频、小额、成本敏感。

## Position in the Market | 它在市场里的位置

在事件市场的价值链里，以太坊是**底座而非舞台**。

它的护城河不是性能，是：
- **开发者与工具生态** —— 钱包、浏览器、审计工具、合约库全部围绕 EVM；
- **稳定币深度** —— 资金进出的默认通道；
- **安全预算** —— 质押规模决定了 rollup 能继承多强的保证。

**"EVM 兼容"这四个字是它最大的输出**：即便交易发生在别的链上，规则仍是它写的（见 [[ethereum-virtual-machine]]）。

## What Could Break It | 什么会让它出问题

- **L1 成本** —— 使小额事件头寸不经济；这是结构性的，不是暂时的。
- **L2 碎片化** —— 资产散落在多条 rollup 上，跨链要经过桥（见 [[bridge]]）。
- **质押集中度** —— 大型质押服务商与交易所代持形成隐性集中（见 [[proof-of-stake]]）。
- **合约不可变性的两面** —— 部署即终局，bug 可能无法修复（见 [[solidity]]）。

## What To Watch | 该盯什么

- **L2 的最终性与提现窗口** —— 决定你的钱多久能真正动。
- **稳定币在 L1 与各 L2 的分布** —— 资金实际在哪条链上。
- **新的结果代币标准** —— 标准变化会传导到所有 EVM 链上的事件市场。
