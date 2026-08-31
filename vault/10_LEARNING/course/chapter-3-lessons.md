---
id: "lesson:chapter-3"
type: lesson
title: "Course Ch.3 Minimal On-chain Kit"
title_zh: "课程 · 第三章 链上最小集"
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

# 课程 · 第三章 (你有 crypto 语境 — 本章是把「熟悉」升级成「精确」, 节奏快)

## quest: concept:ledger

### hook
银行、交易所、区块链、Excel 表 — 剥掉外壳, 全是同一个东西: 一张「谁拥有什么」的表。金融的全部战争, 都是关于谁有权改这张表。

### card
- 本质: 记录「谁拥有什么、发生过什么、谁欠谁什么」的权威数据 — 金融系统的地基本体。
- 数字: 评估任何账本只问两个问题: 谁能写入? 谁能回滚?
- 实例: 你的银行余额 = 银行私有账本上的一行; 你的 USDC = Polygon 公共账本上的一行 — 两行数字, 两种权力结构。

### mechanism
账本的核心不是记录, 是**权威**: 争议发生时以哪张表为准。传统方案 — 指定一个受监管机构当唯一记账员 (银行/登记结算公司), 用法律和审计约束它; 区块链方案 — 让成千上万节点各记一份、用共识规则强制一致, 谁也无权单方面改。两种方案没有优劣只有取舍: 单记账员快、便宜、可纠错 (也可被冻结、被挪用); 分布式账本抗审查、可验证 (也慢、贵、错了难回滚)。这个取舍是第 3 章一切内容的母题, 也是 Polymarket 「一半上链一半不上」的设计逻辑起点。

### traps
- ✗「区块链发明了账本」→ ✓ 账本七千年历史; 区块链发明的是**无需指定记账员的账本** — 把这句说准, 你在任何 crypto 对话里都不会被当外行。

### ammo
- EN: "Every financial system is a ledger plus a power structure over who can write to it. Blockchain didn't invent the ledger — it removed the appointed bookkeeper."

## quest: concept:consensus

### hook
一万台互不信任的电脑, 没有老板, 却对每一笔交易的顺序分毫不差 — 这不是技术奇迹, 是经济设计: 说谎的成本被造得比诚实高。

### card
- 本质: 分布式节点就「哪套交易历史有效」达成一致的机制 — 用经济成本替代机构信任。
- 数字: 攻击成本是共识安全的唯一标尺 — 重写历史需要压倒性算力 (PoW) 或质押多数 (PoS), 造假成本 > 造假收益时系统安全。
- 实例: TRON 用 DPoS (27 个投票选出的超级代表轮流出块, 支线细讲) — 快而集中; Ethereum 用 PoS — 慢而分散: 共识选型 = 性能与去中心化的滑杆位置。

### mechanism
问题的本质: 没有老板的系统里, 两个节点各说一个版本的历史, 听谁的? 共识的答案: 让「投票权」变得昂贵 (算力/质押), 让诚实有奖励、作恶被惩罚 (没收质押), 于是理性参与者的最优策略就是维护同一份历史。你只需带走一个判断工具: **信任假设** — 看任何链先问「我在信任什么?」(多数算力诚实? 多数质押者诚实? 27 个 SR 里的多数?) — 信任假设越集中, 链越快也越像一家公司。第六章 oracle 的争议会把同款问题再问一遍: 链内共识管不了链外事实。

### traps
- ✗「上链 = 绝对安全」→ ✓ 安全性 = 攻击成本, 是**经济量**不是形容词; 小链的攻击成本可能低到一次事件合约的赔付都够本。

### ammo
- EN: "Consensus replaces trusted parties with expensive lying. The only question that matters: what exactly are you trusting, and what does it cost to corrupt it?"

## quest: concept:blockchain

### hook
「要不要上链?」是这个行业被问得最多、答得最烂的问题。答案其实是一道两分钟的判断题, 这一关给你判断标准。

### card
- 本质: 用共识维护、按区块追加的共享账本 — 让互不信任的多方共用一份可验证的历史。
- 数字: 判断题公式: 多方参与 + 互不信任 + 需要共享状态 = 上链有理; 三条缺一 → 中心化数据库更快更便宜。
- 实例: Polymarket 把「抵押与结算」上链 (需要全球用户信任), 把「撮合」放链下 (需要速度) — 教科书级的判断题答案。

