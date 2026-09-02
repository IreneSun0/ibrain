# OPERATIONS — maintenance manual

## Command surface

| command | what it does |
|---|---|
| `make bootstrap` | create the venv and install dependencies |
| `make validate` | the hard gates: frontmatter · duplicate ids · broken links · confidentiality |
| `make health` | full audit, writes `VAULT-HEALTH-REPORT.md` |
| `make indexes` | regenerate indexes and MOC auto-blocks |
| `make refresh` | weekly bundle: indexes + freshness + orphans + duplicate entities |
| `make secretscan` | scan for credential-shaped content |
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

1. `detect_duplicate_entities.py --report` → resolve name collisions.
2. Update the compiled section of any page with new evidence.
3. Append to timelines (never edit existing entries).
4. `fact-checker` spot-audits claims that carry no source.
5. `check_source_freshness.py` → handle stale sources (overdue review, aging
   `verified`, un-fetched URLs).
6. `check_wikilinks.py` → fix broken links.
7. `find_orphan_notes.py` → connect orphans.
8. `relationship-mapper` fills in weak relationships.

## Publishing

`vault/` is a build output. The private vault is the source of truth.

```bash
make publish SOURCE=/path/to/private-vault   # rebuild vault/ + indexes + validate
make site                                    # rebuild docs/
```

Every exclusion rule lives at the top of `scripts/build_public_vault.py`. The run
reports how many notes were withheld and why, and refuses to write onto its own source.

**Before any publish**: `make validate && make secretscan && make test` must all be green.

## Troubleshooting

- **Validators all red for no obvious reason** — check you are in the repo root and the
  venv exists (`make bootstrap`).
- **The hook blocked a legitimate write** — read the specific violation it printed and
  fix it. If the rule itself is wrong, fix `hooks/validate_md_write.sh` and record the
  change here.
