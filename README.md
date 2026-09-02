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

143 个概念、76 个机构和人、75 条关系，全部标注出处，按九个问题串起来。

## 从哪读

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

## 纠错与补充

[提一个纠错 issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md)，或按 [CONTRIBUTING.md](CONTRIBUTING.md) 提交修改。提交前运行 `make validate`。

内容 [CC BY 4.0](LICENSE-CONTENT)，代码 [Apache-2.0](LICENSE)。

<br>

---

<a name="english"></a>

## English

**A knowledge graph of crypto market structure.**
[Open the atlas](https://ailinsun.github.io/cryptoatlas) · [Add or correct an entry](CONTRIBUTING.md)

143 concepts, 76 organisations and people, 75 relationships, all attributed, along nine questions.

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

### Contributing

[Open a correction issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md),
or submit a change following [CONTRIBUTING.md](CONTRIBUTING.md). Run `make validate`
before submitting.

Content [CC BY 4.0](LICENSE-CONTENT), code [Apache-2.0](LICENSE).
