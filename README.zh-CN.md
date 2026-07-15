![Campaign Logic Skill](assets/readme-hero.png)

[English](README.md) | 简体中文

# Campaign Logic Skill V1.1

一套平台无关的营销策划方案逻辑检查配置包。

适用于：

- OpenAI Codex / Codex Cloud
- Claude Code
- WorkBuddy 等国内 Agent 工具
- 支持 `SKILL.md`、`AGENTS.md`、系统提示词或项目规则文件的 Agent 工具
- 其他可上传知识文件或项目说明文件的 Agent 软件

## 快速开始

### Codex / Codex Cloud

将整个文件夹放入项目根目录。

优先读取：

1. `AGENTS.md`
2. `SKILL.md`
3. `config/private-runtime-rules.md`
4. 对应 `workflows/` 文件

### Claude Code

将整个文件夹放入项目目录。

优先读取：

1. `CLAUDE.md`
2. `SKILL.md`
3. `config/private-runtime-rules.md`
4. 对应工作流

## WorkBuddy 及其他国内 Agent

如果平台支持上传知识文件、项目说明文件或系统提示词：

1. 上传 `SKILL.md`
2. 上传与当前任务相关的 `workflows/` 文件
3. 将 `AGENTS.md` 作为项目规则或补充说明
4. 上传需要分析的策划方案
5. 提示 Agent 先读取规则，再开始分析

示例提示词：

请先读取 `SKILL.md` 和 `AGENTS.md`，
再根据我上传的材料类型，选择 `workflows/` 中对应的工作流进行分析。

### 其他 Agent

如果支持系统提示词：

- 将 `SKILL.md` 作为主能力说明
- 将 `config/private-runtime-rules.md` 放入私有系统提示或开发者提示
- 将 `workflows/` 作为子工作流
- 将 `knowledge/` 和 `tests/` 作为知识文件

如果只支持上传文件：

- 上传 `SKILL.md`
- 上传所需工作流
- 私有规则只放在自己的 Agent 配置里，不公开分发

## 配套知识库

腾讯 ima：

https://ima.qq.com/wiki/?shareId=749ceceb753eac5742dc93d51c7318da96b63100624e1c45624836cbcd60d279

使用限制：

- 可能需要微信扫码登录
- 境外网络环境可能无法访问
- 第一版不依赖自动连接
- Skill 会生成检索主题和关键词，用户可手动到 ima 搜索

## 文件结构

```text
campaign-logic-skill-v1/
├─ SKILL.md
├─ README.md
├─ AGENTS.md
├─ CLAUDE.md
├─ SYSTEM_PROMPT.md
├─ config/
│  └─ private-runtime-rules.md
├─ workflows/
│  ├─ intake.md
│  ├─ proposal-review.md
│  ├─ closing-review.md
│  └─ restructure.md
├─ knowledge/
│  ├─ ima-usage-guide.md
│  ├─ source-routing.md
│  └─ search-query-template.md
├─ tests/
│  ├─ TEST_CASES.md
│  └─ regression-checklist.md
└─ examples/
   ├─ framework-example.md
   ├─ proposal-example.md
   └─ closing-example.md
```

## 分发建议

对外公开：

- `SKILL.md`
- `README.md`
- `workflows/`
- `knowledge/`
- `examples/`

个人部署保留但不公开：

- `config/private-runtime-rules.md`
- `SYSTEM_PROMPT.md`

## 当前版本状态

- 规则级测试：通过
- 真实案例模拟：通过
- 适合内部试用、小范围使用
- 尚未完成 ima 自动连接


## 可编辑 PPT 输出

V1.1 新增“方案逻辑白板”功能。

当用户要求把诊断结果直接用于修改方案时，Agent 应：

1. 判断材料阶段
2. 找出当前最需要修正的逻辑
3. 提炼一句话总策略
4. 按总策略主线重排内容
5. 生成可编辑 `.pptx`

该 PPT 是逻辑重构底稿，不是最终视觉设计稿。

相关文件：

- `workflows/editable-ppt.md`
- `config/ppt-output-spec.md`