### mechanism
把前两关拼起来就是区块链: 账本 (记什么) + 共识 (谁说了算) + 区块链式追加 (历史不可篡改地一块接一块)。它买到三样东西: 可验证 (任何人可审计全部历史)、抗审查 (无单点可关停)、可编程 (下一关) — 代价是慢、贵、错了不能改。所以架构判断永远是逐层的: 哪层需要那三样东西就放链上, 哪层要速度和纠错能力就放链下 — 「全链上」和「全链下」都是没做判断的偷懒。这道判断题你会在 hybrid-exchange-architecture (第五章) 里对着 Polymarket 再做一遍。

### traps
- ✗「链上 = 先进」→ ✓ 链是**特定信任问题**的解, 不是先进性的标志; 中心化数据库在 90% 的场景里是更正确的工程答案 — 敢这么说反而显得你懂。

### ammo
- EN: "The blockchain question is never 'is it better' — it's 'which layer of this system needs verifiable, censorship-resistant shared state, and which layer just needs to be fast.'"

## quest: concept:smart-contract

### hook
「如果 X 发生就把钱付给 Y」— 这句话写在纸上需要法院执行, 写在链上自己执行。事件市场的整个链上半场, 建立在这一句话的自动化上。

### card
- 本质: 部署在链上、按写死的规则自动执行的程序 — 把「承诺」变成「机器行为」。
- 数字: 智能合约三性: 自动执行 (无人可拦)、公开可验 (代码就是条款)、不可篡改 (部署后规则锁死) — 三性同时也是三个风险源。
- 实例: Polymarket 的 CTF 合约: 抵押 USDC 锁入、事件判定后按 outcome token 自动兑付 — 「清算所职能」被几百行代码替代。

### mechanism
智能合约把序章的信任基础设施压缩成了代码: 托管 (钱锁在合约里, 不在任何公司手里)、履约 (条件满足自动支付, 无需对方配合)、审计 (规则公开, 全网可验)。但「代码即法律」是双刃剑: 规则写错也照样执行 (漏洞被利用没有撤销键)、规则没覆盖的情形无人裁量 (现实的模糊性塞不进 if-else)。最关键的裂缝: 合约只能感知**链内**状态 — 「选举谁赢了」这种链外事实, 它自己永远不知道 — 这个裂缝由 oracle 填 (本章压轴), 而 oracle 正是事件市场一切结算风险的入口。

### traps
- ✗「智能合约 = 有法律效力的合同」→ ✓ 它是**自动执行的程序**, 法律地位因法域而异; 「code is law」是工程现实, 不是法律现实 — 两层分开说, 合规对话不踩雷。

### ammo
- EN: "A smart contract replaces the clearinghouse with code — custody, execution, audit, all automated. Its one blind spot: it cannot see the real world. That blind spot is called the oracle problem, and it's where our industry lives."

## quest: concept:token

### hook
一行账本数据, 凭什么值钱? 因为它可转移、可验证、且被某个系统承认代表某种权利 — 这三件事凑齐, 数据就成了资产。

### card
- 本质: 由链上合约定义的可转移权利单位 — 「所有权」的可编程形态。
- 数字: 读任何 token 只问一句: 它**代表什么权利**? (货币索取权/治理权/收益权/一个事件的赔付权) — 权利之外的一切都是叙事。
- 实例: outcome token (第五章): 代表「事件发生时兑付 $1」的权利 — 事件市场把风险敞口做成了 token, 于是敞口获得了 token 的一切属性: 可转让、可组合、可链上审计。

### mechanism
token 是智能合约的第一个杀手应用: 合约定义规则 (总量、转移条件、销毁逻辑), 账本记录归属, 共识保证不可双花 — 于是任何权利都能被做成「链上可流通的单位」。对本课程唯一重要的推论: **风险也是一种权利** (获得赔付的权利), 所以风险可以 token 化 — 这就是 outcome token 的本体论。token 化的敞口继承了链的全部性质: 全球可转移 (跨境无摩擦)、可验证 (持仓公开)、可组合 (能塞进 DeFi 乐高) — 也继承了链的全部风险 (合约漏洞、私钥、监管定性)。

### traps
- ✗「token = 加密货币」→ ✓ 货币只是权利的一种; 把「它代表什么权利」问清楚, 是穿越一切 token 叙事迷雾的唯一手电筒。

