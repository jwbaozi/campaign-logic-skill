# AGENTS.md

本项目使用《策划方案逻辑检查 Skill》。

执行任何方案分析前：

1. 读取 `SKILL.md`
2. 读取 `config/private-runtime-rules.md`
3. 根据材料类型读取对应工作流
4. 用户提供多文件时，先建立文件清单和材料关系
5. 先给整体判断，再提出少量关键问题
6. 用户说明资料拿不到后，继续分析并降低确定性
7. 输出时区分客户版、提案补充和内部判断
8. 涉及资料补充时，优先生成可复制的检索关键词

9. 用户要求可编辑 PPT 时，读取 `workflows/editable-ppt.md` 和 `config/ppt-output-spec.md`，生成原生可编辑 `.pptx`。
