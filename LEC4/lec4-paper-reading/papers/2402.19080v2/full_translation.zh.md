# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：MIMDRAM: An End-to-End Processing-Using-DRAM System for High-Throughput, Energy-Efficient and Programmer-Transparent Multiple-Instruction Multiple-Data Processing

中文标题：MIMDRAM：面向高吞吐、节能和程序员透明 MIMD 处理的端到端 Processing-Using-DRAM 系统

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：MIMDRAM 通过细粒度控制 DRAM mats，让同一 subarray 中不同 mats 执行独立 PUD operations，从传统超宽 SIMD PuD 转向更灵活的 MIMD execution model。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：PUD 可利用 DRAM 阵列内部并行性执行 16K 到 262K-bit-wide 的 SIMD 操作，但 DRAM row 粒度过大且固定，导致 SIMD 利用率低、难支持 reduction、编程困难，见 Page 1-2。 传统 PUD 往往要求程序员手工提取极宽数据并行性并映射到 DRAM row，缺少编译器支持，见 Page 2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何把 PUD 操作粒度从完整 DRAM row 缩小到 mat/segment，以匹配应用实际 SIMD parallelism。; 如何在 DRAM 内低成本支持 reduction 等需要跨 column 数据移动的操作。; 如何让编译器自动发现 PUD-friendly regions 并生成合适粒度的 PUD operations。

作者随后给出贡献：提出首个面向 general-purpose applications 的端到端 MIMD PUD 系统，见 Page 3。; 使用 fine-grained DRAM 思路，只分配和控制给定 PUD operation 所需的 DRAM mats，见 Page 2-3 与 Page 4-7。; 加入 local/global interconnect 支持 vector-to-scalar reduction，降低以往 interconnect 面积开销，见 Page 5-7。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：End-to-end PUD architecture; MIMD in DRAM; fine-grained DRAM mats; compiler support。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 MIMD、PUD。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- MIMDRAM 在硬件上增加 latches、isolation transistors 和 selection logic，使单个 DRAM mat 可被独立寻址并执行 PUD operation，见 Page 4-6, Section 4.1。
- 它在 local/global I/O circuitry 中放置低成本 interconnect，以支持不同粒度的 column communication 和 in-DRAM vector reduction，见 Page 6-7, Figure 6。
- memory controller 新增控制单元，协调同一 subarray 内多个 mats 上独立 PUD operations 的并发执行，见 Page 7-8, Section 4.2。
- 软件侧通过 compiler passes 自动 vectorize PUD-friendly regions、选择 SIMD granularity，并调度独立 PUD operations，见 Page 8-11。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 使用 Phoenix、Polybench、Rodinia、SPEC2017 的 12 个真实应用和 495 个多程序混合，见 Page 11, Section 7。
- 比较 CPU、GPU、SIMDRAM、DRISA、Fulcrum 与 MIMDRAM，并分析 single-application、multi-programmed、area-normalized performance、SALP/BLP scaling 和 area，见 Page 12-14。
- 主要指标包括 SIMD utilization、performance per Watt、weighted speedup、harmonic speedup、maximum slowdown、performance per area，见 Page 12-14。

主要结果如下：

- MIMDRAM 平均提供 SIMDRAM 的 15.6x SIMD utilization、14.3x energy efficiency 和 34x performance，见 Page 12, Figure 9。
- 相对 CPU/GPU，MIMDRAM 平均提供 30.6x/6.8x energy efficiency，但在只用单 subarray/bank 时平均性能仍可能低于 CPU/GPU，见 Page 12。
- 多程序混合中，MIMDRAM 相比 SIMDRAM 平均提升 1.68x weighted speedup、1.33x harmonic speedup，并将 maximum slowdown 降低 1.32x，见 Page 13, Figure 10。
- 相比 baseline CPU 的多程序执行，MIMDRAM 总 throughput 提升 19%，见 Page 13, Figure 11。
- 当使用 64 subarrays/bank 和 16 banks 时，MIMDRAM 平均达到 CPU 的 13.2x、GPU 的 2x performance，见 Page 14, Figure 14。
- 面积开销较低：DRAM chip 约 1.11%，CPU die 约 0.6%，见 Page 1 与 Page 14-15。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。
- multiplication/division 等成本高的操作仍是瓶颈，某些 workload 即使用满 DRAM parallelism 也可能低于 CPU，见 Page 14。
- 高 vectorization factor mixes 下 fairness 仍可能比部分 SIMDRAM 多 bank 配置差，需要更好的 QoS/scheduling，见 Page 13。
- 需要修改 DRAM subarray、memory controller、ISA、compiler 和 OS，落地复杂度高。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- MIMDRAM 的 compiler passes 在更复杂控制流或 pointer-heavy 应用上效果如何？
- 是否可以结合 PNM 逻辑单元加速 multiplication/division 和 reduction，从而降低 MIMDRAM 短板？
- 在真实操作系统和多租户环境中，mat/subarray 级资源调度如何保证 QoS？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：MIMDRAM 通过细粒度控制 DRAM mats，让同一 subarray 中不同 mats 执行独立 PUD operations，从传统超宽 SIMD PuD 转向更灵活的 MIMD execution model。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
