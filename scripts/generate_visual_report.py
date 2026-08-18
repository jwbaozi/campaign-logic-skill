"""Render a skill-produced Markdown review as a portable visual HTML report."""

from __future__ import annotations

import argparse
import html
import re
from datetime import date
from pathlib import Path


IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
INLINE_CODE = re.compile(r"`([^`]+)`")
BOLD = re.compile(r"\*\*([^*]+)\*\*")
URL = re.compile(r"(https?://[^\s<]+)")


def inline(value: str) -> str:
    escaped = html.escape(value)
    escaped = IMAGE.sub(lambda match: f'<figure><img src="{html.escape(match.group(2), quote=True)}" alt="{match.group(1)}"><figcaption>{html.escape(match.group(1))}</figcaption></figure>', escaped)
    escaped = BOLD.sub(r"<strong>\1</strong>", escaped)
    escaped = INLINE_CODE.sub(r"<code>\1</code>", escaped)
    return URL.sub(r'<a href="\1" target="_blank" rel="noreferrer">\1</a>', escaped)


def classification(value: str) -> str:
    for label, css in {
        "【缺失】": "missing", "【薄弱】": "weak", "【断层】": "gap", "【冲突】": "conflict",
        "【空泛】": "generic", "【不可落地】": "unworkable", "【可保留】": "retain",
    }.items():
        if label in value:
            return css
    return ""


def render(markdown: str) -> tuple[str, list[tuple[int, str]]]:
    lines = markdown.replace("\r\n", "\n").split("\n")
    blocks: list[str] = []
    toc: list[tuple[int, str]] = []
    index = 0

    while index < len(lines):
        raw = lines[index].strip()
        if not raw:
            index += 1
            continue
        if raw.startswith("!"):
            blocks.append(inline(raw))
        elif match := re.match(r"^(#{1,3})\s+(.+)$", raw):
            level = len(match.group(1))
            title = match.group(2)
            anchor = re.sub(r"[^a-zA-Z0-9\u4e00-\u9fff]+", "-", title).strip("-").lower() or f"section-{index}"
            if level <= 2:
                toc.append((level, title))
            classes = f"issue {classification(title)}" if level == 3 and classification(title) else ""
            blocks.append(f'<h{level} id="{anchor}" class="{classes}">{inline(title)}</h{level}>')
        elif raw.startswith(">"):
            blocks.append(f"<blockquote>{inline(raw.lstrip('> ').strip())}</blockquote>")
        elif raw.startswith(("- ", "* ")):
            items = []
            while index < len(lines) and lines[index].strip().startswith(("- ", "* ")):
                items.append(f"<li>{inline(lines[index].strip()[2:])}</li>")
                index += 1
            blocks.append("<ul>" + "".join(items) + "</ul>")
            continue
        elif re.match(r"^\d+\.\s+", raw):
            items = []
            while index < len(lines) and re.match(r"^\d+\.\s+", lines[index].strip()):
                items.append(f"<li>{inline(re.sub(r'^\d+\.\s+', '', lines[index].strip()))}</li>")
                index += 1
            blocks.append("<ol>" + "".join(items) + "</ol>")
            continue
        elif "|" in raw and index + 1 < len(lines) and re.match(r"^\|?\s*:?-{3,}", lines[index + 1].strip()):
            header = [cell.strip() for cell in raw.strip("|").split("|")]
            index += 2
            rows = []
            while index < len(lines) and "|" in lines[index]:
                cells = [cell.strip() for cell in lines[index].strip().strip("|").split("|")]
                rows.append("<tr>" + "".join(f"<td>{inline(cell)}</td>" for cell in cells) + "</tr>")
                index += 1
            blocks.append("<div class=\"table-wrap\"><table><thead><tr>" + "".join(f"<th>{inline(cell)}</th>" for cell in header) + "</tr></thead><tbody>" + "".join(rows) + "</tbody></table></div>")
            continue
        else:
            paragraph = [raw]
            while index + 1 < len(lines):
                candidate = lines[index + 1].strip()
                if not candidate or candidate.startswith(("#", "- ", "* ", ">", "!")) or re.match(r"^\d+\.\s+", candidate):
                    break
                paragraph.append(candidate)
                index += 1
            blocks.append(f"<p>{inline(' '.join(paragraph))}</p>")
        index += 1

    return "\n".join(blocks), toc


