---
id: "lesson:chapter-0"
type: lesson
title: "Course Ch.0 Money and Risk"
title_zh: "课程 · 序章 钱与风险的地图"
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

# 课程 · 序章 (AI 教学层, 逐关分节; 视图解析 `## quest:` 分隔)

## quest: concept:financial-markets

### hook
一家航空公司怕油价涨, 一个基金想赌油价涨, 一家炼油厂手里囤着油。没有金融市场, 这三个愿望互相看不见; 有了它, 三个愿望变成一笔交易。

### card
- 本质: 让「有钱的」「要钱的」「怕风险的」「想接风险的」互相找到对方的系统。
- 数字: 记住一个分层 — 全球股票+债券市值以「百万亿美元」计, crypto 以「万亿」计, 事件合约以「百亿」计。你在最小、最年轻的那层工作, 但它长在整棵树上。
- 实例: Kalshi 上一张「Fed 三月是否降息」合约 — 有人在对冲利率风险, 有人在表达观点, 这就是金融市场的最小标本。

### mechanism
两个功能, 只有两个: ① 配置资本 — 钱从盈余方流向需要方 (买股票 = 给公司钱, 买债 = 借钱给它); ② 转移风险 — 风险从不想要的人流向愿意收费承接的人 (保险、期货、事件合约全是这个)。所有后面 80 关的机构、工具、规则, 都是在给这两个功能修管道: 交易所降低找到对方的成本, 清算降低对方赖账的成本, 结算把承诺变成钱。判断任何新产品, 先问: 它配置了什么资本, 转移了谁的风险? 答不出 = 大概率是赌博或庞氏。

### traps
- ✗「金融市场 = 炒买炒卖」→ ✓ 投机者是风险转移功能的**对手盘提供者**: 没有愿意接风险的人, 对冲者找不到人卸货。投机不是 bug, 是功能的一半。
- ✗「事件合约是新发明」→ ✓ 风险转移是最古老的功能, 事件合约只是把「非价格型风险」(选举/判决/天气) 也纳入了同一个系统。新的是标的, 不是逻辑。

### ammo
- EN: "Event contracts aren't a casino bolted onto finance — they extend finance's oldest function, risk transfer, to risks that never had a market before."
- 用法: 任何「这不就是赌博」的问题, 先退回这两个功能再回答。

### drill
Q: 一家上市博彩公司股价随世界杯赛果波动。基金买它的股票 vs 买世界杯事件合约, 哪个是更纯净的风险转移? 为什么?
A: 事件合约。股票混入了管理层、杠杆、市场贝塔等噪声; 事件合约只含赛果这一个风险因子 — 「纯净敞口」正是事件市场对机构的卖点。

## quest: concept:price-discovery

### hook
2024 年美国大选夜, 电视台还在等开票, Polymarket 的价格已经先动了。谁告诉市场结果的? 没有谁 — 这就是问题的答案。

### card
- 本质: 市场把散落在无数人脑子里的信息, 通过「用钱投票」压缩成一个数字。
- 数字: 一张事件合约价格 0.62 ≈ 市场认为 62% 概率发生 (先这么用, 第五章再修正这个近似)。
- 实例: 大选夜预测市场价格常领先电视台宣布数十分钟 — 因为知道消息的人会先下注, 价格先于新闻。

### mechanism
每个交易者按自己的信息和判断出价: 觉得便宜就买 (推高价格), 觉得贵就卖 (压低)。价格 = 所有人真金白银投票的实时均衡。关键在「真金白银」: 说错话免费, 下错注亏钱, 所以价格里的信息密度远高于民调和评论。价格发现的质量取决于: 参与者多样性 (信息来源不同)、流动性 (钱能进得来)、市场诚信 (没人操纵)。这三个条件坏掉任何一个, 价格就从「信息」退化成「噪音」— 后面第七章的 market-integrity 就是在保这个。

