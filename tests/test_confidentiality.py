import os
import subprocess
import sys
from pathlib import Path

from test_validators import GOOD, make_vault

OPS = Path(__file__).resolve().parent.parent


def test_confidentiality_downgrade_is_rejected(tmp_path):
    source = GOOD.replace("id: concept:alpha", "id: source:secret")
    source = source.replace("type: concept", "type: source").replace("confidentiality: internal", "confidentiality: confidential")
    source = source.replace("sources: []", "source_type: user-direct\nreliability: high\naccessed_at: 2026-08-26\ncontent_hash: abc\nsources: []")
    consumer = GOOD.replace("[[beta]]", "").replace("sources: []", "sources:\n  - source:secret")
    vault = make_vault(tmp_path, {"07_RESEARCH/sources/secret.md": source,
                                  "02_CONCEPTS/a/consumer.md": consumer})
    env = os.environ.copy()
    env["VAULT_PATH"] = str(vault)
    result = subprocess.run([sys.executable, str(OPS / "scripts" / "check_confidentiality.py")],
                            capture_output=True, text=True, env=env)
    assert result.returncode == 1
    assert "lower than source" in result.stdout