### ammo
- EN: "A token is a programmable claim. Outcome tokens tokenize the most fundamental claim in finance: the right to be paid if something happens."

## quest: concept:oracle

### hook
链上合约锁着一亿美金等着按「选举结果」赔付 — 但链自己永远不知道谁赢了。谁来告诉它? 这个「谁」就是整个事件市场最脆弱的一环。

### card
- 本质: 把链外事实 (赛果/判决/价格) 输进链上合约的机制 — 现实世界与代码世界之间唯一的桥。
- 数字: 合约的安全上限 = oracle 的安全下限 — 代码再完美, 事实输入错了照样错误赔付。
- 实例: Chainlink (价格类主流; Polymarket 2026 起价格市场采用)、Pyth (交易机构直发的第一方数据)、UMA (乐观仲裁型, 第六章主角) — 三种设计哲学, 三种失败方式。

### mechanism
oracle 的难点不是「传数据」而是「谁的数据算数」: 单一数据源 = 单点腐败 (贿赂一个 API 就能偷走池子); 多源聚合 = 中位数防单点, 但源头串谋仍破防; 乐观机制 (UMA 式) = 先假设提议为真、给窗口挑战、争议交投票 — 把「真相」外包给经济博弈。事件市场把 oracle 压力推到极限: 价格类事实连续、多源、易验证; 事件类事实**一次性、可争议、常常含解释空间** (「宣布」算不算「当选」?) — 于是 oracle 从「数据管道」变成「裁判机构」, 它的一切治理缺陷都成了你的结算风险。第六章 oracle-risk 与 dispute-mechanism 展开这场战争的全部细节。

### traps
- ✗「oracle 是数据源」→ ✓ 是「决定哪个数据算数」的**机制** — 数据源可以有一万个, 合约只认 oracle 吐出的那一个数; 权力全在机制层。

### ammo
- EN: "The contract is only as honest as its oracle. In price feeds that's an engineering problem; in event markets it's a governance problem — and governance is exactly where the money has been lost."

## quest: concept:on-chain

### hook
「这个数据上链了」— 这句话到底承诺了什么? 三件具体的事, 而且每件都有价格。

### card
- 本质: 数据或执行直接记录在链的共识状态里 — 买到可验证、可组合、抗单点。
- 数字: 上链的三重承诺: 任何人可验证 / 任何合约可组合调用 / 没有单点能删改。
- 实例: Polymarket 的持仓与结算全部链上可查 — 第三方审计场馆结算行为之所以可能, 就因为这一层在链上。

### mechanism
on-chain 是一种**公开承诺的强度**: 写进共识状态 = 向全世界开放审计权。对机构的意义远超技术: 传统场馆说「相信我们的账」, 链上场馆说「自己去查」— 审计从特权变成公共品。这也重新定义了第三方的可能性: 无需场馆授权就能核验其结算历史 (第八章 auditability 的物质基础)。代价在下一关。

### traps
- ✗「链上数据 = 真实」→ ✓ 链保证的是「没被篡改」, 不保证「当初写进来的是真的」— 垃圾进、垃圾出、只是垃圾不可篡改; 数据的真实性还得靠 oracle 与源头。

### ammo
- EN: "On-chain means auditable by anyone, composable by any contract, deletable by no one. It's not truth — it's tamper-evidence."

## quest: concept:off-chain

### hook
Polymarket 的撮合引擎不在链上 — 全球最大预测市场的心脏跳在普通服务器里。这不是妥协, 是算过账的选择。

### card
- 本质: 在链外系统 (服务器/数据库) 执行或存储 — 买到速度与成本, 付出信任假设。
- 数字: 链下撮合以毫秒计, 链上确认以秒/分钟计, 成本差几个数量级 — 高频撮合上链在物理上不成立。
- 实例: Polymarket: 撮合链下 (要速度)、结算链上 (要信任) — 每一层的取舍都算过这笔账。

### mechanism
off-chain 不是「没上链的落后部分」, 是架构分层的另一半: 撮合要每秒万笔 — 链下; 订单簿状态要毫秒更新 — 链下; 用户体验要即时反馈 — 链下。链下的代价是**回到信任**: 你得相信运营方不插队、不偷跑、不改单 (传统交易所的全部老问题回归)。所以成熟架构的问题从「上不上链」变成「信任边界画在哪」: 哪些环节的作恶能被链上结算层最终纠正 (可以放链下), 哪些环节作恶无法追回 (必须上链) — 用这把刀切一遍任何 crypto 产品, 架构优劣立现。