def build_page(body: str, toc: list[tuple[int, str]], title: str, source: Path) -> str:
    toc_items = "".join(f"<li class=\"level-{level}\">{html.escape(item)}</li>" for level, item in toc)
    return f"""<!doctype html>
<html lang=\"zh-CN\"><head><meta charset=\"utf-8\"><meta name=\"viewport\" content=\"width=device-width,initial-scale=1\">
<title>{html.escape(title)}</title><style>
:root{{--ink:#14213d;--muted:#62708a;--paper:#f7f4ee;--card:#fffdfa;--line:#dce1e8;--accent:#ff6b35;--blue:#2563eb}}
*{{box-sizing:border-box}} body{{margin:0;background:var(--paper);color:var(--ink);font:16px/1.65 "Microsoft YaHei",system-ui,sans-serif}}
header{{padding:64px max(6vw,24px) 40px;background:linear-gradient(120deg,#14213d,#273b68);color:#fff}} header p{{max-width:850px;color:#d9e2f4}}
main{{max-width:1120px;margin:0 auto;padding:28px max(6vw,24px) 72px}} .meta{{display:flex;gap:16px;flex-wrap:wrap;color:#bfd0ef;font-size:13px}}
.notice{{border-left:4px solid var(--accent);background:#fff2eb;padding:14px 18px;margin:24px 0;border-radius:4px}} nav{{background:#edf3ff;padding:18px 22px;border-radius:12px;margin:26px 0}} nav ul{{margin:8px 0;padding-left:20px}} nav .level-2{{margin-left:16px;color:var(--muted)}}
h1{{font-size:clamp(30px,5vw,52px);line-height:1.15;margin:0 0 12px}} h2{{margin-top:46px;font-size:27px;border-bottom:2px solid var(--line);padding-bottom:8px}} h3{{margin-top:28px;background:var(--card);padding:14px 18px;border-left:5px solid var(--blue);box-shadow:0 3px 12px #14213d0b}}
h3.missing{{border-color:#b91c1c}} h3.weak{{border-color:#d97706}} h3.gap{{border-color:#7c3aed}} h3.conflict{{border-color:#be123c}} h3.generic{{border-color:#64748b}} h3.unworkable{{border-color:#ea580c}} h3.retain{{border-color:#15803d}}
p,li,blockquote{{max-width:860px}} blockquote{{margin:18px 0;padding:10px 18px;border-left:4px solid var(--blue);background:#eef5ff}} code{{background:#e8edf5;padding:1px 5px;border-radius:4px;color:#243b64}} figure{{margin:24px 0;max-width:900px;background:var(--card);padding:12px;border-radius:10px;box-shadow:0 5px 18px #14213d12}} figure img{{display:block;max-width:100%;height:auto;border-radius:6px}} figcaption{{color:var(--muted);font-size:13px;margin-top:6px}}
.table-wrap{{overflow:auto;background:var(--card);border-radius:10px;box-shadow:0 4px 14px #14213d0c}} table{{border-collapse:collapse;width:100%;min-width:680px}} th{{background:#e9effb;text-align:left}} th,td{{padding:12px;border-bottom:1px solid var(--line);vertical-align:top}}
.next-step{{margin-top:42px;padding:18px 22px;background:#14213d;color:#fff;border-radius:12px}} footer{{color:var(--muted);font-size:13px;margin-top:56px;border-top:1px solid var(--line);padding-top:16px}} @media print{{body{{background:white}} header{{padding:32px}} main{{max-width:none}}}}
</style></head><body><header><h1>{html.escape(title)}</h1><p>营销方案诊断与行动建议。此报告仅重排原始 Markdown 分析，未新增未经验证的数据或结论。</p><div class=\"meta\"><span>来源：{html.escape(source.name)}</span><span>生成日期：{date.today().isoformat()}</span></div></header><main><div class=\"notice\"><strong>阅读提示：</strong>先确认事实边界与待决事项，再使用策略、执行和 KPI 建议。</div><nav><strong>报告导航</strong><ul>{toc_items}</ul></nav>{body}<section class=\"next-step\"><strong>下一步：</strong>是否需要我继续用多角色审视这份方案？可指定品牌决策、策略、媒介/执行、电商/销售或风险合规视角。</section><footer>由 Campaign Logic Skill 可视化报告流程生成。</footer></main></body></html>"""


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown review to render")
    parser.add_argument("--output", required=True, type=Path, help="HTML report path")
    parser.add_argument("--title", default="营销方案诊断报告")
    args = parser.parse_args()
    source = args.input.resolve()
    body, toc = render(source.read_text(encoding="utf-8"))
    output = args.output.resolve()
    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(build_page(body, toc, args.title, source), encoding="utf-8")
    print(f"Generated {output}")


if __name__ == "__main__":
    main()
