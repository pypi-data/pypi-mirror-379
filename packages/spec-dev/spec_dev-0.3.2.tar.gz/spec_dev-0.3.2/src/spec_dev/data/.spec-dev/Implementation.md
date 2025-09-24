# Implementation Phase — Instructions (v1.3)

**Guardrail:** Enter this phase **only** after the Plan & Intent and Tasks gates are both marked PASS/READY and a human authorises implementation. Execute tasks strictly in order, one at a time. After completing a task (code + tests), stop and wait for the next instruction or hand-off before proceeding. If a task is unclear or blocked, pause and revise the plan or board before writing code.

**Goal:** Deliver the tasks from `active-tasks.md` with tight diffs, full traceability, and documented verification. Update `active-implementation.md` after each task and keep the phase badges in the task board accurate (planned → in progress → completed).

**Output file to update continuously:** `.spec-dev/active-dev/active-implementation.md`

## Rules

- Work on **one task at a time**. Never mix tasks or run ahead.
- Implement only what the task’s `changes` block describes. If scope changes, pause and update the task card first.
- Each task must ship with the tests/docs/telemetry noted in the plan.
- Keep diffs minimal and reversible. Feature flags where appropriate.
- Update the phase heading in `active-tasks.md` to `*(in progress)*` when you begin work on its first task and to `*(completed YYYY-MM-DD)*` after the final task in that phase is done.

## Update Log Format (per completed task)

```
## <Task ID> — <title>
**When**: <YYYY-MM-DD>
**Change Ref**: <commit SHA/link or short patch note>
**Status**: done | partial | reverted
**Evidence**:
- Tests: <commands/results>
- Manual/QA: <steps taken>
- Telemetry: <metrics/alerts touched>
**Notes**: <follow-ups, risks, memory links>
```

> Optional: when you finish the final task in a phase, add a single bullet in the next task entry’s **Notes** (e.g., “Phase 2 complete — exit checks: …”). No separate phase section is required.

## Execution Loop (per task)

1. Re-read the task card and the relevant Plan & Intent sections; restate acceptance criteria internally.
2. Confirm the plan still aligns; if not, stop and update upstream files before coding.
3. Implement the listed changes only. Keep commits focused on the task.
4. Run required tests/QA and capture results.
5. Update docs/telemetry as specified.
6. Append the Update Log entry. Link to any new memory (e.g., `.spec-dev/active-memories/T-XXX`).
7. Run `spec-dev memory T-XXX` (if the file does not exist or needs updates),
   `spec-dev tasks-status T-XXX --set done`, `spec-dev tasks-manifest --rewrite --check`,
   and `spec-dev memories` (add `--ensure` if you need to scaffold missing files).
8. If completing the final task of a phase, update that phase heading in `active-tasks.md` to `*(completed YYYY-MM-DD)*`.
9. Stop. Await human approval or new instructions before starting the next task.

## Completion Criteria

- Every task in `active-tasks.md` has a matching log entry with evidence.
- Phase badges in `active-tasks.md` reflect actual status (planned / in progress / completed with date).
- Tests/docs/telemetry updates are committed as planned.
- No unplanned file edits; task board reflects reality.
- Agent is in a wait state until the next task is authorized.

**Output location:** `.spec-dev/active-dev/active-implementation.md`
