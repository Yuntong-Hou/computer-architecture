# Full Chinese Translation

## Title

原文标题：FPGA-Based Near-Memory Acceleration of Modern Data-Intensive Applications

中文标题：基于 FPGA 的现代数据密集型应用近内存加速

原文位置：Page 1

处理说明：本文件按“完整度优先 + 硬件工程师视角”重写。它不是只翻译摘要，而是按原文结构覆盖摘要、动机、应用分析、加速器实现、实验评估、资源/能效讨论和结论。参考文献列表保留英文，不逐条翻译。

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

现代数据密集型应用既需要高计算能力，又受到严格功耗约束。当前计算系统中，计算单元与内存单元之间昂贵的数据移动浪费了大量执行周期和能量，因此这类应用受到明显限制。基因组分析（genome analysis）和天气预测（weather prediction）是两个典型例子。

近年来，FPGA 将可重构逻辑（reconfigurable fabric）与高带宽内存（High-Bandwidth Memory, HBM）集成在一起，使数据移动更高效，并提升整体性能和能效。这种趋势代表了向近内存计算（near-memory computing）的范式转移。本文利用带 HBM 的 FPGA 改进基因组分析中的 pre-alignment filtering 步骤，以及天气预测模型中的代表性 kernels。实验表明，与高端 IBM POWER9 系统和传统 DDR4 FPGA 板卡相比，HBM-FPGA 方案获得显著加速和节能。作者认为，基于 FPGA 的近内存计算有潜力缓解现代数据密集型应用中的数据移动瓶颈。

### 硬件工程师视角

摘要里的重点不是“FPGA 比 CPU 快”，而是“平台结构决定可实现的带宽和能效”。HBM、OCAPI/CAPI2、BRAM/URAM、PE 数量、通道映射、timing closure 共同决定结果。对硬件工程师来说，这篇文章是一个完整样例：如何把 workload 的访存瓶颈、FPGA 存储层次和真实平台约束连接起来。

---

## 1. Introduction / 引言

### 原文位置
Page 1-3 / Introduction

### 中文翻译

现代计算系统中，计算单元的性能和能效与内存单元之间存在巨大差距。系统通常采用以处理器为中心（processor-centric）的方式：数据必须通过相对较慢且耗能的 off-chip bus，在内存单元和计算单元之间来回移动。对于基因组分析、天气建模等数据密集型负载，这种 memory-CPU-memory 的持续数据搬移带来了极大的执行时间和能耗开销。

作者在 Page 1-2 使用 IBM POWER9 CPU 上的 roofline model（Figure 1）分析三个 kernel：SneakySnake pre-alignment filtering、COSMO weather model 中的 vertical advection (vadvc) 和 horizontal diffusion (hdiff)。图中显示，这些 workload 的 arithmetic intensity 很低，且访存模式复杂，CPU 的微架构特性难以充分发挥作用，实际性能明显低于峰值计算能力。

SneakySnake 的关键问题在于，它把 approximate string matching 转换为 single net routing，并构造一个 chip maze。为了保持速度，SneakySnake 只计算 chip maze 的部分区域，但这会导致对矩阵不同位置的不规则访问，使数据访问模式与内存布局不匹配，空间局部性和 cache effectiveness 都较差。

天气模型中的 vadvc 和 hdiff 是 compound stencil kernels，操作三维网格。它们需要在多个方向访问数据，并受 DRAM latency 与复杂访存模式影响。vadvc 使用 Thomas algorithm 求解垂直方向的 tridiagonal matrix，存在 forward sweep 和 backward sweep；hdiff 由 Laplacian stencil 和 flux stencil 组成，水平访问为主，但仍需要大量内存访问。

