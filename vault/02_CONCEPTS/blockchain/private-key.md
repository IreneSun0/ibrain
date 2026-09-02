---
id: "concept:private-key"
type: concept
title: Private Key
title_zh: 私钥
title_en: Private Key
aliases:
  - 私钥
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
  - id: "concept:wallet"
    rel: component-of
prerequisites: []
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Private Key | 私钥

## Executive Definition / Chinese Explanation | 定义与解释

**Private Key | 私钥** = 一串秘密数字，用它签名就等于证明"我是这个地址的主人"。

**没有找回机制。** 丢了就是永久失去；泄露了就是永久失去。这是链上世界与传统金融最刺眼的差别 —— 银行可以重置密码，链不能。

## Why This Matters | 为什么重要

私钥是[[custody|托管]]问题的技术底座：**"钱在谁手里"这个问题，翻译成技术语言就是"私钥在谁手里"。**

对事件市场：
- **全额抵押锁在链上合约里** —— 平台没有私钥，因此无法挪用（见 [[fully-collateralized-market]]）。这是一个可以在链上验证的安全属性，不是承诺。
- **但你自己的私钥仍是你的单点故障** —— 平台再安全，你的钱包被盗一样归零。

## How It Works | 机制怎么运转

私钥 → 公钥 → 地址，是一条**单向链**：

```
私钥 (随机数)  →  公钥  →  地址
        ↑ 不可逆 ↑ 不可逆
```

从私钥能算出公钥和地址；反过来算不出来（在现有算力下）。

**机构的三种管理方式**：
| 方式 | 机制 | 风险 |
|---|---|---|
| 单签 | 一把私钥 | **单点失效** |
| 多签 | N 把里要 M 把 | 阈值设计 |
| **MPC** | 私钥从不完整存在于任何一处 | 实现复杂度 |

**MPC 是机构托管的主流**：私钥被分片，签名时各方协同计算，**完整私钥从未在任何一台机器上出现过。**

## Concrete Example | 具体例子

链上事件市场用户最常见的三种归零方式，都与私钥有关：

| 方式 | 机制 | 防线 |
|---|---|---|
| 助记词泄露 | 钓鱼、截图、云备份 | 离线保管、不拍照 |
| **无限授权被利用** | 你签过的合约后来被攻破 | 按需授权、定期清理（见 [[erc-20]]） |
| 签错交易 | 界面被篡改或看不懂 | 硬件钱包核对、小额试探 |

**第二种最隐蔽**：你的私钥没有泄露，钱却没了 —— 因为你曾经授权过一个合约，而那个合约后来出了问题。

**这也是为什么"地址分层"是最有效的习惯**：交互地址只放要用的钱，主仓位地址从不签任何授权。

## Common Misconceptions | 常见误解

- **误解一："私钥就是密码。"** 密码可以重置，私钥不能。**它更像房子的唯一一把钥匙，而且没有锁匠。**
- **误解二："交易所有我的钱就等于我有私钥。"** 恰恰相反 —— 钱在交易所，私钥就在交易所。
- **误解三："多签一定比单签安全。"** 阈值设计错了（比如 2/3 都在同一个人手里）等于单签。

## In Practice | 实战里怎么用

链上事件市场的三条私钥纪律：

1. **地址分层** —— 交互地址（会签授权）与存储地址（从不签任何东西）分开。
2. **授权按需给** —— 不给无限额度，定期用区块浏览器清理旧授权。
3. **助记词离线** —— 不截图、不存云、不发消息。

**第 1 条最有效也最少人做**：它把"某个协议被攻破"的损失上限，从"你的全部资产"压到"交互地址里的余额"。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 私钥与密码的根本区别是什么？
  A: 密码可以重置，私钥不能 —— 丢失或泄露都是永久性的，没有任何找回机制。
- Q: MPC 托管的关键性质是什么？
  A: 私钥被分片，签名时各方协同计算，完整私钥从未在任何一台机器上出现过。
- Q: 为什么'地址分层'是最有效的安全习惯？
  A: 它把某个协议被攻破的损失上限，从全部资产压缩到交互地址里的余额。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