### traps
- ✗「价格是官方定的/做市商定的」→ ✓ 做市商只是报价, 成交才是投票; 做市商报错价会被套利者惩罚到改价。
- ✗「价格永远是对的」→ ✓ 价格是**当前信息分布的均衡**, 不是真理。流动性差、参与者单一时, 价格可以错得很稳定。

### ammo
- EN: "Prediction market prices aren't opinions — they're the running settlement of everyone's stakes. That's why they move before the news does."

### drill
Q: 同一事件, Kalshi 价格 0.55, Polymarket 0.60。这说明价格发现失效了吗?
A: 不一定 — 两个场子参与者、费率、合约措辞可能不同 (第六章 contract-equivalence 会教你逐层判断); 若确认合约等价, 5 分差价 = 套利空间, 套利者会把它抹平 — 套利就是跨场价格发现的执行者。

## quest: concept:exchange

### hook
为什么骗子可以开一个「交易所」网站, 却开不出一个真交易所? 差的不是撮合代码 — 那是最便宜的部分。

### card
- 本质: 卖「规则 + 撮合 + 准入 + 行情」的市场基础设施, 它本身通常不是你的对手方。
- 数字: 尽调任何 venue 只需四问 — 市场模型 / 托管 / 结算 / 监管 (这四件套会贯穿全部 81 关)。
- 实例: Kalshi (受监管的美国事件合约交易所) 和 Polymarket (链上结算的全球场) 是你的两个永久参照系。

### mechanism
交易所把「找到对方」的成本打到接近零: 统一合约规格 (大家买卖同一个东西)、集中订单流 (买卖方在同一个池子)、公开行情 (人人看到同一价格)。但注意它**不碰**的三件事: 通常不当对手方 (对手方是另一侧交易者, 或清算所)、不保证你赚钱、不必然托管你的资产 (取决于架构)。所以评估 venue 永远问四件套: 怎么撮合定价? 钱在谁手里、谁能冻结? 赢了怎么真正拿到钱? 牌照是谁发的、出事找谁? 四问里任何一问答不清 — 那不是交易所, 是柜台后面的一个人。

### traps
- ✗「交易所 = 和我交易的公司」→ ✓ 那是 dealer 模式 (支线)。交易所是场地, 你的对手是场上另一个人。混淆这两者 = 看不懂利益冲突在哪。
- ✗「上了交易所 = 安全」→ ✓ 交易所只保证撮合规则, 不保证托管安全和结算兑现 — FTX 的撮合引擎到最后一天都运行良好。

### ammo
- EN: "An exchange sells matching, rules and access — custody and settlement are separate questions, and that's exactly where institutions get hurt."

## quest: concept:market-maker

### hook
你随时打开 Polymarket 都能立刻买到「Fed 降息 YES」。谁规定必须有人 24 小时站在对面等你? 没人规定 — 有人收费干这个。

### card
- 本质: 用自有资金持续挂出买价和卖价、卖「即时性」的专业机构, 靠价差补偿自己承担的两种风险。
- 数字: 记两大成本 — 逆向选择 (被更懂的人挑着打) 和库存风险 (接了货价格跑) ; 价差 = 这两个风险的保险费。
- 实例: Wintermute 2026-05 官宣同时在 Polymarket 和 Kalshi 做市 — 事件市场机构化的标志信号; Susquehanna (SIG) 2024 起就是 Kalshi 的旗舰做市商。

### mechanism
做市商在 0.60/0.62 挂双边: 有人买它就 0.62 卖出, 有人卖它就 0.60 接进, 一来一回赚 0.02。听起来像印钞, 直到: ① 一个知道内幕的人只在你报价错误时成交 (逆向选择, 第一章细讲); ② 你接了一堆 YES, 事件反转, 库存全亏 (库存风险)。所以做市商的真实工作是风险管理: 动态调价差宽度、控制库存上限、跨市场对冲。venue 没有做市商 = 空盘口 = 机构进不来 — 这就是为什么新市场要花钱请做市 (第五章 market-maker-incentive), 也是为什么做市商往往是风险工具的第一批用户: 他们是全场风险最敏感、数据最饥渴的人。