本文的目标是利用现代带 HBM 的 FPGA 近内存计算能力，缓解这两个真实应用中的 memory bottleneck。作者强调现代 FPGA 有四个趋势：第一，HBM 与 FPGA 封装集成，提供比传统 DDR4 FPGA 板卡高一个数量级的带宽；第二，URAM 与 BRAM 提供靠近逻辑的大容量片上存储；第三，CAPI、CCIX、CXL、OCAPI 等 cache-coherent interconnect 让 FPGA 能更紧密地访问 host memory；第四，7-14nm FinFET 工艺提高 FPGA 性能。

论文的主要结论是：HBM-based designs 对 SneakySnake、vadvc、hdiff 分别比 16-core IBM POWER9 快 27.4x、5.3x、12.7x，能效提升 133x、12x、35x。原文位置：Page 3。

### 硬件工程师视角

引言给出的工程判断很直接：如果 workload 的瓶颈在 off-chip data movement，而不是算术吞吐，那么仅增加 CPU core 或 vector width 可能收益有限。硬件方案要从数据路径入手：数据是否能放在 HBM pseudo-channel 附近，PE 是否能独占通道，片上 buffer 是否能承接访问重排，host-FPGA 互连是否成为新瓶颈。

这也提醒我们：近内存加速不是“把计算放到内存旁边”这么简单。真实系统需要看 host interface、coherency、data staging、kernel partition、HBM bank/channel mapping、FPGA SLR placement 和 timing closure。

---

## 2. Near-Memory Computation on FPGAs / FPGA 上的近内存计算

### 原文位置
Page 3 / Figure 2

### 中文翻译

Figure 2 给出系统结构。FPGA 连接两个 HBM2 stacks，每个 stack 有 16 个 pseudo memory channels，因此总共有 32 个 HBM channels。每个 channel 以 256-bit 接口暴露给 FPGA。HBM IP 每个 stack 提供 8 个 memory controllers，用于处理 HBM 通道的数据传输。这种结构能为近内存计算提供高带宽、低延迟访问。

FPGA 通过 OCAPI 连接 IBM POWER9 host processor。FPGA 上实现 accelerator functional unit (AFU)，AFU 通过 TLx (Transaction Layer) 和 DLx (Data Link Layer) 与 host 系统交互。AFU 包含多个 processing elements (PEs)，每个 PE 加速应用的一部分。PE 内部利用 FPGA 的 LUT、FF、URAM、BRAM，以及外部 HBM 形成异构存储层次。

### 硬件工程师视角

这里的系统图非常适合硬件评审：host-to-FPGA 是 1024-bit OCAPI cache line 语义，HBM channel 是 256-bit AXI-like 语义，中间必须有 stream converter / buffering / partitioning。设计中最容易出问题的是带宽宽度不匹配、跨 SLR 布线、HBM pseudo-channel 映射、host coherency overhead 和 PE 数据供给不均衡。

---

## 3. Modern Data-Intensive Applications / 现代数据密集型应用

### 原文位置
Page 3-5 / Case Study 1 and Case Study 2

### 中文翻译

### 3.1 Case Study 1: Pre-Alignment Filtering in Genome Analysis

基因组分析中的 sequence alignment 是核心步骤，通常要计算两个序列之间的 edit distance、edit 类型、edit 位置和 alignment score。传统动态规划算法时间和空间复杂度通常为二次级别，因此代价很高。

在实际 genome analysis pipeline 中，绝大多数待比较的 sequence pairs 都高度不相似，最终 alignment 结果会被丢弃。pre-alignment filtering 的思想是快速估计两个序列的差异，如果 edit distance 超过阈值 E，就避免执行昂贵的 DP-based alignment。

SneakySnake 是一种高并行、高准确度的 pre-alignment filter。它把 approximate string matching 转换为 VLSI 中的 single net routing 问题。目标是在 chip layout 边界的两个 terminal 之间找到穿过最少 obstacles 的最短 routing path。遇到 obstacle 后的后续 routing subproblem 与之前路径相对独立，因此可以并行求解多个 SNR subproblems。

