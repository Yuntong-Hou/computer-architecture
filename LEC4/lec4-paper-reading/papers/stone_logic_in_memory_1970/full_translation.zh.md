# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：A Logic-in-Memory Computer

中文标题：一种 Logic-in-Memory 计算机

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：Stone 1970 提出把带组合逻辑的 memory array 作为高速 cache，使主存对程序表现得像由多个 logic-in-memory sectors 组成，从而以 sector-level 并行操作提升性能。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：作者从 1970 年的微电子趋势出发：未来封装成本可能更多由 pins 而非 gates 决定，因此在 memory array 中增加逻辑可能具有经济吸引力，见 Page 1, Introduction。 论文借鉴 IBM 360/85 cache、Atlas virtual memory 和 Wilkes slave memory，把 logic-in-memory array 嵌入 cache 层，而不是把每个 array 当作孤立功能单元，见 Page 2, Section I-II。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何把 cellular logic-in-memory arrays 嵌入通用计算机系统，而不是仅作为孤立 associative memory 或特殊功能单元。; 如何让主存看起来拥有 logic-enhanced cache 的处理能力和接近 cache 的性能。; 如何设计 sector-level operations 和程序控制，使高并行 memory-side logic 对程序可见。

作者随后给出贡献：提出以 logic-enhanced cache memory array 为中心的 logic-in-memory computer 组织，见 Page 1, Abstract 与 Page 3。; 把操作组织为 sectors 上的 parallel operations，包括 associative search、tag bit operations、sector add、sector scale、sector multiply/copy，见 Page 3-4。; 指出 cache/control mechanism 可让主存对程序表现得像每个 sector 都是 independent logic-in-memory array，见 Page 3-4。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Early logic-in-memory architecture; logic-enhanced cache; sector operations。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Logic-in-memory array、Logic-enhanced cache。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- 基础组织是 cache-organized computer：CPU 请求先到 cache，miss 时把主存 sector 调入 cache；如果 cache sector 是 logic-in-memory array，CPU 就能对逻辑增强 sector 发出操作，见 Page 2-3, Figure 1。
- sector operations 以一个或两个 sector 为粒度，例如 Search on Masked Equality/Threshold、Copy Tag Bit、Tag Bit AND/OR/XOR/NOT、Sector ADD/Scale，见 Page 3-4。
- sector add 可用一组 adders 服务所有 cache sectors，通过 cache output/input buses 和寄存器 R 完成对应 words 的并行加法，见 Page 4, Figure 2。
- program control 可显式 hold/release sectors、提示 sequential data、控制 cache load 方式；bit-slice mode 则让 cache 同时装入许多 words 的同一 bit slice，以支持 mass arithmetic，见 Page 4-5。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 本文是概念性 Short Notes，没有现代意义上的原型实现或 benchmark evaluation。
- 作者引用 IBM 360/85 cache 模拟结果：超过 95% CPU memory requests 命中 cache，整体性能达到“整个主存都像 cache 一样快”的机器的 80%，见 Page 3, Section II。
- 论文用 qualitative reasoning 分析 microelectronics cost、pin limitation、cache sector operations 和 programming-language support，见 Page 1-6。

主要结果如下：

- 摘要声称 logic-in-memory computer 由于 high-speed, highly parallel sector operations，指向 orders-of-magnitude performance increase 的新方向，见 Page 1, Abstract。
- IBM 360/85 相关模拟显示 cache hit 超过 95%，总性能达到理想高速主存机器的 80%，且 cache 只有主存的几个百分点大小，见 Page 3, Section II。
- 作者认为若 microelectronic cost 足够下降，masked equality search 这类每 bit 少量 gates 的功能已可实现，sector add/multiply 等更复杂功能未来也可能合理，见 Page 4。
- bit-slice access 可使一个 sector 同时容纳 m×n 个 words 的一位，从而用 AND/OR/XOR/NOT 在 cache 中做 mass arithmetic，例如 m×n simultaneous additions，见 Page 5。
- 结论强调该机器是 general-purpose by nature，但实际价值取决于 microelectronics 进步、适配算法和高层语言能否暴露新 instructions，见 Page 5-6。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。
- 可行性强依赖当时对 microelectronic packaging/pin/gate cost 的预测，见 Page 1 和 Page 4。
- 作者明确指出 instruction repertoire 的实际 utility 难以衡量，是 future research，见 Page 4。
- 高层语言与 unconventional instruction repertoire 不匹配，若编译器目标语言只用普通指令，强大 memory-side instructions 难以带来实际收益，见 Page 6。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- Stone 的 sector operation 抽象和现代 SIMDRAM/PEI 的 ISA abstraction 有哪些共同点和差异？
- 如果把 logic-enhanced cache 换成现代 HBM logic layer 或 near-cache accelerator，哪些设计仍成立？
- 高层语言如何自然表达 memory-side sector/bit-slice operations，这个问题在现代 PIM 编译器中如何解决？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：Stone 1970 提出把带组合逻辑的 memory array 作为高速 cache，使主存对程序表现得像由多个 logic-in-memory sectors 组成，从而以 sector-level 并行操作提升性能。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
