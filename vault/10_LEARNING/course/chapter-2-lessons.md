---
id: "lesson:chapter-2"
type: lesson
title: "Course Ch.2 Contracts That Shape Risk"
title_zh: "课程 · 第二章 风险的合约形态"
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

# 课程 · 第二章 (event contract 的法律与风险语言在这章打底)

## quest: concept:derivative

### hook
一张纸, 自己一文不值, 却能值一百万 — 因为它指向别的东西。金融最重要的发明不是钱, 是「指向」。

### card
- 本质: 价值取决于**另一个东西** (资产/指数/利率/事件结果) 的合约 — 风险的可编程容器。
- 数字: 全球衍生品名义规模以「百万亿美元」计, 数倍于底层现货 — 因为同一份风险可以被切割、复制、转手无数次。
- 实例: 事件合约在 CFTC 框架下就是衍生品家族的一员 — 这个法律归类是它能被机构碰的前提。

### mechanism
衍生品干的事只有一件: 把风险从「和资产绑死」变成「可以单独拿出来交易」。你不必买下整家公司才能承担它的涨跌, 不必真持有石油才能对冲油价 — 合约把敞口和所有权解耦。解耦之后风险可以: 转移 (对冲者→投机者)、重塑 (线性变非线性)、杠杆化 (小钱控大敞口)。这就是为什么懂衍生品 = 懂现代金融的风险语法; 事件合约只是把这套语法应用到「事实发生与否」这种最原始的不确定性上。

### traps
- ✗「衍生品 = 高风险产品」→ ✓ 衍生品是风险的**容器**, 不是风险本身 — 同一张期货, 对冲者用它降风险, 赌徒用它加杠杆; 危险的是用法和规模, 不是工具。
- ✗「事件合约不算正经衍生品」→ ✓ 在 CFTC 语境它就按衍生品框架监管 (DCM 上市、清算规则) — 这一句法律定位是机构对话的入场券。

### ammo
- EN: "A derivative decouples exposure from ownership. Event contracts do the same for the most primitive underlying of all: whether a thing happens."

## quest: concept:underlying

### hook
「你买的到底是什么?」— 每一张衍生品合约背后都有这个问题。答错它的机构, 才是真正在裸奔。

### card
- 本质: 决定衍生品价值的那个「别的东西」— 价格、指数、利率, 或一个事件的结果。
- 数字: 风控第一问永远是「我真正暴露于哪个 underlying」— 名义上的标的和实际的风险因子经常不是一回事。
- 实例: 「Fed 三月降息」合约的 underlying 不是利率本身, 而是**FOMC 声明这一文本事件** — 差之毫厘的定义, 第六章会变成 resolution 的生死线。

### mechanism
事件合约把 underlying 从「连续数字」换成了「离散事实」, 这个替换有深远后果: ① 价格类 underlying 人人可见且无争议 (BTC 收盘价就是那个数); 事件类 underlying 需要**判定** — 谁说了算、按什么措辞、什么时间窗, 全都要写进合约 (第六章 contract-semantics 的全部内容); ② 价格连续变动, 事件 0/1 跳变 — 风险管理的数学完全不同 (第七章 event-var 为此而生)。所以拿到任何事件合约, 第一动作是把 underlying 用一句话精确说出来: 「什么来源、什么措辞、什么时间之前的什么事实」。说不出 = 你不知道自己买了什么。

### traps
- ✗「标题 = underlying」→ ✓ 标题是营销, 条款才是 underlying — 「X 会赢吗」的实际标的可能是「Y 机构在 Z 日期前以 W 措辞宣布」; 标题相同条款不同的两张合约是**两个不同的 underlying** (第六章等价性判决的根源)。

### ammo
- EN: "In event markets the underlying is not the event — it's the contractual definition of the event. Same headline, different clause, different underlying."

## quest: concept:option

### hook
「要是涨我想赚, 要是跌我不想赔」— 听起来像小孩子的无理要求, 金融却真把它做成了产品, 只是要收一笔「不对称费」。

