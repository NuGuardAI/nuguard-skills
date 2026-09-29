---
name: ai-security-review
description: Use when asked to assess an AI application with the NuGuard package, including AI-SBOM generation, static findings, behavior validation, or authorized red-team testing. Do not use for unrelated code review.
---

# NuGuard AI security review

Select the NuGuard stage that matches the request. Use the `claude-code-llm` skill so Claude Code's model does the LLM steps and no separate LLM key is needed. Use the installed CLI and its current `--help` when flags differ from these examples. Do not install packages automatically or expose credentials in commands or reports.

## Inventory and static findings

1. Run `nuguard sbom generate --source . --output app.sbom.json --no-llm` for an authorized source tree. Use `--from-repo URL` only for a repository the user asked to scan. If the SBOM has zero nodes, check the source path and supported framework before claiming coverage.
2. Run `nuguard analyze --sbom app.sbom.json --min-severity medium --no-llm`. NuGuard may exit nonzero because findings meet `--fail-on`; inspect the report and stderr before calling it an execution failure.
3. Triage each finding against the source and report severity, component, evidence, your verdict, and specific remediation. Distinguish structural risk from a confirmed exploit. Treat missing external scanners or vulnerability feeds as coverage limits.

## Live testing

Only test a live target when the user requested it or authorized that target. Inspect `nuguard.yaml` and confirm the target URL and account. Run `nuguard target verify --config nuguard.yaml` first; this sends probes. Stop if the identity is unexpected or verification fails. `nuguard behavior --config nuguard.yaml --mode static+dynamic` checks intended behavior against a confirmed Cognitive Policy (draft it with `/nuguard-policy`). `nuguard redteam --config nuguard.yaml --scenarios non-destructive` sends adversarial payloads; use destructive scenarios only with explicit authorization.

Store credentials in environment variables or a secret manager, with `${ENV_VAR}` placeholders in config. Never write raw API keys, bearer tokens, or passwords into tracked files, shell command text, logs, or chat output.

## Reporting

Give a short risk summary, a findings table, the top specific fixes, and coverage limits. Quote only the minimum evidence needed and redact secrets or customer data. Never fabricate a passed check or finding. A canary hit is critical evidence; verify the run and identify the affected target before sharing details.
