# GitHub更新说明

# GitHub 更新说明｜v3.0.0

本次发布保留 Campaign Logic 审核能力，并完成多轮方案、节点、趋势、多角色、结案与 51 页 PPT 审核测试。

主要升级：

1. 已上传的实质性方案/PPT 可直接输出文字审核、Markdown 审核源稿和自包含 HTML 审核报告。
2. 结案/复盘不再停留于文字结论，必须生成正式审计报告。
3. 覆盖所有给定营销节点与上新需求，并补充趋势时效、品牌安全和非热梗备选机制。
4. 支持按客户历史、行业、竞品进行同节点对照；资料不足时明确标注缺失而不虚构案例。
5. README 中英文补充测试说明、能力说明和 Mermaid 应用流程图源码。
6. 保留腾讯 ima 知识库链接、使用边界与不可访问时的非阻塞回退规则。

发布目录：Skill 根目录。不要提交客户原始材料或本地生成的客户审核/审计报告。

## v3.0.0 必更文件清单

| 目录/文件 | 是否更新 | 更新内容 |
| --- | --- | --- |
| `SKILL.md` | 必更 | 主路由、直接审核、结案审计、节点覆盖、趋势扫描、多角色审视与 IMA 兼容规则。 |
| `manifest.json`、`VERSION`、`CHANGELOG.md` | 必更 | 版本统一为 `3.0.0`，记录多轮测试后的能力升级。 |
| `README.md`、`README_CN.md` | 必更 | 中英文能力说明、测试说明、HTML 审核报告能力、Mermaid 应用流程图和 IMA 链接。 |
| `workflows/` | 必更 | 审核、结案、趋势、可视化报告、多角色、节点/竞品对照和直接交付工作流。 |
| `logic/` | 必更 | 深度方案审核、节点创意、执行规划、多角色引擎，以及原 Campaign Logic 的兼容优化。 |
| `knowledge/` | 必更 | 教师节/上新/春节/圣诞玩法、IMA 使用说明、输出模板与知识路由。 |
| `scripts/generate_visual_report.py` | 新增必传 | 将 Markdown 事实源稿生成自包含 HTML 审核/审计报告。 |
| `assets/` | 保持完整 | 方法论、策略呈现和 README 图像资产；本次不新增图片，但不可遗漏。 |
| `tests/` | 必更 | 回归校验脚本、测试 12—24、直接 PPT 审核测试和报告示例夹具。 |
| `.gitignore` | 必更 | 忽略 Python 缓存、本地临时渲染目录及客户审核/审计报告。 |
| `deployment/GITHUB_UPDATE_GUIDE.md`、`GITHUB_UPLOAD_CHECKLIST.md` | 必更 | 发布步骤、公开范围和 v3.0.0 Release 检查项。 |

## 不应上传的本地交付物

- 客户原始 Brief、PPT、PDF、数据导出和含个人/业务敏感信息的附件
- 以 `审核报告`、`审计报告` 命名的客户交付文件
- `ppt-audit-temp/`、`__pycache__/`、日志和私有运行规则

## 发布前验证

```powershell
python -X utf8 tests/validate_skill_regression.py
python -X utf8 C:\Users\jw\.codex\skills\.system\skill-creator\scripts\quick_validate.py .
```
