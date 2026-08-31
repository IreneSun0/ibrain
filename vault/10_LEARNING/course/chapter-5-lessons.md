---
id: "lesson:chapter-5"
type: lesson
title: "Course Ch.5 Event Markets Proper"
title_zh: "课程 · 第五章 事件市场本体"
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

# 课程 · 第五章 (主场开始 — 前四章的全部工具在这里合体)

## quest: concept:event-risk

### hook
一家从不碰 crypto 的欧洲基金, 2026 年因为一场美国关税判决单周回撤 8%。它的风控系统里没有任何一行叫「关税」的敞口 — 风险一直在, 只是没有名字。给风险起名字, 就是这一关。

### card
- 本质: 离散现实事件 (判决/选举/政策/地缘) 的发生与否, 对资产组合造成经济后果的不确定性 — 机构组合里**最普遍又最少被计量**的风险。
- 数字: 事件风险的三性: 离散 (0/1 跳变, 非连续扩散)、跨资产 (同一事件同时打击股/债/汇/crypto)、可合约化 (自从有了事件市场)。
- 实例: 选举→政策→利率链、法院判决→个股、监管发文→整个行业 — 每个机构都持有一堆「无名敞口」。

### mechanism
传统风控把风险按资产类别切 (股票风险/利率风险/汇率风险), 事件风险横着穿过所有类别 — 于是没有一个桌子认领它, 它散落在各桌的「残差」里。事件市场做的事: 把这层风险**显性化** (一个事件一个市场, 价格就是它的实时概率) 并**可交易化** (想卸的人和想接的人第一次有了场地)。第一性推论从这里出发: 敞口本已存在 → 显性化后需要计量框架 (event-var, 第七章) → 计量后需要管理基础设施 — 这条三段论就是公司存在的理由, 演讲的骨架也是它。

### traps
- ✗「事件风险 = 事件市场的风险」→ ✓ 顺序反了: 事件风险是机构**本来就有**的; 事件市场是它的显影液和对冲场 — 分清「风险本体」与「风险市场」, 你的叙事立刻高一个层级。

### ammo
- EN: "Institutions already hold event risk — elections, rulings, tariffs — they just hold it unnamed, scattered across every asset class. Event markets didn't create the risk; they made it visible and tradable. This layer makes it measurable."

## quest: concept:event-contract

### hook
把「不确定性」装进一张可交易的合约需要四个零件, 少一个都不成立。数清这四个零件, 你就看懂了这个行业的全部产品。

### card
- 本质: 支付取决于「指定事件是否/如何发生」的标准化合约 — 事件风险的可交易容器。
- 数字: 四零件: 事件定义 (什么算发生) / 判定来源 (谁说了算) / 支付规则 (发生付多少) / 截止时间 — 第六章整章就是对第一、二个零件的深挖。
- 实例: Kalshi 一张「Fed 三月降息 ≥25bp」合约: CFTC 监管的 DCM 上市、全额抵押、$1/$0 支付 — 四零件齐备的教科书样本。

### mechanism
event contract 是第二章衍生品语法的事件版应用: underlying = 一个被合约语言精确定义的事实; 支付结构 = binary option 的台阶函数; 法律外壳 = CFTC 框架下的 DCM 事件合约 (不叫 binary option, 这个名字的雷区第二章排过)。合约化的威力: 风险一旦被标准化, 它就获得了金融资产的全部基础设施 — 可定价 (盘口)、可对冲 (反向持仓)、可清算 (抵押体系)、可监管 (归入衍生品框架)。合约化的代价: **定义即命运** — 四个零件里任何一个写得含糊, 交易的就不是你以为的风险 (第六章的全部悲剧由此而来)。

### traps
- ✗「事件合约的风险在方向判断」→ ✓ 方向只是显性风险; 隐性风险在四零件的**措辞里** — 「宣布」还是「就职」、哪家机构的数据、几点截止 — 职业玩家读条款的时间比看盘久。

### ammo
- EN: "An event contract is four clauses pretending to be a bet: definition, source, payout, deadline. Amateurs trade the direction; professionals trade the clauses."

