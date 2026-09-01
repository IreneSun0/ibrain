<h1 align="center">CryptoAtlas</h1>

<p align="center">
  <b>一张开放、有来源的加密市场结构地图 ——<br>
  每条断言都带着证据等级，达不到的会被 CI 直接打回。</b>
</p>

<p align="center">
  <a href="https://ailinsun.github.io/cryptoatlas"><b>🗺 打开图谱</b></a> ·
  <a href="CONTRIBUTING.md">➕ 补充或纠错</a> ·
  <a href="README.md">🇬🇧 English</a>
</p>

---

大多数加密"知识库"要么是链接堆，要么是自信的 AI 废话：读起来顺，一个来源都没有，然后在第一稿到第十稿之间的某个地方，一个猜测悄悄变成了事实。

这个库反过来做：**认知纪律由 CI 强制执行，不靠自觉。** 标了 `verified` 却没有来源笔记 —— build 失败。断言一条关系却没有证据 —— build 失败。纠错只能追加进时间线，不能覆盖历史。**没有任何东西被呈现得比它实际更确定。**

首页是整个库的活地图：**谁创立、谁投资、结算在哪条链、受谁监管、谁给谁做市** —— 从 297 篇互链笔记里长出来。

## 里面有什么

|  | 数量 |
|---|---:|
| 概念 —— 订单簿、清算、衍生品、托管、预言机、裁决、机构风险 | **143** |
| 实体 —— 场馆、做市商、基金、协议、监管、法域、人物 | **76** |
| 它们之间的 typed 关系 | **75** |
| 实证案例（真实争议，带金额与结局） | 3 |
| 来源笔记 | 21 |
| **总笔记 / 总链接** | **297 / 2,848** |

每个概念都写到完整深度 —— 精确定义、为什么重要、机制拆解、带数字的具体例子、常见误解、实战检查清单、自测题。实质正文中位数约 2,000 字符。

事件与预测市场是挖得最深的一条线（结算问题在那里最难），但它是这张更大的地图里的一个纵向，不是全部。

## 欢迎贡献 —— 这正是重点

**加密行业变化的速度超过任何一个人能跟踪的范围。** 一家场馆改了费率、一个监管转了态度、一家做市商进场或退场 —— 笔记就过时了。如果你在这个行业里，你一定知道一些这张地图还不知道的事。

在这里贡献**特别容易做对**，因为校验器会明确告诉你缺什么：

```bash
git clone https://github.com/ailinsun/cryptoatlas && cd cryptoatlas
make bootstrap          # 建 venv + 装依赖
# 在 vault/ 下编辑或新增笔记
make validate           # 精确告诉你这条断言还缺什么
```

它会拒绝：没有来源却标 `verified`、坏链、重复 id、没有证据的关系。**你不需要猜这个库的规矩 —— build 会强制它。**

三种参与方式，从最轻的开始：

| | 做什么 | 从哪开始 |
|---|---|---|
| **纠错** | 过时的事实、错的日期、变了的费率 | [提一个纠错 issue](https://github.com/ailinsun/cryptoatlas/issues/new?template=correction.md) |
| **补实体** | 缺失的场馆、基金、协议或监管机构 | [CONTRIBUTING.md](CONTRIBUTING.md#adding-an-entity) |
| **补概念** | 这张地图还没解释的机制 | [CONTRIBUTING.md](CONTRIBUTING.md#adding-a-concept) |

某个实体与市场某一部分没有已证实的关联时，笔记会写 `UNKNOWN` 并说明这个空白本身说明了什么。**指出某一条写错了，和新增一条一样有价值。**

## 引擎 —— 拿去做你自己领域的知识库

22 个 Python 脚本、57 个测试、一个写入时校验 hook、6 个 Claude Code subagent、11 个 skill。指向你自己的 vault，同一套纪律就作用在你的领域上。

新克隆默认解析到自带的 `vault/`，**所有命令零配置即可跑通**；要指向别处：`VAULT_PATH=/path/to/vault make validate`。

六条规矩，每一条背后都有一个能让 build 失败的脚本：

| 规矩 | 由谁强制 |
|---|---|
| **每条断言归入五档之一** —— confirmed / inference / hypothesis / unverified / unknown —— 并**可见地**标出来 | `validate_frontmatter.py` |
| **标 `verified` 就必须有来源笔记**，带 content hash 与访问日期 | `validate_frontmatter.py`、`check_source_freshness.py` |
| **编译区与 append-only 证据时间线分离**：纠错靠追加，永不覆盖历史 | vault 政策 §3 |
| **确定性工作永不交给 LLM** —— id、hash、slug、索引、链接解析一律是代码 | `brainlib.py` 与全部生成器 |
| **保密是带类型的天花板**，一篇笔记的保护级别不得低于它自己的来源 | `check_confidentiality.py` |
| **没有任何东西会意外发布** —— 公开树由私库经可审计的脚本**派生**而来 | `build_public_vault.py` |

最后一条是绝大多数项目做错的地方。`scripts/build_public_vault.py` 物化出可发布子集，所有排除规则都声明在那一个文件的顶部：私有目录、个人工作状态、保密等级高于 `public-source` 的内容，以及一条**级联**规则 —— 对手方被撤下的关系笔记一并撤下，保证公开图在自己的引用下闭合。它会写出 `PUBLICATION.md` 清单，记录撤下了什么、为什么。

## 目录结构

```
vault/       知识库 —— 297 篇笔记（由私有源库派生生成）
scripts/     22 个确定性工具：校验器、导入器、生成器、导出器
tests/       57 个测试，含保密天花板的回归防线
.claude/     6 个 subagent + 11 个 skill + 写入时校验 hook
docs/        构建出的站点（生成物，部署到 GitHub Pages）
```

复用引擎：保留 `scripts/`、`tests/`、`.claude/` 和 `vault/90_META/`（schema、政策宪法、关系类型词表、18 个笔记模板），删掉 `vault/` 其余部分，按模板写你自己的笔记 —— `make validate` 会立刻、具体地告诉你在哪里偷懒了。

## 状态

每一页的 frontmatter 和图谱导出里都能看到笔记成熟度：216 reviewed、46 verified、32 seed、3 stale。动态事实带 `last_verified` 日期，靠复核维护而不是靠重写。**没有任何内容被呈现得比它实际更确定** —— 这正是分档存在的意义。

## 许可

- **代码**（`scripts/`、`tests/`、`hooks/`、`.claude/`、`Makefile`）—— [Apache-2.0](LICENSE)
- **内容**（`vault/`、`docs/`）—— [CC BY 4.0](LICENSE-CONTENT)

署名：*CryptoAtlas*, https://github.com/ailinsun/cryptoatlas。来源笔记只记录元数据与摘要并注明出处，不复制原文；原作权利归各自出版方。
