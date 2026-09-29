---
name: nuguard-init
description: Initialize NuGuard config, canary template, and cognitive policy for this project.
allowed-tools: ["Read", "Bash"]
---

Run `nuguard init` in the requested project directory. Use `--target` or `--source` only for values the user supplied, and quote them safely as shell arguments. Check `nuguard init --help` if the installed CLI differs. Do not pass `--force` unless the user explicitly asked to overwrite existing generated files. Do not turn on `--llm` unless the user requested model drafting and credentials are already available in the environment.

Report which files were created and which were skipped. The expected starter files include `nuguard.yaml`, `canary.example.json`, and `cognitive-policy.md`; verify actual output. Keep credentials in environment variables and `${ENV_VAR}` references, never literal YAML values.
