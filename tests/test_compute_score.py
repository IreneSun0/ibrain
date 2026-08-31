import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))
import compute_score as cs


def test_quiz_score_last5_and_scope():
    recs = [{"kind": "quiz", "date": f"2026-09-0{i}", "scope": "industry", "score": i * 10}
            for i in range(1, 8)]  # 10..70
    assert cs.quiz_score(recs) == (30 + 40 + 50 + 60 + 70) / 5
    assert cs.quiz_score(recs, "pm") is None
    recs.append({"kind": "quiz", "date": "2026-09-09", "scope": "pm", "score": 80})
    assert cs.quiz_score(recs, "pm") == 80


def test_mock_score_weighted_newest_first():
    recs = [
        {"kind": "mock", "date": "2026-09-06", "scope": "pm", "score": 40},
        {"kind": "mock", "date": "2026-09-13", "scope": "pm", "score": 60},
        {"kind": "mock", "date": "2026-09-20", "scope": "pm", "score": 80},
    ]
    # newest 80*0.5 + 60*0.3 + 40*0.2 = 66
    assert abs(cs.mock_score(recs) - 66.0) < 1e-9
    assert cs.mock_score(recs[:1]) == 40  # single record → its own score


def test_build_on_real_vault():
    if not (cs.vault_root() / "10_LEARNING" / "plan" / "assessments.yaml").exists():
        import pytest
        pytest.skip("bootcamp scoring needs the private plan data (assessments/schedule)")
    s = cs.build()
    assert 0 <= s["industry"] <= 100 and 0 <= s["pm"] <= 100
    assert s["concepts"]["all"][1] == 81  # mainline quests, not the full library
    assert s["concepts"]["pm"][1] > 40  # stage-7 domain ∩ mainline + cross-stage pool
    assert s["deadline"] == "2026-09-30"


def test_scoreboard_renders(tmp_path):
    out = tmp_path / "scoreboard.md"
    assert cs.main(["--out", str(out)]) == 0
    text = out.read_text(encoding="utf-8")
    assert "行业总分" in text and "PM 专项" in text and "make score" in text
