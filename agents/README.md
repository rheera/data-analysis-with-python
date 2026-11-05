# Agent ID cards

One file per agent that works on this repo: what it is, where it's defined, and its parameters.

| File | Agent |
|---|---|
| `main.yaml` | Claude, the main agent in cloud sessions |
| `minimax.yaml` | MiniMax, called from Python over its API |
| `subagents/*.yaml` | Each subagent Claude can start |

- **The Claude cards are descriptive.** Claude Code doesn't read this folder; the live settings come from the session itself, `CLAUDE.md` and `.claude/` (if added). To make a subagent card live, rewrite it as a Markdown file under `.claude/agents/`.
- **The MiniMax card is real config.** Load it with `yaml.safe_load()` and send `system_prompt` as the first message.
- **Claude model names are left out.** The main agent's model is chosen per session, and subagents use their own definition's model or inherit the main one.
- Snapshot taken with Claude Code 2.1.318 on 2026-11-05. The subagent list and tools can change between versions.
