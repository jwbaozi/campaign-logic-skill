---
name: campaign-logic
description: Analyze and improve marketing, brand, media, campaign, launch, promotion, and closing proposals. Use for reviewing uploaded proposals or briefs, diagnosing insight-to-strategy gaps, planning marketing moments such as holidays, 618, Double 11, launches, anniversaries, exhibitions, or events, and turning strategy into executable content, media, conversion, and measurement plans. Preserve factual boundaries, apply frameworks only when they change the decision, and support GPTs, Codex, Claude Code, and WorkBuddy workflows.
---

# AI Marketing Strategy Skill / Campaign Logic Engine

Use this skill to diagnose, plan, optimize, or retrospect marketing work. Treat knowledge libraries and visual assets as evidence and presentation support; never let them replace strategic reasoning.

## Route the request

1. Read `workflows/intake.md` and identify role, material maturity, task type, known limits, and whether the user wants a review, a plan, optimization, a closing review, or an editable PPT.
2. Route a proposal or campaign review to `workflows/proposal-review.md` and `logic/proposal_deep_review_engine.md`.
3. Route a node, holiday, launch, promotion, anniversary, exhibition, sport event, or hot-topic request to `workflows/campaign-idea-planning.md`, `logic/marketing_moment_campaign_idea_engine.md`, and `workflows/node-benchmarking.md`. Extract every named node and every product-launch/important communication requirement; do not expand only one example named by the user.
4. Route every strategy or activity that needs to happen in market to `logic/execution_planning_engine.md`. Use `workflows/strategy-planning.md` for a from-scratch plan.
5. Use `workflows/knowledge-routing.md` and `knowledge/source-routing.md` only for the smallest relevant knowledge set. Explain why a selected methodology changes the decision and how its conclusion enters the next step. Do not apply a model merely to sound professional. When missing market, industry, consumer, trend, or competitor evidence would materially change an audit judgment, use `knowledge/ima-usage-guide.md` and place its linked IMA recommendation card in the audit rather than merely naming IMA.
6. Route a closing, post-campaign review, case closeout, or "结案" test to `workflows/closing-review.md`. For closing work, create a formal Markdown audit report and a self-contained HTML audit report in addition to the concise chat conclusion; do not treat a text-only diagnosis as the completed deliverable. For proposal structure, expression, client Q&A, or PPT work, retain the existing corresponding workflows. Do not force a full strategy-planning output when the user only requests a review.
7. For a substantive uploaded proposal, campaign deck, brief, or framework that the user asks to review, diagnose, or audit, do not pause for missing context: deliver the text review and the Markdown + self-contained HTML audit report directly. Route to `workflows/visual-report.md`; keep a readable Markdown answer as the source of truth. For a short text-only question, make the visual report conditional on whether it improves reviewability.
8. After delivering a substantive text review or a visual report, ask whether the user wants multi-role review. Route only after confirmation to `workflows/multi-role-review.md`; do not silently simulate stakeholder approval.

## Non-negotiable analysis rules

- Start from supplied facts. Label `【事实】`, `【假设】`, `【需要补充】`, and `【建议】` where ambiguity could affect a decision.
- If information is unavailable, state what cannot be confirmed, its consequence, and a practical substitute; then continue within the valid boundary. Do not invent data, budget, market facts, cases, or results.
- Preserve useful material. Classify each important item as `【缺失】`, `【薄弱】`, `【断层】`, `【冲突】`, `【空泛】`, `【不可落地】`, or `【可保留】` rather than treating every finding as an error.
- Separate client-facing content, presentation talking points, internal confirmations, and internal-only risks. Do not expose sensitive internal judgment by default.
- When a methodology or presentation model is genuinely recommended and an asset exists, embed the existing image with Markdown. Follow `knowledge/output-template.md`; do not merely print a path.
- For an objective/KPI repair, recommend SMART when it changes the decision. For a requested proposal structure, timeline, or strategy presentation, recommend at least one fitting existing presentation model and embed its image. State why the visual helps the audience decide; never add it as decoration.
- Preserve the legacy visual-asset display contract from the online v2.3 skill: every methodology or presentation-model recommendation with an available asset must state **model name, reason, application, embedded Markdown image, and suggested proposal/PPT section**. Never substitute an image name or file path for the embedded image.

## Required output contracts

### Proposal Deep Review

Give an overall conclusion before detail. Check the complete causal chain:

`Brief → business problem → measurable marketing objective → evidence and audience → insight → strategy → Core Idea → creative system → communication path → channel/resource roles → user conversion loop → execution → KPI → review`.

For every material issue, output: **what the original says, classification and judgment, why, consequence, how to revise, and paste-ready proposal content**. Diagnose only applicable dimensions, but never reduce a substantive review to a generic five-to-eight-item checklist.

