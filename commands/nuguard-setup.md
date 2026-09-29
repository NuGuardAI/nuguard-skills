---
name: nuguard-setup
description: Check that the NuGuard CLI is installed and ready to run with Claude Code's model, without needing an LLM API key.
allowed-tools: ["Read", "Bash"]
---

Run `nuguard --help` to check the CLI is on PATH. If it is missing, tell the user to install it with `pipx install nuguard` (or `uv tool install nuguard`) and ask before running the install yourself. Check the Python version the install reports; NuGuard needs Python 3.11 or newer.

Report which optional scanners are on PATH: `grype`, `checkov`, `trivy`, and `semgrep`. A missing scanner is a coverage limit for `nuguard analyze`, not an error. Report only the variable names, never values, of any LLM provider keys exported in the shell (`LITELLM_API_KEY`, `GEMINI_API_KEY`, `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`).

Explain that this plugin runs the CLI without an LLM key and uses Claude Code's model for the LLM steps (see the `claude-code-llm` skill). Suggest `/nuguard-sbom` to start, and `/nuguard-init` for project config.
