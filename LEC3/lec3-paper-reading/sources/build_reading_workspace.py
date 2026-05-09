#!/usr/bin/env python3
import json
import re
import subprocess
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SOURCES = ROOT / "sources"
PDF_DIR = SOURCES / "LEC3"
MANIFEST = SOURCES / "lec3_contents.json"
EXTRACTED = ROOT / "extracted_text"
PAPERS = ROOT / "papers"

VISITED_AT = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S UTC")

TERM_MAP = {
    "DRAM": ("动态随机存取存储器（DRAM）", "主存储器技术，也是本组文献中可靠性、刷新、RowHammer、调度和近数据处理讨论的核心对象。"),
    "RowHammer": ("RowHammer 行锤击", "通过反复激活相邻行导致受害行发生位翻转的 DRAM 可靠性/安全问题。"),
    "RowPress": ("RowPress 行按压", "与长时间保持某行打开相关的 DRAM 位翻转/干扰问题。"),
    "PIM": ("存内处理（Processing-in-Memory, PIM）", "把部分计算移动到存储器附近或存储器内部，以降低数据搬移开销。"),
    "Processing-in-Memory": ("存内处理（Processing-in-Memory, PIM）", "把计算靠近数据放置的体系结构方向。"),
    "near-data": ("近数据处理（near-data processing）", "在接近数据存放位置处执行计算，减少跨层级数据移动。"),
    "near-memory": ("近内存处理（near-memory processing）", "在内存附近配置计算单元以加速访存密集任务。"),
    "PCM": ("相变存储器（Phase-Change Memory, PCM）", "一种非易失性存储器，被用于主存替代/混合内存系统研究。"),
    "ECC": ("错误纠正码（Error-Correcting Code, ECC）", "用于检测和纠正存储器错误的编码机制。"),
    "retention": ("保持时间（retention time）", "DRAM 单元在刷新前保持电荷/数据正确性的时间。"),
    "refresh": ("刷新（refresh）", "DRAM 周期性恢复单元电荷以保持数据正确性的操作。"),
    "memory scheduling": ("内存调度（memory scheduling）", "内存控制器决定请求服务顺序的策略。"),
    "memory controller": ("内存控制器（memory controller）", "管理内存请求、时序约束、调度与刷新等操作的硬件模块。"),
    "QoS": ("服务质量（Quality of Service, QoS）", "多程序/多租户系统中对性能隔离、公平性和延迟目标的约束。"),
    "latency": ("延迟（latency）", "请求从发出到完成所经历的时间。"),
    "bandwidth": ("带宽（bandwidth）", "单位时间内可传输的数据量。"),
    "approximate memory": ("近似内存（approximate memory）", "允许一定错误以换取能耗、性能或容量收益的内存设计。"),
    "genome": ("基因组（genome）", "生物信息学工作负载中待分析的遗传序列数据。"),
    "sequence alignment": ("序列比对（sequence alignment）", "比较 DNA/RNA/蛋白序列相似性的核心生物信息学任务。"),
    "graph processing": ("图处理（graph processing）", "以顶点和边为对象的图算法计算。"),
    "GPU": ("图形处理器（Graphics Processing Unit, GPU）", "高度并行的加速处理器，也常用于通用计算。"),
    "locality": ("局部性（locality）", "程序访问在时间或空间上集中出现的性质。"),
    "metadata": ("元数据（metadata）", "用于描述、管理或优化数据/内存对象的辅助信息。"),
    "Ramulator": ("Ramulator 内存模拟器", "用于建模 DRAM/内存系统时序与行为的模拟工具。"),
    "DDR5": ("第五代双倍数据率同步动态随机存取存储器（DDR5）", "较新的 DRAM 标准。"),
    "HBM": ("高带宽内存（High Bandwidth Memory, HBM）", "通过堆叠和宽接口提供高带宽的内存技术。"),
}


def slugify(name: str) -> str:
    stem = Path(name).stem
    slug = re.sub(r"[^A-Za-z0-9._-]+", "-", stem).strip("-._")
    return slug[:120] or "paper"


