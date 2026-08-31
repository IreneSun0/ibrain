---
id: "lesson:chapter-6"
type: lesson
title: "Course Ch.6 Resolution and Disputes"
title_zh: "课程 · 第六章 结算与争议"
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

# 课程 · 第六章 (全书核心 — 这一章每一关都要能脱稿讲)

## quest: concept:resolution

### hook
事件市场和一切其他市场的分界线只有一条: 股票不需要有人宣布「苹果公司发生了」, 事件合约必须有人宣布「这件事发生了」。这个宣布动作, 就是整个行业的阿喀琉斯之踵。

### card
- 本质: 事件结束后, 按合约规则**判定哪个结果获胜**的过程 — 事实与支付之间的那道门。
- 数字: 判定四要素 = event contract 四零件的后两件展开: 谁提议 / 谁验证 / 多久生效 / 能否推翻。
- 实例: 行业口径的争议底数: 12.3 万判定请求中约 957 起进入争议、7.12% 的争议改判 — 判定不是形式手续, 是有真实错误率的裁决程序。

### mechanism
resolution 是事件市场的「独有器官」: 价格市场的结算输入 (收盘价) 自动存在、无需裁决; 事件市场的结算输入 (「发生了吗」) 必须被**生产**出来 — 由某个程序、按某些条款、面对可能的争议。这个生产过程的每一步都是攻击面: 提议人可能错、来源可能歧义、验证可能被收买、时间窗可能被利用。这条生产线逐站拆开是: 输入 (resolution-source) → 规格书 (contract-semantics) → 故障模式 (oracle-risk / resolution-risk) → 纠错装置 (dispute-mechanism) → 保险 (resolution-insurance) → 全链规程 (settlement-methodology) → 跨市场对账 (contract-equivalence / canonical-event-id)。

### traps
- ✗「resolution 是运营细节」→ ✓ 它是事件市场的**定价之锚**: 交易者定价的从来不是「事件本身」, 而是「这台判定机器会输出什么」— 机器有偏, 价格就有偏。

### ammo
- EN: "Every other market gets its settlement input for free — the closing price just exists. Event markets have to manufacture theirs. That manufacturing line is called resolution, and its defect rate is measurable: of roughly 123k resolution requests, about 957 were disputed, and 7 percent of those flipped."

## quest: concept:resolution-source

### hook
「以 AP 的宣布为准」和「以官方认证结果为准」— 2020 年美国大选, 这两句话之间隔了六个星期和一场宪政风波。来源的选择, 就是风险的选择。

### card
- 本质: 合约指定的、用于判定结果的权威信息来源 — 判定生产线的**原材料供应商**。
- 数字: 来源四检: 会不会出 (可用性) / 出得清不清楚 (明确性) / 和别家冲不冲突 (唯一性) / 出的时间对不对得上合约窗口 (时效性)。
- 实例: 体育盘的来源生态已专业化 — OpticOdds 这类数据商向 venue 和做市商供应赛果与赔率数据; 政治盘还常裸依赖「新闻共识」— 成熟度差一个代际。

### mechanism
来源是判定错误的第一入口, 四种典型死法: ① 来源不出数 (机构改了发布计划 → 合约悬空); ② 来源出数但措辞歧义 (「基本完成」算不算「完成」); ③ 多来源打架 (两家权威机构口径不同 → 各执一词的双方都「对」); ④ 来源出数在时间窗外 (合约截止后才官宣)。职业读盘者拿到合约先查来源条款: 指定的是**单一明确机构的单一明确数据字段**, 还是「主流媒体共识」这类软来源 — 前者的风险可计算, 后者的风险不可计算。行业含义: 来源质量是合约风险评分的第一个输入维度, 也是跨 venue 等价性判断 (本章末) 的第一个比对项。

### traps
- ✗「权威来源 = 无风险来源」→ ✓ 权威机构也会修订数据、推迟发布、改变口径 — 来源风险问的不是「它权威吗」而是「它在合约时间窗内、按合约措辞、无歧义地出数的概率」。

### ammo
- EN: "The resolution source is the supply chain of truth. Professionals underwrite four things: will it publish, will it be unambiguous, will it be unique, will it be on time. 'Major media consensus' fails all four audits."

## quest: concept:contract-semantics

