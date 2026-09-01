---
id: "protocol:morph"
type: protocol-network
title: Morph
title_zh: Morph
aliases:
  - BGB Chain
status: reviewed
importance: tier-3
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
# Morph

## Executive Summary

以太坊 L2。它在这个知识库里被记录，是因为 2025-09 [[bitget]] 把其平台币全部（4.4 亿枚）移交给 Morph 基金会 —— 一半销毁、一半锁定，**该代币成为 Morph 链的 gas 与治理代币**。

这是"交易所平台币转型为公链代币"的一个罕见样本。

## What It Actually Is | 它到底是什么

这类安排的战略含义是**把交易所的用户与代币持有者迁移到链上生态**：

```
平台币 (交易所内部权益)
   → 移交给 L2 基金会
   → 变成链的 gas + 治理代币
   → 持有者的价值锚从「交易所收入」变成「链的使用量」
```

**这是价值捕获逻辑的根本改变**，也是交易所把自身影响力延伸到链上的一种方式（对照 [[mantle]] 与 [[x-layer]] 的不同路径）。

## How It Works | 运作方式

L2 的价值捕获通常依赖交易量与排序器收入。把一个已有持有者基础的交易所代币接进来，等于**跳过冷启动**。

**代价是治理结构的复杂性**：代币的原发行方与链的基金会是两个主体，利益未必一致。

**对事件市场的相关性**：Bitget 有钱包与用户（见 [[gracy-chen]]），若它进入预测市场品类，Morph 是最可能的部署地。

## Position in the Market | 它在市场里的位置

目前 Morph 与事件市场没有已知关联，它的位置与 [[mantle]] 类似：**条件具备、尚未动作。**

**记录它的意义在于完成"交易所系链"这张表** —— 三家头部交易所各有一条链，只有一条已经承载事件市场。这个不对称本身值得跟踪。

## What Could Break It | 什么会让它出问题

- **双主体治理** —— 代币原发行方与链基金会的利益协调。
- **生态成熟度** —— 相对新，采用度待观察。
- **事件市场关联为 UNKNOWN。**

## What To Watch | 该盯什么

- **Bitget 是否上线预测市场并部署于此。**
- **代币移交后的治理实际运作情况。**


<!-- timeline -->

## Timeline

- **2026-08-27** — 建页 (web 核验 2026-08-26)。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
