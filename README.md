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

The plugin supplies two skills, the `/nuguard-config`, `/nuguard-init`, `/nuguard-sbom`, `/nuguard-analyze`, `/nuguard-scan`, `/nuguard-behavior`, and `/nuguard-redteam` commands, and a `security-auditor` agent. It does not store credentials. Configure the CLI with environment variables and `${ENV_VAR}` references in `nuguard.yaml`.

## Skills for Claude Code, Codex, and GitHub Copilot

The shared skills are [`ai-security-review`](skills/ai-security-review/SKILL.md) for NuGuard scan and findings workflows and [`sbom-analysis`](skills/sbom-analysis/SKILL.md) for interpreting an AI-SBOM. To install them in an existing project, clone this repository and run:

```bash
python3 scripts/install.py --project /path/to/project --tool all
```

The installer copies the skills into `.claude/skills/`, `.agents/skills/`, and `.github/skills/`. Use `--tool claude`, `--tool codex`, or `--tool copilot` to select one. It refuses to overwrite an existing modified skill. Claude Code users who install the plugin do not need a second copy of its skills in the project.

## Security and scope

Static scans may read repository content and query vulnerability data sources. Behavior and red-team commands send traffic to a live application; confirm its URL and test identity first. The plugin defaults red-team runs to non-destructive scenarios. Review reports before sharing them because they may contain source paths, findings, or response excerpts. Never put tokens or passwords in command arguments, tracked configuration, or chat output.

## Develop

Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests`. Update examples against the [NuGuard CLI source](https://github.com/NuGuardAI/nuguard/tree/develop/nuguard/cli/commands) when the package changes. The files derived from the NuGuard package plugin and this repository are licensed under [Apache 2.0](LICENSE).