### hook
两张合约, 标题一字不差: 「X 会在 2026 年当选总统吗」。一张按「胜选宣布」判, 一张按「宣誓就职」判。中间隔着的那些日子里, 任何事都可能发生 — 而你以为你买的是同一个东西。

### card
- 本质: 真正决定支付的五要素 — 谓词 (什么算发生)、阈值、时间窗、来源、例外条款 — 合约的**真实基因**, 标题只是它的艺名。
- 数字: 五要素逐项检查是读合约的标准作业程序; 任何一项含糊 = 一个开放的争议入口。
- 实例: 「降息 ≥25bp」— 谓词 (降息)、阈值 (≥25bp)、时间窗 (三月会议)、来源 (Fed 声明)、例外 (紧急会议算不算) — 一句话合约也五脏俱全。

### mechanism
语义是事件合约的**风险本体**: 你的敞口不是对「事件」的, 是对「五要素所定义的那个命题」的 — 命题与你心中的事件之间的任何缝隙, 都是别人的套利空间和你的意外亏损。语义缝隙的三个高发区: 谓词的边界情形 (辞职算不算「离任」? 代理算不算「就任」?)、时间窗的时区与截止瞬间、例外条款的沉默 (没写的情形谁裁量?)。生产级技能: 拿到任何合约, 60 秒内把五要素列成表、圈出含糊项 — 这个动作就是合约风险评估的人肉原型, 也是任何尽调对话里的现场表演项目。

### traps
- ✗「标题相同 = 同一个市场」→ ✓ 标题是营销层, 语义是支付层 — 「同题不同义」是跨 venue 对冲爆掉的第一死因 (basis-risk 关的伏笔在此引爆)。
- ✗「语义问题靠写得更细解决」→ ✓ 细化收敛不了自然语言的开放性 — 总有没写到的情形; 所以语义风险的终极答案不是「完美合约」而是「明确的裁量程序」(两关后的 dispute-mechanism)。

### ammo
- EN: "A contract's title is its stage name; the predicate, threshold, window, source and exceptions are its DNA. Same title, different DNA — that's how 'perfectly hedged' books blow up in event markets."

## quest: concept:oracle-risk

### hook
第三章说过: 合约的诚实上限是 oracle 的诚实下限。现在把这句话变成损益: 当判定机器本身被操纵、被收买、或者单纯宕机 — 你的「稳赢」头寸会发生什么?

### card
- 本质: 链外事实进入链上时, 数据源/提议人/验证机制/治理被操纵或失效的风险 — 判定生产线的**机器故障**。
- 数字: 攻击的经济学判据一行: 操纵 oracle 的成本 < 相关市场的可窃取金额 → 攻击在理性上必然发生 — 安全是算出来的, 不是承诺出来的。
- 实例: UMA (Polymarket 的主裁决层) 2025-26 的三连争议, 把三个结构缺陷钉上公告板: 投票权可以买、挑战激励可能不足、语义缝隙投票解决不了 — 行业教科书级的实证。

### mechanism
oracle-risk 与下一关 resolution-risk 的分界必须刻进肌肉: oracle-risk 是**机器坏了** (数据管道被操纵、提议人说谎、投票被收买、节点宕机) — 即使事实清晰, 机器也输出错误; resolution-risk (下下关) 是**规则本身裁不了** (语义歧义) — 即使机器诚实, 也无正确答案可输出。oracle 攻击面的清单: 数据源污染 (喂假数据)、提议操纵 (抢先提议错误结果赌无人挑战)、治理攻击 (买投票权改判 — 当判定代币市值 < 待判市场规模, 这不是理论)、时序攻击 (在挑战窗口边缘卡点)。机构问「你们的判定为什么可信」时, 按这张清单逐项给出成本估算 — 这就是把安全从形容词变成数字。

### traps
- ✗「用了大牌 oracle = 安全」→ ✓ 安全性随**被保护金额**变化: 同一个 oracle 保 $1M 市场绰绰有余、保 $1B 市场就成了全场最便宜的攻击面 — 安全预算必须随市场规模重算。

### ammo
- EN: "Oracle risk is when the truth machine breaks — bought votes, poisoned feeds, lazy challengers. UMA's back-to-back disputes proved the failure modes are structural, not anecdotal. Price the attack, don't trust the brand."

## quest: concept:dispute-mechanism

