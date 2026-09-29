---
name: nuguard-sbom
description: Generate and summarize a NuGuard AI-SBOM from source or an authorized repository.
allowed-tools: ["Read", "Bash"]
---

Parse the user's requested source, repository URL, ref, output path, and LLM preference. Default to the current directory and `app.sbom.json`. Run `nuguard sbom generate --source . --output app.sbom.json`, or use `--from-repo URL --ref REF` for a repository the user asked to scan. Confirm flags with `nuguard sbom generate --help` when needed. Pass `--llm` only when requested and a provider key is available through the environment.

Read the generated JSON and summarize actual node counts by `component_type`, edge and dependency counts, frameworks, and notable risk metadata. If it has zero nodes, explain the likely coverage gap and stop. Do not present an SBOM risk signal as a confirmed exploit. Do not echo secrets or raw prompt content from the SBOM.
