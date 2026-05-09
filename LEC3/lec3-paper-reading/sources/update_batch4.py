from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(rel, text):
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


STATUS = "第四轮深度阅读完成"
COPYRIGHT_NOTE = "说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料；`full_translation.zh.md` 采用逐节中文详译/译述方式，不提供逐字复刻式全文翻译。"


PAPERS = [
    {
        "slug": "Google-consumer-workloads-data-movement-and-PIM_asplos18",
        "title": "Google Workloads for Consumer Devices: Mitigating Data Movement Bottlenecks",
        "zh_title": "面向消费设备的 Google 工作负载：缓解数据移动瓶颈",
        "authors": "Amirali Boroumand, Saugata Ghose, Youngsok Kim, Rachata Ausavarungnirun, Eric Shiu, Rahul Thakur, Daehyun Kim, Aki Kuusela, Allan Knies, Parthasarathy Ranganathan, Onur Mutlu",
        "year": "2018",
        "venue": "ASPLOS 2018",
        "doi": "10.1145/3173162.3173177",
        "url": "https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/Google-consumer-workloads-data-movement-and-PIM_asplos18.pdf",
        "pages": "16",
        "dataset": "Chrome Telemetry web workloads; TensorFlow Mobile networks; VP9 video playback/capture traces",
        "topic": "Processing-in-Memory; consumer workloads; data movement energy",
        "keywords": "PIM, data movement, Chrome, TensorFlow Mobile, VP9, HBM/HMC, energy efficiency",
        "one": "这篇文章用 Google 消费设备工作负载证明数据移动是主要能耗瓶颈，并评估把简单数据密集型函数卸载到 PIM core/accelerator 后可显著降低能耗和执行时间。",
        "background": "消费设备受电池容量和热设计功耗限制，但 Chrome、移动端 ML、视频播放和视频采集等应用的数据移动开销持续上升；作者希望判断 processing-in-memory 是否能在消费设备严格面积/功耗约束下带来实际收益。",
        "questions": [
            "消费设备常见工作负载中，多少能耗来自主存与计算单元之间的数据移动？",
            "哪些函数/primitive 同时占用大量能耗、以数据移动为主、又适合放到 PIM logic 执行？",
            "在有限 logic-layer 面积与功耗预算下，PIM core 与 fixed-function PIM accelerator 分别是否划算？",
            "PIM 与已有专用硬件/压缩技术相比是否仍有额外价值？",
        ],
        "contribs": [
            "系统分析 Chrome、TensorFlow Mobile、VP9 视频播放/采集四类 Google 消费端工作负载的数据移动能耗。",
            "提出 PIM target 的筛选准则：能耗占比高、memory-bound、在简单 PIM logic 上运行不拖慢整体执行。",
            "给出两类 PIM 实现路线：低功耗通用 PIM core 与按函数定制的 PIM accelerator。",
            "证明 PIM targets 多由 memcopy、memset、basic arithmetic、bitwise operations 等简单 primitive 构成，适合近数据处理。",
            "量化 PIM core 和 PIM accelerator 的面积可行性与平均能耗/性能收益。",
        ],
        "method": "作者先用硬件性能计数器和能耗模型定位主要数据移动函数，再为每类工作负载设计 PIM offloading 方案。PIM core 是 64-bit 低功耗 embedded core；PIM accelerator 是针对具体 PIM target 的固定功能逻辑，假设集成于 3D-stacked memory logic layer。",
        "experiments": "平台基于 Chromebook/consumer-device energy model，工作负载覆盖 Chrome 页面滚动与加载、TensorFlow Mobile 的 VGG-19/ResNet/Inception-ResNet/Residual-GRU、VP9 playback/capture；结果按 CPU-only、CPU+PIM core、CPU+PIM accelerator，以及 VP9 专用硬件/压缩对比。",
        "results": [
            ("跨所有应用，平均 62.7% 系统能耗花在主存与计算单元之间的数据移动。", "Page 1, Introduction, Paragraph 4"),
            ("PIM core 平均降低 49.1% 能耗、提升 44.6% 性能；PIM accelerator 平均降低 55.4% 能耗、提升 54.2% 性能。", "Page 2, Introduction contributions/results"),
            ("PIM core 与 PIM accelerator 面积分别不超过每个 vault 可用 PIM logic 面积的 9.4% 与 35.4%。", "Page 2, Section 3.3"),
            ("Google Docs 页面滚动中，数据移动占 77% 能耗；texture tiling/color blitting 是重要瓶颈。", "Page 4, Figures 1-3"),
            ("VP9 decoder/encoder 的硬件实现里数据移动仍分别占 69.2%/71.5% 能耗，说明即使有专用硬件也可能受数据移动限制。", "Page 15, Figure 21"),
        ],
        "conclusion": "作者认为消费设备中最值得优先攻击的不是单纯算力不足，而是数据移动；对简单、数据密集、可近存实现的函数，PIM 可以在面积可接受的前提下带来显著能效与性能收益。",
        "limitations_author": [
            ("PIM accelerator 更高效但每个 target 需要专用逻辑，面积和设计复杂度高于 PIM core。", "Page 2, Section 1; Page 3, Section 3.3"),
            ("分析基于模型和估算，实际产品集成还受热、成本、内存接口、软件栈迁移影响。", "Page 3, Section 3.1 and Section 3.3"),
        ],
        "limitations_infer": [
            ("工作负载来自 Google 生态，结论对其他厂商应用或新型移动 SoC 需要重新验证。", "推断，基于 Page 1-3 workload scope"),
            ("PIM offload 的编程模型、调度开销和一致性问题不是本文主要展开对象。", "推断，基于 Section 3 target-level evaluation"),
        ],
        "focus": "建议重点读 Page 1-3 的 workload/PIM target 定义、Page 4-9 的各工作负载数据移动拆解、Page 10-15 的 PIM 评估图。",
        "relation": "与 Tesseract、SISA、NERO、NATSA 等 PIM/near-data work 构成互补：本文不是提出单一 PIM 架构，而是用工业消费端 workloads 论证数据移动瓶颈和 PIM 机会。",
        "figures": [
            ("Figure 1", "Page 4", "Chrome scrolling energy breakdown", "说明页面滚动能耗集中在 texture tiling/color blitting 等数据密集函数。"),
            ("Figure 2", "Page 4", "Google Docs scrolling data movement", "显示数据移动占 Google Docs 滚动总能耗 77%。"),
            ("Figure 3", "Page 4", "CPU vs PIM texture tiling", "展示 texture tiling 如何从 CPU 数据搬移流程变成近存执行。"),
            ("Figure 18", "Page 12", "Browser PIM evaluation", "比较浏览器场景中 PIM core/accelerator 的能耗和性能收益。"),
            ("Figure 19", "Page 13", "TensorFlow PIM evaluation", "显示 packing/data organization offload 对移动端 ML 的收益。"),
            ("Figure 21", "Page 15", "VP9 hardware/PIM comparison", "说明专用视频硬件仍受数据移动限制，PIM 与压缩可互补。"),
        ],
        "tables": [],
        "equations": [],
        "terms": [
            ("Processing-in-Memory (PIM)", "存内/近存处理", "Page 1-2", "把部分计算放到 memory logic 附近，以减少主存到 CPU/GPU/accelerator 的数据搬移。", "是"),
            ("PIM target", "PIM 目标函数", "Page 2-3", "能耗占比较高、以数据移动为主、适合简单近存逻辑执行的函数或 primitive。", "是"),
            ("PIM core", "PIM 通用核心", "Page 2, Section 3.3", "低功耗通用 embedded core，可服务多种 target。", "是"),
            ("PIM accelerator", "PIM 专用加速器", "Page 2, Section 3.3", "面向特定 target 的 fixed-function logic，通常收益更高但面积更大。", "是"),
            ("Texture tiling", "纹理分块", "Page 4, Section 4.2", "Chrome 渲染中把 bitmap 转成 tiled texture 的数据整理步骤。", "是"),
        ],
        "translation_sections": [
            ("Abstract / 摘要", "Page 1", "论文指出消费设备的电池与热约束使能效成为一等目标。作者分析 Chrome、TensorFlow Mobile、VP9 playback/capture 等 Google 工作负载，发现主存与计算单元之间的数据移动显著支配能耗和执行时间。将简单、数据密集的 primitive 放到 memory logic 附近执行，可以平均减少 55.4% 系统能耗并缩短 54.2% 执行时间。"),
            ("1. Introduction / 引言", "Page 1-2", "引言从消费设备增长、4K/VR/AR 等需求和电池/散热停滞切入，说明仅提升计算单元不够。核心观察是数据移动能耗远高于计算本身；在作者研究的应用中，平均 62.7% 能耗来自主存与计算单元之间的数据移动。因此，文章把问题转化为识别哪些函数既产生大量数据移动又能被便宜的 PIM logic 执行。"),
            ("2-3. Background and Methodology / 背景与方法", "Page 2-3", "作者介绍 3D-stacked memory 的 logic layer 为 PIM 提供实现空间，但消费设备无法承受复杂通用处理器式 PIM。方法上先用硬件计数器和能耗模型做 workload characterization，再以能耗占比、memory boundedness 和 PIM 执行可行性筛选 PIM target。"),
            ("4-7. Workload Analyses / 工作负载分析", "Page 4-9", "Chrome 部分显示 texture tiling、color blitting 等图形数据整理函数消耗大量数据移动能耗。TensorFlow Mobile 中 packing/data layout conversion 是重要目标。VP9 playback/capture 中，预测、变换、运动估计等数据密集阶段可受益于近存处理。"),
            ("8-10. Evaluation / 评估", "Page 10-15", "实验比较 CPU-only、PIM core 和 PIM accelerator。总体上，PIM accelerator 因定制化更强而收益更大；PIM core 更通用、面积更低。对 Chrome、TensorFlow 和 VP9，减少 off-chip/on-chip data movement 是主要收益来源。"),
            ("11. Conclusion / 结论", "Page 16", "作者总结说，在消费端应用里，数据移动已是系统级能耗与性能瓶颈。只要选取简单、数据密集且可在 memory logic 中实现的目标，PIM 就能在严格面积/功耗预算下提供显著收益。"),
        ],
        "sections": "Abstract; Introduction; Background; Workload Analysis; Chrome; TensorFlow Mobile; VP9 Playback/Capture; Evaluation; Related Work; Conclusion",
    },
    {
        "slug": "HARP-memory-error-profiling_micro21",
        "title": "HARP: Practically and Effectively Identifying Uncorrectable Errors in Memory Chips That Use On-Die Error-Correcting Codes",
        "zh_title": "HARP：在使用 On-Die ECC 的内存芯片中实用且有效地识别不可纠正错误",
        "authors": "Minesh Patel, Geraldo F. Oliveira, Onur Mutlu",
        "year": "2021",
        "venue": "MICRO 2021",
        "doi": "10.1145/3466752.3480061",
        "url": "https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/HARP-memory-error-profiling_micro21.pdf",
        "pages": "18",
        "dataset": "Simulation-based error profiling experiments; DRAM data-retention error case study",
        "topic": "Memory reliability; on-die ECC; error profiling; repair",
        "keywords": "HARP, on-die ECC, active profiling, reactive profiling, repair mechanism, DRAM reliability",
        "one": "HARP 通过把 on-die ECC 后的错误拆成 direct/indirect errors，并结合 active 与 reactive profiling，使内存控制器能更快覆盖需要修复的 at-risk bits。",
        "background": "现代 DRAM/新型内存常在芯片内部使用 on-die ECC 隐藏 raw errors，但系统级 repair mechanism 需要知道哪些 bit 有风险；on-die ECC 让错误在控制器外部呈现为被混淆后的模式，导致传统 profiling 变慢或不完整。",
        "questions": [
            "on-die ECC 会怎样改变内存控制器看到的错误分布？",
            "为什么传统 active/reactive profiling 在 on-die ECC 存在时难以覆盖所有 at-risk bits？",
            "能否在不暴露 ECC metadata 的情况下，实用地识别 direct 和 indirect errors？",
            "HARP 相比 Naive/BEEP 类 baseline 在 profiling rounds 与 repair 效果上提升多少？",
        ],
        "contribs": [
            "首次系统分析 on-die ECC 对 bit-granularity error profiling 的影响。",
            "归纳 on-die ECC 带来的三类挑战：at-risk bits 组合数指数增加、单个 at-risk bit 更难观察、常用 data pattern 被干扰。",
            "提出 Hybrid Active-Reactive Profiling (HARP)，将 direct errors 与 indirect errors 分别处理。",
            "给出 HARP-U 与 HARP-A 两个变体，区分是否知道 on-die ECC parity-check matrix。",
            "用仿真表明 HARP 更快达到 99th-percentile/full coverage，并在 repair case study 中降低 BER。"
        ],
        "method": "HARP 先通过 active profiling 和一个小的 on-die ECC read modification 读取 raw data values，从而识别 direct errors；再在 memory controller 中使用 correction capability 不低于 on-die ECC 的 secondary ECC，在运行中安全地识别由 miscorrection 产生的 indirect errors。",
        "experiments": "论文用仿真对比两个 state-of-the-art baseline profiling algorithms，改变每个 ECC word 中 raw bit errors 数量与错误概率，并用理想 bit-repair mechanism 做端到端 BER case study。",
        "results": [
            ("on-die ECC 让错误在不同 bit positions 之间产生统计依赖，并引出三类 profiling 难题。", "Page 1-2, Abstract and Introduction"),
            ("HARP 对 2/3/4/5 个 pre-correction errors 的场景，只需最佳 baseline 20.6%/36.4%/52.9%/62.1% 的 profiling rounds 即可达到 99th-percentile coverage。", "Page 1-2, Abstract/Contributions"),
            ("HARP 在 raw per-bit error probability 0.75 的 case study 中比最佳 baseline 快 3.7x 完成使 repair 可覆盖全部错误所需的信息。", "Page 1, Abstract; Page 16-17, Case Study"),
            ("HARP-A 知道 parity-check matrix 可预计算 indirect at-risk bits，但 direct-error coverage 与 HARP-U 相同。", "Page 2, Introduction; Section 6"),
        ],
        "conclusion": "HARP 的核心结论是：不应把 on-die ECC 当成透明可靠层；系统级 profiling/repair 必须显式建模它如何改写错误可见性，而 active+reactive 的混合方案可以实用地恢复 coverage。",
        "limitations_author": [
            ("HARP 假设 on-die ECC 使用 systematic encoding，并需要修改 read operation 以读取 raw data values。", "Page 2, Introduction; Section 5-6"),
            ("secondary ECC 的 correction capability 需要不低于 on-die ECC，增加控制器侧开销。", "Page 1-2, HARP overview"),
        ],
        "limitations_infer": [
            ("评估主要是仿真与模型化 case study，真实商用 DRAM 中 ECC 细节和接口可获得性可能受厂商限制。", "推断，基于 Page 1-2 evaluation description"),
            ("若未来 on-die ECC 更复杂或非 systematic，HARP 假设需要重新审视。", "推断，基于 Section 3-6 assumptions"),
        ],
        "focus": "建议重点读 Page 1-2 的问题定义与贡献、Page 5-7 的 on-die ECC 分析、Page 8-11 的 HARP 机制、Page 13-17 的覆盖率和 BER 评估。",
        "relation": "HARP 与 BEER/BEEP/understanding in-DRAM ECC 属于同一条 on-die ECC 可见性与可靠性研究线；BEER 关注恢复 ECC parity-check matrix，HARP 关注在 ECC 存在时如何做 profiling/repair。",
        "figures": [
            ("Figure 1", "Page 2", "repair mechanism + on-die ECC system", "说明 repair 位于控制器，on-die ECC 位于芯片内部，二者可见错误层次不同。"),
            ("Figure 2", "Page 4", "repair granularity wasted capacity", "说明高错误率下细粒度 repair 的容量效率。"),
            ("Figure 3", "Page 5", "on-die ECC operation", "展示 encode/decode/correction 如何改变控制器看到的错误。"),
            ("Figure 5", "Page 9", "HARP architecture", "概括 active + reactive profiling 的系统结构。"),
            ("Figure 6", "Page 13", "direct error coverage", "展示 HARP 比 baseline 更快覆盖 direct at-risk bits。"),
            ("Figure 10", "Page 16", "BER before/after secondary ECC", "说明 HARP 与 secondary ECC/repair 的端到端可靠性效果。"),
        ],
        "tables": [
            ("Table 1", "Page 4", "memory repair mechanisms", "将不同 repair granularity 与代表机制对应起来。"),
            ("Table 2", "Page 6", "on-die ECC amplifies at-risk bits", "说明少数 raw at-risk bits 可扩展成大量 post-correction at-risk bits。"),
        ],
        "equations": [],
        "terms": [
            ("On-die ECC", "芯片内 ECC", "Page 1", "内存芯片内部执行的纠错码，控制器通常不可见其 metadata 和 correction 行为。", "是"),
            ("Direct error", "直接错误", "Page 1-2", "ECC word 数据部分 raw bit error 直接导致的 post-correction error。", "是"),
            ("Indirect error", "间接错误", "Page 1-2", "on-die ECC 在不可纠正错误上发生 miscorrection 后引入的错误。", "是"),
            ("Hybrid Active-Reactive Profiling (HARP)", "混合主动-反应式错误画像", "Page 1-2", "先主动识别 direct errors，再运行时安全发现 indirect errors 的 profiling 算法。", "是"),
            ("Parity-check matrix", "校验矩阵", "Page 2 and Section 3", "描述 ECC code 的矩阵；HARP-A 可用它预计算 indirect at-risk bits。", "是"),
        ],
        "translation_sections": [
            ("Abstract / 摘要", "Page 1", "论文指出内存密度提升加剧错误率，而 on-die ECC 虽能在芯片内部隐藏错误，却会混淆内存控制器对错误的观察，阻碍 bit-level repair 所需的 error profiling。HARP 把 ECC 后不可纠正错误分解为 direct errors 与 indirect errors，并用 hybrid active-reactive profiling 更快达到覆盖。"),
            ("1. Introduction / 引言", "Page 1-2", "作者解释 scaling-related errors、repair mechanism 与 on-die ECC 之间的矛盾：repair 需要知道哪些 bit 有风险，但 on-die ECC 会先修改错误表现形式。传统 profiling 要么只能观察 correction 后结果，要么需要大量测试轮次。"),
            ("2-4. Background and Analysis / 背景与分析", "Page 2-8", "论文回顾 repair granularity、active/reactive profiling、error model 与 on-die ECC，并形式化说明 ECC 如何使 bit errors 之间不再独立。关键结论是，控制器外部看到的 post-correction errors 并不直接对应 raw errors。"),
            ("5-6. HARP / 方法", "Page 8-12", "HARP 的 active phase 利用修改后的 read operation 读取 raw data values，尽快找出 direct at-risk bits；reactive phase 利用 memory-controller secondary ECC 在实际运行时检测和安全标记 indirect errors。HARP-U 不知道校验矩阵，HARP-A 知道并利用校验矩阵辅助 indirect 部分。"),
            ("7-8. Evaluation and Case Study / 评估", "Page 12-17", "实验显示 HARP 相比 baseline 更快达到高覆盖率，尤其在 pre-correction errors 数量增加时优势明显。BER case study 表明，更快且完整的 profiling 能让 repair mechanism 更早覆盖所有需要修复的错误。"),
            ("9. Conclusion / 结论", "Page 17-18", "作者总结 HARP 解决了 on-die ECC 给 profiling 带来的三个核心困难，说明未来内存可靠性机制不能忽略芯片内 ECC 对系统可见错误的改变。"),
        ],
        "sections": "Abstract; Introduction; Background; On-Die ECC Analysis; HARP; Evaluation; Case Study; Related Work; Conclusion",
    },
    {
        "slug": "LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18",
        "title": "The Locality Descriptor: A Holistic Cross-Layer Abstraction to Express Data Locality in GPUs",
        "zh_title": "Locality Descriptor：在 GPU 中表达数据局部性的整体跨层抽象",
        "authors": "Nandita Vijaykumar, Eiman Ebrahimi, Kevin Hsieh, Phillip B. Gibbons, Onur Mutlu",
        "year": "2018",
        "venue": "ISCA 2018",
        "doi": "未找到",
        "url": "https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18.pdf",
        "pages": "14",
        "dataset": "Rodinia, Parboil, PolybenchGPU benchmarks in GPGPU-Sim based simulation",
        "topic": "GPU locality; cross-layer abstraction; cache/NUMA optimization",
        "keywords": "Locality Descriptor, GPU, CTA scheduling, NUMA locality, cache management, prefetching",
        "one": "这篇文章提出 Locality Descriptor，让软件以可移植方式表达 GPU 数据局部性，并让硬件协调 CTA scheduling、cache policy、prefetching 和 NUMA placement 来利用这些语义。",
        "background": "GPU 编程模型擅长表达并行性，却缺少表达 reuse-based locality 与 NUMA locality 的统一接口；软件技巧不便移植，硬件-only 机制又缺少程序语义。",
        "questions": [
            "如何让程序员/编译器表达数据结构、线程组和访问模式之间的局部性关系？",
            "为什么单独 CTA scheduling 或单独 cache policy 不足以转化为性能收益？",
            "Locality Descriptor 需要包含哪些字段才能既可移植又足够驱动硬件优化？",
            "在 cache locality 与 NUMA locality 两类场景下，它相对硬件-only/first-touch 等基线提升多少？",
        ],
        "contribs": [
            "提出面向 GPU 的跨层 Locality Descriptor，明确描述 data structure、locality type、tile semantics、locality semantics 和 priority。",
            "把 locality types 抽象为 INTER-THREAD、INTRA-THREAD 和 NO-REUSE 等类别，并作为软件与硬件之间的契约。",
            "说明硬件可用该抽象协同 CTA scheduling、cache bypass/prioritization、prefetching、memory placement。",
            "在 reuse-based cache locality 与 NUMA locality 两条路径上验证性能收益。",
        ],
        "method": "软件通过 descriptor 标注某个数据结构的地址范围、tile 与 compute tile 对应关系、局部性类型和优先级；硬件运行时将这些语义送给 CTA scheduler、cache controller、prefetcher 和 memory placement mechanism，从而选择对应的策略。",
        "experiments": "作者在 GPGPU-Sim/NUMA GPU simulator 中评估 Rodinia、Parboil、PolybenchGPU 等 benchmark；单芯片系统用于 cache locality，四个 GPU module/NUMA zones 系统用于 NUMA locality。",
        "results": [
            ("Locality Descriptor 在 reuse-based cache hierarchy 场景平均提升 26.6%，最高 46.6%。", "Page 1-2, Abstract/Introduction; Section 6"),
            ("在 NUMA memory system 场景平均提升 53.7%，最高 2.8x。", "Page 1-2, Abstract/Introduction; Section 6"),
            ("单独 CTA scheduling 虽可把 working set 降低 54.5%，但平均性能只提升 3.3%，因为 L1 inflight hit rate 增加导致更多线程一起等待。", "Page 3, Figures 3-4"),
            ("NUMA locality 需要数据放置与 CTA scheduling 协同；简单 first-touch/page placement 对细粒度共享不稳。", "Page 3-4, Figure 5"),
        ],
        "conclusion": "GPU locality 优化需要软件语义与硬件机制共同参与；Locality Descriptor 的价值在于提供足够高层、可移植的语义接口，同时让硬件统一协调多种底层策略。",
        "limitations_author": [
            ("需要程序员或编译器生成 descriptor，局部性语义不准确会影响优化效果。", "Page 4-6, Section 3"),
            ("多个 descriptor 可能冲突，因此需要 priority 机制。", "Page 2 and Section 3"),
        ],
        "limitations_infer": [
            ("实验以模拟器为主，真实 GPU 产品中开放 CTA scheduler、cache policy 和 placement 接口的可行性需要进一步工程化。", "推断，基于 Section 6 methodology"),
            ("高度动态或输入相关的 irregular locality 可能难以静态描述。", "推断，基于 descriptor design assumptions"),
        ],
        "focus": "建议重点读 Page 1-4 的动机案例、Page 5-7 的 descriptor 字段定义、Page 10-13 的性能/NUMA 评估。",
        "relation": "这篇与 X-MEM、MetaSys 同属 cross-layer semantic interface 方向；区别是它专注 GPU locality，X-MEM/MetaSys 更通用地管理 metadata。",
        "figures": [
            ("Figure 1", "Page 2", "histo inter-CTA locality", "用 histo 展示 CTAs 与 data tiles 的共享关系。"),
            ("Figure 2", "Page 2", "Locality Descriptor specification", "给出 descriptor 的调用形式和基本字段。"),
            ("Figure 3", "Page 3", "CTA scheduling working set/speedup", "说明仅暴露 locality 不等于性能提升。"),
            ("Figure 6", "Page 5", "abstraction overview", "展示软件语义到硬件优化的整体路径。"),
            ("Figure 14", "Page 11", "reuse-based locality performance", "展示 cache locality 场景 26.6% 平均性能提升。"),
            ("Figure 17", "Page 12", "NUMA locality performance", "展示 NUMA 场景 53.7% 平均提升。"),
        ],
        "tables": [
            ("Table 1", "Page 10", "simulation configuration", "列出单芯片与 NUMA GPU 模拟系统参数。"),
        ],
        "equations": [],
        "terms": [
            ("Locality Descriptor", "局部性描述符", "Page 1-2", "软件表达数据结构局部性、tile 关系和优化意图的跨层抽象。", "是"),
            ("CTA scheduling", "CTA 调度", "Page 2-3", "把共享数据的 Cooperative Thread Arrays 调度到相同/相近资源上以提高局部性。", "是"),
            ("Reuse-based locality", "基于复用的局部性", "Page 1", "为了提高 cache 利用率而关注数据复用关系。", "是"),
            ("NUMA locality", "NUMA 局部性", "Page 1", "把数据放到使用它的线程附近，减少远端访问。", "是"),
            ("INTRA-THREAD / INTER-THREAD / NO-REUSE", "线程内/线程间/无复用局部性类型", "Page 5-6", "descriptor 中驱动底层优化选择的 locality type。", "是"),
        ],
        "translation_sections": [
            ("Abstract / 摘要", "Page 1", "论文指出 GPU 需要有效利用 cache hierarchy 和未来 NUMA memory hierarchy，但现有 CUDA/OpenCL 主要表达并行性而非数据局部性。Locality Descriptor 让软件表达局部性，硬件据此协调调度、cache 管理和数据放置，带来 cache locality 平均 26.6% 与 NUMA locality 平均 53.7% 的性能提升。"),
            ("1-2. Motivation / 动机", "Page 1-4", "作者用 histo 说明 CTAs 之间共享数据，但硬件难以从地址流自动推断这些语义。单独 CTA scheduling 能减少 working set，却因为 inflight hit 增加而未必提升性能；NUMA 下仅靠 first-touch 也难处理细粒度共享。"),
            ("3. Locality Descriptor / 方法", "Page 4-8", "descriptor 描述数据结构、地址范围、locality type、tile semantics、locality semantics 和 priority。它把程序员/编译器知道的高层语义传给架构，让不同硬件模块以统一接口消费这些信息。"),
            ("4-5. Hardware Support / 硬件支持", "Page 8-10", "硬件侧根据 descriptor 调整 CTA scheduler、cache bypass/prioritization、prefetcher 和 memory placement。关键点不是发明单个策略，而是让多个策略以相同语义协同。"),
            ("6. Evaluation / 评估", "Page 10-13", "实验在多组 GPU benchmark 上显示 descriptor 能把 program semantics 转化为性能。cache locality 场景平均提升 26.6%；NUMA locality 场景平均提升 53.7%，并改善本地访问比例和 zone distribution。"),
            ("7-8. Discussion and Conclusion / 讨论与结论", "Page 13-14", "作者强调 Locality Descriptor 是一种可移植的跨层抽象，可随硬件代际演进映射到不同底层机制。它把 GPU locality 优化从零散技巧变成显式语义接口。"),
        ],
        "sections": "Abstract; Introduction; Case Studies; Locality Descriptor; Architectural Optimizations; Evaluation; Related Work; Conclusion",
    },
    {
        "slug": "MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17",
        "title": "Detecting and Mitigating Data-Dependent DRAM Failures by Exploiting Current Memory Content",
        "zh_title": "利用当前内存内容检测并缓解数据相关 DRAM 失效",
        "authors": "Samira Khan, Chris Wilkerson, Zhe Wang, Alaa R. Alameldeen, Donghyuk Lee, Onur Mutlu",
        "year": "2017",
        "venue": "MICRO 2017",
        "doi": "10.1145/3123939.3123945",
        "url": "https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17.pdf",
        "pages": "14",
        "dataset": "SPEC, STREAM, server benchmarks; DRAM failure/content modeling",
        "topic": "DRAM reliability; data-dependent failures; refresh optimization",
        "keywords": "MEMCON, data-dependent DRAM failures, refresh, PRIL, Pareto write intervals, reliability",
        "one": "MEMCON 不试图离线穷举所有 data-dependent DRAM failures，而是在程序运行时只针对当前内存内容检测失效，并用长写间隔预测来摊销测试成本、减少刷新。",
        "background": "数据相关失效依赖邻近 cell 内容，完整检测通常需要厂商私有的 DRAM 内部结构；系统级机制若不知道物理邻接关系，很难穷举所有可能内容组合。",
        "questions": [
            "系统不知道 DRAM 内部组织时，能否仍在线检测有实际风险的 data-dependent failures？",
            "只检测当前 memory content 是否足以支持降低大多数行的 refresh rate？",
            "runtime testing 什么时候值得做，什么时候成本超过收益？",
            "write intervals 的分布是否能预测测试后内容保持时间？",
        ],
        "contribs": [
            "提出 memory content-based detection/mitigation，把目标从所有可能内容转为当前正在使用的内容。",
            "证明程序实际内容触发的失效数比所有可能内容少 2.4x-35.2x。",
            "提出 cost-benefit model 和 MinWriteInterval，用于决定测试是否能被后续低刷新状态摊销。",
            "发现真实 workload write intervals 近似 Pareto 分布，并提出 PRIL predictor 预测长写间隔。",
            "展示相对 aggressive refresh 可减少约 65%-74% refresh operations 并提升性能。"
        ],
        "method": "当写入改变一行内容后，MEMCON 判断该页/行未来是否可能保持足够久；若 PRIL 预测写间隔超过 MinWriteInterval，就执行 Read-and-Compare 或 Copy-and-Compare 测试。测试未发现失效的行进入低刷新状态，发现失效的行保持高刷新或被其他机制保护。",
        "experiments": "论文结合 DRAM failure/content 分析、测试成本模型，以及 SPEC/STREAM/server workloads 的 write interval 分布与系统性能模拟，比较 aggressive 16ms refresh 与 MEMCON selective testing。",
        "results": [
            ("程序数据内容产生的 failures 比所有可能内容少 2.4x-35.2x。", "Page 2-4, Figure 4"),
            ("Read-and-Compare 与 Copy-and-Compare 的 MinWriteInterval 约为 560ms/864ms。", "Page 5, Figure 6"),
            ("真实应用 write intervals 服从 Pareto-like 分布；平均 81.5% 的总写间隔时间来自超过 1024ms 的长间隔。", "Page 2 and Section 4"),
            ("MEMCON 相比 aggressive refresh 减少 64.7%-74.5% refresh operations。", "Page 2, Introduction; Evaluation"),
            ("在 8/16/32Gb DRAM 下，单核和 4 核系统均获得显著性能提升，且 testing 的额外读写干扰较小。", "Page 1-2 and Evaluation"),
        ],
        "conclusion": "MEMCON 的思想是把可靠性检测与当前内容绑定：只要内容长期不变，就可用一次测试换来较长时间低刷新，从而绕开对 DRAM 内部邻接结构的依赖。",
        "limitations_author": [
            ("MEMCON 明确不检测所有可能的 data-dependent failures，只检测当前内容会触发的失效。", "Page 1, Abstract"),
            ("runtime testing 有额外读写和 latency 成本，需要写间隔足够长才有收益。", "Page 4-5, Section 3.2-3.3"),
        ],
        "limitations_infer": [
            ("若 workload 写入频繁或内容 churn 高，PRIL 难以找到足够多长间隔，收益会下降。", "推断，基于 MinWriteInterval and Pareto predictor"),
            ("低刷新安全性依赖测试覆盖当前内容下的失效；极低概率、温度变化或 aging 影响需要额外保护。", "推断，基于 runtime testing model"),
        ],
        "focus": "建议重点读 Page 1-2 的问题重构、Page 4-6 的 cost-benefit/MinWriteInterval、Page 7-10 的 PRIL 与 write interval 分布、Page 11-13 的 refresh/performance 结果。",
        "relation": "MEMCON 与 RAIDR/REAPER/Avatar 都关注刷新与可靠性开销；区别是 MEMCON 针对 data-dependent failures 并利用当前内容和写间隔，而不是单纯 retention time binning。",
        "figures": [
            ("Figure 1", "Page 2", "DRAM organization", "说明 cell/row/bank 层次和系统无法直接知道的内部结构。"),
            ("Figure 2", "Page 3", "address scrambling/column remapping", "解释系统地址与物理邻接关系不透明为何阻碍 exhaustive testing。"),
            ("Figure 3", "Page 3", "cells failing with different data content", "展示不同内容模式触发不同失效。"),
            ("Figure 4", "Page 4", "rows failing under program content", "量化实际程序内容触发的失效远少于所有可能内容。"),
            ("Figure 5", "Page 5", "testing frequency vs cost", "说明频繁测试、少测试和选择性测试的成本权衡。"),
            ("Figure 6", "Page 5", "MinWriteInterval", "推导测试成本需要多长低刷新时间摊销。"),
        ],
        "tables": [],
        "equations": [],
        "terms": [
            ("Data-dependent failure", "数据相关失效", "Page 1", "DRAM cell 是否失效依赖邻近 cell 中存储的数据内容。", "是"),
            ("MEMCON", "基于内存内容的检测/缓解机制", "Page 1", "运行时只测试当前内容触发的失效，并据此调节 refresh。", "是"),
            ("MinWriteInterval", "最小写间隔", "Page 2 and Section 3.3", "测试成本能被后续低刷新收益摊销所需的最短内容保持时间。", "是"),
            ("PRIL", "概率式剩余间隔长度预测器", "Page 2 and Section 4", "利用 Pareto 分布性质预测页面写后还会保持多久。", "是"),
            ("Aggressive refresh", "激进刷新", "Page 1", "用更短刷新间隔保护所有行，可靠但性能/能耗成本高。", "是"),
        ],
        "translation_sections": [
            ("Abstract / 摘要", "Page 1", "论文研究 data-dependent DRAM failures。由于完整检测所有内容组合需要了解每颗芯片的内部结构，MEMCON 改为在线检测当前内存内容会触发的失效，并在测试后用更低刷新率保护未失败的行。"),
            ("1-2. Background and Motivation / 背景与动机", "Page 1-4", "作者解释 DRAM scaling 加剧 cell-to-cell interference，而地址 scrambling、column remapping 等厂商内部设计使系统很难知道哪些 cell 互为邻居。实验动机表明，程序实际内容触发的失效少于所有可能内容，因此可以只围绕当前内容做检测。"),
            ("3. MEMCON Design / 方法", "Page 4-6", "MEMCON 在写入后根据预测决定是否测试。测试有 Read-and-Compare 与 Copy-and-Compare 两种模式；若测试通过，行进入低刷新状态；若失败或不测试，则继续高刷新或采用其他缓解。MinWriteInterval 用来判定测试成本能否被摊销。"),
            ("4. PRIL Predictor / 写间隔预测", "Page 6-8", "PRIL 基于 Pareto 分布的性质：一个页面在写后已经保持越久，未来继续保持的期望也越长。作者用这个性质识别值得测试的长写间隔。"),
            ("5-6. Evaluation / 评估", "Page 8-13", "实验显示真实应用中长写间隔占据大部分时间，MEMCON 可减少约 64.7%-74.5% refresh operations。相对 aggressive refresh，它在 8/16/32Gb DRAM 下带来明显性能提升，同时 testing 产生的额外读写干扰较小。"),
            ("7. Conclusion / 结论", "Page 13-14", "作者总结 MEMCON 通过利用当前内容，提供了一条不依赖 DRAM 内部组织的系统级检测/缓解路线，尤其适合以刷新开销换可靠性的未来高密度 DRAM。"),
        ],
        "sections": "Abstract; Introduction; Background and Motivation; MEMCON Design; PRIL; Evaluation; Related Work; Conclusion",
    },
    {
        "slug": "MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv",
        "title": "MetaSys: A Practical Open-Source Metadata Management System to Implement and Evaluate Cross-Layer Optimizations",
        "zh_title": "MetaSys：用于实现和评估跨层优化的实用开源元数据管理系统",
        "authors": "Nandita Vijaykumar, Ataberk Olgun, Konstantinos Kanellopoulos, Hasan Hassan, Mehrshad Lotfi, Phillip B. Gibbons, Onur Mutlu",
        "year": "2022",
        "venue": "ACM TACO / arXiv",
        "doi": "未找到",
        "url": "https://github.com/Yuntong-Hou/computer-architecture/blob/main/LEC3/MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv.pdf",
        "pages": "17",
        "dataset": "24 applications and 4 microbenchmarks; RISC-V Rocket Chip FPGA prototype",
        "topic": "cross-layer optimization; metadata management; RISC-V FPGA infrastructure",
        "keywords": "MetaSys, metadata, RISC-V, tagged memory, cross-layer optimization, FPGA, hardware-software interface",
        "one": "MetaSys 提供开源 RISC-V/FPGA 元数据管理基础设施，让研究者用少量 Chisel 代码实现和评估预取、边界检查、返回地址保护等跨层优化。",
        "background": "许多硬件-软件协同优化需要把程序语义传给硬件，但真实硬件评估通常要求 ISA、OS、硬件和应用全栈修改；已有基础设施缺少通用、低开销、支持多组件查询的元数据管理系统。",
        "questions": [
            "能否建立一个通用元数据系统，支持性能、安全和保护类跨层技术？",
            "元数据接口、tagged memory、OS support 和硬件 lookup 会带来多少面积/性能/内存开销？",
            "多个优化同时共享元数据系统是否会互相拖慢？",
            "元数据访问的 locality、TLB miss 和 cache 行为如何影响系统效率？",
        ],
        "contribs": [
            "发布第一个开源 FPGA-based full-system metadata management infrastructure，用 RISC-V Rocket Chip 原型实现。",
            "提供新 RISC-V instructions 和 software library，支持 CREATE、MAP、UNMAP 等动态元数据通信。",
            "使用 tagged memory，把每个地址关联到 tag ID，再由 tag ID 指向 private metadata tables。",
            "用三个 use cases 展示易用性：graph analytics prefetching、bounds checking、return address protection。",
            "系统量化通用 metadata system 的面积、内存、性能开销及瓶颈来源。"
        ],
        "method": "MetaSys 包含三部分：新 RISC-V ISA/software library 作为 hardware-software interface；OS 与硬件维护 Metadata Mapping Table (MMT)、Metadata Mapping Cache (MMC) 和 Private Metadata Tables (PMTs)；模块化 optimization client 让 prefetcher、bounds checker 等组件查询 metadata。",
        "experiments": "作者在 RISC-V Rocket Chip FPGA prototype/仿真环境中实现 3 个 use cases，并用 24 个应用与 4 个 microbenchmarks 测通用 metadata management overhead、并发查询、多技术共存、metadata locality 和 TLB 行为。",
        "results": [
            ("MetaSys 面积开销仅 0.02%（含 17KB SRAM），DRAM metadata memory overhead 为 0.2%，新增 8 条 RISC-V instructions。", "Page 2, Introduction; Section 3"),
            ("通用 metadata system 平均性能开销 2.7%，最重 microbenchmark 最高 27%。", "Page 2, Introduction; Characterization"),
            ("三个 use cases 的额外开销分别约为 0.2% prefetching、14% bounds checking、1.2% return address protection。", "Page 2, Introduction"),
            ("metadata spatial/temporal locality 是性能开销关键；metadata address translation 导致的 TLB misses 是重要瓶颈。", "Page 2, Characterization conclusions"),
            ("每个 use case 在 MetaSys 上只需约 100 行 Chisel 代码。", "Page 1-2, Abstract/Introduction"),
        ],
        "conclusion": "MetaSys 的核心结论是：一个共享、低开销、开源的 metadata substrate 可以显著降低跨层优化的硬件原型实现门槛，并且在多数情况下性能开销可控。",
        "limitations_author": [
            ("metadata locality 差时开销明显上升，最坏 microbenchmark 可达 27%。", "Page 2, Characterization summary"),
            ("security/protection 用例可能需要 Force stall 等保守模式，开销高于性能 hint 类用例。", "Page 4-6, MetaSys modes/use cases"),
        ],
        "limitations_infer": [
            ("基于 RISC-V Rocket Chip 的研究原型，迁移到复杂 OoO server CPU 需要额外工程验证。", "推断，基于 prototype scope"),
            ("新增 ISA 与 OS 支持意味着软件生态迁移成本不可忽略。", "推断，基于 Section 3 interface design"),
        ],
        "focus": "建议重点读 Page 1-2 的系统目标与定量开销、Page 4-7 的 MMT/MMC/PMT 和 ISA 接口、Page 10-15 的 characterization 与 use cases。",
        "relation": "MetaSys 与 Locality Descriptor/X-MEM 同属跨层语义传递方向；Locality Descriptor 聚焦 GPU locality 抽象，MetaSys 更像 CPU 侧可运行的通用 metadata substrate。",
        "figures": [
            ("Figure 1", "Page 4", "MetaSys hardware components and operation", "展示 MMT、MMC、PMT、optimization client 之间的数据路径。"),
            ("Use-case figures", "Sections 5-6", "prefetching/bounds/return-address protection implementations", "说明同一 metadata substrate 如何服务不同目标。"),
            ("Characterization figures", "Evaluation section", "metadata overhead/locality/TLB effects", "展示性能瓶颈主要来自 metadata locality 与 translation。"),
        ],
        "tables": [
            ("Table 1", "Page 4", "MetaSys instructions", "列出 CREATE、MAP、UNMAP 等新 RISC-V 指令及参数。"),
            ("Table 2", "Page 5", "software library calls", "展示应用可调用的库接口。"),
        ],
        "equations": [],
        "terms": [
            ("Metadata", "元数据", "Page 1", "软件传给硬件的额外语义信息，如访问模式、bounds、reuse 等。", "是"),
            ("Tagged memory", "带标签内存", "Page 1 and Section 3", "每个地址关联 tag ID，再由 ID 指向对应 metadata。", "是"),
            ("Metadata Mapping Table (MMT)", "元数据映射表", "Page 4", "保存地址范围到 tag ID 的映射，通常在内存中由 OS 管理。", "是"),
            ("Metadata Mapping Cache (MMC)", "元数据映射缓存", "Page 4", "缓存常用 MMT 映射，减少 metadata lookup 开销。", "是"),
            ("Private Metadata Table (PMT)", "私有元数据表", "Page 4", "靠近具体 optimization component 存储该模块需要的 metadata。", "是"),
        ],
        "translation_sections": [
            ("Abstract / 摘要", "Page 1", "MetaSys 是一个开源 FPGA-based RISC-V 原型基础设施，用于快速实现和评估跨层优化。它提供通用 hardware-software interface 与轻量 metadata management，并用 graph prefetching、bounds checking 和 return address protection 展示可用性。"),
            ("1. Introduction / 引言", "Page 1-2", "作者指出跨层技术需要软件语义、硬件支持、OS 和 ISA 同时改变，真实硬件实现成本高。MetaSys 的目标是把这些共同部分抽象成 metadata substrate，使研究者可更快实现不同优化。"),
            ("3. MetaSys Design / 系统设计", "Page 3-7", "MetaSys 新增 RISC-V instructions 和软件库来创建、映射、取消映射 metadata；采用 tagged memory，把地址映射到 tag ID；OS 管理 MMT，硬件 MMC 缓存常用映射，optimization clients 从 PMT 读取模块私有 metadata。"),
            ("4-6. Use Cases / 用例", "Page 7-11", "三个用例分别展示 performance hint、安全检查和控制流保护：graph analytics prefetcher 使用访问模式元数据；bounds checking 使用 base/bounds；return address protection 保护 stack frame 中返回地址。"),
            ("7. Characterization / 表征评估", "Page 11-15", "作者量化面积、内存和性能开销，发现平均 overhead 低，但 metadata locality 和 TLB miss 会显著影响最坏情况。多个技术共享系统时没有明显额外性能损失，说明单一 substrate 可扩展。"),
            ("8. Conclusion / 结论", "Page 16-17", "论文总结 MetaSys 可以作为跨层优化研究的可复用开源平台，以较低硬件/内存开销支持多种 technique 的真实系统评估。"),
        ],
        "sections": "Abstract; Introduction; Background; MetaSys Design; Use Cases; Characterization; Related Work; Conclusion",
        "code": "https://github.com/CMU-SAFARI/MetaSys",
    },
]


