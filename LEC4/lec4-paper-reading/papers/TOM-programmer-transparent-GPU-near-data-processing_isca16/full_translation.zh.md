# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Transparent Offloading and Mapping (TOM): Enabling Programmer-Transparent Near-Data Processing in GPU Systems

中文标题：TOM：在 GPU 系统中实现程序员透明的 Near-Data Processing

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：TOM 通过编译器选择可 offload 的 memory-intensive code blocks，并用软硬件协同数据映射把 offloaded code 与数据共置，从而无需程序员修改 GPU 程序即可利用 3D-stacked memory logic layer。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：GPU 应用常受 off-chip memory bandwidth 限制；3D-stacked memory 的 logic layer 可以放置 SMs 并靠 TSV 获得高内部带宽，见 Page 1, Section 1。 NDP 系统面临两个核心问题：哪些代码应在 main GPU 还是 memory stack SMs 执行，以及数据如何映射到多个 memory stacks，见 Page 1。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何不让程序员手动标注 offloading code。; 如何在多个 memory stacks 中放置数据，使 offloaded code 和访问数据尽量共置，同时不损害 main GPU 的带宽利用。; 如何根据运行时资源状况控制 offloading aggressiveness，避免 memory stack SMs 成为瓶颈。

作者随后给出贡献：提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。; 提出 programmer-transparent data mapping，利用 offloaded blocks 的可重复内存访问模式预测页面映射，见 Page 2 与 Page 4-6, Section 3.2。; 提出 runtime offloading control，根据 SM 与 bandwidth utilization 动态决定候选 block 是否实际 offload，见 Page 2 与 Page 6。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Near-data processing; GPU; 3D-stacked memory; transparent offloading and data mapping。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Near-Data Processing (NDP)、Transparent Offloading and Mapping (TOM)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- 编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。
- data mapping 机制在 learning phase 评估简单 address mapping options，预测 offloaded block 将访问的 pages，并将这些 pages 放到最接近 offloaded code 的 stack，见 Page 4-6。
- offloading control 防止过度 offload：当 memory stack SMs 的 pending requests 或资源压力过大时，候选 block 可继续在 main GPU 执行，见 Page 6 与 Page 9。
- 实现上增加 offloading metadata table、memory allocation table 和 memory map analyzer 等结构，见 Page 6-7。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 使用 Rodinia、GPGPU-Sim workloads 和 CUDA SDK 中 10 个 memory-intensive GPU applications，见 Page 8-9, Table 2。
- 指标包括 IPC speedup、off-chip memory traffic、energy consumption、warp capacity sensitivity、internal/cross-stack bandwidth sensitivity 和 area，见 Page 9-12。
- baseline 是不能 offload 到 3D-stacked memories 的 GPU 系统；比较不同 NDP offloading/mapping policies，见 Page 9。

主要结果如下：

- TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。
- programmer-transparent data mapping 相比 baseline memory mapping 平均额外提升 10%；例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，见 Page 9。
- 没有 offloading control 时，系统平均变慢 3%/7%；controlled offloading 将 offloaded instructions 从 46.4% 降到 15.7%，避免 memory stack SMs 成瓶颈，见 Page 9-10。
- TOM 平均降低 off-chip memory traffic 38%、最高 99%，平均降低 energy 11%、最高 37%，见 Page 2 与 Page 10。
- 把 memory stack SM warp capacity 提高到 4x 可在保持约 29% speedup 的同时额外节省 20% memory traffic，见 Page 11, Figures 11-12。
- 即使 internal bandwidth 等于 external link bandwidth，TOM 平均仍有 28% speedup，见 Page 11, Figure 13。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。
- data mapping 假设 offloaded block 的访问模式具有可重复性；BFS 这类 irregular workload 可能被错误映射拖慢，见 Page 9。
- 编译器分析使用保守静态估计和 PTX 工具链，真实 GPU ISA/驱动中的实现会更复杂，见 Page 3 与 Page 8。
- offloading aggressiveness 仍可改进，尤其是 offloaded block 中 ALU 指令比例较高时，见 Page 11。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- TOM 的 mapping predictor 如何适应 phase behavior 更剧烈的现代 GPU workloads？
- 在 HBM/CXL 等新内存系统中，TOM 的 offload/mapping cost model 是否仍成立？
- 是否能把 TOM 的透明 offloading 思路迁移到 UPMEM 或其他 PIM 系统？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：TOM 通过编译器选择可 offload 的 memory-intensive code blocks，并用软硬件协同数据映射把 offloaded code 与数据共置，从而无需程序员修改 GPU 程序即可利用 3D-stacked memory logic layer。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下按 TOM/ISCA 2016 论文结构扩写，覆盖 GPU memory bottleneck、3D-stacked memory logic layer、compiler offload candidate selection、data mapping learning/prediction、runtime offloading control、hardware structures、evaluation、traffic/energy/sensitivity、limitations。TOM 是 near-data processing，不是 DRAM-array PuD。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
TOM 研究如何在不要求程序员修改 GPU 程序的情况下利用 3D-stacked memory logic layer。GPU 应用常受 off-chip memory bandwidth 限制，而 3D-stacked memory 内部 TSV 带宽很高。如果在 memory stack logic layer 中放置简化 SMs，将 memory-intensive code blocks offload 到数据附近执行，就能减少 main GPU 与 memory stacks 之间的数据流量。

TOM 面临两个问题：哪些代码应该 offload？数据应映射到哪个 memory stack？如果 offloaded code 和数据不共置，cross-stack traffic 仍会很高；如果过度 offload，memory stack SMs 资源不足，会成为瓶颈。TOM 用编译器选择候选 block，用 learning/prediction 进行 data mapping，并用 runtime offloading control 动态控制实际 offload。

