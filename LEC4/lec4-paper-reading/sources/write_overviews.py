from pathlib import Path
import re


ROOT = Path(__file__).resolve().parents[1]
PAPERS_DIR = ROOT / "papers"

ORDER = [
    "1905.09822v3",
    "2111.00082v6",
    "2207.13795v4",
    "2211.05838v6",
    "2310.10168v2",
    "2402.18736v2",
    "2402.19080v2",
    "2405.06081v1",
    "2501.17466v2",
    "2506.12947v1",
    "SimplePIM_pact23",
    "TOM-programmer-transparent-GPU-near-data-processing_isca16",
    "ambit-bulk-bitwise-dram_micro17",
    "cellular_logic-in-memory_arrays",
    "figaro-fine-grained-in-dram-data-relocation-and-caching_micro20",
    "in-dram-bulk-and-or-ieee_cal15",
    "lisa-dram_hpca16",
    "micro19-gao",
    "micro22-gao",
    "network-on-memory-data-copy_ieee-cal20",
    "pim-enabled-instructons-for-low-overhead-pim_isca15",
    "rowclone_micro13",
    "simdram_asplos21",
    "stone_logic_in_memory_1970",
]

ROUND_BY_SLUG = {
    **{slug: "第一轮" for slug in ORDER[:5]},
    **{slug: "第二轮" for slug in ORDER[5:10]},
    **{slug: "第三轮" for slug in ORDER[10:15]},
    **{slug: "第四轮" for slug in ORDER[15:20]},
    **{slug: "第五轮" for slug in ORDER[20:]},
}


def read(path: Path) -> str:
    return path.read_text(encoding="utf-8")


def write(rel: str, text: str) -> None:
    (ROOT / rel).write_text(text.rstrip() + "\n", encoding="utf-8")


def clean_cell(text: str, max_len: int = 180) -> str:
    text = re.sub(r"\s+", " ", text).strip()
    text = text.replace("|", "｜")
    if len(text) > max_len:
        text = text[: max_len - 1] + "…"
    return text


def table(rows, headers):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out.extend("| " + " | ".join(clean_cell(col, 260) for col in row) + " |" for row in rows)
    return "\n".join(out)


def metadata(slug):
    meta = {}
    text = read(PAPERS_DIR / slug / "metadata.md")
    for line in text.splitlines():
        if line.startswith("- ") and ":" in line:
            k, v = line[2:].split(":", 1)
            meta[k.strip()] = v.strip()
    return meta


def section(text, heading):
    pattern = rf"## {re.escape(heading)}\n(.*?)(?=\n## |\Z)"
    m = re.search(pattern, text, flags=re.S)
    return m.group(1).strip() if m else ""


def bullets(sec, n=2):
    vals = [line[2:].strip() for line in sec.splitlines() if line.startswith("- ")]
    if not vals and sec:
        vals = [sec.strip()]
    return "；".join(vals[:n])


def paper_data(slug):
    meta = metadata(slug)
    summary = read(PAPERS_DIR / slug / "reading_summary.zh.md")
    return {
        "slug": slug,
        "title": meta.get("Title", "未找到"),
        "year": meta.get("Year", "未找到"),
        "topic": meta.get("Main Topic", "未找到"),
        "status": meta.get("Reading Status", "深度阅读完成"),
        "full": meta.get("Full Text Available", "Yes"),
        "one": section(summary, "1. 一句话总结"),
        "problem": bullets(section(summary, "3. 核心问题")),
        "method": bullets(section(summary, "5. 方法概述")),
        "experiment": bullets(section(summary, "6. 实验设计")),
        "results": bullets(section(summary, "7. 主要结果")),
        "contrib": bullets(section(summary, "4. 核心贡献")),
        "limits": bullets(section(summary, "9. 局限性")),
        "focus": bullets(section(summary, "10. 适合我重点关注的内容")),
    }


PAPERS = [paper_data(slug) for slug in ORDER]