### traps
- ✗「做市商操纵价格」→ ✓ 做市商是价格的**乘客**不是司机: 它跟着订单流调价, 主动偏离均衡会被套利。操纵者是另一类人 (第七章)。
- ✗「价差是交易所收的费」→ ✓ 价差归做市商, 是风险补偿; 交易所费率是另一笔钱。机构算成本必须分开算这两项。

### ammo
- EN: "Market makers are the ones who turn a listed contract into a tradable one — and in event markets, they're bleeding on exactly the risks nobody measures yet: semantic mismatch and resolution uncertainty."
- 用法: 对 MM 的开场白从他们的两大成本切入, 立刻证明你懂行。

### drill
Q: MM 在 0.60/0.62 双边挂 $50k, 当天成交量五五开共 $200k, 无库存残留。毛利多少?
A: 每回合赚价差 0.02, $200k 成交 ≈ $100k 买+$100k 卖配对 → 毛利 ≈ $100k × 0.02 ≈ $2,000。再扣逆向选择亏损与费率, 才是净利 — 这就是为什么 MM 对「谁在跟我交易」如此敏感。

## quest: concept:clearing

### hook
你在 Kalshi 赢了 $10 万。从「成交回报」到「钱可提现」之间, 有一段你看不见的机器在转。看不见的部分, 恰恰是机构最在意的部分。

### card
- 本质: 成交之后、结算之前的中间层 — 确认双方义务、多边净额、管理保证金、处置违约。
- 数字: 净额的威力 — A欠B 8、B欠C 6、C欠A 5, 双边要动 19, 净额后只动 3 (序章练习 Q6 亲手算过)。
- 实例: 传统市场成交后由清算所接管; Polymarket 的「清算」被智能合约结构替代 — 全额抵押让违约管理直接消失 (第五章重逢)。

### mechanism
成交只是两个人「说好了」; 清算把说好变成可执行: ① 确认 — 双方义务登记核对; ② 净额 — 千笔对冲成一笔净头寸, 结算量和风险敞口一起坍缩; ③ 保证金 — 按净头寸风险收押金, 价格波动时追加; ④ 违约管理 — 谁交不出钱, 按预案处置。这四步的存在理由只有一个: 从成交到结算有时间差, 时间差里对方可能死掉。时间差越长、杠杆越高, 清算越重; 反之, 事件合约全额抵押 + 即时结算的架构里, 清算被压缩到几乎不可见 — 理解这个「压缩」是理解 CFTC 保证金化辩论 (第二章) 的钥匙。

### traps
- ✗「清算 = 结算」→ ✓ 清算是管理承诺, 结算是履行承诺。中文里俩词常混用, 机构对话里混用一次就露怯。
- ✗「链上不需要清算」→ ✓ 是全额抵押消灭了违约风险, 才不需要传统清算; 一旦事件合约引入保证金 (CFTC 正在讨论), 清算层整套回归。

### ammo
- EN: "Clearing exists because there's a gap between promise and payment. Fully-collateralized markets shrink that gap to zero — margined event contracts would reopen it, and that's the real stake of the CFTC debate."

## quest: concept:clearinghouse

### hook
2008 年雷曼倒下, 和它做过衍生品交易的机构排队数年清点残局; 同期在交易所清算的合约几天内有序了结。同一场危机, 两种结局 — 差的是中间那个机构。

### card
- 本质: 站进每笔成交中间、变成「所有买方的卖方、所有卖方的买方」的机构 (CCP), 用分层资金瀑布吸收违约。
- 数字: 瀑布顺序 — 违约者保证金 → 违约者基金份额 → CCP 自有资本 → 存活会员共担。层层递进, 你只需记顺序。
- 实例: Kalshi 2024-08 拿到自有清算所 Kalshi Klear (DCO) — 一家事件合约交易所自建 CCP, 这是它机构叙事的核心资产。

