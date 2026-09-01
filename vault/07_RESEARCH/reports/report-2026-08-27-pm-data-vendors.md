---
id: "report:2026-08-27-pm-data-vendors"
type: research-report
title: "Prediction-Market Data & API Vendor Landscape (2026-08)"
title_zh: 预测市场数据/API 供应商全景 (2026-08 核验)
aliases: []
status: reviewed
importance: tier-1
domains:
  - prediction-outcome-markets
  - industry-strategy
tags:
  - research-report
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2026-11-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related:
---

# 预测市场数据/API 供应商全景 · 2026-08-27 核验

> Tier B 竞品的证据基座。方法: 优先一手 (公司自家 docs / OpenAPI spec / changelog / `llms.txt`), 辅以独立媒体与投资方公告。**营销口径与规格口径冲突时以规格为准** (本轮抓到两处)。

## TL;DR — 五条改写认知的发现

1. 🔴 **场馆把聚合层吞了**: **Dome** (YC F25, $5.2M, 前类别领头, 做跨平台市场匹配 + 订单路由) **被 Polymarket 收购** (2026-02-19 公布, Polymarket 继 QCEX 后第二笔), 全部 API **2026-04-28 EOL**。详见 [[case-dome-acquisition]]。
2. **两个月后同一模式再现**: **Predexon** 退掉执行与匹配 — Trading API 2026-06-25 停, 跨场馆匹配端点 2026-07-20 起返回 `410 Gone`。它现在是**纯数据商**。 (早前的 Tier B 描述已过期约两个月。)
3. **canonical ID 不再稀缺**: 现在**至少三家**在做 — predictrails (`PR:` 标识符) · [[kairos]] (「one canonical Kairos market id on every venue」) · [[opticodds]] (`canonical_id` / `canonical_market_id`)。**S2 数据面的商品化已经发生**, 不是未来风险。
4. **漏了一个重要竞品**: [[opticodds]] — 体育赔率数据老玩家延伸进预测市场, **明确面向做市商**, 且 canonical 标识符的语义定义最锋利 (「同一个值出现在 Kalshi 与 Polymarket 上, 意味着这两个市场按同一件事结算」)。
5. **出现了 benchmark 位的占位者**: [[adjacent-markets]] (原 Adjacent News, 已改名) 自称「**第一家独立第三方事件合约与预测市场指数提供商**」, 已发 22 个指数 — 这正落在「标准维护者」这个位置上。

## 能力对照 (2026-08-27)

| 供应商 | canonical ID | 跨场馆匹配 | 裁决/结算元数据 | 执行 | 定位 |
|---|---|---|---|---|---|
| **Kairos** | ✅ 单一 canonical id | ✅ 4 场馆 | ✅ CTF split/merge/redeem, NegRisk, resolutions | ✅ NBBO 路由 + EIP-712 外部签名 | **机构** + 零售终端 |
| **OpticOdds** | ✅ `canonical_id`/`canonical_market_id` | ✅ (仅返回跨 ≥2 平台的事件) | 未文档化 | ❌ (给 native ID 供自行路由) | **机构 / 做市商** |
| **PredictRails** | ✅ `PR:` (待核验) | ✅ (待核验) | 声称含裁决质量评分 | ❌ | 机构 |
| **Predexon** | ❌ (已退) | ❌ (已退, 410) | ✅ **UMA oracle 状态+时间线 + WS oracle/lifecycle 频道** | ❌ (已退) | 开发者/量化零售 |
| **FinFeedAPI** | ❌ (`{exchange}/{market}` 作用域) | ❌ | 未文档化 | ❌ | 两者 (自助 + enterprise) |
| **Tatum** | ❌ (共享响应封装, 过滤器按场馆门控) | ❌ | 未文档化 | ❌ (只读) | 零售/开发者 |
| **Blockcircle** | ❌ (置信度评分配对) | ✅ 概率式, 6 场馆 | 未文档化 | ✅ 非托管智能路由 | 零售/prosumer |
| **Adjacent** | — (走指数路线) | — | — | ❌ | **指数/基准提供商** |

> 全部供应商都提供订单簿深度与历史数据 ⟹ **这两项已是入场券, 不是差异化**。

## 关键细节 (影响判断的)