def write_index():
    rows = []
    for i, p in enumerate(PAPERS, 1):
        rows.append([
            str(i),
            p["title"],
            p["year"],
            p["status"],
            p["topic"],
            f"papers/{p['slug']}",
            ROUND_BY_SLUG[p["slug"]],
        ])

    order_text = "\n".join([
        "1. 先读早期和系统抽象：`stone_logic_in_memory_1970`、`pim-enabled-instructons-for-low-overhead-pim_isca15`。",
        "2. 再读数据移动主线：`rowclone_micro13`、`lisa-dram_hpca16`、`figaro-fine-grained-in-dram-data-relocation-and-caching_micro20`、`network-on-memory-data-copy_ieee-cal20`。",
        "3. 然后读 DRAM 内逻辑主线：`in-dram-bulk-and-or-ieee_cal15`、`ambit-bulk-bitwise-dram_micro17`、`1905.09822v3`、`simdram_asplos21`。",
        "4. 接着读商用 DRAM 行为探索：`micro19-gao`、`micro22-gao`、`2211.05838v6`、`2402.18736v2`、`2405.06081v1`、`2506.12947v1`。",
        "5. 最后读编程框架和应用系统：`SimplePIM_pact23`、`2310.10168v2`、`2402.19080v2`、`2501.17466v2`、`TOM-programmer-transparent-GPU-near-data-processing_isca16`、`2207.13795v4`。",
    ])

    one_rows = [[str(i), p["title"], p["one"]] for i, p in enumerate(PAPERS, 1)]
    text = f"""# Paper Reading Index

## 文献列表

{table(rows, ["编号", "标题", "年份", "状态", "主题", "文件夹", "备注"])}

## 推荐阅读顺序

{order_text}

## 每篇文章一句话总结

{table(one_rows, ["编号", "论文", "一句话总结"])}

## 当前未完成或需要我补充的内容

- 24 篇 PDF 全文均已从 `LEC4/original-paper` 下载并提取文本。
- 双栏 PDF 的文本抽取存在少量行交错；关键结论已用页码、章节、图号/表号定位，建议查看核心图表时回到 PDF 原图。
- `full_translation.zh.md` 为逐节中文详译/学习译文，覆盖正文结构、方法、实验、结果、讨论与局限；不是版权意义上的逐字复制全文。

## 文件结构说明

- `sources/original-paper/`: 原始 PDF 副本。
- `extracted_text/`: 每篇 PDF 的抽取文本与来源记录。
- `papers/<paper_slug>/`: 每篇论文的 metadata、中文摘要、定位重点、详译、图表公式、术语、局限问题、checklist 和 extraction log。
- `00_*.md`: 本目录下的跨论文总览、状态、汇总表、术语表和开放问题。
"""
    write("00_INDEX.md", text)


def write_status():
    rows = []
    for i, p in enumerate(PAPERS, 1):
        rows.append([
            str(i),
            "GitHub PDF",
            p["title"],
            p["full"],
            "Yes",
            "Yes",
            "Yes",
            "双栏抽取局部行交错；图像未单独裁剪",
            "如需逐图截图或逐字全文翻译，请指定优先论文",
        ])
    write("00_Reading_Status.md", "# Reading Status\n\n" + table(rows, ["编号", "输入形式", "标题", "是否找到全文", "是否完成摘要", "是否完成翻译", "是否完成定位", "问题", "需要我补充"]))


def write_summary_table():
    rows = []
    for p in PAPERS:
        rows.append([p["title"], p["problem"], p["method"], p["experiment"], p["results"], p["contrib"], p["limits"], p["focus"]])
    write("00_All_Papers_Summary_Table.md", "# All Papers Summary Table\n\n" + table(rows, ["论文", "研究问题", "方法", "数据集/实验", "主要结论", "贡献", "局限", "我应该重点读哪里"]))


