# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture

中文标题：Sectored DRAM：实用、节能且高性能的细粒度 DRAM 架构

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：Sectored DRAM 通过 Variable Burst Length 和 Sectored Activation 只传输/激活 cache block 中可能有用的 word，从而在不显著牺牲带宽的情况下降低 DRAM 能耗并提升内存密集负载性能。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：现代 DRAM 以 cache block 粒度传输、以整行/大范围 cell 激活；但很多 workload 的 spatial locality 较差，cache block 中大量 word 在驻留期间未被使用，见 Page 1, Section 1。 已有 fine-grained DRAM 方案往往吞吐低、面积开销高或没有完整支持细粒度传输和激活，见 Page 1-2, Section 1。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何减少传输未使用 cache-block word 的能耗。; 如何减少激活整条 DRAM row 带来的不必要 activation energy。; 如何在细粒度访问下避免 sector misses 导致的 LLC miss 和性能下降。

作者随后给出贡献：提出 Variable Burst Length (VBL)，按请求 sector 数动态调整 burst cycle 数，见 Page 2 与 Page 6, Section 4.2。; 提出 Sectored Activation (SA)，利用 DRAM row 内已有 mat 结构，只激活必要 sector，见 Page 2 与 Page 5-6, Section 4.1。; 提出 LSQ Lookahead 和 Sector Predictor，用于预测/确定 cache block 中会被使用的 word，见 Page 2 与 Page 7, Section 5。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Fine-grained DRAM; energy-efficient memory; variable burst length; sectored activation。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Variable Burst Length (VBL)、Sectored Activation (SA)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- VBL 复用 DRAM I/O 中每个 burst cycle 选择一个 word 的既有机制，让一次 cache block transfer 可以只包含所需 word，见 Page 2, Page 6。
- SA 增加 sector transistors 与 sector latches，通过现有命令传递 sector bits，使 memory controller 选择要激活的 mat/sector，见 Page 2, Page 5-6。
- LSQ Lookahead 从 younger load/store 指令中收集同一 cache block 的未来 word 需求；Sector Predictor 基于过去访问模式预测会被使用的 sector，见 Page 2 与 Page 7。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 使用 41 个 SPEC2006、SPEC2017 和 DAMOV workload，并按 LLC MPKI 分类，见 Page 9, Section 6.1/Table 3。
- 用 Ramulator/DRAMPower/Rambus Power Model 分析 DRAM power、LLC MPKI、single/multi-core performance、system energy 与 area，见 Page 9-13。
- 与 FPA、PRA、HalfDRAM 等 state-of-the-art fine-grained DRAM architectures 比较，见 Page 12-13, Section 7.4。

主要结果如下：

- 读/写一个 sector 相比读/写全部 sector，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%，见 Page 10, Figure 7。
- 只激活一个 sector 可使 DRAM array activation power 降低 66.5%，但整体 ACT power 只降低 12.7%；SA 额外 activation power 开销仅 0.26%，见 Page 10, Section 7.1。
- Basic Sectored DRAM 会把 LLC MPKI 平均提高 3.1x；LA128-SP512 可把 Basic 的 LLC misses 降低 52%，见 Page 10-11, Figure 8。
- 高 MPKI 16-core workload 上，Sectored DRAM 平均 parallel speedup 比 baseline 高 26%，平均 memory latency 降低 25%，见 Page 11-12, Figure 10。
- DRAM energy 最高/平均降低 33%/20%，system energy 最高/平均降低 23%/14%，见 Page 13, Figure 11/12。
- DRAM chip area overhead 为 1.72%；相对 HalfDRAM，取得 89% performance benefits、12% less DRAM energy、34% less chip area，见 Page 1 与 Page 13。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。
- 低/中 MPKI workload 可能不受益，作者提出动态关闭 Sectored DRAM，见 Page 14, Section 8.2。
- 需要 processor/cache/memory controller 维护 sector bits、LSQ Lookahead 和 predictor，硬件复杂度不只在 DRAM 端，见 Page 7 与 Page 14。
- ECC、prefetching、更细粒度 sector 和更复杂 predictor 多数留给讨论/未来探索，见 Page 14-15, Sections 8.3-8.5。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- 更强 predictor 是否能显著降低 sector miss，又不会引入过高面积和能耗？
- 真实 DDR5/HBM 系统中 sector bits 如何编码和传输最现实？
- 对混合 workload，动态开关策略如何避免频繁切换带来的抖动？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：Sectored DRAM 通过 Variable Burst Length 和 Sectored Activation 只传输/激活 cache block 中可能有用的 word，从而在不显著牺牲带宽的情况下降低 DRAM 能耗并提升内存密集负载性能。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