## quest: concept:outcome-market

### hook
「预测市场」这个名字其实太小了 — 同一套机器不仅能问「会不会发生」, 还能问「是哪一个」「是多少」。给机器一个准确的名字, 才能看清它的全部产品空间。

### card
- 本质: 围绕「离散或有界结果」创建可交易凭证的市场原语 — prediction market 只是它最出名的应用。
- 数字: 三种形态一根轴: 二元 (YES/NO) → 多结果 (N 选一, 本章后面) → 标量 (连续数值, 支线) — 结果空间从 2 到 N 到连续。
- 实例: Hyperliquid 的 HIP-4 (2026 年 mainnet): 一个 perp DEX 加装 outcome-market 扩展 — 说明这是一层可以长在任何交易基础设施上的**原语**, 不是一类独立公司。

### mechanism
outcome market 的通用配方: 把一个不确定性的**全部可能结果**枚举成互斥完备的集合, 每个结果发一种凭证, 结果揭晓后按真实结果兑付。这个抽象的价值在于看清产品边界: 选举 (多结果)、CPI 读数 (标量)、赛事 (二元/多结果) — 全是同一原语的参数化。行业判断也从这里来: 凡是能把结果空间「枚举清楚 + 判定清楚」的不确定性, 都能被做成市场; 反之 (结果空间模糊、判定无权威) 就是产品的自然边界 — 评估任何新 venue 的市场目录, 用这把尺子。

### traps
- ✗「outcome market / prediction market 随便混用」→ ✓ 对外混用无妨, 对内要精确: outcome market 是原语 (机器), prediction market 是应用 (用机器问现实事件) — 原语视角让你能评估「这台机器还能长什么产品」。

### ammo
- EN: "Outcome markets are a primitive, not a product category — any uncertainty with an enumerable outcome space and a decidable resolution can be marketized. That's the real TAM conversation."

## quest: concept:prediction-market

### hook
民调公司访问三千人, 出错; 专家上电视, 出错; 一群匿名者拿真金白银下注 — 价格常常最先对。不是因为他们更聪明, 是因为这台机器**汇聚**聪明的方式不同。

### card
- 本质: 用真金白银交易未来事件结果的市场 — 价格即群体的实时概率估计; outcome market 原语最重要的应用。
- 数字: 双头格局参照系 — Polymarket (全球最大, 链上结算) 与 Kalshi (美国联邦持牌, 估值一年内 $2B→$22B 量级) — 两条路线的估值都说明市场信了这个品类。
- 实例: 序章 price-discovery 的大选夜例子在这里认祖归宗: 预测市场就是价格发现机制对「现实事件」的直接应用。

### mechanism
预测市场 = 序章两个功能在事件维度的合体: 价格发现 (聚合分散信息 → 概率信号, 这是它的**信息产品**) + 风险转移 (对冲者卸事件风险给投机者, 这是它的**金融产品**)。历史包袱: 它长期被当作「新奇的民调替代品」(只看信息产品), 直到机构发现金融产品这一半 — 对冲、做市、跨市场套利 — 行业才从玩具变成资产类别。当下的转折证据: 顶级做市商双场馆进场、交易所巨头的战略投资、监管框架成型 — 你入行的 timing 正好在「玩具→基础设施」的相变点上, 这也是 TOKEN2049 上这个话题的温度来源。

### traps
- ✗「预测市场的产品是预测」→ ✓ 预测 (概率信号) 是**副产品**且免费公开; 可收费的产品是交易、清算、数据与风险管理 — 商业模式长在金融产品那一半。
- ✗「价格准 = 市场成功」→ ✓ 准是必要非充分; 没有对冲需求与做市生态, 再准的价格也只是个漂亮数字 — 评估 venue 看的是**谁在用它管理真实风险**。

### ammo
- EN: "A prediction market sells two things: a probability signal to the world for free, and risk transfer to whoever needs it for a fee. The industry only became investable when people noticed the second product."

## quest: concept:outcome-token