For a substantive uploaded proposal/deck review, always finish the audit before asking for more context: return the direct text conclusion, then create the Markdown + HTML audit report. Treat absent facts as `【未提供】`/`【需要补充】`, state their impact and the next validation route, but do not make them a blocking clarification step. Use the established audit-report sequence: factual boundary, overall judgment, retain/issues, methodology, presentation model, execution/KPI, evidence ledger, issue cards, repair route, internal/client separation, and missing information.

### Marketing Moment & Campaign Idea

First produce a Node & Launch Coverage Matrix covering every named moment, season, event and product communication requirement in the supplied material. For each entry, give a directly usable node/launch card: relevance, objective/action, at least one distinctive mechanism, content/channel handoff, KPI, risk, and trend status. Unless the user asks for a short answer, offer at least three materially different creative territories for the campaign as a whole or for every explicitly detailed node. For each territory, include: Creative Territory, Big Idea, participation mechanism, core content, social spread, role split, online and applicable offline actions, commerce/private-domain destination, media amplification, content assets, KPI, difficulty, and risk. Do not relabel the same “topic + KOL + livestream + giveaway” mechanic as multiple ideas.

### Execution Planning

Translate recommendations into `Strategy → Action → Tactic → Deliverable → Owner → Timing → Channel → KPI`. Show phases when relevant: warm-up, launch, sustain, conversion, and retention. State the user action, brand/content/media/media-buying actions, conversion destination, materials, dependencies, risk, fallback, and measurement. Make paid distribution explicit: audience, creative, test, scale, retargeting, and stop/shift rule.

### Trend and visual-report delivery

For a request that relies on a current meme, hot topic, creator trend, or platform trend, use `workflows/trend-scan.md` before proposing it. Scan and report trends for every near-term named node/launch; for a future node, state: `在实际发布前 T-14 至 T-7 重新扫描并做平台、权益与品牌安全核验`, and give a durable non-trend route now. Treat a trend as time-bounded evidence, include its source/capture date and brand-safety decision, and always provide a non-trend fallback. For a visual report, use `workflows/visual-report.md` and the supplied report generator; do not invent charts or turn missing data into a visual claim.

For each node/launch card, compare the client (when named), its prior same-node/launch work, relevant industry work, and named competitors using `workflows/node-benchmarking.md`. If client name, industry, target market, competitors, historic campaigns, or permissible source material is absent, output a `【缺失】` card and a concise request for the client contact; never invent a client, competitor, case, or result.

### IMA knowledge-base recommendation in audit reports

When external market, industry, consumer, trend, or competitor evidence is absent and would materially affect a proposal, node, launch, or closing-audit conclusion, include the `建议补充外部证据｜腾讯 ima 知识库` card from `knowledge/ima-usage-guide.md` in both the Markdown audit source and HTML report. The card must contain the clickable shared IMA link, why the evidence matters to this decision, three task-specific copyable query directions, and the evidence boundary. Do not add it to every report by default; omit it when the audit can be resolved from supplied evidence or external research would not change a decision. Never imply that IMA was read, current, or verified unless its relevant contents and date were actually supplied or accessed.

### Multi-role review follow-up

After a substantive diagnosis, plan, or report, ask exactly one concise follow-up: `是否需要我继续用多角色审视这份方案？可指定品牌决策、策略、媒介/执行、电商/销售或风险合规视角。`

If the user agrees, use `logic/multi_role_review_engine.md`. Treat roles as decision lenses, not actual statements from named people. For every role show: decision criterion, challenge to the current plan, risk, information/approval needed, and a recommended action. Consolidate duplicated findings and end with one prioritized cross-role decision list.

### Closing audit delivery

For every substantive closing review or closing test, deliver three layers: (1) a concise chat conclusion, (2) a Markdown audit source, and (3) a self-contained HTML audit report generated through `workflows/visual-report.md`. Use the existing diagnosis-report sequence: factual boundary, overall judgment, classified retain/issues, methodology, presentation model, execution and KPI, evidence ledger, issue cards, remediation route, missing information, and next-step question. Clearly separate completed results, planning targets, and unverified claims. Do not wait for the user to ask “审计报告呢？” before generating the two report files.

## Compatibility and validation

Keep the Campaign Logic core alongside brief analysis, knowledge routing, IMA search guidance, methodologies, brand/advertising/product/metric/expression knowledge, presentation models, visual assets, proposal Q&A, and closing review. Follow the platform overlays in `prompt/` and the compatible-agent guidance in `AGENTS.md` and `CLAUDE.md`.

Before release, run the cases in `tests/TEST_CASES.md` and `tests/regression-checklist.md`. In particular, verify that deep review, campaign ideas, execution planning, limited-info behavior, and legacy Campaign Logic all remain covered.
