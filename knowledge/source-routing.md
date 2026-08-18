# Source Routing v2.3

## Purpose

用于帮助 AI Marketing Strategy Skill
根据用户需求判断需要调用的知识模块，并建立知识模块、视觉资产和输出模板之间的调用关系。

------------------------------------------------------------------------

# Routing Logic

用户输入

↓

识别任务类型

↓

调用对应知识模块

↓

如涉及视觉参考，调用 Visual Assets Knowledge

↓

按照 Output Template 规范输出

------------------------------------------------------------------------

# Knowledge Routing Rules

## Engine Routing

Before selecting a knowledge module, route the work type:

- Uploaded proposal, campaign deck, or brief review: `logic/proposal_deep_review_engine.md` plus `logic/campaign_logic_engine.md`.
- Holiday, node, promotion, launch, anniversary, event, or hot topic: `logic/marketing_moment_campaign_idea_engine.md` plus `knowledge/09-marketing-moments/node-and-launch-playbook.md`; extract and cover every named item.
- Any strategy or idea that must happen in market: `logic/execution_planning_engine.md`.
- Current meme, hot-topic, creator-format, or platform-trend request: `workflows/trend-scan.md` before a trend is proposed.
- Visual/shareable/executive report request: `workflows/visual-report.md` after the Markdown analysis is complete.
- User asks for multi-role/stakeholder review or accepts the post-delivery follow-up: `workflows/multi-role-review.md` and `logic/multi_role_review_engine.md`.

Engines establish the reasoning and output contract. Knowledge sources supply only the evidence or method needed for a stated decision; do not replace the engine with a list of references or frameworks.

## Strategy Methodology

Location:

`knowledge/01-strategy-methodology/`

Use when:

-   用户需要制定营销策略
-   用户需要选择分析框架
-   用户需要市场、用户、竞争分析

Related Visual Assets:

`assets/methodology/`

------------------------------------------------------------------------

## Presentation Models

Location:

`knowledge/03-presentation-models/`

Use when:

-   用户需要方案结构建议
-   用户需要 PPT 呈现方式
-   用户需要策略视觉化表达

Related Visual Assets:

`assets/presentation/`

For requested proposal structures, annual/node calendars, or strategy presentation, select and embed at least one matching presentation asset. For objective/KPI repair, select and embed SMART when it changes the decision. See `knowledge/output-template.md`.

------------------------------------------------------------------------

## Visual Assets

Location:

`knowledge/08-visual-assets/`

Purpose:

提供：

-   方法论参考图
-   呈现模型参考图
-   方案结构参考图

Trigger:

当用户请求：

-   推荐营销方法论
-   推荐策略模型
-   推荐 PPT 呈现方式
-   方案结构设计

调用 Visual Assets Knowledge。

------------------------------------------------------------------------

# Output Template

Location:

`knowledge/output-template.md`

Use when:

-   Strategy recommendation
-   Presentation recommendation
-   Proposal review
-   Case review
-   Closing review

Purpose:

确保输出结构统一，并在存在视觉资产时提供图片参考。

------------------------------------------------------------------------

# Asset Mapping

## Methodology

Path:

`assets/methodology/`

Examples:

-   SWOT.png
-   AISAS.png
-   AIPL.png
-   SCQA.png

------------------------------------------------------------------------

## Presentation

Path:

`assets/presentation/`

Examples:

-   new-product-launch-marketing-strategy.png
-   content-matrix-and-content-ecosystem.png
-   annual-marketing-timeline.png

------------------------------------------------------------------------

# Output Rule

当推荐方法论或呈现模型时：

必须输出：

1.  推荐模型
2.  使用原因
3.  应用场景
4.  Visual Reference
5.  建议方案章节

如果不存在对应图片，再说明暂无匹配视觉资产。
