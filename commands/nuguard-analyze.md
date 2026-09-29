---
name: nuguard-analyze
description: Run NuGuard static analysis on an AI-SBOM and explain the findings.
allowed-tools: ["Read", "Bash"]
---

Use the SBOM path the user supplied, or `app.sbom.json`; confirm the file exists. Run `nuguard analyze --sbom app.sbom.json --min-severity medium`, replacing the path or severity with requested values. Check `nuguard analyze --help` before using additional flags. Do not silently disable NGA, ATLAS, CVE, IaC, container, or supply-chain checks.

NuGuard can exit nonzero when findings meet `--fail-on`; inspect its output and stderr to distinguish this from a failed scan. Report actual findings with severity, rule ID, component, evidence, and specific remediation. Note unavailable external scanners or feeds as coverage limits. Redact sensitive snippets before quoting them.