### hook
判定机器一定会出错 (7% 的争议改判率就是证据)。成熟系统和玩具系统的差别不在「不出错」, 在「错了之后发生什么」。

### card
- 本质: 有人认为拟判结果错误时, 系统推翻或维持它的程序 — 质押挑战 / 投票 / 升级仲裁 / 运营方裁定, 四种基本设计。
- 数字: 评估任何争议机制三问: 挑战成本多少 (门槛太高 = 没人纠错) / 谁做终审 (代币持有人? 委员会? 运营方?) / 期限多长 (资金被锁多久)。
- 实例: UMA 的完整流水线: 提议人质押提出结果 → 挑战窗口内任何人可质押反对 → 无人挑战即生效, 有人挑战交 DVM 代币投票终裁 — 「乐观 + 博弈」设计的代表作, 优点与伤疤都最公开。

### mechanism
四种设计是四种权力结构: ① 运营方裁定 — 快、终局, 但「既开赌场又当法官」(中心化风险裸露); ② 质押挑战 (乐观机制) — 平时零成本, 靠「说谎会被挑战没收质押」威慑, 死穴是挑战激励不足时错误静默生效; ③ 代币投票 — 去中心化终审, 死穴是投票权可购买 + 投票人未必读得懂语义争议; ④ 升级仲裁 (混合) — 逐级上诉, 用复杂度换稳健。没有正确答案, 只有**与市场规模匹配**的答案 — 判定标的越大, 越需要挑战激励与终审权力的加固。这里的产业空位: 不当法官, 当**法庭观察员** — 实时监控每个机制的争议状态、历史胜率、当前脆弱度, 把「裁错概率」做成可度量的数据。

### traps
- ✗「有争议机制 = 判定可信」→ ✓ 机制的存在只是下限; 参数 (挑战成本/窗口长度/终审构成) 决定它是真防线还是装饰 — 读参数, 不读白皮书的形容词。

### ammo
- EN: "Every resolution machine errs — the question is what happens next. Four designs, four power structures: operator fiat, optimistic challenge, token vote, escalation. The open role isn't refereeing — it's watching the referees."

## quest: concept:resolution-risk

### hook
你研究三个月, 方向判断完全正确 — X 确实赢了。合约却按 NO 结算, 因为「赢」在条款里的定义和现实的展开方式错了位。这种亏损没有名字的话, 它就会一直被当成「运气不好」。

### card
- 本质: 由规则歧义、来源冲突、时间窗错位、裁量争议导致「最终支付 ≠ 交易者合理预期」的风险 — 事件市场**区别于一切价格市场**的原生风险。
- 数字: 与 oracle-risk 的分界再钉一次: 机器坏了 (oracle) vs 规则裁不了 (resolution) — 前者攻击可定价, 后者歧义要逐条款排查。
- 实例: 判定风险的日常形态: 边界情形无条款覆盖、两个权威来源打架、事件以「没人想到的方式」发生 — 每一次行业争议事件几乎都能归入这三类。

### mechanism
把生产线的故障树画完整: 事实发生 → [来源风险: 出不出数/清不清楚] → [语义风险: 条款盖不盖得住] → [oracle 风险: 机器诚不诚实] → [争议风险: 纠错程序公不公正] → 支付。resolution-risk 是整棵故障树的**总和名称** — 它不可对冲 (你找不到「判定出错」的反向合约… 直到下一关)、难以分散 (同一 venue 的判定机制是系统性共因)、且被普遍错误定价 (散户按「事件概率」定价, 职业按「判定机器输出的概率」定价 — 差值就是职业玩家的午餐)。机构进场卡在哪, 这一关就是答案: 方向风险他们会管, 判定风险没有工具 — 这个赛道的机会用一句话说完: **给这棵故障树装仪表**。

### traps
- ✗「判定风险是小概率长尾」→ ✓ 7% 的争议改判率 + 每次改判都是 100% 的支付反转 — 低频×全额 = 期望损失不可忽略, 且在组合层面是共因风险 (一次机制失灵打穿全部相关持仓)。

### ammo
- EN: "You can be right about the world and still lose the trade — that's resolution risk, and it's what makes event markets different from every price market. Institutions can manage direction; nobody has instrumented the resolution failure tree yet."

## quest: concept:resolution-insurance