### traps
- ✗「链下 = 不安全」→ ✓ 链下 + 链上最终结算的组合里, 链下作恶空间被结算层封顶 — 评估安全要看**信任边界**的位置, 不是看单层。

### ammo
- EN: "Off-chain is where you buy speed with trust. Good architecture isn't maximal on-chain — it's drawing the trust boundary where cheating can't survive settlement."

## quest: concept:erc-standards

### hook
为什么任何钱包都能收任何新发的币? 没人逐个适配 — 大家都长着同一副「接口」。标准是生态的隐形操作系统。

### card
- 本质: Ethereum 生态约定的合约接口规范 — 让钱包、交易所、协议无需互相认识就能互操作。
- 数字: 接口思维一句话: 只要实现同一组函数 (转账/查余额/授权), 生态就把你当同类。
- 实例: 下面三关 (ERC-20/721/1155) 就是三种最重要的「资产形状」标准 — 事件市场用的是第三种。

### mechanism
标准解决组合性问题: 没有标准, N 个应用适配 M 种资产 = N×M 次工程; 有标准 = N+M。这就是 EVM 生态滚雪球的机制 — 每个新协议天生兼容全部存量资产与工具。对你的实用意义: 读懂一个资产先看它是什么标准 — 标准即形状, 形状即能力边界 (能不能进 DEX 池、能不能被钱包显示、能不能批量转移)。

### traps
- ✗「标准是技术细节」→ ✓ 标准是**生态位**: 选了什么标准 = 能接入什么基础设施 = 拿到什么分发 — Polymarket 选 ERC-1155 (三关后) 是产品决策不是技术偏好。

### ammo
- EN: "Standards are why crypto composes. Pick a token standard and you've picked which half of the ecosystem works with you out of the box."

## quest: concept:erc-20

### hook
USDT、USDC、几乎所有你叫得出名的币 — 一个标准统治了「钱形状」的资产: 每一枚都和另一枚完全一样。

### card
- 本质: 同质化 token 标准 — 单位彼此等价、可分割、像钱一样流通。
- 数字: 判断要不要 ERC-20: 资产的单位之间**有没有个体差异**? 没有 (货币/积分/股份) → 20。
- 实例: USDC (Polymarket 的抵押与结算货币) 就是 ERC-20 — 事件市场的「钱」这一半用的是它。

### mechanism
同质化 = 无记名 + 可分割 + 完全互换 — 这三性使 ERC-20 成为链上的「货币模板」: 交易对、借贷池、支付轨道全部围绕它建。事件市场里它扮演**抵押品侧**: 你锁进合约的 USDC 是 ERC-20; 而你换回的「事件权利」不能用它 — 因为不同事件、不同结果的权利互不等价 — 于是需要另外两种形状。

### traps
- ✗「稳定币稳定是因为 ERC-20」→ ✓ 标准只管形状 (怎么转移), 价值稳定靠发行方储备 (第四章 stablecoin 的正题) — 形状与价值两层, 分开审。

### ammo
- EN: "ERC-20 is the shape of money on-chain. In event markets it's the collateral side of the trade — the claims side needs a different shape."

## quest: concept:erc-721

### hook
如果每一枚都独一无二 — 一块地、一张门票、一个编号 — 「钱形状」就装不下了。需要一个「每枚都有身份证」的标准。

### card
- 本质: 非同质化 token 标准 — 每个 token id 独立、不可分割、代表唯一对象。
- 数字: 判断: 单位之间**有个体差异**吗? 有 (每张票座位不同) → 721。
- 实例: NFT 热潮的技术底座; 对本课程它是「形状光谱」的另一极 — 帮你精确理解为什么事件市场两头都不用它。

### mechanism
721 给每个 token 一个唯一 id 和独立归属 — 代价是放弃可分割与互换性, 每笔转移都是单件交易。放进「资产形状光谱」看: 20 = 纯同质 (钱), 721 = 纯异质 (孤品)。事件市场的资产卡在中间: 同一结果的一万份权利互相等价 (像 20), 但「结果 A 的权利」与「结果 B 的权利」完全不同 (像 721) — 光谱两端都不合身, 于是有了下一关。

