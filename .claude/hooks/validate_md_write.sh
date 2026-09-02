#!/bin/bash
# PostToolUse hook: validate vault .md writes (report-only, never rewrites).
# Reads hook JSON from stdin; extracts file_path; runs validators scoped to the file
# plus fast global checks. Exit 2 = feed problems back to Claude (blocking feedback).
set -u
OPS_DIR="$(cd "$(dirname "$0")/../.." && pwd)"
PY="$OPS_DIR/.venv/bin/python"
[ -x "$PY" ] || PY="python3"

INPUT="$(cat)"
FILE=$(printf '%s' "$INPUT" | "$PY" -c "import sys,json
try:
    d=json.load(sys.stdin); print(d.get('tool_input',{}).get('file_path',''))
except Exception: print('')" 2>/dev/null)

# Only act on markdown inside the resolved vault (honours $VAULT_PATH).
case "$FILE" in
  *.md) ;;
  *) exit 0 ;;
esac
VAULT=$("$PY" -c "import sys;sys.path.insert(0,'$OPS_DIR/scripts');import brainlib;print(brainlib.vault_root())" 2>/dev/null)
case "$FILE" in
  "$VAULT"/*) ;;
  *) exit 0 ;;  # not a vault markdown write — nothing to do
esac
case "$FILE" in
  */templates/*|*/99_ARCHIVE/*) exit 0 ;;
esac

OUT=""
R1=$("$PY" "$OPS_DIR/scripts/validate_frontmatter.py" "$FILE" 2>&1) || OUT="$OUT$R1
"
R2=$("$PY" "$OPS_DIR/scripts/detect_duplicate_ids.py" 2>&1) || OUT="$OUT$R2
"
R3=$("$PY" "$OPS_DIR/scripts/check_wikilinks.py" 2>&1) || OUT="$OUT$R3
"
if [ -n "$OUT" ]; then
  echo "vault validation failed for $FILE:" >&2
  echo "$OUT" >&2
  exit 2
fi
exit 0