### hook
如果「方向对了但裁错了」是一种可识别、可统计的损失 — 那按保险业五百年的逻辑, 它就应该可以定价、可以转移。这个产品今天还不存在。「还不存在」是这一关最重要的三个字。

### card
- 本质: 针对判定风险的转移工具: 持仓人付保费, 若市场以特定争议形态错误结算, 获得赔付 — **当前是候选概念, 不是成熟产品类别**。
- 数字: 可保性三前提: 损失可清晰定义 (什么算「裁错」?) / 频率可统计 (争议底数数据) / 定价方与承保方信息对称 (需要中立的判定风险数据 — 看出闭环了吗)。
- 实例: 概念验证的原材料已在行业桌上: 争议历史数据、改判率、机制脆弱度 — 缺的是把它们变成保单的定价引擎。

### mechanism
为什么它还不存在: ① 「裁错」的定义本身可争议 (改判 = 纠正了错误, 还是制造了错误?) — 保单的触发条款会遇到和事件合约一样的语义问题 (递归!); ② 逆向选择剧烈 — 最想投保的人恰是最清楚该合约语义有毒的人; ③ 定价数据垄断在无人系统性收集的角落。三个障碍的公因子都是**数据与判定风险计量** — 也就是说, 谁先建成判定风险的计量层, 谁就握着这个未来产品的定价引擎。这条演化路径可以这样看: 先有仪表, 仪表的读数积累成精算表, 精算表才是保险产品的入场券。注意分寸: 这是**行业可能的演化方向**, 不是任何人的产品承诺。

### traps
- ✗「这产品不存在 = 不值得谈」→ ✓ 恰恰相反 — 「已识别、可统计、未定价」的风险是金融史上每一次产品创新的标准起点 (信用违约互换出现前, 信用风险也「没法转移」); 谈它 = 展示你看得到行业的下一步。

### ammo
- EN: "Resolution insurance doesn't exist yet — and that's the interesting part. The loss is identifiable, the frequency is countable, the pricing data is nobody's. Whoever instruments resolution risk first owns the actuarial table of a product waiting to be born."

## quest: concept:settlement-methodology

### hook
「事实发生」到「钱到账」之间不是一步, 是五步 — 而机构签约前会要求你把五步全部写成文件。能把这份文件讲清楚的人, 在这个行业里少得惊人。

### card
- 本质: 一张事件合约从事实到入账的完整规则链: 判定谁赢 → 按什么价结算 → 何时结算 → 走什么轨道支付 → 出错如何回滚 — 五层规程书。
- 数字: 五层每层一问: Who decides / At what price / When / Through which rail / What if wrong — 这五问是你尽调任何 venue 的杀手锏清单。
- 实例: 用五问对比双雄: Kalshi (监管判定程序→$1/$0→清算体系→受监管轨道→行政申诉路径) vs Polymarket (oracle 判定→$1/$0→即时→链上 USDC→争议窗口内可挑战、生效后不可逆)。

### mechanism
这一关是「结算」(序章) 与「判定」(本章) 的合流点: resolution 只回答第一问, 后四问 (价格/时点/轨道/回滚) 各有自己的风险面 — 多结果盘部分结算的价格规则、判定与支付之间的时滞敞口、轨道的冻结点 (第四章)、以及最被忽视的第五问: **生效后发现裁错了怎么办** — 链上兑付不可逆意味着「回滚」在技术上不存在, 唯一防线被压缩到生效前的争议窗口 (dispute 关的参数在此显出全部分量)。把五层规程做成结构化数据、跨 venue 可比 — 这就是 settlement intelligence 这个词组的字面工程含义。

### traps
- ✗「判定完成 = 结算完成」→ ✓ 判定只是五层的第一层 — 后四层每层都能独立出事; 把 methodology 讲成「谁赢谁拿钱」的人, 尽调问卷第三页就会被问穿。

### ammo
- EN: "Resolution answers who won. Settlement methodology answers four more questions — at what price, when, over which rail, and what happens if it's wrong. Institutions sign after page five, not page one. Making page five legible across venues is literally what settlement intelligence means."

## quest: concept:contract-equivalence

### hook
基金想做的事很简单: Kalshi 买 YES, Polymarket 买 NO, 锁定 4 分价差。这笔「无风险套利」成立的前提是一份没人出具过的文件: 证明两张合约**真的是同一个东西**。

