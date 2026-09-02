<h1 align="center">CryptoAtlas</h1>

<p align="center">
  <b>加密市场结构的知识图谱</b>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas"><b>🗺 打开图谱</b></a> ·
  <a href="CONTRIBUTING.md">➕ 补充或纠错</a> ·
  <a href="#english">English</a>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas">
    <img src=".github/assets/graph.webp" alt="CryptoAtlas 知识图谱" width="100%">
  </a>
</p>

加密这行的资料有两种：交易所的营销稿，和只有圈内人看得懂的黑话。中间那层——**这套东西到底怎么运转的**——很少有人写清楚。

这里是 143 个概念、76 个机构和人、75 条有出处的关系，按九个问题串起来。每条断言都写明了它的把握程度，说不准的地方直接写 `UNKNOWN`。

## 从哪读

九章按一条线走下来，每章回答一个问题：

| 章节 | 回答什么 | 会读到 |
|---|---|---|
| **序章 · 钱与风险的地图** | 为什么这个市场存在？谁需要它？ | 价格发现 · 做市商 · 清算所/中央对手方 · 结算 |
| **一 · 盘口的语言** | 我能以这个价格成交多少？大单会把价格推多远？ | 买卖价差 · 盘口深度 · 滑点 · 逆向选择 · 库存风险 |
| **二 · 风险的合约形态** | 我真正暴露于哪个 underlying？最坏要付多少？ | 二元/数字期权 · 基差风险 · 保证金 · 跨品种/跨头寸保证金 |
| **三 · 链上最小集** | 哪些必须上链？哪些链下更合理？信任假设是什么？ | 预言机 · 智能合约 · ERC-1155 · 自动做市商 |
| **四 · 钱的管道** | 钱在哪个平台？能否自由转移？谁能冻结？ | 托管 · 客户资产隔离 · 结算轨道 · 稳定币 |
| **五 · 事件市场本体** | 这个 contract 到底承诺什么？ | 事件合约 · 隐含概率 · 全额抵押 · 做市激励 |
| **六 · 结算与争议** | 谁决定事实？裁错了怎么办？ | 合约语义 · 指定结果来源 · 争议机制 · 结果判定风险 |
| **七 · 机构风险语言** | 看对方向以后，还有什么能让我拿不到钱或被迫退出？ | 事件风险价值 · 交易对手风险 · 集中度风险 · 监管准入 |
| **终章 · 从知识到系统** | 要让前面这些判断真正可用，必须先造出什么？ | 数据基础设施 · 可审计性 · 风险引擎 |

不想按顺序也行——图谱上点任何一个节点，Kalshi、Polymarket、Jane Street、CFTC、赵长鹏、USDT，都能从那里开始走。

## 一条词条长什么样

每个概念都有定义、机制、**带数字的例子**、常见误解、自测题。比如「滑点」那条里的算题：

> 某 YES 合约卖侧盘口：0.52 × 5,000 份 · 0.53 × 8,000 份 · 0.55 × 20,000 份。
> 你市价买入 $10,000。吃几档、成交均价、相对 best ask 的滑点是多少？
>
> 前两档吃掉 $6,840，剩 $3,160 进第三档买 5,745 份。共 18,745 份，均价 **0.5335**，
> 滑点 **2.6%**。在事件市场里这尤其致命：合约价格本身在 0–1 之间，1 分钱的滑点在
> 0.63 的合约上就是 1.6%，胜率 55% 的策略扣掉往返滑点可能直接变负。

机构和人的词条同理——不写「X 是一家大型做市商」，而是写它在这张图上的位置、谁跟它有关系、什么会让它退出。

## 为什么可以信

- **每条断言标着自己的证据等级**：confirmed / inference / hypothesis / unverified / unknown，直接写在页面上
- **`verified` 必须有来源笔记**，带内容哈希和访问日期；没有就进不了库
- **纠错是往时间线里追加一条**，不覆盖旧的——你能看到一个判断是怎么变的
- **说不准就写 `UNKNOWN`**，不猜

## 一起写

一家场馆改了费率、一个监管改了口径，笔记就过时了。你要是在这行，你一定知道一些这张图还不知道的事。

