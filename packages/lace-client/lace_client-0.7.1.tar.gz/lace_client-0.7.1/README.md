# Lace Client (SDS Generator)

Thin, online-only CLI that generates the EU AI Act Article 53(1)(d) public training summary (DOCX) via the Lace Cloud. No local DOCX generation; `--dry-run` assembles payloads for CI/review.

## Install
```bash
python -m venv .venv && . .venv/bin/activate
pip install -U pip
pip install -e .
```

## Quickstart
```bash
# Dry-run (no network)
python -m lace.cli pack examples/sample \
  --answers-file examples/answers_sample.json \
  --dry-run

# Real run (requires API key)
export LACE_API_KEY=lace_sk_...
python -m lace.cli pack /path/to/dataset \
  --answers-file examples/answers_sample.json \
  --out ./examples/output/summary.docx
```
Notes:
- Online-only: real runs call the Lace API.
- --dry-run prints the payload and EU answers summary without network calls.
- Override base URL with `--api-base` if needed.
