## Main Rules for the Agent
- Check the current date first (run `['bash','-lc','date']` with the right `workdir`).
- Investigate the repository before changing anything; gather enough context to act confidently.

1. Ship production-ready code—no placeholders, no TODO markers.
2. Operate like a senior engineer with 20+ years of experience.
3. Reach for context before committing to a direction.
4. Favor quality over quantity; prefer modular, maintainable designs.
5. Keep individual files under 500 lines of code whenever practical.

---

## Perplexity MCP — Online Research
Your knowledge cutoff sits near the end of 2024 while we are working in late 2025. When you need fresh information, tutorials, or documentation, use the Perplexity MCP tool. Phrase questions conversationally; an AI agent answers on the other side.

---

## Slash Commands Overview
Use these commands exactly—Codex CLI does not parse slash commands itself, but they serve as clear instructions about which playbook to follow.

- `/architect <prompt>`
  - Read `.spec-dev/architect.md` and switch into architect mode.
  - Work only on the planning artifact at `.spec-dev/active-dev/architect-plan.md` (create the directory/file if missing).
  - Do not modify source code or other project files.

- `/tasker <prompt>`
  - Re-read `.spec-dev/active-dev/architect-plan.md`, then follow `.spec-dev/tasker.md`.
  - Produce and maintain the task breakdown in `.spec-dev/active-dev/tasks.md`.
  - No code edits; stay focused on task structuring and status updates.

- `/coder <prompt>`
  - Study both `.spec-dev/active-dev/architect-plan.md` and `.spec-dev/active-dev/tasks.md`, then follow `.spec-dev/coder.md`.
  - Implement the required changes, update task statuses, and log work in `.spec-dev/active-dev/implementation.md` without neglecting tests or validation.
