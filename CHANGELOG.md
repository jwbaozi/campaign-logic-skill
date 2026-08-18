# Changelog

All notable changes to this project will be documented in this file.

------------------------------------------------------------------------

# v3.1.0

## Added

- Added a conditional `建议补充外部证据｜腾讯 ima 知识库` card to substantive proposal, node/launch, and closing audit reports when missing external market, industry, consumer, trend, or competitor evidence would materially change a conclusion.
- Added the clickable shared Tencent ima knowledge-base link and three task-specific, copyable query directions to the audit card.

## Improved

- Preserved the IMA card in both the Markdown audit source and generated HTML audit report.
- Clarified that IMA is not inserted mechanically, must state the decision it can validate, and must never be represented as read, current, or verified unless the relevant material and date were actually supplied or accessed.
- Retained the non-blocking fallback: if ima requires login, is inaccessible, or no result is supplied, continue the audit and record the evidence gap and validation route.
- Restored a standalone `当下热梗/趋势扫描` section for every substantive audit or plan with a near-term named node or launch, even when the user does not explicitly ask for a hot meme. The report must retain candidate(s), source/capture date, fit and risk judgment, usable scope, and a non-trend fallback; an empty scan is reported rather than silently omitted.

## Validated

- Added regression checks for the linked IMA audit card across Skill routing, proposal review, visual-report, knowledge-routing, and IMA usage guidance.
- Tested the updated audit with a 2026 H2 brief that includes product launch, Teacher's Day, Christmas, Spring Festival, competitor comparison, and missing external evidence.

------------------------------------------------------------------------

# v3.0.0

## Validated

- Iterated through multiple practical tests covering proposal review, campaign-moment planning, trend/risk handling, multi-role review, closing audit, and a 51-slide social-media proposal audit.

## Added

- Added mandatory direct-audit delivery for substantive uploaded proposals and decks: concise text conclusion, Markdown audit source, and self-contained HTML audit report.
- Added a shared README application-flow diagram source and diagram-ready capability copy in English and Chinese.

## Improved

- Removed missing context as a blocking step for substantive deck audits; the Skill now labels factual gaps, explains their impact, and completes the strongest evidence-bounded review directly.
- Strengthened closing-audit delivery so it cannot stop at a text-only conclusion.
- Retained and clarified the Tencent ima knowledge-base link, evidence boundary, access limitations, and non-blocking fallback workflow.

------------------------------------------------------------------------

# v2.8.0

## Added

- Added node and launch benchmarking against client history, industry peers, competitors, and attributable public references.
- Added a structured `【缺失】` request for client/industry/competitor evidence when comparison is not possible.

## Improved

- Standardized future-node trend guidance as: “在实际发布前 T-14 至 T-7 重新扫描并做平台、权益与品牌安全核验”.

------------------------------------------------------------------------

# v2.7.0

## Improved

- Added mandatory extraction and coverage of every named marketing node, product launch, and important communication requirement in supplied materials.
- Added direct playbooks for product launch, Spring Festival, and Christmas alongside the Teacher's Day playbook.
- Added per-node trend status and future-node T-14 to T-7 scan windows so a current meme is never reused as a future promise.

------------------------------------------------------------------------

# v2.6.0

## Added

- Added an on-demand Multi-role Review Engine covering brand/business, strategy, media/execution, sales/e-commerce/CRM, and risk/compliance lenses.
- Added a post-delivery question for both text feedback and HTML reports, so multi-role review runs only with user confirmation.

## Improved

- Added a multi-role review call-to-action to generated visual reports and a single-source regeneration rule after role review.

------------------------------------------------------------------------

# v2.5.0

## Added

- Added Teacher's Day playbook with three differentiated campaign territories, phase actions, sensitivity guardrails, and fallback paths.
- Added current-trend scan workflow that requires attributable, time-stamped evidence, brand-safety checks, and a non-trend alternative.
- Added optional visual-report workflow and a dependency-free Markdown-to-HTML report generator.

## Improved

- Made visual methodology and presentation-model recommendations mandatory when a goal/KPI repair or requested proposal structure needs them.
- Added explicit SMART, strategy-framework, and timeline visual-routing rules so existing image assets appear in applicable outputs.

------------------------------------------------------------------------

# v2.4.0

## Added

- Added Proposal Deep Review Engine with evidence-to-strategy diagnosis and paste-ready repair examples.
- Added Marketing Moment & Campaign Idea Engine for differentiated holiday, promotion, launch, and event concepts.
- Added Execution Planning Engine with phase, owner, handoff, media, conversion, KPI, risk, and review requirements.
- Added campaign-idea planning workflow and regression cases for the three engines.

## Improved

- Restored the original Campaign Logic material-boundary, causal-chain, issue-classification, and client/internal separation rules in the primary skill entry point.
- Made methodology selection conditional on a decision it can change instead of a presentation requirement.
- Updated campaign/proposal/strategy routing so knowledge and visual assets support reasoning rather than replace it.

------------------------------------------------------------------------

# v2.3.0

## Added

-   Added Visual Assets Knowledge module
-   Added methodology visual reference mapping
-   Added presentation model visual reference mapping
-   Added asset-index for visual resource management
-   Added output-template for standardized response format

------------------------------------------------------------------------

## Improved

-   Enhanced Strategy Methodology recommendation workflow
-   Enhanced Presentation Model recommendation workflow
-   Added visual reference requirements when recommending frameworks
-   Improved proposal review with methodology and presentation checks
-   Improved case review with reusable framework extraction
-   Improved closing review with methodology and presentation
    retrospective

------------------------------------------------------------------------

## Updated

-   Updated SKILL.md execution rules
-   Updated source-routing.md knowledge routing
-   Updated README.md
-   Updated README_CN.md

------------------------------------------------------------------------

# v2.2.0

## Added

-   Added visual asset library structure
-   Added methodology image assets
-   Added presentation model image assets

## Improved

-   Improved marketing strategy workflow
-   Improved knowledge module organization
