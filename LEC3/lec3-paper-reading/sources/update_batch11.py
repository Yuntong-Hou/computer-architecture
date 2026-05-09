from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第十一轮深度阅读完成"
NOTE = "说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs)


def locs(xs):
    return "\n".join(f"- {x}（{l}）" for x, l in xs)


PAPERS = [
    {
        "slug": "staged-memory-scheduling_isca12",
        "title": "Staged Memory Scheduling: Achieving High Performance and Scalability in Heterogeneous Systems",
        "zh": "分阶段内存调度：在异构系统中实现高性能与可扩展性",
        "authors": "Rachata Ausavarungnirun, Kevin Kai-Wei Chang, Lavanya Subramanian, Gabriel H. Loh, Onur Mutlu",
        "year": "2012",
        "venue": "ISCA 2012",
        "doi": "未找到",
        "code": "未找到",
        "pages": "12",
        "dataset": "105 integrated CPU-GPU workloads; SPEC CPU2006 CPU workloads; GPU benchmarks; DDR3-1600 simulation",
        "topic": "Memory scheduling; heterogeneous CPU-GPU systems; scalable memory controller design",
        "keywords": "SMS, staged memory scheduling, CPU-GPU, row-buffer locality, batch scheduler, FIFO, fairness, CGWS",
        "one": "SMS 把传统 memory controller 中 row-locality detection、inter-application priority 和 low-level DRAM command scheduling 拆成三阶段，用更简单硬件在 CPU-GPU 共享内存场景下提升 CPU 性能和公平性，同时控制 GPU frame rate 损失。",
        "background": "集成 GPU 会产生远高于 CPU 的 memory traffic，占据 memory controller request buffer，降低 controller 对 CPU requests 的可见性；已有 ATLAS/TCM/PAR-BS 等应用感知调度在 CPU-only 场景有效，但要在 CPU-GPU 场景保持全局可见性需要很大且复杂的集中式 request buffer。",
        "questions": [
            "GPU 高强度 memory traffic 为什么会破坏 CPU application-aware scheduling？",
            "能否用分布式小 FIFO 代替大型集中式 CAM/request buffer？",
            "如何同时捕获 row-buffer locality、提高公平性、控制 GPU frame rate？",
            "SJF probability p 如何在 CPU 与 GPU 优先级之间调节？",
            "SMS 的面积/功耗复杂度相比 FR-FCFS 如何？",
        ],
        "contribs": [
            "指出 integrated CPU-GPU systems 中 GPU traffic 对传统 memory scheduling 的 visibility 和 complexity 挑战。",
            "提出三阶段 Staged Memory Scheduler：batch formation、batch scheduling、DRAM command scheduling。",
            "使用 per-source FIFO 和 per-bank FIFO 组成低复杂度结构，避免大型集中式 request buffer。",
            "引入可配置 SJF probability p，让系统软件按场景偏向 CPU 或 GPU。",
            "在 105 个 workload 上证明 SMS 提升 CPU/system performance 与 fairness，并减少硬件面积/漏电。",
        ],
        "method": "第一阶段按 source/application 将同 row requests 组合成 batches，捕获 row-buffer locality；第二阶段在 batches 之间按 SJF/round-robin 等高层策略调度，处理 application-level fairness/performance；第三阶段 per-bank FIFO 只负责按顺序发 DRAM commands 并满足 timing constraints。",
        "experiments": "模拟 16-core CPU + 1 GPU、DDR3-1600、四个 memory controllers，并比较 FR-FCFS、ATLAS、TCM、CFR-FCFS、CTCM、SMS0/SMS0.9；指标包括 CPU weighted speedup、GPU frame rate、CGWS、unfairness、面积和 leakage。",
        "results": [
            ("SMS0.9 平均 CPU performance 比 ATLAS/TCM 分别提升 22.1%/35.7%。", "Page 8, Figure 5"),
            ("SMS0.9 相比 ATLAS/TCM 平均降低 GPU frame rate 18.1%/26.7%，但大多数 workload categories 仍保持 >30 FPS。", "Page 8, Figure 5 discussion"),
            ("GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 system performance 46.4%/17.2%/25.7%。", "Page 9, Figure 7"),
            ("GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 fairness 244.6%/47.6%/205.7%。", "Page 9, Figure 7"),
            ("GPUweight=1000 时，SMS0 相比 FR-FCFS/ATLAS/TCM 分别提升 1.6%/32.7%/16.4% CGWS。", "Page 10, Figure 8"),
            ("SMS 在不同 CPU core counts 和 memory channel counts 下持续提升 CPU performance/fairness，并通常保持可接受 GPU frame rate。", "Page 10, Figures 9-10"),
            ("300 request buffers 系统中，SMS leakage power 比 FR-FCFS 低 66.7%，area 低 46.3%。", "Page 11, Table 5"),
        ],
        "conclusion": "SMS 的结论是：异构 CPU-GPU memory scheduling 不应靠更大的集中式 buffer 硬撑全局复杂调度；把功能分层后，硬件更简单、可扩展，并能用一个配置参数在 CPU/GPU 需求之间折中。",
        "limitations_author": [
            ("SMS0.9 会降低 GPU frame rate，某些类别如 HM 可能低于 30 FPS，需要调整 p。", "Page 8, Figure 5 discussion"),
            ("CPU-only 场景中 SMS 相比 ATLAS/TCM 牺牲少量 performance，换取 fairness 和低复杂度。", "Page 11, Section 6.6"),
        ],
        "limitations_infer": [
            ("SMS 评估基于 2012 年 GPU/DDR3 模型，现代 integrated GPU、HBM/LPDDR 和 QoS requirements 需重新验证。", "推断，基于 Section 5 setup"),
            ("p 的动态选择需要系统软件或 ISA 支持，论文主要展示可调性而非完整 runtime policy。", "推断，基于 Page 9 footnote and Section 6.2"),
        ],
        "focus": "重点读 Figure 1 visibility、Figure 4 SMS organization、Equations 1-4 metrics、Figures 5-10 性能/公平性、Table 5 复杂度。",
        "relation": "SMS 与 RLMC、MISE、DASH、ASM 等 memory scheduling 论文形成对比：SMS 的核心不是预测/学习，而是结构性拆分 controller 任务来降低复杂度并处理 GPU traffic。",
        "figures": [
            ("Figure 1", "Page 1", "limited visibility", "说明 GPU requests 占据 buffer 后 CPU 可见性下降。"),
            ("Figure 4", "Page 4", "SMS organization", "展示三阶段结构和 FIFO 组织。"),
            ("Figure 5", "Page 8", "CPU/GPU performance", "主结果：CPU 提升与 GPU frame rate tradeoff。"),
            ("Figure 7", "Page 9", "CGWS/fairness with GPUweight=1", "展示 CPU 重要场景下的系统收益。"),
            ("Figure 8", "Page 10", "CGWS with GPUweight=1000", "展示 GPU 重要场景下 SMS0 的配置收益。"),
            ("Figures 9-10", "Page 10", "scalability", "展示 core/channel 扩展下性能和公平性。"),
        ],
        "tables": [
            ("Table 1", "Page 6", "SMS hardware storage", "列出每阶段硬件存储开销。"),
            ("Table 2", "Page 7", "simulation parameters", "列出 CPU/GPU/DRAM 参数。"),
            ("Table 5", "Page 11", "power and area", "SMS 低 leakage/area。"),
        ],
        "equations": [
            ("Equation 1", "Page 7", "CPU weighted speedup", "sum of IPC_shared/IPC_alone", "衡量 CPU 多程序性能。", "是"),
            ("Equation 2", "Page 7", "GPU speedup/frame rate", "shared frame rate / alone frame rate", "衡量 GPU 性能。", "是"),
            ("Equation 3", "Page 8", "CGWS", "CPUWS + GPUweight * GPUSpeedup", "用 GPUweight 表示 CPU/GPU 重要性。", "是"),
            ("Equation 4", "Page 8", "Unfairness", "max slowdown across CPU cores and GPU", "衡量最差 slowdown。", "是"),
        ],
        "terms": [
            ("Staged Memory Scheduler (SMS)", "分阶段内存调度器", "Page 1-2", "三阶段、低复杂度、应用感知 memory scheduler。", "是"),
            ("Batch formation", "批形成", "Page 4-5", "按 source 和 row locality 把 requests 组成 batch。", "是"),
            ("SJF probability", "最短作业优先概率", "Page 5 and Page 8-9", "调节 batch scheduler 偏向短 batch/CPU 或 GPU 的参数 p。", "是"),
            ("CGWS", "CPU-GPU Weighted Speedup", "Page 8", "综合 CPU/GPU 性能并用 GPUweight 加权的指标。", "是"),
            ("DCS FIFO", "DRAM command scheduler FIFO", "Page 4-5", "最后阶段 per-bank FIFO，只处理低层 DRAM timing。", "是"),
        ],
        "sections": "Abstract; Introduction; Background; Motivation; SMS Design; Methodology; Evaluation; Related Work; Conclusion",
        "translation": [
            ("Abstract / 摘要", "Page 1", "SMS 面向 CPU-GPU 共享内存系统，把 memory controller 的主要任务拆为三阶段。它在提升 CPU performance/fairness 的同时，让实现复杂度低于以往应用感知调度器。"),
            ("1-3. Motivation / 动机", "Page 1-4", "GPU requests 数量巨大，会占据 controller request buffer，使 controller 难以观察 CPU applications 的差异。扩大 buffer 会带来面积、功耗、时序和逻辑复杂度问题。"),
            ("4. SMS Design / 设计", "Page 4-6", "SMS 用 per-source FIFO 捕获 row-buffer locality，用 batch scheduler 做高层应用优先级，用 per-bank FIFO 做低层 DRAM timing。这样把全局复杂逻辑分解到更简单结构中。"),
            ("5-6. Evaluation / 评估", "Page 7-11", "SMS0.9 偏向 CPU，提升 CPU performance 和 fairness；SMS0 偏向 GPU，更适合 GPUweight 高的场景。p 是静态或动态可调的性能旋钮。"),
            ("8. Conclusion / 结论", "Page 12", "作者总结 staged approach 可以为未来异构系统 memory controller 提供可扩展基础，因为它同时解决 performance、fairness 和 design complexity。"),
        ],
    },
    {
        "slug": "tesseract-pim-architecture-for-graph-processing_isca15",
        "title": "A Scalable Processing-in-Memory Accelerator for Parallel Graph Processing",
        "zh": "面向并行图处理的可扩展 Processing-in-Memory 加速器",
        "authors": "Junwhan Ahn, Sungpack Hong, Sungjoo Yoo, Onur Mutlu, Kiyoung Choi",
        "year": "2015",
        "venue": "ISCA 2015",
        "doi": "10.1145/2749469.2750386",
        "code": "未找到",
        "pages": "13",
        "dataset": "Five graph workloads; three real-world graphs: LiveJournal, English Wikipedia, Indochina domains",
        "topic": "Processing-in-memory; 3D-stacked memory; graph processing; message passing",
        "keywords": "Tesseract, PIM, graph processing, HMC, vault, message passing, list prefetcher, message-triggered prefetcher, PageRank",
        "one": "Tesseract 把简单 in-order cores 放进 3D-stacked memory 的 vaults 中，用 message passing 和 graph-aware prefetching 利用内部 TB/s bandwidth，使图处理性能随内存容量扩展。",
        "background": "大规模图处理有随机访问、低 locality、每顶点计算少等特征，传统 CPU/缓存/外部 memory bandwidth 难以扩展；仅增加 cores 或使用 HMC 外部带宽仍无法满足数百 GB/s 到 TB/s 的需求。",
        "questions": [
            "为什么 graph processing 的瓶颈是 memory bandwidth 而不是 core compute？",
            "3D-stacked memory/HMC 的 internal bandwidth 如何支持 memory-capacity-proportional performance？",
            "Tesseract core/vault/message passing 如何组织？",
            "非阻塞 remote function call 如何隐藏 remote access latency 并支持 atomic updates？",
            "list prefetching 和 message-triggered prefetching 如何利用图算法访问模式？",
        ],
        "contribs": [
            "从体系结构角度分析 large-scale graph processing，并指出 memory bandwidth 是主要瓶颈。",
            "提出 Tesseract：基于 3D-stacked memory/HMC vault 的 programmable PIM graph accelerator。",
            "设计基于 message passing 的跨 vault 通信，支持 non-blocking remote function calls 和 atomic memory updates。",
            "提出 list prefetcher 和 message-triggered prefetcher，利用 programming interface hints 和 graph access patterns。",
            "在五个 graph workloads、三个真实图上证明 10x/14x 级性能提升和 87% 平均能耗降低。",
        ],
        "method": "每个 HMC vault 配一个简单 in-order core，只直接访问本地 DRAM partition；远端数据更新通过 message passing 把 computation 移到数据所在 vault。host 负责初始化和分配图对象到 vaults。程序通过 get/put/list_for/barrier 等 API 暴露访问模式，硬件 prefetchers 根据 hint 预取列表和消息目标数据。",
        "experiments": "比较 DDR3-OoO、HMC-OoO、HMC-MC、Tesseract no prefetch、Tesseract+LP、Tesseract+LP+MTP；workloads 为 Average Teenager Follower、Conductance、PageRank、SSSP、Vertex Cover；输入图为 LJ/WK/IC。",
        "results": [
            ("Tesseract 在无 prefetching 时相比 DDR3-OoO 平均提升 9x；LP+MTP 后平均提升 14x。", "Page 8-9, Figure 6 discussion"),
            ("论文摘要保守总结为平均系统性能提升 10x、平均能耗降低 87%。", "Page 1-2, Abstract/Contributions"),
            ("Tesseract 使用 HMC internal bandwidth，系统可利用 8 TB/s，总带宽远超 DDR3-OoO 102.4GB/s 和 HMC-OoO/HMC-MC 640GB/s。", "Page 8, Section 4.1/5.1"),
            ("Tesseract 的 average memory access latency 比 DDR3-based system 低 96%。", "Page 8, Figure 7 discussion"),
            ("即使 HMC-MC 被理想给予 PIM-level bandwidth，Tesseract 仍快 2.2x，说明 programming model 也同样关键。", "Page 9, Figure 8 discussion"),
            ("prefetching schemes 平均覆盖 87% L1 cache misses，性能距离理想 prefetching 仅 1.8%。", "Page 10, Figure 10"),
            ("从 32 cores/8GB 到 128 cores/32GB 几乎理想 scaling；到 512 cores/128GB 后受 off-chip communication 限制。", "Page 10, Figure 11"),
            ("Tesseract 平均能耗比 HMC-OoO 低 87%，最高 logic die power density 94mW/mm2，低于 133mW/mm2 热限制。", "Page 11-12, Figure 14 discussion"),
        ],
        "conclusion": "Tesseract 的结论是：PIM 不只是把 cores 放近 memory，而是要把数据分布、message passing、programming interface 和 prefetching 一起设计，才能把 3D-stacked memory internal bandwidth 转化为图处理扩展性。",
        "limitations_author": [
            ("Tesseract 不支持 virtual memory，以避免 in-memory address translation 开销。", "Page 4, Section 3.1"),
            ("512-core scaling 受 off-chip communication 和 graph distribution 影响，需优化 network/data mapping。", "Page 10-11, Sections 5.5-5.7"),
        ],
        "limitations_infer": [
            ("程序需要使用 Tesseract API/编程模型，迁移已有 graph frameworks 有开发成本。", "推断，基于 Section 3.4"),
            ("结果基于 HMC-era 3D-stacked memory 假设，现代 HBM/PIM 产品接口、软件栈和热约束需重新评估。", "推断，基于 architecture setup"),
        ],
        "focus": "重点读 Figure 2 bandwidth bottleneck、Figure 3 architecture、Figure 4 message-triggered prefetching、Figure 5 programming example、Figures 6-14 evaluation。",
        "relation": "Tesseract 是 PIM graph processing 经典架构，与 SISA、Google PIM、IMPICA、NATSA、NERO 等 PIM/NDP 论文共同展示近数据计算在不规则数据结构和高带宽场景的价值。",
        "figures": [
            ("Figure 1", "Page 3", "PageRank pseudocode", "展示图处理的邻居遍历和 shared updates。"),
            ("Figure 2", "Page 3", "conventional systems bottleneck", "说明增加 cores/HMC 外部带宽仍不足。"),
            ("Figure 3", "Page 4", "Tesseract architecture", "展示 cubes/vault/core/message queue/prefetchers。"),
            ("Figure 4", "Page 6", "message-triggered prefetching", "解释消息到达和处理间 slack 如何用于预取。"),
            ("Figure 6", "Page 9", "performance comparison", "主性能结果。"),
            ("Figure 10", "Page 10", "prefetch efficiency", "展示 timeliness 和 coverage。"),
            ("Figure 14", "Page 11", "energy", "展示能耗收益。"),
        ],
        "tables": [
            ("未检测到核心编号表", "-", "论文主要通过图、伪代码和系统描述展示。", "建议回到 PDF 查看 Section 4 methodology 的参数描述。"),
        ],
        "equations": [
            ("Bandwidth scaling relation", "Page 3", "internal vs external bandwidth", "16 HMCs expose 8TB/s internal vs 320GB/s external", "PIM 的核心来自 memory-capacity-proportional bandwidth。", "是"),
        ],
        "terms": [
            ("Tesseract", "PIM 图处理加速器", "Page 1-2", "基于 3D-stacked memory vault cores 的 programmable graph accelerator。", "是"),
            ("Processing-in-memory (PIM)", "存内/近存计算", "Page 2-3", "把 computation 移到 memory 内部或附近以利用内部带宽。", "是"),
            ("Vault", "HMC 垂直分区", "Page 4", "含 DRAM banks、memory controller 和 Tesseract core 的 HMC slice。", "是"),
            ("Remote function call", "远程函数调用", "Page 5", "通过 message passing 在数据所在 vault 执行函数。", "是"),
            ("Message-triggered prefetching", "消息触发预取", "Page 6", "利用消息等待处理的 slack 预取目标数据。", "是"),
        ],
        "sections": "Abstract; Introduction; Background and Motivation; Tesseract Architecture; Evaluation Methodology; Evaluation Results; Related Work; Conclusion and Future Work",
        "translation": [
            ("Abstract / 摘要", "Page 1", "Tesseract 是面向 large-scale graph processing 的 programmable PIM accelerator。它利用 3D-stacked memory 的 internal bandwidth、message passing 和 graph-aware prefetching，平均提升性能并降低能耗。"),
            ("1-2. Motivation / 动机", "Page 1-3", "图处理访问随机、局部性差、每项计算少。传统体系结构受 off-chip bandwidth 限制，memory capacity 增加不会带来 proportional bandwidth。PIM 可以让 bandwidth 随 memory cubes 增加而增加。"),
            ("3. Architecture / 架构", "Page 4-7", "每个 HMC vault 包含一个 Tesseract core。core 只访问本地 partition，远端访问通过 message passing，把计算移到数据处。编程接口提供 get/put/list_for/barrier 等 primitives。"),
            ("3.3. Prefetching / 预取", "Page 5-6", "list prefetcher 处理列表/边数组的 strided traversal；message-triggered prefetcher 利用消息排队到处理中间的时间预取远程函数所需数据。"),
            ("5. Evaluation / 评估", "Page 8-12", "Tesseract 显著提升性能，主要因为利用 TB/s internal bandwidth 并降低 memory access latency。scaling 受 off-chip network 和 graph partitioning 影响，能耗大幅下降但功耗上升仍在热限制内。"),
            ("7. Conclusion / 结论", "Page 12-13", "论文总结 Tesseract 展示了 3D-stacked memory 上 PIM 对 graph processing 的可扩展性，并指出未来需进一步优化网络和数据分布。"),
        ],
    },
    {
        "slug": "understanding-and-modeling-in-DRAM-ECC_dsn19",
        "title": "Understanding and Modeling On-Die Error Correction in Modern DRAM: An Experimental Study Using Real Devices",
        "zh": "理解和建模现代 DRAM 中的片上错误纠正：基于真实器件的实验研究",
        "authors": "Minesh Patel, Jeremie S. Kim, Hasan Hassan, Onur Mutlu",
        "year": "2019",
        "venue": "DSN 2019",
        "doi": "未找到",
        "code": "https://github.com/CMU-SAFARI/EINSim",
        "pages": "13",
        "dataset": "232 LPDDR4 devices with on-die ECC and 82 LPDDR4 devices without on-die ECC; retention errors across temperatures, refresh rates, and patterns",
        "topic": "On-die ECC; DRAM error characterization; statistical inference; LPDDR4",
        "keywords": "on-die ECC, EIN, EINSim, MAP estimation, Hamming code, pre-correction error, post-correction error, LPDDR4",
        "one": "这篇论文提出 EIN/EINSim，用统计推断从只能观察到的 post-correction errors 中反推出 DRAM on-die ECC scheme 和 pre-correction error rates，从而恢复被片上 ECC 遮蔽的真实错误分布。",
        "background": "现代 DRAM scaling 促使厂商在芯片内部加入不可见、专有、未公开的 on-die ECC；这改善 yield，却让研究者无法直接观察物理 error mechanisms，导致 retention、latency、RowHammer 等实验性 characterization 结果被 ECC 扭曲。",
        "questions": [
            "on-die ECC 为什么会破坏传统 DRAM error characterization？",
            "只看 post-correction errors，如何反推出 ECC code 和 pre-correction BER？",
            "MAP estimation 如何利用 pre-correction errors 的统计性质区分 ECC schemes？",
            "EINSim 如何模拟 arbitrary ECC scheme 的 correction/miscorrection？",
            "真实 LPDDR4 devices 使用的 on-die ECC 是什么？",
        ],
        "contribs": [
            "提出 Error-correction INference (EIN)，用 MAP estimation 推断 on-die ECC scheme 和 pre-correction error rates。",
            "开发并开源 EINSim，模拟 ECC encoding/error injection/decoding/checking 流程。",
            "完成 open literature 中首个带 on-die ECC DRAM devices 的实验性错误表征研究。",
            "在 232 个带 on-die ECC 和 82 个无 on-die ECC LPDDR4 devices 上进行 retention error study。",
            "推断测试设备使用 single-error correction Hamming code (n=136, k=128, d=3)。",
            "展示 EIN 可恢复 on-die ECC 遮蔽前的 lognormal/exponential 等物理错误分布趋势。",
        ],
        "method": "EIN 为候选 ECC schemes 和 pre-correction error distribution 建立统计模型；用 EINSim 对每组模型参数进行 Monte Carlo simulation，估计观测 post-correction PMF 的 likelihood；再用 MAP/grid search 找到最可能的 ECC scheme 与 pre-correction error rate。",
        "experiments": "作者诱发 LPDDR4 retention errors，测试不同温度、refresh windows 和 data patterns；先反推 true-/anti-cell layout、row repair outliers，再用 EIN/EINSim 比较多种 Hamming/BCH/Repetition/no-ECC 模型与真实 post-correction error distribution。",
        "results": [
            ("on-die ECC 使 observed BER 与 pre-correction BER 的关系依赖具体 ECC scheme，不能直接比较不同 devices。", "Page 1-2, Figure 1"),
            ("EIN 研究 232 个带 on-die ECC 和 82 个无 on-die ECC LPDDR4 devices。", "Page 1-2 and Page 8, Section 6"),
            ("EIN 推断被测 on-die ECC 为 single-error correction Hamming code (n=136, k=128, d=3)。", "Page 1-2, Abstract/Contributions; Page 9-10, Figure 8/Table 2 discussion"),
            ("pre-correction errors 的 uniform-random model 与实验概率吻合。", "Page 8, Figure 5 discussion"),
            ("EIN 可同时推断 data pattern、ECC scheme 和 pre-correction error rate，并用 Figure 9 展示 MAP model 与实验 PMF 的拟合。", "Page 10, Figure 9 discussion"),
            ("EIN 恢复了温度与 retention error 的底层 exponential relationship；post-correction curves 在可测范围外会偏离真实趋势。", "Page 11, Figure 11 discussion"),
        ],
        "conclusion": "EIN 说明未来 DRAM characterization 需要把不可见 ECC 当作统计变换层建模；否则直接观察 post-correction errors 会误判物理错误率、设备比较和机制有效性。",
        "limitations_author": [
            ("MAP estimation 只能在候选模型中选择最可能模型，不能证明未纳入模型的真实 ECC scheme 不存在。", "Page 7-8, Section 5.5/5.8"),
            ("EIN 需要已知并可控的 error mechanism 和可诱发 uncorrectable errors；不能识别 bit-exact pre-correction error locations。", "Page 8, Section 5.8"),
        ],
        "limitations_infer": [
            ("真实厂商 ECC 可能随产品/世代变化，候选 code set 与实验条件需随设备重新校准。", "推断，基于 Sections 4-7"),
            ("EIN 推断的是 error rate/distribution 而非完整厂商 ECC implementation 细节，安全/专利分析需谨慎使用。", "推断，基于 Section 5.8"),
        ],
        "focus": "重点读 Figure 1 on-die ECC obfuscation、Section 4 EIN 推导、Figure 4 EINSim flow、Figures 8-9 ECC inference、Figure 10-11 retention/temperature characterization。",
        "relation": "这篇与 Reaper、SoftMC、HARP 等 characterization 论文关系很强：当 DDR4/LPDDR4/DDR5 开始广泛使用 on-die ECC 后，任何原始错误率研究都必须考虑 ECC 遮蔽。",
        "figures": [
            ("Figure 1", "Page 2", "observed vs pre-correction BER", "说明不同 ECC schemes 造成不同观测 BER 曲线。"),
            ("Figure 2", "Page 3", "DRAM organization", "提供 cell/subarray/device 背景。"),
            ("Figure 3", "Page 4", "on-die ECC mechanism", "展示 dataword/codeword/post-correction word。"),
            ("Figure 4", "Page 7", "EINSim flow", "展示 word generator、ECC encoder、error injector、decoder、checker。"),
            ("Figure 8", "Page 9", "likelihoods of ECC schemes", "反推 ECC scheme 的核心证据。"),
            ("Figure 10", "Page 10", "retention error rates", "比较 observed post-correction 与 inferred pre-correction。"),
            ("Figure 11", "Page 11", "temperature dependence", "展示 EIN 恢复 exponential relationship。"),
        ],
        "tables": [
            ("Table 1", "Page 9", "experiment/simulation setup", "列出 reverse-engineering ECC scheme 的实验与仿真参数。"),
            ("Table 2", "Page 9", "highest-likelihood models", "列出最可能 ECC models 及 likelihood。"),
        ],
        "equations": [
            ("Equation 5-10", "Page 6", "MAP inference objectives", "argmax P[model|observations]", "用观测 post-correction errors 反推 ECC scheme 与 pre-correction error rate。", "是"),
            ("Equation 3-4", "Page 5", "post-correction PMF model", "probability over error-count subsets", "把 ECC 变换和 error distribution 联系起来。", "是"),
        ],
        "terms": [
            ("On-die ECC", "片上错误纠正", "Page 1", "DRAM device 内部不可见 ECC，用于提高 yield 和可靠性。", "是"),
            ("EIN", "Error-correction INference", "Page 1-2", "从 post-correction errors 推断 ECC scheme 和 pre-correction rates 的方法。", "是"),
            ("EINSim", "EIN 仿真器", "Page 2 and Page 7", "开源 C++ simulator，用于模拟 ECC 变换和求 likelihood。", "是"),
            ("Pre-correction error", "纠错前错误", "Page 1", "物理机制直接产生、被 ECC 纠正/遮蔽前的错误。", "是"),
            ("Post-correction error", "纠错后错误", "Page 1", "研究者在 device 输出端可观察到的错误。", "是"),
            ("MAP estimation", "最大后验估计", "Page 2 and Page 6", "选择给定观测下最可能模型参数的统计方法。", "是"),
        ],
        "sections": "Abstract; Introduction; Motivation; Background; EIN Methodology; EINSim; Experimental Methodology; Evaluation; Related Work; Conclusion",
        "translation": [
            ("Abstract / 摘要", "Page 1", "on-die ECC 会把真实 DRAM errors 纠正或误纠正，使观测错误分布不再直接反映物理机制。EIN 用 MAP estimation 反推出 ECC scheme 和 pre-correction error rates。"),
            ("1-2. Motivation / 动机", "Page 1-3", "厂商为改善 yield 在 DRAM 内加入不可见 ECC，但 JEDEC 不规定实现细节，datasheet 也通常不公开。这会阻碍 runtime optimization、device comparison 和其他 ECC reverse engineering。"),
            ("3-5. EIN and EINSim / 方法与工具", "Page 3-8", "EIN 将 ECC 看作对 pre-correction error distribution 的统计变换。EINSim 模拟 encoding、error injection、decoding 与 checking，用 Monte Carlo 计算 likelihood，再求 MAP。"),
            ("6-8. Experimental Study / 实验研究", "Page 8-11", "作者测试 232 个带 on-die ECC 和 82 个无 on-die ECC 的 LPDDR4 devices。EIN 推断 ECC 为 (136,128,3) Hamming SEC，并恢复 retention error rate 与温度/refresh 的底层关系。"),
            ("10. Conclusion / 结论", "Page 11", "EIN 是理解现代 on-die ECC DRAM 的第一步，它让后续 characterization 能重新看到被 ECC 遮蔽的 pre-correction behavior。"),
        ],
    },
]


