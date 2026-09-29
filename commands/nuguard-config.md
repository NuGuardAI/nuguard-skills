---
name: nuguard-config
description: Set up NuGuard CLI configuration without putting credentials in tracked files.
allowed-tools: ["Read", "Edit", "Write", "Bash"]
---

Help configure NuGuard for the current project. Read `nuguard.yaml` if it exists. If absent, run `nuguard init` only if the user requested project setup; otherwise explain that it creates starter files. Check `nuguard init --help` for current flags.

Set the source, SBOM path, LLM model, policy path, and target URL from values the user provides. Put secrets in environment variables or a secret manager and use `${ENV_VAR}` references in `nuguard.yaml`. Never request a raw secret in chat, write it into `.claude/`, or pass it as a shell argument. Refer to `nuguard.yaml.example` in the NuGuard package for the current configuration shape. Do not overwrite existing user configuration without preserving its unrelated settings.

For live testing, confirm the URL, expected test account, and any test restrictions. Explain that `nuguard target verify --config nuguard.yaml` sends probes before the behavior or red-team commands. Report which non-secret settings changed and which environment variable names the user needs to set.
