---
id: "concept:smart-contract"
type: concept
title: Smart Contract
title_zh: 智能合约
title_en: Smart Contract
aliases:
  - 智能合约
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
  - "concept:blockchain"
import_origin: xlsx-learning-map+manual
import_category: 区块链
---
# Smart Contract | 智能合约

## Executive Definition / Chinese Explanation | 定义与解释

**Smart Contract | 智能合约** = 部署在链上、按预设规则自动执行的代码。

它既不"智能"也不完全是"合约"：它不会判断，只会执行；它没有法律主体，不能被起诉，也不会赔偿。**它是一台无人看管的自动售货机。**

## Why This Matters | 为什么重要

事件市场的全额抵押托管就建立在智能合约上：钱锁在合约里，平台没有私钥，**违约在机制上不可能发生**（见 [[fully-collateralized-market]]）。

这是一个真实的架构优势。但它同时引入了一类新风险，而这类风险的形状和传统金融风险完全不同：

- **传统**：对方可能不履约 → 靠信用、抵押、法律解决。
- **合约**：代码会精确履约 —— **包括精确执行一个错误的逻辑。**

**"代码即法律"的另一面是"bug 即损失，且不可上诉"。**

## How It Works | 机制怎么运转

智能合约的风险有四层，从高频到低频：

| 风险 | 表现 |
|---|---|
| **逻辑错误** | 代码写错，执行了非预期行为 |
| **升级权限** | 有管理员密钥能改变行为 → **实质上不是无信任的** |
| **依赖风险** | 调用的外部合约（预言机、稳定币）出问题 |
| **组合风险** | 与其他协议交互产生的意外状态 |

**第二层最需要警惕，也最常被忽略**：很多"链上托管"的合约带有升级权限或管理员密钥。**有升级权限的合约托管，实质上更接近平台托管** —— 只是伪装成了去信任。

**检查方法很简单**：看合约有没有 proxy/admin 角色，多签阈值是多少，时间锁有多长。

## Concrete Example | 具体例子

事件市场里智能合约的实际职责边界：

```
智能合约负责:
  ✓ 锁定抵押品（谁存了多少）
  ✓ 铸造/合并结果代币
  ✓ 按裁决结果分配资金

智能合约不负责:
  ✗ 判断事件是否发生      ← 预言机
  ✗ 撮合订单              ← 通常在链下
  ✗ 判断裁决是否公正      ← 没有任何机制
```

**右边三行是理解事件市场风险的关键**：合约会**忠实执行**预言机给它的结果，**无论那个结果对不对**。

Ukraine 矿产协议案里（见 [[case-uma-dispute-trilogy]]），合约完美地执行了一个被治理攻击操纵的裁决结果 —— **代码没有 bug，损失照样发生。**

## Common Misconceptions | 常见误解

- **误解一："智能合约消除了信任。"** 它把信任从交易对手转移到了**代码、部署者、和预言机**。信任守恒。
- **误解二："审计过就安全。"** 审计降低概率，不消除风险。且审计通常只覆盖代码，不覆盖经济机制设计。
- **误解三："代码即法律。"** 在真实的法律体系里，代码不是法律。**但在链上，代码的执行结果确实不可撤销** —— 两句话都对，指的是不同层面。

## In Practice | 实战里怎么用

对任何持有你资金的合约，做四项检查：

1. **合约地址是什么？** 要能在区块浏览器上查到。
2. **有没有升级权限/管理员密钥？** 多签阈值？时间锁？
3. **依赖哪些外部合约？** 预言机是哪个？稳定币是哪个？
4. **审计报告是谁做的、什么时候、覆盖了哪个版本？**

**第 2 项是分水岭**：有可即时行使的升级权限 = 你信任的是那个密钥的持有者，不是代码。**那和"平台托管"的区别比宣传的小得多。**

## Related Concepts | 相关概念

- 见 frontmatter `prerequisites` / `related` (typed 语义关联层; 词表: 90_META/taxonomy/relationship-types.md)

## Active-Recall Questions | 主动回忆题

- Q: 智能合约把信任从哪里转移到了哪里？
  A: 从交易对手转移到了代码、部署者和预言机。信任守恒，没有被消除。
- Q: 为什么'带升级权限的合约托管'实质上接近平台托管？
  A: 有管理员密钥或可即时行使的升级权限意味着有人能改变合约行为并动用资金，你信任的是密钥持有者而非代码。
- Q: Ukraine 案里合约有 bug 吗？为什么损失仍然发生？
  A: 没有 bug。合约忠实执行了预言机给出的结果，而那个结果被治理攻击操纵了 —— 合约不判断裁决是否公正。


## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (贡献者提供)
