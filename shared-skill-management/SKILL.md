---
name: shared-skill-management
description: Use when creating, updating, linking, validating, testing, or troubleshooting skills shared between Codex and Claude Code. Apply when the user asks where skills live, how to share one SKILL.md across tools, whether to use symbolic links, how to verify automatic skill invocation, or how to manage shared skill source directories.
---

# Shared Skill Management

## Goal

Manage one source skill directory that both Codex and Claude Code can discover without duplicating `SKILL.md`.

Use symbolic links for shared personal skills unless a tool cannot follow the link. If a link fails in a restricted sandbox, prefer moving the source under the most restrictive tool's native skill directory and linking the other tools to it.

## Standard Layout

Preferred durable layout:

```text
/root/shared-agent-skills/<skill-name>/
└── SKILL.md

/root/.agents/skills/<skill-name> -> /root/shared-agent-skills/<skill-name>
/root/.claude/skills/<skill-name> -> /root/shared-agent-skills/<skill-name>
/root/.codex/skills/<skill-name> -> /root/shared-agent-skills/<skill-name>  # optional local compatibility link
```

Codex's documented user skill path is `/root/.agents/skills`. Claude Code's user skill path is `/root/.claude/skills`. Keep `/root/.codex/skills` only when the local Codex installation also scans or displays skills there.

## Create Or Update A Shared Skill

1. Use `skill-creator` before creating or materially changing a skill.
2. Create or edit the source under `/root/shared-agent-skills/<skill-name>/`.
3. Keep frontmatter portable: use at least `name` and `description`; avoid tool-specific fields unless required.
4. Put reusable workflow instructions in `SKILL.md`; do not create extra README or guide files unless the skill truly needs references.
5. Link the skill into each tool:

```bash
mkdir -p /root/.agents/skills /root/.claude/skills /root/.codex/skills
ln -sfn /root/shared-agent-skills/<skill-name> /root/.agents/skills/<skill-name>
ln -sfn /root/shared-agent-skills/<skill-name> /root/.claude/skills/<skill-name>
ln -sfn /root/shared-agent-skills/<skill-name> /root/.codex/skills/<skill-name>
```

## Validation

Run structural validation:

```bash
python /root/.codex/skills/.system/skill-creator/scripts/quick_validate.py /root/shared-agent-skills/<skill-name>
```

Verify links and readable `SKILL.md` files:

```bash
for p in \
  /root/.agents/skills/<skill-name> \
  /root/.claude/skills/<skill-name> \
  /root/.codex/skills/<skill-name>; do
  printf '%s -> %s\n' "$p" "$(readlink -f "$p")"
  test -f "$p/SKILL.md" || exit 1
done
```

For Codex, verify discovery in prompt context:

```bash
codex debug prompt-input 'test skill discovery' | rg '<skill-name>|/root/shared-agent-skills/<skill-name>/SKILL.md'
```

## Invocation Tests

Test both explicit and implicit invocation.

Explicit:

```bash
codex exec --ephemeral --skip-git-repo-check -s danger-full-access '$<skill-name> <small realistic task>'
printf '%s\n' '/<skill-name> <small realistic task>' | claude -p --model sonnet --max-budget-usd 0.50 --setting-sources user
```

Implicit:

```bash
codex exec --ephemeral --skip-git-repo-check -s danger-full-access '<small realistic task that should match the skill description>'
printf '%s\n' '<small realistic task that should match the skill description>' | claude -p --model sonnet --max-budget-usd 0.50 --setting-sources user
```

For Codex, confirm the output says it is using the skill or clearly follows the skill after reading `SKILL.md`. For Claude Code, confirm the output behavior matches the skill; if available, use debug or transcript output to inspect skill loading.

## Troubleshooting

- If Codex discovers the skill but cannot read `SKILL.md` in a restricted sandbox, retry with the same sandbox the user normally uses. If restricted sandboxes must work, move the source under `/root/.agents/skills/<skill-name>` and link Claude Code to that source.
- If a tool does not pick up changes immediately, restart the tool.
- If automatic invocation is weak, improve the `description` with concrete trigger words and realistic task types.
- If two skills have the same `name`, rename one; do not rely on merge behavior.
- Do not duplicate the same skill by copying files into multiple tool directories unless symlinks fail. Copies drift.
