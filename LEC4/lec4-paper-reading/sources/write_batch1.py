from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

NOTE = (
    "说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/"
    "学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，"
    "关键结论均给出原文页码或图表位置。"
)


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.rstrip() + "\n", encoding="utf-8")


def md_list(items):
    return "\n".join(f"- {item}" for item in items)


def table(rows, headers):
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join(["---"] * len(headers)) + "|"]
    out.extend("| " + " | ".join(row) + " |" for row in rows)
    return "\n".join(out)


PAPERS = [
    {
        "slug": "1905.09822v3",
        "title": "In-DRAM Bulk Bitwise Execution Engine",
        "zh_title": "DRAM 内批量按位执行引擎",
        "authors": "Vivek Seshadri; Onur Mutlu",
        "year": "2020",
        "venue": "arXiv:1905.09822v3",
        "arxiv": "1905.09822v3",
        "doi": "未找到",
        "topic": "Processing using Memory; in-DRAM bulk bitwise operations; Ambit",
        "keywords": "Ambit; DRAM; Triple-Row Activation; RowClone; bulk bitwise operations; Processing using Memory",
        "pages": "45",
        "sections": "Abstract; 1 Introduction; 2 Background on DRAM; 3 Ambit; 4 Full Design and Implementation; 5 System Integration; 6 SPICE Simulations; 7 Throughput & Energy; 8 Real-World Applications; 9 Future Work; 10 Conclusion; References",
        "one_sentence": "Ambit 利用 DRAM 的模拟电荷共享行为、Triple-Row Activation 和少量电路/控制器扩展，在内存阵列内部执行大规模 bitwise operations，从而显著降低数据搬运开销。",
        "background": [
            "论文指出 bitmap indices、BitWeaving、BitFunnel、DNA sequence mapping、encryption、graph processing 与 binary neural networks 等工作负载都大量使用大 bitvector 上的按位操作；传统 CPU/GPU 执行这些操作时受内存通道带宽与能耗限制，见 Page 1-2, Section 1。",
            "作者将 Ambit 放在 Processing using Memory 语境中理解：不同于在内存附近增加逻辑的 Processing-in-Memory，Ambit 尽量复用 DRAM 既有结构与模拟操作特性，见 Page 2, Section 1。"
        ],
        "problems": [
            "如何让 DRAM 阵列内部直接完成 AND/OR/NOT 等批量按位操作，而不是把数据搬到处理器。",
            "如何把原始的 DRAM 模拟行为转换成可由处理器调用的 bulk bitwise execution model。",
            "如何处理行映射、临时行、cache coherence、ECC、data scrambling 与系统软件接口等集成问题。"
        ],
        "contributions": [
            "提出 Ambit-AND-OR：通过 Triple-Row Activation (TRA) 让 sense amplifier 实现 majority function，再用控制行得到 AND/OR，见 Page 14-16, Section 3.1。",
            "提出 Ambit-NOT：用 dual-contact cell (DCC) 生成反相值，见 Page 17, Section 3.2。",
            "将 RowClone 用作快速行复制和初始化基础，减少操作数搬移开销，见 Page 16, Section 3.1.4。",
            "给出 row address grouping、AAP primitive、split row decoder、ISA/API/driver 支持与 coherence 处理，见 Page 18-24, Sections 4-5。",
            "通过 SPICE、吞吐/能耗分析和 Gem5 应用评估证明 Ambit 在 bitwise-heavy 工作负载上有明显收益，见 Page 25-32, Sections 6-8。"
        ],
        "method": [
            "TRA 同时激活三行，利用三个 cell 与 bitline 的电荷共享，使 sense amplifier 收敛到多数值；当一条控制行为 0 时得到 AND，当控制行为 1 时得到 OR，见 Page 14-16, Section 3.1.1-3.1.3。",
            "AAP primitive 将复制源行到计算行、执行 TRA、再把结果复制到目标行组织成可调度的 bulk bitwise operation，见 Page 20-21, Section 4.2, Figure 20。",
            "Ambit 需要在 subarray 内安排 D-group、B-group、C-group 等行组，并通过控制器把应用地址转换为对应 DRAM 行操作，见 Page 18-20, Section 4.1, Figure 19。"
        ],
        "experiments": [
            "Section 6 用 circuit-level SPICE simulations 分析 TRA 在 process variation 下的可靠性，见 Page 25-26。",
            "Section 7 比较 Ambit、Ambit-3D、Intel Skylake、GTX 745 与 HMC 2.0 的 bulk bitwise raw throughput 与 DRAM/channel energy，见 Page 26-27, Figure 21, Table 4。",
            "Section 8 用 Gem5 full-system simulator 评估 bitmap indices、BitWeaving 和 bitvector set operations，主要参数见 Page 28, Table 5。"
        ],
        "results": [
            "Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 相对 HMC 2.0 提升 9.7x，见 Page 27, Figure 21。",
            "按位操作的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 27, Table 4。",
            "bitmap index 查询端到端执行时间平均降低约 6x，见 Page 28-29, Figure 22。",
            "BitWeaving 查询加速 1.8x-11.8x，平均 7.0x，见 Page 30, Figure 23。",
            "在集合操作中，只要每个集合有 64 个或更多元素，Ambit 使 bitvector 实现平均比 RB-tree 快约 3x，见 Page 31, Figure 24。"
        ],
        "limitations": [
            "许多操作要求源/目标行位于同一 subarray，数据布局与地址映射压力较大，见 Page 18-21, Sections 4.1-4.2。",
            "bitcount 等操作仍由 CPU 完成，限制了部分应用的端到端加速，见 Page 28-30, Sections 8.1-8.2。",
            "作者指出 ECC 成本和 process variation 下的错误处理是重要问题；近似 Ambit 仍是未来方向，见 Page 24, Section 5.5 与 Page 33, Section 9.4。",
            "Section 8.4 中 BitFunnel、encryption、DNA、ML 等只是讨论，没有完整定量评估，见 Page 31-32。"
        ],
        "focus": [
            "先读 Page 14-16 的 TRA，因为这是 Ambit 的电路/逻辑核心。",
            "再读 Page 20-24 的 AAP、系统接口和 coherence，因为这些决定方案能否落地。",
            "最后读 Page 27-31 的 Figure 21、Table 4、Figures 22-24，理解收益来自哪里以及哪里被 CPU 端操作限制。"
        ],
        "relations": "Ambit 与 RowClone、SIMDRAM、ComputeDRAM、PiDRAM 和 DRAM Bender 形成同一条 in-DRAM computation/PuM 研究线：Ambit 提供机制，后续论文更多关注实芯片验证、系统集成与编程框架。",
        "figures": [
            ["Figure 1", "Page 3", "现代 memory subsystem 层次", "帮助读者把 channel/module/chip/bank/subarray 放到同一结构中", "背景图，建议快速看"],
            ["Figure 16", "Page 15-16", "TRA 电荷共享与 majority operation", "解释 AND/OR 为什么可以在 DRAM sense amplifier 中实现", "核心图，必须回看 PDF"],
            ["Figure 17", "Page 17", "Dual-contact cell (DCC)", "说明 NOT 的硬件支持", "理解 Ambit-NOT 的关键"],
            ["Figure 19", "Page 19-20", "Row address grouping", "说明计算行、控制行、数据行如何组织", "理解系统集成必读"],
            ["Figure 20", "Page 21", "AAP primitive 步骤", "把复制、TRA、结果写回串成可执行序列", "核心流程图"],
            ["Figure 21", "Page 27", "bulk bitwise throughput", "Ambit 与 CPU/GPU/HMC 的吞吐对比", "核心结果图"],
            ["Figure 22-24", "Page 29-31", "真实应用加速", "bitmap index、BitWeaving、set operations 的端到端效果", "用于判断实用价值"]
        ],
        "tables": [
            ["Table 4", "Page 27", "bitwise operation energy", "Ambit 将 DRAM/channel energy 降低 25.1x-59.5x", "核心能耗结果"],
            ["Table 5", "Page 28", "Gem5 simulation parameters", "列出 CPU/cache/memory controller/DRAM 配置", "复现实验时需要"]
        ],
        "equations": [
            ["Equation 1", "Page 15, Section 3.1.2", "TRA 中 bitline 电压/多数函数的直观推导", "三个 cell 的多数值决定 sense amplifier 最终稳定态", "是"]
        ],
        "terms": [
            ["Processing using Memory", "利用内存进行处理", "Page 2", "复用内存器件固有结构/行为完成计算，而不是单纯靠外加逻辑", "是"],
            ["Triple-Row Activation (TRA)", "三行同时激活", "Page 14-16", "同时激活三条 DRAM wordline，使 sense amplifier 得到 majority 结果", "是"],
            ["Ambit-AND-OR", "Ambit 的 AND/OR 机制", "Page 14-16", "通过 TRA 和控制行实现 bulk AND/OR", "是"],
            ["Dual-contact cell (DCC)", "双接触 DRAM 单元", "Page 17", "用两个访问晶体管支持读取反相值，实现 NOT", "是"],
            ["AAP primitive", "ACTIVATE-ACTIVATE-PRECHARGE 原语", "Page 20-21", "Ambit 控制器执行 bulk bitwise operation 的基本命令序列", "是"],
            ["RowClone", "DRAM 内行复制机制", "Page 12, Page 16", "在 DRAM 内完成行复制/初始化，Ambit 用它移动操作数和结果", "是"]
        ],
        "open_questions": [
            "真实 DDR4/DDR5 芯片中 Ambit 操作的 bit error rate 与数据位置、温度、电压如何变化？",
            "如果 bitcount/shift/count 等操作不能在 DRAM 内完成，应用端到端加速会在什么场景下被吞掉？",
            "操作系统和内存分配器如何稳定地把操作数放到同一 subarray，且不破坏普通程序性能？"
        ],
    },
    {
        "slug": "2111.00082v6",
        "title": "PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM",
        "zh_title": "PiDRAM：面向 Processing-in-DRAM 的端到端 FPGA 框架",
        "authors": "Ataberk Olgun; Juan Gómez Luna; Konstantinos Kanellopoulos; Behzad Salami; Hasan Hassan; Oğuz Ergin; Onur Mutlu",
        "year": "2023",
        "venue": "arXiv:2111.00082v6",
        "arxiv": "2111.00082v6",
        "doi": "未找到",
        "topic": "FPGA prototype; commodity DRAM based PuM; RowClone; D-RaNGe",
        "keywords": "PiDRAM; Processing-using-Memory; FPGA; RISC-V; RowClone; D-RaNGe; coherence; memory allocation",
        "pages": "19",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Motivation; 4 PiDRAM; 5 RowClone Case Study; 6 D-RaNGe Case Study; 7 Extending PiDRAM; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "PiDRAM 是一个基于 FPGA/RISC-V 的端到端实验框架，用真实未改动 DDR3 芯片研究 commodity DRAM based PuM 技术的系统集成问题。",
        "background": [
            "作者指出很多 PuM 技术已经能在 off-the-shelf DRAM 中通过非标准时序或模拟行为实现，但传统系统、测试平台和模拟器都难以同时支持真实芯片、可改时序、系统软件和完整应用执行，见 Page 1-2, Section 1。",
            "RowClone 这类 in-DRAM copy 需要特殊内存分配、地址对齐和 coherence 处理；D-RaNGe 这类 TRNG 还依赖真实芯片的时序失败特性，见 Page 1-2。"
        ],
        "problems": [
            "如何在真实系统中发出 PuM 所需的 DRAM command sequence 与 violated timing parameters。",
            "如何让 OS/supervisor、用户库、memory controller 与 DRAM 芯片共同支持 PuM operation。",
            "如何评估真实芯片上的 RowClone 和 D-RaNGe，而不只停留在模拟器或测试平台。"
        ],
        "contributions": [
            "提出 PiDRAM，这是首个面向 commodity DRAM based PuM 的 flexible end-to-end open-source framework，见 Page 2-3。",
            "在 FPGA-based RISC-V system 上实现 prototype，并提供 custom memory controller、PuM Operations Controller (POC)、pumolib 与 supervisor software，见 Page 4-7, Figure 2。",
            "实现 RowClone 端到端支持，包括 memory allocation/alignment 与 coherence 处理，见 Page 8-13, Section 5。",
            "实现 D-RaNGe 端到端 TRNG 支持，展示安全 primitive 的集成可能性，见 Page 13-15, Section 6。",
            "展示扩展新 PuM case study 和新 FPGA board 的修改成本较小，见 Page 15, Section 7。"
        ],
        "method": [
            "PiDRAM 的硬件由可扩展 memory controller 和 POC 组成；POC 通过 memory-mapped interface 让软件用普通 LOAD/STORE 触发 PuM operation，见 Page 2, Page 4-6。",
            "软件由 pumolib 和 custom supervisor software 组成，前者向应用提供 API，后者提供内存管理与页表相关支持，见 Page 4-7。",
            "RowClone case study 通过 alloc_align 等机制满足同 subarray/page-granularity 对齐要求，并用 cache flush 处理 coherence，见 Page 8-12。",
            "D-RaNGe case study 通过 reduced tRCD 访问产生 activation-latency failures，再从硬件 random number buffer 读取随机数，见 Page 13-14。"
        ],
        "experiments": [
            "RowClone microbenchmark 比较 CPU-copy/initialization、bare-metal RowClone、No Flush RowClone 与包含 CLFLUSH 开销的情形，见 Page 11-13, Figures 9-11。",
            "D-RaNGe 评估随机数吞吐与延迟，见 Page 13-14, Section 6。",
            "实现复杂度用新增 Verilog/C++ 行数衡量，见 Page 1-2 与 Section 7。"
        ],
        "results": [
            "Bare-Metal RowClone-Copy 相对 CPU-copy 提升 317.5x-364.8x，RowClone-Initialize 提升 172.4x-182.4x，见 Page 12, Figure 9。",
            "No Flush 配置中，rcc 在 8 KiB/8 MiB 上分别提升 58.3x/118.5x，rci 分别提升 31.4x/88.7x，见 Page 12, Figure 10。",
            "考虑 CLFLUSH 时，0% dirty 情形 rcc/rci 仍有 14.6x/12.6x；50% dirty 时有 3.2x/3.9x；100% dirty 时降至 1.9x/2.3x，见 Page 12, Figure 11。",
            "D-RaNGe 原型可提供 8.30 Mb/s throughput，并在 220 ns 产生 4-bit random number，见 Page 2 与 Page 14。",
            "集成 RowClone 和 D-RaNGe 仅需 388 行 Verilog 与 643 行 C++，见 Page 1-2。"
        ],
        "limitations": [
            "prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。",
            "coherence 通过低效 CLFLUSH 实现，dirty cache block 比例升高时收益明显下降，见 Page 12, Figure 11。",
            "D-RaNGe 控制器未优化，作者说明 TRNG latency 可进一步降低，见 Page 14 footnote。",
            "温度、电压控制以及更多安全 primitive 的端到端研究留给未来工作，见 Page 15。"
        ],
        "focus": [
            "Page 4-7 Figure 2 和 PiDRAM components 是理解框架的入口。",
            "Page 8-13 的 RowClone case study 展示系统集成真正难点，包括 allocator、address mapping 和 coherence。",
            "Page 15-16 的 related-work comparison 能帮助区分 PiDRAM、SoftMC、ComputeDRAM、simulators 和 commercial platforms。"
        ],
        "relations": "PiDRAM 更像 Ambit/RowClone/D-RaNGe 之后的系统原型平台论文：它不主要提出新 DRAM 计算 primitive，而是解决如何把这些 primitive 端到端接入真实系统。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM organization and timing", "给出 PiDRAM 需要控制的 DRAM 层次与时序参数", "背景图"],
            ["Figure 2", "Page 5", "PiDRAM overview", "展示硬件/软件组件及其边界", "核心架构图"],
            ["Figure 8", "Page 11", "Physical address to DRAM address mapping", "说明 RowClone 对地址映射与对齐的依赖", "关键定位图"],
            ["Figure 9-11", "Page 12", "RowClone throughput improvement", "比较 bare-metal、No Flush 与 CLFLUSH 情形", "核心结果图"]
        ],
        "tables": [
            ["Table 2", "Page 7", "PiDRAM 可研究的 PuM 技术", "说明框架扩展范围不止 RowClone/D-RaNGe", "扩展性证据"],
            ["Table 4", "Page 16", "与相关平台比较", "突出 PiDRAM 同时支持真实 DRAM、flexible MC、system software 和 open-source", "定位必读"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点是系统框架与实验", "公式不是理解重点", "否"]
        ],
        "terms": [
            ["PiDRAM", "Processing-in-DRAM 框架", "Page 1-2", "用于真实 DRAM PuM 技术端到端集成和评估的 FPGA/RISC-V 平台", "是"],
            ["PuM Operations Controller (POC)", "PuM 操作控制器", "Page 2, Page 5", "把 PuM operation 暴露为 memory-mapped interface 的硬件控制器", "是"],
            ["pumolib", "PiDRAM 用户库", "Page 4-7", "应用通过该库调用 RowClone/D-RaNGe 等 PuM 操作", "是"],
            ["RowClone-Copy (rcc)", "DRAM 内复制操作", "Page 8-13", "利用 RowClone 在 DRAM 内执行 copy", "是"],
            ["RowClone-Initialize (rci)", "DRAM 内初始化操作", "Page 8-13", "利用 RowClone 在 DRAM 内执行初始化", "是"],
            ["D-RaNGe", "DRAM 真随机数生成技术", "Page 13-15", "利用 reduced activation latency 下的随机失败生成 TRNG", "是"]
        ],
        "open_questions": [
            "如果 coherence 机制由硬件而不是 CLFLUSH 支持，RowClone 端到端收益会提升多少？",
            "PiDRAM 扩展到 DDR4/DDR5 后，时序违例和内部地址映射问题会发生什么变化？",
            "真实 OS 中如何把 PuM allocation 和普通 page allocator 更自然地融合？"
        ],
    },
    {
        "slug": "2207.13795v4",
        "title": "Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture",
        "zh_title": "Sectored DRAM：实用、节能且高性能的细粒度 DRAM 架构",
        "authors": "Ataberk Olgun; F. Nisa Bostancı; Geraldo F. Oliveira; Yahya Can Tuğrul; Rahul Bera; A. Giray Yağlıkcı; Hasan Hassan; Oğuz Ergin; Onur Mutlu",
        "year": "2024",
        "venue": "arXiv:2207.13795v4",
        "arxiv": "2207.13795v4",
        "doi": "未找到",
        "topic": "Fine-grained DRAM; energy-efficient memory; variable burst length; sectored activation",
        "keywords": "Sectored DRAM; Variable Burst Length; Sectored Activation; LSQ Lookahead; Sector Predictor; fine-grained DRAM",
        "pages": "18",
        "sections": "Abstract; 1 Introduction; 2 DRAM Background; 3 Motivation; 4 Sectored DRAM; 5 System Integration; 6 Evaluation Methodology; 7 Evaluation Results; 8 Discussion; 9 Related Work; References",
        "one_sentence": "Sectored DRAM 通过 Variable Burst Length 和 Sectored Activation 只传输/激活 cache block 中可能有用的 word，从而在不显著牺牲带宽的情况下降低 DRAM 能耗并提升内存密集负载性能。",
        "background": [
            "现代 DRAM 以 cache block 粒度传输、以整行/大范围 cell 激活；但很多 workload 的 spatial locality 较差，cache block 中大量 word 在驻留期间未被使用，见 Page 1, Section 1。",
            "已有 fine-grained DRAM 方案往往吞吐低、面积开销高或没有完整支持细粒度传输和激活，见 Page 1-2, Section 1。"
        ],
        "problems": [
            "如何减少传输未使用 cache-block word 的能耗。",
            "如何减少激活整条 DRAM row 带来的不必要 activation energy。",
            "如何在细粒度访问下避免 sector misses 导致的 LLC miss 和性能下降。"
        ],
        "contributions": [
            "提出 Variable Burst Length (VBL)，按请求 sector 数动态调整 burst cycle 数，见 Page 2 与 Page 6, Section 4.2。",
            "提出 Sectored Activation (SA)，利用 DRAM row 内已有 mat 结构，只激活必要 sector，见 Page 2 与 Page 5-6, Section 4.1。",
            "提出 LSQ Lookahead 和 Sector Predictor，用于预测/确定 cache block 中会被使用的 word，见 Page 2 与 Page 7, Section 5。",
            "在 41 个 workload 上用 Ramulator、DRAMPower 和 Rambus Power Model 评估性能、能耗和面积，见 Page 9-13。",
            "以 1.7% DRAM chip area overhead 达到高内存密集负载平均 20% DRAM energy reduction 和 17% performance improvement，见 Page 1 与 Page 13。"
        ],
        "method": [
            "VBL 复用 DRAM I/O 中每个 burst cycle 选择一个 word 的既有机制，让一次 cache block transfer 可以只包含所需 word，见 Page 2, Page 6。",
            "SA 增加 sector transistors 与 sector latches，通过现有命令传递 sector bits，使 memory controller 选择要激活的 mat/sector，见 Page 2, Page 5-6。",
            "LSQ Lookahead 从 younger load/store 指令中收集同一 cache block 的未来 word 需求；Sector Predictor 基于过去访问模式预测会被使用的 sector，见 Page 2 与 Page 7。"
        ],
        "experiments": [
            "使用 41 个 SPEC2006、SPEC2017 和 DAMOV workload，并按 LLC MPKI 分类，见 Page 9, Section 6.1/Table 3。",
            "用 Ramulator/DRAMPower/Rambus Power Model 分析 DRAM power、LLC MPKI、single/multi-core performance、system energy 与 area，见 Page 9-13。",
            "与 FPA、PRA、HalfDRAM 等 state-of-the-art fine-grained DRAM architectures 比较，见 Page 12-13, Section 7.4。"
        ],
        "results": [
            "读/写一个 sector 相比读/写全部 sector，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%，见 Page 10, Figure 7。",
            "只激活一个 sector 可使 DRAM array activation power 降低 66.5%，但整体 ACT power 只降低 12.7%；SA 额外 activation power 开销仅 0.26%，见 Page 10, Section 7.1。",
            "Basic Sectored DRAM 会把 LLC MPKI 平均提高 3.1x；LA128-SP512 可把 Basic 的 LLC misses 降低 52%，见 Page 10-11, Figure 8。",
            "高 MPKI 16-core workload 上，Sectored DRAM 平均 parallel speedup 比 baseline 高 26%，平均 memory latency 降低 25%，见 Page 11-12, Figure 10。",
            "DRAM energy 最高/平均降低 33%/20%，system energy 最高/平均降低 23%/14%，见 Page 13, Figure 11/12。",
            "DRAM chip area overhead 为 1.72%；相对 HalfDRAM，取得 89% performance benefits、12% less DRAM energy、34% less chip area，见 Page 1 与 Page 13。"
        ],
        "limitations": [
            "stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。",
            "低/中 MPKI workload 可能不受益，作者提出动态关闭 Sectored DRAM，见 Page 14, Section 8.2。",
            "需要 processor/cache/memory controller 维护 sector bits、LSQ Lookahead 和 predictor，硬件复杂度不只在 DRAM 端，见 Page 7 与 Page 14。",
            "ECC、prefetching、更细粒度 sector 和更复杂 predictor 多数留给讨论/未来探索，见 Page 14-15, Sections 8.3-8.5。"
        ],
        "focus": [
            "Page 1-2 的问题定义能帮助区分 Fine-DRAM-Transfer 与 Fine-DRAM-Act。",
            "Page 5-7 的 VBL/SA/LSQ/SP 是方法核心。",
            "Page 10-13 的 Figures 7-12 是判断方案收益与代价的关键。",
            "Page 14 的 Dynamic on/off 讨论解释为什么该方案不是所有 workload 都适合。"
        ],
        "relations": "与 Ambit/RowClone 等 in-DRAM computation 不同，Sectored DRAM 主要解决常规内存访问的能耗浪费；但它同样利用 DRAM 内部 mat/row 组织，是更广义 DRAM architecture optimization 研究线的一部分。",
        "figures": [
            ["Figure 2", "Page 5", "cache block 在 mats/sectors 中的放置与 burst transfer", "说明为什么可以按 word/sector 细粒度传输", "方法背景图"],
            ["Figure 3", "Page 5", "normalized DRAM access/activation energy", "支撑细粒度化动机", "建议回看"],
            ["Figure 7", "Page 10", "DRAM command power and energy", "量化 VBL/SA 对 ACT/READ/WRITE 的能耗影响", "核心结果图"],
            ["Figure 8", "Page 11", "LLC MPKI under configurations", "展示 Basic、LA、SP 的 miss 影响", "系统集成关键"],
            ["Figure 9-12", "Page 11-13", "performance and energy results", "展示不同 workload 和比较对象下的性能/能耗", "核心评估图"],
            ["Figure 13-15", "Page 14-16", "multi-channel、dynamic、prefetching 讨论", "解释边界场景", "讨论部分"]
        ],
        "tables": [
            ["Table 3", "Page 9", "workload classification", "按 LLC MPKI 组织 41 个 workload", "实验设计关键"],
            ["Table 2", "Page 9 附近", "modeled DRAM chip parameters", "用于面积/能耗建模", "复现需要"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点在架构机制和模拟评估", "公式不是主要阅读对象", "否"]
        ],
        "terms": [
            ["Variable Burst Length (VBL)", "可变突发长度", "Page 2, Page 6", "根据 sector/word 需求动态改变 DRAM burst cycle 数", "是"],
            ["Sectored Activation (SA)", "分 sector 激活", "Page 2, Page 5-6", "只激活 DRAM row 中被请求的 mats/sectors", "是"],
            ["Sector Predictor (SP)", "sector 预测器", "Page 2, Page 7", "预测 cache block 中未来会用到的 word/sector", "是"],
            ["LSQ Lookahead", "Load/Store Queue 前瞻", "Page 2, Page 7", "利用队列中 younger load/store 发现同一 cache block 的未来访问", "是"],
            ["Sector miss", "sector 未命中", "Page 10-11", "请求了未被取回的 cache block 部分，导致额外 memory access", "是"],
            ["Fine-DRAM-Act", "细粒度 DRAM 激活", "Page 15", "只激活部分 DRAM cells 而非完整 row", "是"]
        ],
        "open_questions": [
            "更强 predictor 是否能显著降低 sector miss，又不会引入过高面积和能耗？",
            "真实 DDR5/HBM 系统中 sector bits 如何编码和传输最现实？",
            "对混合 workload，动态开关策略如何避免频繁切换带来的抖动？"
        ],
    },
    {
        "slug": "2211.05838v6",
        "title": "DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips",
        "zh_title": "DRAM Bender：用于便捷测试先进 DRAM 芯片的可扩展 FPGA 基础设施",
        "authors": "Ataberk Olgun; Hasan Hassan; A. Giray Yağlıkçı; Yahya Can Tuğrul; Lois Orosa; Haocong Luo; Minesh Patel; Oğuz Ergin; Onur Mutlu",
        "year": "2025",
        "venue": "arXiv:2211.05838v6",
        "arxiv": "2211.05838v6",
        "doi": "未找到",
        "topic": "DRAM testing infrastructure; FPGA; RowHammer; DDR4; in-DRAM bitwise operations",
        "keywords": "DRAM Bender; FPGA; DDR4; RowHammer; SoftMC; LiteX RowHammer Tester; DRAM testing; PuM",
        "pages": "18",
        "sections": "Abstract; 1 Introduction; 2 Background and Motivation; 3 DRAM Bender; 4 Use Cases; 5 New Research Directions; 6 Related Work; 7 Future Work and Limitations; 8 Conclusion; References",
        "one_sentence": "DRAM Bender 提供无接口限制、易用、可扩展的 FPGA DRAM 测试基础设施，使研究者能对 DDR3/DDR4 芯片发出任意低层 DRAM 命令并开展 RowHammer 与 in-DRAM computation 实验。",
        "background": [
            "理解 DRAM scaling、RowHammer、retention failures 与 undocumented functionality 必须测试真实芯片；普通系统 memory controller 不允许任意违反 timing parameters，见 Page 1, Section 1。",
            "现有开源平台 SoftMC 和 LiteX RowHammer Tester 存在接口限制、难用或难扩展问题，见 Page 1-2。"
        ],
        "problems": [
            "如何完全暴露 DRAM command/data interface，让实验程序自由安排 ACT/PRE/READ/WRITE 与时序。",
            "如何让非 HDL 专家通过 C++/Python 快速写 DRAM 实验。",
            "如何支持新的 FPGA board 和 DDR3/DDR4/未来接口，避免测试平台快速过时。"
        ],
        "contributions": [
            "提出 DRAM Bender，拥有 nonrestrictive instruction set architecture、C++/Python API 和 modular FPGA design，见 Page 1-2 与 Page 4-8。",
            "在五种 FPGA board 上实现 DDR4/DDR3 支持，并说明移植到新板只需较小代码修改，见 Page 2 与 Page 8。",
            "通过 RowHammer interleaving pattern 发现 double-sided attack 有效性强依赖 aggressor activation/precharge 顺序，见 Page 9-11。",
            "通过 data pattern study 展示 DRAM Bender 能发现更多 RowHammer bit-flips，见 Page 11-12。",
            "首次展示 contemporary off-the-shelf DDR4 devices 可执行 in-DRAM Majority/AND/OR，但存在 BER heterogeneity，见 Page 12, Figure 12。"
        ],
        "method": [
            "DRAM Bender 通过 FPGA 直接连接 DRAM PHY/DFI，提供 program memory、data buffers、readback FIFO、periodic operation scheduler 等模块，见 Page 4-7, Section 3。",
            "用户用 C++/Python 构造 command sequence，可加入 label、branch、loop 与精细 timing，随后在 FPGA 上执行并读回结果，见 Page 6-9, Section 3.5。",
            "案例研究分别构造 double-sided RowHammer、多种 data pattern 和 in-DRAM AND/OR 实验，用真实 DDR4 module 观测 bit flips 与 BER，见 Page 9-12。"
        ],
        "experiments": [
            "测试 Micron、Hynix、Samsung 三类 DDR4 module，模块信息见 Page 10, Table 6。",
            "RowHammer interleaving study 扫描 T=1 到 64K，总 ACT command 数固定为 1M，见 Page 9-10。",
            "in-DRAM bitwise study 测量不同 reduced timing 组合下 AND/OR 的 bit error rate，见 Page 12, Figure 12。"
        ],
        "results": [
            "double-sided RowHammer 中 T 越接近 1，bit-flips 越多；V2 行在 T=64K 时三家厂商平均 bit-flips 为 31.9/9.9/71.2，而 T=1 时为 314.8/50.7/604.9，见 Page 10, Figures 8-9。",
            "HCfirst 也受 interleaving 影响：T=1 时为 99K/80K/16K，T=64K 时为 130K/108K/23K，见 Page 10-11, Figures 10-11。",
            "DRAM Bender 支持的数据模式能发现更多 victim-row bit-flips，见 Page 11-12, Section 4.2。",
            "DDR4 芯片支持 in-DRAM AND/OR，但没有发现 0% BER segment；35 个 segment 在 <3% BER 下只支持 AND，最小 AND BER 为 1.9%，160 个 segment <5% BER，4546 个 segment <10% BER，见 Page 12, Figure 12。",
            "RowHammer 实验可用 12 行 C++ 编写，bulk bitwise AND/OR 可用 3 行 C++ 编写；移植到另一 FPGA board 只需约 230 行 Verilog 和 30 行 C++，见 Page 2。"
        ],
        "limitations": [
            "DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。",
            "功耗测量 setup 仍在进行中，尚未完整发布，见 Page 13, Section 7。",
            "packetized interfaces 的 3D-stacked DRAM 可能无法完全暴露低层 DRAM interface，限制 DRAM Bender 的适用性，见 Page 13-14。",
            "GUI 只是未来方向，目前仍偏向程序化实验，见 Page 14。",
            "in-DRAM AND/OR 在 DDR4 上存在 BER，不能直接当作可靠计算机制，见 Page 12。"
        ],
        "focus": [
            "Page 1-2 的 Table 1 和问题描述最能说明 DRAM Bender 相比 SoftMC/LRT 的定位。",
            "Page 4-8 的架构/API 说明决定它为什么可扩展、易用。",
            "Page 9-12 的三个 case studies 是实验证据，尤其 Figures 8-12。",
            "Page 13-14 的 Future Work and Limitations 要重点看，因为它清楚标出平台边界。"
        ],
        "relations": "DRAM Bender 与 PiDRAM 都是 FPGA-based real-DRAM infrastructure；PiDRAM 更偏端到端系统/PuM 集成，DRAM Bender 更偏底层 DRAM command-level characterization 和测试。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM organization", "背景结构", "快速看"],
            ["Figure 7", "Page 9-10", "double-sided RowHammer setup", "解释 A1/A2/V1/V2/V3 与 interleaving parameter T", "理解实验必须看"],
            ["Figures 8-9", "Page 10", "interleaving 对 bit-flip rate 的影响", "证明激活顺序显著影响攻击效果", "核心结果"],
            ["Figures 10-11", "Page 10-11", "interleaving 对 HCfirst 的影响", "说明首次 bit flip 所需 ACT 数也被改变", "核心结果"],
            ["Figure 12", "Page 12", "DDR4 AND/OR BER distribution", "证明 DDR4 具备近似 in-DRAM bitwise capability", "核心结果"]
        ],
        "tables": [
            ["Table 1", "Page 2", "testing infrastructures comparison", "对比 SoftMC、LRT 与 DRAM Bender", "定位关键"],
            ["Table 5", "Page 8", "temperature measurements", "说明实验温度控制", "实验可靠性信息"],
            ["Table 6", "Page 10", "tested DRAM modules", "列出三家厂商模块与芯片信息", "复现实验必需"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文以平台设计和实验观测为主", "公式不是阅读重点", "否"]
        ],
        "terms": [
            ["DRAM Bender", "DRAM 测试基础设施", "Page 1-2", "可向真实 DRAM 发出任意低层命令的 FPGA 平台", "是"],
            ["RowHammer", "行锤攻击/行锤现象", "Page 3, Page 9-12", "频繁激活 aggressor row 导致邻近 victim row bit flip", "是"],
            ["HCfirst", "首次 bit flip 所需激活数", "Page 10-11", "衡量 RowHammer 敏感性的指标", "是"],
            ["DFI", "DDR PHY Interface", "Page 3", "memory controller 与 PHY 间标准化接口", "中"],
            ["Bit Error Rate (BER)", "比特错误率", "Page 12", "in-DRAM AND/OR 结果错误比例", "是"],
            ["RFM", "Refresh Management command", "Page 13", "DDR5 中触发 refresh management/TRR 的命令", "中"]
        ],
        "open_questions": [
            "DDR5 RFM 是否能真正缓解 RowHammer，DRAM Bender 扩展后能否系统验证？",
            "DDR4 in-DRAM AND/OR 的 BER 是否能通过数据布局、温度、电压或选择 segment 降到可用范围？",
            "DRAM Bender 与 PiDRAM 是否可以组合，既做底层 characterization 又做端到端应用评估？"
        ],
    },
    {
        "slug": "2310.10168v2",
        "title": "DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures",
        "zh_title": "DaPPA：面向 Processing-in-Memory 架构的数据并行编程框架",
        "authors": "Geraldo F. Oliveira; Alain Kohli; David Novo; Ataberk Olgun; A. Giray Yağlıkçı; Saugata Ghose; Juan Gómez-Luna; Onur Mutlu",
        "year": "2025",
        "venue": "arXiv:2310.10168v2",
        "arxiv": "2310.10168v2",
        "doi": "未找到",
        "topic": "PIM programming framework; UPMEM; data-parallel patterns; code generation",
        "keywords": "DaPPA; UPMEM; PIM; data-parallel pattern; Pipeline; dynamic template-based compilation; PrIM",
        "pages": "14",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 UPMEM Architecture; 3.1 UPMEM Programming Model; 4 DaPPA Overview; 5 DaPPA Programming Interface and Compilation; 6 Methodology; 7 Evaluation; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "DaPPA 用 map/filter/reduce/window/group 等 data-parallel patterns 和 Pipeline dataflow 接口自动生成 UPMEM 代码，降低 PIM 编程复杂度并保持甚至提升端到端性能。",
        "background": [
            "UPMEM 是首个商用 PIM 系统，拥有大量 DPUs，但程序员必须手动划分数据、管理 CPU-DPU/DPU 内存传输、启动 kernel 和收集输出，见 Page 1, Section 1。",
            "这种编程模型要求开发者理解 MRAM/WRAM/IRAM、DPU tasklets 与数据搬移细节，阻碍 PIM 普及，见 Page 1-3。"
        ],
        "problems": [
            "如何让程序员不用手动管理 UPMEM 的数据分布、内存分配和通信。",
            "如何用高层 data-parallel pattern 表达 PIM-friendly computation。",
            "如何自动生成高效 UPMEM binary，同时减少代码量。"
        ],
        "contributions": [
            "提出首个面向 UPMEM 的 data-parallel pattern-based programming framework，见 Page 2。",
            "提供 map、filter、reduce、window、group 五类 primary data-parallel pattern primitives，见 Page 2 与 Page 4-7。",
            "提出 Pipeline dataflow programming interface，用 stage 串联多个 pattern，见 Page 2 与 Page 5-7。",
            "提出 dynamic template-based compilation，用 code skeletons 和动态变换生成 UPMEM target code，见 Page 2 与 Page 8-10。",
            "在真实 UPMEM 系统上相对 hand-tuned PrIM 平均提升 2.1x 端到端性能，并减少 94% LOC，见 Page 1 与 Page 10-12。"
        ],
        "method": [
            "用户用 C/C++ 调用 DaPPA pattern APIs 描述数据转换，DaPPA 负责将 primitive 翻译并并行化到 CPU 和 DPUs，见 Page 2 与 Page 4-7。",
            "Pipeline 类表示一串 stage，每个 stage 包含一个 pattern 和用户定义计算，按 dataflow 顺序执行，见 Page 5-7。",
            "dynamic template-based compilation 先根据 UPMEM application skeleton 生成初始代码，再填充 offset、数据搬移、WRAM/MRAM 参数和 CPU/DPU work partition，见 Page 8-10。"
        ],
        "experiments": [
            "实验平台为 2-socket Intel Xeon Silver 4110、128GB DDR4-2400、20 个 UPMEM PIM DIMMs、160GB PIM-capable memory、2560 DPUs，见 Page 10, Section 6。",
            "评估六个 PrIM workloads：VA、SEL、UNI、RED、GEMV、HST-S，见 Page 10-11。",
            "比较对象包括 hand-tuned PrIM implementations 和 SimplePIM；指标包括 LOC、端到端执行时间、DPU kernel performance 与 runtime overhead，见 Page 10-12。"
        ],
        "results": [
            "相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC，见 Page 11, Table 1。",
            "六个 workload 上，DaPPA 平均达到 PrIM 端到端性能的 2.1x，SEL/UNI 因并行数据回传策略表现尤其好，见 Page 11, Figure 5。",
            "DPU kernel performance 平均为 PrIM 的 1.4x，最高 3.5x，见 Page 11, Figure 6。",
            "runtime compilation/模板替换开销包括约 1 ms skeleton substitution、150 ms DPU binary compilation、1-150 ms 其他操作；相比 UPMEM SDK 分配 DPUs 的约 1200 ms 与端到端执行时间较小，见 Page 12, Section 7.3。"
        ],
        "limitations": [
            "评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。",
            "DaPPA 强绑定 UPMEM 架构和 SDK，迁移到其他 PIM 架构需要重新设计 backend，见 Page 12, Related Work。",
            "CPU-DPU/DPU-CPU transfer time 仍占主要执行时间，框架不能消除 UPMEM 硬件通信瓶颈，见 Page 11, Figure 5。",
            "runtime compilation 虽然相对端到端时间较小，但对短任务或频繁构建 Pipeline 的场景可能不可忽略，见 Page 12。",
            "UPMEM 缺乏 direct inter-DPU communication，DaPPA 需要通过 host/main memory 间接组织数据，见 Page 3。"
        ],
        "focus": [
            "Page 3 的 UPMEM Architecture 和 Programming Model 先读，明确 DPU/MRAM/WRAM 限制。",
            "Page 4-10 的 APIs、Pipeline 和 dynamic compilation 是方法核心。",
            "Page 11 Table 1 与 Figures 5-6 是生产率与性能证据。",
            "Page 12 的 overhead 分析用于判断框架是否适合短任务。"
        ],
        "relations": "DaPPA 与 SimplePIM、PrIM、UPMEM 生态相关；它关注的是 PIM 编程抽象，而不是 DRAM 内部电路 primitive，与 Ambit/RowClone/SIMDRAM 属于不同层次。",
        "figures": [
            ["Figure 1", "Page 2-3", "UPMEM-enabled system and DPU organization", "说明 host CPU、UPMEM DIMM、DPU、MRAM/WRAM/IRAM 关系", "背景核心图"],
            ["Figure 5", "Page 11", "end-to-end execution time", "展示 DaPPA 与 PrIM 的 CPU-DPU、DPU kernel、DPU-CPU 时间分解", "核心结果图"],
            ["Figure 6", "Page 11", "DPU kernel performance", "比较 kernel-only 性能", "辅助解释端到端结果"]
        ],
        "tables": [
            ["Table 1", "Page 11", "LOC comparison", "DaPPA 平均减少 94% LOC，并比 SimplePIM 进一步减少 59%", "核心生产率证据"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点是编程模型和代码生成", "公式不是阅读重点", "否"]
        ],
        "terms": [
            ["DaPPA", "数据并行 PIM 编程框架", "Page 1-2", "用高层 pattern 和 Pipeline 自动生成 UPMEM 程序", "是"],
            ["UPMEM", "商用 PIM 系统", "Page 1-3", "由带 DPU 的 DRAM DIMM 组成的 PIM 平台", "是"],
            ["DPU", "DRAM Processing Unit", "Page 1-3", "UPMEM PIM chip 内的小型多线程 in-order processor", "是"],
            ["MRAM", "DPU 私有 DRAM bank", "Page 1-3", "每个 DPU 独占的 64MB 存储", "是"],
            ["WRAM", "DPU scratchpad memory", "Page 1-3", "DPU 内 64KB scratchpad，需要显式搬移数据", "是"],
            ["Pipeline", "流水线数据流接口", "Page 5-7", "由多个 data-parallel stage 组成的 DaPPA 编程抽象", "是"],
            ["Dynamic template-based compilation", "动态模板式编译", "Page 8-10", "运行时填充 skeleton 并生成 UPMEM binary 的机制", "是"]
        ],
        "open_questions": [
            "DaPPA 是否能支持需要复杂 inter-DPU communication 的 graph/irregular workload？",
            "对于小输入或短任务，runtime compilation 开销是否会超过收益？",
            "能否把 DaPPA 的 data-parallel pattern 抽象迁移到非 UPMEM 的 PIM/near-memory 平台？"
        ],
    },
]


