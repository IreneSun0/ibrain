<h1 align="center">iBrain</h1>

<p align="center">
  <b>一个每条断言都带着证据等级的加密市场结构知识库 ——<br>以及那套不允许它含糊过去的引擎。</b>
</p>

<p align="center">
  <a href="https://irenesun0.github.io/ibrain"><b>📖 阅读知识库</b></a> ·
  <a href="README.md">🇬🇧 English</a>
</p>

---

大多数 AI 生成的知识库都是自信的废话：读起来顺，一个来源都没有，然后在第一稿到第十稿之间的某个地方，悄悄把一个猜测升级成了事实。

这个 repo 想做相反的事：一个真实主题上的真实知识库，**而它的认知纪律由 CI 强制执行，不靠自觉。**

## 一、知识库 — 308 篇预测市场基础设施笔记

覆盖加密市场究竟是怎么搭起来的：订单簿与做市、清算与结算、链层、衍生品与保证金、托管与稳定币、机构风险词汇、按辖区看的监管 —— 以及支撑这一切运转的场馆、基金、协议和人。

事件与预测市场是其中挖得最深的一条线（24 个概念 + 3 个裁决/预言机/争议的实证案例），因为结算问题在那里最难 —— 但它是这张更大的地图里的一个纵向，不是全部。

|  | 数量 |
|---|---:|
| 概念 | 143 |
| 实体（场所 / 机构 / 协议 / 监管 / 辖区 / 人物） | 76 |
| typed 关系 | 11 |
| 来源笔记 | 21 |
| 前置 + 语义关联边 | 285 |
| **总笔记 / 总链接** | **308 / 2,848** |

**143 个概念全部写到完整深度** —— 精确定义、为什么重要、机制拆解、带数字的具体例子、常见误解、实战检查清单、自测题。实质正文中位数约 2,000 字符（初次导入时是 600）。

[站点](https://irenesun0.github.io/ibrain)打开是**生态图谱** —— 谁创立、谁投资、结算于哪条链、受谁监管、谁给谁做市 —— 另一个视图把材料按 9 章阅读路径铺开，核心与延伸是筛选器而不是等级。

## 二、引擎 — 你可以直接拿走复用的部分

22 个 Python 脚本、57 个测试、一个写入时校验 hook、6 个 Claude Code subagent 和 11 个 skill。指向你自己的 vault，同一套纪律就作用在你的领域上。

```bash
git clone https://github.com/IreneSun0/ibrain && cd ibrain
make bootstrap     # 建 venv + 装依赖
make validate      # frontmatter · 重复 id · 坏链 · 保密等级
make site          # → docs/index.html
```

新克隆默认解析到自带的 `vault/`，**所有命令零配置即可跑通**。要指向自己的库：`VAULT_PATH=/path/to/vault make validate`。

## 它凭什么不一样

六条规矩，每一条背后都有一个能让 build 失败的脚本：

| 规矩 | 由谁强制 |
|---|---|
| **每条断言必须归入五档之一** —— confirmed / inference / hypothesis / unverified / unknown —— 并且**可见地**标出来 | `validate_frontmatter.py` |
| **标 `verified` 就必须有来源笔记**，且带 content hash 与访问日期 | `validate_frontmatter.py`、`check_source_freshness.py` |
| **编译区与 append-only 证据时间线分离**：纠错靠追加，永不覆盖历史 | vault 政策 §3，`vault-auditor` 审计 |
| **确定性工作永不交给 LLM** —— id、hash、slug、索引、链接解析一律是代码 | `brainlib.py` 与全部生成器 |
| **保密是带类型的天花板**，一篇笔记的保护级别不得低于它自己的来源 | `check_confidentiality.py` |
| **没有任何东西会意外发布** —— 公开树由私库经可审计的脚本**派生**而来 | `build_public_vault.py` |

最后一条是绝大多数项目做错的地方，值得展开讲。

### 发布是一个 build 步骤，不是一句承诺

私库是唯一真相源。`scripts/build_public_vault.py` 物化出可发布子集，**所有排除规则都声明在那一个文件的顶部**：

- 整棵私有目录、个人工作状态、vault 运维产物 —— 丢弃
- 保密等级高于 `public-source` 的 —— 丢弃
- **级联**：对手方被撤下的关系笔记也一并撤下，保证公开图在自己的引用下是闭合的
- 项目专属批注段 —— 剥离
- 确定性重写规则一次性清掉所有私有标识符，**重新发布不依赖任何人记得去手改哪个文件**

它会写出 `PUBLICATION.md` 清单，说明撤下了多少篇、各是什么原因。脚本幂等，CI 会对产物再跑一遍 `make validate`。

## 目录结构

```
vault/            已发布的知识库（生成物 —— 要改请改私库）
scripts/          24 个确定性工具：校验器、导入器、生成器、导出器
tests/            57 个测试，含保密天花板的回归防线
.claude/          6 个 subagent + 11 个 skill + 写入时校验 hook
docs/             构建出的站点（GitHub Pages）
```

| 脚本组 | 作用 |
|---|---|
| `validate_frontmatter` · `detect_duplicate_ids` · `check_wikilinks` · `check_confidentiality` | 硬闸门 —— `make validate` |
| `check_evidence_coverage` · `check_source_freshness` · `find_orphan_notes` · `detect_duplicate_entities` | 软审计 —— `make health` |
| `ingest_xlsx` · `ingest_chat_export` · `normalize_wikilinks` | 幂等导入器 |
| `generate_indexes` · `generate_mocs` · `generate_study_queue` | 派生页面 |
| `export_graph` · `build_learning_view` | 图谱与站点 |
| `build_public_vault` · `secret_scan` | 发布闸门 |

## 拿去做你自己领域的知识库

上面没有一条是预测市场专属的。复用方法：

1. 保留 `scripts/`、`tests/`、`.claude/` 和 `vault/90_META/` —— schema、政策宪法、关系类型词表、18 个笔记模板。
2. 删掉 `vault/` 其余部分，按模板写你自己的笔记。
3. `make validate` 会立刻、具体地告诉你在哪里偷懒了。

如果你用 Claude Code，`.claude/` 是最值得看的部分：subagent 有硬性职责边界（researcher 不得给重要性分级，strategist 不得建 decision 页），PostToolUse hook 在每次 markdown 写入后重跑校验，并把违规直接甩回给模型当场修。

## 状态

每一页的 frontmatter 和图谱导出里都能看到笔记成熟度：172 reviewed、85 verified、37 seed、3 stale。

**143 个概念已全部写完。** 剩下标 `seed` 的主要是实体与来源层 —— 那些页面看重的是时效而非篇幅，靠 `last_verified` 日期维护而不是靠扩写。**没有任何内容被呈现得比它实际更确定** —— 这正是分档存在的意义。

## 许可

- **代码**（`scripts/`、`tests/`、`hooks/`、`.claude/`、`Makefile`）—— [Apache-2.0](LICENSE)
- **内容**（`vault/`、`docs/`）—— [CC BY 4.0](LICENSE-CONTENT)

内容署名：*iBrain, Irene Sun*。来源笔记只记录元数据与摘要并注明出处，不复制原文；原作权利归各自出版方。
