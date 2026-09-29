---
name: nuguard-scan
description: Run NuGuard's unified SBOM and static analysis scan; extend to live testing only when requested.
allowed-tools: ["Read", "Bash"]
---

For a normal scan, run `nuguard scan --source . --steps sbom,analyze`, changing `--source` if the user specified another path. Check `nuguard scan --help` for additional options. Default reports are under `nuguard-reports/`; list only files that were actually written. A findings-based nonzero exit is distinct from a CLI error.

If the user asks for a full audit, first run the static scan. Check the requested policy, target URL, credentials, and test account. Run `nuguard target verify --config nuguard.yaml` before live tests and stop on an unexpected identity. Then use `nuguard behavior --config nuguard.yaml --mode static+dynamic` and, if red-team testing was requested, `nuguard redteam --config nuguard.yaml --scenarios non-destructive`. The unified `scan` CLI has no scenario-safety flag, so do not add its `redteam` step by default. Destructive scenarios need explicit authorization.

Summarize findings by severity, the specific fixes, and any skipped stage or coverage limit. Do not fabricate report artifacts or clean results.
