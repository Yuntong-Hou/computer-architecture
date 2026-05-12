# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture

中文标题：PIM-enabled Instructions：低开销、局部性感知的 Processing-in-Memory 架构

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：这篇论文把简单 PIM operations 封装为主机 ISA 中的 PIM-enabled instructions，并用硬件局部性监控在 host-side 和 memory-side 执行之间动态选择，从而兼顾 PIM 带宽优势与 cache locality。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：作者指出早期和现代 PIM 往往需要新的编程模型、非 cacheable memory region 或显式 cache flush，难以无缝接入现有系统，见 Page 1, Section 1。 3D-stacked DRAM/HMC 提供 logic die、TSV 内部高带宽和低能耗传输，但如果所有操作都强制在 memory side 执行，高局部性数据反而会失去 on-chip cache 优势，见 Page 2-3, Sections 2.1-2.2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何让 PIM operation 像普通 host instruction 一样使用，而不是引入全新的 PIM 编程模型。; 如何让 PIM operation 与现有 cache coherence 和 virtual memory 机制兼容。; 如何根据数据局部性动态决定 PEI 在 host processor 还是 memory-side logic 上执行。

作者随后给出贡献：提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。; 提出 single-cache-block restriction，使 PEI 的目标内存范围限制在一个 LLC cache block 内，以简化 localization、coherence 和 locality profiling，见 Page 3-4, Section 3.1。; 设计 PEI Computation Unit (PCU) 与 PEI Management Unit (PMU)，支持 host-side/memory-side PEI execution、atomicity、coherence 和 locality monitoring，见 Page 5-7, Section 4。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Processing-in-memory ISA interface; locality-aware PIM execution; 3D-stacked DRAM。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 PIM-enabled instruction (PEI)、PEI Computation Unit (PCU)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。
- single-cache-block restriction 限制单个 PEI 只访问一个 LLC block，并把 input/output operands 也限制在一个 cache block 内，从而使 coherence、translation 和 locality profiling 都落在现有粒度上，见 Page 3-4。
- PMU 在 LLC 附近维护 PIM directory 与 locality monitor：前者管理 in-flight PEI 的 reader-writer atomicity，后者以 cache-like partial tags 监控目标 cache block 的局部性，见 Page 5-7。
- Locality-Aware policy 根据目标数据是否可能在 cache 中受益，选择 host-side 或 memory-side PCU；balanced dispatch 进一步根据 request/response bandwidth 平衡执行位置，见 Page 9-11。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 在 HMC-based 系统模型上模拟 10 个 workload：图处理、hash join、histogram、R-probe、streamcluster、SVM 等，输入分为 small/medium/large，见 Page 8-9, Table 3。
- 比较 Host-Only、PIM-Only、Ideal-Host 和 Locality-Aware 四种配置，指标包括 normalized IPC、off-chip transfer、multiprogrammed throughput、energy、area 和敏感性，见 Page 9-12。
- PageRank motivation 中用 9 个真实 graph 评估 in-memory atomic add 的收益/风险，见 Page 3, Figure 2。
- multiprogrammed evaluation 随机组合 200 个 workload，测试动态 locality-aware 机制在混合局部性下的表现，见 Page 10, Figure 9。

主要结果如下：

- PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。
- large inputs 中 PIM-Only 相比 Ideal-Host 平均快 44%；small inputs 中 PIM-Only 平均慢 20%，因为即使数据适合 cache 也访问 DRAM，见 Page 9, Figure 6。
- Locality-Aware 在 large inputs 中通过把 79% PEIs offload 到 memory-side，相比 Host-Only 提升 47%；在 small inputs 中通过让 86% PEIs host-side 执行，相比 PIM-Only 提升 32%，见 Page 9, Section 7.1。
- medium graph workloads 中，Locality-Aware 同时利用 host-side 与 memory-side PCUs，分别比 Host-Only 和 PIM-Only 快 12% 和 11%，见 Page 9-10。
- balanced dispatch 在 SC/SVM 上最多进一步提升 25%，见 Page 11, Figure 10。
- Locality monitor storage overhead 为 512KB，即 LLC capacity 的 3.1%；理想化 PIM directory/locality monitor 只分别带来 0.13%/0.31% 性能提升，说明 PMU overhead 很小，见 Page 9 与 Page 11。
- Locality-Aware 在所有输入规模下 memory hierarchy energy 最低；memory-side PCUs 只占 HMC energy 的 1.4%，area overhead 估计为 logic die area 的 1.85%，见 Page 12, Section 7.7。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。
- 软件仍需把目标代码改写为 PEIs；作者认为编译器未来可自动识别，但本文主要假设程序员手动修改，见 Page 4, Section 3.3。
- PEI 与普通 load/store 之间的 atomicity 不是自动保证的，需要 pfence 等同步，见 Page 4, Section 3.2。
- 评估基于模拟 HMC/PCU 模型，真实 HMC/HBM 产品中的接口、timing 和 coherence 支持可能不同。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- single-cache-block restriction 是否会限制现代图分析/数据库中更复杂的 PIM primitives？
- PEI 的 locality monitor 能否迁移到 HBM/CXL memory expander 场景？
- 编译器如何自动识别 PEI 插入点并和 ordinary vectorization/pass ordering 协同？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：这篇论文把简单 PIM operations 封装为主机 ISA 中的 PIM-enabled instructions，并用硬件局部性监控在 host-side 和 memory-side 执行之间动态选择，从而兼顾 PIM 带宽优势与 cache locality。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