def md_list(items):
    return "\n".join(f"- {item}" for item in items)


def md_loc_list(items):
    return "\n".join(f"- {text}（{loc}）" for text, loc in items)


def render_key_points(p):
    rows = []
    base_points = [
        ("作者想解决的问题", p["background"], "Page 1, Abstract/Introduction", "论文开头明确把研究目标放在该瓶颈或可靠性挑战上。", "高", "这是理解全文动机的入口。"),
        ("核心问题", "；".join(p["questions"][:2]), "Page 1-2, Introduction", "研究问题在 introduction 中被拆解成可评估问题。", "高", "先抓问题，再读方法细节。"),
        ("核心方法", p["method"], "Method/design sections", "作者在方法章节给出机制或抽象设计。", "高", "这是本文与相关工作的主要差异。"),
    ]
    for text, loc in p["results"][:4]:
        base_points.append(("关键结果", text, loc, "定量结果来自论文实验或摘要贡献段。", "高", "这些数字支撑作者主要结论。"))
    base_points.append(("局限", p["limitations_author"][0][0], p["limitations_author"][0][1], "作者在机制边界或设计假设中直接体现。", "中", "复现或迁移时需要优先检查。"))
    base_points.append(("需要追问", p["limitations_infer"][0][0], p["limitations_infer"][0][1], "该点为基于实验范围的推断。", "中", "不是论文确定结论，但适合后续阅读。"))
    for i, row in enumerate(base_points, 1):
        kind, content, loc, evidence, importance, understanding = row
        rows.append(f"| {i} | {kind}：{content} | {loc} | {evidence} | {importance} | {understanding} |")
    return "\n".join(rows)


