# NuGuard Skills

Open source, reusable agent skills for building and reviewing AI security software with NuGuard conventions. The same `SKILL.md` files work with Claude Code, Codex, and GitHub Copilot. They are guidance for coding agents, not a security scanner or a substitute for server-side controls.

## Skills

| Skill | Use it for |
| --- | --- |
| `nuguard-aibom` | AI bill of materials extraction, graph identity, evidence, and exports |
| `nuguard-tenant-security` | Tenant isolation, authorization, hostile inputs, and sensitive data |
| `nuguard-api-contracts` | Changes to service APIs and their clients or tests |
| `nuguard-frontend` | NuGuard React, TypeScript, validation, and error handling |
| `nuguard-code-review` | Evidence-based review of NuGuard changes |

Each skill is independently selectable. Read its frontmatter to see when it applies. The skills use repository files as the source of truth when a local NuGuard implementation differs from an example here.

## Install in a project

Clone this repository, then run from the clone:

```bash
python3 scripts/install.py --project /path/to/your-project --tool all
```

The installer copies the skills to `.claude/skills/`, `.agents/skills/`, and `.github/skills/` for Claude Code, Codex, and GitHub Copilot respectively. Select one tool with `--tool claude`, `--tool codex`, or `--tool copilot`. It does not overwrite existing skills; a conflicting skill stops installation and leaves that skill untouched. Commit the installed skills in your project if you want the team to share them.

For a personal installation, copy the desired folders from `skills/` into `~/.claude/skills/` or `~/.codex/skills/`. Copilot skills belong in a repository's `.github/skills/` directory.

## Use

Ask your agent to use a skill by name, for example, “Use `nuguard-aibom` to review this extraction change,” or let the agent select it from its description. NuGuard repository instructions, actual API schemas, and current code take precedence over examples in this package.

## Contributing

Keep each skill focused on decisions that require NuGuard context. Add a clear trigger in the frontmatter, avoid secrets and customer data, and verify examples against the current public code before proposing a change. Run `python3 scripts/validate.py` and `python3 -m unittest discover -s tests` before opening a pull request.

Licensed under the [MIT License](LICENSE).
