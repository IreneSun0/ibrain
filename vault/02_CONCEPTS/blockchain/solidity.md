---
id: "concept:solidity"
type: concept
title: Solidity
title_zh: Solidity智能合约语言
title_en: Solidity
aliases:
  - Solidity智能合约语言
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
related: []
prerequisites:
  - "concept:smart-contract"
  - "concept:ethereum-virtual-machine"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Solidity | Solidity智能合约语言

## Executive Definition / Chinese Explanation | 定义与解释

**Solidity** = 编写 [[ethereum-virtual-machine|EVM]] 智能合约最主流的编程语言。

它看起来像 JavaScript，但语义完全不同：**每一行都花真钱（[[gas]]），每一次部署都不可撤销，每一个 bug 都可能直接等于资金损失。**

## Why This Matters | 为什么重要

对不写代码的人，Solidity 值得理解的只有一件事：**它的错误后果与普通软件完全不同。**

| | 普通软件 | Solidity 合约 |
|---|---|---|
| 发现 bug | 发补丁 | **可能改不了**（无升级权限时） |
| bug 后果 | 功能异常 | **资金直接损失** |
| 攻击者 | 需要访问权限 | **任何人都能调用** |
| 代码可见性 | 通常闭源 | **通常公开可读** |

**最后两行的组合是关键**：代码公开 + 任何人可调用 = **合约上线那一刻就在接受全世界的免费渗透测试**，而奖金是合约里锁着的全部资金。

## How It Works | 机制怎么运转

事件市场合约的常见风险点：

1. **重入攻击** —— 外部调用中途被回调，状态未更新就被再次提取。
2. **权限设计** —— 谁能升级、谁能暂停、谁能提取（见 [[smart-contract]]）。
3. **整数与精度** —— 事件合约涉及份额分配，舍入误差可能被放大利用。
4. **预言机接口** —— **合约信任预言机的输入。预言机错，合约就精确地执行错误。**

**第 4 条最重要也最常被审计忽略**：审计通常检查代码正确性，而不检查"输入来源是否可信"。

## Concrete Example | 具体例子

为什么审计不等于安全 —— 一个事件市场的真实风险分层：

```
Solidity 代码       → 可审计 ✓
合约权限设计         → 可检查 ✓
预言机输入的正确性   → 审计范围之外 ✗
裁决机制的经济安全   → 审计范围之外 ✗
```

**Ukraine 矿产协议案里，合约代码完全正确**（见 [[case-uma-dispute-trilogy]]）—— 它忠实执行了预言机给出的、被治理攻击操纵的结果。

**没有任何代码审计能发现这个问题，因为它不是代码问题。**

**这就是为什么"合约已审计"是必要条件而远非充分条件。**

## Common Misconceptions | 常见误解

- **误解一："审计过就安全。"** 审计覆盖代码，不覆盖经济机制与输入可信度。
- **误解二："开源所以安全。"** 开源让好人能审查，也让攻击者能研究。**它提高透明度，不自动提高安全性。**
- **误解三："合约部署了就不能改。"** 很多合约留有升级权限 —— **那本身是另一类风险**（见 [[custody]]）。

## In Practice | 实战里怎么用

不写代码的人也能做的四项合约尽调：

1. **合约地址是什么？** 能在区块浏览器上查到吗？
2. **代码开源并验证了吗？** 浏览器上显示"已验证"意味着源码与字节码对得上。
3. **有没有升级权限/管理员密钥？** 多签阈值？时间锁？
4. **审计报告覆盖了哪个版本？** 部署的是不是被审计的那一版？

**第 4 问最常被含糊带过** —— 审计报告写的是三个月前的版本，部署的是昨天改过的，这种情况并不罕见。

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: Solidity 合约的错误后果与普通软件有何不同？
  A: 代码公开且任何人可调用，bug 直接等于资金损失，且在无升级权限时可能根本改不了。
- Q: 为什么'合约已审计'是必要而非充分条件？
  A: 审计覆盖代码正确性，不覆盖预言机输入的可信度与裁决机制的经济安全 —— 那些是审计范围之外的。
- Q: 不写代码的人可做的四项合约尽调是什么？
  A: 查合约地址、代码是否开源并验证、有无升级权限与多签阈值、审计报告覆盖的是不是部署的那一版。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: 区块链)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-08-27** — 语义关联层判断 (AI seed, 待人工复核): 前置 = smart-contract, ethereum-virtual-machine; typed 关系 0 条。词表见 [[relationship-types|关系类型受控词表]]。
- **2026-08-31** — 扩写为完整科普条目 (定义/机制/例子/误解/实战/自测); 原 seed 内容并入, 未删除既有断言。
