---
id: "protocol:winklink"
type: protocol-network
title: WINkLink
title_zh: TRON预言机网络
title_en: WINkLink
aliases:
  - TRON预言机网络
status: reviewed
importance: tier-2
domains:
  - blockchain
  - tron-ecosystem
tags:
  - protocol-network
  - xlsx-import
created: 2026-08-26
updated: 2026-08-31
last_verified: 
review_after: 2027-02-26
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources:
  - "source:2026-08-26-industry-learning-map-xlsx"
  - "source:2026-08-26-winklink-winklink-org"
related:
  - id: "protocol:tron"
    rel: provides-infrastructure-to
    note: 为 TRON 智能合约提供链外数据的去中心化 oracle
prerequisites: []
import_origin: xlsx-learning-map
import_category: TRON生态
---
# WINkLink | TRON预言机网络

## Executive Summary

[[tron]] 生态的去中心化预言机，为链上合约提供链外数据。**2025-05，TRON 把官方 oracle 从 WINkLink 切换为 [[chainlink]]。**

这次切换本身比这个协议更有信息量：**它说明预言机层的竞争正在向少数几家收敛。**

## What It Actually Is | 它到底是什么

预言机是所有链的必需件，因为[[ethereum-virtual-machine|虚拟机]]的确定性要求禁止合约自己读外部数据（见 [[oracle]]）。

**生态自建 oracle 与采用通用 oracle 的取舍**：

| | 自建（WINkLink 式） | 通用（Chainlink 式） |
|---|---|---|
| 控制力 | 强 | 弱 |
| 可信度 | 受生态背书限制 | **跨生态验证** |
| 采用成本 | 低（生态内） | 需接入 |

**TRON 的切换说明它认为第二列的可信度更重要** —— 尤其当链上承载近半流通 USDT 时，喂价出错的代价极高（见 [[tether]]）。

## How It Works | 运作方式

对事件市场，这个案例的价值在于**它展示了预言机可以被替换**。

很多人把"某平台用某预言机"当成固定属性，实际上它是可切换的架构选择 —— 而**切换本身就是一个应该被监测的事件**（见 [[settlement-methodology]]）：同一个平台在切换前后的裁决风险画像不同。

## Position in the Market | 它在市场里的位置

在事件市场的裁决基础设施图谱上，WINkLink 现在的位置是**被替代者**。

它仍然存在并服务 TRON 生态的部分应用，但在最关键的官方喂价位置上已被取代。

**这是一个有用的先例**：生态自建的预言机，在需要跨生态可信度的场景下会被通用方案挤出。

## What Could Break It | 什么会让它出问题

- **采用度下降** —— 失去官方位置后的长期地位不明。
- **生态绑定** —— 命运与单一链高度相关。

## What To Watch | 该盯什么

- **是否还有其他链做类似切换** —— 若是，说明收敛是趋势。
- **TRON 生态的事件类应用采用哪个预言机。**

## Sources

- [[src-2026-08-26-industry-learning-map-xlsx]] — 学习地图 workbook (user-direct, 作者提供)
- [[src-2026-08-26-winklink-winklink-org]] — <https://winklink.org/>

<!-- timeline -->

## Timeline

- **2026-08-26** — 从学习地图 workbook 导入 (分类: TRON生态)。 [Source: [[src-2026-08-26-industry-learning-map-xlsx]]]
- **2026-09-01** — 实体语义关联层: 依实体页已有 CONFIRMED 事实补 1 条 typed 关系 (词表见 [[relationship-types|关系类型受控词表]]); 证据为本页来源, 未新增断言。
- **2026-08-31** — 扩写为完整实体条目 (定位/运作/市场位置/风险/观察点); 原有断言保留。