**Kairos** (kairos.trade): a16z crypto 领投 **$2.5M seed**, 2026-02-03 公布; 创始人 Jay Malavia (Cboe 量化研究, 含早期预测市场项目; Geneva Trading; NASA ML) 与 Zayd Alzein (Cboe 低延迟数据流与订单簿重建)。公开上线 2026-06-26 — **入市约两个月**。覆盖 Kalshi/Polymarket/Predict.fun/**Hyperliquid** (唯一覆盖四家)。scoped API key + IP 白名单; 定价按量报价不公开。⚠ 名称极易撞车 (Kairos Power 核电/Kairos 人脸识别/同名开源项目), 认域名。

**OpticOdds**: `canonical_id` 组同一事件跨平台, `canonical_market_id` 标同一结果跨平台; 端点只返回「成员横跨 ≥2 平台」的 canonical 事件; SSE 流全订单簿快照; 覆盖 Kalshi + Polymarket, 含**非体育**类 (选举/经济指标/加密价位/文化)。有专门的 *OpticOdds for Prediction Market Makers* 指南。

**Predexon** (predexon.com): 现为纯数据。**优势项 = UMA 裁决数据** (`/v2/polymarket/uma/markets`, oracle 状态与事件时间线, WS oracle 频道推送 proposal/dispute/settlement/reset)。另有 mempool 抢先 (「比 Polymarket RTDS 早最多 5 秒」, 一手营销未验)、tick 级历史 (Parquet)、钱包聚类与聪明钱。定价公开: Free / Dev $49 / Pro $249 / Enterprise $499+。⚠ **其定价页仍在卖已下线的 Trading API** — 营销与规格冲突, 以 OpenAPI spec 为准 (62 路径仅 1 个非 GET)。

**FinFeedAPI**: 母公司 **API Bricks** — 同时运营 **CoinAPI** (2017 起家)。即 CoinAPI 团队把交易所数据 schema 套到事件市场。覆盖 Polymarket/Kalshi/Manifold/Myriad/**Hyperliquid HIP-4** (与 Kairos 并列唯一覆盖 HIP-4 的两家)。**跨资产是其真差异化** (预测市场与股票/外汇/SEC filings 同一把 key)。

**Tatum**: 预测市场 API 真实存在 (`/v4/data/prediction`, 18 端点, doc 更新至 2026-08-21) 但**只有 Polymarket + Kalshi, 只读**。其自身文档诚实说明: 部分过滤器**只有 Polymarket 支持**, 不带 `platform=polymarket` 会返回 400 ⟹ 「归一化」= 共享响应封装, **不是统一工具模型**。

**Blockcircle**: 6 场馆 (Polymarket/Kalshi/Manifold/PredictIt/Metaculus/Opinion), 5,000+ 市场; 匹配是**置信度评分** (Cross Match scores) 非 canonical ID; 执行非托管、智能路由, **但锁在 $800/年档**。定价公开 (Free/$390/$800/$4,788 年)。

**Adjacent** (adjacent.markets, 原 adj.news — 旧 API 域名已 NXDOMAIN): 22 个指数 (政治期货指数、各类选举指数、预测市场衍生参考利率); 公开 API 无鉴权 CORS 开放但延迟 15 分钟; 创始人 Lucas Kohorst, pre-seed。

## 数据质量说明

最强证据: Predexon (机器可读 OpenAPI spec + 带日期 changelog, 均已解析) · FinFeedAPI/Tatum (一手 `llms.txt` 与 `.md` 文档源) · Dome (一手文档横幅 + 独立媒体) · Kairos 融资 (a16z + Fortune 双源)。
最弱证据: **一切规模与性能数字** (Blockcircle 各项指标 / Predexon「快 5 秒」/ Kairos「快 2-3 秒」) 均为一手营销未验。Predexon 创始人身份与「100+ 客户」为第三方单源, 暂按 provisional。
访问限制: finfeedapi.com 与 apibricks.io 对非浏览器客户端返回 403, 其预测市场定价页未能读取。

<!-- timeline -->

## Timeline

- **2026-08-27** — research agent 产出 (~65 次抓取/检索); 转录进 Tier B 实体页群与 [[case-dome-acquisition]]。
