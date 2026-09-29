---
name: nuguard-sbom
description: Generate an AI-SBOM from source or an authorized repository, then review it for coverage gaps using Claude Code's model.
allowed-tools: ["Read", "Grep", "Glob", "Bash"]
---

Parse the user's requested source, repository URL, ref, output path, and format. Default to the current directory and `app.sbom.json`. Run `nuguard sbom generate --source . --output app.sbom.json --no-llm`, or use `--from-repo URL --ref REF` for a repository the user asked to scan. Use `--format cyclonedx` or `cyclonedx-ext` only if requested. Confirm flags with `nuguard sbom generate --help` when needed. Follow the `claude-code-llm` skill: do not add `--llm` and do not ask for an LLM key.

Read the generated JSON and summarize actual node counts by `component_type`, edge and dependency counts, frameworks, and notable risk metadata. If it has zero nodes, explain the likely coverage gap and stop.

Then do the review the CLI's LLM pass would otherwise do. For a local source tree, search the code for agents, tools, prompts, model calls, datastores, and MCP servers that are missing from the SBOM (dynamic registration, non-literal prompts, custom orchestration). List each gap with file and line, and say what to add or how to widen extraction. For a remote repository you have not cloned, say the review was skipped. Do not modify the SBOM, present a risk signal as a confirmed exploit, or echo secrets or raw prompt content.
