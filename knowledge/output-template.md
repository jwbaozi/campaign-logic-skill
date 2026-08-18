# Output Template v2.3

## Visual Reference Requirement

When a methodology or presentation model has a corresponding visual
asset, the assistant MUST display the image.

Do not only provide image names or file paths.

------------------------------------------------------------------------

# Strategy Recommendation Output

## Recommended Methodology

推荐方法论：

------------------------------------------------------------------------

## Why

为什么该方法论适合当前问题：

------------------------------------------------------------------------

## Application

如何应用到营销方案：

------------------------------------------------------------------------

## Visual Reference

必须使用 Markdown 图片格式：

``` markdown
![Methodology Name](assets/methodology/xxx.png)
```

Example:

``` markdown
![AISAS](assets/methodology/AISAS.png)
```

------------------------------------------------------------------------

## Suggested Proposal Section

建议应用章节：

------------------------------------------------------------------------

# Presentation Recommendation Output

## Recommended Presentation Model

推荐呈现模型：

------------------------------------------------------------------------

## Why

为什么适合该方案：

------------------------------------------------------------------------

## Application

如何应用于 PPT：

------------------------------------------------------------------------

## Visual Reference

必须使用 Markdown 图片格式：

``` markdown
![Presentation Model](assets/presentation/xxx.png)
```

------------------------------------------------------------------------

## Suggested Proposal Section

建议应用页面：

------------------------------------------------------------------------

# General Rule

错误方式：

    Visual Reference:
    assets/methodology/AISAS.png

正确方式：

``` markdown
Visual Reference:

![AISAS](assets/methodology/AISAS.png)
```

目标：

用户看到的是图片，而不是图片路径。

------------------------------------------------------------------------

# Deep Review Issue Card

For a material proposal issue, output before any visual recommendation:

1. 原方案写了什么
2. 分类与判断：`【缺失】`、`【薄弱】`、`【断层】`、`【冲突】`、`【空泛】`、`【不可落地】` 或 `【可保留】`
3. 为什么
4. 会造成什么后果
5. 建议怎么改
6. 可直接替换/补进方案的内容示例

Use `【示例假设】` for wording that relies on unverified inputs. Do not use a methodology asset or a presentation asset as a substitute for this diagnosis.

------------------------------------------------------------------------

# Mandatory visual recommendation when applicable

For an objective or KPI that must be defined or repaired, use SMART if it changes the decision and embed:

```markdown
![SMART](assets/methodology/SMART.png)
```

For a requested proposal structure, annual/node calendar, or strategy presentation, recommend the fitting visual model and embed it. Examples:

- `annual-marketing-timeline.png` for a month/node calendar.
- `integrated-marketing-timeline.png` for phased communication and conversion.
- `marketing-strategy-framework.png` for the evidence-to-strategy chain.

For each recommendation write: **what decision it solves, why this model fits, what the audience should see, and where it belongs in the proposal**. Do not embed unrelated pictures merely to satisfy a format requirement.
