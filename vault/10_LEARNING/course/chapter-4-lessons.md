---
id: "lesson:chapter-4"
type: lesson
title: "Course Ch.4 The Money Pipes"
title_zh: "课程 · 第四章 钱的管道"
aliases: []
status: seed
importance: tier-1
domains:
  - learning
tags:
  - course
  - bootcamp
created: 2026-08-27
updated: 2026-08-27
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources: []
related: []
---

# 课程 · 第四章 (短章, 4 关 — 机构对话的「钱在哪」四连问全在这里)

## quest: concept:custody

### hook
机构谈任何合作, 第一个电话永远打给同一个部门问同一句话: 「资产在谁手里?」— 答不好这句, 后面一切免谈。

### card
- 本质: 保管资产与密钥、控制转账权限的职能 — 「谁物理上摸得到钱」这个问题的答案。
- 数字: custody 三问 (与抵押品三问呼应): 谁持有密钥? 破产时资产算谁的? 谁能冻结/转走?
- 实例: Fireblocks — 机构级 MPC 托管基础设施: 密钥被数学拆分, 任何单方 (包括它自己) 都无法单独动钱 — 机构入场 crypto 的标配底座。

### mechanism
crypto 把托管问题推到极端: 私钥即所有权, 丢了无人能补, 被盗无人能追。于是托管光谱两端拉开 — 自托管 (你自己拿钥匙: 主权完整, 但机构受托责任不允许「钥匙在某个员工手机里」) vs 第三方托管 (专业机构+保险+审计: 合规友好, 但回到「相信一家公司」)。中间解是 MPC/多签: 密钥拆片、多方共管、单点失守不失金。事件市场的映射: Polymarket 模式 = 用户自托管+合约锁抵押 (钱在代码手里); Kalshi 模式 = 受监管清算体系托管 (钱在制度手里) — 两种答案都成立, 但机构问卷上是完全不同的两栏。

### traps
- ✗「托管 = 保管箱业务, 不重要」→ ✓ FTX 一案的本质就是托管失败 (客户资产与自营混用) — 托管是 crypto 机构化十年来**每一次大爆炸的震中**, 没有例外。
- ✗「链上 = 不需要托管讨论」→ ✓ 链上只是把问题换成「谁持有签名权限、合约管理员是谁、能不能升级合约」— 问题换了皮, 没消失。

### ammo
- EN: "Every institutional conversation starts with custody: who holds the keys, whose asset is it in bankruptcy, who can freeze it. Answer those three before anyone asks."

## quest: concept:custody-segregation

### hook
交易所倒闭那天, 决定你能不能拿回钱的不是余额数字, 而是一个此前没人细看的会计安排: 你的钱和它的钱, 记在一本账上还是两本。

### card
- 本质: 客户资产与平台自有资产**分账记录、分离保管** — 平台破产时客户资产不被当作破产财产。
- 数字: 一个判据切一切: 平台挪用客户资产在操作上是「不可能」还是仅仅「不允许」— 前者是结构, 后者是承诺。
- 实例: FTX (混同挪用, 客户排队当债权人) vs 受监管清算体系的隔离账户 vs 链上合约托管 (代码强制隔离) — 三种答案, 一个教训。

### mechanism
不隔离的世界: 你的存款进平台大池子, 平台亏损/挪用/破产, 你从「资产所有人」降级成「无担保债权人」排队分残值。隔离的三个强度等级: ① 账面隔离 (分开记账 — 最弱, 靠自觉); ② 法律隔离 (信托/独立法人持有 — 破产隔离有法律效力); ③ 结构隔离 (链上合约锁定 — 平台想挪都没有技术路径)。事件市场的机构叙事里这是暗线主角: 全额抵押锁在公开合约里 = 结构隔离的极致形态 — 「不是我们不挪, 是我们挪不了」比任何审计报告都硬。

### traps
- ✗「平台承诺隔离 = 隔离」→ ✓ FTX 的服务条款也写着客户资产隔离 — 承诺级隔离在压力下的价值为零; 只认结构与法律强度, 不认措辞。

### ammo
- EN: "Segregation has three grades: promised, legal, structural. Crypto's gift to finance is grade three — funds locked in a public contract that the operator physically cannot touch."

