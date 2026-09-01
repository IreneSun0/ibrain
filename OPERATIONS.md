# OPERATIONS — maintenance manual

## Command surface

| command | what it does |
|---|---|
| `make bootstrap` | create the venv and install dependencies |
| `make validate` | the hard gates: frontmatter · duplicate ids · broken links · confidentiality |
| `make health` | full audit, writes `VAULT-HEALTH-REPORT.md` |
| `make indexes` | regenerate indexes, MOC auto-blocks, query eval |
| `make study` | regenerate the study queue and next-session sheet |
| `make refresh` | weekly bundle: indexes + study + freshness + orphans + duplicate entities |
| `make ingest` | run the importers (idempotent) |
| `make secretscan` | scan for credential-shaped content |
| `make learning-view` | rebuild the site into `dist/` (see `make site` for `docs/`) |
| `make publish SOURCE=...` | rebuild `vault/` from a private source vault |
| `make site` | build `docs/` for GitHub Pages |
| `make test` | run the pytest suite |

## The write-time hook

`.claude/settings.json` registers a PostToolUse hook that runs after every markdown
write inside the resolved vault: frontmatter validation for that file, plus a
repo-wide duplicate-id and broken-link check.

**It reports; it never rewrites** — and it never touches `09_ORIGINALS/`. Failures are
handed back to the model so it fixes them in the same turn.

## Weekly maintenance loop

1. Process the inbox (`01_INBOX/*` → filed by `librarian`).
2. `detect_duplicate_entities.py --report` → resolve name collisions.
3. Update the compiled section of any page with new evidence.
4. Append to timelines (never edit existing entries).
5. `fact-checker` spot-audits claims that carry no source.
6. `check_source_freshness.py` → handle stale sources (overdue review, aging
   `verified`, un-fetched URLs).
7. `check_wikilinks.py` → fix broken links.
8. `find_orphan_notes.py` → connect orphans.
9. `relationship-mapper` fills in weak relationships.
10. Update the coverage matrix and generate the gap report.
11. `make study` refreshes the queue.
12. Weekly synthesis → `11_OUTPUTS/weekly-synthesis/`.

## Publishing

`vault/` is a build output. The private vault is the source of truth.

```bash
make publish SOURCE=/path/to/private-vault   # rebuild vault/ + indexes + validate
make site                                    # rebuild docs/
```

Every exclusion rule lives at the top of `scripts/build_public_vault.py`. The script
writes a `PUBLICATION.md` manifest recording how many notes were withheld and why, and
it refuses to write onto its own source.

**Before any publish**: `make validate && make secretscan && make test` must all be green.

## Troubleshooting

- **Validators all red for no obvious reason** — check you are in the repo root and the
  venv exists (`make bootstrap`).
- **An importer overwrote hand-written content** — check whether that page's
  `import_origin` was left without the `+manual` marker. Restore with git, fix the
  marker, re-import.
- **The hook blocked a legitimate write** — read the specific violation it printed and
  fix it. If the rule itself is wrong, fix `hooks/validate_md_write.sh` and record the
  change here.