def run(args):
    proc = subprocess.run(args, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace"), proc.stderr.decode("utf-8", "replace")


def parse_pdfinfo(pdf: Path):
    code, out, err = run(["pdfinfo", str(pdf)])
    info = {}
    if code != 0:
        return info, err.strip()
    for line in out.splitlines():
        if ":" in line:
            key, value = line.split(":", 1)
            info[key.strip()] = value.strip()
    return info, ""


def extract_pdf_text(pdf: Path):
    code, out, err = run(["pdftotext", "-layout", "-enc", "UTF-8", str(pdf), "-"])
    if code != 0:
        return [], err.strip()
    pages = out.split("\f")
    if pages and not pages[-1].strip():
        pages = pages[:-1]
    return pages, ""


def clean_lines(text: str):
    lines = []
    for raw in text.splitlines():
        line = re.sub(r"\s+", " ", raw).strip()
        if line:
            lines.append(line)
    return lines


def first_location(pages, pattern: str, flags=re.IGNORECASE):
    regex = re.compile(pattern, flags)
    for idx, page in enumerate(pages, start=1):
        lines = clean_lines(page)
        for lidx, line in enumerate(lines, start=1):
            if regex.search(line):
                return f"Page {idx}, line {lidx}"
    return "未定位"


def infer_title(pdf_name: str, info, pages):
    title = info.get("Title", "").strip()
    bad = {"", "untitled", "microsoft powerpoint", "powerpoint presentation"}
    if title.lower() not in bad and len(title) > 6:
        return title

    if pages:
        lines = clean_lines(pages[0])
        useful = []
        for line in lines[:30]:
            low = line.lower()
            if low.startswith(("arxiv:", "abstract", "proceedings", "copyright", "isbn", "issn")):
                continue
            if re.fullmatch(r"\d+", line):
                continue
            useful.append(line)
            if len(" ".join(useful)) > 120 or len(useful) >= 3:
                break
        if useful:
            return " ".join(useful)

    return Path(pdf_name).stem


def infer_year(name: str, info):
    for pattern in [
        r"(?:micro|isca|dsn|hpca|asplos|iccd|fpl|taco|tcad|sigmetrics|imw|isscc)(\d{2})",
        r"_(\d{4})",
        r"-(\d{4})",
    ]:
        m = re.search(pattern, name, re.IGNORECASE)
        if m:
            year = m.group(1)
            return "20" + year if len(year) == 2 else year
    m = re.match(r"(\d{2})(\d{2})\.", name)
    if m:
        yy = int(m.group(1))
        return str(2000 + yy)
    for key in ("CreationDate", "ModDate"):
        m = re.search(r"(20\d{2}|19\d{2})", info.get(key, ""))
        if m:
            return m.group(1)
    return "未找到"


def infer_venue(name: str):
    pairs = [
        ("micro", "MICRO"),
        ("isca", "ISCA"),
        ("dsn", "DSN"),
        ("hpca", "HPCA"),
        ("asplos", "ASPLOS"),
        ("iccd", "ICCD"),
        ("fpl", "FPL"),
        ("taco", "ACM TACO"),
        ("tcad", "IEEE TCAD"),
        ("sigmetrics", "SIGMETRICS"),
        ("ieeemicro", "IEEE Micro"),
        ("ieee_micro", "IEEE Micro"),
        ("isscc", "ISSCC"),
        ("springer", "Springer book chapter"),
        ("arxiv", "arXiv"),
    ]
    low = name.lower()
    for needle, venue in pairs:
        if needle in low:
            return venue
    if re.match(r"\d{4}\.\d+", name):
        return "arXiv"
    return "未找到"


def infer_topic(name: str, title: str):
    text = f"{name} {title}".lower()
    if "rowhammer" in text or "rowpress" in text:
        return "DRAM disturbance / RowHammer"
    if "pim" in text or "processing-in-memory" in text or "near-memory" in text or "near-data" in text:
        return "Processing-in-Memory / Near-Data Processing"
    if "genome" in text or "genasm" in text:
        return "Genome analysis acceleration"
    if "pcm" in text or "phase-change" in text:
        return "Phase-change memory"
    if "refresh" in text or "retention" in text:
        return "DRAM refresh / retention profiling"
    if "ecc" in text or "error" in text or "failure" in text or "reliability" in text:
        return "Memory reliability"
    if "scheduler" in text or "scheduling" in text or "slowdown" in text or "mise" in text:
        return "Memory scheduling / QoS"
    if "gpu" in text or "locality" in text:
        return "GPU locality / memory hierarchy"
    if "ramulator" in text:
        return "Memory-system simulation"
    if "ddr5" in text:
        return "DRAM device / DDR5"
    return "Computer architecture / memory systems"


def extract_abstract(pages):
    joined = "\n".join(f"[Page {idx}]\n{page}" for idx, page in enumerate(pages[:3], start=1))
    m = re.search(
        r"(?is)\babstract\b\s*[-—:]?\s*(.*?)(?:\n\s*(?:1\s+)?(?:introduction|i\.\s*introduction|keywords|index terms)\b)",
        joined,
    )
    if m:
        return re.sub(r"\s+", " ", m.group(1)).strip()[:3000]
    return ""


def extract_sections(pages):
    candidates = []
    section_re = re.compile(
        r"^(?:\d+(?:\.\d+)*|[IVX]+)\.?\s+[A-Z][A-Za-z0-9,;:()/'’\- ]{3,90}$|^(?:Abstract|Introduction|Background|Related Work|Method|Methodology|Evaluation|Experimental Setup|Results|Discussion|Conclusion|References|Appendix)\b",
        re.IGNORECASE,
    )
    for pidx, page in enumerate(pages, start=1):
        for line in clean_lines(page):
            if len(line) > 120:
                continue
            if section_re.match(line):
                normalized = line.strip()
                if normalized.lower() not in {c[0].lower() for c in candidates}:
                    candidates.append((normalized, f"Page {pidx}"))
    return candidates[:40]


def extract_captions(pages, kind: str):
    if kind == "figure":
        regex = re.compile(r"\b(?:Fig\.|Figure)\s+([A-Za-z0-9.]+)[:.\s-]+(.{10,260})", re.IGNORECASE)
    else:
        regex = re.compile(r"\bTable\s+([A-Za-z0-9.]+)[:.\s-]+(.{10,260})", re.IGNORECASE)
    rows = []
    seen = set()
    for pidx, page in enumerate(pages, start=1):
        for line in clean_lines(page):
            m = regex.search(line)
            if not m:
                continue
            key = (m.group(1), m.group(2)[:80].lower())
            if key in seen:
                continue
            seen.add(key)
            rows.append((m.group(1), f"Page {pidx}", m.group(2).strip()))
    return rows[:80]


def extract_equation_hints(pages):
    rows = []
    eq_re = re.compile(r"(?:Equation|Eq\.)\s*\(?([0-9A-Za-z.]+)\)?|^\s*\(?([0-9]+)\)\s*$", re.IGNORECASE)
    seen = set()
    for pidx, page in enumerate(pages, start=1):
        lines = page.splitlines()
        for lidx, line in enumerate(lines, start=1):
            if eq_re.search(line):
                snippet = re.sub(r"\s+", " ", line).strip()
                if not snippet:
                    continue
                if snippet in seen:
                    continue
                seen.add(snippet)
                rows.append((f"Eq hint {len(rows)+1}", f"Page {pidx}, line {lidx}", snippet[:180]))
    return rows[:50]


def detect_terms(pages):
    text = "\n".join(pages)
    found = []
    for term, (zh, desc) in TERM_MAP.items():
        if re.search(rf"\b{re.escape(term)}\b", text, re.IGNORECASE):
            found.append((term, zh, first_location(pages, rf"\b{re.escape(term)}\b"), desc))
    return found


def md_escape(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ").strip()


def summarize_abstract(abstract: str):
    if not abstract:
        return "未能从 PDF 文本中稳定提取 abstract；需要阅读 extracted_text 中的 Page 1 起始部分确认。"
    sentences = re.split(r"(?<=[.!?])\s+", abstract)
    return " ".join(sentences[:3]).strip()


def write_paper_files(item, pdf: Path):
    slug = slugify(pdf.name)
    paper_dir = PAPERS / slug
    paper_dir.mkdir(parents=True, exist_ok=True)

    info, info_error = parse_pdfinfo(pdf)
    pages, extract_error = extract_pdf_text(pdf)
    page_count = int(info.get("Pages", "0") or 0)
    title = infer_title(pdf.name, info, pages)
    year = infer_year(pdf.name, info)
    venue = infer_venue(pdf.name)
    topic = infer_topic(pdf.name, title)
    abstract = extract_abstract(pages)
    abstract_summary = summarize_abstract(abstract)
    sections = extract_sections(pages)
    figures = extract_captions(pages, "figure")
    tables = extract_captions(pages, "table")
    equations = extract_equation_hints(pages)
    terms = detect_terms(pages)
    word_count = len(re.findall(r"[A-Za-z0-9_]+", "\n".join(pages)))

    extracted_path = EXTRACTED / f"{slug}.txt"
    with extracted_path.open("w", encoding="utf-8") as out:
        out.write(f"Source PDF: {pdf}\n")
        out.write(f"GitHub URL: {item.get('html_url', '')}\n")
        out.write(f"Accessed: {VISITED_AT}\n\n")
        for idx, page in enumerate(pages, start=1):
            out.write(f"\n\n===== Page {idx} =====\n\n")
            out.write(page.rstrip() + "\n")

    arxiv_id = "未找到"
    m = re.match(r"(\d{4}\.\d+)(?:v\d+)?\.pdf$", pdf.name)
    if m:
        arxiv_id = m.group(1)
    doi = "未找到"

    authors = info.get("Author", "未找到") or "未找到"
    if authors.lower() in {"anonymous", "unknown"}:
        authors = "未找到"

    keywords = sorted({topic, *(term for term, *_ in terms[:8])})
    keyword_text = ", ".join(keywords) if keywords else "未找到"

    reading_status = "已下载并提取原文；待逐篇深度阅读与完整中文翻译"
    full_text = "Yes" if pages and word_count > 500 else "No"

    metadata = f"""# Paper Metadata

- Title: {title}
- Chinese Title: 待深度翻译确认
- Authors: {authors}
- Year: {year}
- Venue / Journal / Conference: {venue}
- DOI: {doi}
- arXiv ID: {arxiv_id}
- URL: {item.get('html_url', '未找到')}
- PDF Source: {item.get('download_url', str(pdf))}
- Code / Project Page: 未找到
- Dataset: 待深度阅读确认
- Main Topic: {topic}
- Keywords: {keyword_text}
- Reading Status: {reading_status}
- Full Text Available: {full_text}
- Notes: 本文件由批量提取脚本生成。由于本轮共有 53 个 PDF，除原文提取和索引外，深度语义总结、完整翻译、实验细节核验仍需逐篇完成；未完成项不会被标记为完成。
"""
    (paper_dir / "metadata.md").write_text(metadata, encoding="utf-8")

    section_lines = "\n".join(f"- {name}: {loc}" for name, loc in sections[:18]) or "- 未稳定识别章节标题。"
    focus = {
        "DRAM disturbance / RowHammer": "建议重点读 problem/threat model、实验平台、位翻转触发条件、防御比较和局限。",
        "Processing-in-Memory / Near-Data Processing": "建议重点读系统架构、数据映射、编程/ISA 接口、性能/能耗评估和适用工作负载。",
        "Memory reliability": "建议重点读错误模型、测量方法、故障分类、ECC/恢复机制和真实系统数据。",
        "Memory scheduling / QoS": "建议重点读调度目标函数、公平性/slowdown 模型、baseline 和多程序实验。",
        "Phase-change memory": "建议重点读写入开销、耐久性、混合内存管理和与 DRAM 的权衡。",
        "Genome analysis acceleration": "建议重点读算法映射、近似/精确匹配机制、硬件结构和端到端加速比。",
    }.get(topic, "建议重点读问题定义、系统模型、核心机制、实验设置、主要表格和作者承认的局限。")
    intro_loc = first_location(pages, r"\bintroduction\b")
    eval_loc = first_location(pages, r"\b(evaluation|experimental|results?)\b")
    conclusion_loc = first_location(pages, r"\b(conclusion|discussion)\b")
    reading_summary = f"""# 中文阅读摘要

> 状态说明：本文 PDF 已下载并成功提取文本，但尚未完成逐段深度阅读与完整中文翻译。以下是基于文件名、PDF 元数据、abstract/章节标题/图表标题的“初步阅读索引”，不能替代完整论文报告。

## 1. 一句话总结

这篇材料的主题初步归类为 **{topic}**；从可提取文本看，核心内容需要围绕标题 `{title}` 回到原文继续精读。

## 2. 研究背景

初步背景线索：{abstract_summary}

原文定位：Abstract 通常位于 Page 1；Introduction 检测位置：{intro_loc}。

## 3. 核心问题

- 待深度阅读确认：作者具体要解决的瓶颈、失效模式或系统设计问题。
- 可先回溯位置：Page 1 Abstract；{intro_loc}。

## 4. 核心贡献

- 待深度阅读确认：贡献列表通常位于 Introduction 后半部分。
- 可检索关键词：contribution, propose, design, evaluate, demonstrate。

## 5. 方法概述

待逐篇精读确认。当前只完成结构定位，识别到的章节如下：

{section_lines}

## 6. 实验设计

待逐篇精读确认。Evaluation/Results 初步位置：{eval_loc}。

## 7. 主要结果

待逐篇精读确认。请优先查看 Tables 与 Figures 文件中列出的表格/图注位置。

## 8. 关键结论

待逐篇精读确认。Conclusion/Discussion 初步位置：{conclusion_loc}。

## 9. 局限性

待逐篇精读确认。当前不能只基于 abstract 或文件名判断局限。

## 10. 适合我重点关注的内容

{focus}

## 11. 和其他文献的关系

这篇材料属于 LEC3 中的 `{topic}` 主题簇，可与同主题文件在 `00_Cross_Paper_Synthesis.md` 中一起阅读。
"""
    (paper_dir / "reading_summary.zh.md").write_text(reading_summary, encoding="utf-8")

    key_rows = [
        ["1", "标题和主题识别", "Page 1 / PDF metadata", title, "高", f"先确认本文是否确实属于 {topic}。"],
        ["2", "Abstract 中的问题背景", "Page 1 / Abstract", abstract_summary[:220], "高", "这是进入全文前的最小上下文；不能替代方法和实验阅读。"],
        ["3", "Introduction 起点", intro_loc, "检测到 Introduction/引言关键词。", "高", "贡献、动机和问题定义通常集中在这里。"],
        ["4", "Evaluation/Results 起点", eval_loc, "检测到 evaluation/results/experimental 关键词。", "高", "主要实验设置和结论需要从这里核验。"],
        ["5", "Conclusion/Discussion 起点", conclusion_loc, "检测到 conclusion/discussion 关键词。", "中", "适合确认作者最终主张和局限。"],
    ]
    key_table = "\n".join(
        "| " + " | ".join(md_escape(cell) for cell in row) + " |" for row in key_rows
    )
    key_points = f"""# Key Points with Source Locations

> 状态说明：以下为“定位索引”，不是完整深度结论。所有未精读项均标为待确认。

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
{key_table}
"""
    (paper_dir / "key_points_with_locations.zh.md").write_text(key_points, encoding="utf-8")

    translation = f"""# Full Chinese Translation

## Title

原文标题：{title}

中文标题：待深度翻译确认

## 翻译状态

未完成完整中文翻译。

原因：本轮一次性识别到 53 个 PDF，已经完成合法来源下载和全文文本提取；但为了遵守“不要在未完整阅读时假装已读完”和“不要生成不准确完整翻译”的要求，本文件暂不填充伪完整译文。

可回溯原文：`paper reading/extracted_text/{slug}.txt`

## Abstract / 摘要

### 原文位置

Page 1 / Abstract（若 PDF 文本结构无 Abstract 标题，请以 extracted text 的 Page 1 为准）

### 中文翻译

待逐篇翻译。

## 后续处理建议

建议按 `00_INDEX.md` 的推荐顺序，每次选择 1-3 篇进行完整中文翻译和深度阅读报告生成。
"""
    (paper_dir / "full_translation.zh.md").write_text(translation, encoding="utf-8")

    fig_rows = "\n".join(
        f"| Figure {md_escape(num)} | {loc} | {md_escape(cap[:100])} | 待阅读图像本体确认 | 可能支撑方法或实验叙述 | 建议回到 PDF 查看原图 |"
        for num, loc, cap in figures
    ) or "| 未稳定识别 | 未定位 | 未提取到图注 | 图像可能存在但文本提取未捕获 | 需要回 PDF | 建议人工检查 |"
    table_rows = "\n".join(
        f"| Table {md_escape(num)} | {loc} | {md_escape(cap[:100])} | 待阅读表格本体确认 | 可能包含实验结果或参数 | 建议回到 PDF 查看原表 |"
        for num, loc, cap in tables
    ) or "| 未稳定识别 | 未定位 | 未提取到表注 | 表格可能存在但文本提取未捕获 | 需要回 PDF | 建议人工检查 |"
    eq_rows = "\n".join(
        f"| {md_escape(num)} | {loc} | {md_escape(snippet)} | 待确认 | 待结合上下文解释 | 待判断 |"
        for num, loc, snippet in equations
    ) or "| 未稳定识别 | 未定位 | 未提取到公式编号 | 待确认 | 公式可能被 PDF 文本化破坏 | 待判断 |"
    fte = f"""# Figures, Tables, and Equations Notes

> 说明：本文件基于 `pdftotext` 捕获的图注/表注/公式编号线索生成。图像、复杂表格和公式排版本身未被还原，建议回到 PDF 查看。

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{fig_rows}

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{table_rows}

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
{eq_rows}
"""
    (paper_dir / "figures_tables_equations_notes.zh.md").write_text(fte, encoding="utf-8")

    term_rows = "\n".join(
        f"| {md_escape(term)} | {md_escape(zh)} | {loc} | {md_escape(desc)} | 是 |"
        for term, zh, loc, desc in terms
    ) or "| 未稳定识别 | 待确认 | 未定位 | 需要深度阅读后整理 | 待确认 |"
    terminology = f"""# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
{term_rows}
"""
    (paper_dir / "terminology.zh.md").write_text(terminology, encoding="utf-8")

    limitations = f"""# Limitations and Questions

## 1. 作者明确承认的局限

待逐篇深度阅读确认。请优先搜索 `limitation`, `threat`, `future work`, `assumption`。

## 2. 论文中隐含的局限

当前不能只基于文件名/abstract 推断为确定事实。需要结合方法、实验设置和评估范围判断。

## 3. 实验设计可能存在的问题

- 待确认 baseline 是否充分。
- 待确认 workload/dataset 是否代表目标场景。
- 待确认仿真、原型或真实系统测量之间是否存在外推风险。

## 4. 方法可能不适用的场景

待深度阅读确认。

## 5. 我阅读时应该追问的问题

- 作者的问题定义是否清楚，和 `{topic}` 主题中的其它论文有什么差异？
- 关键结论是否由实验表格/图支撑？
- 论文是否依赖特定硬件假设、错误模型或工作负载分布？
- 有哪些结论需要回到 Page 1 Abstract、{intro_loc}、{eval_loc}、{conclusion_loc} 核验？

## 6. 后续可以继续阅读的方向

优先与 `00_Cross_Paper_Synthesis.md` 中同主题论文一起读，形成对比。
"""
    (paper_dir / "limitations_and_questions.zh.md").write_text(limitations, encoding="utf-8")

    checklist = """# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题
- [ ] 我能解释作者的方法
- [ ] 我能指出核心创新
- [ ] 我能看懂主要实验表格
- [ ] 我能解释最重要的图
- [ ] 我知道这篇文章的局限
- [ ] 我知道这篇文章和其他工作的关系
- [ ] 我知道哪些结论有原文支持
- [ ] 我知道哪些问题还需要继续查证
- [ ] 我已经核对 extracted_text 中的页码和 PDF 页码是否一致
- [ ] 我已经确认 full_translation.zh.md 是否完成，而不是只看到了占位状态
"""
    (paper_dir / "reading_checklist.md").write_text(checklist, encoding="utf-8")

    extraction_log = f"""# Extraction Log

- Input Type: GitHub repository folder PDF
- Source: {item.get('html_url', '未找到')}
- Access Status: 下载成功
- Full Text Retrieved: {'Yes' if pages else 'No'}
- PDF Pages: {page_count or len(pages) or '未找到'}
- Sections Detected: {len(sections)}
- Figures Detected: {len(figures)} via caption text; images not extracted
- Tables Detected: {len(tables)} via caption text; table structure not reconstructed
- Equations Detected: {len(equations)} via numbering/text hints only
- Appendix Detected: {'Yes' if first_location(pages, r'\\bappendix\\b') != '未定位' else 'No'}
- Supplementary Material Detected: 未检测到
- OCR Used: No
- Missing Content: 图像本体、复杂公式排版、复杂表格结构可能未被文本提取完整；完整中文翻译未完成
- Parsing Problems: {info_error or extract_error or '未发现致命提取错误'}
- Uncertain Parts: 标题/作者/数据集/贡献/局限需要逐篇人工或 LLM 深读确认
- Need User Action: 若需要完整翻译，请按推荐顺序指定 1-3 篇继续逐篇处理
- Extracted Text File: paper reading/extracted_text/{slug}.txt
- Accessed: {VISITED_AT}

## Quality Check

- 已下载 PDF: Yes
- 已提取带页码原文: {'Yes' if pages else 'No'}
- 是否只读 abstract: 当前只生成自动索引，未声称完成深度阅读
- 是否遗漏 appendix: 仅通过文本关键词检测，需回 PDF 复核
- 是否提取图表公式: 已提取文本线索；未还原图像/表格/公式排版
- 是否给出原文位置: 已为关键入口和图表线索标注页码/行号
- 中文翻译是否覆盖完整正文: No
- 术语翻译是否一致: 初步术语表使用全局 TERM_MAP，待深读扩充
- 是否存在推测: Yes，主题和部分元数据为启发式推断
"""
    (paper_dir / "extraction_log.md").write_text(extraction_log, encoding="utf-8")

    return {
        "slug": slug,
        "name": pdf.name,
        "title": title,
        "year": year,
        "venue": venue,
        "topic": topic,
        "status": reading_status,
        "full_text": full_text,
        "pages": page_count or len(pages),
        "figures": len(figures),
        "tables": len(tables),
        "equations": len(equations),
        "terms": [t[0] for t in terms],
        "url": item.get("html_url", ""),
        "summary": abstract_summary,
        "intro": intro_loc,
        "eval": eval_loc,
        "conclusion": conclusion_loc,
    }


def make_global_files(records):
    topic_counts = Counter(r["topic"] for r in records)
    rows = []
    for idx, r in enumerate(records, start=1):
        rows.append(
            f"| {idx} | {md_escape(r['title'][:120])} | {r['year']} | 已下载/已提取/待深读翻译 | {md_escape(r['topic'])} | papers/{r['slug']} | {r['pages']} pages |"
        )
    index = f"""# Paper Reading Index

## 文献列表

| 编号 | 标题 | 年份 | 状态 | 主题 | 文件夹 | 备注 |
|---|---|---|---|---|---|---|
{chr(10).join(rows)}

## 推荐阅读顺序

1. 先读 DRAM/RowHammer 基础与综述：`dram-row-hammer_isca14`, `RowHammer-Retrospective_ieee_tcad19`, `rowhammer-and-other-memory-issues_date17`, `RowPress_isca23`。
2. 再读 DRAM retention/refresh/reliability：`raidr-dram-refresh_isca12`, `avatar-dram-refresh_dsn15`, `reaper-dram-retention-profiling-lpddr4_isca17`, `HARP-memory-error-profiling_micro21`, `BEER-bit-exact-ECC-recovery_micro20`。
3. 接着读 memory scheduling/QoS：`staged-memory-scheduling_isca12`, `mise-predictable_memory_performance-hpca13`, `application-slowdown-model_micro15`, `dash_deadline-aware-heterogeneous-memory-scheduler_taco16`。
4. 然后读 PIM / near-data / accelerator：`ModernPrimerOnPIM_springer-emerging-computing-bookchapter21`, `Google-consumer-workloads-data-movement-and-PIM_asplos18`, `tesseract-pim-architecture-for-graph-processing_isca15`, `GenASM-approximate-string-matching-framework-for-genome-analysis_micro20`。
5. 最后读工具、接口和新近 arXiv/器件材料：`Ramulator2_arxiv23`, `MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv`, `a-1.1v-16gb-ddr5-dram_isscc2023` 等。

## 每篇文章一句话总结

当前已生成每篇的初步主题归类和 abstract 入口索引；完整一句话深度总结待逐篇精读后补全。

## 当前未完成或需要我补充的内容

- 53 篇材料均已下载并提取原文。
- 53 篇完整中文翻译均未完成；每个 `full_translation.zh.md` 已明确标记待翻译。
- 图像本体、复杂表格和公式排版未被 OCR/视觉方式还原。

## 文件结构说明

- `sources/LEC3/`: 下载的 PDF 源文件副本。
- `extracted_text/`: 每篇 PDF 的带页码原文文本。
- `papers/<paper_short_name>/`: 每篇材料的元数据、初步阅读索引、图表公式线索、术语、问题清单和处理日志。
"""
    (ROOT / "00_INDEX.md").write_text(index, encoding="utf-8")

    status_rows = []
    for idx, r in enumerate(records, start=1):
        status_rows.append(
            f"| {idx} | GitHub LEC3 PDF | {md_escape(r['title'][:100])} | {r['full_text']} | 初步索引完成，深度摘要未完成 | No | 初步定位完成 | 53篇批量任务，尚未逐篇深读/翻译 | 如需完整翻译，请指定优先论文 |"
        )
    status = f"""# Reading Status

| 编号 | 输入形式 | 标题 | 是否找到全文 | 是否完成摘要 | 是否完成翻译 | 是否完成定位 | 问题 | 需要我补充 |
|---|---|---|---|---|---|---|---|---|
{chr(10).join(status_rows)}
"""
    (ROOT / "00_Reading_Status.md").write_text(status, encoding="utf-8")

    summary_rows = []
    for r in records:
        summary_rows.append(
            f"| {md_escape(r['title'][:80])} | 待深读确认 | {md_escape(r['topic'])} | 待深读确认 | 待深读确认 | 待深读确认 | 待深读确认 | {md_escape(r['intro'])}; {md_escape(r['eval'])} |"
        )
    summary = f"""# All Papers Summary Table

> 状态说明：这是批量提取后的索引表，不是完整深度总结表。未精读字段保留为“待深读确认”。

| 论文 | 研究问题 | 方法 | 数据集/实验 | 主要结论 | 贡献 | 局限 | 我应该重点读哪里 |
|---|---|---|---|---|---|---|---|
{chr(10).join(summary_rows)}
"""
    (ROOT / "00_All_Papers_Summary_Table.md").write_text(summary, encoding="utf-8")

    topic_lines = "\n".join(f"- {topic}: {count} 篇/份" for topic, count in topic_counts.most_common())
    synthesis = f"""# Cross-Paper Synthesis

> 状态说明：以下综合是基于文件名、初步文本提取和主题归类的学习路线，不是逐篇精读后的最终综述。

## 1. 这些文献共同关注的问题

LEC3 的材料集中在 memory systems：DRAM 可靠性与安全、刷新/保持时间、RowHammer/RowPress、内存调度与 QoS、Processing-in-Memory / Near-Data Processing、PCM/新型内存、模拟器与跨层接口。

主题分布：

{topic_lines}

## 2. 方法之间的关系

- DRAM 可靠性论文通常从真实设备测量、错误模型、检测/恢复机制和系统级缓解出发。
- RowHammer/RowPress 论文更偏安全与电路/架构交界处，需要和 refresh/retention 文献一起读。
- Memory scheduling/QoS 论文关注多程序干扰、slowdown 估计、公平性和截止时间。
- PIM/near-data 论文关注数据搬移瓶颈，将计算靠近内存以提升带宽利用率和能效。

## 3. 技术路线对比

- 测量型：通过真实 DRAM/系统数据建立错误或保持时间分布。
- 机制型：提出刷新、纠错、恢复、调度或接口机制。
- 加速型：针对图、基因组、稀疏矩阵、时序分析等 workload 设计 near-memory/PIM 架构。
- 工具型：模拟器、控制平台或元数据管理，为后续研究提供实验基础。

## 4. 结论是否一致

待逐篇精读确认。初步看，这批材料共同指向一个核心判断：数据搬移、DRAM 可靠性和内存系统干扰是现代系统的重要瓶颈，但不同论文的假设、设备代际和 workload 可能导致结论边界不同。

## 5. 争议点或不确定点

- RowHammer/RowPress 防御的覆盖范围和代价是否能跨 DRAM 代际成立。
- Retention/refresh profiling 的离线成本、在线适用性和温度敏感性。
- PIM/near-data 的收益是否被编程模型、数据布局和系统集成成本抵消。
- 仿真结果与真实硬件结果之间的外推风险。

## 6. 哪些论文适合先读

先读综述/基础：`ModernPrimerOnPIM_springer-emerging-computing-bookchapter21`, `RowHammer-Retrospective_ieee_tcad19`, `memory-scaling_imw13`。

## 7. 哪些论文适合深入读

深入读经典机制：`dram-row-hammer_isca14`, `raidr-dram-refresh_isca12`, `staged-memory-scheduling_isca12`, `pcm_isca09`, `tesseract-pim-architecture-for-graph-processing_isca15`, `GenASM-approximate-string-matching-framework-for-genome-analysis_micro20`。

## 8. 我的学习路线建议

1. 建立 DRAM/内存系统基础概念。
2. 学 RowHammer/retention/refresh 这条可靠性主线。
3. 学 memory scheduling/QoS，理解共享内存系统性能隔离。
4. 学 PIM/near-data，把数据搬移瓶颈和应用加速联系起来。
5. 最后读工具/模拟器/接口论文，理解如何复现实验。

## 9. 后续值得补充阅读的方向

- 最新 DDR5/LPDDR5 RowHammer 防御和 TRR 分析。
- CXL memory pooling 与 disaggregated memory。
- HBM-PIM、UPMEM、Samsung/AiM 等产业 PIM 平台。
- 真实云数据中心内存错误研究。
"""
    (ROOT / "00_Cross_Paper_Synthesis.md").write_text(synthesis, encoding="utf-8")

    global_terms = {}
    for r in records:
        for term in r["terms"]:
            global_terms.setdefault(term, set()).add(r["slug"])
    term_rows = []
    for term, papers in sorted(global_terms.items()):
        zh, desc = TERM_MAP.get(term, ("待确认", "待确认"))
        importance = "高" if len(papers) >= 5 or term in {"DRAM", "RowHammer", "PIM", "ECC"} else "中"
        term_rows.append(
            f"| {md_escape(term)} | {md_escape(zh)} | {', '.join(sorted(papers)[:8])}{' 等' if len(papers) > 8 else ''} | {md_escape(desc)} | {importance} |"
        )
    glossary = f"""# Global Glossary

| English Term | 中文翻译 | 出现论文 | 简明解释 | 重要程度 |
|---|---|---|---|---|
{chr(10).join(term_rows) if term_rows else '| 待确认 | 待确认 | 待确认 | 待深度阅读后整理 | 待确认 |'}
"""
    (ROOT / "00_Glossary.md").write_text(glossary, encoding="utf-8")

    open_questions = """# Open Questions

| 编号 | 问题 | 相关论文 | 原文位置 | 为什么重要 | 下一步建议 |
|---|---|---|---|---|---|
| 1 | 每篇论文的核心贡献是否已从 Introduction 和 Evaluation 中逐条核验？ | 全部 | 各论文 Introduction / Evaluation | 避免只基于 abstract 或文件名形成误解 | 按推荐顺序逐篇精读 |
| 2 | 哪些 PDF 的图表/公式在文本提取中丢失或错位？ | 全部 | 各论文 figures_tables_equations_notes.zh.md | 图表通常支撑核心结论 | 回 PDF 人工查看关键图表 |
| 3 | RowHammer/RowPress 相关论文的设备代际、温度、电压和访问模式假设是否一致？ | RowHammer/RowPress 主题簇 | 各论文 Method/Evaluation | 这些假设决定结论外推范围 | 做同主题对照表 |
| 4 | PIM/near-data 论文是否考虑编程模型、数据搬移到 PIM 的代价和系统集成？ | PIM 主题簇 | Architecture/Evaluation | 决定加速收益是否真实可落地 | 逐篇抽取 baseline 与 overhead |
| 5 | Memory scheduling 论文的 slowdown/fairness 指标是否可直接比较？ | scheduling 主题簇 | Evaluation/metrics | 指标差异会影响论文间结论比较 | 建立指标术语表 |
"""
    (ROOT / "00_Open_Questions.md").write_text(open_questions, encoding="utf-8")


def main():
    EXTRACTED.mkdir(parents=True, exist_ok=True)
    PAPERS.mkdir(parents=True, exist_ok=True)
    items = json.loads(MANIFEST.read_text(encoding="utf-8"))
    by_name = {item["name"]: item for item in items if item.get("name", "").lower().endswith(".pdf")}
    records = []
    for name in sorted(by_name):
        pdf = PDF_DIR / name
        if not pdf.exists():
            continue
        records.append(write_paper_files(by_name[name], pdf))
    make_global_files(records)
    print(f"processed {len(records)} PDFs")


if __name__ == "__main__":
    main()
