# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic

中文标题：Proteus：通过动态位精度、自适应数据表示和灵活算术实现高性能 Processing-Using-DRAM

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：现有 PUD 多采用 bulk bit-serial execution model，用固定 two's complement 和固定 bit-precision 处理整行数据，导致大量 inconsequential bits 被无谓计算，见 Page 1-2。 PUD 还面临 throughput-oriented execution 难隐藏低并行场景下的单操作延迟，以及高精度操作延迟随 bit-width 线性或二次增长的问题，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。; 如何在 PUD operation 内并行执行独立 in-DRAM primitives，缓解单操作延迟。; 如何为不同 bit-precision 自动选择最合适的 data representation 和 arithmetic algorithm。

作者随后给出贡献：提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。; 利用 narrow values 动态降低 PUD operation bit-precision，减少 latency 和 energy，见 Page 2。; 利用 SALP 将一个 data word 的不同 bits 分散到多个 subarrays，跨 bit 并行执行独立 primitives，见 Page 2 与 Page 4-5。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Dynamic bit precision; PUD arithmetic; redundant binary representation; runtime µProgram selection。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Dynamic bit-precision、Narrow values。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。
- Parallelism-Aware µProgram Library 保存不同 bit-precision、two's complement/RBR、bit-serial/bit-parallel 算法的 µPrograms 及 cost model LUTs，见 Page 2 与 Page 8-10。
- µProgram Select Unit 在发出 PUD operation 时查询 bit-precision 和 cost LUT，选择最低延迟或最低能耗的 µProgram，见 Page 2 与 Page 8-10。
- Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 使用 12 个真实应用，来自 Phoenix、Polybench、Rodinia、SPEC2017；系统配置见 Page 12, Tables 2-3。
- 比较 CPU、A100 GPU、SIMDRAM-SP、SIMDRAM-DP、Proteus LT/EN with static/dynamic precision，见 Page 12-13。
- 额外分析 data mapping/representation conversion overhead、floating-point synthetic throughput、GPU tensor cores 对比和面积开销，见 Page 13-14。

主要结果如下：

- Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。
- SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。
- Dynamic Bit-Precision Engine 使 Proteus 相比 static bit-precision 性能提升 46%，energy consumption 降低 58%，见 Page 12-13, Figures 11-12。
- Proteus 平均比 CPU/GPU/SIMDRAM 分别降低 90.3x、21x、8.1x energy consumption，见 Page 1 与 Page 13。
- 在 int8/int4 GEMM-heavy workloads 上，Proteus 相对 A100 tensor cores 提供 20x/43x performance per mm² 和 484x/767x performance per Watt，见 Page 14, Figure 14。
- 面积开销低：DRAM chip 1.6%，CPU die 0.03%，见 Page 1 与 Page 14-15。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。
- baseline PUD substrate 不支持 floating-point，浮点评估使用 synthetic analysis 而非完整真实应用，见 Page 13-14。
- Proteus 依赖 Ambit、LISA、SALP 等底层机制，真实硬件实现需要这些机制可靠可用，见 Page 14-15。
- 动态 bit-precision 需要对象追踪、转置缓冲和元数据维护；短任务上的 runtime/metadata 开销仍需进一步验证。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- Proteus 与 MIMDRAM 是否可以结合，同时解决位精度和资源粒度问题？
- 如果应用包含大量 floating-point 或不规则数据结构，Proteus 的收益还剩多少？
- 动态 bit-precision metadata 在多线程、多进程和虚拟内存环境中如何维护一致性？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
