---
id: "report:2026-08-27-kb-tooling-landscape"
type: research-report
title: "Knowledge-Base Visualization Tooling Landscape (2026-08)"
title_zh: 知识库可视化工具版图 (2026-08 核验)
aliases:
  - 工具版图
status: reviewed
importance: tier-2
domains:
  - meta
tags:
  - research-report
created: 2026-08-27
updated: 2026-08-27
last_verified: 2026-08-27
review_after: 2027-02-27
confidence: high
epistemic_status: confirmed
confidentiality: public-source
sources: []
related: []
---

# 知识库可视化工具版图 · 2026-08-27 核验

> 触发: Irene「去看一下有哪些顶尖开发者用的工具」。方法: GitHub REST API / npm / PyPI / VS Code Marketplace / Obsidian 官方 registry (6,989 插件) **实时拉取**版本号与最后提交日; 12 个月无 commit 判死。

## 结论: 我们不需要图数据库

320 节点 / 901 边的图, 按 Memgraph 官方内存公式算约 **435 KB**。在这个量级上性能基准全是噪音 —— 上图数据库只买到两样东西: **Cypher 语言** + **一个能点开的界面**。而后者用 Cytoscape.js + 一份 JSON 导出就能有, 不必背运维成本。

**推荐的三层, 按投入排序**:

| 层 | 工具 | 投入 | 给什么 | Bases 做不到的 |
|---|---|---|---|---|
| 库内工作台 | **Obsidian Bases** (核心功能, 免费) | ~0 | frontmatter 变可交互表格 | — |
| 全局可视化 | **自建控制台** (已建, `make console`) | 已完成 | 319 节点图谱 + 证据/战略/领域四视图 | — |
| 分析层 | **DuckDB 读导出 JSON** (`scripts/query.sql`) | ~1h | **真 SQL**: join / GROUP BY / 递归 CTE | 跨行聚合 |

## 五条推翻常见说法的核验结果

1. 🔴 **Kùzu 已死** — `kuzudb/kuzu` 仓库**已归档**, 最后 push 2025-10-10; Kùzu Inc. **被 Apple 收购** (2026-02 经欧盟申报曝光)。**所有 2025 年前的「用 Kùzu 做嵌入式知识图谱」教程全部作废。** 继任者是 LadybugDB (1,671★, MIT, 仍在 commit)。
2. **Obsidian 官方解决了数据库, 放弃了图**: Bases 从 2025-05 EA → **2025-08-18 全量 GA**, 之后拿到 API、三种新视图、group-by、汇总、PDF 导出; 同一窗口内**核心 graph view 20 个月零新功能**。⟹ **DB 那半白送, 图那半是自己的活** — 这正是自建控制台的理由。
3. **Bases 只读 frontmatter, 不读正文 inline field** — 大多数人迁不过去是因为满篇 `due:: 2026-06-10`。**本库元数据全在 frontmatter, 所以零迁移直接可用。**
4. **Bases 的天花板是逐行求值** — 没有 `sum`/`count`/`join`/`rollup`, 跨行聚合只能靠 view 层的列汇总。**「把所有指向本页的笔记的 confidence 求均值」做不到** — 这正是 SQL 层存在的理由。
5. ⚠️ **GraphRAG / Graphiti / Cognee 对本库是纯重复劳动** — 它们的价值是**用 LLM 从非结构化文本里抽实体和关系**, 而本库**已经手工做完了**这件事 (stable ID + typed relationship notes + 证据档位字段)。让 LLM 再抽一遍 = 付 API 费换一份比手写更差、更不可控的图。**这是最明确的一条「别做」。**

## 死亡名单 (别碰)