[提一个纠错 issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md)，或者直接改——`make validate` 会告诉你这条断言还缺什么。写法见 [CONTRIBUTING.md](CONTRIBUTING.md)。

内容 [CC BY 4.0](LICENSE-CONTENT)，工具 [Apache-2.0](LICENSE)。把 `VAULT_PATH` 指向你自己的库，同一套校验就作用在你的领域。

<br>

---

<a name="english"></a>

## English

**A knowledge graph of crypto market structure.**
[Open the atlas](https://ailinsun.github.io/cryptoatlas) · [Add or correct an entry](CONTRIBUTING.md)

Writing about crypto comes in two flavours: exchange marketing, and jargon only insiders
parse. The layer in between — **how this machinery actually works** — rarely gets written
down.

This is 143 concepts, 76 organisations and people, and 75 sourced relationships, strung
along nine questions. Every claim states how sure it is, and where nobody knows, it says
`UNKNOWN`.

### Where to start

| chapter | answers | you'll meet |
|---|---|---|
| **Prologue · A Map of Money and Risk** | Why does this market exist? Who needs it? | Price Discovery · Market Maker · Clearinghouse · Settlement |
| **1 · The Language of the Order Book** | How much can I fill at this price? How far will a large order move it? | Spread · Depth · Slippage · Adverse Selection · Inventory Risk |
| **2 · The Shapes Risk Takes** | What am I actually exposed to? What is the worst I can pay? | Binary/Digital Option · Basis Risk · Margin · Portfolio Margin |
| **3 · The On-Chain Minimum Set** | What must go on-chain, what belongs off-chain, and what am I trusting? | Oracle · Smart Contract · ERC-1155 · AMM |
| **4 · The Plumbing of Money** | Where is the money held? Can it move freely? Who can freeze it? | Custody · Custody Segregation · Settlement Rail · Stablecoin |
| **5 · Event Markets Themselves** | What is an event contract, and why is its price a probability? | Event Contract · Implied Probability · Fully Collateralized |
| **6 · Settlement and Disputes** | Who decides what happened — and what if they get it wrong? | Contract Semantics · Resolution Source · Dispute Mechanism |
| **7 · The Language Institutions Speak** | How do I express this exposure in the vocabulary of a risk desk? | Event VaR · Counterparty Risk · Concentration Risk · Regulatory Access |
| **8 · From Knowledge to Systems** | What has to be built for any of this to be usable at scale? | Data Infrastructure · Auditability · Risk Engine |

Or ignore the order — click any node on the graph. Kalshi, Polymarket, Jane Street, the
CFTC, CZ and USDT are all valid places to start.

### What an entry looks like

Every concept carries a definition, the mechanism, **a worked numeric example**, the
common misconceptions, and self-test questions. From the one on slippage:

> The ask side of a YES contract: 0.52 × 5,000 · 0.53 × 8,000 · 0.55 × 20,000.
> You market-buy $10,000. How many levels do you clear, at what average, and what is the
> slippage against best ask?
>
> The first two levels take $6,840; the remaining $3,160 buys 5,745 at the third.
> 18,745 contracts at an average of **0.5335** — **2.6%** slippage. This bites harder in
> event markets, where the contract itself trades between 0 and 1: a cent of slippage on
> a 0.63 contract is 1.6%, and a 55%-edge strategy can go negative on the round trip.

Entries on firms and people work the same way. Not "X is a large market maker", but where
it sits on this map, who it is connected to, and what would make it leave.

### Why you can trust it

- **Every claim carries its evidence tier** — confirmed / inference / hypothesis /
  unverified / unknown — visibly, on the page
- **`verified` requires a source note** with a content hash and an access date
- **Corrections append to a timeline** rather than overwriting it, so you can see how a
  judgement changed
- **Where nobody knows, it says `UNKNOWN`** instead of guessing

### Contributing

A venue changes its fees, a regulator shifts position, and a note goes stale. If you work
in this market, you know something this map doesn't.

[Open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md),
or fix it yourself — `make validate` names what a claim is still missing. Conventions are
in [CONTRIBUTING.md](CONTRIBUTING.md).

Content [CC BY 4.0](LICENSE-CONTENT), tooling [Apache-2.0](LICENSE). Point `VAULT_PATH` at
your own vault and the same checks apply to your domain.
