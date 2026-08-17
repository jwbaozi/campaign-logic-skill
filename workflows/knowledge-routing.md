# Knowledge Routing Workflow v2.1

## Purpose

根据用户任务类型，自动判断需要调用的知识模块。

Knowledge Routing 的目标：

用户需求

↓

识别问题类型

↓

匹配知识模块

↓

组合调用相关知识

↓

支持营销策略输出

---

# Routing Principles

## 基本规则

不要根据关键词直接推荐模型。

必须先判断：

1. 用户想解决什么问题？
2. 当前处于哪个营销阶段？
3. 需要什么类型的知识支持？

---

# Task Based Routing

## 1. Market Understanding（市场理解）

适用：

- 行业趋势分析
- 市场机会判断
- 竞争环境分析
- 用户研究

调用：

- IMA Industry Knowledge Base
- Strategy Methodology Library


推荐方法：

- PEST
- 3C
- SWOT


---

## 2. Strategy Planning（策略制定）

适用：

- 制定营销策略
- 明确传播方向
- 设计增长路径

调用：

- Strategy Methodology Library
- Brand Theory Library
- Product Selling Points Library


推荐方法：

- STP
- SWOT
- SCQA
- 4P
- HBG
- HOOK


---

## 3. Consumer Journey（消费者路径）

适用：

- 用户决策分析
- 转化路径设计
- 内容传播规划

调用：

- Strategy Methodology Library
- Presentation Model Library


推荐模型：

- AISAS
- AIPL


---

## 4. Brand Strategy（品牌策略）

适用：

- 品牌定位
- 品牌资产建设
- 长期品牌规划

调用：

- Brand Theory Library
- Strategy Methodology Library
- Presentation Model Library


推荐模型：

- 品牌定位模型
- 品牌生命周期模型
- AIPL


---

## 5. Advertising & Media（广告投放）

适用：

- 投放策略
- 媒体规划
- 效果分析

调用：

- Advertising Knowledge Library
- Media Metrics Library


关注：

- 曝光指标
- 互动指标
- 转化指标
- ROI
- CPA
- CTR


---

## 6. Product Value（产品卖点）

适用：

- 产品价值提炼
- 卖点包装
- 用户利益表达

调用：

- Product Selling Points Library
- Marketing Expression Library


分析：

- 产品优势
- 用户利益
- 差异化价值


---

## 7. Proposal Presentation（方案呈现）

适用：

- PPT结构设计
- 模型选择
- 方案视觉化


调用：

- Presentation Model Library
- Marketing Expression Library


必须输出：

1. 推荐模型
2. 使用原因
3. 解决的问题
4. PPT章节位置
5. 参考图片（如存在）


---

# Multi Knowledge Routing

部分任务需要组合调用多个知识模块。

---

## New Product Launch

调用：

- IMA Industry Knowledge Base
- Strategy Methodology Library
- Product Selling Points Library
- Presentation Model Library
- Marketing Expression Library

同时调用 `logic/execution_planning_engine.md`，输出公域、商域和私域的预热→引爆→转化→沉淀链路；明确开屏、信息流、直播、品牌号、达人、用户内容和电商跳转等环节仅在适用时使用及其承接。


---

## Brand Campaign Planning

调用：

- Brand Theory Library
- Strategy Methodology Library
- Presentation Model Library
- Marketing Expression Library

若为节点、节日、大促、周年、赛事、展会或热点，优先调用 `logic/marketing_moment_campaign_idea_engine.md`，先判断相关性，再给差异化创意方向与执行链。


---

## Campaign Closing Review

调用：

- Advertising Knowledge Library
- Media Metrics Library
- Marketing Expression Library


注意：

区分：

Campaign Result

与：

Business Result


---

## Marketing Case Analysis

调用：

- Marketing Cases
- Advertising Knowledge Library
- Media Metrics Library
- Strategy Methodology Library


输出：

- 为什么有效
- 可复制经验
- 不可复制因素


---

# IMA Knowledge Base Routing

当缺少市场、行业、用户、竞品信息时：

调用：

Tencent ima Knowledge Base

如果无法访问：

不要停止分析。

应输出：

## Recommended Search Topics

并提供：

- 搜索主题
- 关键词组合
- 推荐查询方向


---

# Routing Restrictions

禁止：

- 为了显得专业堆叠多个模型
- 没有分析问题直接推荐框架
- 用单一知识模块解决所有问题

必须：

先诊断问题，再调用知识。
