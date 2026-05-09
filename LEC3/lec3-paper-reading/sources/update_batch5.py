from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATUS = "第五轮深度阅读完成"
NOTE = "说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。"


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


def bullets(xs):
    return "\n".join(f"- {x}" for x in xs)


def locs(xs):
    return "\n".join(f"- {x}（{l}）" for x, l in xs)


P = [
    {
        "slug": "ModernPrimerOnPIM_springer-emerging-computing-bookchapter21",
        "title": "A Modern Primer on Processing in Memory",
        "zh": "Processing in Memory 现代入门",
        "authors": "Onur Mutlu, Saugata Ghose, Juan Gómez-Luna, Rachata Ausavarungnirun",
        "year": "2020/2021",
        "venue": "Springer book chapter / Emerging Computing",
        "doi": "未找到",
        "pages": "42",
        "dataset": "Survey chapter; no new experimental dataset",
        "topic": "PIM survey; data movement; PUM/PNM; adoption challenges",
        "keywords": "PIM, PUM, PNM, RowClone, Ambit, Tesseract, 3D-stacked memory, programming model",
        "one": "这是一篇系统性 PIM 入门综述，从数据移动和内存 scaling 问题出发，梳理 Processing Using Memory 与 Processing Near Memory 两大路线及其落地挑战。",
        "background": "现代系统以 processor-centric 方式把数据搬到计算单元，而数据密集应用、能耗限制和 off-chip data movement 成本共同使这种设计越来越难扩展。",
        "questions": ["为什么 data movement 已经成为性能、能耗和可扩展性瓶颈？", "PUM 与 PNM 的技术基础、收益和限制分别是什么？", "RowClone、Ambit、Tesseract、移动端 PNM、GPU PNM、GenASM/NATSA 等案例之间如何归类？", "PIM 真正进入实际系统还缺哪些编程模型、runtime、coherence、virtual memory 和 benchmark 支持？"],
        "contribs": ["总结 PIM 重新兴起的应用趋势与内存技术趋势。", "区分 Processing Using Memory (PUM) 与 Processing Near Memory (PNM) 两条设计路线。", "用 RowClone、Ambit、Gather-Scatter DRAM、Tesseract、mobile workloads、GPU workloads、genome/time-series 等案例组织领域知识。", "专门讨论 adoption challenges：编程模型、调度、数据映射、一致性、虚拟内存、数据结构、benchmark 和真实硬件。"],
        "method": "综述式组织：先论证 DRAM scaling、RowHammer/retention 等可靠性压力和 data movement 能耗，再按照 PUM/PNM 两类实现路线分层介绍代表工作，最后总结采用 PIM 的系统问题。",
        "experiments": "本文不是新实验论文；主要基于已有论文的定量结果和图示，例如 DRAM bandwidth/latency scaling、RowHammer vulnerability、data movement vs computation energy、RowClone/Ambit/Tesseract/NATSA 等案例。",
        "results": [("DRAM capacity 扩展远快于 bandwidth/latency 改善，主存瓶颈恶化。", "Page 4-6, Figure 1"), ("RowHammer、retention time variation 等可靠性问题说明 memory scaling 需要更智能的 memory controller。", "Page 4-8, Figures 2-3"), ("data movement energy 可比计算高 100-1000x，强化了 PIM 的必要性。", "Page 10-12, Figures 7-8"), ("PUM 可用 RowClone/Ambit 等低成本 DRAM operation 做 bulk copy、initialization、bitwise operations。", "Page 14-18, Figures 10-12"), ("PNM 利用 3D-stacked memory logic layer 支持 Tesseract、移动端 PIM target、GPU offload、genome/time-series 等更通用处理。", "Page 18-24, Figures 15-16 and subsections 7.1-7.6")],
        "conclusion": "PIM 的价值不只是某个加速器，而是把计算系统从 processor-centric 推向 data-centric；但真正落地需要跨 device、architecture、system、programming model 的协同。",
        "limitations_author": [("PIM adoption 仍受 programming model、runtime scheduling、data mapping、coherence、virtual memory 等系统问题限制。", "Page 24-31, Section 8"), ("不同 PIM substrates 的可编程性、成本和可维护性差异很大，不能用单一方案覆盖所有 workload。", "Page 13-24, Sections 5-7")],
        "limitations_infer": [("综述覆盖面大但不是统一实验平台，跨案例的数字不能直接横向比较。", "推断，基于 survey nature"), ("截至本文时间点，commercial PIM adoption 仍处早期，后续标准和产品进展需要另查。", "推断，基于 Section 8-9")],
        "focus": "先读 Page 1-3 和目录建立地图，再读 Page 12-24 的 PUM/PNM 案例，最后读 Page 24-31 的 adoption challenges。",
        "relation": "这篇是本组 LEC3 PIM 论文的总地图；Google PIM、Tesseract、NATSA、NERO、GenASM、SISA 等都可挂到它的 PNM 脉络下。",
        "figures": [("Figure 1", "Page 4", "DRAM capacity/bandwidth/latency scaling", "显示容量、带宽、延迟扩展不均衡。"), ("Figure 8", "Page 12", "data movement vs computation energy", "说明搬数据比算数据昂贵得多。"), ("Figure 9", "Page 13", "3D-stacked DRAM overview", "解释 PNM logic layer 的硬件基础。"), ("Figure 10", "Page 15", "RowClone Fast Parallel Mode", "展示 PUM 如何用 DRAM 行操作完成复制。"), ("Figure 11", "Page 16", "Ambit triple-row activation", "展示 DRAM 内模拟多数逻辑实现 AND/OR。"), ("Figure 15", "Page 19", "Tesseract overview", "展示 graph processing 的 PNM 系统路线。")],
        "tables": [("Table 1", "Page 13", "PUM vs PNM enabling technologies", "对两类 PIM 路线的技术基础与实现位置进行归纳。")],
        "terms": [("Processing-in-Memory (PIM)", "存内/近存处理", "Page 1", "把计算放在数据所在位置附近以减少数据移动。", "是"), ("Processing Using Memory (PUM)", "利用内存本身计算", "Page 13-14", "利用 DRAM/存储器模拟或操作特性完成计算。", "是"), ("Processing Near Memory (PNM)", "近内存处理", "Page 13 and 18", "在 memory controller 或 3D-stacked memory logic layer 中放置计算逻辑。", "是"), ("RowClone", "DRAM 内行复制", "Page 14-15", "用连续 ACTIVATE 等方式做低成本 bulk copy/initialization。", "是"), ("Ambit", "DRAM 内位运算机制", "Page 15-17", "利用 triple-row activation 和 sense amplifier 实现 bulk bitwise operations。", "是")],
        "sections": "Abstract; Introduction; Major Trends; Memory Scaling; Processor-Centric Design; PIM Enablers; PUM; PNM; Adoption; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "本章指出现代系统的大量瓶颈来自把数据搬到计算单元。PIM 把计算机制放在内存芯片、3D-stacked memory logic layer 或 memory controller 附近，以减少或消除数据移动。文章重点讨论 PUM 与 PNM 两类路线及其跨层挑战。"), ("1-5. Motivation and Enablers / 动机与使能技术", "Page 2-14", "作者从 DRAM scaling、RowHammer、retention、hybrid memory、data movement energy 等趋势解释为什么需要 intelligent memory。3D-stacked memory 和新型非易失内存为 PIM 提供了新的物理基础。"), ("6. Processing Using Memory / PUM", "Page 14-18", "PUM 利用 DRAM 内部操作特性做计算。RowClone 适合 bulk copy/initialization；Ambit 适合 bulk bitwise operations；其他机制把 DRAM 用作安全 primitive 或 gather-scatter substrate。"), ("7. Processing Near Memory / PNM", "Page 18-24", "PNM 在内存附近加入可编程或专用逻辑。案例包括 Tesseract graph processing、移动端 Google workload function offload、GPU NDP、PIM-enabled instructions、genome analysis 和 time-series analysis。"), ("8-9. Adoption and Outlook / 落地挑战与展望", "Page 24-31", "要让 PIM 真正可用，还需要编程模型、代码生成、runtime scheduling、data mapping、coherence、virtual memory、数据结构和 benchmark 支持。作者主张以 data-centric 方式重新设计系统。")],
    },
    {
        "slug": "NATSA_time-series-analysis-near-data_iccd20",
        "title": "NATSA: A Near-Data Processing Accelerator for Time Series Analysis",
        "zh": "NATSA：面向时间序列分析的近数据处理加速器",
        "authors": "Ivan Fernandez, Ricardo Quislant, Christina Giannoula, Mohammed Alser, Juan Gómez-Luna, Eladio Gutiérrez, Oscar Plata, Onur Mutlu",
        "year": "2020",
        "venue": "ICCD 2020",
        "doi": "未找到",
        "pages": "10",
        "dataset": "Synthetic time series; ECG and seismology data; SCRIMP/matrix profile workloads",
        "topic": "Near-data processing; time series analysis; matrix profile; HBM",
        "keywords": "NATSA, matrix profile, time series, HBM, NDP, SCRIMP, anytime algorithm",
        "one": "NATSA 用 HBM logic-layer 附近的专用浮点处理单元计算 matrix profile，显著减少时间序列分析的数据移动瓶颈。",
        "background": "Matrix profile 是 exact anytime motif/discord discovery 的代表算法，但低算术强度和大数据量让 CPU/GPU 实现受内存带宽与数据移动限制。",
        "questions": ["matrix profile 的 distance matrix/profile/profile index 如何构成主要计算？", "如何把对角线计算划分到 near-HBM processing units，同时保持 anytime property？", "专用 NDP accelerator 相比多核 CPU、GPU 和通用 NDP core 有多大收益？", "HBM 带宽、精度和窗口大小如何影响 NATSA？"],
        "contribs": ["提出第一个面向 time series analysis 的 near-data processing accelerator。", "设计针对 matrix profile 的专用 floating-point PUs/DCU/DPU，贴近 HBM 接口。", "提出 diagonal scheduling/partitioning scheme，兼顾负载均衡与 anytime property。", "对性能、能耗、面积和 HBM/DDR4/general-purpose NDP 进行比较。"],
        "method": "NATSA 将 time series 数据放在 3D-stacked HBM 中，多个 processing units 直接从 HBM 读取并计算 matrix profile 的对角线。设计包含 dot product/update、Euclidean distance、profile update 等专用单元，并通过 diagonal scheduling 分配工作。",
        "experiments": "基线包括 DDR4-OoO multicore、HBM-OoO、HBM-inOrder general-purpose NDP、Intel Xeon Phi KNL、NVIDIA GPU 等；评估 synthetic rand 128K-2M、ECG、seismology 等数据，比较 double/single precision、性能、能耗、面积。",
        "results": [("NATSA 相比 state-of-the-art multi-core baseline 最高 14.2x、平均 9.9x 性能提升。", "Page 1-2, Abstract/Introduction; Page 6, Figure 7"), ("能耗最高降低 27.2x、平均降低 19.4x。", "Page 1-2 and Page 7, Figure 9"), ("相比 64 in-order core general-purpose NDP，NATSA 性能提升 6.3x、能耗降低 10.2x。", "Page 1-2 and Page 7"), ("NATSA 比 Xeon Phi KNL 和 GTX 1050 在等效性能点有更小面积，且分别节能 11.0x 和 4.1x。", "Page 2 and Page 7, Figures 9-10"), ("HBM 能让 SCRIMP 更好扩展，但通用 core 仍无法完全利用 HBM 带宽。", "Page 3 and Page 8, Figures 3 and 11")],
        "conclusion": "时间序列 matrix profile 属于典型 memory-bound 数据密集 workload；只有把定制计算贴近 HBM 并平衡带宽与计算单元，才能同时获得性能和能效。",
        "limitations_author": [("NATSA 专注 matrix profile/SCRIMP 类 exact anytime 算法，通用性低于 general-purpose NDP cores。", "Page 2-5, design scope"), ("某些 scheduling 模式可能牺牲 anytime property 来换取优化机会。", "Page 5, Section 4 scheduling")],
        "limitations_infer": [("专用 accelerator 的收益依赖 HBM 带宽和足够大的 time series；小数据或不同算法可能收益较低。", "推断，基于 Figures 7 and 11"), ("实际集成需要考虑 HBM 容量、主机接口、编程栈和数据预处理成本。", "推断，基于 system design")],
        "focus": "重点读 Page 2 的 Eq.1/Matrix Profile 定义、Page 4-5 NATSA 架构和调度、Page 6-8 Figures 7-11 结果。",
        "relation": "与 Modern Primer 的 PNM time-series 案例对应；也与 NERO/GenASM/SISA 一样展示 domain-specific near-data acceleration。",
        "figures": [("Figure 1", "Page 1", "time series anomaly and matrix profile", "解释 profile 高值如何对应 anomaly。"), ("Figure 2", "Page 2", "distance matrix/profile/index", "定义核心数据结构。"), ("Figure 5", "Page 4", "NATSA design near HBM", "展示 PUs 与 HBM 接口连接。"), ("Figure 6", "Page 5", "diagonal scheduling", "说明负载分配和 anytime property。"), ("Figure 7", "Page 6", "speedup", "展示 NATSA 性能收益。"), ("Figure 9", "Page 7", "energy consumption", "展示 NATSA 能耗优势。")],
        "tables": [("Table 1", "Page 6", "synthetic time series", "列出性能评估用 synthetic workloads。"), ("Table 3", "Page 8", "NATSA components for 48 PUs", "展示设计空间中的资源配置。")],
        "terms": [("Matrix profile", "矩阵轮廓", "Page 1-2", "每个 subsequence 与最相似 subsequence 的距离数组。", "是"), ("Anytime algorithm", "可中断算法", "Page 1", "随时停止也能返回当前有效近似结果的算法。", "是"), ("Diagonal scheduling", "对角线调度", "Page 5", "按 distance matrix 对角线划分工作，降低同步并保持算法性质。", "是"), ("High Bandwidth Memory (HBM)", "高带宽内存", "Page 1-2", "3D-stacked memory，为 near-data accelerator 提供高带宽。", "是"), ("Processing Unit (PU)", "处理单元", "Page 4", "NATSA 中计算 matrix profile 的专用近存单元。", "是")],
        "sections": "Abstract; Introduction; Matrix Profile; Motivation; NATSA Design; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "NATSA 针对 matrix profile 的大数据、低算术强度特点，把专用浮点计算单元放到 HBM 附近。相比多核实现，它最高提升 14.2x 性能、最高降低 27.2x 能耗。"), ("1-2. Background / 背景", "Page 1-3", "时间序列 motif/discord discovery 可用于流行病学、基因组、神经科学等领域。Matrix profile 用欧氏距离构建 distance matrix、profile 和 profile index，但数据移动成为主要瓶颈。"), ("3-4. NATSA Design / 方法", "Page 3-5", "NATSA 贴近 HBM 设计多个专用 PU，支持 dot product、distance computation 和 profile update。diagonal scheduling 把 distance matrix 的对角线分给不同 PU，降低负载不均并保留 anytime 特性。"), ("5-6. Evaluation / 评估", "Page 5-8", "实验比较 DDR4/HBM 多核、通用 NDP、GPU 和 NATSA。NATSA 在大 time series 上利用 HBM 带宽更充分，性能、能耗和面积均优于通用平台。"), ("8. Conclusion / 结论", "Page 9", "作者总结 NATSA 说明 time series analysis 是近数据专用加速的合适目标：当算法 memory-bound 且计算模式稳定时，贴近 HBM 的专用设计可以明显优于搬数据到 CPU/GPU。")],
    },
    {
        "slug": "NERO-near-memory-stencil-acceleration-for-weather_fpl20",
        "title": "NERO: A Near High-Bandwidth Memory Stencil Accelerator for Weather Prediction Modeling",
        "zh": "NERO：面向天气预报建模的近 HBM stencil 加速器",
        "authors": "Gagandeep Singh, Dionysios Diamantopoulos, Christoph Hagleitner, Juan Gómez-Luna, Sander Stuijk, Onur Mutlu, Henk Corporaal",
        "year": "2020",
        "venue": "FPL 2020",
        "doi": "未找到",
        "pages": "9",
        "dataset": "COSMO weather model vadvc and hdiff compound stencil kernels",
        "topic": "FPGA+HBM; weather prediction; stencil acceleration; near-memory computing",
        "keywords": "NERO, HBM, FPGA, stencil, COSMO, POWER9, CAPI2, vadvc, hdiff",
        "one": "NERO 在 FPGA+HBM 上为 COSMO 天气模型的 compound stencil kernels 构建近内存加速器，相比 16-core POWER9 同时提升性能和能效。",
        "background": "天气/气候模型中的 vadvc 和 hdiff 等 compound stencil 具有复杂不规则访问和低算术强度，在 POWER9 CPU 上受 DRAM bandwidth 限制，常规 CPU 优化难以突破 roofline。",
        "questions": ["FPGA+HBM 能否缓解天气 prediction stencil 的 memory bandwidth bottleneck？", "如何在 CAPI2/SNAP 框架下把 host、FPGA、HBM 和 on-chip memory hierarchy 协同起来？", "HBM ports、PE 数量、tile/window size 和 URAM/BRAM/HBM 分层如何影响性能？", "相对 POWER9 与 DDR4-FPGA，HBM-FPGA 的性能/能耗收益多大？"],
        "contribs": ["提出 NERO，第一个 near-HBM FPGA-based accelerator for COSMO compound stencils。", "为 vadvc 和 hdiff 设计 hardware-software framework 和优化 API。", "使用高层综合与 auto-tuning 搜索 tile/window/resource 配置。", "在真实 POWER9+CAPI2+HBM FPGA 平台上评估性能、能耗和扩展性。"],
        "method": "NERO 将 HBM-based FPGA 作为 CAPI2 coherent accelerator 接入 POWER9。host 通过 SNAP API 发起任务，数据经 DMA 到 FPGA/HBM；多个 PE 使用独立 HBM ports，并结合 URAM/BRAM/HBM 层次缓存 compound stencil 所需邻域数据。",
        "experiments": "平台为 IBM POWER9 AC922 和 HBM2 FPGA board；对 vadvc、hdiff 做 single/half precision、DDR4 vs HBM FPGA、不同 PE 数量、auto-tuning 与 energy efficiency 比较。",
        "results": [("POWER9 roofline 显示 vadvc/hdiff 受 host DRAM bandwidth 限制，64-thread 性能仅 29.1/58.5 GFLOP/s。", "Page 1, Figure 1"), ("HBM-based NERO 对 vadvc 和 hdiff 分别比 16-core POWER9 快 4.2x 和 8.3x。", "Page 1-2; Page 6, Figure 6"), ("相同两个 kernel 的能耗分别降低 22x 和 29x。", "Page 1-2; Page 7, Figure 7"), ("能效达到约 1.5 GFLOPS/Watt 和 17.3 GFLOPS/Watt。", "Page 1 and Page 7"), ("HBM ports 与 PE 数量线性扩展有助于 hdiff/vadvc，但资源和 window size 选择决定面积-性能权衡。", "Page 4-6, Figures 3 and 5-6")],
        "conclusion": "NERO 说明 weather stencil 这类低算术强度、内存受限 workload 适合用近 HBM FPGA 加速，但需要面向应用的数据布局、memory hierarchy 和 auto-tuning。",
        "limitations_author": [("本文聚焦 COSMO 的 vadvc/hdiff 两个代表 kernel，不等于完整天气模型端到端加速。", "Page 1-2 and Section 2"), ("FPGA 需要足够并行性与细致映射来弥补较低频率。", "Page 2, Introduction")],
        "limitations_infer": [("CAPI2/POWER9/HBM FPGA 平台特定，迁移到 CXL/CCIX 或不同 FPGA 需重新调优。", "推断，基于 platform setup"), ("compound stencil 的边界处理、全模型通信和多节点扩展未成为本文重点。", "推断，基于 kernel scope")],
        "focus": "先读 Figure 1 roofline，再读 Figure 3/4 系统架构，最后读 Figure 6/7 性能能效。",
        "relation": "与 NATSA 同为 HBM 近数据专用加速器；NATSA 面向 matrix profile，NERO 面向 weather compound stencil。",
        "figures": [("Figure 1", "Page 1", "POWER9/FPGA roofline", "说明 CPU 受内存带宽限制。"), ("Figure 2", "Page 3", "POWER9 + HBM FPGA platform", "展示 CAPI2 连接和 HBM stacks。"), ("Figure 3", "Page 4", "NERO architecture/data flow", "展示 PE、HBM port、URAM/BRAM/HBM 数据流。"), ("Figure 4", "Page 5", "NERO application framework", "展示 SNAP API 与 job manager。"), ("Figure 6", "Page 6", "performance vs PE count", "展示 HBM/DDR4 FPGA 和 POWER9 性能对比。"), ("Figure 7", "Page 7", "energy efficiency", "展示 GFLOPS/Watt 优势。")],
        "tables": [("Table 1", "Page 5", "system parameters", "记录 POWER9 与 FPGA/HBM 配置。")],
        "terms": [("Compound stencil", "复合 stencil", "Page 1-2", "天气模型中由多种邻域访问和计算模式组合而成的 stencil kernel。", "是"), ("CAPI2", "Coherent Accelerator Processor Interface 2", "Page 1-3", "POWER9 与 FPGA coherent accelerator 的连接接口。", "是"), ("HBM port", "HBM 端口", "Page 4", "PE 访问 HBM 带宽的并行入口。", "是"), ("Processing Element (PE)", "处理单元", "Page 4", "NERO 中执行 stencil 计算的 FPGA 单元。", "是"), ("COSMO", "小尺度天气模型联盟模型", "Page 1", "本文的天气预测模型来源。", "是")],
        "sections": "Abstract; Introduction; Background; Design Methodology; Application Framework; Evaluation; Related Work; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "NERO 针对天气预测模型中的 compound stencil kernel，使用 FPGA+HBM 近内存加速。实验显示 vadvc/hdiff 相比 16-core POWER9 分别快 4.2x/8.3x，能耗降低 22x/29x。"), ("1-2. Background / 背景", "Page 1-3", "COSMO dycore 包含 horizontal stencils、vertical tridiagonal solvers 和 point-wise computation。vadvc 与 hdiff 代表这种复杂访问和低算术强度，roofline 表明 CPU 受 DRAM 带宽限制。"), ("3. NERO Design / 设计", "Page 3-5", "NERO 通过 CAPI2/SNAP 连接 host 与 FPGA。数据从 host 传入 FPGA/HBM，多个 PE 使用独立 HBM ports 和 URAM/BRAM/HBM 层次读取邻域数据。auto-tuning 用于选择 tile/window 和资源配置。"), ("4. Evaluation / 评估", "Page 5-7", "HBM-based design 随 PE 增加取得更好扩展，相比 DDR4-FPGA 更能支撑 stencil bandwidth。最终设计在性能和能效上均明显优于 POWER9。"), ("5-6. Related Work and Conclusion / 相关工作与结论", "Page 8-9", "作者认为 near-HBM FPGA 是天气预测建模的有前景路线，但核心在于根据 kernel 访问模式定制 memory hierarchy 和并行结构。")],
    },
    {
        "slug": "Ramulator2_arxiv23",
        "title": "Ramulator 2.0: A Modern, Modular, and Extensible DRAM Simulator",
        "zh": "Ramulator 2.0：现代、模块化、可扩展的 DRAM 模拟器",
        "authors": "Haocong Luo, Yahya Can Tuğrul, F. Nisa Bostancı, Ataberk Olgun, A. Giray Yağlıkçı, Onur Mutlu",
        "year": "2023",
        "venue": "arXiv / simulator paper",
        "doi": "未找到",
        "pages": "4",
        "dataset": "Validation traces; RowHammer mitigation case study workloads",
        "topic": "DRAM simulation; modular memory controller; RowHammer mitigation evaluation",
        "keywords": "Ramulator 2.0, DRAM simulator, DDR5, LPDDR5, HBM3, GDDR6, RowHammer, PARA, Hydra",
        "one": "Ramulator 2.0 通过 interface/implementation/plugin 架构把 DRAM controller、device spec 和研究扩展解耦，使新标准和 RowHammer mitigation 可快速模块化评估。",
        "background": "内存系统研究越来越需要修改 controller 和 DRAM 行为，但旧模拟器常把 DRAM spec 与 controller 强耦合，新增命令、时序或防御机制成本高。",
        "questions": ["如何把 DRAM memory system 的关键组件抽象为可替换 interface/implementation？", "如何用简洁可读的 syntax 描述 DDR5/LPDDR5/HBM3/GDDR6 等标准？", "RowHammer mitigation 能否作为 plugin 接入不修改 baseline controller？", "模块化是否牺牲验证准确性和 simulation speed？"],
        "contribs": ["提出 C++20 模块化 DRAM simulator，可作为 standalone 或 gem5 memory library。", "提供 human-readable DRAM specification syntax 和 reusable templated lambda functions。", "实现 DDR5、LPDDR5、HBM3、GDDR6 以及 DDR3/DDR4/HBM 等标准。", "将 PARA、TWiCe、Graphene、Hydra、RRS、ideal refresh mitigation 作为 plugins 实现。", "开源 MIT license。"],
        "method": "Ramulator 2.0 将 frontend、address mapper、memory controller、scheduler、refresh manager、DRAM device model 等组件定义为 interfaces，并允许多个 implementations。controller plugins 在 issued DRAM command 触发点更新状态，用统一接口请求 refresh/maintenance。",
        "experiments": "论文展示软件架构、RowHammer mitigation plugin case study、与 Micron Verilog model 的 command trace 验证，以及与 Ramulator 1.0/DRAMsim2/DRAMsim3/USIMM 的 simulation speed 对比。",
        "results": [("DDR4 timing constraints 示例从 Ramulator 1.0 的 82 行减少到 32 行，降低 61% 代码量。", "Page 3, Section 2.2"), ("六种 RowHammer mitigation 可作为 plugins 接入同一未修改 controller。", "Page 1-2, Figures 1-2"), ("Ramulator 2.0 对 Micron Verilog Model 做命令 trace 验证。", "Page 3, Section 3.1"), ("simulation speed 与现有 cycle-accurate DRAM simulators 相比保持快速。", "Page 3, Table 1"), ("RowHammer case study 显示现有 mitigation 在低 tRH 下性能开销明显，说明需要更高效可扩展方案。", "Page 3-4, Figure 3")],
        "conclusion": "Ramulator 2.0 的重点不是提出新的 DRAM policy，而是提供能快速实现、验证和比较新 memory-controller/DRAM design ideas 的基础设施。",
        "limitations_author": [("论文篇幅短，重点展示框架与案例，未覆盖所有可能 DRAM/SoC 集成场景。", "Page 1-4"), ("cycle-accurate DRAM simulator 仍依赖模型准确性和配置正确性。", "Page 3 validation section")],
        "limitations_infer": [("C++20 和插件架构提高扩展性，但用户仍需理解 DRAM timing/state machine 才能安全修改。", "推断，基于 Section 2"), ("RowHammer case study 是展示模块化能力，不等同于完整防御方案排名。", "推断，基于 Section 3.3")],
        "focus": "重点读 Page 1 的问题与贡献、Page 2 的 interface/implementation 架构、Page 3 的 spec syntax/validation/speed、Figure 3 的 RowHammer case study。",
        "relation": "它为 LEC3 中大量 DRAM reliability/RowHammer 工作提供评估基础设施语境，尤其适合理解 PRAC/Chronus/Svärd 等防御如何在 simulator 中比较。",
        "figures": [("Figure 1", "Page 2", "software architecture", "展示 Ramulator 2.0 组件接口和请求路径。"), ("Figure 2", "Page 2", "RowHammer mitigation plugins", "展示 PARA/Graphene/TRR/Hydra/RFM 等如何作为插件。"), ("Figure 3", "Page 4", "RowHammer mitigation overhead", "展示不同 tRH 下 defense overhead。")],
        "tables": [("Table 1", "Page 3", "simulation performance comparison", "比较 Ramulator 2.0 与其他 DRAM simulators 的速度。")],
        "terms": [("Interface / Implementation", "接口/实现", "Page 2", "Ramulator 2.0 中解耦组件功能与具体行为的核心抽象。", "是"), ("Controller plugin", "控制器插件", "Page 2", "不修改 baseline controller 即可接入统计或防御机制。", "是"), ("DRAM specification syntax", "DRAM 规格描述语法", "Page 2-3", "用简洁字符串和模板函数定义组织、命令、时序和状态。", "是"), ("Refresh Management (RFM)", "刷新管理", "Page 1-3", "DDR5/LPDDR5/GDDR6/HBM3 等标准中的维护命令之一。", "是"), ("RowHammer mitigation", "RowHammer 缓解机制", "Page 1-4", "PARA/TWiCe/Graphene/Hydra/RRS 等防御插件。", "是")],
        "sections": "Introduction; Design Features; Validation; Simulation Speed; RowHammer Case Study; Conclusion",
        "translation": [("Abstract / 摘要", "Page 1", "Ramulator 2.0 是模块化、可扩展的 DRAM simulator，支持快速实现 memory controller 与 DRAM design changes。它提供独立接口、简洁 DRAM spec syntax、新标准支持、RowHammer mitigation plugins，并以 MIT license 开源。"), ("1. Introduction / 引言", "Page 1", "作者指出现有模拟器难以承载 intrusive design changes，因为 controller、DRAM spec、时序和功能实现耦合。Ramulator 2.0 的目标是让新标准、新调度、新 mitigation 能以模块方式加入。"), ("2. Design Features / 设计特性", "Page 2-3", "框架用 Interface 和 Implementation 抽象组件，配置文件实例化具体实现。DRAM specification 使用 human-readable 字符串、permutation timing constraints 和 templated lambda functions，减少重复代码。"), ("3. Evaluation / 验证与案例", "Page 3-4", "作者通过命令 trace 对照 Verilog model 验证正确性，比较 simulation speed，并以六种 RowHammer mitigation 展示 controller plugin 能力。"), ("Conclusion / 结论", "Page 4", "Ramulator 2.0 的价值在于让内存系统研究更敏捷：研究者可以更快实现复杂 controller/DRAM 修改，并在统一框架中比较。")],
        "code": "https://github.com/CMU-SAFARI/ramulator2",
    },
    {
        "slug": "RowHammer-Retrospective_ieee_tcad19",
        "title": "RowHammer: A Retrospective",
        "zh": "RowHammer 回顾",
        "authors": "Onur Mutlu, Jeremie S. Kim",
        "year": "2019",
        "venue": "IEEE TCAD retrospective article",
        "doi": "未找到",
        "pages": "16",
        "dataset": "Survey/retrospective; summarizes 129-module RowHammer study and follow-up works",
        "topic": "RowHammer; DRAM reliability; hardware security; mitigations",
        "keywords": "RowHammer, disturbance errors, PARA, Google Project Zero, DRAM security, memory scaling",
        "one": "这篇回顾把 RowHammer 从 DRAM disturbance error、真实攻击、缓解机制、后续研究和未来 memory security 方法论五个层面系统串起来。",
        "background": "RowHammer 证明电路级失效机制可以变成广泛、实用的系统安全漏洞；随着 DRAM scaling，类似问题可能继续出现。",
        "questions": ["RowHammer 的物理机制和可重复 bit flip 特性是什么？", "为什么用户态 hammering 能破坏 memory isolation 并触发权限提升？", "原始 ISCA 2014 论文和后续工作提出了哪些 mitigation？", "为什么作者主张 principled system-memory co-design 而不只是补丁式防御？"],
        "contribs": ["总结 ISCA 2014 RowHammer 发现：129 个模块中 110 个出现错误，2012-2013 模块全部脆弱。", "回顾 Google Project Zero 及后续 VM/mobile/JavaScript/RDMA 等攻击路线。", "归纳原始七类防御和后续研究防御，重点讨论 PARA。", "把 RowHammer 放入更广泛的 memory scaling、NAND/PCM 类 disturbance/security 问题中讨论。", "提出面向未来 memory reliability/security 的原则性研究方法。"],
        "method": "回顾性 survey：先复述 RowHammer 机制与原始实验，再按 attacks、defenses、circuit-level studies、platforms、persistence、broader context 分类梳理后续文献。",
        "experiments": "本文本身不是新实验论文；关键证据来自原始 RowHammer study 的 129 DRAM modules、Google Project Zero 攻击和多篇后续研究。",
        "results": [("原始研究测试 129 个 2008-2014 年模块，其中 110 个表现 RowHammer errors，最早可追溯到 2010。", "Page 2, Figure 1"), ("2012-2013 年模块全部 vulnerable，说明问题随制程缩放显著出现。", "Page 2, Figure 1 discussion"), ("Google Project Zero 2015 证明用户态程序可利用 RowHammer 获取 kernel privileges。", "Page 1 and Section III-A"), ("PARA 以很低概率刷新 adjacent rows，p=0.001 或 0.005 时可提供强保证且性能开销小于 0.75%。", "Page 4, Section II-E"), ("ECC、提高 refresh rate、row remapping、access counters 等方案各有成本或覆盖限制。", "Page 4-8, Sections II-E and III-B")],
        "conclusion": "RowHammer 的根本启示是硬件可靠性缺陷可能直接破坏安全边界；未来需要可观测、可建模、可更新的 memory-system co-design，而不是在问题暴露后单点修补。",
        "limitations_author": [("提高 refresh rate 是直接短期方案，但会带来显著性能/能耗问题。", "Page 7, Section III-B"), ("PARA 虽低开销，但需要 memory controller 或 DRAM chip/interface 支持。", "Page 4 and Page 8, PARA discussion")],
        "limitations_infer": [("作为 retrospective，它整合已有结果，不提供统一实验复现。", "推断，基于文章类型"), ("2019 之后 TRR bypass、RowPress、VRD 等新现象需要继续读更新文献。", "推断，基于发表时间")],
        "focus": "重点读 Page 1-4 的 RowHammer 机制和 PARA，再读 Section III-A/III-B 的攻击防御谱系，最后读 Section IV 的未来方法论。",
        "relation": "它是 RowHammer 线索的历史总览；后续 2020-2026 的 TRRespass、RowPress、Svärd、PRAC、Chronus、VRD 等论文可看作对这篇展望的延伸。",
        "figures": [("Figure 1", "Page 2", "error rate vs manufacture date", "展示 129 个模块中 RowHammer vulnerability 随年代出现。"), ("Figure 2", "Page 7", "refresh rate vs RowHammer errors", "说明仅提高 refresh rate 成本高。")],
        "tables": [("Table I", "Page 7", "uncorrectable multi-bit RowHammer errors", "说明普通 ECC 对多 bit RowHammer error 覆盖有限。")],
        "terms": [("RowHammer", "行锤击", "Page 1", "反复访问 aggressor row 导致相邻 victim row bit flips 的 DRAM disturbance 现象。", "是"), ("Disturbance error", "扰动错误", "Page 1-3", "电路组件间干扰导致非目标 cell 状态改变。", "是"), ("PARA", "Probabilistic Adjacent Row Activation", "Page 4", "关闭 row 时以低概率刷新相邻行的防御机制。", "是"), ("Memory isolation", "内存隔离", "Page 2-4", "访问一个地址不应影响其他地址的数据，是系统可靠性和安全的基础。", "是"), ("Targeted refresh", "定向刷新", "Page 8", "只刷新被认为可能受 hammering 影响的相邻行。", "是")],
        "sections": "Abstract; Introduction; RowHammer Summary; Attacks; Defenses; Circuit Studies; Platforms; Future Directions",
        "translation": [("Abstract / 摘要", "Page 1", "文章回顾 RowHammer：反复访问某个 DRAM row 会在相邻 row 的可预测 bit 位置引发 bit flips。Google Project Zero 之后，多种实际攻击证明它是硬件可靠性问题转化为安全漏洞的代表。"), ("I-II. Problem Summary / 问题总结", "Page 1-4", "作者复述原始 ISCA 2014 发现、RowHammer 的 circuit-level disturbance 机制、用户态触发方式和可重复 bit flip 特征。129 个模块中 110 个有错误，说明问题广泛存在。"), ("III-A. Attacks / 攻击", "Page 4-6", "后续攻击包括 kernel privilege escalation、VM takeover、mobile device attack、JavaScript/WebGL/RDMA 远程触发等。核心都是利用 RowHammer 打破 memory isolation。"), ("III-B. Defenses / 防御", "Page 6-9", "防御包括制造更可靠 DRAM、ECC、提高刷新率、remapping/retirement、runtime detection、access counters、PARA 等。PARA 以低概率 adjacent-row refresh 获得强保证，但需要 controller/DRAM 支持。"), ("IV. Future Directions / 未来方向", "Page 12-15", "作者把 RowHammer 放到更广泛的 memory scaling/security 语境中，主张通过系统-内存协同、可观测接口、可配置 controller 和更早期的 vulnerability discovery 来避免下一类问题。")],
    },
]


