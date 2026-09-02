"""The README states counts and quotes the atlas. A knowledge base whose pitch is
that CI enforces its discipline cannot advertise figures or content that drift, so
both are asserted here."""
import json
import re
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from brainlib import iter_notes  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault"
README = ROOT / "README.md"
ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset"}


def test_readme_counts_match_the_vault():
    by: dict[str, int] = {}
    for n in iter_notes(VAULT):
        by[n.ntype] = by.get(n.ntype, 0) + 1
    stated = {int(m.replace(",", "")) for m in re.findall(r"\b\d[\d,]*\b", README.read_text("utf-8"))}
    for label, want in (("concepts", by.get("concept", 0)),
                        ("entities", sum(v for k, v in by.items() if k in ENTITY_TYPES))):
        assert want in stated, f"README states no {label} count of {want}"


def test_readme_quotes_the_chapters_verbatim(tmp_path):
    """The reading path is the README's main content. If a chapter is renamed or
    rewritten, the README must be rewritten with it — not left describing a version
    of the atlas that no longer ships."""
    out = subprocess.run([sys.executable, str(ROOT / "scripts" / "build_learning_view.py"),
                          "--out", str(tmp_path / "index.html")], capture_output=True, text=True)
    assert out.returncode == 0, out.stderr
    import yaml  # noqa: E402

    mainline = yaml.safe_load(
        (VAULT / "10_LEARNING" / "plan" / "mainline.yaml").read_text("utf-8"))
    text = README.read_text("utf-8")
    # the README uses full-width punctuation; the source questions are half-width
    norm = lambda s: s.replace("? ", "？").replace("?", "？").replace(", ", "，").replace(",", "，")
    for ch in mainline["chapters"]:
        assert norm(str(ch["question"])) in text, \
            f"chapter {ch['n']} question is not in the README: {ch['question']}"
        assert str(ch["question_en"]) in text, \
            f"chapter {ch['n']} English question is not in the README"
        assert str(ch["title_en"]).replace("Ch.", "").strip() in text, \
            f"chapter {ch['n']} English title is not in the README"


def test_readme_named_concepts_exist():
    """Every term the README promises the reader will meet is a real note."""
    sys.path.insert(0, str(ROOT / "scripts"))
    import export_graph as eg  # noqa: E402
    nodes = eg.build()["nodes"]
    names = {n.get("titleZh") or "" for n in nodes} | {n.get("title") or "" for n in nodes}
    names.discard("")
    rows = re.findall(r"^\|\s*\*\*[^|]+\*\*\s*\|[^|]+\|([^|]+)\|\s*$",
                      README.read_text("utf-8"), re.M)
    promised = [t.strip() for row in rows for t in row.split("·")]
    assert len(promised) >= 60, f"the reading-path tables name too few concepts: {promised}"
    # a README may shorten a note's name, but only by truncating it — never by
    # inventing a name the reader will not find on the site
    missing = [t for t in promised
               if not any(n.lower().startswith(t.lower().rstrip("s")) for n in names)]
    assert not missing, f"README names concepts the vault does not have: {missing}"
