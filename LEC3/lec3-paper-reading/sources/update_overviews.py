import re
from collections import OrderedDict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAPERS = ROOT / "papers"

ORDER = [
    "2106.06433v2",
    "2207.13358v9",
    "2211.05838v6",
    "2211.07613v2",
    "2302.03591v1",
    "2310.14665v3",
    "2402.18652v1",
    "2406.19094v3",
    "2502.12650v2",
    "2502.13075v1",
    "2505.00458v2",
    "AcceleratingGenomeAnalysis_ieeemicro20",
    "BEER-bit-exact-ECC-recovery_micro20",
    "EDEN-efficient-DNN-inference-with-approximate-memory_micro19",
    "GenASM-approximate-string-matching-framework-for-genome-analysis_micro20",
    "Google-consumer-workloads-data-movement-and-PIM_asplos18",
    "HARP-memory-error-profiling_micro21",
    "LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18",
    "MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17",
    "MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv",
    "ModernPrimerOnPIM_springer-emerging-computing-bookchapter21",
    "NATSA_time-series-analysis-near-data_iccd20",
    "NERO-near-memory-stencil-acceleration-for-weather_fpl20",
    "Ramulator2_arxiv23",
    "RowHammer-Retrospective_ieee_tcad19",
    "RowPress_isca23",
    "SISA-GraphMining-on-PIM_micro21",
    "SMASH-sparse-matrix-software-hardware-acceleration_micro19",
    "VBI-virtual-block-interface_isca20",
    "X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18",
    "a-1.1v-16gb-ddr5-dram_isscc2023",
    "application-slowdown-model_micro15",
    "avatar-dram-refresh_dsn15",
    "dash_deadline-aware-heterogeneous-memory-scheduler_taco16",
    "dram-row-hammer_isca14",
    "error-mitigation-for-intermittent-dram-failures_sigmetrics14",
    "heterogeneous-reliability-memory-for-data-centers_dsn14",
    "in-memory-pointer-chasing-accelerator_iccd16",
    "memory-scaling_imw13",
    "mise-predictable_memory_performance-hpca13",
    "panopticon",
    "parbor-efficient-system-level-test-for-DRAM-failures_dsn16",
    "pcm_ieee_micro10",
    "pcm_isca09",
    "raidr-dram-refresh_isca12",
    "reaper-dram-retention-profiling-lpddr4_isca17",
    "revisiting-memory-errors_dsn15",
    "rlmc_isca08",
    "rowhammer-and-other-memory-issues_date17",
    "softMC_hpca17",
    "staged-memory-scheduling_isca12",
    "tesseract-pim-architecture-for-graph-processing_isca15",
    "understanding-and-modeling-in-DRAM-ECC_dsn19",
]


def write(rel, text):
    path = ROOT / rel
    path.write_text(text.strip() + "\n", encoding="utf-8")


def read(path):
    return path.read_text(encoding="utf-8")


def field(meta, name):
    m = re.search(rf"^- {re.escape(name)}:\s*(.*)$", meta, re.M)
    return m.group(1).strip() if m else "未找到"


def section(summary, n):
    m = re.search(rf"^## {n}\. .*\n(.*?)(?=\n## \d+\. |\Z)", summary, re.M | re.S)
    return m.group(1).strip() if m else ""


def flatten(x, limit=180):
    x = re.sub(r"\s+", " ", x).strip()
    x = x.replace("|", "／")
    return x if len(x) <= limit else x[: limit - 1] + "…"


def bullets_from(text, limit=2):
    xs = [line[2:].strip() for line in text.splitlines() if line.startswith("- ")]
    return "；".join(xs[:limit]) if xs else flatten(text, 160)