def render_translation(p):
    parts = []
    for heading, loc, text in p["translation_sections"]:
        parts.append(f"## {heading}\n\n### 原文位置\n{loc}\n\n### 中文翻译\n{text}\n\n---")
    return "\n\n".join(parts)


def render_figures(items):
    if not items:
        return "| 未检测到编号图 | - | - | 本轮未发现需要单列的编号图。 | - | - |"
    return "\n".join(f"| {num} | {loc} | {theme} | {meaning} | 支撑论文关键论证 | 建议回到 PDF 查看图中轴/图例 |" for num, loc, theme, meaning in items)


def render_tables(items):
    if not items:
        return "| 未检测到核心表 | - | - | 本轮未发现需要单列的核心表。 | - | - |"
    return "\n".join(f"| {num} | {loc} | {theme} | {meaning} | 支撑方法或实验设置 | 建议回到 PDF 查看细项 |" for num, loc, theme, meaning in items)


def render_equations(items):
    if not items:
        return "| 未检测到核心编号公式 | - | - | 本轮阅读未发现必须掌握的核心编号公式。 | - | 否 |"
    return "\n".join(f"| {num} | {loc} | {role} | {symbols} | {intuition} | {master} |" for num, loc, role, symbols, intuition, master in items)


for p in PAPERS:
    slug = p["slug"]
    code = p.get("code", "未找到")
    pdf_source = f"paper reading/sources/LEC3/{slug}.pdf"
    extracted = f"paper reading/extracted_text/{slug}.txt"

    write(f"papers/{slug}/metadata.md", f"""
# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh_title']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: {p['doi']}
- arXiv ID: 未找到
- URL: {p['url']}
- PDF Source: {pdf_source}
- Code / Project Page: {code}
- Dataset: {p['dataset']}
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: {STATUS}
- Full Text Available: Yes
- Notes: {COPYRIGHT_NOTE}
""")

    write(f"papers/{slug}/reading_summary.zh.md", f"""
# 中文阅读摘要

## 1. 一句话总结
{p['one']}

## 2. 研究背景
{p['background']}

## 3. 核心问题
{md_list(p['questions'])}

## 4. 核心贡献
{md_list(p['contribs'])}

## 5. 方法概述
{p['method']}

## 6. 实验设计
{p['experiments']}

## 7. 主要结果
{md_loc_list(p['results'])}

## 8. 关键结论
{p['conclusion']}

## 9. 局限性
作者明确或设计中直接体现的局限：
{md_loc_list(p['limitations_author'])}

我基于论文范围推断的潜在问题：
{md_loc_list(p['limitations_infer'])}

## 10. 适合我重点关注的内容
{p['focus']}

## 11. 和其他文献的关系
{p['relation']}
""")

    write(f"papers/{slug}/key_points_with_locations.zh.md", f"""
# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
{render_key_points(p)}
""")

    write(f"papers/{slug}/full_translation.zh.md", f"""
# Full Chinese Translation

## Title
原文标题：{p['title']}

中文标题：{p['zh_title']}

> {COPYRIGHT_NOTE}

{render_translation(p)}
""")

    write(f"papers/{slug}/figures_tables_equations_notes.zh.md", f"""
# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_figures(p['figures'])}

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
{render_tables(p['tables'])}

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
{render_equations(p['equations'])}
""")

    term_rows = "\n".join(f"| {en} | {zh} | {loc} | {explain} | {core} |" for en, zh, loc, explain, core in p["terms"])
    write(f"papers/{slug}/terminology.zh.md", f"""
# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
{term_rows}
""")

    write(f"papers/{slug}/limitations_and_questions.zh.md", f"""
# Limitations and Questions

## 1. 作者明确承认的局限
{md_loc_list(p['limitations_author'])}

## 2. 论文中隐含的局限
{md_loc_list(p['limitations_infer'])}

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
{md_list(p['questions'])}

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。
""")

    checklist = [
        "我能说清楚这篇文章解决的问题",
        "我能解释作者的方法或系统设计",
        "我能指出核心创新与已有工作的差异",
        "我能找到支撑主要结论的图、表或实验位置",
        "我能复述最重要的定量结果",
        "我知道这篇文章的局限和适用边界",
        "我知道这篇文章和 LEC3 其他 memory/PIM/reliability 论文的关系",
        "我知道哪些结论有原文位置支持",
        "我知道哪些问题还需要继续查证",
    ]
    write(f"papers/{slug}/reading_checklist.md", "# Reading Checklist\n\n" + "\n".join(f"- [ ] {x}" for x in checklist))

    write(f"papers/{slug}/extraction_log.md", f"""
# Extraction Log

- Input Type: GitHub repository PDF
- Source: {p['url']}
- Access Status: 成功下载并读取本地 PDF
- Full Text Retrieved: Yes
- PDF Pages: {p['pages']}
- Sections Detected: {p['sections']}
- Figures Detected: Yes
- Tables Detected: {'Yes' if p['tables'] else 'No core tables detected in this round'}
- Equations Detected: {'Yes' if p['equations'] else 'No core numbered equations detected in this round'}
- Appendix Detected: 未发现独立 appendix 或本轮未作为重点处理
- Supplementary Material Detected: 未发现
- OCR Used: No
- Extracted Text File: {extracted}
- Missing Content: 图中细小标注和复杂版式建议回到 PDF 人工核对
- Parsing Problems: PDF 双栏文本存在局部换行错位；已按页码、章节和图表编号定位关键结论
- Uncertain Parts: DOI/arXiv/代码页如 metadata 标注“未找到”则表示未在 PDF 抽取文本中确认
- Need User Action: 无；如需逐字全文翻译，请确认版权授权范围后再处理
- Quality Check: 已覆盖摘要、引言、方法、实验、主要结果、局限、图表/公式、术语与复习 checklist
- Batch Status: {STATUS}
""")

print(f"updated {len(PAPERS)} papers for batch 4")
