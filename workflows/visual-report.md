# Visual Report Workflow

Use when the final result has multiple material findings, requires executive review, needs a shareable decision record, or the user explicitly asks for a visual report. Do not make a report mandatory for a short answer or when it would only decorate unverified claims. **Exceptions:** a substantive closing review, post-campaign review, closing test, or substantive uploaded proposal/deck audit always requires the formal Markdown + HTML audit report specified in `workflows/closing-review.md` or `workflows/proposal-review.md`; do not wait for the user to ask for it.

## Delivery decision

Recommend a visual report when it will make one or more of these easier to review: issue priority, causal chain, visual reference, phase ownership, KPI map, decisions needed, and factual boundary. Keep the Markdown diagnosis as the canonical content; the report is a presentation layer, not a new analysis.

## Required report content

1. Title, source material, generated date, and factual-boundary note
2. Executive conclusion and priority issues
3. Causal-chain or strategy-chain view
4. Issue cards using the same classifications and evidence as the Markdown review
5. Methodology/presentation recommendation with existing image references when applicable
6. Phased execution and KPI table when applicable
7. Decisions required, missing information, risks, and next steps
8. When external market, industry, consumer, trend, or competitor evidence would materially change a conclusion, the linked `建议补充外部证据｜腾讯 ima 知识库` card from `knowledge/ima-usage-guide.md`. Keep its clickable link, decision purpose, task-specific queries, and evidence boundary in the Markdown source so the HTML report preserves the same card.
9. For every substantive report containing a near-term named node/launch, a standalone `当下热梗/趋势扫描` section from `workflows/trend-scan.md`: candidate(s), source and capture date, fit/risk decision, permitted use, and non-trend fallback. Keep the section even when no candidate passes; never silently remove it because a user did not explicitly ask for a hot meme.

After delivering either the Markdown source or the HTML report, ask: `是否需要我继续用多角色审视这份方案？可指定品牌决策、策略、媒介/执行、电商/销售或风险合规视角。` If the user agrees, follow `workflows/multi-role-review.md`; then regenerate the report from the expanded Markdown source if a report is still wanted.

## Generator

After preparing the Markdown review, run:

```powershell
python -X utf8 scripts/generate_visual_report.py review.md --output visual-review-report.html --title "项目名称｜营销方案诊断"
```

The generator creates one self-contained HTML file and renders Markdown headings, bullets, tables, blockquotes, and local Markdown images. Place the report in the skill root or use paths that keep `assets/` relative to the report; otherwise images will not display. Open the HTML locally and verify that no absent data became a chart or a result claim.