SneakySnake 包括三个步骤。第一，构造 chip maze Z：矩阵条目表示 reference sequence 和 query sequence 字符之间的比较结果，0 表示可走路径，1 表示 obstacle。第二，在每一行寻找最长可用路径：从 checkpoint 开始数连续 0，遇到 obstacle 后比较各行的连续 0 长度，并选择最长路径。第三，用路径遇到的 obstacle 数估计 edit 数。如果 obstacle 数不超过阈值 E，则认为需要继续 alignment；否则过滤掉。

### 3.2 Case Study 2: Weather Modeling and Prediction

COSMO 是用于高分辨率天气预测的非静力大气模型。其 dynamical core 求解 curvilinear grid 上的 Euler equations，并在垂直方向使用 implicit discretization，在水平方向使用 explicit discretization。由此产生三类计算模式：horizontal stencils、vertical tridiagonal solvers 和 point-wise computation。

本文选择两个代表性 compound stencil kernels：vertical advection (vadvc) 和 horizontal diffusion (hdiff)。hdiff 在 3D grid 上执行 Laplacian 和 flux stencil，水平访问为主，在垂直方向没有依赖，因此可较充分并行。vadvc 使用 Thomas algorithm 沿垂直方向求解 tridiagonal matrix，包含 forward sweep 和 backward sweep，因此并行度更受限，控制流和数据访问更复杂。

### 硬件工程师视角

这两个 case study 代表两类常见硬件加速挑战。SneakySnake 是 irregular access + bit/logic-heavy + memory-bound；weather stencil 是 structured grid + streaming reuse + bandwidth/latency sensitive。硬件工程中不能用同一套 buffer 和 PE 策略套所有 kernel。SneakySnake 更依赖寄存器化 maze row 和数据搬移优化；hdiff 更依赖 stencil window reuse；vadvc 更依赖垂直方向依赖处理和控制流优化。

---

## 4. Accelerator Implementation / 加速器实现

### 原文位置
Page 5-7 / Figure 5

### 中文翻译

作者分别为 SneakySnake、vadvc 和 hdiff 在 HBM FPGA 板卡上实现加速器，并使用 Vivado HLS 设计流程。Figure 5 展示从 host DRAM 到 FPGA PE 的端到端数据流。

第一，输入数据位于 host DRAM 中，经 1024-bit OCAPI interface 传到 FPGA。data-fetch engine 读取 1024-bit POWER9 cache line，并写入 1024-bit buffer，再转换成 256-bit HBM pseudo-channel 宽度。对 weather prediction，输入是天气模拟的 atmospheric data；对 genome analysis，输入是 read/reference sequences。

第二，初始 buffering 后，HBM-write engine 将数据映射到 HBM memory。作者把数据划分到多个 HBM channels，以利用 data-level parallelism 并支持扩展。

第三，每个 PE 被分配一个 dedicated HBM memory channel。这样每个 PE 都能从独立 256-bit channel 读取数据，减少 channel contention。由于 HBM channel 为 256-bit，而 OCAPI 宽度为 1024-bit，作者设计 stream converter，把 256-bit HBM stream 转成 1024-bit stream。

第四，每个 PE 执行计算。SneakySnake 中，read/reference sequence pairs 在 PEs 之间平均划分；vadvc/hdiff 中，每个 PE 处理输入 grid 的一个 block。对于 SneakySnake，每个 chip maze row 被存为长度等于 read length 的 register array，使各行可同时访问。每轮计算连续 0 的数量，遇到 obstacle 后用最大连续 0 的数量进行 shifting，以避免不规则数组访问。

第五，结果计算完成后，HBM-write engine 将结果写回对应 HBM channel，再由 write-back engine 传回 host 进行后续处理。

优化方面，作者使用三类 HLS 策略：利用算法内在并行性做 hardware pipelining；把 data arrays 划分到多个 BRAM/URAM physical memories，避免双端口片上存储造成 pipeline stall；把输入数据划分给多个 PE，让所有 PE 利用 data-level parallelism。

### 硬件工程师视角