| 工具 | 状态 |
|---|---|
| **Kùzu** | 已归档, Apple 收编 |
| **CozoDB** | 最后 release 2023-12 (32 个月), 4,097★ 是 2022-23 年攒的陷阱 |
| **Dendron** | VS Code 扩展最后更新 **2023-08-12** |
| **Juggl** (Obsidian 图插件) | 最后 release 2023-11 |
| **Graph Analysis** (Obsidian) | 已从官方 store 下架 (release 停在 2022-01)。其 link prediction 无替代品, 只能 BRAT 装 |
| 两个知名 3D Graph fork | 均停在 2023。**活着的是第三个** `apoo711/obsidian-3d-graph` (2026-08-26 刚发版) |
| **Reor** | 已归档 |
| **MkDocs Material** | 🔴 **已公告 EOL: 2026-11-05 (约 10 周后)** — 从其 `SECURITY.md` 原文核实。同时反直觉的好消息: Insiders 付费墙已于 9.7.0 取消, 全部功能并入免费 MIT 版。继任者 Zensical 仍是 v0.0.57 |
| **MkDocs core** | 休眠 (最后 release 2024-08, 一年只有 2 次 commit) 且上游三分裂 (MkDocs 2.0 取消插件系统且未指定 license / ProperDocs 分叉) |
| **Foam** | 工具本身很活 (Marketplace 0.44.5, 2026-08-18, 27 万安装), 但**发布链路已死** — 官方文档推荐的三个站点模板全部停更于 2020-2023 |
| mem0 自托管 MCP | 已归档, 官方推云端 = 最强锁定 |

## 会让 Markdown 不再是真源的 (取消资格)

- **Logseq DB 2.0** (2026-07): **SQLite 成为权威**, markdown 降为导出格式; file-based 那支改名 Logseq OG, **只剩安全维护无新功能**
- **SiYuan**: 存 `.sy` JSON AST, **不能再用 grep/脚本/pandoc 直接改笔记**
- Trilium 系 / Notion 系

**纯 read-layer 因此安全** (Markdown 仍唯一真源, 删掉可重建): DuckDB · Neo4j · LadybugDB · Quartz · Obsidian Publish · Datasette · Marimo · Quarto · Gephi · 全部 MCP server · **Obsidian Bases** (`.base` 本身是纯 YAML, 进 Git)。

## 若要发布成可浏览站点 (二轮深挖修正版)

**三个「零转换 + 六项全中」的选项** (原生 wikilink · 力导图 · backlinks · 全文搜索 · LaTeX · 读 vault 不改结构):

| | 模型 | 成本 | 健康度 |
|---|---|---|---|
| **Quartz v5** | git clone + Node 22 | 免费 | 352 commit/年 · ⚠️ **bus factor = 1** |
| **obsidian-digital-garden** (2,478★) | Obsidian 插件 → GitHub → Vercel | 免费 | v2.84.0 (2026-08-10), d3+PixiJS 图, 与 Quartz 几乎同款架构 |
| **Obsidian Publish** | 托管, 零构建 | **$8-10/站/月** | 官方; **30 分钟上线** |

⚠️ **Quartz v5 的两个实操风险** (二轮核实):
1. **维护者已事实上换人**: 最近 100 次 commit 中 **95 次是 saberzero1**, 原作者 jackyzha0 过去一年只有 7 次 commit。**没有正式交接公告** — 这是事实接管不是书面交接。README 仍署原作者。
2. **d3 与 pixi.js 是运行时从 `cdn.jsdelivr.net` 加载的, 不是打包进去的** — 站点要完全离线或有严格 CSP 时必须改。(对比: 本库自建控制台**完全自包含, 零运行时 CDN**。)

⚠️ **两者都会让笔记公开** — 本库含 confidential 战略材料, **发布前必须先做保密过滤** (`build_console.py` 的 `--public-only` 是同一个问题的解法)。

