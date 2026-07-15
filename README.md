# Campaign Logic Skill

[English](README.md) | [简体中文](README.zh-CN.md)

A cross-platform skill for reviewing, restructuring, and improving marketing campaign proposals.

It supports rough ideas, outlines, TXT files, Word documents, PDFs, PowerPoint files, screenshots, incomplete proposals, complete proposals, and campaign closing reports.

## What It Does

Campaign Logic Skill helps users:

- identify the maturity of proposal materials
- detect broken or missing logic
- extract the most important issues to revise
- build a clear core strategy line
- restructure proposal flow
- distinguish client-facing content from internal analysis
- generate an editable PowerPoint blueprint
- continue analysis even when some data is unavailable

## Core Workflow

Material review  
→ Role identification  
→ Proposal maturity assessment  
→ Proposal type recognition  
→ Overall judgment  
→ Logic diagnosis  
→ Core strategy extraction  
→ Proposal restructuring  
→ Editable PowerPoint blueprint

## Supported Proposal Types

- Campaign proposals
- General proposal frameworks
- Individual campaign proposals
- Campaign closing reports
- Mixed-format proposal materials

## Editable PowerPoint Blueprint

The skill can generate an editable PowerPoint draft based on the proposal review.

The output may include:

- material assessment
- the most important logic issues
- a one-sentence core strategy
- a step-by-step strategy line
- a restructured proposal outline
- page-by-page editing boards
- missing information placeholders
- internal review notes

The PowerPoint output is designed as an editable logic blueprint, not as a final visual design.

## Supported Agent Environments

This repository can be used with tools that support project instructions, Markdown-based skills, system prompts, or repository-level rules, including:

- OpenAI Codex
- Codex Cloud
- Claude Code
- Other similar Agent tools

## Codex Setup

1. Clone or download this repository.
2. Place the repository files in your project root.
3. Make sure `AGENTS.md` and `SKILL.md` are available.
4. Ask Codex to read the relevant files before reviewing your proposal.

Example prompt:

```text
Please read AGENTS.md and SKILL.md first.
Then select the appropriate workflow from the workflows folder
and review the marketing proposal I provide.
