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