### traps
- ✗「NFT = 图片」→ ✓ 721 是「唯一性」的标准, 图片只是第一个流行用例 — 门票、房契、身份凭证同属此形状; 把标准和用例分开, 判断力立刻上一档。

### ammo
- EN: "ERC-721 is the shape of uniqueness. Event markets need something in between money and one-of-a-kind — which is exactly the next standard."

## quest: concept:erc-1155

### hook
一个大选市场有五个候选人 — 五种互斥的「权利」, 每种各有几万份等价份额。为它部署五份合约? Polymarket 的答案: 一份合约, 管理全部。

### card
- 本质: 一份合约同时管理多个 token id、每个 id 下无限等价份额、支持批量操作 — 「多类别×同质份额」的标准。
- 数字: 多结果市场的完美形状: N 个结果 = N 个 id, 每个 id 内份额互换 — 部署与操作成本从 N 份合约坍缩为 1。
- 实例: Polymarket 的 CTF (条件代币框架) 用 ERC-1155 承载全部 outcome token — 你交易的每一份 YES/NO 都是 1155 上的一个 id。

### mechanism
1155 = 20 与 721 的合体: id 之间异质 (721 性), id 之内同质 (20 性), 外加批量转移 (一笔交易动多个 id — 组合持仓调仓的 gas 优势)。事件市场的映射严丝合缝: 市场 = 合约, 结果 = id, 持仓 = 份额。这个标准选择的下游后果: 全部 outcome token 天生可组合进 EVM 生态 (钱包可显示、DeFi 可抵押的技术前提), 持仓结构链上全透明 (任何人都读得到每个地址的事件敞口 — 链上审计路线的数据基础)。一个标准选型, 决定了一个市场的可审计性 — 这就是「标准是产品决策」的实证。

### traps
- ✗「1155 是 NFT 标准的变体」→ ✓ 对事件市场它是**风险敞口的容器标准** — 谈论它的正确语境是市场结构, 不是 NFT。

### ammo
- EN: "One contract, many outcomes, fungible shares within each — ERC-1155 is why a Polymarket position is a legible, on-chain, composable risk object. Standard choice is market-structure choice."

## quest: concept:automated-market-maker

### hook
一个新市场, 没有做市商愿意来 — 盘口空着。DeFi 的暴力解法: 不求人, 用一条公式和一池钱自动报价。便宜、永在, 但有个专坑事件市场的暗伤。

### card
- 本质: 用公式+资金池自动定价的做市机制 — 无需人类做市商即可冷启动的「always-on 盘口」。
- 数字: 最简公式 x·y=k: 池里两种资产数量乘积恒定, 买走一边价格自动上移 — 一行数学替代一个做市团队。
- 实例: 与 CLOB 的分工已收敛: 主流事件盘 CLOB (定价准、机构友好), 长尾市场 AMM 冷启动 — 两种机制各守一段流动性光谱。

### mechanism
LP (流动性提供者) 把两边资产存入池子, 公式按存量自动报价, 交易者直接与池子成交 — 做市从「职业」变成「存款」。代价一: 资本效率低 (资金摊满全价格带, 而 CLOB 做市商只在市价附近集火)。代价二对事件市场是致命伤: 事件价格终局必然走向 0 或 1 — 池子**数学上保证**在临近判定时被知情者单边掏空, LP 的「无常损失」在这里是**必然损失**。所以事件 AMM 的真实用途是冷启动引导, 起量后流动性迁往 CLOB — 理解这条迁移路径, 你就能看懂任何新 venue 的流动性战略。

### traps
- ✗「AMM 民主化了做市 = 人人该当 LP」→ ✓ 事件市场的 LP 是在**卖终局必被行权的期权** — 临判定期的单边流会精确收割池子; 散户 LP 的亏损是设计使然, 不是运气。
- ✗「AMM 会取代 CLOB」→ ✓ 五年实践的答案是分层共存: 深度与定价效率要求高的主流盘归 CLOB, 长尾冷启动归 AMM。

### ammo
- EN: "An AMM is a formula pretending to be a market maker. In event markets it has one fatal flaw: prices must converge to zero or one, so the pool is mathematically guaranteed to be picked off at the end. Bootstrap with it — don't retire on it."