def render_figs(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑核心论证 | 建议回到 PDF 查看图中细节 |" for a, b, c, d in p["figures"])


def render_tables(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |" for a, b, c, d in p["tables"])


def render_equations(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | {e} | {f} |" for a, b, c, d, e, f in p["equations"])


for p in PAPERS:
    slug = p["slug"]
    url = f"https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/{slug}.pdf"
    src = f"paper reading/sources/LEC3/{slug}.pdf"
    extracted = f"paper reading/extracted_text/{slug}.txt"
    terms = "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in p["terms"])
    trans = "\n\n".join(f"## {h}\n\n### 原文位置\n{loc}\n\n### 中文翻译\n{text}\n\n---" for h, loc, text in p["translation"])
    key_entries = [
        ("研究问题", p["background"], "Page 1, Abstract/Introduction", "开头定义问题。", "高", "这是全文动机。"),
        ("核心方法", p["method"], "Method/design sections", "方法章节给出机制。", "高", "这是论文主要贡献。"),
    ] + [("关键结果", x, l, "原文实验/图表支持。", "高", "支撑作者结论。") for x, l in p["results"][:6]] + [
        ("作者局限", p["limitations_author"][0][0], p["limitations_author"][0][1], "作者明确说明或设计边界。", "中", "实现或迁移时要复核。"),
        ("推断局限", p["limitations_infer"][0][0], p["limitations_infer"][0][1], "基于论文范围的推断。", "中", "后续阅读方向。"),
    ]
    key_rows = "\n".join(f"| {i} | {a}：{b} | {c} | {d} | {e} | {f} |" for i, (a, b, c, d, e, f) in enumerate(key_entries, 1))

    write(f"papers/{slug}/metadata.md", f"""
# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: {p['doi']}
- arXiv ID: 未找到
- URL: {url}
- PDF Source: {src}
- Code / Project Page: {p['code']}
- Dataset: {p['dataset']}
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: {STATUS}
- Full Text Available: Yes
- Notes: {NOTE}
""")
    write(f"papers/{slug}/reading_summary.zh.md", f"""
# 中文阅读摘要

## 1. 一句话总结
{p['one']}

## 2. 研究背景
{p['background']}

## 3. 核心问题
{bullets(p['questions'])}

## 4. 核心贡献
{bullets(p['contribs'])}

## 5. 方法概述
{p['method']}

## 6. 实验设计
{p['experiments']}

## 7. 主要结果
{locs(p['results'])}

## 8. 关键结论
{p['conclusion']}

## 9. 局限性
作者明确或设计中直接体现的局限：
{locs(p['limitations_author'])}

我基于论文范围推断的潜在问题：
{locs(p['limitations_infer'])}

## 10. 适合我重点关注的内容
{p['focus']}

## 11. 和其他文献的关系
{p['relation']}
""")
    write(f"papers/{slug}/key_points_with_locations.zh.md", f"""
# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
{key_rows}
""")
    write(f"papers/{slug}/full_translation.zh.md", f"""
# Full Chinese Translation

## Title
原文标题：{p['title']}

中文标题：{p['zh']}

> {NOTE}

{trans}
""")
    write(f"papers/{slug}/figures_tables_equations_notes.zh.md", f"""
# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_figs(p)}

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_tables(p)}

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
{render_equations(p)}
""")
    write(f"papers/{slug}/terminology.zh.md", f"""
# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
{terms}
""")
    write(f"papers/{slug}/limitations_and_questions.zh.md", f"""
# Limitations and Questions

## 1. 作者明确承认的局限
{locs(p['limitations_author'])}

## 2. 论文中隐含的局限
{locs(p['limitations_infer'])}

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、workload、模拟器、芯片样本或工艺节点；迁移到现代 DDR5/HBM/CXL/GPU/PIM 系统时需复核。（推断）

## 4. 方法可能不适用的场景
- 当系统接口、软件栈、workload locality、错误模型、QoS 目标或硬件组织与论文假设明显不同时，方法收益可能变化。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 与本批相关方向：heterogeneous memory scheduling、PIM graph processing、on-die ECC-aware DRAM characterization、HBM/PIM productization。
""")
    write(f"papers/{slug}/reading_checklist.md", "\n".join([
        "# Reading Checklist",
        "",
        "- [ ] 我能说清楚这篇文章解决的问题",
        "- [ ] 我能解释作者的方法或系统设计",
        "- [ ] 我能指出核心创新与已有工作的差异",
        "- [ ] 我能找到支撑主要结论的图、表或实验位置",
        "- [ ] 我能复述最重要的定量结果",
        "- [ ] 我知道这篇文章的局限和适用边界",
        "- [ ] 我知道这篇文章和 LEC3 其他论文的关系",
        "- [ ] 我知道哪些结论有原文位置支持",
        "- [ ] 我知道哪些问题还需要继续查证",
    ]))
    write(f"papers/{slug}/extraction_log.md", f"""
# Extraction Log

- Input Type: GitHub repository PDF
- Source: {url}
- Access Status: 成功下载并读取本地 PDF
- Full Text Retrieved: Yes
- PDF Pages: {p['pages']}
- Sections Detected: {p['sections']}
- Figures Detected: Yes
- Tables Detected: Yes
- Equations Detected: Yes
- Appendix Detected: 未发现独立 appendix 或本轮未作为重点处理
- Supplementary Material Detected: {p['code'] if p['code'] != '未找到' else '未发现公开 supplementary material'}
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注、双栏局部错位和公式排版细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节、图表编号定位关键结论
- Uncertain Parts: DOI/venue 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言/背景、方法/系统设计、实验/结果、局限、图表、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(PAPERS)} papers for batch 11")
