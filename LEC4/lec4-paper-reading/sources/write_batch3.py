from write_batch1 import write_papers


PAPERS = [
    {
        "slug": "SimplePIM_pact23",
        "title": "SimplePIM: A Software Framework for Productive and Efficient Processing-in-Memory",
        "zh_title": "SimplePIM：面向高生产率和高效率 Processing-in-Memory 的软件框架",
        "authors": "Jinfan Chen; Juan Gómez-Luna; Izzat El Hajj; Yuxin Guo; Onur Mutlu",
        "year": "2023",
        "venue": "PACT 2023",
        "arxiv": "未找到",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/SimplePIM",
        "topic": "PIM programming framework; UPMEM; iterators; collective communication",
        "keywords": "SimplePIM; UPMEM; map; reduce; zip; broadcast; scatter; gather; allreduce; allgather",
        "pages": "12",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 SimplePIM Programming Framework; 4 Implementation and Optimizations; 5 Evaluation; 6 Discussion; 7 Related Work; References",
        "one_sentence": "SimplePIM 用管理、通信和处理三类高层接口把 UPMEM 的数据分布、scratchpad 管理和通信细节隐藏起来，让程序员用 map/reduce/zip 等迭代器高效编写真实 PIM 程序。",
        "background": [
            "UPMEM 是首个商用 general-purpose PIM 系统，但程序员需要手动分布数据、启动 PIM kernels、管理 DRAM bank 与 scratchpad transfer，并协调多线程，见 Page 1-2, Sections 1-2。",
            "作者把 PIM 系统类比为受 host CPU 统一协调的分布式系统：PIM cores 有自己的内存区域，但通信和元数据管理由 host 负责，见 Page 1。"
        ],
        "problems": [
            "如何降低真实 UPMEM PIM 系统的编程门槛。",
            "如何提供 Host-PIM 与 PIM-PIM communication primitives，同时避免程序员处理 alignment、transfer size 和 metadata。",
            "如何在提高代码生产率的同时保持或提升手写优化代码性能。"
        ],
        "contributions": [
            "提出 SimplePIM，这是面向 real PIM systems 的 high-level programming framework，见 Page 1-2。",
            "提供 management interface，用 ID/metadata 管理 PIM-resident arrays，见 Page 3, Section 3.1。",
            "提供 communication interface，包括 broadcast、scatter、gather、allreduce 和 allgather，见 Page 3-5, Section 3.2。",
            "提供 processing interface，包括 map、reduce、zip 等 iterator，见 Page 3 与 Section 3.3-4。",
            "在六个应用上评估 SimplePIM，相比 hand-optimized UPMEM 代码减少 66.5%-83.1% LoC，并在三项任务上加速 1.10x-1.43x，见 Page 1-2 与 Page 7-9。"
        ],
        "method": [
            "management interface 在 host CPU 上集中保存 PIM array 的 ID、长度、类型和 PIM DRAM 地址，支持 lookup/register/free，见 Page 3。",
            "communication interface 把 host-PIM 和 PIM-PIM 通信包装成 collective primitives；PIM-PIM 通信通过 host 透明完成，见 Page 3-5。",
            "processing interface 用 map、reduce、zip 处理 arbitrary arrays，使应用逻辑与 PIM cores/threads 的并行分解解耦，见 Page 3 与 Page 5-6。",
            "实现中加入 lazy zip、transfer-size tuning、reduction variants 和 UPMEM-specific optimizations，见 Page 6-9。"
        ],
        "experiments": [
            "六个应用包括 reduction、vector addition、histogram、linear regression、logistic regression 和 K-means，见 Page 7, Section 5.1。",
            "baseline 为 PrIM benchmark 和 prior hand-tuned UPMEM implementations，实验在最多 2432 PIM cores 上做 weak/strong scaling，见 Page 7-9。",
            "生产率用 effective PIM-related lines of code 衡量，性能用 execution time 分解为 CPU time 和 PIM kernel time，见 Page 7-9。"
        ],
        "results": [
            "SimplePIM 的 LoC reduction 为 2.98x-5.93x；例如 histogram 从 114 行降到 21 行，K-means 从 206 行降到 68 行，见 Page 7, Table 1。",
            "weak scaling 中，SimplePIM 在 vector addition、logistic regression、K-means 上分别比 hand-optimized 快 1.10x、1.17x、1.37x，见 Page 9, Figure 9。",
            "strong scaling 中，SimplePIM 在上述三项上平均加速 1.15x、1.22x、1.43x；reduction、histogram、linear regression 性能大体相当，见 Page 9, Figure 10。",
            "strong scaling 中除 reduction 外，SimplePIM 在五个 workload 上用 2x PIM cores 得到超过 1.8x speedup，用 4x PIM cores 得到超过 3x speedup，见 Page 9。",
            "histogram 的 reduction variant 表明 shared accumulator 与 thread-private accumulator 的优劣取决于 bin 数和 scratchpad 占用，见 Page 9, Figure 11。"
        ],
        "limitations": [
            "当前实现针对 UPMEM，虽然框架思想可迁移，但其他 PIM 架构需要重新实现 backend，见 Page 9-10, Section 6。",
            "目前主要支持 map/reduce/zip；prefix sum/filter 可扩展，但 stencil、convolution、tree/irregular access 更困难，见 Page 10。",
            "PIM-PIM communication 仍通过 host 模拟，硬件缺少直接 PIM core 通信会限制部分应用，见 Page 10。",
            "hand-optimized 代码若手动采用相同优化，理论上可达到或超过 SimplePIM；SimplePIM 的主要价值是替程序员自动承担这些工作，见 Page 9。"
        ],
        "focus": [
            "Page 2 Figure 1 先理解 UPMEM 架构和编程难点。",
            "Page 3-6 的三个接口是 SimplePIM 设计主体。",
            "Page 7 Table 1 是生产率证据，Page 8-9 Figures 9-11 是性能证据。",
            "Page 10 Discussion 说明 SimplePIM 未来扩展边界。"
        ],
        "relations": "SimplePIM 是 DaPPA 的前序/相邻工作：两者都降低 UPMEM 编程复杂度，但 DaPPA 更进一步自动管理 dataflow 和 template-based compilation。",
        "figures": [
            ["Figure 1", "Page 2", "UPMEM PIM architecture", "展示 host、PIM DRAM banks、PIM cores、scratchpad 和 instruction memory", "背景核心图"],
            ["Figure 9", "Page 8", "weak scaling results", "比较 SimplePIM 与 hand-optimized 的执行时间", "核心结果"],
            ["Figure 10", "Page 9", "strong scaling results", "展示不同 PIM core 数下的 strong scaling", "核心结果"],
            ["Figure 11", "Page 9", "histogram reduction variants", "分析 shared accumulator 与 thread-private accumulator", "优化细节"]
        ],
        "tables": [
            ["Table 1", "Page 7", "lines of effective PIM-related code", "SimplePIM 减少 2.98x-5.93x 代码量", "生产率核心证据"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文以软件框架和实验为主", "公式不是重点", "否"]
        ],
        "terms": [
            ["SimplePIM", "PIM 高层软件框架", "Page 1", "用高层 API 简化真实 PIM 编程", "是"],
            ["Management interface", "管理接口", "Page 3", "集中管理 PIM-resident array metadata", "是"],
            ["Communication interface", "通信接口", "Page 3-5", "提供 broadcast/scatter/gather/allreduce/allgather", "是"],
            ["Processing interface", "处理接口", "Page 3", "提供 map/reduce/zip iterators", "是"],
            ["UPMEM", "商用 PIM 系统", "Page 1-2", "带有 DRAM 内 PIM cores 的商用系统", "是"],
            ["Scratchpad memory", "软件管理暂存存储", "Page 2", "每个 PIM core 的 64KB 本地存储", "是"]
        ],
        "open_questions": [
            "SimplePIM 如何支持 irregular graph/tree workloads？",
            "如果 UPMEM 后续硬件支持直接 DPU-DPU 通信，SimplePIM 的 collective API 如何优化？",
            "SimplePIM 与 DaPPA 的 pattern/Pipeline 抽象能否合并成统一 PIM 编程层？"
        ],
    },
    {
        "slug": "TOM-programmer-transparent-GPU-near-data-processing_isca16",
        "title": "Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems",
        "zh_title": "TOM：在 GPU 系统中实现程序员透明的 Near-Data Processing",
        "authors": "Kevin Hsieh; Eiman Ebrahimi; Gwangsun Kim; Niladrish Chatterjee; Mike O'Connor; Nandita Vijaykumar; Onur Mutlu; Stephen W. Keckler",
        "year": "2016",
        "venue": "ISCA 2016",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "Near-data processing; GPU; 3D-stacked memory; transparent offloading and data mapping",
        "keywords": "TOM; NDP; GPU; 3D-stacked memory; offloading; data mapping; memory bandwidth",
        "pages": "13",
        "sections": "Abstract; 1 Introduction; 2 Motivation; 3 Mechanism; 4 Implementation; 5 Methodology; 6 Evaluation; 7 Related Work; References",
        "one_sentence": "TOM 通过编译器选择可 offload 的 memory-intensive code blocks，并用软硬件协同数据映射把 offloaded code 与数据共置，从而无需程序员修改 GPU 程序即可利用 3D-stacked memory logic layer。",
        "background": [
            "GPU 应用常受 off-chip memory bandwidth 限制；3D-stacked memory 的 logic layer 可以放置 SMs 并靠 TSV 获得高内部带宽，见 Page 1, Section 1。",
            "NDP 系统面临两个核心问题：哪些代码应在 main GPU 还是 memory stack SMs 执行，以及数据如何映射到多个 memory stacks，见 Page 1。"
        ],
        "problems": [
            "如何不让程序员手动标注 offloading code。",
            "如何在多个 memory stacks 中放置数据，使 offloaded code 和访问数据尽量共置，同时不损害 main GPU 的带宽利用。",
            "如何根据运行时资源状况控制 offloading aggressiveness，避免 memory stack SMs 成为瓶颈。"
        ],
        "contributions": [
            "提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。",
            "提出 programmer-transparent data mapping，利用 offloaded blocks 的可重复内存访问模式预测页面映射，见 Page 2 与 Page 4-6, Section 3.2。",
            "提出 runtime offloading control，根据 SM 与 bandwidth utilization 动态决定候选 block 是否实际 offload，见 Page 2 与 Page 6。",
            "在 10 个 memory-intensive GPGPU workloads 上评估 TOM，见 Page 8-12。",
            "展示平均 30%、最高 76% 性能提升，并降低 off-chip traffic 和 energy，见 Page 2 与 Page 9-10。"
        ],
        "method": [
            "编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。",
            "data mapping 机制在 learning phase 评估简单 address mapping options，预测 offloaded block 将访问的 pages，并将这些 pages 放到最接近 offloaded code 的 stack，见 Page 4-6。",
            "offloading control 防止过度 offload：当 memory stack SMs 的 pending requests 或资源压力过大时，候选 block 可继续在 main GPU 执行，见 Page 6 与 Page 9。",
            "实现上增加 offloading metadata table、memory allocation table 和 memory map analyzer 等结构，见 Page 6-7。"
        ],
        "experiments": [
            "使用 Rodinia、GPGPU-Sim workloads 和 CUDA SDK 中 10 个 memory-intensive GPU applications，见 Page 8-9, Table 2。",
            "指标包括 IPC speedup、off-chip memory traffic、energy consumption、warp capacity sensitivity、internal/cross-stack bandwidth sensitivity 和 area，见 Page 9-12。",
            "baseline 是不能 offload 到 3D-stacked memories 的 GPU 系统；比较不同 NDP offloading/mapping policies，见 Page 9。"
        ],
        "results": [
            "TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。",
            "programmer-transparent data mapping 相比 baseline memory mapping 平均额外提升 10%；例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，见 Page 9。",
            "没有 offloading control 时，系统平均变慢 3%/7%；controlled offloading 将 offloaded instructions 从 46.4% 降到 15.7%，避免 memory stack SMs 成瓶颈，见 Page 9-10。",
            "TOM 平均降低 off-chip memory traffic 38%、最高 99%，平均降低 energy 11%、最高 37%，见 Page 2 与 Page 10。",
            "把 memory stack SM warp capacity 提高到 4x 可在保持约 29% speedup 的同时额外节省 20% memory traffic，见 Page 11, Figures 11-12。",
            "即使 internal bandwidth 等于 external link bandwidth，TOM 平均仍有 28% speedup，见 Page 11, Figure 13。"
        ],
        "limitations": [
            "TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。",
            "data mapping 假设 offloaded block 的访问模式具有可重复性；BFS 这类 irregular workload 可能被错误映射拖慢，见 Page 9。",
            "编译器分析使用保守静态估计和 PTX 工具链，真实 GPU ISA/驱动中的实现会更复杂，见 Page 3 与 Page 8。",
            "offloading aggressiveness 仍可改进，尤其是 offloaded block 中 ALU 指令比例较高时，见 Page 11。"
        ],
        "focus": [
            "Page 1 的两个 Challenge 是 TOM 的设计入口。",
            "Page 3 Equations 1-4 是 offload candidate cost model 的关键。",
            "Page 4-6 的 mapping learning/prediction 解释 TOM 如何做到 programmer-transparent。",
            "Page 9-12 Figures 8-13 是性能、traffic、energy 和敏感性核心证据。"
        ],
        "relations": "TOM 属于 processing-near-memory/3D-stacked memory logic layer 路线，与 Ambit/PuD 不同：它在 memory stack logic layer 放计算单元，而不是用 DRAM cell/sense amplifier 本身计算。",
        "figures": [
            ["Figure 1", "Page 1", "NDP GPU system overview", "展示 main GPU、memory stacks、logic-layer SMs 和 cross-stack links", "架构入口"],
            ["Figure 2", "Page 2", "ideal offloading speedup", "说明静态 offload selection 的潜在收益", "动机图"],
            ["Figure 3", "Page 2", "ideal memory mapping speedup", "说明数据映射也很重要", "动机图"],
            ["Figure 7", "Page 6", "NDP hardware block diagram", "展示 TOM 需要的硬件/软件结构", "实现图"],
            ["Figure 8", "Page 10", "speedup under policies", "TOM 核心性能结果", "核心结果"],
            ["Figure 9-10", "Page 10", "memory traffic and energy", "展示 traffic/energy 降低", "核心结果"],
            ["Figure 11-13", "Page 11", "warp capacity/internal bandwidth sensitivity", "说明设计参数影响", "敏感性分析"]
        ],
        "tables": [
            ["Table 2", "Page 8-9", "evaluated workloads", "列出 10 个 memory-intensive GPU workloads", "实验设计"]
        ],
        "equations": [
            ["Equations 1-4", "Page 3", "offloading bandwidth cost-benefit", "估计 live-in/out register transfer 与 load/store traffic 节省", "是"]
        ],
        "terms": [
            ["Near-Data Processing (NDP)", "近数据处理", "Page 1", "把计算放到数据附近，例如 3D-stacked memory logic layer", "是"],
            ["Transparent Offloading and Mapping (TOM)", "透明卸载与映射", "Page 1-2", "自动选择 offload code 并映射数据的机制组合", "是"],
            ["Memory stack", "内存堆叠", "Page 1", "含 DRAM layers 与 logic layer 的 3D-stacked memory", "是"],
            ["Offload candidate", "卸载候选代码块", "Page 3", "编译器认为 offload 可节省带宽的 instruction block", "是"],
            ["tmap", "透明数据映射", "Page 9", "TOM 的 programmer-transparent mapping policy", "是"],
            ["Offloading aggressiveness control", "卸载激进度控制", "Page 9", "运行时决定是否真的 offload candidate blocks", "是"]
        ],
        "open_questions": [
            "TOM 的 mapping predictor 如何适应 phase behavior 更剧烈的现代 GPU workloads？",
            "在 HBM/CXL 等新内存系统中，TOM 的 offload/mapping cost model 是否仍成立？",
            "是否能把 TOM 的透明 offloading 思路迁移到 UPMEM 或其他 PIM 系统？"
        ],
    },
    {
        "slug": "ambit-bulk-bitwise-dram_micro17",
        "title": "Ambit: In-Memory Accelerator for Bulk Bitwise Operations Using Commodity DRAM Technology",
        "zh_title": "Ambit：使用商用 DRAM 技术的批量按位操作内存内加速器",
        "authors": "Vivek Seshadri; Donghyuk Lee; Thomas Mullins; Hasan Hassan; Amirali Boroumand; Jeremie Kim; Michael A. Kozuch; Onur Mutlu; Phillip B. Gibbons; Todd C. Mowry",
        "year": "2017",
        "venue": "MICRO-50",
        "arxiv": "未找到",
        "doi": "10.1145/3123939.3124544",
        "topic": "In-DRAM bitwise accelerator; Ambit; TRA; bulk bitwise operations",
        "keywords": "Ambit; Triple-Row Activation; RowClone; DCC; bulk bitwise operations; DRAM; MICRO 2017",
        "pages": "15",
        "sections": "Abstract; 1 Introduction; 2 DRAM Background; 3 Ambit-AND-OR; 4 Ambit-NOT; 5 Design and System Integration; 6 SPICE Simulations; 7 Throughput and Energy; 8 Applications; 9 Related Work; References",
        "one_sentence": "Ambit 利用 triple-row activation 和 dual-contact cell，在 commodity DRAM 内直接执行 bulk AND/OR/NOT，从而让大型 bitvector 操作摆脱外部内存带宽瓶颈。",
        "background": [
            "bitmap indices、BitWeaving、BitFunnel、DNA、encryption、graph 和 networking 等应用大量使用 bulk bitwise operations，传统 CPU/GPU/HMC 受外部内存带宽限制，见 Page 1-2。",
            "Ambit 的目标是使用 DRAM analog operation 和内部 row buffer/bank parallelism，而不是在 logic layer 增加普通计算单元，见 Page 1-2。"
        ],
        "problems": [
            "如何在 DRAM array 内实现 AND/OR/NOT 且保持低面积开销。",
            "如何避免支持任意三行激活导致的宽地址总线和复杂 row decoder。",
            "如何把 in-DRAM bitwise operations 暴露给 CPU，同时处理 coherence、ECC 和 data scrambling。"
        ],
        "contributions": [
            "提出 Ambit-AND-OR，通过 triple-row activation 实现 majority function 并由控制行得到 AND/OR，见 Page 4-6, Section 3。",
            "提出 Ambit-NOT，通过 dual-contact cell 使用 sense amplifier inverter 实现 NOT，见 Page 6, Figure 5。",
            "提出 designated rows、reserved row addresses、split row decoder 和 AAP primitive 等低成本实现，见 Page 6-9, Section 5。",
            "通过 SPICE 证明 Ambit 在显著 process variation 下仍可工作，见 Page 10, Section 6。",
            "对 throughput、energy 和三类真实应用进行评估，见 Page 10-12, Sections 7-8。"
        ],
        "method": [
            "TRA 同时激活三行共享同一组 sense amplifiers 的 rows，产生三输入 majority；将其中一行初始化为 0 得到 AND，初始化为 1 得到 OR，见 Page 4-5。",
            "Ambit-NOT 使用 dual-contact cell 连接到 sense amplifier 两侧，读取并复制反相值，见 Page 6, Figure 5。",
            "实际实现只允许 designated rows 做 TRA，并用 RowClone 把源数据复制到这些行，再复制结果到目标行，见 Page 5-8。",
            "系统接口包括 bbop instructions/API、cache coherence handling、ECC/data scrambling 处理，见 Page 8-9。"
        ],
        "experiments": [
            "SPICE 使用 55nm DDR3 model 和 Monte-Carlo process variation 评估 TRA 可靠性，见 Page 10, Table 2。",
            "raw throughput/energy 比较 Skylake、GTX 745、HMC 2.0、Ambit 和 Ambit-3D，见 Page 10-11, Figure 9/Table 3。",
            "Gem5 full-system simulation 评估 bitmap index、BitWeaving 和 bitvector set operations，见 Page 11-12, Figures 10-12。"
        ],
        "results": [
            "Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 比 HMC 2.0 高 9.7x，见 Page 10, Figure 9。",
            "bitwise operations 的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 11, Table 3。",
            "SPICE 中 ±5% variation 下 TRA 无错误；±10%/±15% 下错误比例为 0.29%/6.01%，见 Page 10, Table 2。",
            "bitmap index 查询平均降低 6x 执行时间，见 Page 11, Figure 10。",
            "BitWeaving 加速 1.8x-11.8x，平均 7.0x，见 Page 12, Figure 11。",
            "set operations 中，当每个集合有 64 个或更多元素时，Ambit 平均比 RB-tree 快 3x，见 Page 12, Figure 12。"
        ],
        "limitations": [
            "Ambit 要求操作数映射到同一 subarray，并需要 RowClone 在 designated rows 间搬移，见 Page 5-8。",
            "bitcount 仍由 CPU 执行，会限制 bitmap/BitWeaving 等端到端加速，见 Page 11-12。",
            "ECC 需要支持 bitwise-homomorphic 或专门处理，否则 in-DRAM computation 结果难以保护，见 Page 9。",
            "真实芯片 process variation、测试和 yield 仍需厂商级验证；SPICE 只是模型证据。"
        ],
        "focus": [
            "Page 4-6 的 TRA 与 DCC 是理解 Ambit 的核心。",
            "Page 6-9 的 low-cost implementation 说明为什么方案可接入 commodity interface。",
            "Page 10-12 的 Figure 9/Table 3/Figures 10-12 是主要证据。",
            "把这篇与 `1905.09822v3` 对照看：后者是更长的扩展/教程式版本。"
        ],
        "relations": "Ambit 是 LEC4 多篇 PuD 论文的关键源头：后续 DRAM Bender、FCDRAM、SiMRA、PuDHammer 等都在不同方向验证、扩展或审视 Ambit 类多行激活机制。",
        "figures": [
            ["Figure 1", "Page 3", "DRAM subarray organization", "解释 rows 与 sense amplifiers 的共享关系", "背景图"],
            ["Figure 5", "Page 6", "dual-contact cell", "展示 NOT 的硬件机制", "核心方法图"],
            ["Figure 7", "Page 7", "row address grouping", "展示 designated rows 与控制行组织", "系统实现关键"],
            ["Figure 8", "Page 8", "bitwise command sequences", "展示不同 bitwise operations 的命令序列", "核心流程"],
            ["Figure 9", "Page 10", "throughput comparison", "展示 Ambit 与 CPU/GPU/HMC 的吞吐差距", "核心结果"],
            ["Figure 10-12", "Page 11-12", "application performance", "展示 bitmap、BitWeaving、set operations 的端到端收益", "核心结果"]
        ],
        "tables": [
            ["Table 1", "Page 7", "B-group address mapping", "说明保留地址如何映射到 ACTIVATE/PRECHARGE 控制", "实现细节"],
            ["Table 2", "Page 10", "process variation effect", "TRA 在不同 variation 下错误率", "可靠性证据"],
            ["Table 3", "Page 11", "energy of bitwise operations", "Ambit 能耗降低 25.1x-59.5x", "核心结果"],
            ["Table 4", "Page 11", "simulation parameters", "Gem5/full-system 参数", "复现实验"]
        ],
        "equations": [
            ["Equation 1", "Page 5", "TRA 电荷共享/多数函数", "解释三行激活时 sense amplifier 为什么输出 majority", "是"]
        ],
        "terms": [
            ["Ambit", "内存内批量按位加速器", "Page 1", "利用 DRAM analog operation 执行 bitwise operations", "是"],
            ["Triple-Row Activation (TRA)", "三行同时激活", "Page 4-5", "同时激活三行得到 majority function", "是"],
            ["Dual-contact cell (DCC)", "双接触单元", "Page 6", "支持读取反相值以实现 NOT", "是"],
            ["AAP", "ACTIVATE-ACTIVATE-PRECHARGE", "Page 8", "Ambit 执行 bulk bitwise operation 的基础命令序列", "是"],
            ["RowClone", "DRAM 内行复制", "Page 5", "用于把源/目标行搬到 designated rows", "是"],
            ["BitWeaving", "数据库位编织扫描技术", "Page 11-12", "把列值按 bit plane 存放以用 bitwise operations 加速 predicate", "中"]
        ],
        "open_questions": [
            "Ambit 在真实 DDR4/DDR5 芯片上的错误率与 PuDHammer 风险如何权衡？",
            "能否把 bitcount、shift、加法等扩展到 DRAM 内，减少 CPU 残留瓶颈？",
            "编译器/OS 如何自动完成 subarray-aware data placement？"
        ],
    },
    {
        "slug": "cellular_logic-in-memory_arrays",
        "title": "Cellular Logic-in-Memory Arrays",
        "zh_title": "细胞式逻辑内存阵列",
        "authors": "William H. Kautz",
        "year": "1969",
        "venue": "IEEE Transactions on Computers, Vol. C-18, No. 8",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "Early logic-in-memory; cellular arrays; sorting memory; associative memory",
        "keywords": "CLIM; cellular logic; logic-in-memory; sorting array; content-addressed memory; pushdown memory",
        "pages": "9",
        "sections": "Abstract; I Introduction; II Cellular Logic-in-Memory Arrays; III Sorting Array I; IV/V Uses of Sorting Array; VI Sorting Array II; VII Conclusions; References",
        "one_sentence": "这篇 1969 年论文提出 cellular logic-in-memory (CLIM) arrays，把二维规则存储阵列中的每个 cell 增强为含逻辑与存储的小单元，用于排序、关联存储、pushdown memory 和可编程逻辑。",
        "background": [
            "论文写在大规模集成电路兴起时期，核心问题是“芯片上应该放什么样的大而有用的网络”，见 Page 1, Section I。",
            "作者认为二维重复 cell 阵列能带来功能灵活、可测试、可容错、易互连等优势，是 customized arrays 的替代方案，见 Page 1-3, Section II。"
        ],
        "problems": [
            "在端子数受限、芯片不可修复、需要少数模块类型的 LSI 背景下，如何组织有用的数字电路模块。",
            "如何让每个阵列 cell 同时包含少量逻辑和存储，以兼具 memory 和 logic array 的角色。",
            "如何用一个具体 sorting array 说明 CLIM 的工程可行性和多功能性。"
        ],
        "contributions": [
            "系统提出 CLIM arrays 的设计特征：identical cells、local neighbor connections、cell-level storage 和 programmability，见 Page 1-2, Section II。",
            "总结 CLIM 的八类优势：functional flexibility、testability、fault accommodation、subarray interconnectability、logical performance、design ease、low power/high speed、functional decomposition，见 Page 1-3。",
            "详细描述 Sorting Array I：一种 single-address multiple-word memory，可保持内部 words 有序，见 Page 3-7。",
            "说明 Sorting Array I 还可用作 content-addressed memory、pushdown memory、buffer memory 和 switching function array，见 Page 6-8。",
            "给出 Sorting Array II 并比较其更慢、时钟要求更精确、灵活性不如 Sorting Array I，见 Page 8-9。"
        ],
        "method": [
            "CLIM 基本形式是二维矩形 identical cells，每个 cell 包含简单 logic-and-storage circuit，并主要连接相邻 cells，见 Page 2。",
            "functional flexibility 来自 cell flip-flop storage 对 cell mode 的“programming”，使 cell 可扮演 adder、switch、register stage 等角色，见 Page 2。",
            "Sorting Array I 每行存一个 n-bit word，通过 cell 间比较和移动维持有序，可在读出时得到最大或最小 word，见 Page 3-6。",
            "Sorting Array II 用 brick-wall pattern 和 serial comparison/row interchange 实现排序，但灵活性较差，见 Page 8。"
        ],
        "experiments": [
            "本文不是现代实验评估论文，而是架构/工程概念论文；证据主要是结构设计、逻辑方程、用途分析和复杂度讨论。",
            "作者以 sorting arrays 为例，分析 cell complexity、terminal count、clocking、fault accommodation 和可测试性，见 Page 3-9。"
        ],
        "results": [
            "Sorting Array I 可作为保持 words 有序的 single-address multiword memory，也可作为 CAM、pushdown memory、queue/buffer memory 和 programmable switching array，见 Page 1 与 Page 6-8。",
            "论文指出 isolated faulty cells 有时可通过重编程或移除行/列绕过，见 Page 2 与 Page 9。",
            "Sorting Array II 与 Sorting Array I cell complexity 类似，但缺少 Sorting Array I 的多功能性，且更慢、需要更精确 clocking，见 Page 8-9。",
            "结论认为 CLIM arrays 至少适用于 conventional/associative memories 和具有自然迭代结构的计算电路；随着 per-gate cost 降低，CLIM 的吸引力会增强，见 Page 9, Section VII。"
        ],
        "limitations": [
            "这是一篇 1969 年概念与工程设计论文，没有现代 benchmark、能耗、面积或系统级定量评估。",
            "任意 combinational/sequential logic 的 gate utilization efficiency 低于 memory/register/arithmetic 等自然迭代结构，见 Page 2-3。",
            "fault accommodation 是有限的，不适用于所有 array 类型或 fault 类型，见 Page 2。",
            "Sorting Array II 灵活性差、速度慢且 clocking 要求更严格，见 Page 8-9。"
        ],
        "focus": [
            "Page 1-3 Section II 是历史价值最高的部分，定义了 CLIM 的设计原则。",
            "Page 3-7 的 Sorting Array I 展示 logic-in-memory 如何具体实现一种功能存储结构。",
            "Page 8-9 的 Sorting Array II 和 Conclusion 用来比较设计权衡。",
            "读这篇时重点看思想脉络，不要按现代实验论文标准要求它。"
        ],
        "relations": "这是 PIM/logic-in-memory 的早期思想源头之一；后来的 Stone logic-in-memory、near-data processing、Ambit/PuD 都可以看作在不同技术时代重新探索“把逻辑放进/靠近存储”的问题。",
        "figures": [
            ["Fig. 1", "Page 3-4", "Sorting Array I cell and registers", "展示 basic sorting array 的 cell logic、X/W registers 和连接", "核心结构图"],
            ["Fig. 3", "Page 5", "key/nonkey word portions", "说明排序 array 如何处理 key 与 nonkey fields", "用途细节"],
            ["Fig. 4", "Page 7", "switching function realization", "展示 Sorting Array I 可用于实现 switching functions", "扩展用途"],
            ["Fig. 5", "Page 8", "Sorting Array II", "展示第二种较慢且不灵活的 sorting array", "比较设计"]
        ],
        "tables": [
            ["未检测到核心表格", "全文", "论文主要使用图和文字推导", "无核心表格", "无"]
        ],
        "equations": [
            ["Cell logic equations", "Page 3-4, Fig. 1", "描述 Sorting Array I cell 的逻辑行为", "帮助理解 sorting memory 如何运行", "中"]
        ],
        "terms": [
            ["Cellular Logic-in-Memory (CLIM)", "细胞式逻辑内存", "Page 1", "每个阵列 cell 同时含逻辑和存储的二维规则结构", "是"],
            ["Cellular array", "细胞阵列", "Page 1-2", "由大量相同 cell 以规则邻接方式组成的阵列", "是"],
            ["Sorting array", "排序阵列", "Page 3-8", "能自动保持内部 words 有序的 CLIM array", "是"],
            ["Content-addressed memory", "内容寻址存储器", "Page 1, Page 6-8", "按内容而非地址查找/选择 word 的存储器", "中"],
            ["Pushdown memory", "下推存储/栈式存储", "Page 1, Page 6-8", "类似 stack 的存储用途", "中"],
            ["Fault accommodation", "故障容纳", "Page 1-2, Page 9", "通过绕过或重编程减少故障 cell 影响", "是"]
        ],
        "open_questions": [
            "CLIM 的规则二维结构思想如何映射到现代 DRAM subarray 或 SRAM compute-in-memory？",
            "哪些现代 workload 具有足够自然的迭代/局部结构，适合 CLIM 式设计？",
            "早期 CLIM 的 fault accommodation 思路能否启发现代 PIM 的 yield/reliability 处理？"
        ],
    },
    {
        "slug": "figaro-fine-grained-in-dram-data-relocation-and-caching_micro20",
        "title": "FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching",
        "zh_title": "FIGARO：通过细粒度 DRAM 内数据重定位和缓存提升系统性能",
        "authors": "Yaohua Wang; Lois Orosa; Xiangjun Peng; Yang Guo; Saugata Ghose; Minesh Patel; Jeremie S. Kim; Juan Gómez Luna; Mohammad Sadrosadati; Nika Mansouri Ghiasi; Onur Mutlu",
        "year": "2020",
        "venue": "MICRO 2020",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "Fine-grained in-DRAM data relocation; in-DRAM cache; DRAM latency reduction",
        "keywords": "FIGARO; FIGCache; in-DRAM cache; global row buffer; relocation; row segment; LISA-VILLA",
        "pages": "16",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 FIGARO; 4 Latency and Energy Analysis; 5 FIGCache; 6 Other Use Cases; 7 Methodology; 8 Evaluation; 9 Sensitivity Studies; 10 Related Work; References",
        "one_sentence": "FIGARO 复用 DRAM bank 内共享 global row buffer，以 cache-block/row-segment 粒度在 subarrays 间重定位数据，并构建 FIGCache 来提升 DRAM row buffer locality 和系统性能。",
        "background": [
            "DRAM 容量提升远快于访问延迟改善；in-DRAM cache 用小而快的 DRAM 区域缓存慢区域数据，但现有方案以整行 8KB 粒度迁移，浪费空间且迁移延迟受物理距离影响，见 Page 1-2。",
            "现代 DRAM bank 中所有 subarrays 共享 global row buffer，作者发现它可作为跨 subarray 细粒度 relocation 的通道，见 Page 1-2。"
        ],
        "problems": [
            "如何避免 in-DRAM cache 以整行粒度搬移大量不会被访问的数据。",
            "如何让跨 subarray relocation latency 与物理距离无关，避免大量 fast subarrays 交错布局。",
            "如何在 heterogeneous 和 homogeneous DRAM banks 中都获得 in-DRAM cache 收益。"
        ],
        "contributions": [
            "提出 FIGARO substrate，支持 bank 内 subarrays 之间 column/cache-block granularity data relocation，且 latency distance-independent，见 Page 2-6。",
            "提出 FIGCache，把 DRAM row 的 small fragments/row segments 缓存在 in-DRAM cache row 中，而非整行缓存，见 Page 2 与 Page 6-8。",
            "FIGCache 可在有 fast subarrays 的 heterogeneous bank 和仅有 slow subarrays 的 conventional bank 中工作，见 Page 1-2。",
            "展示 FIGCache 对性能、能耗、row buffer hit rate、cache hit rate 和硬件开销的影响，见 Page 9-11。",
            "讨论 FIGARO/FIGCache 在 RowHammer mitigation 和 row-buffer side-channel mitigation 中的潜在用途，见 Page 8。"
        ],
        "method": [
            "FIGARO 允许两个 local row buffers 通过 global row buffer 进行 unaligned data transfer，使源列可写入目标不同列，不经过 off-chip memory channel，见 Page 2 与 Section 4。",
            "FIGCache 使用 row segment granularity，把来自不同 DRAM rows 的 hot segments co-locate 到同一 cache row，提高 cache utilization 和 row buffer hit rate，见 Page 2 与 Page 6-8。",
            "memory controller 维护 FIGCache Tag Store (FTS)，记录 row segment tags、benefit counters、dirty/valid bits，并用 benefit-based replacement 选择缓存内容，见 Page 7-8 与 Page 11。",
            "FIGCache-Fast 使用少量 fast subarrays；FIGCache-Slow 只保留 slow subarray 中少量 rows 作为 cache，见 Page 8-9。"
        ],
        "experiments": [
            "评估 Base、LISA-VILLA、FIGCache-Slow、FIGCache-Fast、FIGCache-Ideal 和 LL-DRAM，见 Page 9, Section 8。",
            "包括 single-thread applications、eight-core multiprogrammed workloads 和 multithreaded applications，并按 memory intensity 分类，见 Page 9。",
            "指标包括 speedup、in-DRAM cache hit rate、DRAM row buffer hit rate、system energy breakdown、area/power overhead 和 sensitivity studies，见 Page 9-12。"
        ],
        "results": [
            "FIGCache-Fast 在 20 个 eight-core workloads 上平均提升 16.3% performance；100% memory-intensive workloads 平均提升 27.1%，见 Page 9, Figure 8。",
            "FIGCache-Slow 即使没有 fast subarrays，也在 multiprogrammed workloads 上平均提升 12.4% performance，见 Page 9。",
            "FIGCache-Fast 比 LISA-VILLA 平均高 4.7% performance，且只用两个 fast subarrays，而 LISA-VILLA 使用 16 个，见 Page 9。",
            "FIGCache-Slow/Fast 的整个 DRAM system row buffer hit rate 比 LISA-VILLA 平均高 18%，见 Page 10, Figure 10。",
            "memory-intensive single-core applications 中，FIGCache-Slow/Fast 分别降低 system energy 6.9%/11.1%；摘要报告 8-core workloads 上 DRAM energy 平均降低 7.8%，见 Page 10-11 与 Page 1。",
            "FIGARO DRAM chip area overhead <0.3%；FIGCache-Fast 额外 fast subarrays 面积 0.7%，低于 LISA-VILLA 的 5.6%；FIGCache-Slow 仅 0.2%，见 Page 11。"
        ],
        "limitations": [
            "需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。",
            "FIGCache 效果依赖 temporal locality、row segment size、replacement policy 和 hot data identification，见 Page 11-12 Sensitivity Studies。",
            "row segment 太大退化为整行缓存，relocation latency 和 cache underutilization 上升，见 Page 11, Section 9.2。",
            "RowHammer/side-channel mitigation 只是其他用例讨论，不是主要实验验证对象，见 Page 8。"
        ],
        "focus": [
            "Page 1-2 的 Figure 1-2 先理解为什么整行 relocation inefficient。",
            "Page 4-6 的 FIGARO RELOC latency/energy 是底层机制关键。",
            "Page 6-8 FIGCache design 说明如何把机制转化为缓存。",
            "Page 9-11 Figures 7-11 和 overhead 段落是评价该设计的核心。"
        ],
        "relations": "FIGARO 与 RowClone/LISA 同属 DRAM 内数据移动路线；与 Ambit/PuD 计算不同，它主要解决 DRAM 内缓存和 relocation 粒度问题，但同样利用 subarray/global row buffer 结构。",
        "figures": [
            ["Figure 1", "Page 1", "DRAM chip organization", "说明 subarray、local row buffer、global row buffer 关系", "背景核心图"],
            ["Figure 2", "Page 2", "state-of-the-art cache vs FIGCache", "展示 FIGCache-Fast/Slow 与传统 in-DRAM cache 的差异", "方法入口"],
            ["Figure 3", "Page 3", "DRAM bank/subarray detail", "说明 FIGARO 依赖的 LRB/GRB 路径", "机制背景"],
            ["Figure 7-8", "Page 9", "single-thread/eight-core performance", "FIGCache 核心性能结果", "核心结果"],
            ["Figure 9-10", "Page 10", "cache hit rate and row buffer hit rate", "解释性能提升来源", "核心分析"],
            ["Figure 11", "Page 10-11", "energy breakdown", "展示 energy reduction 来源", "核心结果"],
            ["Figure 12-14", "Page 11-12", "sensitivity studies", "分析 capacity、segment size、replacement policy", "参数边界"]
        ],
        "tables": [
            ["Table 1", "Methodology section", "system configuration", "用于 Base/LISA/FIGCache 参数设置", "复现实验需要"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文重点在 DRAM 操作序列与缓存机制", "公式不是重点", "否"]
        ],
        "terms": [
            ["FIGARO", "细粒度 DRAM 内重定位 substrate", "Page 1-2", "通过 global row buffer 支持 bank 内 cache-block granularity relocation", "是"],
            ["FIGCache", "基于 FIGARO 的 DRAM 内缓存", "Page 1-2", "缓存 row segments 而不是完整 DRAM rows", "是"],
            ["Global Row Buffer (GRB)", "全局行缓冲", "Page 1-3", "连接同一 bank 内 subarrays 与 I/O 的共享缓冲", "是"],
            ["Local Row Buffer (LRB)", "本地行缓冲", "Page 1-3", "每个 subarray 的 sense amplifier row buffer", "是"],
            ["Row segment", "行片段", "Page 2", "DRAM row 的小片段，可小到 cache block", "是"],
            ["FTS", "FIGCache Tag Store", "Page 11", "memory controller 中保存缓存 row segment metadata 的表", "是"]
        ],
        "open_questions": [
            "FIGARO 的 RELOC 操作在真实 DDR4/DDR5 芯片上能否以论文时序安全实现？",
            "FIGCache 与 Sectored DRAM 的 fine-grained access 思路能否结合？",
            "FIGCache 在现代多租户安全攻击和 RowHammer mitigation 中的实际收益需要怎样验证？"
        ],
    },
]


if __name__ == "__main__":
    write_papers(PAPERS, status="第三轮 5 篇深度阅读完成")
    print(f"Wrote batch 3 files for {len(PAPERS)} papers")
