-- query.sql — SQL over the iBrain vault.
--
-- Design note: DuckDB has a community `markdown` extension, but it is a
-- 28-star single-maintainer project (≈1k weekly downloads) whose wikilink
-- extraction is line-based and does not skip code fences. We already own a
-- deterministic extractor (export_graph.py) and DuckDB reads JSON natively
-- with zero extensions — so we go through the export instead. Fewer moving
-- parts, and every parsing rule stays in one tested place.
--
-- Usage:
--   python3 scripts/export_graph.py --out dist/graph.json
--   duckdb -ui -init scripts/query.sql        # local web UI
--   duckdb -init scripts/query.sql            # plain REPL
-- (install once: brew install duckdb)

CREATE OR REPLACE VIEW g AS
  SELECT * FROM read_json_auto('dist/graph.json');

CREATE OR REPLACE VIEW notes AS
  SELECT n.* FROM g, UNNEST(g.nodes) AS t(n);

CREATE OR REPLACE VIEW edges AS
  SELECT e.* FROM g, UNNEST(g.edges) AS t(e);

-- one row per (note, domain) so GROUP BY domain counts multi-domain notes honestly
CREATE OR REPLACE VIEW note_domains AS
  SELECT n.id, n.title, n.titleZh, n.type, n.status, n.confidence, n.importance,
         n.epistemic, n.confidentiality, n.sourceCount, d AS domain
  FROM notes n, UNNEST(CASE WHEN len(n.domains) = 0 THEN ['(none)'] ELSE n.domains END) AS t(d);

-- what the graph actually leans on
CREATE OR REPLACE VIEW degree AS
  SELECT n.id, n.title, n.titleZh, n.type, n.status, n.importance,
         (SELECT count(*) FROM edges e WHERE e.source = n.id OR e.target = n.id) AS deg
  FROM notes n;

-- typed relationship edges resolved to readable endpoints
CREATE OR REPLACE VIEW typed_edges AS
  SELECT e.relType AS rel, e.relStatus AS status,
         a.titleZh AS from_zh, a.title AS from_en,
         b.titleZh AS to_zh,   b.title AS to_en,
         e.note AS evidence_note
  FROM edges e
  JOIN notes a ON a.id = e.source
  JOIN notes b ON b.id = e.target
  WHERE e.kind = 'typed';

.print ''
.print '  iBrain SQL — 视图: notes / edges / note_domains / degree / typed_edges'
.print ''
.print '  -- 领域 × 成熟度 (Bases 做不到的跨行聚合)'
.print '  SELECT domain, count(*) AS n,'
.print '         count(*) FILTER (status=''verified'') AS verified,'
.print '         round(100.0*count(*) FILTER (status=''verified'')/count(*)) AS pct'
.print '  FROM note_domains GROUP BY domain ORDER BY n DESC;'
.print ''
.print '  -- 声称 verified 却一个来源都没引 (应为 0)'
.print '  SELECT id, title FROM notes'
.print '  WHERE status=''verified'' AND sourceCount=0 AND type<>''source'';'
.print ''
.print '  -- 有 URL 但无内容快照的来源 (审计的核心问题)'
.print '  SELECT id, url FROM notes WHERE type=''source'' AND url<>'''' AND NOT hasHash;'
.print ''
.print '  -- 图里最承重的 20 个节点'
.print '  SELECT titleZh, title, type, deg FROM degree ORDER BY deg DESC LIMIT 20;'
.print ''
.print '  -- 孤儿: 零连接的笔记'
.print '  SELECT id, title FROM degree WHERE deg=0;'
.print ''
.print '  -- 全部 typed 关系, 人可读'
.print '  SELECT rel, from_zh, to_zh, status FROM typed_edges ORDER BY rel;'
.print ''
.print '  -- 机密内容分布 (分享任何导出前先跑这个)'
.print '  SELECT confidentiality, count(*) FROM notes GROUP BY 1 ORDER BY 2 DESC;'
.print ''