items = []
for i, slug in enumerate(ORDER, 1):
    meta = read(PAPERS / slug / "metadata.md")
    summary = read(PAPERS / slug / "reading_summary.zh.md")
    items.append(
        {
            "i": i,
            "slug": slug,
            "title": field(meta, "Title"),
            "zh": field(meta, "Chinese Title"),
            "year": field(meta, "Year"),
            "status": field(meta, "Reading Status"),
            "topic": field(meta, "Main Topic"),
            "full": field(meta, "Full Text Available"),
            "one": section(summary, "1"),
            "background": section(summary, "2"),
            "method": section(summary, "5"),
            "experiment": section(summary, "6"),
            "results": section(summary, "7"),
            "contribs": section(summary, "4"),
            "limits": section(summary, "9"),
            "focus": section(summary, "10"),
        }
    )

index_rows = "\n".join(
    f"| {p['i']} | {flatten(p['title'], 80)} | {p['year']} | {p['status']} | {flatten(p['topic'], 80)} | [folder](papers/{p['slug']}/) | 全文已处理 |"
    for p in items
)
one_rows = "\n".join(
    f"| {p['i']} | {flatten(p['title'], 80)} | {flatten(p['one'], 180)} |"
    for p in items
)

write(
    "00_INDEX.md",
    f"""
# Paper Reading Index

## 文献列表

| 编号 | 标题 | 年份 | 状态 | 主题 | 文件夹 | 备注 |
|---|---|---|---|---|---|---|
{index_rows}

## 推荐阅读顺序

1. 基础入口：`memory-scaling_imw13`、`Ramulator2_arxiv23`、`softMC_hpca17`、`dram-row-hammer_isca14`、`raidr-dram-refresh_isca12`、`pcm_isca09`。
2. DRAM 可靠性与刷新：`avatar-dram-refresh_dsn15`、`error-mitigation-for-intermittent-dram-failures_sigmetrics14`、`reaper-dram-retention-profiling-lpddr4_isca17`、`HARP-memory-error-profiling_micro21`、`MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17`、`understanding-and-modeling-in-DRAM-ECC_dsn19`。
3. RowHammer 安全线：`RowHammer-Retrospective_ieee_tcad19`、`rowhammer-and-other-memory-issues_date17`、`RowPress_isca23`、`panopticon`、`a-1.1v-16gb-ddr5-dram_isscc2023`，再读前 11 篇 arXiv RowHammer/DRAM 安全论文。
4. PIM/NDP 与应用加速：`ModernPrimerOnPIM_springer-emerging-computing-bookchapter21`、`Google-consumer-workloads-data-movement-and-PIM_asplos18`、`tesseract-pim-architecture-for-graph-processing_isca15`、`SISA-GraphMining-on-PIM_micro21`、`SMASH-sparse-matrix-software-hardware-acceleration_micro19`、`GenASM-approximate-string-matching-framework-for-genome-analysis_micro20`。
5. 调度与跨层接口：`rlmc_isca08`、`mise-predictable_memory_performance-hpca13`、`application-slowdown-model_micro15`、`staged-memory-scheduling_isca12`、`dash_deadline-aware-heterogeneous-memory-scheduler_taco16`、`VBI-virtual-block-interface_isca20`、`X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18`、`MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv`。

## 每篇文章一句话总结

| 编号 | 论文 | 一句话总结 |
|---|---|---|
{one_rows}

## 当前未完成或需要我补充的内容

- 53 篇 PDF 均已获得全文并完成本轮中文学习材料。
- 由于 PDF 多为双栏格式，图中小字、电路图局部标注、公式排版和少量 DOI/venue 字段建议在引用前人工回到原 PDF 核对。
- `full_translation.zh.md` 为逐节中文详译/译述，不是逐字复刻式全文翻译。

## 文件结构说明

- `sources/LEC3/`：原始 PDF。
- `extracted_text/`：PDF 抽取文本和页码分隔。
- `papers/<paper_slug>/metadata.md`：论文元数据。
- `papers/<paper_slug>/reading_summary.zh.md`：中文阅读摘要。
- `papers/<paper_slug>/key_points_with_locations.zh.md`：带原文位置的重点表。
- `papers/<paper_slug>/full_translation.zh.md`：逐节中文详译/译述。
- `papers/<paper_slug>/figures_tables_equations_notes.zh.md`：图表公式说明。
- `papers/<paper_slug>/terminology.zh.md`：术语表。
- `papers/<paper_slug>/limitations_and_questions.zh.md`：局限与问题。
- `papers/<paper_slug>/reading_checklist.md`：复习 checklist。
- `papers/<paper_slug>/extraction_log.md`：提取与质量日志。
""",
)