## quest: concept:settlement-rail

### hook
你赢了钱要提现 — 走银行电汇三天到账周末歇业, 走链上三分钟到账全年无休。「钱怎么动」这条看不见的轨道, 正在发生百年一遇的换轨。

### card
- 本质: 资金完成最终转移的网络通道 — 银行体系 / 卡组织 / 区块链, 每条轨道有自己的速度、成本、可达性与冻结点。
- 数字: 评估任何轨道四指标: 多快到账 (finality)、什么时间开门 (24/7?)、跨境到不到、谁能按暂停键。
- 实例: TRON — 全球 USDT 的主结算轨: 承载近半流通 USDT (~$90B 量级), 季度结算额以万亿美元计 — 一条链事实上成为了新兴市场的美元清算网络。

### mechanism
传统轨道 (代理行体系) 的特征: 分层中介、营业时间、T+N、每一跳都是一个冻结点与一笔费用; 链上轨道: 全年无休、分钟级最终性、点对点直达 — 但冻结点没有消失, 只是**换了位置** (稳定币发行方可冻结地址、合约管理权限、入出金口岸)。事件市场为什么天然长在链上轨道: 全球参与者、7×24 的事件 (选举夜是周二凌晨)、判定后即时兑付 — 传统轨道在这三项上全部不及格。机构问「钱怎么进出」时, 你按四指标+冻结点地图回答, 就是专业级答案。

### traps
- ✗「链上轨道 = 无人能冻结」→ ✓ USDT/USDC 发行方都有地址冻结权限且**常规行使** (配合执法) — 链上轨道的冻结点在资产层而非网络层; 画错冻结点位置的合规分析全盘皆错。

### ammo
- EN: "Settlement rails decide who your money has to ask permission from, and when. Event markets run on stablecoin rails because elections don't happen during banking hours."

## quest: concept:stablecoin

### hook
一条链上的美元, 没有银行账户也能全球流转 — 它凭什么值一美元? 答案不在链上, 在一家公司的资产负债表里。这个错位就是稳定币的全部风险与全部力量。

### card
- 本质: 锚定法币价值的链上 token — crypto 世界的现金、抵押品与结算货币三合一。
- 数字: 双头垄断格局 — USDT (Tether, 流通 ~$180B+ 量级, 约六成份额) 与 USDC (Circle, ~$70B+ 量级, 2025 年 IPO 上市) ; 事件市场结算几乎清一色 USDC。
- 实例: Polymarket 的每一笔抵押、每一笔赔付都是 USDC — 稳定币是事件市场的血液, 不是配角。

### mechanism
机制一句话: 发行方收你 1 美元存进储备, 给你 1 枚链上凭证, 承诺随时 1:1 赎回 — 稳定的来源是**储备资产+赎回承诺**, 不是代码。于是稳定币风险 = 发行方风险的三个面: ① 储备质量 (拿什么资产撑着 — 国债还是商票? 审计还是仅 attestation?); ② 赎回可靠性 (挤兑日兑不兑得动); ③ 冻结权限 (发行方可拉黑地址 — 合规必需, 也是审查风险)。事件市场全额抵押在 USDC 里的含义: 你的「无违约风险」头寸, 底层枕着 Circle 的储备管理 — 机构风控清单上这一行不能省。推论: event 资本以稳定币计价、在稳定币轨道流动 — 监控事件敞口必须连稳定币风险一起监控。

### traps
- ✗「稳定币 = 无风险现金」→ ✓ 它是**发行方的负债凭证**: 脱锚史 (2023 年 USDC 硅谷银行事件短暂脱锚) 证明「稳定」是储备管理的成果, 不是属性。
- ✗「USDT 和 USDC 差不多」→ ✓ 储备披露强度、监管姿态、主战场 (USDT 强于新兴市场轨道/TRON, USDC 强于合规机构/事件市场) 全然不同 — 机构语境里两者不可互换。

### ammo
- EN: "A stablecoin is a bearer claim on an issuer's balance sheet, running on rails that never close. Event markets settle in USDC — which means every 'fully collateralized' position still leans on Circle's reserves. Institutions should price that."
