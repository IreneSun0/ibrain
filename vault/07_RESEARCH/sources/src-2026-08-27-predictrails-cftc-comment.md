---
id: "source:2026-08-27-predictrails-cftc-comment"
type: source
source_type: regulatory-filing
title: "PredictRails comment to CFTC Prediction Markets ANPRM (comment 115352)"
publisher: PredictRails (filed with CFTC)
author: Michael Izhaky
published_at: 2026-04-29
accessed_at: 2026-08-27
url: "https://comments.cftc.gov/PublicComments/ViewComment.aspx?id=115352"
primary_source: true
reliability: medium
content_hash: ""
archive_path: ""
status: seed
importance: tier-1
domains:
  - prediction-outcome-markets
  - regulation-compliance
  - industry-strategy
tags:
  - source
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2026-10-27
confidence: medium
epistemic_status: mixed
confidentiality: public-source
sources: []
related:
  - "person:michael-izhaky"
---

# Source: PredictRails 致 CFTC ANPRM 评论 (comment 115352)

## What This Source Is

PredictRails 对 CFTC「Prediction Markets」**ANPRM** (RIN 3038-AF65, FR 2026-05105) 的公开评论。

- **Comment ID 115352** · 日期 **2026-04-29** · **21 页** (附件形式)
- 签署人 **Michael Izhaky** / PredictRails; 文件内联系邮箱 `michael@predictrails.ai`
- 原文 PDF: <https://comments.cftc.gov/Handlers/PdfHandler.ashx?id=35886>
- 评论目录: `comments.cftc.gov/PublicComments/CommentList.aspx?id=7654` (该 ANPRM 共收约 3,500 条评论)

## ⚠ 证据链诚实说明 (reliability: medium 的原因)

**原始 PDF 本轮未能打开** — `comments.cftc.gov` 对自动化访问出示 Cloudflare 人机验证挑战 (我们不绕过 bot-detection)。以下内容摘自独立追踪站 **Prediction Market Pulse** 的 ANPRM 数据集 (2026-05-27 提取, 含 comment ID 与 PDF handle, 其 UI 标注为「Excerpt — see official comment」)。

⟹ **档位: SINGLE-SOURCE (聚合站转引)。** 引用具体措辞前, **必须由人在普通浏览器里打开上面的 PDF handle 核对原文**。→ 研究队列 R16。

Prediction Market Pulse: 独立美国预测市场追踪站, 由 Josh Pearl (前 Penn Interactive 高管, 受监管博彩) 与 Grant Hartman (Chariot Solutions) 运营; 其数据集从全部记录中筛出 314 条实质性申报做分类。

## 六条核心主张 (摘录)

1. 机构参与的约束是**基础设施, 不是需求** ("infrastructure, not demand")
2. 首要问题是**裁决歧义** (resolution ambiguity), 不是市场准入或产品范围
3. 事件合约分两类 (**到期型 vs 触发型**), 需要不同的保证金/监察/风险方法
4. **canonical 合约标识符**是仓位限额、跨场馆聚合与监察的前提
5. **结算 oracle 是独立的风险向量** (数据覆盖、修订、可操纵性)
6. **cross-margining 对机构跨场馆参与是必需的**; 监管应「技术中立、基础设施优先」

**姿态声明 (原文)**: 「We do not offer legal conclusions or policy recommendations on the permissible scope of event contracts.」— 该 docket 中唯一明确采取「不提政策建议」姿态的申报。

## 它请求 CFTC 做什么

- 要求所有 DCM 上市事件合约提供**结构化、机器可读的裁决规格**, 需枚举: 结算 oracle (具体数据集/发布物) · 触发定义 (阈值/平滑或平均方法/结算类型) · **数据修订的处理** (含合格 vs 不合格修订的非对称处理) · oracle 已知覆盖限制 · 出现分歧时的权威发布面 · 争议升级程序
- 建立**裁决事件类型的标准化分类**, 「类比 ISDA 的信用事件定义」
- DCM 发布**结算 oracle 可靠性评估** (覆盖范围/已知排除/历史可靠性/可操纵性) — 「目前不存在评估结算机制是否适用的标准化框架」
- 结构化**争议解决程序** (定时限、升级路径、公开先例), 「参照 ISDA determinations committee」
- **成立工作组** (可能设在 CFTC Innovation Advisory Committee 内) **制定标准化事件合约标识符规范**, 借鉴 CUSIP Global Services、ANNA、ISDA 的参考数据基础设施
- 论证现有标识符不够用: CUSIP/ISIN 为静态参考数据的证券设计; 事件合约的身份由**裁决标准、裁决来源、到期与所指事件**定义; LEI 标的是法律实体不是工具, 与合约标识问题正交

## 它摆出的证据

- **市场规模**: $9B (2024) → $44B (2025) → **$275B 年化 (2026 初)**
- 🔑 **霍尔木兹海峡案例 (2026-03, 成交 $25M+)**: 合约标题暗示的是宽泛的航运判断, 而操作性规则是「IMF PortWatch 的 7 日移动平均通行船次须 ≥ 60」。识别出六类结构性风险: 标题与触发不匹配 · 来源模型依赖 · **过滤实体风险** (只统计 AIS 报告船只; 关闭应答器的船不可见 — 据称实地校验发现 AIS 漏掉约一半实际通行, 含数十艘油轮) · 平滑方法 · **修订非对称** (修订可以把结果改成 YES, 却无法撤销一个已合格的读数) · 发布面歧义 (图表 vs 可下载文件)
- **CDS/ISDA 先例论证**: 1999/2003 前的 CDS 有定制条款、参考实体标识不一致、裁决有争议; ISDA 标准化了信用事件定义、参考实体标识符 (Markit **RED codes**, 后为 LEI) 与裁决委员会 — 「预测市场今天处于可比的阶段」
- **跨市场外溢**: 当事件合约价格喂给相邻的大宗、外汇或保险市场时, 标题与实际结算机制之间的误导性关系会把错误假设传导进与该预测市场毫无直接联系的市场

## ⚠ 防误引 (重要)

有搜索引擎摘要把这句话归给 PredictRails: 「No two CFTC-registered prediction market platforms currently publish their market data in a standardized format…」
**它不是 PredictRails 的**, 出自 **First Strike Research** (comment 114879, 2026-04-10, PDF handle 35830)。PredictRails 的 handle 是 **35886**。**不得把该引文放在 PredictRails 名下。**

## 同 docket 的邻近申报 (「Suppliers to PMs」聚类)

Solidus Labs (Chen Arad) · Eventus Systems + Tölt Strategies (Dorothy D. DeWitt, **前 CFTC 市场监督主任**) · Vantage (自称首个独立第三方预测市场监察平台申报) · Vigilentis · Data Boiler Technologies (Kelvin To, 49pp) · MindCast AI · Convexly Research · Castle Technologies · Vitruvitas · FanLabel Music Markets。
⟹ **这是当前可见的同类参与者集合**, 值得逐个看 (研究队列 R17)。

## Freshness

accessed 2026-08-27 (聚合站转引) · **待人工核对原始 PDF** · review 2026-10-27
