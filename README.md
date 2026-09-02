<h1 align="center">CryptoAtlas</h1>

<p align="center">
  <b>一张开放、有来源的加密市场结构地图 ——<br>
  每条断言都带着证据等级，达不到的会被 CI 直接打回。</b>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas"><b>🗺 打开图谱</b></a> ·
  <a href="CONTRIBUTING.md">➕ 补充或纠错</a> ·
  <a href="README.en.md">🇬🇧 English</a>
</p>

<p align="center">
  <img alt="CI" src="https://github.com/ailinsun/cryptoatlas/actions/workflows/ci.yml/badge.svg">
  <img alt="notes" src="https://img.shields.io/badge/notes-292-4c8fd6">
  <img alt="links" src="https://img.shields.io/badge/links-2%2C813-4c8fd6">
  <img alt="code" src="https://img.shields.io/badge/code-Apache--2.0-3faa8e">
  <img alt="content" src="https://img.shields.io/badge/content-CC%20BY%204.0-3faa8e">
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas">
    <img src=".github/assets/graph.webp" alt="CryptoAtlas 知识图谱" width="100%">
  </a>
</p>

---

概念、场馆、做市商、监管、人 —— 以及**谁创立、谁投资、结算在哪条链、受谁监管、谁给谁做市**。全部互链，全部标注证据等级。

不同之处只有一条：**纪律由 CI 强制，不靠自觉。** 标 `verified` 却没有来源笔记，build 失败；断言一条关系却没有证据，build 失败；纠错只能追加进时间线，不能覆盖历史。

## 里面有什么

|  | 数量 |
|---|---:|
| 概念 —— 订单簿、清算、衍生品、托管、预言机、裁决、机构风险 | **143** |
| 实体 —— 场馆、做市商、基金、协议、监管、法域、人物 | **76** |
| 它们之间的 typed 关系 | **75** |
| 实证案例（真实争议，带金额与结局） | 3 |
| 来源笔记 | 21 |
| **总笔记 / 总链接** | **292 / 2,813** |

每个概念写到完整深度：定义、为什么重要、机制、带数字的例子、常见误解、实战清单、自测题。成熟度公开可见 —— 216 reviewed · 46 verified · 23 seed · 3 stale。

## 参与贡献

**一家场馆改了费率、一个监管转了态度、一家做市商进场或退场，笔记就过时了。** 如果你在这行，你一定知道一些这张地图还不知道的事。

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap     # 建 venv + 装依赖
make validate      # 精确告诉你这条断言还缺什么
```

不用猜规矩，校验器会指出来：没来源却标 `verified`、坏链、重复 id、没有证据的关系，一律拒绝。

| | 做什么 | 从哪开始 |
|---|---|---|
| **纠错** | 过时的事实、错的日期、变了的费率 | [提一个纠错 issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) |
| **补实体** | 缺失的场馆、基金、协议或监管机构 | [CONTRIBUTING.md](CONTRIBUTING.md#adding-an-entity) |
| **补概念** | 这张地图还没解释的机制 | [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-concept) |

指出某一条写错了，和新增一条一样有价值。

## 引擎

15 个 Python 脚本 · 42 个测试 · 一个写入时校验 hook · 6 个 subagent · 7 个 skill。指向你自己的 vault（`VAULT_PATH=/path/to/vault`），同一套纪律就作用在你的领域上。

| 规矩 | 由谁强制 |
|---|---|
| 每条断言归入五档之一（confirmed / inference / hypothesis / unverified / unknown）并可见地标出 | `validate_frontmatter.py` |
| 标 `verified` 必须有来源笔记，带 content hash 与访问日期 | `check_source_freshness.py` |
| 保密是带类型的天花板：一篇笔记不得低于它自己的来源 | `check_confidentiality.py` |
| 公开树由私库经可审计的脚本**派生**，没有东西会意外发布 | `build_public_vault.py` |

最后一条是多数项目做错的地方。`build_public_vault.py` 的排除规则全部声明在文件顶部，并带一条**级联**规则 —— 对手方被撤下的关系笔记一并撤下，保证公开图在自己的引用下闭合。

## 结构

```
vault/       知识库 —— 292 篇笔记（由私有源库派生生成）
scripts/     15 个确定性工具：校验器、生成器、导出器
tests/       42 个测试，含保密天花板的回归防线
.claude/     6 个 subagent + 7 个 skill + 写入时校验 hook
```

复用引擎：留下 `scripts/`、`tests/`、`.claude/` 和 `vault/90_META/`（schema、政策、关系词表、18 个模板），删掉 `vault/` 其余部分，写你自己的笔记。

## 许可

**代码**（`scripts/`、`tests/`、`hooks/`、`.claude/`、`Makefile`）[Apache-2.0](LICENSE) · **内容**（`vault/`、`docs/`）[CC BY 4.0](LICENSE-CONTENT)

署名：*CryptoAtlas*, https://github.com/ailinsun/cryptoatlas。来源笔记只记录元数据与摘要并注明出处，不复制原文。