### card
- 本质: 付权利金买到「权利而非义务」— 收益不对称: 下行封底, 上行敞开。
- 数字: 期权买方最大亏损 = 权利金 (锁死); 卖方收固定权利金、扛无限风险 — 买卖双方的风险形状互为镜像。
- 实例: 事件合约的买方结构上就像期权买方: 最多亏掉合约价, 上限 $1 — 这个相似是下一关的入口。

### mechanism
期权把「义务」从交易里拆掉了: 期货双方都必须履约 (对称义务), 期权买方到期可以走人 (不对称权利)。这份不对称本身有价格 — 权利金, 由三样东西定: 现在离行权条件多远、还剩多少时间、underlying 抖得多厉害 (波动率)。事件合约与期权的深层同构: 一张 0.30 的 YES 合约 ≈ 一张「事件发生则赔付 $1」的期权, 0.30 就是它的权利金 — 于是期权的全部思维工具 (时间价值衰减、临近到期的价格收敛) 都能搬进事件市场。这也是机构衍生品柜台看得懂事件合约的原因。

### traps
- ✗「期权与期货差不多」→ ✓ 一个是对称义务、保证金驱动; 一个是不对称权利、权利金驱动 — 风险形状完全不同, 混用会把风控模型直接做错。
- ✗「买期权风险小」→ ✓ 单笔封底 ≠ 策略安全: 权利金会 100% 归零, 连续买等于连续交保费 — 事件合约同理, 0.05 的长尾合约大概率就是归零的命。

### ammo
- EN: "An option is asymmetry with a price tag. An event contract is the purest option there is: premium in, one dollar or zero out."

## quest: concept:binary-option

### hook
把一张事件合约的支付画出来: 发生 $1, 不发生 $0, 中间什么都没有。这个形状在衍生品教科书里早有名字 — 而这个名字在法律上恰恰**不能**随便用。

### card
- 本质: 支付只有两档 (固定金额或零) 的期权 — 事件合约的经济学孪生兄弟。
- 数字: payoff 图 = 一个台阶函数: 条件满足跳到 $1, 否则贴地 $0 — 没有中间态。
- 实例: curriculum 的经典练习: 把任一 event contract 摊开画 payoff, 你画出的就是 binary option — 然后在旁边标注法律分类的不同。

### mechanism
经济上, 事件合约 ≈ binary option: 同样的台阶支付、同样的「价格≈概率」读法、同样的临期收敛行为。法律上, 两者被刻意分开: 零售 binary options 在多个法域被禁或严管 (历史上是诈骗重灾区), 而美国事件合约走的是 CFTC 指定合约市场 (DCM) 通道 — 交易所上市、全额抵押、受监管结算。这个「经济相同、法律不同」的双重性是你的对话利器: 对量化人用 binary option 的语言讲定价, 对合规人必须换 event contract 的语言讲框架 — 用错场合会同时得罪两边。

### traps
- ✗「既然经济等价, 名字无所谓」→ ✓ 名字就是监管通道: 叫 binary option 触发一套禁令记忆, 叫 event contract 进入 DCM 框架 — 行业花了十年才把这两个词分开, 别一句话给合回去。

### ammo
- EN: "Economically it's a binary option; legally it's an event contract on a regulated DCM. That one sentence is the whole story of how this industry became investable."

### drill
Q: 0.30 买入 YES ×10,000 份。画出到期损益两点。
A: 发生: (1−0.30)×10,000 = **+$7,000**; 不发生: −0.30×10,000 = **−$3,000**。最大亏损在买入时刻就已锁死 — 这就是「全额抵押」在买方视角的含义 (本章 collateral 关再看卖方视角)。

## quest: concept:hedging

### hook
对冲的目的不是赚钱 — 是花钱买「少输」。听懂这句话的反直觉, 才算入了风险管理的门。

