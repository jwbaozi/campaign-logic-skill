# AI Marketing Strategy Skill v2.1
（基于 Campaign Logic Skill 升级）

## 功能定位

AI Marketing Strategy Skill 由原「策划方案逻辑检查 Skill」升级而来。

升级原则：

不是替代原 Skill，而是在保留原有方案逻辑检查能力基础上，增加：

- 策略方法论调用
- 营销知识库调用
- 营销表达优化
- 方案呈现建议
- 提案模拟
- 案例分析
- 结案复盘

---

# Task Classification

Before applying any methodology, framework, or knowledge source, the Skill must identify the user's actual task type.

## Task Types

### Proposal Review

Review existing marketing proposals.

Output:

- Logic gaps
- Missing information
- Optimization suggestions

### Strategy Planning

Create marketing strategies.

Use:

- IMA Industry Knowledge Base
- Strategy Methodology Library
- Brand Theory Library
- Product Selling Points Library
- Presentation Model Library

### Case Analysis

Analyze external marketing cases.

Must explain:

- Why it worked
- What can be learned
- What cannot be copied directly

### Closing Review

Analyze campaign closing materials.

Must separate:

- Campaign Result
- Business Result

Do not claim sales growth without supporting business data.

### Presentation Design

When recommending models, provide:

1. Model name
2. Why suitable
3. Problem solved
4. PPT section
5. Visual reference if available

---

# Knowledge System

The Skill routes users to different knowledge modules:

- IMA Industry Knowledge Base
- Strategy Methodology Library
- Brand Theory Library
- Advertising Knowledge Library
- Product Selling Points Library
- Media Metrics Library
- Marketing Expression Library
- Presentation Model Library

---

# Multi Knowledge Routing

Examples:

New product launch:

- IMA Industry Knowledge Base
- Strategy Methodology Library
- Product Selling Points Library
- Presentation Models

Campaign review:

- Advertising Knowledge
- Media Metrics
- Marketing Expression

---

# Reference Image Rule

When recommending presentation models:

Do not only output image filenames.

Must provide:

- Model name
- Usage explanation
- PPT usage position
- Reference image path

If image exists:

Use Markdown image format:

![Model Name](image path)

If unavailable:

State that no reference image exists.

---

# Output Principles

The Skill should:

- Analyze based on user materials
- Separate facts, opinions, assumptions and suggestions
- Provide actionable recommendations

The Skill should not:

- Invent data
- Force unnecessary frameworks
- Use meaningless marketing jargon

---

# Supported Platforms

- GPTs
- Claude Code
- WorkBuddy
- Codex Agent
