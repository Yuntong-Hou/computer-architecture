# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures

中文标题：DaPPA：面向 Processing-in-Memory 架构的数据并行编程框架

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：DaPPA 用 map/filter/reduce/window/group 等 data-parallel patterns 和 Pipeline dataflow 接口自动生成 UPMEM 代码，降低 PIM 编程复杂度并保持甚至提升端到端性能。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：UPMEM 是首个商用 PIM 系统，拥有大量 DPUs，但程序员必须手动划分数据、管理 CPU-DPU/DPU 内存传输、启动 kernel 和收集输出，见 Page 1, Section 1。 这种编程模型要求开发者理解 MRAM/WRAM/IRAM、DPU tasklets 与数据搬移细节，阻碍 PIM 普及，见 Page 1-3。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何让程序员不用手动管理 UPMEM 的数据分布、内存分配和通信。; 如何用高层 data-parallel pattern 表达 PIM-friendly computation。; 如何自动生成高效 UPMEM binary，同时减少代码量。

作者随后给出贡献：提出首个面向 UPMEM 的 data-parallel pattern-based programming framework，见 Page 2。; 提供 map、filter、reduce、window、group 五类 primary data-parallel pattern primitives，见 Page 2 与 Page 4-7。; 提出 Pipeline dataflow programming interface，用 stage 串联多个 pattern，见 Page 2 与 Page 5-7。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：PIM programming framework; UPMEM; data-parallel patterns; code generation。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 DaPPA、UPMEM。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- 用户用 C/C++ 调用 DaPPA pattern APIs 描述数据转换，DaPPA 负责将 primitive 翻译并并行化到 CPU 和 DPUs，见 Page 2 与 Page 4-7。
- Pipeline 类表示一串 stage，每个 stage 包含一个 pattern 和用户定义计算，按 dataflow 顺序执行，见 Page 5-7。
- dynamic template-based compilation 先根据 UPMEM application skeleton 生成初始代码，再填充 offset、数据搬移、WRAM/MRAM 参数和 CPU/DPU work partition，见 Page 8-10。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 实验平台为 2-socket Intel Xeon Silver 4110、128GB DDR4-2400、20 个 UPMEM PIM DIMMs、160GB PIM-capable memory、2560 DPUs，见 Page 10, Section 6。
- 评估六个 PrIM workloads：VA、SEL、UNI、RED、GEMV、HST-S，见 Page 10-11。
- 比较对象包括 hand-tuned PrIM implementations 和 SimplePIM；指标包括 LOC、端到端执行时间、DPU kernel performance 与 runtime overhead，见 Page 10-12。

主要结果如下：

- 相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC，见 Page 11, Table 1。
- 六个 workload 上，DaPPA 平均达到 PrIM 端到端性能的 2.1x，SEL/UNI 因并行数据回传策略表现尤其好，见 Page 11, Figure 5。
- DPU kernel performance 平均为 PrIM 的 1.4x，最高 3.5x，见 Page 11, Figure 6。
- runtime compilation/模板替换开销包括约 1 ms skeleton substitution、150 ms DPU binary compilation、1-150 ms 其他操作；相比 UPMEM SDK 分配 DPUs 的约 1200 ms 与端到端执行时间较小，见 Page 12, Section 7.3。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。
- DaPPA 强绑定 UPMEM 架构和 SDK，迁移到其他 PIM 架构需要重新设计 backend，见 Page 12, Related Work。
- CPU-DPU/DPU-CPU transfer time 仍占主要执行时间，框架不能消除 UPMEM 硬件通信瓶颈，见 Page 11, Figure 5。
- runtime compilation 虽然相对端到端时间较小，但对短任务或频繁构建 Pipeline 的场景可能不可忽略，见 Page 12。
- UPMEM 缺乏 direct inter-DPU communication，DaPPA 需要通过 host/main memory 间接组织数据，见 Page 3。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- DaPPA 是否能支持需要复杂 inter-DPU communication 的 graph/irregular workload？
- 对于小输入或短任务，runtime compilation 开销是否会超过收益？
- 能否把 DaPPA 的 data-parallel pattern 抽象迁移到非 UPMEM 的 PIM/near-memory 平台？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：DaPPA 用 map/filter/reduce/window/group 等 data-parallel patterns 和 Pipeline dataflow 接口自动生成 UPMEM 代码，降低 PIM 编程复杂度并保持甚至提升端到端性能。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
