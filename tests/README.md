# Tests Framework

## Purpose

用于验证 AI Marketing Strategy Skill v3.0 是否按照设计运行。

测试重点：

-   是否识别正确任务类型
-   是否调用正确知识模块
-   是否保持原有方案审核能力
-   是否输出符合营销策划要求的结果
-   对实质性方案/PPT 审核是否不因信息缺失而阻塞，并直接交付文字与正式审核报告

## Static regression check

Run `python -X utf8 tests/validate_skill_regression.py` from the skill root to verify the v3.0 routing, audit-report contracts, IMA retention, README flow-diagram source, manifest version, and required cases. Run the prompt scenarios in `TEST_CASES.md` in the target agent host for behavioral regression.
