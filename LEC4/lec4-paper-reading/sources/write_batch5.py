from write_batch1 import write_papers


PAPERS = [
    {
        "slug": "pim-enabled-instructons-for-low-overhead-pim_isca15",
        "title": "PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture",
        "zh_title": "PIM-enabled Instructions：低开销、局部性感知的 Processing-in-Memory 架构",
        "authors": "Junwhan Ahn; Sungjoo Yoo; Onur Mutlu; Kiyoung Choi",
        "year": "2015",
        "venue": "ISCA 2015",
        "arxiv": "未找到",
        "doi": "10.1145/2749469.2750385",
        "topic": "Processing-in-memory ISA interface; locality-aware PIM execution; 3D-stacked DRAM",
        "keywords": "PIM-enabled instructions; PEI; locality-aware execution; HMC; PCU; PMU; cache coherence; virtual memory",
        "pages": "13",
        "sections": "Abstract; 1 Introduction; 2 Background and Motivation; 3 PIM Abstraction; 4 Architecture; 5 Workloads and Operations; 6 Methodology; 7 Evaluation Results; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "这篇论文把简单 PIM operations 封装为主机 ISA 中的 PIM-enabled instructions，并用硬件局部性监控在 host-side 和 memory-side 执行之间动态选择，从而兼顾 PIM 带宽优势与 cache locality。",
        "background": [
            "作者指出早期和现代 PIM 往往需要新的编程模型、非 cacheable memory region 或显式 cache flush，难以无缝接入现有系统，见 Page 1, Section 1。",
            "3D-stacked DRAM/HMC 提供 logic die、TSV 内部高带宽和低能耗传输，但如果所有操作都强制在 memory side 执行，高局部性数据反而会失去 on-chip cache 优势，见 Page 2-3, Sections 2.1-2.2。"
        ],
        "problems": [
            "如何让 PIM operation 像普通 host instruction 一样使用，而不是引入全新的 PIM 编程模型。",
            "如何让 PIM operation 与现有 cache coherence 和 virtual memory 机制兼容。",
            "如何根据数据局部性动态决定 PEI 在 host processor 还是 memory-side logic 上执行。"
        ],
        "contributions": [
            "提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。",
            "提出 single-cache-block restriction，使 PEI 的目标内存范围限制在一个 LLC cache block 内，以简化 localization、coherence 和 locality profiling，见 Page 3-4, Section 3.1。",
            "设计 PEI Computation Unit (PCU) 与 PEI Management Unit (PMU)，支持 host-side/memory-side PEI execution、atomicity、coherence 和 locality monitoring，见 Page 5-7, Section 4。",
            "提出 runtime locality-aware execution：硬件根据 locality monitor 决定 PEI 的执行位置，见 Page 6-7。",
            "用 10 个 emerging data-intensive workloads 证明该机制能在不同输入规模和多程序环境中自适应选择执行位置，见 Page 9-12, Section 7。"
        ],
        "method": [
            "PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。",
            "single-cache-block restriction 限制单个 PEI 只访问一个 LLC block，并把 input/output operands 也限制在一个 cache block 内，从而使 coherence、translation 和 locality profiling 都落在现有粒度上，见 Page 3-4。",
            "PMU 在 LLC 附近维护 PIM directory 与 locality monitor：前者管理 in-flight PEI 的 reader-writer atomicity，后者以 cache-like partial tags 监控目标 cache block 的局部性，见 Page 5-7。",
            "Locality-Aware policy 根据目标数据是否可能在 cache 中受益，选择 host-side 或 memory-side PCU；balanced dispatch 进一步根据 request/response bandwidth 平衡执行位置，见 Page 9-11。"
        ],
        "experiments": [
            "在 HMC-based 系统模型上模拟 10 个 workload：图处理、hash join、histogram、R-probe、streamcluster、SVM 等，输入分为 small/medium/large，见 Page 8-9, Table 3。",
            "比较 Host-Only、PIM-Only、Ideal-Host 和 Locality-Aware 四种配置，指标包括 normalized IPC、off-chip transfer、multiprogrammed throughput、energy、area 和敏感性，见 Page 9-12。",
            "PageRank motivation 中用 9 个真实 graph 评估 in-memory atomic add 的收益/风险，见 Page 3, Figure 2。",
            "multiprogrammed evaluation 随机组合 200 个 workload，测试动态 locality-aware 机制在混合局部性下的表现，见 Page 10, Figure 9。"
        ],
        "results": [
            "PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。",
            "large inputs 中 PIM-Only 相比 Ideal-Host 平均快 44%；small inputs 中 PIM-Only 平均慢 20%，因为即使数据适合 cache 也访问 DRAM，见 Page 9, Figure 6。",
            "Locality-Aware 在 large inputs 中通过把 79% PEIs offload 到 memory-side，相比 Host-Only 提升 47%；在 small inputs 中通过让 86% PEIs host-side 执行，相比 PIM-Only 提升 32%，见 Page 9, Section 7.1。",
            "medium graph workloads 中，Locality-Aware 同时利用 host-side 与 memory-side PCUs，分别比 Host-Only 和 PIM-Only 快 12% 和 11%，见 Page 9-10。",
            "balanced dispatch 在 SC/SVM 上最多进一步提升 25%，见 Page 11, Figure 10。",
            "Locality monitor storage overhead 为 512KB，即 LLC capacity 的 3.1%；理想化 PIM directory/locality monitor 只分别带来 0.13%/0.31% 性能提升，说明 PMU overhead 很小，见 Page 9 与 Page 11。",
            "Locality-Aware 在所有输入规模下 memory hierarchy energy 最低；memory-side PCUs 只占 HMC energy 的 1.4%，area overhead 估计为 logic die area 的 1.85%，见 Page 12, Section 7.7。"
        ],
        "limitations": [
            "单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。",
            "软件仍需把目标代码改写为 PEIs；作者认为编译器未来可自动识别，但本文主要假设程序员手动修改，见 Page 4, Section 3.3。",
            "PEI 与普通 load/store 之间的 atomicity 不是自动保证的，需要 pfence 等同步，见 Page 4, Section 3.2。",
            "评估基于模拟 HMC/PCU 模型，真实 HMC/HBM 产品中的接口、timing 和 coherence 支持可能不同。"
        ],
        "focus": [
            "Page 3-4 的 PEI abstraction 和 single-cache-block restriction 是全文的系统设计核心。",
            "Page 5-7 的 PCU/PMU 说明如何把 PEI 接入 cache coherence、atomicity 和 locality monitoring。",
            "Page 9 Figure 6 必读，因为它展示 PIM-Only 在 small/large input 上完全相反的效果。",
            "Page 10-12 的 multiprogrammed、balanced dispatch、energy/area 结果可帮助判断 PEI 是否实用。"
        ],
        "relations": "这篇论文属于 processing-near-memory/PIM interface 路线，与 RowClone/Ambit/SIMDRAM 的 DRAM-array primitive 不同；它解决的是如何把简单 memory-side operations 融入 ISA、cache coherence 和 locality-aware scheduling。",
        "figures": [
            ["Figure 1", "Page 3", "PageRank pseudocode", "说明 PEI atomic add 的目标代码位置", "动机图"],
            ["Figure 2", "Page 3", "in-memory atomic add speedup", "展示 PIM 在不同 graph locality 下既可能加速也可能减速", "核心动机图"],
            ["Figure 3", "Page 5", "architecture overview", "展示 PCU、PMU、HMC/vault 结构", "核心架构图"],
            ["Figure 6", "Page 9", "speedup comparison by input size", "展示 Host-Only/PIM-Only/Locality-Aware 的 trade-off", "核心结果图"],
            ["Figure 7", "Page 10", "normalized off-chip transfer", "解释 PIM-Only 为什么在大输入有用、小输入有害", "关键结果图"],
            ["Figure 8", "Page 10", "PageRank graph-size sensitivity", "展示 Locality-Aware 随 graph size 逐步增加 memory-side PEI 比例", "敏感性图"],
            ["Figure 9", "Page 10", "multiprogrammed workloads", "证明混合 workload 下动态选择仍有效", "核心结果图"],
            ["Figure 10", "Page 11", "balanced dispatch", "展示 bandwidth-balance policy 的额外收益", "优化图"],
            ["Figure 12", "Page 12", "energy consumption", "展示 Locality-Aware 能耗最低", "能耗结果图"]
        ],
        "tables": [
            ["Table 1", "Page 8", "implemented PIM operations", "列出 PEI operation 类型及读写属性", "实验基础"],
            ["Table 3", "Page 9", "input sets", "列出 10 个 workloads 的 small/medium/large 输入", "复现实验重要"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文核心是系统架构、执行策略和模拟评估", "公式不是主要学习重点", "否"]
        ],
        "terms": [
            ["PIM-enabled instruction (PEI)", "PIM 使能指令", "Page 2-3", "既可在 host 也可在 memory-side logic 上执行的 ISA extension", "是"],
            ["PEI Computation Unit (PCU)", "PEI 计算单元", "Page 5", "执行 PEI 的 host-side 或 memory-side 硬件单元", "是"],
            ["PEI Management Unit (PMU)", "PEI 管理单元", "Page 5-7", "管理 PEI atomicity、coherence 和 locality profiling", "是"],
            ["Single-cache-block restriction", "单 cache block 限制", "Page 3", "限制单个 PIM operation 访问一个 LLC block", "是"],
            ["Locality-Aware execution", "局部性感知执行", "Page 9", "根据数据局部性选择 host-side 或 memory-side 执行 PEI", "是"],
            ["pfence", "PIM memory fence", "Page 4", "等待之前所有 PEIs 完成的同步指令", "是"]
        ],
        "open_questions": [
            "single-cache-block restriction 是否会限制现代图分析/数据库中更复杂的 PIM primitives？",
            "PEI 的 locality monitor 能否迁移到 HBM/CXL memory expander 场景？",
            "编译器如何自动识别 PEI 插入点并和 ordinary vectorization/pass ordering 协同？"
        ],
    },
    {
        "slug": "rowclone_micro13",
        "title": "RowClone: Fast and Energy-Efficient In-DRAM Bulk Data Copy and Initialization",
        "zh_title": "RowClone：快速且节能的 DRAM 内批量数据复制与初始化",
        "authors": "Vivek Seshadri; Yoongu Kim; Chris Fallin; Donghyuk Lee; Rachata Ausavarungnirun; Gennady Pekhimenko; Yixin Luo; Onur Mutlu; Phillip B. Gibbons; Michael A. Kozuch; Todd C. Mowry",
        "year": "2013",
        "venue": "MICRO-46",
        "arxiv": "未找到",
        "doi": "10.1145/2540708.2540719",
        "topic": "In-DRAM bulk copy and initialization; RowClone-FPM; RowClone-PSM",
        "keywords": "RowClone; Fast Parallel Mode; Pipelined Serial Mode; DRAM row buffer; bulk copy; bulk zeroing; copy-on-write",
        "pages": "13",
        "sections": "Abstract; 1 Introduction; 2 DRAM Background; 3 RowClone Detailed Design; 4 System Support; 5 Applications; 6 Methodology; 7 Evaluation; 8 Related Work; 9 Conclusion; References",
        "one_sentence": "RowClone 利用 DRAM 内部整行激活和 row buffer，将 bulk copy/initialization 完全放在 DRAM 内执行，提出同 subarray 的 FPM 和跨 bank 的 PSM，显著降低 copy/zeroing 的 latency、bandwidth 和 energy。",
        "background": [
            "bulk data copy 和 initialization 常见于 fork/CoW、bulk zeroing、OS 和应用服务；传统系统即使没有计算也必须把数据经 memory channel 来回搬运，见 Page 1-2, Section 1。",
            "DRAM 每次 ACTIVATE 都会把整行 cells 复制到 row buffer，RowClone 的关键观察是可以复用这个内部高带宽路径来复制整行，见 Page 2-4, Sections 2-3。"
        ],
        "problems": [
            "如何减少 bulk copy/initialization 经过 memory channel 带来的 latency、bandwidth 和 energy。",
            "如何在低 DRAM area overhead 下提供同 subarray 与跨 bank 的 copy path。",
            "如何让 ISA、memory controller、cache coherence 和 OS allocator 能安全使用 DRAM 内 copy。"
        ],
        "contributions": [
            "提出 Fast Parallel Mode (FPM)，通过 source ACTIVATE 后紧接 destination ACTIVATE，在同 subarray 内复制整行，见 Page 4, Section 3.1。",
            "提出 Pipelined Serial Mode (PSM)，利用 DRAM chip shared internal bus 在 banks 间流水化传输 cache lines，见 Page 4-5, Section 3.2。",
            "提出 memcopy/meminit ISA support、alignment/size 检测、cache coherence 处理和 OS page allocation support，见 Page 5-7, Section 4。",
            "展示 RowClone 可加速 Copy-on-Write 和 Bulk Zeroing 等系统 primitive，见 Page 7, Section 5。",
            "在 forkbench、六个 copy/initialization-intensive applications 和多核 workloads 中评估性能、带宽和能耗，见 Page 8-12, Section 7。"
        ],
        "method": [
            "FPM 对同一 subarray 的 src/dst 先 ACTIVATE src 把数据装入 row buffer，再 ACTIVATE dst 让已稳定 bitlines 覆盖 dst cells，最后 PRECHARGE；这相当于一次整行 copy，见 Page 4, Figure 4。",
            "PSM 在 source bank 激活源行、destination bank 激活目标行后，用 TRANSFER command 经 shared internal bus 逐 cache line 传输，并重叠读写延迟，见 Page 5, Figure 5。",
            "bulk initialization 预留初始化值行，例如 zero row；通过 FPM/PSM 把该行复制到目标区域，实现 bulk zeroing 或任意值初始化，见 Page 5。",
            "系统集成包括 memcopy/meminit instructions、RowClone-aware page allocation 以提高 FPM 命中、以及 cache coherence 处理 dirty source/destination lines，见 Page 5-7。"
        ],
        "experiments": [
            "raw latency/energy 分析比较 baseline、FPM、inter-bank PSM 和 intra-bank PSM 的 4KB copy/zeroing，见 Page 8-9, Table 3。",
            "forkbench 通过 parent address space size S 和 child updated pages N 控制 copy intensity，比较 FPM/PSM 的 IPC 与 DRAM energy，见 Page 9-10, Figures 7-9。",
            "六个应用包括 bootup、compile、forkbench、mcached、mysql、shell，比较 baseline、RowClone、RowClone-ZI，见 Page 10-11, Table 4/Figures 10-11/Table 5。",
            "多核实验随机组合 copy/initialization-intensive 和 SPEC CPU2006 memory-intensive benchmarks，评估 2/4/8-core 的 weighted speedup、fairness、bandwidth 和 energy，见 Page 11, Table 7。",
            "还与 memory-controller DMA baseline 比较，见 Page 12, Section 7.5。"
        ],
        "results": [
            "4KB copy 中，baseline latency/energy 为 1046ns/3.6µJ，FPM 为 90ns/0.04µJ，即 latency 降低 11.62x、energy 降低 74.4x；4KB zeroing 中 FPM latency/energy 降低 6.06x/41.5x，见 Page 9, Table 3。",
            "inter-bank PSM 对 4KB copy latency/energy 降低 1.93x/3.2x；intra-bank PSM latency 几乎不降但 energy 降低 1.5x，见 Page 9, Table 3。",
            "forkbench 中 FPM peak performance improvement 为 2.2x，平均 30%；DRAM energy 最多降低 80%、平均 50%，见 Page 9-10, Figures 8-9。",
            "六个应用中 copy/initialization 占 memory traffic 的 10%-80%；RowClone-ZI 对 forkbench/shell 分别提升 66%/40%，见 Page 10, Figures 10-11。",
            "RowClone-ZI 在六个应用上将 DRAM energy 降低 15%-69%、bandwidth 降低 16%-81%，见 Page 11, Table 5。",
            "4-core workloads 中 RowClone 平均 weighted speedup 提升 10%，RowClone-ZI 提升 20%；8-core 中 weighted speedup 提升 27%，memory bandwidth/instruction 降低 28%，memory energy/instruction 降低 17%，见 Page 11, Figure 12/Table 7。",
            "memory-controller DMA 平均比 baseline 慢 2%，比 RowClone 慢 16%，且不节省 DRAM energy，见 Page 12, Section 7.5。"
        ],
        "limitations": [
            "FPM 要求 source/destination 在同一 subarray、操作整行对齐，不能部分复制，见 Page 4, Section 3.1。",
            "PSM 更通用但受 shared internal bus 限制，收益远低于 FPM，见 Page 5 与 Page 9。",
            "RowClone 初始化可能导致应用随后访问 zeroed pages 时出现低 MLP cache misses，需要 RowClone-ZI 缓解，见 Page 10。",
            "需要 ISA、memory controller、DRAM peripheral logic、cache coherence 和 OS allocator 的协同，见 Page 5-7。"
        ],
        "focus": [
            "Page 4 Figure 4 是 FPM 的核心，必须理解为什么第二个 ACTIVATE 会覆盖 destination row。",
            "Page 5 Figure 5 是 PSM 的核心，说明跨 bank copy 为什么只能逐 cache line。",
            "Page 9 Table 3 是 raw latency/energy 证据，Page 10-11 Figures/Tables 是端到端证据。",
            "注意 RowClone-ZI：它说明 DRAM 内初始化不等于自动提升性能，cache 行为仍然关键。"
        ],
        "relations": "RowClone 是 LEC4 很多论文的基础 primitive：Ambit 用它复制临时行，LISA/FIGARO 扩展数据移动范围，SIMDRAM 用它做 vertical layout shift 和 operand movement，PiDRAM 则把它端到端原型化。",
        "figures": [
            ["Figure 1", "Page 2", "DRAM chip organization", "展示 banks、subarrays、row buffer 和 internal bus", "背景图"],
            ["Figure 3", "Page 3", "DRAM subarray access steps", "解释 ACTIVATE/READ/PRECHARGE", "背景核心图"],
            ["Figure 4", "Page 4", "Fast Parallel Mode", "展示同 subarray row copy 的电路状态", "核心方法图"],
            ["Figure 5", "Page 5", "Pipelined Serial Mode", "展示 source/destination bank 和 TRANSFER 数据流", "核心方法图"],
            ["Figure 8", "Page 9", "forkbench performance", "展示 FPM/PSM 在不同 N/S 下的 IPC 提升", "核心结果图"],
            ["Figure 9", "Page 10", "forkbench DRAM energy", "展示 FPM/PSM 能耗降低", "核心结果图"],
            ["Figure 11", "Page 10", "application IPC with RowClone-ZI", "展示 RowClone-ZI 解决初始化后 cache miss 问题", "关键结果图"],
            ["Figure 12-13", "Page 11", "multi-core evaluation", "展示多核 weighted speedup 与 copy intensity 关系", "核心结果图"]
        ],
        "tables": [
            ["Table 1", "Page 5", "memcopy/meminit semantics", "定义 RowClone 暴露给软件的 ISA 指令", "系统接口"],
            ["Table 3", "Page 9", "4KB latency and energy", "FPM/PSM 相对 baseline 的 raw benefit", "核心表"],
            ["Table 4", "Page 10", "copy/initialization-intensive benchmarks", "列出六个应用", "实验设计"],
            ["Table 5", "Page 11", "energy and bandwidth reduction", "RowClone-ZI 在所有六个应用上降低 energy/bandwidth", "核心表"],
            ["Table 7", "Page 11", "multi-core metrics", "2/4/8-core 下 speedup、fairness、bandwidth、energy", "核心表"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文主要是 DRAM 操作机制与系统评估", "公式不是主要学习重点", "否"]
        ],
        "terms": [
            ["RowClone", "DRAM 内复制/初始化机制", "Page 1", "通过 DRAM 内部 row buffer 和 internal bus 完成 bulk operations", "是"],
            ["Fast Parallel Mode (FPM)", "快速并行模式", "Page 4", "同 subarray 内用背靠背 ACTIVATE 复制整行", "是"],
            ["Pipelined Serial Mode (PSM)", "流水串行模式", "Page 5", "跨 bank 用 internal bus 逐 cache line 流水复制", "是"],
            ["Bulk Zeroing (BuZ)", "批量置零", "Page 5", "通过复制预置零行初始化目标行", "是"],
            ["FMTC", "copy 造成的内存流量比例", "Page 9", "Fraction of Memory Traffic due to Copies，用于解释 forkbench 收益", "是"],
            ["RowClone-Zero-Insert (RowClone-ZI)", "RowClone 零插入", "Page 10", "zeroing 后同时把 zero cache lines 插入 cache，避免后续低 MLP miss", "是"]
        ],
        "open_questions": [
            "现代 DDR4/DDR5 是否允许 FPM 所需的背靠背 ACTIVATE，或需要 DRAM 标准新增 copy command？",
            "RowClone-aware allocator 在真实 OS 中会如何影响 fragmentation、NUMA 和安全隔离？",
            "RowClone 与 ECC/encryption/compression memory systems 结合时如何保证正确性？"
        ],
    },
    {
        "slug": "simdram_asplos21",
        "title": "SIMDRAM: An End-to-End Framework for Bit-Serial SIMD Computing in DRAM",
        "zh_title": "SIMDRAM：面向 DRAM 内位串行 SIMD 计算的端到端框架",
        "authors": "Nastaran Hajinazar; Geraldo F. Oliveira; Sven Gregorio; João Dinis Ferreira; Nika Mansouri Ghiasi; Minesh Patel; Mohammed Alser; Saugata Ghose; Juan Gómez-Luna; Onur Mutlu",
        "year": "2021",
        "venue": "ASPLOS 2021",
        "arxiv": "未找到",
        "doi": "10.1145/3445814.3446749",
        "topic": "Processing-using-DRAM; bit-serial SIMD; MAJ/NOT synthesis; end-to-end framework",
        "keywords": "SIMDRAM; MAJ; NOT; Majority-Inverter Graph; bit-serial SIMD; Ambit; RowClone; LISA; PuM",
        "pages": "21",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 SIMDRAM Overview; 4 SIMDRAM Framework; 5 System Integration; 6 Methodology; 7 Evaluation; 8 Related Work; 9 Conclusion; Appendix; References",
        "one_sentence": "SIMDRAM 把 Ambit 式 MAJ/NOT DRAM primitive 组织成端到端框架，通过自动合成 MAJ/NOT 表示、分配计算行并生成 DRAM µProgram，让用户可在 DRAM 内执行灵活的 bit-serial SIMD operations。",
        "background": [
            "processing-using-DRAM 直接利用 DRAM cell/sense amplifier 行为，拥有高内部带宽和阵列并行性，但已有 Ambit 类方案主要支持 AND/OR/NOT 或少量固定操作，见 Page 1-2, Section 1。",
            "复杂操作需要 shift、add、compare、multiply、bitcount、ReLU 等；SIMDRAM 选择 vertical data layout 与 MAJ/NOT 作为逻辑完备基础，见 Page 2, Section 1。"
        ],
        "problems": [
            "如何把任意用户定义的 operation 转换成高效 MAJ/NOT-based in-DRAM implementation。",
            "如何在有限 B-group/C-group rows 中为 operands/intermediates 分配 DRAM rows，并生成正确 DRAM command sequence。",
            "如何提供 ISA、programming interface、control unit、page/coherence/transposition 支持，使 PuM 从 primitive 变成端到端框架。"
        ],
        "contributions": [
            "提出首个面向 processing-using-DRAM 的 flexible end-to-end framework，支持 wide range of operations，见 Page 1-3。",
            "提出三步流程：生成 efficient MAJ/NOT representation，分配 DRAM rows 并生成 µProgram，由 SIMDRAM control unit 执行，见 Page 1 与 Page 5, Figure 3。",
            "使用 Majority-Inverter Graph (MIG) transformation rules 优化 MAJ/NOT 实现，见 Appendix/Page 19, Table 4/Figure 15。",
            "支持 16 类 operations，包括 arithmetic、relational、predication、bitcount、ReLU、reduction 等，见 Page 21, Table 5。",
            "提供 ISA/programming/hardware support，包括 bbop instructions、µProgram scratchpad、control unit 和 transposition unit，见 Page 9-11 与 Page 15。",
            "在 16 operations、7 个真实 kernels、reliability、data movement、transposition、area 上系统评估，见 Page 12-15。"
        ],
        "method": [
            "Step 1 将 AND/OR/NOT logic 转为 optimized MAJ/NOT implementation；MAJ/NOT 是逻辑完备集合，常比先生成 AND/OR 再映射到 Ambit 更少 DRAM commands，见 Page 4-5 与 Page 19。",
            "Step 2 根据 MIG dependency 把 operands 和 intermediate values 分配到 SIMDRAM 的 B-group/C-group/D-group rows，并生成 AP/AAP µOps，见 Page 5 与 Appendix Algorithm 1。",
            "Step 3 中 memory controller 内的 SIMDRAM control unit 读取 µProgram，发出 DRAM commands，管理 computation start-to-end，见 Page 5, Figure 3。",
            "SIMDRAM 使用 vertical data layout：一个 operand 的 bit 放在同一 DRAM column 上下排列，每条 bitline 成为 SIMD lane；shift 可通过 row copy 实现，见 Page 2。",
            "系统层面处理 page faults、address translation、coherence、interrupts、limited subarray size、security 和 limitations，见 Page 10-11, Sections 5.3-5.6。"
        ],
        "experiments": [
            "使用 gem5 实现 SIMDRAM，与 Intel Skylake CPU、NVIDIA Titan V GPU 和 Ambit 比较；CPU 使用 AVX-512，GPU 使用真实计时和 nvml energy，见 Page 11-12, Section 6/Table 2。",
            "synthetic evaluation 测试 16 operations，在 8/16/32/64-bit element sizes 和 1/4/16 DRAM banks 下报告 throughput 与 energy efficiency，见 Page 12-13, Figures 9-10。",
            "真实 kernels 包括 BitWeaving、TPC-H Q1、kNN、LeNET、VGG-13、VGG-16、brightness，见 Page 13, Figure 11。",
            "可靠性用 SPICE/Monte-Carlo 评估 TRA、back-to-back TRA 与 QRA 在 45/32/22nm 和不同 process variation 下失败率，见 Page 14, Table 3。",
            "还评估 data movement overhead、data transposition overhead 和 area overhead，见 Page 14-15, Figures 13-14/Section 7.8。"
        ],
        "results": [
            "单 DRAM bank 上，SIMDRAM 在 16 operations 上平均提供 Ambit 的 2.0x throughput 与 2.6x energy efficiency；在 7 个 kernels 上平均提供 Ambit 的 2.5x performance，见 Page 1-2 与 Page 12-13。",
            "16 banks 上，SIMDRAM 在 16 operations 上提供 CPU/GPU 的 88x/5.8x throughput，以及 257x/31x energy efficiency，见 Page 1-2 与 Page 12-13, Figures 9-10。",
            "7 个 real-world kernels 上，SIMDRAM:16 平均提供 CPU/GPU 的 21x/2.1x performance；BitWeaving 最高为 CPU/GPU 的 65x/5.4x，见 Page 13, Figure 11。",
            "SIMDRAM:1 在所有 kernels 上都超过 CPU，平均 2.9x；SIMDRAM:1 相比 Ambit 平均 2.5x，TPC-H 最高 4.8x，见 Page 13。",
            "相对 DualityCache:Realistic，SIMDRAM:16 在 addition/subtraction/multiplication/division latency 上分别平均快 52.9x/52.4x/1.8x/2.1x，并平均能耗低 600x，见 Page 13-14, Figure 12。",
            "TRA/TRAb2b 在 ±5% process variation 下无错误；22nm 时 QRA 无法正确工作，而 TRA 在 ±10%/±20% variation 下失败率为 0.42%/4.50%，见 Page 14, Table 3。",
            "worst-case intra-bank data movement overhead 平均 0.39%，inter-bank 平均 17.5%；data transposition overhead 在 SIMDRAM:1/SIMDRAM:16 中平均 7.1%/44.6%，见 Page 14-15, Figures 13-14。",
            "SIMDRAM 相比 Ambit 不增加 DRAM circuitry；memory controller 中 control/transposition units 面积约为 high-end CPU die 的 0.2%，见 Page 15, Section 7.8。"
        ],
        "limitations": [
            "当前框架只支持 integer/fixed-point operations；floating-point operations 因 mantissa alignment 和 per-bitline shift 等问题仍然困难，见 Page 11, Section 5.6。",
            "不能低成本支持跨 bitline shuffle/reduction，除非增加 dedicated bit-shift/shuffle circuitry，见 Page 11。",
            "需要程序员手动改写或未来编译器插入 bbop instructions；自动 compiler backend 留给未来工作，见 Page 10, Section 5.2。",
            "输入数据需在 DRAM 中且需要 cache flush/pinning，coherence 目前依赖程序员负责 flush，见 Page 10-11, Section 5.3。",
            "SIMDRAM 可能增加 RowHammer vulnerability，防护机制需另行研究，见 Page 11, Section 5.5。"
        ],
        "focus": [
            "Page 2 的 vertical layout + MAJ/NOT 是理解 SIMDRAM 的关键抽象。",
            "Page 5 Figure 3 是三步框架总览，建议优先看。",
            "Page 19 Figure 15/Table 4 展示 full addition 如何从 AND/OR/NOT 转成 MAJ/NOT。",
            "Page 12-14 Figures 9-13 与 Table 3 是性能、能耗、可靠性核心证据。",
            "Page 10-11 的 system integration/limitations 决定 SIMDRAM 是否能落地。"
        ],
        "relations": "SIMDRAM 站在 RowClone、Ambit、LISA 之上：RowClone/LISA 提供数据移动，Ambit 提供 TRA/DCC primitive，SIMDRAM 则提供自动合成、编程接口和控制单元，把 primitive 组合成通用 PuM 框架。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM organization", "说明 SIMDRAM 依赖的 subarray/bitline/row buffer 结构", "背景图"],
            ["Figure 2", "Page 4", "SIMDRAM subarray organization", "展示 D-group/C-group/B-group rows 与 DCC", "核心结构图"],
            ["Figure 3", "Page 5", "SIMDRAM framework", "展示 MAJ/NOT synthesis、row allocation、µProgram execution 三步", "核心总览图"],
            ["Figure 9", "Page 12", "throughput of 16 operations", "比较 CPU/GPU/Ambit/SIMDRAM", "核心结果图"],
            ["Figure 10", "Page 13", "energy efficiency of 16 operations", "展示 SIMDRAM throughput per watt 优势", "核心结果图"],
            ["Figure 11", "Page 13", "real-world kernel speedup", "展示 7 个 kernels 的端到端收益", "核心结果图"],
            ["Figure 12", "Page 13", "DualityCache comparison", "展示考虑 DRAM-to-cache movement 后 SIMDRAM 优势", "对比图"],
            ["Figure 13", "Page 14", "data movement overhead", "展示 intra/inter-bank movement overhead", "开销图"],
            ["Figure 14", "Page 15", "data transposition overhead", "展示 vertical layout 转置成本", "开销图"],
            ["Figure 15", "Page 19", "full addition MIG synthesis", "展示 MAJ/NOT transformation 过程", "方法细节图"]
        ],
        "tables": [
            ["Table 2", "Page 11", "evaluated system configurations", "列出 CPU/GPU/Ambit/SIMDRAM 参数", "实验设计"],
            ["Table 3", "Page 14", "TRA/QRA failure rates", "TRA/TRAb2b 比 QRA 更可靠，±5% 无错误", "可靠性核心表"],
            ["Table 4", "Page 19", "MAJ/NOT transformation rules", "MIG 优化规则", "方法核心表"],
            ["Table 5", "Page 21", "evaluated SIMDRAM operations", "16 operations 的 latency scaling 和表达式", "操作覆盖表"]
        ],
        "equations": [
            ["MAJ(A,B,C)=A·B+A·C+B·C", "Page 3, Section 2.2.2", "三输入 majority operation 定义", "TRA 的逻辑抽象", "是"],
            ["MIG transformation rules", "Page 19, Table 4", "把 AND/OR/NOT graph 转成 MAJ/NOT graph", "SIMDRAM synthesis 的形式化基础", "是"]
        ],
        "terms": [
            ["SIMDRAM", "DRAM 内 bit-serial SIMD 框架", "Page 1", "用 MAJ/NOT 和 vertical layout 支持通用 PuM operations", "是"],
            ["Majority operation (MAJ)", "多数逻辑", "Page 3", "三个输入中多数为 1 则输出 1，是 TRA 的逻辑模型", "是"],
            ["Vertical data layout", "垂直数据布局", "Page 2", "一个元素的 bits 沿同一 bitline 分布，使 bitline 成为 SIMD lane", "是"],
            ["Majority-Inverter Graph (MIG)", "多数-反相图", "Page 19", "用 MAJ/NOT 表示和优化逻辑的图结构", "是"],
            ["bbop instruction", "bulk bitwise operation 指令", "Page 9-10", "程序员/编译器调用 SIMDRAM operation 的 ISA 接口", "是"],
            ["µProgram", "微程序", "Page 5", "SIMDRAM control unit 执行的 DRAM command sequence", "是"],
            ["Transposition unit", "转置单元", "Page 15", "负责 horizontal/vertical layout 转换的 memory-controller 结构", "是"]
        ],
        "open_questions": [
            "SIMDRAM 如何高效支持 floating-point、shuffle 和 cross-bitline reduction？",
            "程序员手动改写 bbop 的负担多大，实际 compiler backend 能否自动完成？",
            "SIMDRAM 对 RowHammer、ECC、memory encryption 和 data layout security 的影响如何处理？"
        ],
    },
    {
        "slug": "stone_logic_in_memory_1970",
        "title": "A Logic-in-Memory Computer",
        "zh_title": "一种 Logic-in-Memory 计算机",
        "authors": "Harold S. Stone",
        "year": "1970",
        "venue": "IEEE Transactions on Computers, Short Notes",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "Early logic-in-memory architecture; logic-enhanced cache; sector operations",
        "keywords": "logic-in-memory; cache memory; sector operations; associative search; sector add; bit-slice mode",
        "pages": "6",
        "sections": "Abstract; I Introduction; II A Computer Organization Containing a High-Speed Buffer Memory; III Logic-in-Memory Cache Organization; IV Logic-in-Memory Caches Operating Under Program Control; V Discussion; References",
        "one_sentence": "Stone 1970 提出把带组合逻辑的 memory array 作为高速 cache，使主存对程序表现得像由多个 logic-in-memory sectors 组成，从而以 sector-level 并行操作提升性能。",
        "background": [
            "作者从 1970 年的微电子趋势出发：未来封装成本可能更多由 pins 而非 gates 决定，因此在 memory array 中增加逻辑可能具有经济吸引力，见 Page 1, Introduction。",
            "论文借鉴 IBM 360/85 cache、Atlas virtual memory 和 Wilkes slave memory，把 logic-in-memory array 嵌入 cache 层，而不是把每个 array 当作孤立功能单元，见 Page 2, Section I-II。"
        ],
        "problems": [
            "如何把 cellular logic-in-memory arrays 嵌入通用计算机系统，而不是仅作为孤立 associative memory 或特殊功能单元。",
            "如何让主存看起来拥有 logic-enhanced cache 的处理能力和接近 cache 的性能。",
            "如何设计 sector-level operations 和程序控制，使高并行 memory-side logic 对程序可见。"
        ],
        "contributions": [
            "提出以 logic-enhanced cache memory array 为中心的 logic-in-memory computer 组织，见 Page 1, Abstract 与 Page 3。",
            "把操作组织为 sectors 上的 parallel operations，包括 associative search、tag bit operations、sector add、sector scale、sector multiply/copy，见 Page 3-4。",
            "指出 cache/control mechanism 可让主存对程序表现得像每个 sector 都是 independent logic-in-memory array，见 Page 3-4。",
            "讨论显式 cache control、matrix row/column access、bit-slice mode 和高层语言支持，见 Page 4-6。",
            "把 logic-in-memory 视为 general-purpose 而非单一专用 associative/Solomon-like computer，见 Page 5。"
        ],
        "method": [
            "基础组织是 cache-organized computer：CPU 请求先到 cache，miss 时把主存 sector 调入 cache；如果 cache sector 是 logic-in-memory array，CPU 就能对逻辑增强 sector 发出操作，见 Page 2-3, Figure 1。",
            "sector operations 以一个或两个 sector 为粒度，例如 Search on Masked Equality/Threshold、Copy Tag Bit、Tag Bit AND/OR/XOR/NOT、Sector ADD/Scale，见 Page 3-4。",
            "sector add 可用一组 adders 服务所有 cache sectors，通过 cache output/input buses 和寄存器 R 完成对应 words 的并行加法，见 Page 4, Figure 2。",
            "program control 可显式 hold/release sectors、提示 sequential data、控制 cache load 方式；bit-slice mode 则让 cache 同时装入许多 words 的同一 bit slice，以支持 mass arithmetic，见 Page 4-5。"
        ],
        "experiments": [
            "本文是概念性 Short Notes，没有现代意义上的原型实现或 benchmark evaluation。",
            "作者引用 IBM 360/85 cache 模拟结果：超过 95% CPU memory requests 命中 cache，整体性能达到“整个主存都像 cache 一样快”的机器的 80%，见 Page 3, Section II。",
            "论文用 qualitative reasoning 分析 microelectronics cost、pin limitation、cache sector operations 和 programming-language support，见 Page 1-6。"
        ],
        "results": [
            "摘要声称 logic-in-memory computer 由于 high-speed, highly parallel sector operations，指向 orders-of-magnitude performance increase 的新方向，见 Page 1, Abstract。",
            "IBM 360/85 相关模拟显示 cache hit 超过 95%，总性能达到理想高速主存机器的 80%，且 cache 只有主存的几个百分点大小，见 Page 3, Section II。",
            "作者认为若 microelectronic cost 足够下降，masked equality search 这类每 bit 少量 gates 的功能已可实现，sector add/multiply 等更复杂功能未来也可能合理，见 Page 4。",
            "bit-slice access 可使一个 sector 同时容纳 m×n 个 words 的一位，从而用 AND/OR/XOR/NOT 在 cache 中做 mass arithmetic，例如 m×n simultaneous additions，见 Page 5。",
            "结论强调该机器是 general-purpose by nature，但实际价值取决于 microelectronics 进步、适配算法和高层语言能否暴露新 instructions，见 Page 5-6。"
        ],
        "limitations": [
            "论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。",
            "可行性强依赖当时对 microelectronic packaging/pin/gate cost 的预测，见 Page 1 和 Page 4。",
            "作者明确指出 instruction repertoire 的实际 utility 难以衡量，是 future research，见 Page 4。",
            "高层语言与 unconventional instruction repertoire 不匹配，若编译器目标语言只用普通指令，强大 memory-side instructions 难以带来实际收益，见 Page 6。"
        ],
        "focus": [
            "Page 1 的 Abstract 很值得读：它已经提出 logic-enhanced cache、sector operations 和主存抽象三件事。",
            "Page 2-3 对 IBM 360/85 cache 的讨论是理解“为什么放在 cache 层”的关键。",
            "Page 3-4 的 sector instruction examples 是本文最接近 ISA/operation design 的部分。",
            "Page 5-6 关于 bit-slice mode 和 high-level languages 的讨论很现代，能和 SIMDRAM/PEI 对照。"
        ],
        "relations": "Stone 1970 是早期 logic-in-memory/PIM 思想源头之一：它不像现代 DRAM PuM 论文那样使用 sense amplifier 或 RowClone，而是从 cache organization、sector operations 和编程语言可用性角度预见了后来的 PIM 系统问题。",
        "figures": [
            ["Figure 1", "Page 2", "cache-organized computer", "展示 processor-control-memory 的 cache buffer 组织", "背景结构图"],
            ["Figure 2", "Page 4", "word slice of logic-in-memory cache with sector add", "展示 sector add 如何由 adders 和 cache buses 支持", "核心示意图"]
        ],
        "tables": [
            ["未检测到核心编号表", "全文", "本文无核心数据表", "以概念描述为主", "否"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文不是公式驱动论文", "概念和架构组织是重点", "否"]
        ],
        "terms": [
            ["Logic-in-memory array", "逻辑内存阵列", "Page 1", "每个 storage element 附带组合逻辑的 memory array", "是"],
            ["Logic-enhanced cache", "逻辑增强 cache", "Page 1-3", "作为 CPU 与主存之间高速 buffer 的 logic-in-memory array", "是"],
            ["Sector", "扇区/数据块", "Page 1-4", "logic-in-memory operations 的块级操作单位", "是"],
            ["Associative search", "关联搜索", "Page 3", "在 sector 内按 masked equality/threshold 查找 words", "是"],
            ["Sector ADD", "扇区加法", "Page 4", "两个 sectors 对应 words 并行相加", "是"],
            ["Bit-slice mode", "位片模式", "Page 5", "从许多 words 中取同一 bit slice 放入 cache 并并行处理", "是"],
            ["High-level language mismatch", "高层语言不匹配", "Page 6", "语言语义无法表达机器强指令导致其难以被编译器使用", "是"]
        ],
        "open_questions": [
            "Stone 的 sector operation 抽象和现代 SIMDRAM/PEI 的 ISA abstraction 有哪些共同点和差异？",
            "如果把 logic-enhanced cache 换成现代 HBM logic layer 或 near-cache accelerator，哪些设计仍成立？",
            "高层语言如何自然表达 memory-side sector/bit-slice operations，这个问题在现代 PIM 编译器中如何解决？"
        ],
    },
]


if __name__ == "__main__":
    write_papers(PAPERS, status="第五轮 4 篇深度阅读完成")
    print(f"Wrote batch 5 files for {len(PAPERS)} papers")