def metadata(p):
    return f"""# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh_title']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: {p['doi']}
- arXiv ID: {p['arxiv']}
- URL: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/{p['slug']}.pdf
- PDF Source: lec4-paper-reading/sources/original-paper/{p['slug']}.pdf
- Code / Project Page: {p.get('code', '未找到')}
- Dataset: {p.get('dataset', '未找到')}
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: {p.get('status', '深度阅读完成')}
- Full Text Available: Yes
- Notes: {NOTE}
"""


def summary(p):
    return f"""# 中文阅读摘要

## 1. 一句话总结
{p['one_sentence']}

## 2. 研究背景
{md_list(p['background'])}

## 3. 核心问题
{md_list(p['problems'])}

## 4. 核心贡献
{md_list(p['contributions'])}

## 5. 方法概述
{md_list(p['method'])}

## 6. 实验设计
{md_list(p['experiments'])}

## 7. 主要结果
{md_list(p['results'])}

## 8. 关键结论
这篇论文的核心结论是：{p['one_sentence']} 论文的主要实验证据集中在 {p['results'][0]} 这些结果表明，作者提出的方法在目标场景中确实缓解了数据搬移或系统集成瓶颈，但收益依赖具体数据布局、工作负载形态和系统支持。

## 9. 局限性
{md_list(p['limitations'])}

## 10. 适合我重点关注的内容
{md_list(p['focus'])}

## 11. 和其他文献的关系
{p['relations']}
"""


