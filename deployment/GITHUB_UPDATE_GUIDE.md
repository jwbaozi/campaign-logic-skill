# GitHub Update Guide｜v3.0.0

1. 在原 GitHub 仓库克隆出的工作目录中更新 Skill 根目录文件。
2. 提交 `SKILL.md`、`manifest.json`、`VERSION`、`CHANGELOG.md`、`README.md`、`README_CN.md`、`workflows/`、`logic/`、`knowledge/`、`scripts/`、`assets/`、`tests/` 和 `.gitignore` 的公开内容。
3. 不提交客户原始文件、`ppt-audit-temp/` 或以 `审核报告`/`审计报告` 命名的本地交付物。
4. 运行 `python -X utf8 tests/validate_skill_regression.py` 和 Skill 校验脚本。
5. 推送至原分支或创建 PR；创建 `v3.0.0` Release，并在 GitHub 页面检查中英文 README 的 Mermaid 图与 ima 链接。
