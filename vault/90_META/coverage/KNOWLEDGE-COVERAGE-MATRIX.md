# KNOWLEDGE COVERAGE MATRIX | 知识覆盖矩阵

> 状态词表: `unmapped` / `seeded` / `partially-covered` / `well-covered` / `needs-refresh`。**没有 "complete"** — 缺口永远可见。更新: **2026-08-27 (第二轮: 语料导入 + 四路核验 + 独立审计)**。

## ⚠ 覆盖度 ≠ 可靠度 (独立审计 2026-08-27 的核心提醒)

本表衡量的是「**有没有页面**」, 不是「**页面可不可信**」。审计发现: 341 页里 76 页标 `verified`, 但 22 个 source note 中**只有 2 个有 content_hash**, 19 个 URL 来源**无快照** ⟹ 当前的 "verified" 多数意味着「**存在一个引用形状的指向**」, 而不是「**被引材料已保全且确实支持该断言**」。
**⟹ 例行事实依赖前必须带可见 caveat; GBrain 索引前必须先建保密过滤导出。** 详见 CODEX-AUDIT-REPORT。

| Domain | 重要性 | 覆盖 | verified | seed | 缺概念 | 缺人物 | 缺组织 | 来源质量 | 学习进度 | 下一步研究 |
|---|---|---|---|---|---|---|---|---|---|---|
| financial-markets | tier-1 | partially-covered | 0 | ~18 | 回购/ETF 机制、做市义务制度 | 传统交易所人物全缺 | DTCC/Euroclear/CME 详页 | workbook+手写, 一手引用未挂 | Stage 1 未开始 | 传统清算结算细读 |
| exchanges | tier-1 | well-covered | 11 venue | 3 | 上币机制、费率经济学专页 | 交易所二级高管 | Coinbase/Kraken/Upbit | 2026-08 web 核验 | Stage 2 未开始 | Coinbase 等美系 CEX |
| market-microstructure | tier-1 | partially-covered | 0 | ~17 | 队列位置、tick size、内化 | 学界 (Harris/O'Hara) | — | workbook | Stage 3 未开始 | Harris 选读→行内引用回填 |
| derivatives | tier-1 | partially-covered | 0 | ~25 | 期权希腊字母、SPAN 细节 | — | CME Clearing 详页 | workbook | Stage 4 未开始 | CFTC margin 提案精读 |
| blockchain | tier-2 | partially-covered | ~10 链页 | ~28 | MEV、账户抽象、restaking | Vitalik 等 | Solana/EigenLayer 页 | workbook+核验 | Stage 5 未开始 | EigenLayer (oracle 线牵引) |
| crypto-market-structure | tier-1 | well-covered | ~15 | ~12 | 永续资金费套利结构 | — | Coinbase/托管商补 | 2026-08 web 核验 | Stage 6 未开始 | 稳定币立法实施细则跟踪 |
| stablecoins-wallets-payments | tier-1 | partially-covered | 2 (Tether/Circle) | 2 | 支付轨费用结构、法币通道 | Ardoino/Allaire 人物页 | StraitsX/Paxos | 核验 | — | GENIUS 实施细则 (2026-07 出) |
| prediction-outcome-markets | **tier-1 主场** | well-covered | ~22 | ~24 | 组合保证金落地形态、税务 | Predict.fun "Ding" 实名、亚洲团队 | ANPRM「Suppliers to PMs」聚类其余申报者 (R17) | 一手 docs + 核验 | Stage 7 未开始 | R16 PDF 原文核对 · R17 竞争集合 · OKX 信号 |
| **pm-data-vendors** (新域) | tier-1 | partially-covered | 8 | 0 | — | Kairos/Predexon 创始人细节 | OpticOdds 定价 (R15) · 是否有未发现的 Tier A | 一手 docs/OpenAPI | — | R12 Predexon 是否向上爬 |
| institutional-risk | tier-1 | partially-covered | 0 | ~20 | 风险预算实操、委托书条款 | CRO 群像 | 风险供应商 (MSCI/Barra) 详页 | workbook | Stage 8 未开始 | 机构对话后回填真实痛点 |
| regulation-compliance | tier-1 | well-covered | 11 | ~4 | 州法细节逐州 | 州 AG 群像 | GRA (SG)/HKMA 独立页 | 一手监管源 | — | 🔴 **EU 咨询 9/30 截止 (卡 Irene)** · NPRM final 跟踪 (R7) |
| tron-ecosystem | tier-2 | well-covered | ~8 | ~6 | Energy 定价市场深度 | — | Sinohope 独立页 | 核验 | — | Energy 租赁经济学 |
| people-networks | tier-1 | well-covered | 17 人物 | 0 | — | 传统金融人物 · ANPRM 申报者群像 | — | 2026-08 核验 | — | R17 |
| industry-strategy | tier-1 | partially-covered | 0 | ~8 | 定价/打包策略比较 | — | — | workbook | — | 竞品定价调研 |
| learning | tier-1 | seeded | — | — | quizzes/self-assessments 未建 | — | — | — | 全部未开始 | Irene 跑第一个 session |

## 结构性缺口 (跨域)

0. 🔴 **证据保全缺失 (独立审计首要发现)**: 22 个 source note 只有 2 个有 content_hash; 4 份 research report 无外部 URL。**URL 一变就无法证明当初看到的是什么。** → R19, 需 Irene 决定优先级。
1. **对话导出未导入** → 09_ORIGINALS 缺第一手语境。
2. **行内一手引用未回填**: workbook 概念页的 sources 停在 workbook+URL 登记级; researcher 抓取回填是升 verified 的前提 (R5)。
3. **04_EVENTS 目录空**: 大事目前记在实体页 timeline; 高价值事件 (2025-10-10 清算风暴 / CZ 赦免 / HTX 制裁) 值得独立事件页。
4. **quizzes / self-assessments 空**: 等 Stage 1 实跑后按需生成, 不预造 filler。
5. **概念页深度不足 (审计发现)**: 134 个 workbook 导入概念中, 多数没有系统回答「为何存在 / 钱在哪 / 风险在哪 / 谁担损失 / 如何结算 / 什么会坏 / 实战怎么用」七问; 部分 active-recall 答案是「见上文」, 不构成独立答案键。→ 学习循环推进时逐个补, 不批量生成。
6. **查询基准只测文件存在性**: 15/15 的分数**不代表答案正确或有证据** (脚本输出已按审计意见改为明示这一点)。