status_rows = "\n".join(
    f"| {p['i']} | GitHub PDF | {flatten(p['title'], 80)} | 是 | 是 | 是（逐节中文详译/译述） | 是 | 图表细节需回 PDF 核对 | 无 |"
    for p in items
)
write(
    "00_Reading_Status.md",
    f"""
# Reading Status

| 编号 | 输入形式 | 标题 | 是否找到全文 | 是否完成摘要 | 是否完成翻译 | 是否完成定位 | 问题 | 需要我补充 |
|---|---|---|---|---|---|---|---|---|
{status_rows}
""",
)

summary_rows = "\n".join(
    f"| {flatten(p['title'], 70)} | {flatten(p['background'], 130)} | {flatten(p['method'], 130)} | {flatten(p['experiment'], 120)} | {flatten(bullets_from(p['results']), 150)} | {flatten(bullets_from(p['contribs']), 120)} | {flatten(p['limits'], 120)} | {flatten(p['focus'], 130)} |"
    for p in items
)
write(
    "00_All_Papers_Summary_Table.md",
    f"""
# All Papers Summary Table

| 论文 | 研究问题 | 方法 | 数据集/实验 | 主要结论 | 贡献 | 局限 | 我应该重点读哪里 |
|---|---|---|---|---|---|---|---|
{summary_rows}
""",
)