实现部分最值得学习的是“按数据路径设计加速器”。作者并不是简单复制 CPU kernel，而是让数据从 host cache line 到 HBM channel，再到 PE 的 register/BRAM/URAM 层次中逐级变形。实际项目中，这种数据宽度转换、streaming、buffer partition 和 channel affinity 往往比算术单元本身更决定性能。

需要注意的工程风险包括：HLS stream 默认使用 BRAM FIFO，可能导致 BRAM 成为瓶颈；PE 增多后跨 SLR routing 可能导致 timing closure 失败；每 PE 独占 HBM channel 可提升扩展性，但 channel power 和资源消耗会降低能效。

---

## 5. Evaluation / 实验评估

### 原文位置
Page 7-10 / Figure 6, Table 1

### 中文翻译

作者从性能、能耗和 FPGA resource utilization 三方面评估 SneakySnake、vadvc、hdiff。平台包括 Alpha-Data ADM-PCIE-9H7 HBM FPGA、Alpha-Data ADM-PCIE-9V3 DDR4 FPGA、IBM POWER9 host。外部互连包括 CAPI2 和 OCAPI。CPU baseline 是 16-core IBM POWER9，使用全部 64 hardware threads。

数据集方面，SneakySnake 使用 100bp_2 数据集前 30,000 个 sequence pairs，每条序列长度 100 bp。天气实验使用 256 x 256 x 64 grid，类似 COSMO 模型。

### 5.1 Performance Analysis

Figure 6(a)-(c) 给出运行时间。作者把 PE 数量从 1 扩展到 FPGA 资源可容纳的最大数量。DDR4 FPGA 上 SneakySnake、vadvc、hdiff 分别最多容纳 4、4、8 个 PE；HBM FPGA 上分别最多容纳 12、14、16 个 PE。

第一，full HBM+OCAPI designs 相比 64-thread IBM POWER9，SneakySnake、vadvc、hdiff 分别快 27.4x、5.3x、12.7x。OCAPI 相比 CAPI2 进一步提升 28%、37%、44%，原因是 OCAPI bitwidth 为 1024-bit，是 CAPI2 的两倍，同时 coherency logic 移到 IBM POWER CPU 上，释放 FPGA 面积并提升加速器频率。

第二，单 PE 时 DDR4-CAPI2 FPGA 比 HBM-CAPI2 更快，因为 DDR4 channel 宽度是 512-bit，而单个 HBM pseudo-channel 是 256-bit。作者用 HBM_multi+OCAPI 让一个 PE 从 4 个 HBM pseudo-channels 取数，分别获得 1.4x、1.2x、1.8x 性能提升。

第三，随着 PE 数量增加，HBM-based designs 在每个 PE 读取独立 HBM channel 时表现出较好扩展性。但 multi-channel per PE 设计由于需要更多 HBM channels，最多只能容纳 3 个 PE，否则 timing constraints 失败。结果说明“给每个 PE 更多带宽”和“放更多 PE”之间存在面积与时序权衡。

第四，DDR4-based designs 在 vadvc/hdiff 上扩展非线性，因为多个 PE 竞争同一个 memory channel。对于最 memory-bound 的 SneakySnake，单 PE 已经让 memory bandwidth 饱和，增加 PE 并不能减少总时间。

### 5.2 Energy Efficiency Analysis

Figure 6(d)-(f) 给出能效。SneakySnake 用 Mseq/s/Watt 表示，vadvc/hdiff 用 GFLOPS/Watt 表示。作者用 AMESTER 读取 POWER9 系统传感器，并以 active power 评估。

full HBM+OCAPI designs 相比 POWER9，SneakySnake、vadvc、hdiff 能效分别提升 133x、12x、35x。低 PE 数时 DDR4-CAPI2 可能略优于 HBM-CAPI2，但 PE 数增加后，HBM 多通道优势体现出来。multi-channel-single PE 设计虽然给单 PE 更多带宽，但每增加一个 HBM channel 约增加 1 Watt 功耗，因此能效提升并不显著。