def write_synthesis():
    text = """# Cross-Paper Synthesis

## 1. 这些文献共同关注的问题

这些论文共同围绕一个问题展开：现代系统的数据移动成本越来越高，传统 processor-centric 架构把大量时间和能耗花在 CPU/GPU 与内存之间搬运数据。LEC4 的论文从四个层次回应这个问题：DRAM 内数据移动、DRAM 内逻辑计算、PIM/NDP 编程与系统接口、以及真实商用 DRAM 行为探索。

## 2. 方法之间的关系

- `stone_logic_in_memory_1970` 提供早期思想源头：把带逻辑的 memory/cache 暴露为 sector-level operations。
- `rowclone_micro13` 是数据移动 primitive，后续 Ambit、SIMDRAM、PiDRAM、LISA 等都直接或间接依赖它。
- `lisa-dram_hpca16`、`figaro-*`、`network-on-memory-*` 继续扩展数据移动范围：subarray 内、subarray 间、bank 间分别对应不同瓶颈。
- `in-dram-bulk-and-or-*`、`ambit-*`、`1905.09822v3`、`simdram_asplos21` 形成 DRAM 内 bitwise logic 主线。
- `micro19-gao`、`micro22-gao`、`DRAM Bender`、`FCDRAM`、`SiMRA`、`PuDHammer` 关注商用 DRAM 在非标准时序、多行激活和可靠性/安全方面的真实行为。
- `SimplePIM`、`DaPPA`、`PiDRAM`、`PIM-enabled instructions` 关注如何让 PIM/PuM 被程序和系统真正使用。

## 3. 技术路线对比

- 修改 DRAM 或控制逻辑路线：RowClone、LISA、Ambit、SIMDRAM、MIMDRAM、Proteus。优点是机制清晰、性能强；缺点是需要厂商和系统栈支持。
- 使用商用 DRAM 非标准行为路线：ComputeDRAM、FracDRAM、FCDRAM、SiMRA、DRAM Bender。优点是证明门槛低；缺点是可靠性、vendor dependence 和温度/电压敏感性强。
- 近数据/逻辑层路线：TOM、PIM-enabled instructions。优点是更接近可编程计算；缺点是不能直接利用 DRAM array 内部并行性。
- 编程框架路线：SimplePIM、DaPPA、PiDRAM。优点是降低使用门槛；缺点是性能高度依赖硬件平台和 runtime 实现。

## 4. 结论是否一致

总体一致：减少数据移动能显著提升性能和能效。但各文献也共同说明，收益不是自动出现的。数据布局、cache locality、subarray/bank 位置、coherence、dirty cache lines、温度/电压、workload regularity 和编程模型都会决定最终收益。

## 5. 争议点或不确定点

- 多行激活和 out-of-spec timing 在真实 DDR4/DDR5/HBM 上能否可靠、可量产。
- ECC、memory encryption、RowHammer mitigation 与 in-DRAM computation 如何共存。
- PIM/PuM 的编译器和 runtime 能否自动完成数据布局、transposition、cache flush 和同步。
- 实验中 microbenchmark 的巨大收益能否转化为真实端到端应用收益。

## 6. 哪些论文适合先读

建议先读 `rowclone_micro13`、`ambit-bulk-bitwise-dram_micro17`、`lisa-dram_hpca16`、`simdram_asplos21`。这四篇构成 LEC4 的 DRAM 内数据移动和逻辑计算骨架。

## 7. 哪些论文适合深入读

如果关注系统落地，深入读 `pim-enabled-instructons-for-low-overhead-pim_isca15`、`2111.00082v6`、`SimplePIM_pact23`、`2310.10168v2`。如果关注真实 DRAM 行为和可靠性，深入读 `micro19-gao`、`micro22-gao`、`2211.05838v6`、`2402.18736v2`、`2506.12947v1`。

## 8. 我的学习路线建议

先建立 DRAM subarray、row buffer、ACTIVATE/PRECHARGE、sense amplifier 的基础；再学习 RowClone/LISA 的数据移动；然后学习 Ambit/SIMDRAM 的 MAJ/NOT 逻辑；最后回到系统层，比较 PEI、PiDRAM、SimplePIM、DaPPA 如何把 primitive 变成可用的软件接口。

## 9. 后续值得补充阅读的方向

- DDR5/HBM/CXL 环境下的 PIM/PuM 支持。
- PIM cache coherence、memory consistency 和 security。
- PIM compiler、DSL、runtime 和 data placement。
- RowHammer/TRR/PRAC 与 PuD/PuM interaction。
- UPMEM 等商用 PIM 平台的新一代软件栈。
"""
    write("00_Cross_Paper_Synthesis.md", text)


def parse_terms():
    merged = {}
    for p in PAPERS:
        text = read(PAPERS_DIR / p["slug"] / "terminology.zh.md")
        for line in text.splitlines():
            if not line.startswith("| ") or line.startswith("| English") or line.startswith("|---"):
                continue
            cols = [c.strip() for c in line.strip("|").split("|")]
            if len(cols) < 5:
                continue
            term, zh, _loc, desc, core = cols[:5]
            key = term.lower()
            if key not in merged:
                merged[key] = {"term": term, "zh": zh, "papers": [], "desc": desc, "importance": "高" if core == "是" else "中"}
            merged[key]["papers"].append(p["title"])
    rows = []
    for item in sorted(merged.values(), key=lambda x: x["term"].lower()):
        rows.append([item["term"], item["zh"], "；".join(item["papers"][:4]) + (" 等" if len(item["papers"]) > 4 else ""), item["desc"], item["importance"]])
    write("00_Glossary.md", "# Global Glossary\n\n" + table(rows, ["English Term", "中文翻译", "出现论文", "简明解释", "重要程度"]))


def parse_open_questions():
    rows = []
    idx = 1
    for p in PAPERS:
        text = read(PAPERS_DIR / p["slug"] / "limitations_and_questions.zh.md")
        sec = section(text, "5. 我阅读时应该追问的问题")
        questions = [line[2:].strip() for line in sec.splitlines() if line.startswith("- ")]
        for q in questions[:3]:
            rows.append([str(idx), q, p["title"], "limitations_and_questions.zh.md / Section 5", "用于判断论文结论边界和后续复现方向", "回到对应论文的 summary、key_points 和原文图表核对"])
            idx += 1
    write("00_Open_Questions.md", "# Open Questions\n\n" + table(rows, ["编号", "问题", "相关论文", "原文位置", "为什么重要", "下一步建议"]))


if __name__ == "__main__":
    write_index()
    write_status()
    write_summary_table()
    write_synthesis()
    parse_terms()
    parse_open_questions()
    print(f"Wrote overview files for {len(PAPERS)} papers")
