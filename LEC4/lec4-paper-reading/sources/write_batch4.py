from write_batch1 import write_papers


PAPERS = [
    {
        "slug": "in-dram-bulk-and-or-ieee_cal15",
        "title": "Fast Bulk Bitwise AND and OR in DRAM",
        "zh_title": "DRAM 内快速批量按位 AND 与 OR",
        "authors": "Vivek Seshadri; Kevin Hsieh; Amirali Boroumand; Donghyuk Lee; Michael A. Kozuch; Onur Mutlu; Phillip B. Gibbons; Todd C. Mowry",
        "year": "2015",
        "venue": "IEEE Computer Architecture Letters",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "In-DRAM bulk bitwise operations; triple-row activation; RowClone",
        "keywords": "DRAM; bulk bitwise AND; bulk bitwise OR; triple-row activation; RowClone; bitmap index",
        "pages": "4",
        "sections": "Abstract; 1 Introduction; 2 Background on DRAM Operation; 3 In-DRAM AND and OR; 4 Latency, Throughput, and Energy Analysis; 5 Analysis of a Real-World Bitmap Index; 6 Related Work; 7 Conclusion; References",
        "one_sentence": "这篇短论文提出用三行同时激活让 DRAM sense amplifier 执行 majority function，并通过控制第三行实现大批量 AND/OR，从而把 bitmap 等应用中的按位操作留在 DRAM 内完成。",
        "background": [
            "作者指出 bitwise AND/OR 广泛用于 masking、initialization 和 bitmap indices；传统系统必须把源数据从 DRAM 读到处理器再写回，带来高 latency、bandwidth 和 energy，见 Page 1, Section 1。",
            "论文建立在 DRAM cell、bitline、sense amplifier 与 RowClone 的背景上：如果能在 subarray 内快速复制临时行，就能把三行激活组织成完整的 AND/OR 操作，见 Page 1-2, Sections 2-3。"
        ],
        "problems": [
            "如何在 DRAM 内部完成 bulk bitwise AND/OR，而不是经由 CPU 和外部内存通道搬运大量数据。",
            "如何利用现有 DRAM 操作和 RowClone，以很小 DRAM logic 改动支持三行同时激活。",
            "如何证明这种机制对真实 bitmap index 查询有端到端性能收益。"
        ],
        "contributions": [
            "提出三行同时连接到 bitline 的机制，使 sense amplifier 输出三者多数值；第三行为 0 时得到 AND，为 1 时得到 OR，见 Page 2, Section 3。",
            "用 RowClone-FPM/PSM 复制源行、初始化控制行并写回结果，从而保护原始源数据，见 Page 2, Section 3。",
            "提出只对固定临时行 D1/D2/D3 支持 triple-row activation 的低成本实现，避免任意三行同时激活的复杂 decoder，见 Page 3, Sections 3.1-3.2。",
            "分析 latency、throughput 和 energy，展示相对 Intel AVX baseline 的大幅收益，见 Page 3-4, Section 4。",
            "用 FastBit bitmap index range queries 做真实应用分析，见 Page 4, Section 5。"
        ],
        "method": [
            "核心 primitive 是 triple-row activation：同时激活三行后，bitline 偏移由三颗 cell 的多数值决定；令控制行 R=0 得到 A AND B，R=1 得到 A OR B，见 Page 2, Section 3 与 Figure 4。",
            "完整 AND/OR 会先把 A/B 复制到 D1/D2，把 R0 或 R1 复制到 D3，然后同时激活 D1/D2/D3，最后复制结果到 C，见 Page 2, Section 3。",
            "保守实现需要四个 RowClone-FPM，典型 latency 为 340ns；aggressive 版本通过单独小 row decoder 重叠 destination activation，把每次 RowClone-FPM 降到 50ns，总 latency 约 200ns，见 Page 3, Section 4。",
            "软件侧需要暴露新的 bulk bitwise instructions 或库接口；作者建议可先在 FastBit 等共享库中利用硬件加速，见 Page 3, Section 3.3。"
        ],
        "experiments": [
            "throughput microbenchmark 重复计算两个向量的 bitwise AND，并与 Intel Core i7-4790K 上的 AVX implementation 比较，见 Page 3, Section 4 与 Figure 5。",
            "energy 使用 Rambus power model 估算，baseline 只计 DRAM 访问能耗，不计 cache 和 computation energy，见 Page 4, Section 4。",
            "真实应用使用 FastBit 和 STAR 数据集上的 range queries，测量 query 时间中 bitwise OR 所占比例，并估算替换为 in-DRAM OR 后的端到端提升，见 Page 4, Section 5/Table 1/Figure 6。"
        ],
        "results": [
            "当 working set 不适合任何 on-chip cache 时，baseline AVX throughput 下降到 3.9 GB/s；conservative 机制达到 22.4 GB/s，aggressive 机制达到 38.2 GB/s，见 Page 3, Section 4 与 Figure 5。",
            "论文摘要报告该方法可使 bulk bitwise AND/OR throughput 提升 9.7x、energy 降低 50.5x，见 Page 1, Abstract。",
            "conservative 机制能耗降低 31.6x，aggressive 机制能耗降低 50.5x，见 Page 4, Section 4。",
            "FastBit range queries 中，bitwise OR 平均占 query execution time 的 31%，见 Page 4, Table 1。",
            "aggressive 机制配合 4 banks 时，range queries 平均性能提升 30%；即使假设 triple-row activation latency 高 2x，conservative 1-bank 仍提升 18%，见 Page 4, Section 5/Figure 6。"
        ],
        "limitations": [
            "最佳情形依赖 A/B/C 与临时行位于同一 subarray；跨 subarray/bank copy 需要 RowClone-PSM 或更慢路径，见 Page 2, Section 3。",
            "机制只直接覆盖 AND/OR，NOT、XOR、count 等操作不在本文实现范围内，见 Page 3-4。",
            "需要 DRAM 支持 triple-row activation variant、RowClone 支持和 memory controller/ISA/software 改动，见 Page 3, Sections 3.2-3.3。",
            "FastBit 应用结果是基于测量 OR 操作次数后的估算，不是完整硬件原型实测，见 Page 4, Section 5。"
        ],
        "focus": [
            "先看 Page 2 的 Figure 4 和公式化多数函数解释，这是全文技术核心。",
            "再看 Page 2-3 关于 D1/D2/D3、R0/R1 和 RowClone 的五步流程，理解为什么源数据不会被破坏。",
            "最后看 Page 3-4 的 Figure 5、Table 1、Figure 6，判断 microbenchmark 与 FastBit 的收益分别代表什么。"
        ],
        "relations": "这篇 IEEE CAL 短文是 Ambit/MICRO 2017 的早期核心机制版本，重点更集中在 AND/OR 和 FastBit；后续 Ambit 扩展了 NOT、系统集成、SPICE 验证和更多应用。",
        "figures": [
            ["Figure 1", "Page 1", "DRAM subarray", "说明多个 rows 共享 bitlines 和 sense amplifiers", "背景图"],
            ["Figure 3", "Page 2", "DRAM cell access steps", "解释 precharge、charge sharing、sense amplification", "理解电路行为必读"],
            ["Figure 4", "Page 2", "simultaneously connecting three cells", "展示三行激活为什么得到多数值", "核心方法图"],
            ["Figure 5", "Page 3", "throughput comparison with Intel AVX", "展示 cache 容量变化下 baseline 与 in-DRAM 机制吞吐差异", "核心结果图"],
            ["Figure 6", "Page 4", "FastBit range query performance", "展示真实 bitmap range query 的端到端提升", "应用结果图"]
        ],
        "tables": [
            ["Table 1", "Page 4", "FastBit OR time fraction", "range query 中 29%-34% 时间花在 OR，平均 31%", "应用动机和收益边界"]
        ],
        "equations": [
            ["majority expression", "Page 2, Section 3", "RA + RB + AB = R(A + B) + R(AB)", "R=1 得到 OR，R=0 得到 AND", "是"]
        ],
        "terms": [
            ["Triple-row activation", "三行同时激活", "Page 2", "同时把三行 cell 接到 bitline，让 sense amplifier 输出多数值", "是"],
            ["Sense amplifier", "感测放大器", "Page 1-2", "DRAM 中把微小 bitline 电压偏移放大为 0/1 的电路", "是"],
            ["RowClone-FPM", "RowClone 快速并行模式", "Page 2", "同 subarray 内通过背靠背 ACTIVATE 复制整行", "是"],
            ["Bulk bitwise operation", "批量按位操作", "Page 1", "对 KB/MB 级 bitvector 执行 AND/OR", "是"],
            ["FastBit", "bitmap index 库", "Page 4", "论文用来估算真实 range query 收益的开源 bitmap index 实现", "是"]
        ],
        "open_questions": [
            "真实芯片中 triple-row activation 在 process/temperature/voltage variation 下错误率是多少？",
            "如果操作数跨 subarray 或跨 bank，性能会下降到什么程度？",
            "如何将 AND/OR primitive 扩展成完整 bitwise ISA 并处理 ECC/cache coherence？"
        ],
    },
    {
        "slug": "lisa-dram_hpca16",
        "title": "Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM",
        "zh_title": "LISA：用低成本互连 subarray 实现快速 DRAM 子阵列间数据移动",
        "authors": "Kevin K. Chang; Prashant J. Nair; Donghyuk Lee; Saugata Ghose; Moinuddin K. Qureshi; Onur Mutlu",
        "year": "2016",
        "venue": "HPCA 2016",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "Inter-subarray data movement; DRAM substrate; Row Buffer Movement; in-DRAM copy and caching",
        "keywords": "LISA; RBM; RISC; VILLA; LIP; inter-subarray copy; DRAM; bulk data movement",
        "pages": "13",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Low-Cost Inter-Linked Subarrays; 4 LISA-RISC; 5 LISA-VILLA; 6 LISA-LIP; 7 Hardware Cost; 8 Methodology; 9 Evaluation; 10 Other Applications; 11 Related Work; 12 Conclusion; References",
        "one_sentence": "LISA 在相邻 DRAM subarray 的 bitlines 之间加入低成本 isolation transistors，使 row buffer movement 能跨 subarray 快速传输整行数据，并由此支持快速 copy、in-DRAM cache 和更短 precharge latency。",
        "background": [
            "bulk data movement 在 OS 和应用中很常见，但传统 memcpy 需要经由窄 off-chip channel；RowClone 虽能在 DRAM 内复制，但快速路径受限于同一 subarray，见 Page 1, Section 1。",
            "作者观察到 subarray 内 bitlines 天然是极宽的数据通路，且相邻 subarrays 物理距离很近；LISA 的关键是把这些 bitlines 用低成本 link 接起来，见 Page 2-3, Section 3。"
        ],
        "problems": [
            "如何让不同 subarray 之间也能像同一 subarray 内那样快速移动整行数据。",
            "如何以低面积开销提供新的 DRAM substrate，而不是为每个应用单独设计复杂机制。",
            "如何把快速 inter-subarray movement 用于 copy、caching 和 precharge 等多个场景。"
        ],
        "contributions": [
            "提出 Low-Cost Inter-Linked SubArrays (LISA)，在相邻 subarrays 的 bitlines 间加入 isolation transistors，见 Page 2-4, Section 3。",
            "提出 Row Buffer Movement (RBM)，让已激活 row buffer 驱动相邻 precharged row buffer，从而跨 subarray 移动数据，见 Page 4, Section 3.2。",
            "提出 LISA-RISC，用 RBM 实现 Rapid Inter-Subarray Copy，将 8KB inter-subarray copy latency 降低 9.2x，见 Page 5-7, Section 4。",
            "提出 LISA-VILLA，用 LISA 支持 heterogeneous-latency subarrays 中的 fast-row caching，见 Page 7-8, Section 5。",
            "提出 LISA-LIP，用邻近 subarray 的 precharge units 加速 precharge，见 Page 8, Section 6。",
            "展示三种应用组合后平均性能提升 94.8%、memory energy 降低 49.0%，见 Page 11, Section 9.4。"
        ],
        "method": [
            "LISA 的硬件核心是给相邻 subarrays 的同列 bitlines 增加 link；当 link 打开时，一个 row buffer 可通过 bitlines 驱动相邻 row buffer，见 Page 3, Figure 3。",
            "RBM 是新的数据移动操作：源 row buffer 已激活，目标 subarray 处于 precharged 状态，打开 link 后目标 row buffer 感测并锁存源数据，见 Page 4, Section 3.2。",
            "LISA-RISC 用两次 RBM 和写回步骤复制 open-bitline 架构中的两半 row；其 latency 随 hop count 线性增长但仍远低于 RC-InterSA，见 Page 5-7, Figure 7/Table 1。",
            "LISA-VILLA 设计 fast subarrays 并用 LISA-RISC 把 hot rows 快速复制到 fast region；LISA-LIP 则把两个 precharge units 联合起来加快 bitline precharge，见 Page 7-8。"
        ],
        "experiments": [
            "用符合 JEDEC/ITRS 的 SPICE circuit model 估计 RBM 和 linked precharge timing，并加入 60%/42.9% guardband，见 Page 4 与 Page 8。",
            "copy 评估比较 memcpy、RowClone variants 和 LISA-RISC，包含 single-core bootup/forkbench/shell 与 50 个 four-core mixed workloads，见 Page 9-10。",
            "VILLA/LIP 评估使用 memory-intensive four-core workloads，并报告 weighted speedup、row-buffer hit rate、energy 和 sensitivity，见 Page 10-11。",
            "硬件成本通过 prior area models、Micron power calculator、DRAMPower/Ramulator 等工具估计，见 Page 7-9。"
        ],
        "results": [
            "RBM 在保守 60% margin 后仍达到 8ns latency 和 500 GB/s data transfer bandwidth，相当于 DDR4-2400 64-bit channel 的 26x，见 Page 2 与 Page 4。",
            "8KB copy 中，memcpy latency/energy 为 1366.25ns/6.2µJ，RC-InterSA 为 1363.75ns/4.33µJ，LISA-RISC 1/7/15-hop 为 148.5/196.5/260.5ns 和 0.09/0.12/0.17µJ，见 Page 7, Table 1。",
            "four-core copy-intensive workloads 中，LISA-RISC-1 平均 weighted speedup 比 memcpy 高 66.2%，比 RC-InterSA 高 2.2x；memory energy per instruction 平均降低 55.4%，见 Page 10, Figure 13。",
            "LISA-VILLA 在四核 workload 上平均性能提升 5.1%、最高 16.1%；若用 RC-InterSA 搬 hot rows，反而降低 52.3%，见 Page 10-11, Figure 14。",
            "LISA-LIP 使 precharge latency 从 13.1ns 降至 guardband 后 5ns，即 2.6x 更低；平均性能提升 8.1%，最高 13.2%，见 Page 8 与 Page 11, Figure 15。",
            "三种应用组合平均性能提升 94.8%，memory energy reduction 为 49.0%，见 Page 11, Figure 16。"
        ],
        "limitations": [
            "LISA 需要修改 DRAM array/subarray 间连接和控制逻辑，虽面积开销小但仍需 DRAM 厂商采纳，见 Page 8, Section 7。",
            "LISA-RISC copy latency 随 copy distance/hop count 增长；Table 4 显示 1 到 63 hops 的 latency 从 148.5ns 到 644.5ns，见 Page 11。",
            "VILLA 的收益依赖 hot-row detection/caching policy，作者承认 hit rate 可由更好策略提升，见 Page 10-11, Section 9.2。",
            "coherence、cache dirty blocks 和 OS/software 对 copy 的可见性仍需系统支持，见 Page 6, Section 4.3。"
        ],
        "focus": [
            "Page 2-4 的 LISA/RBM 是整篇论文的 substrate 核心。",
            "Page 5-7 的 Figure 7/Table 1 是理解 LISA-RISC 相比 RowClone 的关键。",
            "Page 10-11 的 Figures 13-16 展示单个应用和组合效果。",
            "Page 12 的 other applications 提示 LISA 与 Ambit/bitwise operation 的关系。"
        ],
        "relations": "LISA 补上 RowClone/Ambit 的 inter-subarray 数据移动短板：RowClone 负责同 subarray 快速复制，LISA 负责跨 subarray 高带宽搬移，因此它也是后续 FIGARO、NoM 等数据移动论文的重要前序。",
        "figures": [
            ["Figure 1", "Page 1", "RowClone vs LISA transfer path", "对比窄 internal data bus 与 LISA bitline links", "动机图"],
            ["Figure 3", "Page 4", "LISA subarray links", "展示 isolation transistors 如何连接相邻 bitlines", "核心架构图"],
            ["Figure 7", "Page 6", "LISA-RISC command timeline", "对比 LISA-RISC 与 RC-InterSA 的 row copy 步骤", "核心流程图"],
            ["Figure 8", "Page 7", "8KB copy latency and energy", "展示 LISA-RISC 的低 latency/energy", "核心结果图"],
            ["Figure 13", "Page 10", "four-core copy evaluation", "展示 LISA-RISC weighted speedup 和 energy", "核心结果图"],
            ["Figure 14", "Page 11", "LISA-VILLA performance", "展示 fast-subarray caching 的效果和 RC-InterSA 反例", "核心结果图"],
            ["Figure 15", "Page 11", "LISA-LIP speedup", "展示 precharge 加速收益", "结果图"],
            ["Figure 16", "Page 11", "combined LISA applications", "展示 RISC/VILLA/LIP 的叠加收益", "综合结果图"]
        ],
        "tables": [
            ["Table 1", "Page 7", "8KB copy latency and energy", "LISA-RISC 1/7/15-hop 大幅低于 memcpy 与 RC-InterSA", "核心表"],
            ["Table 4", "Page 11", "copy distance sensitivity", "hop 数越大收益越小，但 63-hop 仍有 42.4% WS improvement", "敏感性分析"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文核心是 DRAM substrate、电路 timing 与系统评估", "公式不是主要学习重点", "否"]
        ],
        "terms": [
            ["Low-Cost Inter-Linked Subarrays (LISA)", "低成本互连子阵列", "Page 2", "用 isolation transistors 连接相邻 subarrays bitlines 的 DRAM substrate", "是"],
            ["Row Buffer Movement (RBM)", "行缓冲移动", "Page 4", "通过 LISA links 将一个 row buffer 的内容移动到相邻 row buffer", "是"],
            ["Rapid Inter-Subarray Copy (RISC)", "快速子阵列间复制", "Page 5", "基于 RBM 的跨 subarray copy 机制", "是"],
            ["VILLA DRAM", "可变延迟 DRAM", "Page 7", "用 fast/slow subarrays 管理 hot rows 的 heterogeneous DRAM", "是"],
            ["Linked Precharge (LIP)", "联动预充电", "Page 8", "利用邻近 subarray 的 precharge unit 加速 precharge", "是"],
            ["Isolation transistor", "隔离晶体管", "Page 3-4", "打开或关闭相邻 bitlines 连接的开关", "是"]
        ],
        "open_questions": [
            "LISA links 在 DDR5/HBM bank/subarray 组织中是否仍能以相似面积和 timing 成本实现？",
            "LISA-RISC 与 cache coherence/dirty data 结合时，端到端 OS copy 加速会下降多少？",
            "VILLA 的 hot-row caching policy 如果换成现代 learned/prefetch-aware policy，收益是否显著提高？"
        ],
    },
    {
        "slug": "micro19-gao",
        "title": "ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs",
        "zh_title": "ComputeDRAM：使用现成商用 DRAM 的内存内计算",
        "authors": "Fei Gao; Georgios Tziantzioulis; David Wentzlaff",
        "year": "2019",
        "venue": "MICRO-52",
        "arxiv": "未找到",
        "doi": "10.1145/3352460.3358260",
        "topic": "Off-the-shelf DRAM computation; timing-violating command sequences; bit-serial processing",
        "keywords": "ComputeDRAM; off-the-shelf DRAM; row copy; AND; OR; timing violation; SoftMC; bit-serial",
        "pages": "14",
        "sections": "Abstract; 1 Introduction; 2 Background; 3 Compute in DRAM; 4 In-Memory Compute Framework; 5 Experimental Methodology; 6 Experimental Results; 7 Discussion; 8 Related Work & Applications; 9 Conclusion; References",
        "one_sentence": "ComputeDRAM 证明无需修改商用 DDR3 DRAM 芯片，只要由可编程 memory controller 发出违反 JEDEC timing 的命令序列，就能在部分模块中实现 row copy、AND 和 OR，并进一步构造 bit-serial 计算框架。",
        "background": [
            "传统 in-memory compute 往往要求修改 DRAM array 或加入额外电路，而 DRAM 行业成本敏感、利润率低，导致这类设计难以商业落地，见 Page 1, Abstract/Introduction。",
            "作者重新审视 memory controller 对 DRAM commands/timing 的控制，发现快速连续 ACTIVATE/PRECHARGE/ACTIVATE 可让多个 rows 在未改动芯片中同时打开并发生 charge sharing，见 Page 3, Section 3。"
        ],
        "problems": [
            "是否可以在 off-the-shelf, unmodified, commercial DRAM 中实现 in-memory row copy 与逻辑 AND/OR。",
            "哪些 vendor/configuration 的 DRAM 能可靠执行这些非标准操作，稳定性受 voltage/temperature 影响如何。",
            "只具备 non-inverting AND/OR/row-copy primitives 时，如何构造任意 bit-serial computation。"
        ],
        "contributions": [
            "首次展示在未修改商用 DRAM 中实现 row copy，见 Page 1-2 与 Page 3-4。",
            "首次展示在未修改商用 DRAM 中实现 bit-wise logical AND 和 OR，见 Page 1-2 与 Page 4-5。",
            "系统刻画 DDR3 modules from all major DRAM vendors 的可行 timing windows 和可靠性，见 Page 8-11, Figures 10-13。",
            "分析 supply voltage 与 temperature 对操作鲁棒性的影响，见 Page 10-11, Section 6.3。",
            "提出用值与 complement 成对保存的 bit-serial software framework，使 AND/OR 足以表达 NAND/XOR/ADD 等计算，见 Page 6-7, Section 4。"
        ],
        "method": [
            "ComputeDRAM 用 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 等 timing-violating command sequence 让多行在同一 subarray 中同时影响 bitline，从而实现 row copy 或 AND/OR，见 Page 3-5, Figures 3-6。",
            "row copy 利用短 T2 让 R1 的 bitline 状态覆盖 R2；AND/OR 进一步缩短 T1/T2，使三行 charge sharing，第三行作为常量选择 AND 或 OR，见 Page 3-5。",
            "软件框架把每个值和其逻辑反相值一起存储；用 AND/OR 的 De Morgan 关系构造 NAND、XOR 和 ADD，见 Page 6, Equations 2-5。",
            "系统通过 SoftMC/FPGA 自定义 memory controller 发出精确命令序列，并用 error table 避免坏 columns/rows，见 Page 7-8, Figure 9。"
        ],
        "experiments": [
            "实验平台基于 Xilinx ML605 FPGA 和 SoftMC，测试 32 个 DDR3 modules、13 个 DRAM groups，见 Page 8, Section 5。",
            "exploratory timing scan 在 T1/T2 空间中寻找 row copy 与 AND/OR 成功区域，见 Page 9, Figure 10。",
            "robustness test 对 row copy 执行 1000 次随机复制，对 AND/OR 执行 10000 次随机操作，并统计 column success ratio，见 Page 10, Figure 11。",
            "supply voltage 从 1.2V 到 1.6V，temperature 从 30°C 到 80°C，测试环境变化对成功列比例的影响，见 Page 10-11, Figure 12。",
            "discussion 中估算 bit-serial vector operations 的 cycles、throughput 和 energy efficiency，见 Page 11-12, Table 2。"
        ],
        "results": [
            "Figure 10 显示至少存在 off-the-shelf unmodified commercial DRAM modules 可同时执行 row copy 与 logical AND/OR；几乎所有 configuration groups 至少有部分 columns 能执行 row copy，见 Page 9。",
            "逻辑 AND/OR 主要在 SKhynix_2G_1333 与 SKhynix_4G_1333B groups 中可跨 subarray 全列执行；SKhynix_4G_1600 也能执行但不是所有 columns，见 Page 9。",
            "row copy 中，53.9%-96.9% 的 columns 在测试 modules 中达到 100% success ratio；AND/OR 中，92.5%-99.98% columns 达到 100% success ratio，见 Page 10, Figure 11。",
            "在合理的 supply voltage variation (±0.1V) 与 temperature 范围内系统可继续工作，但不同 vendor 对 voltage/temperature 的最优 timing 偏好不同，见 Page 11, Section 6.3。",
            "单个 DDR3 module 中 row copy 需要 18 memory cycles、peak bandwidth 182 GB/s；8-bit AND/OR 需要 1376 cycles、peak throughput 19 GOPS；8-bit ADD 需要 10656 cycles、peak throughput 2.46 GOPS，见 Page 12, Section 7.1。",
            "若数据原本需要从 DRAM 到 CPU 再写回，ComputeDRAM 相比 vector unit 的 energy efficiency 对 row copy 为 347x，对 8-bit AND/OR 为 48x，对 ADD 为 9.3x，见 Page 12, Section 7.2。"
        ],
        "limitations": [
            "不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。",
            "可靠使用需要 error table 排除坏 columns/rows，这会降低可用容量并增加软件/地址转换复杂度，见 Page 6-7 与 Page 10。",
            "操作对 voltage/temperature 敏感，实际产品可能需要 binning，以标定哪些模块在什么环境下可靠，见 Page 11, Section 6.3。",
            "ComputeDRAM 适合 massive vector/bit-serial workloads；单个标量 ADD 需要上千 cycles，不适合低并行度计算，见 Page 12, Section 7.1。"
        ],
        "focus": [
            "Page 3-5 的 Figures 3-6 是理解 timing-violation 如何变成 row copy/AND/OR 的核心。",
            "Page 6 的 Equations 2-5 说明为什么只有 non-inverting operations 也能构造任意计算。",
            "Page 9-11 的 Figures 10-13 是判断真实芯片可行性和稳定性的核心证据。",
            "Page 12 的 throughput/energy discussion 要和 Ambit/RowClone 的修改 DRAM 方案对照看。"
        ],
        "relations": "ComputeDRAM 与 Ambit 解决相似 primitive，但路线相反：Ambit 修改 DRAM 控制逻辑支持规范化 TRA，ComputeDRAM 则用现有商用 DRAM 的 out-of-spec timing 行为做 proof-of-concept。",
        "figures": [
            ["Figure 1", "Page 2", "DRAM hierarchy", "说明 bank/subarray/row buffer 层次", "背景图"],
            ["Figure 3", "Page 3", "command sequence for in-memory operations", "定义 T1/T2 timing intervals", "核心方法图"],
            ["Figure 4", "Page 4", "row copy timeline", "解释如何用越界命令完成 row copy", "核心方法图"],
            ["Figure 5-6", "Page 4-5", "logical AND/OR timeline", "展示 AND/OR 的 charge sharing 过程", "核心方法图"],
            ["Figure 9", "Page 8", "testing framework", "展示 FPGA/SoftMC 测试平台", "实验平台图"],
            ["Figure 10", "Page 9", "timing heatmap", "展示不同 DRAM groups 的成功 timing windows", "核心结果图"],
            ["Figure 11", "Page 10", "CDF of column success ratio", "展示 row copy 与 AND/OR 稳定性", "核心结果图"],
            ["Figure 12-13", "Page 11", "voltage/temperature sensitivity", "展示环境变化对成功率和 timing 的影响", "鲁棒性结果"]
        ],
        "tables": [
            ["Table 2", "Page 11", "memory command cycles for 1-bit operation", "row copy/SHIFT/AND/OR/XOR/ADD 的 command cycles", "理解 bit-serial 成本必读"]
        ],
        "equations": [
            ["Equations 2-5", "Page 6, Section 4", "用 AND/OR 和 complement pairs 构造 AND/OR/NAND/XOR", "展示 non-inverting primitives 的计算完备性路线", "是"]
        ],
        "terms": [
            ["ComputeDRAM", "商用 DRAM 内计算机制", "Page 1", "通过越界 timing command sequence 在未改 DRAM 中执行计算", "是"],
            ["Timing-violating command sequence", "违反时序的命令序列", "Page 3", "故意缩短 DRAM command intervals 以触发非标准 charge sharing 行为", "是"],
            ["Row copy", "行复制", "Page 3-4", "把一行数据复制到另一行的 in-memory primitive", "是"],
            ["Column success ratio", "列成功率", "Page 8-10", "某列在重复测试中产生正确结果的比例", "是"],
            ["Error table", "错误表", "Page 7", "记录坏 rows/columns，运行时避免使用", "是"],
            ["Bit-serial computing", "位串行计算", "Page 6-7", "按 bit slice 在大量元素上并行执行计算", "是"]
        ],
        "open_questions": [
            "DDR4/DDR5 是否仍保留类似可利用的 timing-violation 行为，还是控制逻辑会过滤这些命令？",
            "error table、binning 与温度/电压监控的系统成本是否会抵消无需改 DRAM 的优势？",
            "如何把 ComputeDRAM 的不稳定 primitive 包装成可由 OS/编译器安全使用的接口？"
        ],
    },
    {
        "slug": "micro22-gao",
        "title": "FracDRAM: Fractional Values in Off-the-Shelf DRAM",
        "zh_title": "FracDRAM：在现成商用 DRAM 中存储分数电压值",
        "authors": "Fei Gao; Georgios Tziantzioulis; David Wentzlaff",
        "year": "2022",
        "venue": "MICRO 2022",
        "arxiv": "未找到",
        "doi": "10.1109/MICRO56248.2022.00066",
        "topic": "Fractional DRAM values; off-the-shelf DRAM; F-MAJ; DRAM PUF",
        "keywords": "FracDRAM; fractional value; Frac; Half-m; F-MAJ; PUF; off-the-shelf DRAM; timing violation",
        "pages": "15",
        "sections": "Abstract; I Introduction; II Background; III Primitive Operations; IV Evaluation Methodology; V Evaluation; VI Use Cases; VII Related Work; VIII Conclusion; References",
        "one_sentence": "FracDRAM 打破 DRAM 只能存 0/1 的二值抽象，通过特殊时序命令在未修改商用 DRAM 中产生接近 Vdd/2 的 fractional values，并用它增强 majority operation 与构造高吞吐 DRAM PUF。",
        "background": [
            "DRAM cell 本质是 capacitor，电压可处于 0 到 Vdd 之间；传统接口只把它抽象成 0/1，见 Page 1, Introduction。",
            "ComputeDRAM 已显示 out-of-spec command timing 能在商用 DRAM 中产生新行为；FracDRAM 进一步利用 PRECHARGE 的 Vdd/2 电路，把中间电压作为可用状态，见 Page 1-3。"
        ],
        "problems": [
            "是否能在 off-the-shelf DRAM cell 中稳定写入并验证 fractional value。",
            "fractional value 能否扩大 ComputeDRAM-style majority operation 的适用模块范围并提高稳定性。",
            "fractional value 能否构造无需改 DRAM 的高吞吐、环境鲁棒 PUF。"
        ],
        "contributions": [
            "首次展示在未修改商用 DRAM 中存储 fractional values，见 Page 1-2, Introduction。",
            "提出 Frac operation，用 ACTIVATE 后立即 PRECHARGE 中断 sense amplification，把整行 cell 拉向 Vdd/2，见 Page 3, Section III-A。",
            "提出 Half-m operation，通过四行激活与 trailing PRECHARGE 在一行中混合写入 normal 和 Half values，见 Page 3-4, Section III-B。",
            "用 retention time profile 和 MAJ3 results 验证 fractional value 的存在，见 Page 5-7, Section V。",
            "提出 F-MAJ 扩展/稳定 majority operation，并提出 Frac-based PUF，见 Page 8-12, Section VI。"
        ],
        "method": [
            "Frac operation 先 PRECHARGE bitline 到 Vdd/2，再 ACTIVATE target row，并在 sense amplifier 完全放大前立刻 PRECHARGE 中断，使 cell 保留介于 Vdd/2 与初始值之间的电压，见 Page 3, Figure 3。",
            "多次 Frac 会把 cell voltage 更接近 Vdd/2，且更少依赖初始值；Half-m 则通过四行同时打开和中断，在同一 row 生成 weak zero、weak one 与 Half，见 Page 3-4, Figures 3-4。",
            "验证 fractional value 不能直接普通 read，因为 read 会破坏/放大它；作者用 retention time 变化和 MAJ3 操作结果间接证明，见 Page 5, Section IV-B。",
            "F-MAJ 在四行激活中让一行存 fractional value，使其等效调节 charge sharing 的偏置；PUF 则用 10 次 Frac 把 row 拉近 Vdd/2，再读取 sense amplifier variation 形成 response，见 Page 8-12。"
        ],
        "experiments": [
            "评估 582 个 DDR3 chips，来自 7 个 major vendors，并按 vendor/configuration 分为多个 groups，见 Page 1 与 Page 4-5。",
            "Frac 评估包括 retention time profile、MAJ3 with fractional value；Half-m 评估包括 retention 与 MAJ3 结果，见 Page 5-8, Figures 6-8。",
            "F-MAJ 在可四行激活的 groups 上测试 coverage，并在 group B/C 上进行 10000 次随机输入稳定性测试，见 Page 8-10, Figures 9-10。",
            "PUF 评估用 normalized Hamming Distance、Hamming Weight、NIST random tests，以及不同电压/温度和跨三个月采样，见 Page 10-12, Figures 11-12。"
        ],
        "results": [
            "Frac 使平均约 55% cells 的 retention time 随 Frac 次数单调下降，支持其电压被逐步拉向 Vdd/2 的解释，见 Page 6, Figure 6。",
            "F-MAJ 可在所有能打开四行的 DRAM chips 上执行；group B 最佳配置达到 99.8% coverage，而原始 MAJ3 coverage 为 98.0%，见 Page 9, Figure 9。",
            "F-MAJ 稳定性测试中，group B 至少 95.4% columns 可可靠执行；in-memory majority 平均错误率从 9.1% 降到 2.2%，见 Page 10, Figure 10。",
            "Frac-based PUF 中，Intra-HD 最大为 0.051，Inter-HD 最小为 0.27，说明同一模块响应稳定而不同模块区分明显，见 Page 11, Figure 11。",
            "在 1.4V 与不同温度、跨 10 天/3 个月的数据中，maximum Intra-HD 仍远低于 minimum Inter-HD，说明 PUF 对环境变化较鲁棒，见 Page 11, Figure 12。",
            "PUF 响应经 modified Von Neumann extractor 后通过 NIST 15 项 randomness tests；8KB segment evaluation time 为 1.5µs，优化 memory controller 可降到 0.7µs，见 Page 12。"
        ],
        "limitations": [
            "retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。",
            "fractional value 的普通 readout 是 destructive，作者指出 Half-m/ternary storage 的 readout 与 data recovery 仍不成熟，见 Page 12, Section VI-C。",
            "不同 DRAM groups 偏好的 F-MAJ 配置不同，黑盒商用 DRAM 让原因难以确定，见 Page 9。",
            "实验平台主要覆盖 DDR3；DDR4 只在相关工作/潜力中讨论，完整支持仍需更多验证，见 Page 12-13。"
        ],
        "focus": [
            "Page 3 的 Frac/Half-m primitive 是全文最重要的机制部分。",
            "Page 5-7 的验证方法很关键，因为 fractional value 不能直接读出。",
            "Page 8-10 的 F-MAJ 说明 fractional value 如何改善 ComputeDRAM-style majority。",
            "Page 10-12 的 PUF 评估展示该机制的一个更现实用例。"
        ],
        "relations": "FracDRAM 是 ComputeDRAM 的延伸：ComputeDRAM 利用商用 DRAM 的多行激活实现 0/1 逻辑，FracDRAM 则把中间电压状态显式作为工具，用于 majority 稳定化和 security primitive。",
        "figures": [
            ["Figure 1", "Page 1", "fractional value command intuition", "展示特殊时序如何在 DRAM cell 中生成 fractional value", "入口图"],
            ["Figure 3", "Page 3", "Frac operation voltage timeline", "解释 ACTIVATE/PRECHARGE 如何中断 sense amplification", "核心方法图"],
            ["Figure 4", "Page 4", "Half-m voltage timeline", "展示同一 row 中 zero/one/Half 的生成", "核心方法图"],
            ["Figure 6", "Page 6", "retention time after Frac", "用 retention time profile 间接验证 fractional voltage", "核心验证图"],
            ["Figure 9", "Page 9", "F-MAJ coverage", "展示 fractional value 对 majority coverage 的改善", "核心结果图"],
            ["Figure 10", "Page 10", "F-MAJ stability", "展示错误率从 9.1% 降到 2.2%", "核心结果图"],
            ["Figure 11-12", "Page 11", "PUF HD and environment robustness", "展示 uniqueness、reliability 与环境鲁棒性", "核心结果图"]
        ],
        "tables": [
            ["DRAM group table", "Page 4", "evaluated chips/groups", "列出 vendor、frequency、chip 数与 Frac 支持情况", "实验设计基础"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文核心是电压状态、命令时序和实验验证", "公式不是主要学习重点", "否"]
        ],
        "terms": [
            ["Fractional value", "分数电压值", "Page 1", "介于传统 0/Vdd 与 1/ground 之间的 DRAM cell 电压状态", "是"],
            ["Frac operation", "Frac 操作", "Page 3", "用 ACTIVATE 后立即 PRECHARGE 中断放大以生成 fractional value", "是"],
            ["Half-m operation", "掩码 Half 操作", "Page 3-4", "在 masked bits 中混合写入 normal values 与 Half values", "是"],
            ["F-MAJ", "Fractional majority operation", "Page 8-10", "用 fractional value 改善四行激活下 majority operation 的覆盖和稳定性", "是"],
            ["Physical Unclonable Function (PUF)", "物理不可克隆函数", "Page 10", "利用制造差异生成设备唯一响应的安全 primitive", "是"],
            ["Intra-HD / Inter-HD", "模块内/模块间汉明距离", "Page 11", "衡量 PUF reliability 与 uniqueness 的指标", "是"]
        ],
        "open_questions": [
            "fractional value 如果需要长期保存或可恢复读取，需要怎样的 sense amplifier 或 refresh 支持？",
            "FracDRAM 在 DDR4/DDR5/HBM 上的可行性与稳定性如何？",
            "把 fractional states 用于 ternary computation 或密度提升时，错误模型和 ECC 如何设计？"
        ],
    },
    {
        "slug": "network-on-memory-data-copy_ieee-cal20",
        "title": "NoM: Network-on-Memory for Inter-Bank Data Transfer in Highly-Banked Memories",
        "zh_title": "NoM：面向高 bank 数内存的 bank 间数据传输 Network-on-Memory",
        "authors": "Seyyed Hossein SeyyedAghaei Rezaei; Mehdi Modarressi; Rachata Ausavarungnirun; Mohammad Sadrosadati; Onur Mutlu; Masoud Daneshtalab",
        "year": "2020",
        "venue": "IEEE Computer Architecture Letters",
        "arxiv": "未找到",
        "doi": "未找到",
        "topic": "3D-stacked memory; inter-bank data copy; circuit-switched network-on-memory",
        "keywords": "NoM; Network-on-Memory; 3D-stacked memory; inter-bank copy; TDM circuit switching; RowClone; HMC; HBM",
        "pages": "4",
        "sections": "Abstract; 1 Introduction; 2 Network-on-Memory; 2.1 TDM Slot Allocation; 2.2 Data Transfer on NoM; 2.3 NoM Implementation; 3 Evaluation; 4 Conclusion; References",
        "one_sentence": "NoM 在高 bank 数 3D-stacked memory 内加入轻量级 TDM circuit-switched network，让不同 banks 之间可直接并发 copy 数据，缓解 RowClone 等共享 internal bus 方案的 inter-bank bottleneck。",
        "background": [
            "bulk data copy 在程序和 OS 服务中很常见，传统系统需要 DRAM 与处理器之间来回复制；RowClone/LISA 减少了部分搬移，但 inter-bank copy 仍受共享 internal bus 限制，见 Page 1, Section 1。",
            "3D-stacked memories 如 HMC/HBM 有数百个 banks 和多个 memory controllers，跨 bank copy 更常见，也更不适合单一共享 bus，见 Page 1, Section 1。"
        ],
        "problems": [
            "如何在 3D-stacked memory 的多个 banks 之间直接、快速地复制数据。",
            "如何支持多个 inter-bank copy operations 并发执行，而不是让所有 copy 争用共享 internal bus。",
            "如何让新增 interconnect 对 DRAM 面积和时序影响保持很低。"
        ],
        "contributions": [
            "提出 Network-on-Memory (NoM)，用 3D mesh links 连接 highly-banked memory 中相邻 banks，见 Page 1-2, Section 2。",
            "采用 TDM-based circuit switching，由 centralized circuit control unit (CCU) 在 memory controller 中建立路径，见 Page 2, Section 2.1。",
            "提出 NoM-Light，复用既有 TSVs 以降低 full 3D mesh vertical links 的额外开销，见 Page 3, Section 2.3。",
            "把 NoM 与 RowClone/LISA 组合：intra-subarray/bank copy 由 RowClone/LISA 处理，inter-bank copy 由 NoM 处理，见 Page 3, Section 2.3。",
            "在 copy-intensive workloads 中展示平均 3.8x 相对 conventional 3D DRAM、75% 相对 RowClone 的性能提升，见 Page 1 与 Page 4。"
        ],
        "method": [
            "NoM 给每个 bank 增加简单 circuit-switched router，包括 crossbar、single-cycle latch、local slot table/controller 和 links；bank 可通过 NoM links 或传统 bus 发送/接收数据，见 Page 2, Figure 1。",
            "CCU 保持全网 reserved time slots 状态，用硬件 accelerator 在 TDM slot table 中为 source-destination bank 找到 collision-free path，见 Page 2, Section 2.1。",
            "copy 操作分为 circuit setup 与 data transfer：CCU 接收 direct data copy request，建立路径，调度 source vault controller read 和 destination vault controller write，见 Page 2-3, Figure 2。",
            "NoM full 3D mesh 使用 X/Y/Z 邻接 links；NoM-Light 删除额外 vertical mesh links，并复用 HMC 既有 TSVs，见 Page 3, Section 2.3。"
        ],
        "experiments": [
            "目标是 HMC-like 3D-stacked memory，NoM topology 为 8x8x4 mesh，link width 为 64 bits，见 Page 3, Section 2.3/3。",
            "比较 baseline conventional 3D-stacked DRAM、RowClone、NoM 和 NoM-Light；RowClone/LISA 可与 NoM 组合分别处理 intra 与 inter copy，见 Page 3。",
            "workloads 是模拟 mcached memory object caching system 的四个 benchmarks，其中 20%-60% memory traffic 来自 inter-bank copy，见 Page 4, Section 3/Figure 3。",
            "指标包括 IPC、energy per access、area overhead、operating frequency 和 link frequency sensitivity，见 Page 4。"
        ],
        "results": [
            "NoM 相比 RowClone 平均 IPC 高 75%，因为它加速 inter-bank copies 并允许多个 inter-bank copies 与其他 memory accesses 并发执行，见 Page 4, Section 3/Figure 4。",
            "摘要和结论报告 NoM 相比 conventional 3D-stacked DRAM 平均性能提升 3.8x，相比 RowClone 提升 75%，见 Page 1, Abstract 与 Page 4, Conclusion。",
            "NoM-Light 比 baseline NoM IPC 低 5%-20%，但仍显著优于 RowClone，见 Page 4, Section 3。",
            "NoM 相比 baseline DDR3 memory 可将 energy per access 最高降低 3.2x；相比 RowClone 最多多消耗 9% energy，主要来自额外 links 和 logic，见 Page 4, Energy analysis。",
            "NoM area overhead 低于 1% of a 16MB HMC bank；single hop latency 低于 300ps，TDM slot allocation accelerator critical path 低于 500ps，见 Page 4, Area/Operating frequency。",
            "即使 NoM link frequency 降低 25% 或 50%，性能退化呈 sublinear，仍优于 RowClone，见 Page 4, Operating frequency。"
        ],
        "limitations": [
            "NoM 主要针对 highly-banked 3D-stacked memory；传统低 bank 数 DDR 系统的收益和实现形态不一定相同，见 Page 1-2。",
            "设计需要在 DRAM bank 周围加入 routers/links/slot tables/CCU，对现有 HMC/HBM 仍是硬件修改，见 Page 2-3。",
            "实验 workload 较集中于 copy-intensive/mcached-style traffic；processor-intensive benchmarks 不是目标场景，见 Page 4。",
            "NoM 相比 RowClone 可能最多增加 9% energy，且需要软件/ISA 发出 direct data copy request 并维护 consistency，见 Page 3-4。"
        ],
        "focus": [
            "Page 1 先把 NoM 与 RowClone/LISA 的适用范围区分清楚：它专门解决 inter-bank copy。",
            "Page 2 Figure 1 和 Page 3 Figure 2 是理解 NoM router、CCU 和 copy flow 的关键。",
            "Page 4 Figure 3/4 展示 workload copy traffic 与性能收益，应重点看。",
            "把 NoM 与 LISA 对照：LISA 解决 inter-subarray，NoM 解决 inter-bank。"
        ],
        "relations": "NoM 接在 RowClone/LISA 之后补齐更高层次的数据移动：RowClone 做同 subarray copy，LISA 做跨 subarray copy，NoM 做 3D-stacked memory 中跨 bank copy。",
        "figures": [
            ["Figure 1", "Page 2", "DRAM structure with NoM links and modified bank", "展示每个 bank 的 circuit-switched router、CS buffers 和 NoM links", "核心架构图"],
            ["Figure 2", "Page 3", "NoM on 3D DRAM and example circuit", "展示从 bank A 到 bank B 的 TDM slots/path", "核心流程图"],
            ["Figure 3", "Page 4", "memory traffic breakdown", "说明目标 workloads 中 20%-60% traffic 来自 inter-bank copy", "实验动机图"],
            ["Figure 4", "Page 4", "performance of NoM and NoM-Light", "比较 NoM、NoM-Light、RowClone 和 baseline", "核心结果图"]
        ],
        "tables": [
            ["未检测到核心编号表", "全文", "短文主要用 Figures 3-4 和正文报告结果", "无核心表格", "否"]
        ],
        "equations": [
            ["未检测到核心编号公式", "全文", "本文主要是网络结构和系统评估", "公式不是重点", "否"]
        ],
        "terms": [
            ["Network-on-Memory (NoM)", "内存上网络", "Page 1", "连接 3D-stacked memory banks 的轻量级 inter-bank copy network", "是"],
            ["TDM circuit switching", "时分复用电路交换", "Page 2", "为 copy path 预留周期性 time slots，避免 packet-switched router 复杂度", "是"],
            ["Circuit Control Unit (CCU)", "电路控制单元", "Page 2", "在 memory controller 中集中分配和配置 NoM paths", "是"],
            ["NoM-Light", "轻量 NoM", "Page 3", "复用既有 TSVs 以减少 full 3D mesh vertical link 成本的变体", "是"],
            ["Vault controller", "vault 控制器", "Page 1-3", "HMC-like 3D memory 中控制一个 vault 内 banks 的控制器", "是"],
            ["Inter-bank copy", "bank 间复制", "Page 1", "源和目标位于不同 DRAM banks 的 direct data copy", "是"]
        ],
        "open_questions": [
            "NoM 在真实 HBM3/HBM4 的 bank group、pseudo-channel 和 TSV 组织上如何映射？",
            "direct data copy request 的 ISA/OS 接口和 memory consistency 需要什么支持？",
            "当 workload 不以 copy 为主，而是混合 gather/scatter 或 reduction 时，NoM 是否能泛化为更通用 in-memory network？"
        ],
    },
]


if __name__ == "__main__":
    write_papers(PAPERS, status="第四轮 5 篇深度阅读完成")
    print(f"Wrote batch 4 files for {len(PAPERS)} papers")