作者特别指出，增加 PE 和 HBM channel 数量并不总是提升能效。hdiff 的能效随 PE 增加到 8 个左右后趋于饱和；SneakySnake 和 vadvc 在某些 PE 数之后能效下降。SneakySnake 大量时间花在数据获取上，因此性能提升不一定转化成能效提升。

### 5.3 FPGA Resource Utilization

Table 1 显示 full HBM+OCAPI designs 的资源使用。SneakySnake 使用 58% BRAM、0% DSP、18% FF、70% LUT、1% URAM。vadvc 使用 90% BRAM、39% DSP、37% FF、55% LUT、53% URAM。hdiff 使用 96% BRAM、4% DSP、10% FF、15% LUT、8% URAM。

作者观察到 BRAM 使用率很高，因为 hls::streams 通常实现为 BRAM FIFOs。SneakySnake 不执行 floating-point，因此不用 DSP。vadvc 比 hdiff 资源消耗更高，因为其 compound stencil 更复杂且输入参数更多。虽然 hdiff 理论上还能放更多 PE，但作者只使用单个 HBM stack 的 16 channels，因为更多 PE 会产生 timing constraint violations。

### 硬件工程师视角

评估部分提供了几个可迁移的工程规则。

第一，单通道带宽、总带宽和 PE 数是不同概念。HBM 单 pseudo-channel 可能不如 DDR4 channel 宽，但 HBM 的价值在于多个 channel 并行和近逻辑访问。

第二，性能峰值 PE 数和能效最优 PE 数不同。硬件产品设计通常不能只追求最高吞吐，还要看每 channel 功耗、散热、时序、利用率和实际 workload mix。

第三，HLS 设计的 bottleneck 很可能是 BRAM/URAM banking 与 FIFO，而不是 LUT/DSP。做 FPGA+HBM 项目时，资源表要作为一等结果分析。

---

## 6. Discussion and Conclusion / 讨论与结论

### 原文位置
Page 10 / Discussion

### 中文翻译

论文总结了利用 near-memory-capable FPGA accelerators 加速三个核心 kernel 的经验。第一，HBM-based near-memory FPGA 设计相对 POWER9 CPU 可提升 5.3x-27.4x 性能和 12x-133x 能效。第二，每个 PE 使用 dedicated HBM channel 可以避免 DDR4 FPGA 常见的 memory access congestion，并让多数 data-parallel applications 的性能随 PE 数量近似线性扩展。第三，HBM 设计最大性能通常由可容纳的最大 PE 数决定，但继续增加 PE 可能引起 timing constraint violations，尤其是 HBM channels 只直接连到 SLR0 时。第四，能效会随 PE/channel 增加而饱和甚至下降。

作者希望这些近内存加速基因组分析和天气预测的努力，以及识别和解决的工程挑战，能为未来使用强大近内存可重构加速器加速现代数据密集型应用奠定基础。

### 面向硬件工作的学习提炼

这篇论文对未来硬件工作的启发有三点。

第一，内存带宽要靠“结构化暴露”才能被应用使用。HBM channel 很多，但如果数据布局、PE 划分、buffer 组织和 host interface 不匹配，理论带宽不会自动转化为性能。

第二，near-memory accelerator 的系统边界很重要。host memory 到 FPGA、FPGA 到 HBM、HBM 到 PE、PE 到片上 buffer 都是潜在瓶颈。硬件工程师需要用带宽表、时序约束、资源表和 workload profile 一起评估。

第三，真实应用优先。本文没有只展示合成 benchmark，而是选择 genome pre-alignment 和 weather stencil。对工程团队来说，这提醒我们：架构创新必须用真实 workload 的数据路径检验，否则容易只优化了漂亮但不代表产品负载的微基准。

---

## References / 参考文献

### 原文位置
Page 10-13 / References

参考文献列表保留英文原文，不逐条翻译。建议配套阅读 SneakySnake、NERO、Google consumer workloads for PIM、Modern Primer on PIM，以及 FPGA/HBM/OCAPI/CXL 平台文档。
