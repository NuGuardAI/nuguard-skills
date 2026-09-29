---
name: nuguard-behavior
description: Run NuGuard behavior validation against an AI application and judge the results with Claude Code's model.
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---

Read `nuguard.yaml` or the config path the user supplied, and the Cognitive Policy path it names. If there is no policy, run `/nuguard-policy` first and get the user's confirmation of it. Follow the `claude-code-llm` skill: leave `llm.api_key` unset and pass `--intent` with a one-line description of the app, taken from the policy or the user, so the CLI does not need an LLM to infer it.

For `--mode static`, run `nuguard behavior --config nuguard.yaml --sbom app.sbom.json --mode static --format json --output behavior-report.json`; no live target is needed. For `dynamic` or `static+dynamic`, confirm the authorized target URL and expected test account, then run `nuguard target verify --config nuguard.yaml` first because it sends probes. Stop if verification fails or discovers an unexpected identity. Then run `nuguard behavior --config nuguard.yaml --mode static+dynamic --format json --output behavior-report.json` unless another mode was requested. Check `nuguard behavior --help` for extra flags. Never pass credentials as command arguments; the config uses `${ENV_VAR}` references.

Read `behavior-report.json`. Follow the "Judging behavior results" section of the `claude-code-llm` skill for failed or uncertain scenarios. Distinguish policy alignment and intent drift from confirmed exploitation. Explain which tests ran, what was observed, and any failed or skipped checks, and say that guided multi-turn coverage was not steered by Claude Code's model. Redact sensitive response content.
