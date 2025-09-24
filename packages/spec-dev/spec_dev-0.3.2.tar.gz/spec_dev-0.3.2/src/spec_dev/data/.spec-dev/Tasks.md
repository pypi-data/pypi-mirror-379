# Tasks Phase — Instructions (v1.3)

**Guardrail:** You are in the Tasks phase. Translate the approved Plan & Intent into a phased execution board, then stop. Do not write code or merge tasks. Keep the board additive—move finished cards to the `Done` phase with the CLI instead of deleting them.

**Goal:** Produce `active-tasks.md` — a phase-structured, independently testable set of tasks that implements the plan. This becomes the authoritative change plan.

**Single output file:** `.spec-dev/active-dev/active-tasks.md`

## Requirements

- Organise tasks under numbered phase headings (`## Phase 0 — …`, `## Phase 1 — …`). Each phase title should include a status badge in parentheses, e.g. `*(planned)*`, `*(in progress)*`, `*(completed YYYY-MM-DD)*`.
- 5–25 tasks total. If more than 25, split into phases or feature flags.
- Each task remains ≤ ~6 hours and owns its acceptance criteria.
- Tasks must list exact **file paths** and **operations** (add/modify/delete/move) without wildcards.
- Maintain the canonical task header format `### T-### — <title>` so CLI tooling continues to work.
- Every task must include a `**Status:**` line (`pending`, `in-progress`, `done`) and a `changes` fenced block for manifest generation.
- Reference Plan & Intent sections when helpful, especially for cross-phase dependencies.

## Task Entry Format (per task)

```
### T-001 — <short title>
**Status:** pending
**Phase Goal:** <how this task contributes to the phase objective>
**Acceptance (Given/When/Then)**:
- Given …
- When …
- Then …

**Changes**
```changes
<path>: <op> -> <detail> @ <optional selector>
```

**Dependencies**: [T-000, …] or []
**Owner**: agent   **Estimate**: 3h   **Risk**: medium
**Notes**: <optional clarifications, links to plan sections>
```

> `changes` blocks remain mandatory so `spec-dev tasks-manifest` can build the coverage file. Add `@ <selector>` to scope work to a region (e.g. `@ fn:init`). If omitted, the task claims the entire file.

## Flow

1. **Phase Outline** — Copy the ordered phases from `active-plan.md` (Phase 0, Phase 1, …). Note the objective and any phase-level dependencies under each heading.
2. **Draft Tasks** — Under each phase, add `### T-###` sections following the strict format above. Call out tests/docs/telemetry in `Changes` or `Notes`.
3. **Sequencing & Dependencies** — Ensure tasks are ordered logically within each phase. Use `Dependencies` sparingly for true blockers.
4. **Status Management** — Initialise all tasks with `**Status:** pending`. Use `spec-dev tasks-status T-### --set <pending|in-progress|done>` to update later; keep the heading badge (`*(planned)*`, etc.) aligned with actual status.
5. **Coverage Validation** — Run `spec-dev tasks-manifest --auto-scope --rewrite --check` after drafting to regenerate `active-dev/file-coverage.json` and ensure unique `(path, selector)` pairs.
6. **Sanity Pass** — Confirm every plan action maps to a task, file paths are precise, and phase exit criteria are satisfied by the listed tasks.

## Readiness Checklist
- [ ] Phases mirror the plan and include status badges.
- [ ] Every task follows the strict header + status + acceptance + `changes` format.
- [ ] `spec-dev tasks-manifest --rewrite --check` passes with no collisions.
- [ ] Each task is independently testable with clear acceptance criteria.
- [ ] Dependencies are minimal and non-circular.
- [ ] Notes reference relevant plan sections where extra context is helpful.

## Gate
- End the file with `Gate: READY FOR IMPLEMENTATION` only when all checks pass and the Plan & Intent phase is marked `Gate: PASS`.
- If anything is missing, leave the gate unset and pause for review.
- After the gate is marked READY, stop and wait for human approval before entering the Implementation phase.

**Output location:** `.spec-dev/active-dev/active-tasks.md`
