# Plan & Intent Phase — Instructions (v2.2)

**Guardrail:** Create a single `active-plan.md` that explains the strategy, file impact, and delivery phases. Stop for review before writing tasks or code.

**Goal:** Show how we will land the request: what success looks like, which files we will touch or create, and the phased path to completion.

**Single output file:** `.spec-dev/active-dev/active-plan.md`

## Flow

1. **Context Snapshot**
   - Problem & goal in one or two bullets.
   - Constraints or assumptions (timelines, tech debt, approvals).

2. **Strategy Summary**
   - Approach overview (1–2 paragraphs) covering the key design/architecture ideas.
   - Major risks, trade-offs, or decisions to confirm.

3. **File Impact Map**
   - Existing files to modify (table: `Path / Change Theme / Notes`).
   - New files to create (table: `Path / Purpose / Notes`). Include docs/config/infra if relevant.

4. **Phased Execution Plan**
   - Lay out ordered phases (`Phase 0`, `Phase 1`, …).
   - For each phase capture:
     - **Objective** — what the phase achieves.
     - **Work Items** — key steps or modules.
     - **Primary Files** — main files/folders touched.
     - **Exit Check** — how we know the phase is done (tests, demos, metrics).

5. **Validation & Rollout**
   - Testing plan (unit, integration, manual) with owners/tools.
   - Telemetry or observability changes (metrics, logs, dashboards).
   - Rollout notes (flags, stages, rollback triggers).

6. **Open Questions**
   - Outstanding items, who owns them, and when we need answers.

## Readiness Checklist
- [ ] Strategy summary explains how we will win and why it is safe.
- [ ] File impact map covers every file to touch and create.
- [ ] Phases are ordered with objectives, work items, primary files, and exit checks.
- [ ] Validation and rollout steps are actionable.
- [ ] Open questions list has owners or dates.

## Gate
- Append `Gate: PASS` once the checklist is complete; otherwise `Gate: FAIL — <reason>` and stop.
- Do not begin Tasks until this phase is reviewed and marked PASS.

**Style Tips**
- Keep the plan narrative and skimmable—aim for clarity over ceremony.
- Use plain bullets and short paragraphs; add appendices only if more depth is required.
- Reference prior memories or docs inline when they inform the approach.

**Output location:** `.spec-dev/active-dev/active-plan.md`
