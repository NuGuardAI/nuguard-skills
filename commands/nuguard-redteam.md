---
name: nuguard-redteam
description: Run authorized non-destructive NuGuard adversarial testing and report evidence.
allowed-tools: ["Read", "Bash"]
---

Check `nuguard.yaml` or the user-specified config, SBOM path, target URL, and test identity. Red-team testing sends adversarial payloads and can consume target quota. Run `nuguard target verify --config nuguard.yaml` first; stop if it fails or identifies an unexpected account. Do not use `--launch` or destructive scenarios unless the user explicitly requested them.

Run `nuguard redteam --config nuguard.yaml --scenarios non-destructive`, adjusting only options the user requested and confirming them with `nuguard redteam --help`. If the user explicitly authorized destructive testing, include `destructive` only within the authorized target and scope. Do not expose credentials in shell arguments or output.

Report confirmed findings with severity, scenario, minimum necessary response evidence, and a concrete fix. Distinguish a target quota failure or aborted run from a clean result. Redact canary values, secrets, and customer data in the report.