def fig_rows(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑核心论证 | 建议回到 PDF 查看坐标/标注 |" for a, b, c, d in p["figures"]) or "| 未检测到核心图 | - | - | - | - | - |"


def table_rows(p):
    return "\n".join(f"| {a} | {b} | {c} | {d} | 支撑方法/实验理解 | 建议回到 PDF 查看细项 |" for a, b, c, d in p["tables"]) or "| 未检测到核心表 | - | - | - | - | - |"


for p in P:
    slug = p["slug"]
    url = f"https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/{slug}.pdf"
    source = f"paper reading/sources/LEC3/{slug}.pdf"
    extracted = f"paper reading/extracted_text/{slug}.txt"
    code = p.get("code", "未找到")
    terms = "\n".join(f"| {a} | {b} | {c} | {d} | {e} |" for a, b, c, d, e in p["terms"])
    trans = "\n\n".join(f"## {h}\n\n### 原文位置\n{loc}\n\n### 中文翻译\n{text}\n\n---" for h, loc, text in p["translation"])
    key_rows = []
    entries = [
        ("研究问题", p["background"], "Page 1, Abstract/Introduction", "论文开头明确给出动机。", "高", "这是后续方法的出发点。"),
        ("核心方法", p["method"], "Method/design or survey sections", "正文方法/综述结构支撑。", "高", "关注作者如何把问题切成可执行机制。"),
    ] + [("关键结果", x, l, "原文给出定量或分类证据。", "高", "这些结果支撑主要结论。") for x, l in p["results"][:5]] + [
        ("局限", p["limitations_author"][0][0], p["limitations_author"][0][1], "作者边界或设计假设体现。", "中", "迁移/复现时要先检查。"),
        ("追问", p["limitations_infer"][0][0], p["limitations_infer"][0][1], "基于实验范围的推断。", "中", "适合后续补读。"),
    ]
    for i, e in enumerate(entries, 1):
        key_rows.append(f"| {i} | {e[0]}：{e[1]} | {e[2]} | {e[3]} | {e[4]} | {e[5]} |")

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
- PDF Source: {source}
- Code / Project Page: {code}
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
{chr(10).join(key_rows)}
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
{fig_rows(p)}

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{table_rows(p)}

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| {'Equation 1' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '未检测到核心编号公式'} | {'Page 2' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '-'} | {'matrix profile 的 Euclidean distance 计算' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '本轮阅读未发现必须掌握的核心编号公式'} | {'Qi,j、mu、sigma、m 等' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '-'} | {'用 dot product、均值和标准差高效计算 subsequence 距离' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '-'} | {'是' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else '否'} |
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
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
{bullets(p['questions'])}

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。
""")
    write(f"papers/{slug}/reading_checklist.md", "\n".join(["# Reading Checklist", "", "- [ ] 我能说清楚这篇文章解决的问题", "- [ ] 我能解释作者的方法或综述结构", "- [ ] 我能指出核心创新与已有工作的差异", "- [ ] 我能找到支撑主要结论的图、表或实验位置", "- [ ] 我能复述最重要的定量结果或分类结论", "- [ ] 我知道这篇文章的局限和适用边界", "- [ ] 我知道这篇文章和 LEC3 其他论文的关系", "- [ ] 我知道哪些结论有原文位置支持", "- [ ] 我知道哪些问题还需要继续查证"]))
    write(f"papers/{slug}/extraction_log.md", f"""
# Extraction Log

- Input Type: GitHub repository PDF
- Source: {url}
- Access Status: 成功下载并读取本地 PDF
- Full Text Retrieved: Yes
- PDF Pages: {p['pages']}
- Sections Detected: {p['sections']}
- Figures Detected: Yes
- Tables Detected: {'Yes' if p['tables'] else 'No core tables detected in this round'}
- Equations Detected: {'Yes' if slug == 'NATSA_time-series-analysis-near-data_iccd20' else 'No core numbered equations detected in this round'}
- Appendix Detected: 未发现独立 appendix 或本轮未作为重点处理
- Supplementary Material Detected: 未发现
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注和双栏排版细节建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节和图表编号定位关键结论
- Uncertain Parts: DOI/arXiv 如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言、方法/综述结构、实验/案例、主要结果、局限、图表/公式、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(P)} papers for batch 5")
