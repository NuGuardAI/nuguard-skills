---
name: nuguard-scan
description: Run NuGuard's unified SBOM and static analysis scan, triaged by Claude Code's model; extend to live behavior testing only when requested.
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---

For a normal scan, run `nuguard scan --source . --steps sbom,analyze`, changing `--source` if the user specified another path. Do not pass `--llm`; follow the `claude-code-llm` skill. Check `nuguard scan --help` for additional options. Default reports are under `nuguard-reports/`; list only files that were actually written. A findings-based nonzero exit is distinct from a CLI error. Then triage the findings and review SBOM coverage as `/nuguard-analyze` and `/nuguard-sbom` describe.

If the user asks for a full audit, first run the static scan. Draft and confirm the policy with `/nuguard-policy`, then check the target URL, credentials, and test account. Run `nuguard target verify --config nuguard.yaml` before live tests and stop on an unexpected identity. Then follow `/nuguard-behavior` for `nuguard behavior --config nuguard.yaml --mode static+dynamic`. Run red-team testing only if requested, using `nuguard redteam --config nuguard.yaml --scenarios non-destructive`. The unified `scan` CLI has no scenario-safety flag, so do not add its `redteam` step by default. Destructive scenarios need explicit authorization.

Summarize findings by severity, the specific fixes, and any skipped stage or coverage limit. Do not fabricate report artifacts or clean results.