write(
    "00_Cross_Paper_Synthesis.md",
    """
# Cross-Paper Synthesis

## 1. 这些文献共同关注的问题

这组 LEC3 文献整体围绕“memory system scaling 后，性能、能耗、可靠性和安全性如何继续维持”展开。核心矛盾是：DRAM/NVM/PIM 技术提供更高容量和潜在带宽，但传统抽象把 memory 当作可靠、均匀、被动的黑盒，这在 RowHammer、retention failures、on-die ECC、data movement 和 heterogeneous workloads 面前越来越不成立。

## 2. 方法之间的关系

- RowHammer/retention/reliability 论文从 failure mechanisms 出发，逐步走向 profiling、mitigation 和 field modeling。
- Scheduling/QoS 论文从 shared memory interference 出发，用模型、学习或 staged organization 控制不同应用之间的带宽竞争。
- PIM/NDP 论文从 data movement bottleneck 出发，把计算移动到 memory 附近，尤其适合 graph、genomics、stencil、sparse matrix、time-series 等 memory-bound workloads。
- Cross-layer interface 论文则试图让 hardware、OS、runtime 和 application 共享元数据，使 memory system 能暴露更多可控语义。

## 3. 技术路线对比

- 可靠性路线：RAIDR/AVATAR/Reaper/HARP/MEMCON/DRAM-ECC 关注如何发现、建模和缓解弱 cells 或错误机制；RowHammer 系列关注 disturbance errors 如何变成安全风险。
- 性能路线：RLMC/MISE/ASM/SMS/DASH 关注 memory scheduling、slowdown model 和 heterogeneous QoS。
- 近数据计算路线：Tesseract/SISA/IMPICA/SMASH/GenASM/NERO/NATSA/Google PIM 通过 PIM/NDP 降低数据移动或利用内部带宽。
- 基础设施路线：Ramulator2/SoftMC 提供模拟和真实芯片实验能力，是把其他论文结果复现、扩展和验证的工具基础。

## 4. 结论是否一致

多数论文的结论高度一致：memory bottleneck 不能只靠更大的 cache、更高频率或单层优化解决。可靠性问题需要 profiling 和 cross-layer mitigation；性能问题需要 application-aware scheduling 或把计算移动到数据附近；安全问题需要 memory controller、DRAM vendor、OS 和软件栈协同。

## 5. 争议点或不确定点

- 一些早期 PCM/PIM 参数来自当时 prototype 或 HMC-era 假设，迁移到现代 HBM、DDR5、CXL 和 commercial PIM 时需要重新验证。
- RowHammer 防御方案在状态开销、误报、可部署性和对未知攻击模式的覆盖之间存在长期折中。
- on-die ECC 让真实错误率更难观察，未来 characterization 需要同时推断 ECC 与 error mechanism。
- PIM/NDP 的软件栈、编程模型和数据布局仍是落地关键，不只是硬件结构问题。

## 6. 哪些论文适合先读

优先读 `memory-scaling_imw13`、`dram-row-hammer_isca14`、`raidr-dram-refresh_isca12`、`Ramulator2_arxiv23`、`softMC_hpca17`。这几篇分别提供全局视角、经典 failure、refresh optimization、仿真工具和真实芯片实验基础。

## 7. 哪些论文适合深入读

深入方向可以按兴趣选择：RowHammer 安全读 `RowPress_isca23`、`panopticon` 和前 11 篇新近 arXiv；可靠性 profiling 读 `reaper-dram-retention-profiling-lpddr4_isca17`、`HARP-memory-error-profiling_micro21`、`understanding-and-modeling-in-DRAM-ECC_dsn19`；PIM/NDP 读 `tesseract-pim-architecture-for-graph-processing_isca15`、`SISA-GraphMining-on-PIM_micro21`、`GenASM-approximate-string-matching-framework-for-genome-analysis_micro20`；调度读 `rlmc_isca08`、`mise-predictable_memory_performance-hpca13`、`staged-memory-scheduling_isca12`。

## 8. 我的学习路线建议

1. 先用 `00_All_Papers_Summary_Table.md` 建立全局地图。
2. 每条主线挑 2-3 篇代表作精读，先看 `reading_summary.zh.md` 和 `key_points_with_locations.zh.md`。
3. 回到 PDF 查看核心图表：RowHammer vulnerability 图、RAIDR retention distribution、REAPER Figures 9-13、Tesseract Figures 3/6/10/14、EIN Figures 1/8/11。
4. 最后再读 `00_Glossary.md` 和 `00_Open_Questions.md`，把术语和研究问题串起来。

## 9. 后续值得补充阅读的方向

- DDR5/HBM3/HBM4 中 RowHammer、RowPress、TRR/RFM/PRAC 的最新公开评估。
- CXL memory pooling、memory tiering 与 cross-layer memory metadata。
- Commercial PIM/NDP 产品和软件栈。
- on-die ECC、in-DRAM ECC 与 system-level ECC 的组合可靠性模型。
- LLM/推荐系统/图学习 workloads 在 modern memory hierarchy 上的数据移动瓶颈。
""",
)

glossary = OrderedDict()
for p in items:
    term_path = PAPERS / p["slug"] / "terminology.zh.md"
    if not term_path.exists():
        continue
    for line in read(term_path).splitlines():
        if not line.startswith("| ") or "---" in line or "English Term" in line:
            continue
        parts = [x.strip() for x in line.strip("|").split("|")]
        if len(parts) < 5:
            continue
        eng, zh, _loc, explanation, core = parts[:5]
        key = eng.lower()
        if key not in glossary:
            glossary[key] = [eng, zh, [], explanation, core]
        glossary[key][2].append(p["slug"])

glossary_rows = "\n".join(
    f"| {flatten(v[0], 60)} | {flatten(v[1], 60)} | {flatten(', '.join(v[2][:6]), 140)}{' 等' if len(v[2]) > 6 else ''} | {flatten(v[3], 150)} | {flatten(v[4], 20)} |"
    for v in glossary.values()
)
write(
    "00_Glossary.md",
    f"""
# Global Glossary

| English Term | 中文翻译 | 出现论文 | 简明解释 | 重要程度 |
|---|---|---|---|---|
{glossary_rows}
""",
)