### hook
你在 Polymarket 点下「Buy YES」的那一刻, 链上多了一行记录: 你持有某个 ERC-1155 id 的一万份。你买的不是「观点」— 是一种可以转账、抵押、审计的**资产**。

### card
- 本质: 代表「特定结果发生时兑付固定金额」权利的 token — 事件敞口的资产化形态。
- 数字: 完备集恒等式: 同一市场全部结果的 token 各持一份 = 无论如何都兑付 $1 → 全套价格之和理论上 = $1 (偏离即套利, 下下关用它)。
- 实例: Polymarket CTF: 存入 $1 USDC 可铸「YES+NO」各一份 (合并恒等), 结果揭晓后胜方 token 1:1 兑付 — 第三章 ERC-1155 的形状在这里落地。

### mechanism
outcome token 把「头寸」从账户余额升级为**独立资产**, 三个后果依次展开: ① 可转移 — 敞口能在二级市场随时换手 (退出不必等事件揭晓); ② 可组合 — 能进钱包、进 DeFi、做抵押品 (事件敞口进入了更大的金融乐高); ③ 可审计 — 谁持有多少、何时进出, 链上全透明 — 任何人都能从链上重建某个地址的事件敞口画像, 这是价格市场做不到的数据条件。铸造/合并机制 (存 $1 铸全套、合全套赎 $1) 是这套体系的物理定律: 它锚定了价格和恒等式, 也让做市商能无限「进货」。

### traps
- ✗「买 YES = 下注记录」→ ✓ 是持有资产 — 你可以不等结果、在价格有利时卖出离场; 把事件仓位当「注」管理的人错过了一整层交易策略 (概率漂移交易)。

### ammo
- EN: "An outcome token turns a position into an asset: transferable before resolution, composable across DeFi, and auditable on-chain. That last property is the raw material for everything above it."

## quest: concept:implied-probability

### hook
价格 0.62 = 62% 概率 — 这是全行业最常用的一句话, 也是被误用得最狠的一句话。这一关教你什么时候能这么读, 什么时候这么读会亏钱。

### card
- 本质: 把 0-1 区间的合约价格**近似**读作市场对事件的概率估计 — 有用的近似, 危险的等号。
- 数字: 三个偏差源记死: 费率与价差 (机械抬价/压价)、资金成本 (钱被锁到判定日的时间价值)、流动性溢价 (薄盘价格代表少数人) — 修正它们之后才敢叫概率。
- 实例: 全套结果价格加总常 > $1 几个美分 — 不是市场犯傻, 是费率与摩擦的指纹 (下一关拿它当尺子用)。

### mechanism
为什么价格≈概率成立: 若真概率 60% 而价格 0.50, 期望收益为正, 买家涌入推价上行 — 套利力量把价格钉向概率。为什么只是「≈」: 上面三个偏差源都在拉扯这颗钉子, 且**长尾市场拉得最凶** — 0.03 的合约可能只是无人做市的报价残影, 读作「3% 概率」等于拿噪音当信号。机构级用法: 把 implied probability 当**起点**而非答案 — 先做偏差修正 (去费率、去时间价值、按深度加权), 再和自有模型对比找错价。liquidity-adjusted 思想在概率维度的投影就是这关: 要看「你的规模能实现的概率」, 不是屏幕上的数。

### traps
- ✗「价格 = 真概率」→ ✓ 价格 = 概率 × 摩擦的合影; 长尾与临期市场里摩擦是主角。
- ✗「概率读数是散户玩具」→ ✓ 修正后的 implied probability 是机构做跨市场比价、事件定价的**基准曲线** — 工具没错, 错的是不做修正就用。

### ammo
- EN: "Price approximates probability the way a shadow approximates a shape — good enough at noon, useless at dusk. Strip out fees, funding and thin-book noise before you call it a probability."

### drill
Q: 某二元市场 YES 0.34 / NO 0.70, 无费率市场。套利在哪, 每套一组赚多少?
A: 全套价 1.04 > 1 → 卖出恒等套装: 铸造 YES+NO (成本 $1) 分别卖出得 $1.04, 无风险赚 $0.04/组 (忽略摩擦)。恒等式偏离就是印钞机 — 这也是为什么成熟市场的偏离总是恰好 ≈ 摩擦成本。

