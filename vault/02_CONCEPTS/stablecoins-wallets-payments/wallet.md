---
id: "concept:wallet"
type: concept
title: Wallet
title_zh: 钱包
title_en: Wallet
aliases:
  - 钱包
status: reviewed
importance: tier-2
domains:
  - stablecoins-wallets-payments
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
  - id: "concept:distribution"
    rel: mechanism-of
    note: 钱包正在成为 crypto 的金融分发入口
prerequisites:
  - "concept:private-key"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Wallet | 钱包

## Executive Definition / Chinese Explanation | 定义与解释

**Wallet | 钱包** = 管理[[private-key|私钥]]、构造并签名交易的软件或硬件。

**它不"装"钱** —— 资产始终在链上，钱包只是你控制它们的钥匙串。这个措辞上的误解，导致了大量真实损失。

## Why This Matters | 为什么重要

钱包在事件市场里的战略位置远超"工具"：**它是分发入口。**

一个拥有数亿用户的钱包，把预测市场嵌进自己的界面，等于一夜之间给某个场馆送去了巨大的流量 —— **而用户甚至不需要知道自己在用哪个场馆**（见 [[distribution]]）。

**这条链路已经在真实发生**：主流交易所钱包内嵌的预测市场由第三方场馆驱动，用户一键进入、免 gas。

**含义**：**分发权正在从场馆转移到钱包。** 谁掌握入口，谁就有议价权。

## How It Works | 机制怎么运转

钱包的三种形态，托管性质完全不同：

| 形态 | 私钥在谁手里 | 便利 | 风险 |
|---|---|---|---|
| **托管钱包**（交易所） | 平台 | 最高 | 平台可挪用 |
| **自托管热钱包** | 你（联网设备） | 高 | 设备被攻破 |
| **硬件钱包** | 你（离线） | 低 | 物理丢失 |

**"内嵌预测市场"的钱包通常是托管或半托管的** —— 便利来自于平台替你管理密钥和 gas。

**这是一个真实的取舍，不是缺陷**：但用户应该知道，一键免 gas 的代价通常是把托管交回给平台。

## Concrete Example | 具体例子

同一个事件市场头寸，三种钱包路径的风险差异：

| 路径 | 你控制私钥吗 | 平台倒闭时 | gas |
|---|---|---|---|
| 交易所内嵌 | **否** | 进破产财产 | 平台代付 |
| 自托管 + 直连合约 | **是** | **合约照常结算** | 你付 |
| 硬件钱包 + 直连 | **是（离线）** | **合约照常结算** | 你付 |

**第一行的便利是真实的，风险也是真实的。**

**判断标准很简单**：如果你的头寸规模超过你能承受损失的额度，就不该走托管路径 —— 无论界面多方便。

## Common Misconceptions | 常见误解

- **误解一："钱包里装着我的币。"** 币在链上，钱包只有私钥。**换个钱包导入助记词，资产照样在。**
- **误解二："内嵌的预测市场就是钱包自己做的。"** 通常由第三方场馆驱动，规则与裁决都是那家的。**出争议要找的是场馆，不是钱包。**
- **误解三："托管钱包更安全因为有客服。"** 客服解决的是操作问题；平台破产时客服帮不了你。

## In Practice | 实战里怎么用

按头寸规模选择钱包路径：

1. **小额、高频** → 托管或内嵌钱包，便利优先。
2. **中额** → 自托管热钱包，定期清理授权（见 [[erc-20]]）。
3. **大额** → 硬件钱包 + 地址分层（见 [[private-key]]）。

**再问一条内嵌场景专属的问题**：**这个内嵌的市场由谁驱动、规则是谁的、争议找谁？** 界面提供方和产品发行方常常不是同一家。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 钱包到底管理的是什么？
  A: 私钥，不是资产。资产始终在链上，钱包只是控制它们的钥匙串。
- Q: 为什么说钱包在事件市场里是战略位置？
  A: 它是分发入口 —— 内嵌预测市场可以把巨大流量一夜送给某个场馆，分发权正从场馆转移到钱包。
- Q: 使用内嵌预测市场时该额外问什么？
  A: 这个市场由谁驱动、规则与裁决是谁的、出争议找谁 —— 界面提供方与产品发行方常常不是同一家。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