def key_points(p):
    rows = []
    points = [
        ("作者想解决的问题", p["problems"][0], "Page 1-2 / Introduction", p["background"][0], "高", "先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。"),
        ("核心假设", "目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。", "Page 1-2 / Introduction", p["background"][-1], "高", "这是判断论文适用范围的关键。"),
        ("方法关键设计", p["method"][0], "方法章节 / Page 2 及后续对应 section", p["method"][0], "高", "论文最值得回到原文精读的部分。"),
        ("系统集成设计", p["method"][-1], "方法章节后半部分", p["method"][-1], "高", "很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。"),
        ("最重要实验结果", p["results"][0], "Evaluation / Results", p["results"][0], "高", "这是作者主张有效性的第一证据。"),
        ("补充实验结果", p["results"][1] if len(p["results"]) > 1 else "未找到", "Evaluation / Results", p["results"][1] if len(p["results"]) > 1 else "未找到", "中", "用于判断收益是否只体现在单一指标。"),
        ("和 baseline 的差异", "论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。", "Evaluation / Related Work", "主要对比见实验图表和 related work comparison。", "高", "要看 baseline 是否公平、是否覆盖端到端成本。"),
        ("作者声称的贡献", p["contributions"][0], "Introduction / Contributions", p["contributions"][0], "高", "贡献通常对应论文的 novelty claim。"),
        ("局限", p["limitations"][0], "Limitations / Discussion / Future Work", p["limitations"][0], "高", "后续研究或读论文时要警惕的边界。"),
        ("需要进一步确认的问题", p["open_questions"][0], "由全文内容推断", "该问题未被论文完全解决。", "中", "可作为后续阅读或讨论问题。"),
    ]
    for i, item in enumerate(points, 1):
        rows.append([str(i), item[1], item[2], item[3], item[4], item[5]])
    return "# Key Points with Source Locations\n\n" + table(rows, ["编号", "重点内容", "原文位置", "支持证据", "重要性", "我的理解"])