## quest: concept:multi-outcome-market

### hook
「谁会赢得大选」有五个候选人 — 五个二元市场拼起来问, 还是一个市场直接问? 差别不是界面美观, 是一整套概率约束会不会自动生效。

### card
- 本质: 同一事件 N 个互斥结果各发一种 token 的市场 — 全部结果恰有一个发生。
- 数字: 约束恒等式: N 个结果价格之和理论 = $1; 加总显著 >1 = 摩擦或套利, 显著 <1 = 有结果没被枚举 (「其他」候选人缺席)。
- 实例: 大选盘是事件市场的流量心脏 — 而大选天然是多结果结构; ERC-1155 的「一约多 id」(第三章) 正为此形状而生。

### mechanism
多结果市场把「概率分布」直接做成了产品: 每个结果的价格是分布的一个点, 全套价格就是完整分布 — 交易者不只表达「会不会」, 而是「是哪一个」。恒等式约束是它的免疫系统: 任何结果被高估, 套利者买入其余全套对冲, 把分布压回自洽。设计上的魔鬼在**完备性**: 结果集必须互斥且穷尽 — 「其他/以上皆非」桶没设计好, 就会出现「没有任何 token 该赔付」的真空地带, 判定层直接炸锅 (第六章 contract-semantics 的常客案由)。读多结果盘的职业姿势: 先看全套加总 (市场健康度), 再看分布形状 (共识集中度), 最后看「其他」桶的定义 (完备性风险)。

### traps
- ✗「多结果 = N 个独立二元盘」→ ✓ 独立二元盘之间**没有**恒等式约束, 概率可以互相矛盾且无套利机制纠正 — 结构选择决定了价格的自洽性。

### ammo
- EN: "A multi-outcome market sells you the whole probability distribution, with an arbitrage-enforced constraint that it sums to one. The devil is the 'other' bucket — incomplete outcome sets are where resolutions go to die."

## quest: concept:fully-collateralized-market

### hook
「你们怎么保证赢家一定拿得到钱?」— 传统市场的答案是一整章的清算瀑布 (序章); 事件市场的答案短得离谱: 「钱早就锁在那了。」

### card
- 本质: 最坏情况的全部支付义务, 在开仓时刻就已 100% 由锁定抵押支持 — 违约在结构上不可能。
- 数字: 代价与收益同一枚硬币: 违约概率 ≈ 0 (无信用链条) vs 资本效率低 (每 $1 敞口锁 $1, 无杠杆)。
- 实例: 美国 DCM 框架下的事件合约现行全额抵押; Polymarket 的 CTF、Hyperliquid HIP-4 同样 — 全行业当前的共同答案, 也是 CFTC 保证金化讨论想要松动的东西。

### mechanism
机制在 outcome-token 关已见过: 铸造全套需存入全额 $1 — 最坏支付被**前置**锁定, 于是序章那套违约管理机器 (保证金追缴/强平/CCP 瀑布) 整体失业。这是两种安全哲学的对决: 传统市场「允许违约可能, 用分层资本吸收」 vs 全额抵押「让违约在物理上不发生」。谁对? 取决于标的性质 — 第二章 margin 关的裂缝在此复现: 事件价格 0/1 跳变, 保证金模型的「覆盖最坏波动」假设失效, **全额抵押可能不是保守选择而是唯一数学上诚实的选择**。这句判断是你在 CFTC 议题上的立场支点: 保证金化释放资本效率, 但把跳变型标的塞进扩散型模型 — 收益给了做市商, 尾部留给了清算体系。

### traps
- ✗「全额抵押 = 无风险」→ ✓ 消灭的只是**对手方违约**风险; 判定错误 (第六章)、稳定币储备 (第四章)、合约漏洞 — 一个都没少; 「无违约」≠「无风险」, 混用这两个词的分析全部打折。

### ammo
- EN: "Full collateralization doesn't manage default risk — it makes default structurally impossible, at the price of capital efficiency. The CFTC margin debate is really asking: can you fit a jump process into a diffusion-based margin model? Nobody has shown the math yet."

