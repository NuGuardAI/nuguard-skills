---
name: nuguard-policy
description: Draft and validate a Cognitive Policy for behavior testing, written by Claude Code's model from the SBOM and source.
allowed-tools: ["Read", "Write", "Edit", "Bash"]
---

Behavior validation needs a Cognitive Policy that states what the application should and must not do. Use the SBOM path the user supplied, or `app.sbom.json`; if it is missing, run `/nuguard-sbom` first. Run `nuguard policy draft --sbom app.sbom.json --no-llm --output cognitive-policy.md` to get the current template (add `--force` only if the user agreed to overwrite an existing file). Check `nuguard policy draft --help` if the flags differ.

Then read the template, the SBOM, and the relevant source, and rewrite the policy with the application's real purpose, allowed and forbidden topics, restricted tool actions, data-handling rules, and human-escalation rules. Keep the template's structure so `nuguard policy validate` accepts it. Ask the user for a one-line description of the app if the code does not make its purpose clear. Do not invent rules the code or the user does not support; mark uncertain ones for the user to confirm.

Run `nuguard policy validate --file cognitive-policy.md` and fix reported problems. Show the user a summary of the policy and get confirmation before it is used for behavior testing. Never put secrets or real customer data in the policy.
