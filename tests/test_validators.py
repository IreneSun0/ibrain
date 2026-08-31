import subprocess
import sys
from pathlib import Path

OPS = Path(__file__).resolve().parent.parent
SCRIPTS = OPS / "scripts"


def run(script, *args, env_vault=None):
    import os
    env = os.environ.copy()
    if env_vault:
        env["VAULT_PATH"] = str(env_vault)
    return subprocess.run([sys.executable, str(SCRIPTS / script), *args],
                          capture_output=True, text=True, env=env)


def make_vault(tmp_path, files: dict):
    (tmp_path / "90_META" / "schemas").mkdir(parents=True)
    import shutil
    real_schema = OPS / "vault" / "90_META" / "schemas" / "frontmatter-schema.json"
    shutil.copy(real_schema, tmp_path / "90_META" / "schemas" / "frontmatter-schema.json")
    for rel, content in files.items():
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(content, encoding="utf-8")
    return tmp_path


GOOD = """---
id: concept:alpha
type: concept
title: Alpha
status: seed
created: 2026-08-26
updated: 2026-08-26
confidence: high
epistemic_status: confirmed
confidentiality: internal
sources: []
---
Links to [[beta]].
"""

BETA = GOOD.replace("concept:alpha", "concept:beta").replace("Alpha", "Beta").replace("[[beta]]", "[[alpha]]")


def test_validate_frontmatter_pass(tmp_path):
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD, "02_CONCEPTS/a/beta.md": BETA})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 0, r.stdout + r.stderr


TYPED_REL = GOOD.replace("sources: []", """sources: []
prerequisites:
  - concept:beta
related:
  - id: "concept:beta"
    rel: contrasts-with
    note: test edge
""")


def test_validate_frontmatter_typed_related_pass(tmp_path):
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": TYPED_REL, "02_CONCEPTS/a/beta.md": BETA})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 0, r.stdout + r.stderr


def test_validate_frontmatter_catches_bad_concept_rel(tmp_path):
    bad = TYPED_REL.replace("rel: contrasts-with", "rel: vibes-with")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad, "02_CONCEPTS/a/beta.md": BETA})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "not in concept relation vocabulary" in r.stdout


def test_validate_frontmatter_catches_unknown_related_and_prereq_ids(tmp_path):
    bad = TYPED_REL.replace("concept:beta", "concept:ghost")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "related references unknown id" in r.stdout
    assert "prerequisites references unknown id" in r.stdout


def test_validate_frontmatter_catches_see_also_without_note(tmp_path):
    bad = TYPED_REL.replace("rel: contrasts-with\n    note: test edge", "rel: see-also")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad, "02_CONCEPTS/a/beta.md": BETA})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "requires a note" in r.stdout


def test_validate_frontmatter_catches_non_concept_prerequisite(tmp_path):
    person = BETA.replace("type: concept", "type: person").replace(
        "confidentiality: internal", "confidentiality: internal\nimportance: tier-2")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": TYPED_REL.replace(
        "related:", "related_off:"), "03_ENTITIES/p/beta.md": person})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "is not a concept page" in r.stdout


def test_validate_frontmatter_catches_verified_without_sources(tmp_path):
    bad = GOOD.replace("status: seed", "status: verified")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "verified but sources is empty" in r.stdout


def test_validate_frontmatter_catches_bad_enum(tmp_path):
    bad = GOOD.replace("confidence: high", "confidence: absolutely")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1


def test_validate_frontmatter_catches_impossible_date_and_scalar_list(tmp_path):
    bad = GOOD.replace("created: 2026-08-26", 'created: "2026-02-30"').replace("sources: []", "sources: source:one")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": bad})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "not a real calendar date" in r.stdout
    assert "field `sources` must be a list" in r.stdout


def test_source_requires_locator(tmp_path):
    source = GOOD.replace("id: concept:alpha", "id: source:alpha").replace("type: concept", "type: source")
    source = source.replace("sources: []", "source_type: official-documentation\nreliability: high\naccessed_at: 2026-08-26\nsources: []")
    v = make_vault(tmp_path, {"07_RESEARCH/sources/alpha.md": source})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "source requires at least one locator" in r.stdout