评估显示，在 10 个 memory-intensive GPGPU workloads 上，TOM 平均提升 30%、最高 76%，平均降低 off-chip memory traffic 38%，平均降低 energy 11%。

### 硬件工程师思考
TOM 的核心不是“把更多 SM 放进内存”，而是 code-data co-location。Near-data processing 成败取决于 offloaded work 是否真的主要访问本地 stack 数据，以及 offload overhead 是否小于节省的 bandwidth。

## 1. Introduction / 引言

### 原文位置
Page 1-2

### 中文翻译
GPU 提供大量并行计算，但许多 GPGPU workloads 受限于 memory bandwidth。3D-stacked memory 提供高内部带宽和 logic layer，可在每个 memory stack 中放置少量 SMs。这样，部分 memory-intensive code 可在 stack 内执行，减少跨 package/channel 的 traffic。

但手动 offload 对程序员负担很重。程序员必须知道哪些 basic blocks memory-intensive、哪些数据在哪个 stack、offload 后 live-in/live-out registers 如何传输。TOM 的目标是 programmer-transparent，由编译器和硬件自动选择。

### 硬件工程师思考
TOM 属于系统级 NDP，挑战更像 GPU compiler/runtime 和 memory mapping，而不是 DRAM 电路。它对现代 HBM GPU、chiplet GPU、CXL-attached memory accelerator 都有启发：计算靠近数据前，必须先决定数据放哪里。

## 3. TOM Design / TOM 设计

### 原文位置
Page 3-7

### 中文翻译
Offload candidate selection 由编译器完成。编译器估计将一个 code block 放到 memory stack SM 执行后，TX/RX bandwidth 如何变化。若节省的 memory traffic 大于 live-in/live-out register transfer 和控制开销，则标记为 candidate。Page 3 Equations 1-4 给出 cost-benefit 模型。

Data mapping 是 TOM 的第二核心。TOM 在 learning phase 评估简单 address mapping options，观察 offloaded blocks 的访问模式，并预测哪些 pages 会被哪个 memory stack 的 offloaded code 频繁访问。随后将这些 pages 映射到最接近对应 offloaded execution 的 stack。这个机制对访问模式可重复的 workload 有效。

Runtime offloading control 负责防止过度 offload。如果 memory stack SMs pending requests 过多或资源压力高，候选 block 可继续在 main GPU 执行。这样避免 memory-side compute resources 成为瓶颈。

实现上，TOM 增加 offloading metadata table、memory allocation table、memory map analyzer 等结构。编译器和 runtime 共同管理候选 blocks、数据 mapping 和实际 offload decisions。

### 硬件工程师思考
TOM 同时处理三个映射：code block -> execution site，page -> memory stack，runtime pressure -> offload decision。这三者必须闭环。如果只做编译器 offload，不做 data mapping，可能把计算放到错误 stack；如果只做 data mapping，不控制 offload，stack SM 会被压垮。

## 4-5. Evaluation / 评估

### 原文位置
Page 8-12; Table 2; Figures 8-13

### 中文翻译
评估使用 Rodinia、GPGPU-Sim workloads 和 CUDA SDK 中 10 个 memory-intensive GPU applications。Baseline 是不能 offload 到 3D-stacked memories 的 GPU 系统。指标包括 IPC speedup、off-chip traffic、energy、warp capacity sensitivity、internal/cross-stack bandwidth sensitivity 和 area。

TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，所有 workload 均有 speedup。Transparent data mapping 相比 baseline memory mapping 平均额外提升 10%。例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，说明 mapping 对 code-data co-location 很关键。

如果没有 offloading control，系统平均变慢 3%/7%。Controlled offloading 将 offloaded instructions 从 46.4% 降到 15.7%，避免 memory stack SMs 成为瓶颈。这个结果说明不是 offload 越多越好。

Traffic/energy 方面，TOM 平均降低 off-chip memory traffic 38%、最高 99%，平均降低 energy 11%、最高 37%。当 memory stack SM warp capacity 提高到 4x 时，可维持约 29% speedup 并额外节省 20% memory traffic。即使 internal bandwidth 等于 external link bandwidth，TOM 平均仍有 28% speedup。

### 硬件工程师思考
TOM 的敏感性分析很有价值：internal bandwidth 不是唯一因素，warp capacity、offload aggressiveness 和 mapping accuracy 同样重要。真实硬件项目不能只宣传 HBM 内部带宽，还要给出 logic layer compute capacity 和调度策略。

## Limitations and Conclusion / 局限与结论

### 原文位置
Page 11-13

### 中文翻译
TOM 主要面向 memory-intensive GPU workloads。Compute-intensive code 通常不会被选为 candidate。Data mapping 假设 offloaded blocks 的访问模式有可重复性；BFS 等 irregular workload 可能被错误预测拖慢。编译器分析基于 PTX 和保守估计，真实 GPU ISA/driver 中实现更复杂。

结论强调，TOM 通过编译器、runtime 和硬件 mapping 协同，使 GPU 程序可透明利用 3D-stacked memory logic layer。它展示 NDP 系统的关键不只是有 near-data SM，而是自动选择代码、放置数据和控制 offload。

### 硬件工程师复习重点

- Page 1：两个 challenge，offload selection 和 data mapping。
- Page 3 Equations 1-4：candidate cost model。
- Page 4-6：mapping learning/prediction。
- Page 9：无 control 会变慢，说明 offload 不是越多越好。
- Page 10-12：traffic/energy/sensitivity 反映工程边界。

### 对未来工作的启发
TOM 对现代 GPU/HBM 设计的启发是：near-data compute 需要 compiler + page mapping + runtime throttling。只在 memory stack 放 compute units 不够，数据和代码必须动态共置。