### card
- 本质: 建立与既有风险**反向**的头寸, 让坏结果发生时有东西反向赔你。
- 数字: 完美对冲的期望收益 ≤ 0 (对冲成本) — 你买的是波动的坍缩, 不是收益。
- 实例: 制药公司在 FDA 判决前买「不获批」的 YES — 判决坏, 合约赔; 判决好, 主业赚 — 两个世界里都活着。

### mechanism
对冲三步: ① 识别敞口 (我怕什么事? 怕多少钱?); ② 找反向工具 (什么东西在那件事发生时升值?); ③ 定对冲比例 (全对冲锁死一切上行, 部分对冲留一点敞口)。第三步是艺术, 第二步是事件市场的存在理由: 在事件合约出现前, 「监管判决、选举、地缘事件」这类风险**没有直接反向工具**, 机构只能用相关资产粗糙代理 (买波动率、减仓) — 事件合约第一次给了这些风险精确的对冲腿。但「精确」有个天敌: 你找到的反向工具和你的真实风险往往不完全重合 — 下一关就是为这个裂缝命名的。

### traps
- ✗「对冲 = 稳赚的套利」→ ✓ 对冲是**支出**: 付出成本消灭波动; 把对冲做成盈利中心的机构, 都是在裸卖风险而不自知。
- ✗「有相关性就能对冲」→ ✓ 相关性会在压力时刻断裂 — 平时 0.9 相关的两个资产, 危机日可以同向崩; 真对冲要的是**机制上的**反向, 不是统计上的。

### ammo
- EN: "Hedging is buying the collapse of variance, not buying returns. Event contracts matter because they gave institutions a direct hedge leg for risks that never had one."

## quest: concept:basis-risk

### hook
你在 Kalshi 持有「X 当选」YES, 去 Polymarket 买了「X 当选」NO 对冲。选举夜出了幺蛾子: 一个平台裁 YES, 另一个裁 NO。你的「完美对冲」在两边同时亏损 — 欢迎来到这个赛道的创业理由。

### card
- 本质: 对冲工具与被对冲风险**不完全相同**, 导致两者不会一比一互相抵消 — 裂缝的名字。
- 数字: 对冲后剩下的敞口 = basis; basis ≠ 0 就有 basis risk — 对冲从不消灭风险, 只是把大风险换成小 basis。
- 实例: 跨 venue「同题」事件合约: 措辞差一个从句 (「宣布」vs「就职」)、来源差一家机构、时间窗差一天 — 平时价格同步, 争议时刻分道扬镳。

### mechanism
basis 的三个来源, 事件市场全占且更凶: ① 标的不同 — 两张合约的 contract-semantics 有语义缝隙 (第六章的判决对象); ② 结算机制不同 — 一边 CFTC 框架内裁定, 一边 UMA 预言机裁定, **同一事实可以得出两个官方答案**; ③ 时间不同 — 结算日错开, 中间隔着一段裸奔期。价格市场的 basis 是统计问题 (相关性), 事件市场的 basis 是**语义问题** (定义) — 统计问题靠数据解决, 语义问题必须逐条读条款。这就是 contract-equivalence 判决书的市场缺口: 没人愿意读, 但钱死在不读上。

### traps
- ✗「同题合约 = 天然对冲对」→ ✓ 标题相同只保证营销相同; 敞口是否相同要过语义四层检查 — 「同题不同义」是事件市场亏钱方式排行榜的榜首。
- ✗「basis risk 很小, 可以忽略」→ ✓ 它平时小到看不见, 出事时**一次吃掉全部对冲收益** — 尾部型风险的经典画像, 忽略它的人都是在捡钢镚。

### ammo
- EN: "In price markets, basis is a statistical residual. In event markets, basis is semantic — two contracts with the same headline can legally resolve to opposite answers. Measuring that gap is the open business."

## quest: concept:leverage

### hook
同样看对方向, 一个人赚 5%, 一个人赚 50%, 第三个人爆仓离场 — 三人唯一的区别是同一个旋钮拧到了几。

