---
name: nuguard-behavior
description: Run NuGuard behavior validation for a configured AI application target.
allowed-tools: ["Read", "Bash"]
---

Read `nuguard.yaml` or the config path the user supplied. For `--mode static`, run `nuguard behavior --config nuguard.yaml --mode static`; no live target is needed. For `dynamic` or `static+dynamic`, confirm the authorized target URL and expected test account. Run `nuguard target verify --config nuguard.yaml` first because it sends probes. Stop if verification fails or discovers an unexpected identity.

Run `nuguard behavior --config nuguard.yaml --mode static+dynamic` unless another mode was requested. Check `nuguard behavior --help` for extra flags. Distinguish policy alignment and intent drift from confirmed exploitation. Explain which tests ran, what was observed, and any failed or skipped checks. Redact sensitive response content.