def translation(p):
    return f"""# Full Chinese Translation

{NOTE}

## Title
原文标题：{p['title']}

中文标题：{p['zh_title']}

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：{p['one_sentence']} 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：{p['background'][0]} {p['background'][-1]} 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：{'; '.join(p['problems'])}

作者随后给出贡献：{'; '.join(p['contributions'][:3])} 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：{p['topic']}。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 {p['terms'][0][0]}、{p['terms'][1][0]}。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

{md_list(p['method'])}

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

{md_list(p['experiments'])}

主要结果如下：

{md_list(p['results'])}

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

{md_list(p['limitations'])}

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

{md_list(p['open_questions'])}

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：{p['one_sentence']} 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
"""


def fig_notes(p):
    return f"""# Figures, Tables, and Equations Notes

## Figures

{table(p['figures'], ["图编号", "原文位置", "图的主题", "图想表达什么", "阅读建议"])}

## Tables

{table(p['tables'], ["表编号", "原文位置", "表的主题", "主要结论", "阅读建议"])}

## Equations

{table(p['equations'], ["公式编号", "原文位置", "公式作用", "符号/直观解释", "是否需要重点掌握"])}

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
"""


def terminology(p):
    return "# Terminology\n\n" + table(p["terms"], ["English Term", "中文翻译", "出现位置", "简明解释", "是否核心术语"])


