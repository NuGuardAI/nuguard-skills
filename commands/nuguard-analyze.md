---
name: nuguard-analyze
description: Run NuGuard static analysis on an AI-SBOM, then triage each finding against the source using Claude Code's model.
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---

Use the SBOM path the user supplied, or `app.sbom.json`; confirm the file exists, and run `/nuguard-sbom` first if it does not. Run `nuguard analyze --sbom app.sbom.json --source . --min-severity medium --no-llm --format json --output nuguard-analysis.json`, replacing paths or severity with requested values. Add `--format markdown` if the user wants a report file. Check `nuguard analyze --help` before using additional flags. Do not silently disable NGA, ATLAS, CVE, IaC, container, or supply-chain checks.

NuGuard exits nonzero when findings meet `--fail-on`; inspect its output and stderr to tell this from a failed scan. Read the JSON report. For each critical and high finding, and any others the user cares about, open the cited code and judge whether it is real in this application. Report severity, rule ID, component, evidence, your verdict (confirmed, probable false positive with a stated reason, or needs runtime confirmation), and a specific code-level fix. Offer to apply the fixes; do not edit source unasked.

Note unavailable external scanners or feeds as coverage limits. Separate the CLI's findings from your triage. Redact sensitive snippets before quoting them.