def test_source_rejects_invalid_url(tmp_path):
    source = GOOD.replace("id: concept:alpha", "id: source:alpha").replace("type: concept", "type: source")
    source = source.replace("sources: []", "source_type: official-documentation\nreliability: high\naccessed_at: 2026-08-26\nurl: http-not-a-url\nsources: []")
    v = make_vault(tmp_path, {"07_RESEARCH/sources/alpha.md": source})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "not an absolute HTTP(S) URL" in r.stdout


def test_relationship_requires_evidence_and_known_entities(tmp_path):
    rel = GOOD.replace("id: concept:alpha", "id: rel:alpha--depends-on--missing")
    rel = rel.replace("type: concept", "type: relationship")
    rel = rel.replace("sources: []", "sources: []\nentity_a: concept:beta\nentity_b: org:missing\nrelationship_type: depends-on\nrelationship_status: active")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/beta.md": BETA, "06_RELATIONSHIPS/rel.md": rel})
    r = run("validate_frontmatter.py", env_vault=v)
    assert r.returncode == 1
    assert "requires field `evidence`" in r.stdout
    assert "entity_b references unknown id `org:missing`" in r.stdout


def test_duplicate_ids_detected(tmp_path):
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD,
                              "02_CONCEPTS/b/alpha2.md": GOOD.replace("title: Alpha", "title: Alpha2")})
    r = run("detect_duplicate_ids.py", env_vault=v)
    assert r.returncode == 1
    assert "concept:alpha" in r.stdout


def test_broken_wikilink_detected(tmp_path):
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD.replace("[[beta]]", "[[missing-note]]")})
    r = run("check_wikilinks.py", env_vault=v)
    assert r.returncode == 1
    assert "missing-note" in r.stdout


def test_wikilink_alias_resolution(tmp_path):
    beta_alias = BETA.replace("sources: []", "sources: []\naliases:\n  - B-Side")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD.replace("[[beta]]", "[[B-Side]]"),
                              "02_CONCEPTS/a/beta.md": beta_alias})
    r = run("check_wikilinks.py", env_vault=v)
    assert r.returncode == 0, r.stdout


def test_frontmatter_id_is_not_native_wikilink_target(tmp_path):
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD.replace("[[beta]]", "[[concept:beta]]"),
                              "02_CONCEPTS/a/beta.md": BETA})
    r = run("check_wikilinks.py", env_vault=v)
    assert r.returncode == 1
    assert "concept:beta" in r.stdout


def test_wikilink_chinese_filename_and_alias(tmp_path):
    beta = BETA.replace("[[alpha]]", "[[甲方]]").replace("sources: []", "sources: []\naliases:\n  - 乙方")
    alpha = GOOD.replace("[[beta]]", "[[乙方]]")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/甲方.md": alpha, "02_CONCEPTS/a/乙.md": beta})
    r = run("check_wikilinks.py", env_vault=v)
    assert r.returncode == 0, r.stdout


def test_ambiguous_alias_is_rejected(tmp_path):
    beta1 = BETA.replace("sources: []", "sources: []\naliases:\n  - Shared")
    beta2 = beta1.replace("concept:beta", "concept:gamma").replace("title: Beta", "title: Gamma")
    v = make_vault(tmp_path, {"02_CONCEPTS/a/alpha.md": GOOD.replace("[[beta]]", "[[Shared]]"),
                              "02_CONCEPTS/a/beta.md": beta1,
                              "02_CONCEPTS/a/gamma.md": beta2})
    r = run("check_wikilinks.py", env_vault=v)
    assert r.returncode == 1
    assert "ambiguous" in r.stdout


def test_renamed_company_alias_collision_is_reported(tmp_path):
    org1 = GOOD.replace("id: concept:alpha", "id: org:newco").replace("type: concept", "type: organization")
    org1 = org1.replace("sources: []", "sources: []\nimportance: tier-2\naliases:\n  - OldCo")
    org2 = org1.replace("id: org:newco", "id: org:otherco").replace("title: Alpha", "title: OtherCo")
    v = make_vault(tmp_path, {"03_ENTITIES/organizations/newco.md": org1,
                              "03_ENTITIES/organizations/otherco.md": org2})
    r = run("detect_duplicate_entities.py", env_vault=v)
    assert r.returncode == 1
    assert "oldco" in r.stdout


def test_secret_scan_clean_on_real_repos():
    r = run("secret_scan.py")
    assert r.returncode == 0, r.stdout
