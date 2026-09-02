---
id: "concept:custody"
type: concept
title: Custody
title_zh: 托管
title_en: Custody
aliases:
  - Custodian
  - 托管
  - 托管人
status: reviewed
importance: tier-1
domains:
  - crypto-market-structure
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
  - id: "org:fireblocks"
    rel: instantiated-by
    note: 机构 MPC 托管/结算基础设施
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: Crypto市场结构
---
# Custody | 托管

## Executive Definition / Chinese Explanation | 定义与解释

**Custody | 托管** = 谁实际持有资产、谁能移动它。

在加密语境里它归结为一个问题：**私钥在谁手上。** 界面上显示的余额是承诺，私钥才是控制权。

## Why This Matters | 为什么重要

托管是 FTX 类事故的**唯一根因**：用户以为钱在自己的账户里，实际上钱在平台的钱包里，平台可以随时挪用。

事件市场在这一点上做了一个真实的架构改进：**全额抵押的钱锁在链上合约里，平台没有私钥，无法挪用**（见 [[fully-collateralized-market]]）。这不是营销话术，是可以在链上验证的属性。

**但注意边界**：托管解决的是"钱会不会被卷走"，不解决"钱会不会被分给错的人"（裁决风险）。

## How It Works | 机制怎么运转

三种托管模型，控制权递减：

| 模型 | 私钥在谁手上 | 风险 |
|---|---|---|
| **自托管** | 你 | 你自己弄丢就没了 |
| **合约托管** | 没有人（代码执行） | 合约 bug；升级权限被滥用 |
| **第三方托管** | 持牌托管行 | 托管行信用；但有法律救济 |
| **平台托管** | 平台 | **平台可挪用 —— 这是最危险的一种** |

**关键追问：合约托管真的没有人能动吗？** 很多"链上托管"的合约带有升级权限或管理员密钥。**有升级权限的合约托管，实质上更接近平台托管。** 这是最常见的伪装。

## Concrete Example | 具体例子

检查"钱到底在哪"的实操路径：

- **[[polymarket]]** —— USDC 锁在 Polygon 上的条件代币合约里。任何人可以在区块浏览器上查到合约地址、余额、以及资金能否被单一地址转出。
- **[[kalshi]]** —— 链下 USD，但在 CFTC 持牌框架内，客户资金有法定的隔离要求（见 [[custody-segregation]]）。**用监管替代密码学。**
- **某离岸平台** —— 界面显示余额，但钱在平台的热钱包里，与运营资金混同。**这种情况从界面上完全看不出来。**

**前两种都能被独立验证（一种靠链，一种靠监管审计），第三种只能靠相信。**

## Common Misconceptions | 常见误解

- **误解一："我的账户余额就是我的钱。"** 余额是平台的账面记录。**关键是私钥和法律权属，不是界面数字。**
- **误解二："上链就是自托管。"** 合约托管不等于你控制。**要看合约有没有升级权限、管理员密钥。**
- **误解三："持牌平台一定隔离客户资金。"** 持牌平台**有义务**隔离，这和"一定做到"是两回事 —— 但至少违反时有法律后果。

## In Practice | 实战里怎么用

对任何平台做三步托管尽调：

1. **钱在哪个地址/账户？** 要能被指出来。指不出来的，答案就是"在平台手里"。
2. **谁能移动它？** 链上：合约有没有升级权限、管理员密钥、多签阈值是多少。链下：有没有独立托管行、有没有隔离账户审计。
3. **平台破产时会发生什么？** 客户资产是破产财产还是隔离资产？**这个问题的答案决定了你在最坏情况下能拿回多少。**

第 3 问用于识别极端情况下的实际资产控制权。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 加密语境下托管问题归结为哪一个问题？
  A: 私钥在谁手上。界面余额是承诺，私钥才是控制权。
- Q: 为什么'带升级权限的合约托管'是伪装？
  A: 有升级权限或管理员密钥意味着有人能改变合约行为并动用资金，实质上更接近平台托管而非无人可动的合约托管。
- Q: 托管尽调里信息量最大、却最少被问的一问是什么？
  A: 平台破产时客户资产是破产财产还是隔离资产 —— 它决定最坏情况下能拿回多少。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
