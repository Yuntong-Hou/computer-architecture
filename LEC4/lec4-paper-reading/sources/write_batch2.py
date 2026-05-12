from write_batch1 import write_papers


PAPERS = [
    {
        "slug": "2402.18736v2",
        "title": "Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis",
        "zh_title": "真实 DRAM 芯片中的功能完备布尔逻辑：实验表征与分析",
        "authors": "İsmail Emir Yüksel; Yahya Can Tuğrul; Ataberk Olgun; F. Nisa Bostancı; A. Giray Yağlıkçı; Geraldo F. Oliveira; Haocong Luo; Juan Gómez-Luna; Mohammad Sadrosadati; Onur Mutlu",
        "year": "2024",
        "venue": "arXiv:2402.18736v2",
        "arxiv": "2402.18736v2",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/FCDRAM",
        "topic": "Processing-using-DRAM; functionally-complete Boolean logic; COTS DDR4 characterization",
        "keywords": "FCDRAM; PuD; NOT; NAND; NOR; AND; OR; many-input Boolean operations; COTS DDR4",
        "pages": "17",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Methodology; 4 Simultaneous Multiple-Row Activation; 5 NOT Operation; 6 Many-Input NAND/NOR/AND/OR; 7 Limitations; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "这篇论文证明部分未改动 COTS DDR4 芯片能够执行 NOT、NAND、NOR 以及多输入 AND/OR，从而在真实 DRAM 中形成 functionally-complete Boolean logic。",
        "background": [
            "Processing-using-DRAM (PuD) 利用 DRAM 电路的模拟操作特性在内存内部执行大规模 bitwise computation，从而减少 CPU/GPU 与主存之间的数据搬移，见 Page 1, Section 1。",
            "已有真实芯片实验主要展示 MAJ3、AND 和 OR，但还没有在 COTS DRAM 中展示 functionally-complete operation set，例如 NOT 与 NAND/NOR，见 Page 1-2。"
        ],
        "problems": [
            "COTS DRAM 芯片是否能执行功能完备的布尔操作集合，而不修改芯片或接口。",
            "这些操作在不同数据模式、温度、位置、速度等级和 die revision 下是否可靠。",
            "如何解释 NOT、NAND/NOR 和多输入 AND/OR 在真实 DRAM 中出现的底层原因。"
        ],
        "contributions": [
            "首次实验展示 unmodified off-the-shelf DRAM chips 能执行 NOT、NAND、NOR，以及多输入 NAND/NOR/AND/OR，见 Page 2。",
            "在 256 个现代 DDR4 chips、22 个 DRAM modules 上系统表征这些操作的 success rate，见 Page 1-2。",
            "提出两个底层操作假设：open-bitline sense amplifier 可产生 NOT，操控 reference terminal voltage 可产生 AND/NAND 与 OR/NOR，见 Page 2, Figure 1。",
            "定量评估 data pattern dependence 与 temperature 对 success rate 的影响，见 Page 13-14, Figures 18-19。",
            "开源 FCDRAM infrastructure，便于后续研究复现和扩展，见 Page 1。"
        ],
        "method": [
            "NOT 的核心假设是：在 open-bitline 架构中，同时连接 sense amplifier 两端的两个 DRAM cell，可利用反相端把一个 cell 的值取反并写入另一个 cell，见 Page 2, Figure 1a 与 Page 7, Section 5.1。",
            "AND/NAND 与 OR/NOR 的核心假设是：通过初始化 reference-side cells 改变 reference voltage，使 compute-side cells 的电压关系表达 AND 或 OR；相反端自然得到 NAND 或 NOR，见 Page 2, Figure 1b 与 Page 10-11, Section 6.1。",
            "作者用 success rate 衡量可靠性，即一个 DRAM cell 在 10000 trials 中正确执行 bitwise operation 的比例，见 Page 1-2 与 Page 8。",
            "实验覆盖 row distance、data pattern、temperature、speed rate、chip density 和 die revision 等因素，见 Page 8-14。"
        ],
        "experiments": [
            "NOT operation 在不同 row distance 和 temperature 下评估，结果见 Page 8-9, Figures 7-10。",
            "2/4/8/16-input AND、NAND、OR、NOR 的 success rate 分布见 Page 12, Figure 15。",
            "data pattern、temperature、speed rate、chip density/die revision 的影响分别见 Page 13-14, Figures 18-21。"
        ],
        "results": [
            "COTS DRAM 可执行 NOT，平均 success rate 为 98.37%，见 Page 1-2 与 Page 8-9。",
            "16-input AND、NAND、OR、NOR 的平均 success rate 分别为 94.94%、94.94%、95.85%、95.87%，见 Page 12, Figure 15。",
            "随机数据模式相比 all-1s/0s 只使 NAND、NOR、AND、OR 平均 success rate 分别下降 1.39%、1.97%、1.43%、1.98%，见 Page 13, Figure 18。",
            "温度从 50°C 升到 95°C 时，AND、NAND、OR、NOR 的平均 success rate 最大变化分别为 1.66%、1.65%、1.63%、1.64%，见 Page 14, Figure 19。",
            "物理位置、speed rate、chip density 与 die revision 会显著影响 success rate；例如 4-input NAND 在 2133 到 2400 MT/s 间可下降 29.89%，见 Page 13-14, Figures 17/20/21。"
        ],
        "limitations": [
            "并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。",
            "测试芯片最多支持到 16-input Boolean operations；是否能更多输入取决于未公开 row decoder 设计，见 Page 15, Section 7。",
            "这些操作依赖违反厂商推荐 timing parameters 和未文档化内部行为，现阶段不等价于标准、可靠的商用功能，见 Page 14-15。",
            "论文主要是芯片能力表征，没有完整系统/应用级加速评估。"
        ],
        "focus": [
            "先读 Page 2 Figure 1，理解 NOT 与 AND/NAND 的物理直觉。",
            "再读 Page 12 Figure 15，掌握多输入操作的可靠性证据。",
            "Page 13-14 Figures 17-21 是判断 robustness 和芯片差异的关键。",
            "Page 14-15 Section 7 必读，因为它明确说明哪些 COTS 芯片不支持这些行为。"
        ],
        "relations": "这篇论文延伸 Ambit/ComputeDRAM/DRAM Bender 的真实芯片 PuD 路线：从展示 AND/OR 推进到 functionally-complete Boolean logic 和多输入逻辑。",
        "figures": [
            ["Figure 1", "Page 2", "NOT 与 AND/NAND 操作示意", "说明现代 DRAM sense amplifier 如何可能执行布尔逻辑", "核心机制图，必须看"],
            ["Figure 7", "Page 8", "NOT success rate", "展示 NOT 在 COTS DRAM 中的成功率分布", "核心结果"],
            ["Figure 10", "Page 9", "NOT 温度敏感性", "展示温度对 NOT 可靠性的影响", "建议查看"],
            ["Figure 15", "Page 12", "2/4/8/16-input AND/NAND/OR/NOR success rate", "证明多输入逻辑可高可靠执行", "核心结果"],
            ["Figure 18", "Page 13", "data pattern effect", "说明随机数据模式影响较小", "鲁棒性证据"],
            ["Figure 19-21", "Page 14", "temperature/speed/die effects", "展示温度影响小但 speed/die 影响大", "边界条件必读"]
        ],
        "tables": [
            ["未检测到核心表格", "全文", "主要证据来自 figures", "表格不是本文主要承载形式", "无"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "论文以实验表征和物理假设为主", "公式不是重点", "否"]
        ],
        "terms": [
            ["Functionally-complete Boolean logic", "功能完备布尔逻辑", "Page 1-2", "能组合表达任意布尔函数的一组操作，例如 NAND 或 AND+NOT", "是"],
            ["Success rate", "成功率", "Page 1-2", "某 cell 在多次试验中正确执行操作的比例", "是"],
            ["COTS DRAM", "商用现货 DRAM", "Page 1", "未修改、可购买的 DRAM 芯片", "是"],
            ["Open-bitline architecture", "开放位线架构", "Page 2", "sense amplifier 两端连接不同 subarray/cell 的 DRAM 结构", "是"],
            ["Reference voltage", "参考电压", "Page 2", "sense amplifier 比较另一端的基准电压，可被多行激活操控", "是"],
            ["Many-input Boolean operation", "多输入布尔操作", "Page 10-12", "输入数超过两个的 AND/NAND/OR/NOR 操作", "是"]
        ],
        "open_questions": [
            "为什么 Micron/Samsung 芯片不完整支持这些操作，是否由命令过滤或 row decoder 设计造成？",
            "如果把这些行为正式做进 DRAM 标准，需要增加哪些接口和校验机制？",
            "在包含 ECC、refresh、温度变化和真实工作负载的系统里，success rate 能否满足应用要求？"
        ],
    },
    {
        "slug": "2402.19080v2",
        "title": "MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing",
        "zh_title": "MIMDRAM：面向高吞吐、节能和程序员透明 MIMD 处理的端到端 Processing-Using-DRAM 系统",
        "authors": "Geraldo F. Oliveira; Ataberk Olgun; Abdullah Giray Yağlıkçı; F. Nisa Bostancı; Juan Gómez-Luna; Saugata Ghose; Onur Mutlu",
        "year": "2024",
        "venue": "arXiv:2402.19080v2",
        "arxiv": "2402.19080v2",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/MIMDRAM",
        "topic": "End-to-end PUD architecture; MIMD in DRAM; fine-grained DRAM mats; compiler support",
        "keywords": "MIMDRAM; Processing-using-DRAM; MIMD; SIMD utilization; DRAM mats; vector reduction; compiler passes",
        "pages": "19",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Motivation; 4 MIMDRAM Architecture; 5 Compiler Support; 6 System Support; 7 Methodology; 8 Evaluation; 9 Related Work; References",
        "one_sentence": "MIMDRAM 通过细粒度控制 DRAM mats，让同一 subarray 中不同 mats 执行独立 PUD operations，从传统超宽 SIMD PuD 转向更灵活的 MIMD execution model。",
        "background": [
            "PUD 可利用 DRAM 阵列内部并行性执行 16K 到 262K-bit-wide 的 SIMD 操作，但 DRAM row 粒度过大且固定，导致 SIMD 利用率低、难支持 reduction、编程困难，见 Page 1-2。",
            "传统 PUD 往往要求程序员手工提取极宽数据并行性并映射到 DRAM row，缺少编译器支持，见 Page 2。"
        ],
        "problems": [
            "如何把 PUD 操作粒度从完整 DRAM row 缩小到 mat/segment，以匹配应用实际 SIMD parallelism。",
            "如何在 DRAM 内低成本支持 reduction 等需要跨 column 数据移动的操作。",
            "如何让编译器自动发现 PUD-friendly regions 并生成合适粒度的 PUD operations。"
        ],
        "contributions": [
            "提出首个面向 general-purpose applications 的端到端 MIMD PUD 系统，见 Page 3。",
            "使用 fine-grained DRAM 思路，只分配和控制给定 PUD operation 所需的 DRAM mats，见 Page 2-3 与 Page 4-7。",
            "加入 local/global interconnect 支持 vector-to-scalar reduction，降低以往 interconnect 面积开销，见 Page 5-7。",
            "提供 compiler passes 与 ISA/OS/data allocation 支持，使 PUD execution 对程序员透明，见 Page 8-11。",
            "在 12 个真实应用和 495 个 multiprogrammed mixes 上评估性能、能效、throughput、公平性和 SIMD utilization，见 Page 11-14。"
        ],
        "method": [
            "MIMDRAM 在硬件上增加 latches、isolation transistors 和 selection logic，使单个 DRAM mat 可被独立寻址并执行 PUD operation，见 Page 4-6, Section 4.1。",
            "它在 local/global I/O circuitry 中放置低成本 interconnect，以支持不同粒度的 column communication 和 in-DRAM vector reduction，见 Page 6-7, Figure 6。",
            "memory controller 新增控制单元，协调同一 subarray 内多个 mats 上独立 PUD operations 的并发执行，见 Page 7-8, Section 4.2。",
            "软件侧通过 compiler passes 自动 vectorize PUD-friendly regions、选择 SIMD granularity，并调度独立 PUD operations，见 Page 8-11。"
        ],
        "experiments": [
            "使用 Phoenix、Polybench、Rodinia、SPEC2017 的 12 个真实应用和 495 个多程序混合，见 Page 11, Section 7。",
            "比较 CPU、GPU、SIMDRAM、DRISA、Fulcrum 与 MIMDRAM，并分析 single-application、multi-programmed、area-normalized performance、SALP/BLP scaling 和 area，见 Page 12-14。",
            "主要指标包括 SIMD utilization、performance per Watt、weighted speedup、harmonic speedup、maximum slowdown、performance per area，见 Page 12-14。"
        ],
        "results": [
            "MIMDRAM 平均提供 SIMDRAM 的 15.6x SIMD utilization、14.3x energy efficiency 和 34x performance，见 Page 12, Figure 9。",
            "相对 CPU/GPU，MIMDRAM 平均提供 30.6x/6.8x energy efficiency，但在只用单 subarray/bank 时平均性能仍可能低于 CPU/GPU，见 Page 12。",
            "多程序混合中，MIMDRAM 相比 SIMDRAM 平均提升 1.68x weighted speedup、1.33x harmonic speedup，并将 maximum slowdown 降低 1.32x，见 Page 13, Figure 10。",
            "相比 baseline CPU 的多程序执行，MIMDRAM 总 throughput 提升 19%，见 Page 13, Figure 11。",
            "当使用 64 subarrays/bank 和 16 banks 时，MIMDRAM 平均达到 CPU 的 13.2x、GPU 的 2x performance，见 Page 14, Figure 14。",
            "面积开销较低：DRAM chip 约 1.11%，CPU die 约 0.6%，见 Page 1 与 Page 14-15。"
        ],
        "limitations": [
            "若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。",
            "multiplication/division 等成本高的操作仍是瓶颈，某些 workload 即使用满 DRAM parallelism 也可能低于 CPU，见 Page 14。",
            "高 vectorization factor mixes 下 fairness 仍可能比部分 SIMDRAM 多 bank 配置差，需要更好的 QoS/scheduling，见 Page 13。",
            "需要修改 DRAM subarray、memory controller、ISA、compiler 和 OS，落地复杂度高。"
        ],
        "focus": [
            "Page 1-3 的三大局限是理解 MIMDRAM 为什么需要 MIMD 的关键。",
            "Page 4-7 的硬件设计和 Figure 6 是方法核心。",
            "Page 8-11 的编译器与系统支持决定“programmer-transparent”是否成立。",
            "Page 12-14 的 Figures 9-14 用来判断收益、代价和边界。"
        ],
        "relations": "MIMDRAM 与 SIMDRAM、DRISA、Fulcrum 直接相关；它不是证明某个 DRAM primitive 能工作，而是提出更灵活的 PuD 系统架构与编译支持。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM module/subarray/mat 结构", "说明 MIMDRAM 利用 mat 作为细粒度执行资源", "背景关键图"],
            ["Figure 6", "Page 7", "PUD vector reduction 示例", "展示 MIMDRAM 如何在 DRAM 内支持 reduction", "核心方法图"],
            ["Figure 9", "Page 12", "single-application SIMD utilization/performance/energy", "展示对 SIMDRAM、CPU、GPU 的核心收益", "核心结果"],
            ["Figure 10", "Page 13", "multi-programmed workload results", "展示 throughput、turnaround、fairness", "核心结果"],
            ["Figure 11", "Page 13", "CPU multi-programmed comparison", "说明 MIMDRAM 相对 CPU 的 throughput 提升", "建议查看"],
            ["Figure 14", "Page 14", "SALP/BLP scalability", "说明利用更多 subarrays/banks 后的潜力", "理解边界必读"]
        ],
        "tables": [
            ["Table 2", "Page 11", "system configuration", "给出 CPU/GPU/SIMDRAM/MIMDRAM 模型参数", "复现实验需要"],
            ["Table 3", "Page 11", "evaluated applications", "列出 12 个应用、benchmark suite 和 PUD 指令类型", "实验设计关键"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点是架构、编译和系统评估", "公式不是重点", "否"]
        ],
        "terms": [
            ["MIMD", "多指令多数据", "Page 1-3", "不同 mats 可执行不同 PUD operations，而非全 subarray 同步执行同一操作", "是"],
            ["PUD", "Processing-using-DRAM", "Page 1", "利用 DRAM 模拟操作属性执行计算", "是"],
            ["DRAM mat", "DRAM 阵列小块", "Page 2-3", "subarray 内较小二维阵列，是 MIMDRAM 的细粒度资源单位", "是"],
            ["SIMD utilization", "SIMD 利用率", "Page 12", "实际有用 lane 占可用 lane 的比例", "是"],
            ["Vector reduction", "向量归约", "Page 6-7", "把向量多元素聚合成标量，如 sum reduction", "是"],
            ["SALP/BLP", "subarray/bank-level parallelism", "Page 13-14", "利用多个 subarray/bank 并发执行，提高 PUD 吞吐", "是"]
        ],
        "open_questions": [
            "MIMDRAM 的 compiler passes 在更复杂控制流或 pointer-heavy 应用上效果如何？",
            "是否可以结合 PNM 逻辑单元加速 multiplication/division 和 reduction，从而降低 MIMDRAM 短板？",
            "在真实操作系统和多租户环境中，mat/subarray 级资源调度如何保证 QoS？"
        ],
    },
    {
        "slug": "2405.06081v1",
        "title": "Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis",
        "zh_title": "商用 DRAM 芯片中的同时多行激活：实验表征与分析",
        "authors": "İsmail Emir Yüksel; Yahya Can Tuğrul; F. Nisa Bostancı; Geraldo F. Oliveira; A. Giray Yağlıkçı; Ataberk Olgun; Melina Soysal; Haocong Luo; Juan Gómez-Luna; Mohammad Sadrosadati; Onur Mutlu",
        "year": "2024",
        "venue": "arXiv:2405.06081v1",
        "arxiv": "2405.06081v1",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/SiMRA-DRAM",
        "topic": "Simultaneous many-row activation; MAJX; Multi-RowCopy; COTS DDR4 characterization",
        "keywords": "SiMRA; MAJ5; MAJ7; MAJ9; Multi-RowCopy; input replication; PuD; COTS DDR4",
        "pages": "18",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Methodology; 4 Simultaneous Many-Row Activation; 5 MAJX; 6 Multi-RowCopy; 7 Hypotheses and Input Replication; 8 Case Studies; 9 Limitations; 10 Related Work; 11 Conclusion; References",
        "one_sentence": "这篇论文表征了 COTS DDR4 中 simultaneous many-row activation，证明真实芯片可同时激活最多 32 行、执行 MAJ5/7/9，并将一行并发复制到最多 31 行。",
        "background": [
            "PUD 操作常依赖 multiple-row activation；此前真实芯片工作主要研究两行、三行或四行激活，尚不清楚更多行是否能被稳健地同时激活，见 Page 1-2。",
            "作者提出 Q1-Q5，系统询问 many-row activation 的可行性、可实现操作、鲁棒性、改善方式以及 data pattern/temperature/voltage/timing 的影响，见 Page 1-2。"
        ],
        "problems": [
            "COTS DRAM 是否能稳健地同时激活超过四行，甚至 32 行。",
            "这种能力能否实现 MAJX 和 Multi-RowCopy 等新的 PuD operations。",
            "如何提高 MAJX 成功率，并理解数据模式、温度、电压和 timing 对可靠性的影响。"
        ],
        "contributions": [
            "在 120 个 COTS DDR4 chips 上展示可同时激活 2/4/8/16/32 行，见 Page 2 与 Section 4。",
            "展示 MAJ5、MAJ7、MAJ9 以及 Multi-RowCopy：将一行内容同时复制到最多 31 行，见 Page 2, Sections 5-6。",
            "提出 input replication 能显著提升 MAJX success rate，见 Page 2 与 Page 10, Section 7.2。",
            "评估 timing delay、data pattern、temperature、voltage 对 simultaneous many-row activation、MAJX 和 Multi-RowCopy 的影响，见 Page 2 与 Sections 4-7。",
            "用七个 majority-based microbenchmarks 和 cold-boot attack prevention case study 分析潜在性能收益，见 Page 10-12, Section 8。"
        ],
        "method": [
            "作者用 DRAM Bender 精细调度 ACT/PRE 等命令，违反标准 timing parameters，以触发 simultaneous many-row activation，见 Page 3-5。",
            "MAJX 通过同时激活奇数个输入行实现多数函数；Multi-RowCopy 通过多行同时激活把一个源行并发写入多个目标行，见 Page 5-9。",
            "input replication 把 MAJX 输入操作数的多个副本放到所有激活行中，提高 bitline voltage perturbation 的 sensing margin，见 Page 10, Section 7.2。",
            "success rate、温度、电压、data pattern 和 row decoder 假设共同用于解释真实芯片行为，见 Page 4-10。"
        ],
        "experiments": [
            "测试 120 个 DDR4 chips、18 个 DRAM modules，来自两个主要制造商；部分 Samsung 芯片作为限制讨论，见 Page 2 与 Page 12。",
            "MAJ3/5/7/9 与 Multi-RowCopy 的可靠性在多种 timing、data pattern、temperature、voltage 下评估，见 Sections 4-7。",
            "七个 microbenchmarks 包括 AND/OR/XOR/ADD/SUB/MUL/DIV；cold-boot prevention 比较 RowClone、Frac 和 Multi-RowCopy，见 Page 10-12, Section 8。"
        ],
        "results": [
            "COTS DRAM 可同时激活最多 32 行；MAJ3/MAJ5/MAJ7/MAJ9 平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%，见 Page 2。",
            "将一行复制到 1/3/7/15/31 个目标行的平均 success rate 分别为 99.996%、99.989%、99.998%、99.999%、99.982%，见 Page 2。",
            "MAJ3 使用 32-row activation 并复制每个输入 10 次时，平均 success rate 比 4-row activation 高 30.81%，见 Page 1-2 与 Page 10。",
            "data pattern 对 MAJX 与 Multi-RowCopy 的平均影响分别为 11.52% 和 0.07%；temperature/voltage 变化导致最大 success rate 变化为 2.13%/1.32%，见 Page 1-2。",
            "MAJ5/7/9 在七个 microbenchmarks 中相对 MAJ3 平均提升 121.61% (Mfr. M) 和 46.54% (Mfr. H)，见 Page 11, Figure 16。",
            "Multi-RowCopy content destruction 相对 RowClone 和 Frac 最多分别加速 20.87x 和 7.55x，见 Page 11-12, Figure 17。"
        ],
        "limitations": [
            "部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。",
            "当前只能控制 consecutive two-row activation 或 simultaneous 2/4/8/16/32-row activation，无法任意选择激活行数，可能受 1.5ns timing granularity 限制，见 Page 12。",
            "PUD operations 对 transient errors 的潜在影响没有完全探索，见 Page 12。",
            "MAJ9 在某些厂商上因 success rate 差可能导致性能退化，见 Page 11。"
        ],
        "focus": [
            "Page 1-2 的 Q1-Q5 和回答构成全文骨架。",
            "Page 10 的 input replication 是提高可靠性的核心洞见。",
            "Page 11 Figures 16-17 是从芯片能力到应用潜力的关键证据。",
            "Page 12 Section 9 明确 COTS 芯片能力的边界。"
        ],
        "relations": "这篇论文与 FCDRAM 是互补关系：FCDRAM 展示 functionally-complete Boolean logic，本论文展示 simultaneous many-row activation、MAJX 和 Multi-RowCopy。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM organization", "解释 row/subarray/sense amplifier 背景", "背景图"],
            ["Figure 14", "Page 10", "hypothetical row decoder design", "解释为什么可能同时激活多行", "机制推断图"],
            ["Figure 16", "Page 11", "MAJX microbenchmark speedup", "展示 MAJ5/7/9 的潜在性能收益", "核心结果"],
            ["Figure 17", "Page 11-12", "content destruction speedup", "展示 Multi-RowCopy 在 cold-boot 防护中的收益", "应用案例核心图"]
        ],
        "tables": [
            ["Table 2", "Page 18", "tested DDR4 module characteristics", "列出测试模块和芯片信息", "复现实验关键"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点是实验表征与命令序列", "否", "否"]
        ],
        "terms": [
            ["Simultaneous many-row activation", "同时多行激活", "Page 1-2", "一次或近似一次激活超过四条 DRAM rows", "是"],
            ["MAJX", "X 输入多数操作", "Page 1-2", "X>3 的 majority operation，如 MAJ5/7/9", "是"],
            ["Multi-RowCopy", "多行并发复制", "Page 1-2", "把一行内容同时复制到多个目标行", "是"],
            ["Input replication", "输入复制", "Page 10", "把输入副本放入多个激活行以提高 sensing margin", "是"],
            ["Cold-boot attack", "冷启动攻击", "Page 11", "利用 DRAM 断电后短时保留数据读取机密信息", "中"],
            ["FracDRAM", "分数电荷 DRAM 技术", "Page 3, Page 11", "利用 fractional values 执行 MAJ3 等操作", "中"]
        ],
        "open_questions": [
            "能否设计标准化 DRAM 接口，让行数和 row group 更可控地执行 SiMRA？",
            "MAJ9 等低 success rate 操作是否能通过 input replication、ECC 或重试策略变得实用？",
            "simultaneous many-row activation 是否会加剧 read disturbance，这与 PuDHammer 论文直接相关。"
        ],
    },
    {
        "slug": "2501.17466v2",
        "title": "Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic",
        "zh_title": "Proteus：通过动态位精度、自适应数据表示和灵活算术实现高性能 Processing-Using-DRAM",
        "authors": "Geraldo F. Oliveira; Mayank Kabra; Yuxin Guo; Kangqi Chen; A. Giray Yağlıkçı; Melina Soysal; Mohammad Sadrosadati; Joaquin O. Bueno; Saugata Ghose; Juan Gómez-Luna; Onur Mutlu",
        "year": "2025",
        "venue": "arXiv:2501.17466v2",
        "arxiv": "2501.17466v2",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/Proteus",
        "topic": "Dynamic bit precision; PUD arithmetic; redundant binary representation; runtime µProgram selection",
        "keywords": "Proteus; dynamic bit-precision; narrow values; RBR; µProgram Library; SALP; bit-serial PUD",
        "pages": "18",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Motivation; 4 Proteus; 5 Implementation; 6 Methodology; 7 Evaluation; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。",
        "background": [
            "现有 PUD 多采用 bulk bit-serial execution model，用固定 two's complement 和固定 bit-precision 处理整行数据，导致大量 inconsequential bits 被无谓计算，见 Page 1-2。",
            "PUD 还面临 throughput-oriented execution 难隐藏低并行场景下的单操作延迟，以及高精度操作延迟随 bit-width 线性或二次增长的问题，见 Page 1-2。"
        ],
        "problems": [
            "如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。",
            "如何在 PUD operation 内并行执行独立 in-DRAM primitives，缓解单操作延迟。",
            "如何为不同 bit-precision 自动选择最合适的 data representation 和 arithmetic algorithm。"
        ],
        "contributions": [
            "提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。",
            "利用 narrow values 动态降低 PUD operation bit-precision，减少 latency 和 energy，见 Page 2。",
            "利用 SALP 将一个 data word 的不同 bits 分散到多个 subarrays，跨 bit 并行执行独立 primitives，见 Page 2 与 Page 4-5。",
            "引入 redundant binary representation (RBR) 支持高精度运算，减少或限制 carry propagation，见 Page 2。",
            "设计 Parallelism-Aware µProgram Library、Dynamic Bit-Precision Engine 和 µProgram Select Unit，见 Page 2 与 Page 5-10。"
        ],
        "method": [
            "Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。",
            "Parallelism-Aware µProgram Library 保存不同 bit-precision、two's complement/RBR、bit-serial/bit-parallel 算法的 µPrograms 及 cost model LUTs，见 Page 2 与 Page 8-10。",
            "µProgram Select Unit 在发出 PUD operation 时查询 bit-precision 和 cost LUT，选择最低延迟或最低能耗的 µProgram，见 Page 2 与 Page 8-10。",
            "Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。"
        ],
        "experiments": [
            "使用 12 个真实应用，来自 Phoenix、Polybench、Rodinia、SPEC2017；系统配置见 Page 12, Tables 2-3。",
            "比较 CPU、A100 GPU、SIMDRAM-SP、SIMDRAM-DP、Proteus LT/EN with static/dynamic precision，见 Page 12-13。",
            "额外分析 data mapping/representation conversion overhead、floating-point synthetic throughput、GPU tensor cores 对比和面积开销，见 Page 13-14。"
        ],
        "results": [
            "Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。",
            "SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。",
            "Dynamic Bit-Precision Engine 使 Proteus 相比 static bit-precision 性能提升 46%，energy consumption 降低 58%，见 Page 12-13, Figures 11-12。",
            "Proteus 平均比 CPU/GPU/SIMDRAM 分别降低 90.3x、21x、8.1x energy consumption，见 Page 1 与 Page 13。",
            "在 int8/int4 GEMM-heavy workloads 上，Proteus 相对 A100 tensor cores 提供 20x/43x performance per mm² 和 484x/767x performance per Watt，见 Page 14, Figure 14。",
            "面积开销低：DRAM chip 1.6%，CPU die 0.03%，见 Page 1 与 Page 14-15。"
        ],
        "limitations": [
            "真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。",
            "baseline PUD substrate 不支持 floating-point，浮点评估使用 synthetic analysis 而非完整真实应用，见 Page 13-14。",
            "Proteus 依赖 Ambit、LISA、SALP 等底层机制，真实硬件实现需要这些机制可靠可用，见 Page 14-15。",
            "动态 bit-precision 需要对象追踪、转置缓冲和元数据维护；短任务上的 runtime/metadata 开销仍需进一步验证。"
        ],
        "focus": [
            "Page 1-2 的三大短板是 Proteus 的动机主线。",
            "Page 4-5 Figure 3 解释 bit-serial addition 中哪些 primitive 能并行。",
            "Page 8-10 的 µProgram Library 和 Pareto analysis 是方法选择逻辑。",
            "Page 12-14 Figures 11-14 是核心性能/能耗证据。"
        ],
        "relations": "Proteus 建立在 SIMDRAM、Ambit、LISA、SALP 等工作上，解决的是 PuD arithmetic 的运行时自适应和高精度低延迟问题，可与 MIMDRAM 的资源粒度控制互补。",
        "figures": [
            ["Figure 2", "Page 4", "required bit-precision distribution", "说明 narrow values 普遍存在，支撑动态位精度", "动机关键图"],
            ["Figure 3", "Page 5", "bit-serial PUD addition", "展示哪些步骤必须串行、哪些可并行", "方法关键图"],
            ["Figure 10", "Page 10", "Pareto analysis", "展示不同 µPrograms 的 throughput/energy tradeoff", "选择逻辑关键图"],
            ["Figure 11", "Page 12", "performance per mm²", "Proteus 对 CPU/GPU/SIMDRAM 的核心性能比较", "核心结果"],
            ["Figure 12", "Page 13", "energy reduction", "展示 Proteus 能耗收益", "核心结果"],
            ["Figure 13", "Page 13", "mapping/format conversion overhead", "说明转换成本", "开销分析"],
            ["Figure 14", "Page 14", "tensor core comparison", "窄精度 GEMM 下与 A100 tensor cores 比较", "重点看"]
        ],
        "tables": [
            ["Table 2", "Page 12", "evaluated system configurations", "列出 CPU/GPU/SIMDRAM/Proteus 参数", "复现关键"],
            ["Table 3", "Page 12", "evaluated applications", "列出应用、内存 footprint、bit-precision 和 PUD instructions", "实验设计关键"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点是 runtime/µProgram 选择和系统评估", "公式不是重点", "否"]
        ],
        "terms": [
            ["Dynamic bit-precision", "动态位精度", "Page 1-2", "根据运行时数据实际范围选择更小 bit-width", "是"],
            ["Narrow values", "窄值", "Page 1-2", "虽然存为 32/64-bit，但有效位很少的值", "是"],
            ["Redundant Binary Representation (RBR)", "冗余二进制表示", "Page 2", "用多个 digit 组合表示同一值，限制 carry propagation", "是"],
            ["µProgram", "微程序", "Page 1-2", "实现一个 PUD operation 的 DRAM command sequence", "是"],
            ["Parallelism-Aware µProgram Library", "并行性感知微程序库", "Page 2", "保存不同算法/表示/位宽下的 µProgram 和 cost model", "是"],
            ["Dynamic Bit-Precision Engine", "动态位精度引擎", "Page 2", "在数据转置/写回过程中识别对象所需位宽", "是"]
        ],
        "open_questions": [
            "Proteus 与 MIMDRAM 是否可以结合，同时解决位精度和资源粒度问题？",
            "如果应用包含大量 floating-point 或不规则数据结构，Proteus 的收益还剩多少？",
            "动态 bit-precision metadata 在多线程、多进程和虚拟内存环境中如何维护一致性？"
        ],
    },
    {
        "slug": "2506.12947v1",
        "title": "PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips",
        "zh_title": "PuDHammer：真实 DRAM 芯片中 Processing-using-DRAM 的读扰动影响实验分析",
        "authors": "İsmail Emir Yüksel; Akash Sood; Ataberk Olgun; Oğuzhan Canpolat; Haocong Luo; F. Nisa Bostancı; Mohammad Sadrosadati; A. Giray Yağlıkçı; Onur Mutlu",
        "year": "2025",
        "venue": "arXiv:2506.12947v1",
        "arxiv": "2506.12947v1",
        "doi": "未找到",
        "topic": "Read disturbance; PuD security/reliability; RowHammer; CoMRA; SiMRA; PRAC mitigation",
        "keywords": "PuDHammer; read disturbance; RowHammer; RowPress; CoMRA; SiMRA; TRR; PRAC; HCfirst",
        "pages": "20",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Methodology; 4 CoMRA Read Disturbance; 5 SiMRA Read Disturbance; 6 Combined RowHammer and PuDHammer; 7 TRR; 8 Countermeasures; 9 Related Work; 10 Conclusion; References",
        "one_sentence": "PuDHammer 首次系统表征 multiple-row activation-based PuD operations 对 DRAM read disturbance 的影响，发现 CoMRA/SiMRA 可显著放大类似 RowHammer 的安全与可靠性风险。",
        "background": [
            "PuD 操作通常需要 consecutive 或 simultaneous multiple-row activation，而现代 DRAM 已知存在 RowHammer/RowPress 等 read disturbance 问题；此前没有工作研究 PuD 多行激活是否会加剧读扰动，见 Page 1。",
            "作者把用于 in-DRAM copy 的 consecutive multiple-row activation 称为 CoMRA，把用于 bitwise operations 的 simultaneous multiple-row activation 称为 SiMRA，见 Page 1-2。"
        ],
        "problems": [
            "multiple-row activation-based PuD 是否会比传统 RowHammer 更容易诱发 bitflip。",
            "data pattern、temperature、timing、row-on time、spatial variation 等因素如何影响 PuDHammer。",
            "现有 TRR/PRAC 类 RowHammer mitigation 能否防住 PuDHammer，代价多大。"
        ],
        "contributions": [
            "首次在 316 个真实 DDR4 chips、40 个 modules、4 个制造商上表征 PuD 多行激活导致的 read disturbance，见 Page 1-2。",
            "分别分析 CoMRA 和 SiMRA 的 HCfirst 分布，并与 RowHammer/RowPress 对比，见 Page 5-10。",
            "分析 RowHammer 与 PuDHammer 组合 access pattern 的效果，见 Page 11, Section 6。",
            "证明 PuDHammer 可绕过某 in-DRAM TRR mitigation 并产生更多 bitflips，见 Page 12, Section 7。",
            "提出三类 countermeasure，并改造 PRAC 评估性能开销，见 Page 13-14, Section 8。"
        ],
        "method": [
            "使用 HCfirst 作为主要 vulnerability metric，即诱发首个 bitflip 所需 hammer cycles；越低表示越脆弱，见 Page 5, Section 4.2。",
            "CoMRA 实验反复执行 in-DRAM copy 风格的 src/dst 连续激活；SiMRA 实验同时激活 2/4/8/16/32 行并测量 victim rows，见 Page 5-10。",
            "作者使用 bisection-method algorithm 搜索每个 victim row 的 HCfirst，并对每行重复 5 次报告最小值，见 Page 5。",
            "mitigation 部分将 PRAC 扩展到多行同时计数，并提出 area-optimized、performance-optimized 与 weighted counting，见 Page 13-14。"
        ],
        "experiments": [
            "CoMRA 与 RowHammer 比较、data pattern、temperature、single/double-sided、RowPress、timing delay、copy direction、spatial variation 等实验见 Page 5-8。",
            "SiMRA 的 double/single-sided、data pattern、temperature、row-on time、voltage、activated row count 等实验见 Page 8-10。",
            "TRR 与 PRAC mitigation 在真实芯片和 Ramulator 2.0 cycle-level simulation 中评估，见 Page 12-14。"
        ],
        "results": [
            "CoMRA 与 SiMRA 分别使最低 HCfirst 相比 RowHammer 低 13.98x 和 158.58x，见 Page 2 与 Page 5/9。",
            "double-sided CoMRA 中，99% DRAM rows 相比 RowHammer 用更少 activation counts 发生首个 bitflip，见 Page 5-6, Figure 4。",
            "SiMRA 的数据模式和 row-on time 可使平均 HCfirst 分别变化最高 57.80x 和 270.27x，见 Page 9-10, Figures 14/17。",
            "RowHammer 与 CoMRA/SiMRA 组合比 RowHammer 单独更有效；三者组合使 average HCfirst 降低 1.66x，见 Page 2 与 Page 11。",
            "在开启 TRR 的测试模块中，SiMRA 和 CoMRA 分别比 RowHammer 平均诱发 11340x 和 1.10x 更多 bitflips，见 Page 2 与 Page 12, Figure 24。",
            "改造后的 PRAC-PO-WC 对 PuDHammer 的平均/最大性能开销为 48.26%/98.83%；4µs period 下开销为 19.26%，而 naive 方案为 69.15%，见 Page 14, Figure 25。"
        ],
        "limitations": [
            "论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。",
            "作者只 sketch 部分 countermeasures，详细设计和面积/能耗评估留给未来工作，见 Page 13。",
            "PRAC-PO 的面积开销没有完整评估；多 counter simultaneous update 可能需要大量 incrementers 和 counter access，见 Page 14。",
            "device-level physical causes 仍需后续研究，见 Page 2 与 Page 14-15。"
        ],
        "focus": [
            "Page 1-2 先读，抓住 PuDHammer 为什么是 PuD 系统必须考虑的新风险。",
            "Page 5 Figure 4 与 Page 9 Figure 13/14 是 CoMRA/SiMRA 风险证据。",
            "Page 12 Figure 24 展示 TRR bypass，是安全影响最强的部分。",
            "Page 13-14 Figure 25 说明现有 mitigation 的性能代价。"
        ],
        "relations": "PuDHammer 是对 SiMRA/FCDRAM/Ambit 等 PuD 能力论文的重要安全可靠性补充：前者证明 DRAM 能算，PuDHammer 提醒多行激活可能显著加剧 read disturbance。",
        "figures": [
            ["Figure 1", "Page 2", "DRAM organization", "背景结构", "快速看"],
            ["Figure 4", "Page 5", "CoMRA vs RowHammer HCfirst", "证明 CoMRA 加剧 read disturbance", "核心结果"],
            ["Figure 13", "Page 9", "SiMRA HCfirst change", "展示 SiMRA 相比 RowHammer 的 HCfirst 降低", "核心结果"],
            ["Figure 14/17", "Page 9-10", "data pattern 和 RowPress/on-time 影响", "说明 operating conditions 可大幅改变风险", "边界条件核心"],
            ["Figure 21", "Page 11", "combined RowHammer/PuDHammer", "展示组合 access pattern 更有效", "安全影响"],
            ["Figure 24", "Page 12", "TRR enabled/disabled bitflips", "说明 PuDHammer 可绕过 TRR", "核心安全结果"],
            ["Figure 25", "Page 14", "PRAC mitigation overhead", "展示防护 PuDHammer 的性能开销", "mitigation 核心图"]
        ],
        "tables": [
            ["DRAM module table", "Methodology section", "测试芯片/模块信息", "316 chips、40 modules、4 manufacturers", "复现实验需要"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文以实验测量和 mitigation 分析为主", "公式不是重点", "否"]
        ],
        "terms": [
            ["PuDHammer", "PuD 诱发读扰动现象", "Page 1", "multiple-row activation-based PuD 操作造成或加剧 read disturbance", "是"],
            ["CoMRA", "consecutive multiple-row activation", "Page 1-2", "连续激活多行，常用于 in-DRAM copy", "是"],
            ["SiMRA", "simultaneous multiple-row activation", "Page 1-2", "同时激活多行，常用于 in-DRAM bitwise operations", "是"],
            ["HCfirst", "首次 bitflip 所需 hammer count", "Page 5", "衡量 read disturbance 脆弱性的指标", "是"],
            ["TRR", "Target Row Refresh", "Page 1-2, Page 12", "DRAM 内 RowHammer mitigation", "是"],
            ["PRAC", "Per Row Activation Counting", "Page 1-2, Page 13", "DDR5 标准化的逐行激活计数防护思路", "是"]
        ],
        "open_questions": [
            "未来支持 PuD 的 DRAM 标准应如何同时保证计算能力和 read disturbance isolation？",
            "是否能设计比 PRAC-PO-WC 开销更低的 PuDHammer-specific mitigation？",
            "PuDHammer 的物理机制与 RowHammer/RowPress 是否相同，还是存在新的耦合路径？"
        ],
    },
]


if __name__ == "__main__":
    write_papers(PAPERS, status="第二轮 5 篇深度阅读完成")
    print(f"Wrote batch 2 files for {len(PAPERS)} papers")
