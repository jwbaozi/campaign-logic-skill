# Multi-role Review Workflow

Use after the user explicitly asks for or agrees to multi-role review. It applies equally after a text diagnosis and after an HTML visual report.

1. Repeat the factual boundary and the roles selected. If no roles are given, ask the user to confirm the four default lenses in `logic/multi_role_review_engine.md`; do not assume they represent real people.
2. Read `logic/multi_role_review_engine.md` and create one role card per approved lens.
3. Keep each card tied to an existing issue, decision, or assumption. Do not repeat the full original diagnosis.
4. Consolidate duplicate concerns into a cross-role decision list, separating proposal-stage decisions, pre-launch validations, and post-launch optimization.
5. If a visual report exists, append the same role cards to the Markdown source and regenerate the report; do not create a second, contradictory analysis.