### card
- 本质: 判断两个 venue 的合约是否代表同一经济事件与同一 payoff 的**判决程序** — 跨市场套利、对冲、净额的合法性地基。
- 数字: 判决四层比对 (语义五要素为底): 谓词等价? 来源等价? 时间窗等价? 判定机制等价? — 四层全过才敢叫等价, 任何一层存疑即有 basis。
- 实例: 行业已在为它建基础设施: Dome 曾以跨平台市场匹配 API (get-matching-markets) 切入此题后被收购 — 「匹配」能力本身成为被收购标的, 说明这个问题的产业价值已被定价。

### mechanism
等价性判决是第二章 basis-risk 的解药工序: 逐层比对两张合约的 DNA, 输出的不是「等价/不等价」的二值, 而是**风险分级** — 完全等价 (可套利可净额) / 条件等价 (在 X 情形下分叉, 分叉概率可估) / 名义等价 (同题不同义, 对冲即裸奔)。这个判决的价值链条: 交易层 (套利者的入场许可) → 风控层 (跨 venue 敞口能否合并计算, cross-margin 关的伏笔回收) → 清算层 (未来跨 venue 净额的前提)。为什么它是一项稀缺能力: 判决需要同时读懂语义 (法律功)、判定机制 (工程功)、市场结构 (金融功) — 三种能力的交集小到几乎没有竞争者, 而判决书的每一份输出都直接站在机构资金的闸门上。

### traps
- ✗「等价性是二值判断」→ ✓ 是**条件概率判断**: 「在 95% 的事件展开路径上等价, 在争议路径上分叉」— 把分叉概率算出来, 判决书才从法律文书变成风险定价输入。

### ammo
- EN: "Cross-venue arbitrage assumes a document nobody issues: proof that two contracts are the same thing. Equivalence isn't binary — it's a probability of divergence across event paths. Underwriting that probability is the signature unsolved product."

## quest: concept:canonical-event-id

### hook
「特斯拉 Q4 交付超预期吗」在四个 venue 上是四张不同措辞的合约。基金的风控系统想问一个再普通不过的问题: 「我在**这个事件**上总敞口多少?」— 今天没有任何系统答得出来, 因为「这个事件」在数据层根本不存在。

### card
- 本质: 跨平台给「同一现实事件」建立稳定唯一标识, 把各 venue 的合约归拢到同一事件之下 — 事件维度数据聚合的**主键**。
- 数字: 没有主键的世界: 敞口按 venue 割裂、监控按合约割裂、事件维度的一切聚合分析在数据结构上不可能 — 主键是「事件作为资产类别」的第一块地基。
- 实例: OpticOdds 对 canonical 标识的处理是本赛道最锋利的实践: **只返回真正跨平台匹配的事件** — 把「匹配」做成产品约束而非尽力而为, 宁缺毋滥的工程哲学。

### mechanism
canonical-event-id 是上一关的工程结晶: 等价性判决回答「这两张合约是不是同一事件」, 判决结果沉淀为数据结构就是 canonical id — 每个现实事件一个主键, 各 venue 合约作为它的子节点挂载, 等价性分级标注在边上。有了主键, 三件此前不可能的事变成 SQL 查询: 跨 venue 事件敞口聚合 (event-var 的数据前提, 第七章接力)、跨市场操纵监控 (同一事件在 A 场拉价、B 场收割 — 无主键则永远隐形)、事件维度的历史分析。深刻之处: 主键的质量**就是**等价性判决的质量 — 错误的归并比不归并更危险 (把不等价的合约合并计算敞口 = 风控系统里埋雷)。所以这不是爬虫+字符串匹配的活, 是判决驱动的数据工程 — 门槛即护城河。

### traps
- ✗「事件匹配是个 NLP 问题」→ ✓ 标题相似度只能做候选召回; 归并判决必须过语义四层比对 — 用 NLP 直接归并的系统, 会在第一次「同题不同义」争议里把客户的风控表变成事故报告。

### ammo
- EN: "Ask any fund a trivial question — 'what's my total exposure to this event?' — and no system on earth can answer it, because 'this event' doesn't exist as a data object. Canonical event IDs create it. The catch: the ID is only as good as the equivalence ruling behind it — merging two non-equivalent contracts is worse than not merging at all."