### card
- 本质: 用小于敞口的资本控制全额敞口 — 收益与亏损同倍放大的旋钮。
- 数字: 10 倍杠杆下, 10% 反向波动 = 本金归零 — 杠杆倍数就是你的「死亡波动阈值」的倒数。
- 实例: 美国事件合约现行 DCM 框架**不允许杠杆** (全额抵押) — 而 CFTC 正在讨论的保证金化, 本质就是「要不要给这个市场装杠杆旋钮」。

### mechanism
杠杆改变的不是方向判断, 是**生存时间**: 无杠杆的错误头寸可以扛到反转, 杠杆头寸在中途就被强制退场 (下章预告: liquidation 在支线, 但机制要懂) — 「对了方向、死在路上」是杠杆交易者的标准墓志铭。对市场结构的影响更深: 杠杆放大了违约可能 → 需要保证金体系 → 需要清算层 → 需要 CCP — 序章那整套基础设施, 一半是为杠杆的后果修的。反过来看事件市场: 无杠杆 = 无违约链条 = 不需要那套设施 — 资本效率差, 但结构极简。两种世界的取舍, 本章最后两关正面展开。

### traps
- ✗「杠杆是工具中性的」→ ✓ 对个体或许, 对**系统**不是: 全场杠杆越高, 连锁强平的多米诺越密 — 2026 年每次 crypto 大回撤里的连环爆仓都是同一个剧本。

### ammo
- EN: "Leverage doesn't change whether you're right — it changes whether you survive long enough to be right."

## quest: concept:collateral

### hook
金融的信任问题最终只有一个答案: 「先把东西押在这」。一切复杂的保证金体系, 都是这句话的工程化。

### card
- 本质: 为担保未来履约而**预先锁定**的资产 — 违约发生时唯一真实的赔付来源。
- 数字: 抵押品三问 — 押的是什么 (质量)、押了多少 (覆盖率)、押在谁手里 (托管) — 任何信用结构的体检表。
- 实例: Polymarket 的抵押品是 USDC、锁在链上合约里、100% 覆盖最坏支付 — 三问的答案全部公开可验, 这就是链上市场对机构的核心卖点。

### mechanism
承诺是空气, 抵押品是物质 — 违约时法庭和清算所能拿到的只有后者。抵押品体系的全部工程围绕三个问题: ① 质量 — 押的东西自己会不会跌 (现金最优, 波动资产要打折/haircut); ② 数量 — 覆盖多少比例的潜在损失 (100% = 全额抵押, <100% = 保证金化, 覆盖率就是资本效率与安全的滑杆); ③ 托管 — 押在中立第三方还是对手方自己手里 (FTX 教训: 押在对手方手里的抵押品等于没押)。第四章 custody 与第七章 counterparty-risk 都会回到这三问 — 抵押品是贯穿全课的一根钢筋。

### traps
- ✗「抵押品 = 成本」→ ✓ 抵押品是**信用的替代品**: 无抵押的世界里你要为每个对手方做尽调、设额度、买保险 — 押金是最便宜的信任。
- ✗「押了就安全」→ ✓ 三问缺一不可 — 足额但押在对手方手里 (托管失败)、足额但押的是会崩的币 (质量失败), 历史上都赔穿过。

### ammo
- EN: "Collateral is the only part of a promise that survives a default. Quality, coverage, custody — three questions, and the third one is where crypto keeps failing."

## quest: concept:margin

### hook
100% 抵押太浪费, 0% 抵押是裸奔 — 于是金融发明了一个动态的中间态: 押一部分, 随风险涨跌加减。这个中间态撑起了百万亿衍生品市场, 也是 CFTC 正在为事件合约纠结的问题。

### card
- 本质: 制度化、按风险动态计算的部分抵押 — 清算体系吸收违约波动的缓冲垫。
- 数字: 保证金 = 覆盖「预期最坏波动」而非「最坏结果」— 比如覆盖 99% 置信度下两日波动; 剩下 1% 靠清算所瀑布接。
- 实例: CME 期货保证金常为名义值的几个百分点 — 20 倍隐含杠杆的资本效率, 换来整套追保/强平/CCP 机器的运转成本。