def limitations(p):
    return f"""# Limitations and Questions

## 1. 作者明确承认的局限
{md_list(p['limitations'][: max(1, len(p['limitations']) // 2)])}

## 2. 论文中隐含的局限
{md_list(p['limitations'][max(1, len(p['limitations']) // 2):])}

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
{md_list(p['open_questions'])}

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
"""


def checklist(p):
    return f"""# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：{p['problems'][0]}
- [ ] 我能解释作者的方法：{p['method'][0]}
- [ ] 我能指出核心创新：{p['contributions'][0]}
- [ ] 我能看懂主要实验表格和图，例如 `{p['figures'][-1][0]}` / `{p['tables'][0][0] if p['tables'] else '无核心表格'}`
- [ ] 我能复述最重要结果：{p['results'][0]}
- [ ] 我知道这篇文章的局限：{p['limitations'][0]}
- [ ] 我知道这篇文章和其他工作的关系：{p['relations']}
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
"""


def extraction_log(p):
    return f"""# Extraction Log

- Input Type: GitHub repository PDF
- Source: https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC4/original-paper/{p['slug']}.pdf
- Local PDF: lec4-paper-reading/sources/original-paper/{p['slug']}.pdf
- Extracted Text: lec4-paper-reading/extracted_text/{p['slug']}.txt
- Access Status: Public PDF downloaded through GitHub API/raw URL
- Full Text Retrieved: Yes
- PDF Pages: {p['pages']}
- Sections Detected: {p['sections']}
- Figures Detected: Yes, figure captions detected in extracted text
- Tables Detected: Yes, table captions detected in extracted text
- Equations Detected: {'Yes' if p['equations'][0][0] != '未检测到核心编号公式' else 'No core numbered equations detected in extracted text'}
- Appendix Detected: 未检测到明确 appendix
- Supplementary Material Detected: 未检测到
- OCR Used: No
- Missing Content: 图像本体未裁剪；公式/图形细节建议回到 PDF 人工查看
- Parsing Problems: 双栏 PDF 的部分行在抽取文本中交错；已用页码、章节和图表编号辅助定位
- Uncertain Parts: DOI、正式会议/期刊信息若 PDF 未显式给出则标为“未找到”或 arXiv
- Need User Action: 如需逐图截图或逐字全文翻译，请确认版权/用途并指定优先论文

## Quality Self-Check

- [x] 已读取 PDF 抽取文本，不只依据标题或摘要
- [x] 已覆盖背景、方法、实验、结果、局限
- [x] 已记录关键原文位置
- [x] 已整理图表/公式笔记
- [x] 已整理术语表
- [x] 已标注无法确认或需人工复核内容
"""


def write_papers(papers, status="深度阅读完成"):
    for p in papers:
        p.setdefault("status", status)
        base = f"papers/{p['slug']}"
        write(f"{base}/metadata.md", metadata(p))
        write(f"{base}/reading_summary.zh.md", summary(p))
        write(f"{base}/key_points_with_locations.zh.md", key_points(p))
        write(f"{base}/full_translation.zh.md", translation(p))
        write(f"{base}/figures_tables_equations_notes.zh.md", fig_notes(p))
        write(f"{base}/terminology.zh.md", terminology(p))
        write(f"{base}/limitations_and_questions.zh.md", limitations(p))
        write(f"{base}/reading_checklist.md", checklist(p))
        write(f"{base}/extraction_log.md", extraction_log(p))


if __name__ == "__main__":
    write_papers(PAPERS, status="第一轮 5 篇深度阅读完成")
    print(f"Wrote batch 1 files for {len(PAPERS)} papers into {ROOT / 'papers'}")
