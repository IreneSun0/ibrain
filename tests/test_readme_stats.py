"""The README states counts. A knowledge base whose pitch is that CI enforces its
discipline cannot advertise numbers that drift — so the numbers are asserted here."""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from brainlib import iter_notes  # noqa: E402

ROOT = Path(__file__).resolve().parents[1]
VAULT = ROOT / "vault"
ENTITY_TYPES = {"person", "organization", "exchange-venue", "protocol-network",
                "market-maker-fund", "regulator", "jurisdiction", "product", "token-asset"}


def _counts() -> dict[str, int]:
    notes = list(iter_notes(VAULT))
    by = {}
    for n in notes:
        by[n.ntype] = by.get(n.ntype, 0) + 1
    return {
        "notes": len(notes),
        "concepts": by.get("concept", 0),
        "entities": sum(v for k, v in by.items() if k in ENTITY_TYPES),
        "sources": by.get("source", 0),
        "cases": by.get("case-study", 0),
    }


def test_readme_counts_match_the_vault():
    c = _counts()
    for readme in (ROOT / "README.md", ROOT / "README.zh-CN.md"):
        text = readme.read_text(encoding="utf-8")
        nums = {int(m.replace(",", "")) for m in re.findall(r"\*\*([\d,]+)(?:\s*/|\*\*)", text)}
        for label, want in (("concepts", c["concepts"]), ("entities", c["entities"]),
                            ("notes", c["notes"])):
            assert want in nums, (
                f"{readme.name} does not state the real {label} count ({want}); "
                f"numbers it does state: {sorted(nums)} — run the counts and update it")