**其他候选的实测结论**:
- **Astro Starlight**: 核心健康 (0.41.9, 2026-08-25), `starlight-obsidian` 转换插件很好 (作者就是 Starlight 的 Astro 7 PR 提交者)。但**图谱是结构性弱点** — 唯一来源 `starlight-site-graph` npm 停在 0.5.0 (12 个月前), 其 `package.json` 声明 `astro: ^6.0.0` **明确排除 Astro 7**, 而 npm 会**静默**把它装到 Astro 7 上不给任何警告。⚠️ 另注: **Astro 7 (2026-06-22) 把默认 Markdown 引擎换成了 Sätteri (Rust), `remarkPlugins` 已废弃** — 2026-06 之前所有「用 remark 插件加 wikilinks」的教程全部过期。
- **Emanote**: **没有力导向图谱** (全仓库 `forceSimulation` 零命中, 只有层级 uptree); 搜索依赖的 Stork 已于 2023 停更; 且安装需要 Nix。
- **Kiln** (Go 单二进制): 功能清单与需求几乎完美吻合 (含 Canvas 缩放), 但 2025-12 才创建, pre-1.0, **已安静 3.3 个月**, 71★ 单维护者。**可以试, 不要押。**
- **Flowershow**: 免费档**没有全文搜索**且无自定义域名 (搜索在 $50/年 付费墙后)。
- **SilverBullet**: 自托管服务端应用不是静态站生成器; 其静态发布与图谱插件**全部已归档**。工种不对。

## Agent 查询通道 (MCP)

- **Local REST API with MCP** (Obsidian 插件, 2,855★) — v4.0.0 起**自带 MCP server**, 结构上淘汰了第三方 REST 包装型。⚠️ **必须 pin ≥4.1.3** (4.1.3 修了 `%2F` 路径穿越, 可读写删任意主机文件)。需要 Obsidian 开着。
- **mcpvault** (1,637★, MIT) — **直读磁盘不需要 Obsidian 开着**, 有 `--read-only`, AST 感知的 frontmatter 更新, 防路径穿越与 symlink 逃逸, stdio-only 不开网络口。**无插件路径的最优解。**
- ⚠️ **MCP spec 2026-07-28 是破坏性重设计** (session 与 `initialize` 握手移除; Roots/Sampling/Logging 弃用)。选 server 时按新 spec 核一遍。

## 图可视化库 (若自建)

**300–3000 typed node 的首选是 Cytoscape.js** — 不是因为性能 (那个量级都行), 而是因为它有**声明式 selector 样式系统** (按 `data(type)` 给边着色/换线型 = typed relationship 的展示需求) + 内置图算法。1,520 万周下载。
需要 3k 以上 → Sigma.js v3 + graphology (WebGL + WebWorker 布局); ⚠️ **v4 仍是 alpha, 别上生产**。
cosmos.gl 对 320 节点是杀鸡用牛刀。d3-force 停在 2021 **不是死亡** (功能冻结, 2,218 万周下载)。
**这些全部是 npm 包, bundle 后完全离线可跑, 无运行时 CDN 依赖。**

## 什么规模才该升级

| 现在 overkill 的 | 何时成立 |
|---|---|
| Neo4j / Memgraph / Apache AGE | >5,000 节点, 或 >5 种关系类型且真要做路径/中心性分析。**唯一提前成立的理由: 想要 Bloom 那个界面** (仍是最好的免费图 GUI, 且 Neo4j Desktop 内免费 — ⚠️ **Bloom 没有被废弃**, 2026-08-24 刚发 2.36.0; 被废的是 NeoDash) |
| LadybugDB (嵌入式) | >2,000 节点。⚠️ 它 schema-first (关系类型要预先 DDL), 且自我标注为 AI 辅助的 revival 项目, 只有 10 个月大 |
| GraphRAG 系列 | 有 >2,000 篇**未经手工结构化**的文档。**本库不在这个场景** |

<!-- timeline -->

## Timeline

- **2026-08-27** — 建页。触发自 Irene 的工具调研要求; 结论已落地为 4 个 Bases 视图 + `scripts/query.sql`。