## quest: concept:hybrid-exchange-architecture

### hook
「Polymarket 到底是不是去中心化的?」— 这个问题本身问错了。正确的问题: 它把哪一半放在了链上, 为什么恰好是那一半?

### card
- 本质: 高频部分放链下 (撮合/盘口), 信任部分放链上 (托管/结算) — 按「哪层需要什么」切开的架构。
- 数字: 一条分界线: **作恶能被结算层纠正的环节可以链下, 作恶无法追回的环节必须链上** (第三章 off-chain 关的刀, 在此正式开刃)。
- 实例: Polymarket 全图: 链下 CLOB 撮合 (毫秒级、免 gas) + Polygon 链上 USDC 全额抵押 + ERC-1155 outcome token + oracle 判定 — 每个组件都在它该在的一侧。

### mechanism
把前三章的判断题合并成一张架构图: 撮合要速度 → 链下 (第三章); 托管要「挪不了」→ 链上合约 (第四章); 结算要可验证 → 链上 (第三章); 判定要连接现实 → oracle (第三章压轴)。信任边界的位置: 链下撮合方**理论上**能插队排序, 但它碰不到钱 (抵押在链上合约里)、改不了结算 (按链上 token 兑付) — 作恶空间被结算层封顶, 这就是 hybrid 的安全论证。行业意义: 这套架构平衡了机构的两个矛盾需求 (交易体验要像 CEX, 资产安全要像 DeFi), 事实上成为链上事件市场的收敛设计。

### traps
- ✗「hybrid = 半吊子去中心化」→ ✓ 是**按风险性质分层**的工程最优解 — 全链上 (撮合慢到不可用) 和全链下 (回到 FTX 信任模型) 都是更差的答案; 「哪半上链」的判断力恰恰是架构成熟的标志。

### ammo
- EN: "Polymarket's architecture answers one question precisely: which layers need trustlessness and which need speed. Matching lies off-chain because cheating there can't survive on-chain settlement. That sentence is the whole design."

## quest: concept:market-maker-incentive

### hook
新市场上线第一天: 盘口空空, 没人愿意第一个挂单 — 因为第一个挂单的人被收割得最狠 (第一章的逆向选择)。市场的冷启动问题, 最后都变成一张付费清单。

### card
- 本质: venue 付费 (返佣/奖励/流动性合约) 换取做市商持续挂出**指定宽度与规模**的双边报价 — 流动性的采购合同。
- 数字: 典型条款三要素: 最大价差 (报价不得宽于 X)、最小规模 (每边至少挂 Y)、在场时间 (Z% 时段必须有报价)。
- 实例: 第一章的呼应闭环: Kalshi 与 SIG、Polymarket 与 Wintermute — 头部 venue 与头部 MM 的绑定, 底层都是这类安排在驱动。

### mechanism
逻辑链条: 没有 MM → 盘口空 → 交易者不来 → 更没有 MM (死循环); venue 的解法是补贴第一推动: 用返佣与奖励**买断** MM 早期承担的逆向选择与库存成本, 让飞轮转过临界点后补贴退坡。设计的艺术在于「买行为不买刷量」: 按「有效报价时长×规模×价差质量」付费 (买的是真深度), 而不是按成交量付费 (会买来对敲刷量)。双重含义: ① MM 在激励合同下被**要求**在自己看不清的市场持续报价 — 风险工具的需求方就是这么被制度制造出来的; ② 评估任何 venue 的「流动性成色」要先问多少是补贴撑的 — 补贴退坡日就是真实流动性的验货日。

### traps
- ✗「激励计划 = 市场虚假繁荣」→ ✓ 冷启动补贴是所有双边市场的标准动作 (交易所/打车/外卖同构) — 问题不在有没有补贴, 在**补贴退出后流动性留不留得下**; 用这个标准看 venue, 而不是道德判断。

### ammo
- EN: "Market maker programs are how venues purchase their cold start — paying MMs to quote markets they can't yet read. Which is precisely why MMs need someone who can read those markets for them. That's our door."
