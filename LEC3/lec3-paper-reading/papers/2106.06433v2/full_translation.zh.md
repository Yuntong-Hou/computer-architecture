# Full Chinese Translation

> 说明：以下为面向学习的逐节中文详译/译述，保留关键英文术语、模型名、指标名和数值；参考文献不逐条翻译。

## Title

原文标题：FPGA-Based Near-Memory Acceleration of Modern Data-Intensive Applications

中文标题：基于 FPGA 的现代数据密集型应用近内存加速

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

现代数据密集型应用既需要高计算能力，又常受到严格功耗约束。当前计算系统中，计算单元和内存单元之间的数据搬移代价很高，使这类应用浪费大量执行周期和能量。基因组分析和天气预测是典型例子。近期 FPGA 将可重构逻辑与高带宽内存（High Bandwidth Memory, HBM）集成在同一平台上，可以更有效地移动数据、提升性能和能效，这体现了向近内存计算（near-memory computing）转变的趋势。本文利用带 HBM 的 FPGA 加速 genome analysis 的 pre-alignment filtering，以及 weather prediction model 中的代表性 kernels。实验显示，相比高端 IBM POWER9 系统和传统 DDR4 FPGA 板，本文方案有显著加速和能耗节省。作者的结论是：基于 FPGA 的 near-memory computing 有潜力缓解现代数据密集型应用中的数据搬移瓶颈。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 3

### 中文翻译

现代系统采取 processor-centric 设计，数据必须通过较慢且耗电的 off-chip bus 在内存和计算单元之间往返。对于 genome analysis、weather modeling 等 workload，这种 CPU-memory-CPU 数据移动成为主要成本。作者用 POWER9 上的 roofline model 说明：SneakySnake、vadvc、hdiff 的实际性能受 memory bandwidth 和 memory hierarchy 限制，而不是 CPU peak FLOPS 限制。

本文目标是利用带 HBM 的现代 FPGA 加速两个真实数据密集型应用。作者强调现代 FPGA 的四个趋势：HBM 与 FPGA 同封装、URAM/BRAM 等更大的片上存储、OCAPI/CAPI/CCIX/CXL 等 cache-coherent interconnect、7-14nm FinFET 带来的更强可重构逻辑能力。这些趋势让 FPGA 更接近 data-centric computing。

作者选择两个 case studies：基因组 pre-alignment filtering 和 COSMO weather prediction kernels。前者会快速过滤掉大多数不相似序列，避免昂贵的 dynamic programming alignment；后者代表气象模拟中常见的 compound stencil 计算。

## 2. Near-Memory Computation on FPGAs / FPGA 上的近内存计算

### 原文位置

Page 3 / Figure 2

### 中文翻译

系统由 IBM POWER9 主机连接 HBM-based FPGA。FPGA 连接两个 HBM2 stacks，每个 stack 有 16 个 pseudo memory channels，总计 32 个 256-bit channels。HBM IP 负责数据传输。FPGA 通过 OCAPI 连接 host CPU，并在 FPGA 内实现 accelerator functional unit (AFU)。AFU 包含多个 processing elements (PEs)，每个 PE 加速应用的一部分，并使用 LUT、FF、BRAM、URAM 等 FPGA 资源。

## 3. Modern Data-Intensive Applications / 现代数据密集型应用

### 原文位置

Page 3 - Page 5

### 中文翻译

### 3.1 Genome Analysis: Pre-Alignment Filtering

Sequence alignment 是基因组分析中的基础步骤，但通常使用 dynamic programming，时间和空间复杂度较高。在实际 pipeline 中，大量 sequence pairs 高度不相似，因此如果能在正式 alignment 前快速过滤，就能节省大量时间。SneakySnake 将 approximate string matching 问题转换为 VLSI single net routing 问题，通过构建并部分遍历 chip maze 来估计 edit distance。这个方法并行度高，但访存不规则，cache locality 不好。

### 3.2 Weather Prediction Kernels

COSMO weather model 中的 vadvc 和 hdiff 是 compound stencil kernels。它们在三维网格上执行多次 element-wise 和 stencil 计算，需要反复访问邻近 grid points。虽然 stencil 可并行，但复杂访存和数据复用需求使其容易受到 DRAM latency/bandwidth 限制。

## 4. Accelerator Design / 加速器设计

### 原文位置

Page 5 - Page 7

### 中文翻译

数据从 host DRAM 经 POWER9 cache line 传到 FPGA board memory，再由 FPGA 端的 engines 搬入 HBM 或片上存储。作者对每个 kernel 设计多个 PEs，尽量将数据分布到不同 HBM channels。为了提高吞吐，设计使用 Vivado HLS pragmas 做 pipeline、array partitioning 和 stream-based dataflow。对片上存储，作者结合 BRAM、URAM 和 HBM 构成 heterogeneous memory hierarchy，并用 greedy strategy 选择合适的数据放置方式。

## 5. Evaluation / 实验评估

### 原文位置

Page 7 - Page 10

### 中文翻译

实验比较 HBM FPGA、DDR4 FPGA 和 IBM POWER9 CPU。HBM 平台为 Alpha-Data ADM-PCIE-9H7，DDR4 平台为 ADM-PCIE-9V3；互连包括 CAPI2 和 OCAPI。SneakySnake 使用 100bp_2 数据集前 30,000 个 sequence pairs；weather kernels 使用 256 x 256 x 64 grid。

主要性能结论是：最大规模 HBM+OCAPI designs 在 SneakySnake、vadvc、hdiff 上分别比 64-thread POWER9 快 27.4x、5.3x、12.7x。OCAPI 比 CAPI2 更快，原因包括更宽的数据通路和更高可用 FPGA area / clock frequency。多 PE 且每个 PE 使用 dedicated HBM channel 时，HBM 设计更容易扩展；DDR4 设计因所有 PE 竞争单一 memory channel 而快速饱和。

能效方面，HBM+OCAPI designs 分别比 POWER9 提高 133x、12x、35x。作者也指出，更多 PE 和更多 HBM channels 不一定带来更高能效，因为每个 HBM channel 会增加功耗，某些 kernel 的数据搬移时间或控制流开销会使能效出现饱和甚至下降。

## 6. Discussion / 讨论

### 原文位置

Page 10

### 中文翻译

作者总结了四个关键经验。第一，HBM-based FPGA 可以在这些 workload 上显著提升性能和能效。第二，dedicated HBM channel per PE 避免了 DDR4 单通道拥塞，使数据并行应用更容易随 PE 数扩展。第三，最大性能往往受可放置 PE 数和 timing closure 限制；HBM channels 连接到特定 SLR，复杂设计可能难以收敛。第四，最高能效点可能早于最高性能点出现，因为增加 channel 和 PE 会增加功耗。

## References / 参考文献

参考文献列表保持英文原文，请回到 PDF Page 10-13 查看。
