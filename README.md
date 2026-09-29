# NuGuard Skills and Claude Code Plugin

Skills and a Claude Code plugin for the open source [NuGuard Python package](https://github.com/NuGuardAI/nuguard). They help an agent generate and interpret an AI-SBOM, run NuGuard's static analysis, and use behavior or red-team testing against an authorized live target.

This repository adapts the [package plugin on `develop`](https://github.com/NuGuardAI/nuguard/tree/develop/plugin). The NuGuard package and its current CLI help, schema, and configuration remain authoritative if a command or field changes. The plugin expects the `nuguard` CLI to be installed separately; it does not bundle the Python package.

## Claude Code plugin

In Claude Code:

```text
/plugin marketplace add NuGuardAI/nuguard-skills
/plugin install nuguard
```

Or use `claude plugin marketplace add NuGuardAI/nuguard-skills` and `claude plugin install nuguard` in a terminal. Install the package with `pipx install nuguard` or another Python environment of your choice, then check `nuguard --help`.

The plugin supplies three skills, the commands below, and a `security-auditor` agent. It does not store credentials. Configure the CLI with environment variables and `${ENV_VAR}` references in `nuguard.yaml`.

| Command | What it does |
| --- | --- |
| `/nuguard-setup` | Check the CLI, optional scanners, and LLM setup |
| `/nuguard-init`, `/nuguard-config` | Create and edit `nuguard.yaml` without putting secrets in it |
| `/nuguard-sbom` | Generate an AI-SBOM, then review it for coverage gaps |
| `/nuguard-analyze` | Run static analysis, then triage each finding against the source |
| `/nuguard-policy` | Draft and validate the Cognitive Policy that behavior testing checks against |
| `/nuguard-behavior` | Verify the target, run behavior validation, and judge the results |
| `/nuguard-scan` | SBOM plus static analysis in one step; a full audit adds behavior testing |
| `/nuguard-redteam` | Non-destructive adversarial testing of an authorized live target |

A typical developer flow is `/nuguard-setup`, `/nuguard-sbom`, `/nuguard-analyze`, then `/nuguard-policy` and `/nuguard-behavior` once the app is running locally or in a test environment.

### LLM: Claude Code's model

You do not need an LLM API key. The plugin runs the CLI in its deterministic mode (`--no-llm`, no `llm.api_key`) and Claude Code's model does the LLM steps: reviewing the SBOM for gaps, triaging findings, drafting the Cognitive Policy, and judging behavior results. The [`claude-code-llm`](skills/claude-code-llm/SKILL.md) skill defines the split. Claude Code's model runs in your session, so guided multi-turn coverage and adaptive red-team mutation still need a provider key configured for the CLI. If you set one yourself, the plugin uses it as configured.

## Skills for Claude Code, Codex, and GitHub Copilot

The shared skills are [`ai-security-review`](skills/ai-security-review/SKILL.md) for NuGuard scan and findings workflows, [`sbom-analysis`](skills/sbom-analysis/SKILL.md) for interpreting an AI-SBOM, and [`claude-code-llm`](skills/claude-code-llm/SKILL.md) for using the host agent's model instead of a separate LLM key. To install them in an existing project, clone this repository and run:

```bash
python3 scripts/install.py --project /path/to/project --tool all
```

The installer copies the skills into `.claude/skills/`, `.agents/skills/`, and `.github/skills/`. Use `--tool claude`, `--tool codex`, or `--tool copilot` to select one. It refuses to overwrite an existing modified skill. Claude Code users who install the plugin do not need a second copy of its skills in the project.

## Security and scope

Static scans may read repository content and query vulnerability data sources. Behavior and red-team commands send traffic to a live application; confirm its URL and test identity first. The plugin defaults red-team runs to non-destructive scenarios. Review reports before sharing them because they may contain source paths, findings, or response excerpts. Never put tokens or passwords in command arguments, tracked configuration, or chat output.

## Develop

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests`. Update examples against the [NuGuard CLI source](https://github.com/NuGuardAI/nuguard/tree/develop/nuguard/cli/commands) when the package changes. The files derived from the NuGuard package plugin and this repository are licensed under [Apache 2.0](LICENSE).
