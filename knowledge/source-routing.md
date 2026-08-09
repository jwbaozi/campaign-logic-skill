# Source Routing v2.2

## Purpose

用于帮助 AI Marketing Strategy Skill 根据用户需求，
判断需要调用哪些知识模块，并建立知识模块与视觉资产之间的调用关系。

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

整合输出结果

------------------------------------------------------------------------

# Knowledge Routing Rules

## 01 Strategy Methodology

Location:

`knowledge/01-strategy-methodology/`

Use when:

-   用户需要制定营销策略
-   用户需要选择分析框架
-   用户需要策略推导方法
-   用户需要市场、用户、竞争分析

Examples:

-   如何分析市场机会？
-   新品上市应该使用什么策略模型？
-   如何制定传播策略？

Related Visual Assets:

`knowledge/08-visual-assets/`

`assets/methodology/`

------------------------------------------------------------------------

## 02 Brand Theory

Location:

`knowledge/02-brand-theory/`

Use when:

-   用户需要品牌定位
-   用户需要品牌建设逻辑
-   用户需要品牌长期策略

Related Visual Assets:

`knowledge/08-visual-assets/`

------------------------------------------------------------------------

## 03 Presentation Models

Location:

`knowledge/03-presentation-models/`

Use when:

-   用户需要方案结构建议
-   用户需要 PPT 呈现方式
-   用户需要策略视觉化表达

Examples:

-   这一页 PPT 应该怎么呈现？
-   用户旅程应该使用什么模型？
-   策略部分如何视觉化？

Related Visual Assets:

`knowledge/08-visual-assets/`

`assets/presentation/`

------------------------------------------------------------------------

## 04 Advertising Knowledge

Location:

`knowledge/04-advertising-knowledge/`

Use when:

-   用户需要广告行业知识
-   用户需要传播逻辑
-   用户需要广告机制解释

------------------------------------------------------------------------

## 05 Media Metrics

Location:

`knowledge/05-media-metrics/`

Use when:

-   用户需要广告指标解释
-   用户需要效果分析
-   用户需要投放数据分析

------------------------------------------------------------------------

## 06 Product Selling Points

Location:

`knowledge/06-product-selling-points/`

Use when:

-   用户需要产品卖点分析
-   用户需要产品价值提炼

------------------------------------------------------------------------

## 07 Marketing Expression

Location:

`knowledge/07-marketing-expression/`

Use when:

-   用户需要优化营销表达
-   用户需要专业化方案语言
-   用户需要提案措辞优化

------------------------------------------------------------------------

# 08 Visual Assets

Location:

`knowledge/08-visual-assets/`

Purpose:

用于提供：

1.  方法论参考图
2.  呈现模型参考图
3.  方案结构参考图

------------------------------------------------------------------------

# Visual Assets Trigger Conditions

当用户请求：

-   推荐营销方法论
-   推荐策略模型
-   推荐 PPT 呈现方式
-   方案结构设计
-   视觉化表达建议

调用：

`Visual Assets Knowledge`

------------------------------------------------------------------------

# Asset Mapping

## Methodology Assets

Path:

`assets/methodology/`

Used for:

-   SWOT
-   PEST
-   3C
-   AISAS
-   AIPL
-   SMART
-   3W
-   5W2H
-   SCQA
-   HOOK
-   HBG
-   KISS
-   McKinsey 7-Step Method
-   4P
-   Ogilvy Brand Positioning Triangle
-   5A

------------------------------------------------------------------------

## Presentation Assets

Path:

`assets/presentation/`

Used for:

-   新品上市方案
-   年度营销规划
-   内容矩阵
-   媒体投放组合
-   品牌战略呈现
-   社交媒体规划
-   用户旅程
-   营销节奏规划

------------------------------------------------------------------------

# Output Rule

当推荐方法论或呈现模型时：

如果存在对应视觉资产，需要输出：

1.  推荐模型
2.  使用原因
3.  Visual Reference（图片路径）
4.  应用场景

不要只输出文字解释。

------------------------------------------------------------------------

# Priority Rule

视觉资产匹配优先级：

1.  精确匹配模型图片
2.  对应类别图片
3.  总览图片
