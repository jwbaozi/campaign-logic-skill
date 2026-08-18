"""Static regression checks for the v2.8 skill routing and output contracts."""

from __future__ import annotations

import json
import sys
from pathlib import Path


def read(root: Path, relative: str) -> str:
    path = root / relative
    if not path.is_file():
        raise AssertionError(f"Missing required file: {relative}")
    return path.read_text(encoding="utf-8")


def require(text: str, phrase: str, source: str) -> None:
    if phrase not in text:
        raise AssertionError(f"Missing required text in {source}: {phrase}")


def main() -> None:
    root = Path(sys.argv[1]).resolve() if len(sys.argv) > 1 else Path(__file__).resolve().parents[1]
    manifest = json.loads(read(root, "manifest.json"))
    if manifest.get("version") != "3.1.0":
        raise AssertionError("manifest.json version must be 3.1.0")

    skill = read(root, "SKILL.md")
    for phrase in (
        "proposal_deep_review_engine.md",
        "marketing_moment_campaign_idea_engine.md",
        "execution_planning_engine.md",
        "workflows/trend-scan.md",
        "workflows/visual-report.md",
        "workflows/multi-role-review.md",
        "logic/multi_role_review_engine.md",
        "workflows/node-benchmarking.md",
        "workflows/closing-review.md",
        "【缺失】",
        "【可保留】",
        "Strategy → Action → Tactic → Deliverable → Owner → Timing → Channel → KPI",
        "do not pause for missing context",
        "Markdown + self-contained HTML audit report",
        "legacy visual-asset display contract",
        "suggested proposal/PPT section",
        "当下热梗/趋势扫描",
        "even if the user did not explicitly ask for a meme",
    ):
        require(skill, phrase, "SKILL.md")

    deep_review = read(root, "logic/proposal_deep_review_engine.md")
    for phrase in ("原方案写了什么", "会造成什么后果", "可直接替换/补进方案的内容示例"):
        require(deep_review, phrase, "logic/proposal_deep_review_engine.md")

    idea = read(root, "logic/marketing_moment_campaign_idea_engine.md")
    for phrase in ("at least three distinct territories", "User participation mechanism", "Media amplification"):
        require(idea, phrase, "logic/marketing_moment_campaign_idea_engine.md")

    execution = read(root, "logic/execution_planning_engine.md")
    for phrase in ("预热 / 引爆 / 持续 / 转化 / 沉淀", "retargeting", "stop/shift condition"):
        require(execution, phrase, "logic/execution_planning_engine.md")

    teacher_day = read(root, "knowledge/09-marketing-moments/teacher-day.md")
    for phrase in ("Recognition", "Utility and experience", "Community contribution"):
        require(teacher_day, phrase, "knowledge/09-marketing-moments/teacher-day.md")

    node_playbook = read(root, "knowledge/09-marketing-moments/node-and-launch-playbook.md")
    for phrase in ("Product Proof Lab", "Spring Festival / Chinese New Year", "Christmas", "未来扫描"):
        require(node_playbook, phrase, "knowledge/09-marketing-moments/node-and-launch-playbook.md")

    trend = read(root, "workflows/trend-scan.md")
    for phrase in ("capture date/time", "brand/product fit", "non-trend creative route", "If no candidate passes"):
        require(trend, phrase, "workflows/trend-scan.md")

    benchmarking = read(root, "workflows/node-benchmarking.md")
    for phrase in ("【缺失】客户/行业/竞品同节点对照资料", "【客户历史】", "【同行业】", "【竞品】", "【公开参考】"):
        require(benchmarking, phrase, "workflows/node-benchmarking.md")

    report = read(root, "workflows/visual-report.md")
    require(report, "generate_visual_report.py", "workflows/visual-report.md")
    require(report, "当下热梗/趋势扫描", "workflows/visual-report.md")
    read(root, "scripts/generate_visual_report.py")

    ima = read(root, "knowledge/ima-usage-guide.md")
    for phrase in ("https://ima.qq.com/wiki/?shareId=", "不阻塞方案审核", "不把未读取的 IMA 内容表述为已验证事实", "建议补充外部证据｜腾讯 ima 知识库", "[打开你的腾讯 ima 共享知识库]", "建议检索："):
        require(ima, phrase, "knowledge/ima-usage-guide.md")

    for source in ("SKILL.md", "workflows/proposal-review.md", "workflows/visual-report.md", "workflows/knowledge-routing.md"):
        require(read(root, source), "建议补充外部证据｜腾讯 ima 知识库", source)

    for readme_name in ("README.md", "README_CN.md"):
        readme = read(root, readme_name)
        for phrase in ("mermaid", "HTML", "ima.qq.com/wiki/?shareId="):
            require(readme, phrase, readme_name)

    claude = read(root, "CLAUDE.md")
    for phrase in ("AI Marketing Strategy Skill v3.0", "Markdown 审核源稿", "自包含 HTML 审计报告", "T-14 至 T-7"):
        require(claude, phrase, "CLAUDE.md")

    closing = read(root, "workflows/closing-review.md")
    for phrase in ("必须", "Markdown 审计报告", "自包含 HTML 审计报告", "Mandatory Closing Audit Report", "证据台账", "多角色审视提问"):
        require(closing, phrase, "workflows/closing-review.md")

    proposal = read(root, "workflows/proposal-review.md")
    for phrase in ("Do not block on missing context", "Markdown audit source", "self-contained HTML audit report", "without waiting for the user to ask for a report", "当下热梗/趋势扫描"):
        require(proposal, phrase, "workflows/proposal-review.md")

    report_fixture = read(root, "tests/fixtures/actual-project-review.md")
    for phrase in ("上新｜产品证据实验室", "路线一｜把被看见还给老师", "圣诞节｜秘密善意接力", "2027 春节｜新年有用仪式", "来源发布日期 / 本次抓取日期", "非热梗备选", "【缺失】客户/行业/竞品同节点对照资料", "在实际发布前 T-14 至 T-7 重新扫描并做平台、权益与品牌安全核验"):
        require(report_fixture, phrase, "tests/fixtures/actual-project-review.md")

    roles = read(root, "logic/multi_role_review_engine.md")
    for phrase in ("决策标准", "会追问什么", "主要风险", "需要确认/批准什么", "建议动作"):
        require(roles, phrase, "logic/multi_role_review_engine.md")

    cases = read(root, "tests/TEST_CASES.md")
    for case in range(12, 25):
        require(cases, f"测试 {case}", "tests/TEST_CASES.md")

    print("Static regression checks passed: v3.1 linked IMA audit card, direct proposal and closing audit reports, IMA/README retention, node benchmarking, all-node coverage, visual routing, trend scan, visual report, multi-role review, and cases 12-24.")


if __name__ == "__main__":
    main()