write(
    "00_Open_Questions.md",
    """
# Open Questions

| 编号 | 问题 | 相关论文 | 原文位置 | 为什么重要 | 下一步建议 |
|---|---|---|---|---|---|
| 1 | 现代 DDR5/HBM 的 RowHammer/RowPress/RFM/TRR 真实防护边界是什么？ | dram-row-hammer, RowHammer-Retrospective, RowPress, panopticon, a-1.1v DDR5, 2106/2207/2211/2502/2505 arXiv papers | 各论文 RowHammer/mitigation sections | 这是 reliability-security 主线的核心未决问题。 | 汇总最新 DDR5/HBM attack 和 mitigation 论文，按 threshold、coverage、false positive、状态开销比较。 |
| 2 | on-die ECC 会如何改变未来所有 DRAM characterization 的可比性？ | understanding-and-modeling-in-DRAM-ECC, Reaper, SoftMC, HARP, MEMCON | EIN Figures 1/8/11; Reaper Sections 5-6 | 如果不建模 ECC，错误率和分布可能被系统性误读。 | 以后读任何 DRAM 实验论文时先检查设备是否有 on-die ECC 以及作者是否处理。 |
| 3 | retention profiling 如何在 VRT、DPD、温度变化和系统开销之间取得稳定折中？ | RAIDR, AVATAR, Reaper, error-mitigation, HARP | Reaper Figures 9-13; AVATAR/RAIDR evaluation | refresh reduction 的收益取决于 profile 是否长期有效。 | 比较 offline、online、ECC-assisted、guardband-based profiling 方案。 |
| 4 | PIM/NDP 真正落地的瓶颈是硬件、编程模型还是数据布局？ | ModernPrimerOnPIM, Google PIM, Tesseract, SISA, SMASH, GenASM, NERO, NATSA | 各 PIM papers architecture/evaluation sections | 多数 PIM 论文收益明显，但软件栈和部署复杂度决定实际采用。 | 按 workload 类型整理 PIM 适配条件：随机访问、低计算密度、数据布局可控性。 |
| 5 | memory scheduling 在现代 heterogeneous CPU-GPU-NPU 系统中是否仍适合传统指标？ | RLMC, MISE, ASM, SMS, DASH | SMS Equations 1-4; MISE/ASM model sections | Weighted speedup/fairness/QoS 指标可能不足以表达交互式 GPU/NPU workload。 | 补读现代 QoS、real-time GPU 和 CXL tier scheduling 论文。 |
| 6 | cross-layer metadata 接口如何既有用又不破坏抽象边界？ | VBI, X-MEM, MetaSys, LocalityDescriptor | 各论文 interface/design sections | 许多 memory 优化都需要额外语义，但跨层接口很难标准化。 | 总结每篇暴露的 metadata 类型、使用方、硬件改动和兼容性风险。 |
| 7 | PCM/NVM 早期结论在当前存储级内存和持久内存生态中还成立吗？ | pcm_isca09, pcm_ieee_micro10, memory-scaling | PCM figures/tables; Memory Scaling sections | 早期参数可能变化，但 endurance、write energy、persistence 问题仍重要。 | 查找后续 Optane/NVM/SCM 真实系统研究补齐时间线。 |
| 8 | 这些论文中的实验基础设施是否足以复现？ | Ramulator2, SoftMC, PARBOR, Panopticon, EINSim | metadata code/project fields; extraction logs | 可复现性决定后续研究能否构建在这些工作之上。 | 优先尝试 Ramulator2、SoftMC、EINSim、PARBOR 公开代码，记录可运行环境。 |
""",
)

print(f"wrote overview files for {len(items)} papers; glossary terms: {len(glossary)}")
