# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM

中文标题：PiDRAM：面向 Processing-in-DRAM 的端到端 FPGA 框架

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：PiDRAM 是一个基于 FPGA/RISC-V 的端到端实验框架，用真实未改动 DDR3 芯片研究 commodity DRAM based PuM 技术的系统集成问题。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：作者指出很多 PuM 技术已经能在 off-the-shelf DRAM 中通过非标准时序或模拟行为实现，但传统系统、测试平台和模拟器都难以同时支持真实芯片、可改时序、系统软件和完整应用执行，见 Page 1-2, Section 1。 RowClone 这类 in-DRAM copy 需要特殊内存分配、地址对齐和 coherence 处理；D-RaNGe 这类 TRNG 还依赖真实芯片的时序失败特性，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何在真实系统中发出 PuM 所需的 DRAM command sequence 与 violated timing parameters。; 如何让 OS/supervisor、用户库、memory controller 与 DRAM 芯片共同支持 PuM operation。; 如何评估真实芯片上的 RowClone 和 D-RaNGe，而不只停留在模拟器或测试平台。

作者随后给出贡献：提出 PiDRAM，这是首个面向 commodity DRAM based PuM 的 flexible end-to-end open-source framework，见 Page 2-3。; 在 FPGA-based RISC-V system 上实现 prototype，并提供 custom memory controller、PuM Operations Controller (POC)、pumolib 与 supervisor software，见 Page 4-7, Figure 2。; 实现 RowClone 端到端支持，包括 memory allocation/alignment 与 coherence 处理，见 Page 8-13, Section 5。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：FPGA prototype; commodity DRAM based PuM; RowClone; D-RaNGe。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 PiDRAM、PuM Operations Controller (POC)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- PiDRAM 的硬件由可扩展 memory controller 和 POC 组成；POC 通过 memory-mapped interface 让软件用普通 LOAD/STORE 触发 PuM operation，见 Page 2, Page 4-6。
- 软件由 pumolib 和 custom supervisor software 组成，前者向应用提供 API，后者提供内存管理与页表相关支持，见 Page 4-7。
- RowClone case study 通过 alloc_align 等机制满足同 subarray/page-granularity 对齐要求，并用 cache flush 处理 coherence，见 Page 8-12。
- D-RaNGe case study 通过 reduced tRCD 访问产生 activation-latency failures，再从硬件 random number buffer 读取随机数，见 Page 13-14。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- RowClone microbenchmark 比较 CPU-copy/initialization、bare-metal RowClone、No Flush RowClone 与包含 CLFLUSH 开销的情形，见 Page 11-13, Figures 9-11。
- D-RaNGe 评估随机数吞吐与延迟，见 Page 13-14, Section 6。
- 实现复杂度用新增 Verilog/C++ 行数衡量，见 Page 1-2 与 Section 7。

主要结果如下：

- Bare-Metal RowClone-Copy 相对 CPU-copy 提升 317.5x-364.8x，RowClone-Initialize 提升 172.4x-182.4x，见 Page 12, Figure 9。
- No Flush 配置中，rcc 在 8 KiB/8 MiB 上分别提升 58.3x/118.5x，rci 分别提升 31.4x/88.7x，见 Page 12, Figure 10。
- 考虑 CLFLUSH 时，0% dirty 情形 rcc/rci 仍有 14.6x/12.6x；50% dirty 时有 3.2x/3.9x；100% dirty 时降至 1.9x/2.3x，见 Page 12, Figure 11。
- D-RaNGe 原型可提供 8.30 Mb/s throughput，并在 220 ns 产生 4-bit random number，见 Page 2 与 Page 14。
- 集成 RowClone 和 D-RaNGe 仅需 388 行 Verilog 与 643 行 C++，见 Page 1-2。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。
- coherence 通过低效 CLFLUSH 实现，dirty cache block 比例升高时收益明显下降，见 Page 12, Figure 11。
- D-RaNGe 控制器未优化，作者说明 TRNG latency 可进一步降低，见 Page 14 footnote。
- 温度、电压控制以及更多安全 primitive 的端到端研究留给未来工作，见 Page 15。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- 如果 coherence 机制由硬件而不是 CLFLUSH 支持，RowClone 端到端收益会提升多少？
- PiDRAM 扩展到 DDR4/DDR5 后，时序违例和内部地址映射问题会发生什么变化？
- 真实 OS 中如何把 PuM allocation 和普通 page allocator 更自然地融合？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：PiDRAM 是一个基于 FPGA/RISC-V 的端到端实验框架，用真实未改动 DDR3 芯片研究 commodity DRAM based PuM 技术的系统集成问题。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
