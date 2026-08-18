# Proposal Review Workflow v2.4

Use for a marketing plan, campaign deck, brief, framework, or multi-file proposal that the user wants checked, diagnosed, or improved.

## Flow

`intake → material boundary and overall judgment → Campaign Logic causal-chain review → preserve valid content → ranked issue cards → execution/KPI closure → client/internal separation → Markdown audit source → HTML audit report`.

## Required execution

1. Read `workflows/intake.md`; state what can and cannot be judged from the supplied material.
2. Apply `logic/campaign_logic_engine.md` and `logic/proposal_deep_review_engine.md`; check Brief, commercial problem, goal, evidence, audience, insight, strategy, Core Idea, creative system, communication path, user loop, operations, KPI, and review.
3. Use the issue-card contract for every material finding. Classify it as `【缺失】`, `【薄弱】`, `【断层】`, `【冲突】`, `【空泛】`, `【不可落地】`, or `【可保留】`.
4. Call `logic/execution_planning_engine.md` for every material execution recommendation. Make the action, content, handoff, deliverable, owner, timing, channel, KPI, and risk explicit.
5. Use a methodology, presentation model, or visual asset only when it resolves a named decision. For goal/KPI repair, use SMART when appropriate; for a requested proposal structure, timeline, or strategy presentation, recommend and embed at least one fitting existing presentation model. Follow `knowledge/output-template.md`; embed assets in Markdown rather than printing paths.
6. Do not block on missing context. Label absent facts, explain the effect, and give a practical validation route; then finish the strongest evidence-bounded review possible from the uploaded material.
7. For a substantive uploaded proposal/deck, generate the Markdown audit source and self-contained HTML audit report through `workflows/visual-report.md` without waiting for the user to ask for a report. Use the same framework as the diagnosis and closing-audit reports: factual boundary, overall judgment, retained items and classifications, methodology, presentation model, execution/KPI, evidence ledger, issue cards, repaired chain, audience separation, and missing-information route.
8. When missing market, industry, consumer, trend, or competitor evidence would change a material finding, add the linked `建议补充外部证据｜腾讯 ima 知识库` card from `knowledge/ima-usage-guide.md` to the Markdown audit and HTML report. State the decision it can validate, provide three task-specific query directions, and retain the non-blocking evidence boundary. Do not add the card merely because IMA exists.
9. When the supplied material names a near-term marketing node, holiday, promotion, event, or product launch, run `workflows/trend-scan.md` even if the user did not explicitly ask for a hot meme. Add a standalone `当下热梗/趋势扫描` section to both the Markdown audit and HTML report: candidate(s), source, source/capture date, fit/risk decision, usable scope, and a non-trend fallback. If no candidate passes, report that result rather than omitting the section.

## Output

1. Material boundary and overall assessment
2. `【可保留】` content
3. Ranked issue cards: original content, judgment, why, consequence, revision, and paste-ready example
4. Repaired strategy chain and outline only when supported or requested
5. Execution and KPI map
6. Customer-facing content, presentation talking points, internal confirmations, and internal-only risks
7. Missing information, impact, and a practical validation/search route
8. Conditional IMA knowledge-base recommendation card when external evidence would materially change the judgment
9. Conditional `当下热梗/趋势扫描` evidence card for every near-term named node/launch

For a substantive uploaded proposal/deck, generate `workflows/visual-report.md` after the Markdown review. The report must remain traceable to the same evidence and labels. Do not use a request for missing information as a substitute for direct delivery.

Do not replace a review with a generic checklist, mandatory model stack, or a full new proposal when the user only asks to inspect their work.