### mechanism
没有 CCP: 你的每笔交易信用都取决于「具体对面那个人」, 机构要给每个对手方做尽调、设额度。有 CCP: 成交瞬间被替换成「你 vs CCP」+「CCP vs 对方」两笔 — 你从此只面对一个对手方, 而这个对手方用瀑布结构把任何单点违约摊到整个体系。代价: CCP 自己成了系统最大单点, 所以它被最重的监管盯着 (资本、压力测试、恢复计划)。看懂 CCP, 你就有了评估任何市场信用结构的标尺: 问「谁站在中间, 它的瀑布有几层, 每层多厚」。链上全额抵押的答案是「没人站中间, 因为智能合约把最坏支付提前锁死了」— 两种哲学, 第五章正面对撞。

### traps
- ✗「CCP 消灭了风险」→ ✓ 只是**集中并互助化**了风险; 极端日 CCP 本身可能成为传染源 — 这是机构风险对话的高级弹药。
- ✗「Polymarket 没有清算所 = 不安全」→ ✓ 它用 100% 抵押替代 CCP 职能; 两种模式各付各的代价 (资本效率 vs 信用分层), 不是谁更「正规」。

### ammo
- EN: "A clearinghouse is where counterparty risk goes to be mutualized. Smart-contract escrow is where it goes to be eliminated — at the price of capital efficiency. Every venue picks one."

## quest: concept:settlement

### hook
「账面盈利」和「钱到账」之间隔着什么? 隔着一整关。这关的名字叫结算 — 整条 settlement-intelligence 命题就长在这条缝里。

### card
- 本质: 把承诺变成事实 — 钱和资产真正换手、且不可撤销的那一刻。
- 数字: 传统证券 T+1 (隔天), 链上 finality 以秒/分钟计, 事件合约 = 事实判定后支付 $1/$0 — 三种节奏, 三种风险窗口。
- 实例: Polymarket 的结算 = Polygon 链上 USDC 按 outcome token 兑付; Kalshi = 清算体系内账务交割。同一个「赢了」, 两条完全不同的到账路径。

### mechanism
结算的全部学问在三个词: 什么时候 (T+N / 即时)、走什么轨道 (银行账本 / 证券系统 / 区块链)、能不能反悔 (finality)。窗口越长, 中间死掉的方式越多 (对手方破产、银行冻结、链重组) — 这些统称结算风险 (第七章)。事件合约的特殊性: 它的结算多了一个前置环节 —「事实判定」(resolution, 第六章), 于是风险窗口从「成交→交割」延长为「成交→事实发生→判定→交割」, 每一段都能出错。值得注意的是: 行业都在盯价格, 没人系统性地盯这条结算链 — 而机构的钱恰恰死在这条链上。

### traps
- ✗「成交了就是我的了」→ ✓ 成交产生的是债权, 结算才产生所有权。倒闭的交易所里, 「已成交未结算」的用户排在债权人队伍里。
- ✗「链上 = 即时结算 = 无结算风险」→ ✓ 链上转账即时, 但事件合约的结算取决于 oracle 判定 — 链的速度救不了判定的错误。

### ammo
- EN: "Settlement is where promises become facts. In event markets the chain is longer — trade, event, resolution, payout — and every extra link is a place institutions lose money. That chain is where the unsolved problems live."

### drill
Q: 用「结算三问」(何时/什么轨道/可否反悔) 各一句话回答: Kalshi vs Polymarket。
A: Kalshi — 事实判定后, 走受监管清算体系内部账务, 监管框架下有争议处置程序; Polymarket — 判定后即时, 走 Polygon 链上 USDC, 链上兑付不可逆 (所以判定层的争议机制成为唯一防线 — 第六章的主战场)。