### mechanism
保证金是杠杆和违约之间的调节阀: 押金覆盖短期波动 (initial margin 开仓门槛, 支线细分), 价格反向走时追加 (margin call), 追不上就强平 (liquidation) — 三段式把「违约」提前拦截成「退场」。全系统的前提是**能算准波动**: 模型说两日最多跌 5%, 收 6% 押金; 真跌 15% 时, 缺口由清算所瀑布吞下。事件合约保证金化的技术难题恰在这: 事件价格不是连续扩散, 是 0/1 跳变 — 「两日最坏波动」可以直接是 100%, 传统保证金模型的数学地基在这里裂开。这条裂缝是你在 CFTC 话题上最锋利的一句话。

### traps
- ✗「保证金是交易成本」→ ✓ 是**风险押金**, 平仓退还 — 成本是它的资金占用利息, 不是它本身; 算错这个的财务模型会高估交易成本一个量级。
- ✗「保证金化 = 行业进步」→ ✓ 是取舍: 资本效率↑ 违约链条↑ 清算设施需求↑ — 对跳变型标的, 传统模型还未必成立; 「进步」与否取决于你问的是做市商还是清算风控。

### ammo
- EN: "Margin models price the tail of a diffusion. Event contracts don't diffuse — they jump from one to zero. That's the unsolved math at the heart of the CFTC margining debate."

### drill
Q: 事件合约价 0.60, 若按「覆盖 99% 两日波动」收保证金, 模型该收多少?
A: 陷阱题 — 事件价格两日内可跳至 0 或 1, 99% 分位的「波动」可以就是 0.60 或 0.40 (全额) — 除非模型引入「判定前概率漂移有界」的假设。这道题的正确答案是**指出模型假设不成立**, 而这正是机构风控对事件合约保证金化的真实疑虑。

## quest: concept:cross-margin

### hook
你在同一清算所持有「Fed 降息」YES 和高度反向的利率期货 — 分开算要押两份全额, 合并算风险互相抵消大半。省下的资本从哪来? 从「承认组合内的对冲关系」来。

### card
- 本质: 允许相关头寸的风险互抵、按**净风险**收保证金的模式 — 资本效率的第二级火箭。
- 数字: 对冲良好的组合, cross-margin 可把保证金需求压缩数倍 — 这就是机构选择「在哪清算」的经济学。
- 实例: 事件合约进入机构组合的终局想象: 事件头寸与相关资产在同一保证金池互抵 — 前提是有人能证明「相关」— 这个证明恰好需要 canonical-event-id 和 event-var (第六七章)。

### mechanism
逐仓保证金把每个头寸当孤岛, 各收各的; cross-margin 承认组合是网络: YES+反向期货的净风险远小于两者之和, 押金按净额收。天堂有个地下室: 互抵成立依赖「相关性假设在压力下依然成立」— 而危机日相关性会翻脸 (对冲腿失效、两头寸同向亏损), 此时净额算法**系统性低估**了风险。所以 cross-margin 的边界 = 风控对相关性稳定度的信心边界。事件市场版的深水区: 跨 venue 的「同题」合约能不能互抵? 答案取决于它们是否真等价 — 于是资本效率问题被翻译成了语义判定问题, 等价性判决书直接站在这笔钱的闸门上。

### traps
- ✗「互抵省的钱是免费的」→ ✓ 省的是「正常日」的资本, 押上的是「相关性断裂日」的尾部 — cross-margin 是卖了一份尾部保险换现金流。
- ✗「跨 venue 自然可以互抵」→ ✓ 不同清算体系之间**没有**互抵 (各自瀑布独立); 跨 venue 事件敞口在今天是各押各的 — 这个低效正是行业下一阶段的整合方向。

### ammo
- EN: "Cross-margin is the clearing system agreeing that your hedge is real. For event contracts across venues, nobody can certify that yet — the contract-equivalence problem is standing between the industry and its capital efficiency."
