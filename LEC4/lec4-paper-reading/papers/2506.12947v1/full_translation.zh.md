# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：PuDHammer: Experimental Analysis of Read Disturbance Effects of Processing-using-DRAM in Real DRAM Chips

中文标题：PuDHammer：真实 DRAM 芯片中 Processing-using-DRAM 的读扰动影响实验分析

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：PuDHammer 首次系统表征 multiple-row activation-based PuD operations 对 DRAM read disturbance 的影响，发现 CoMRA/SiMRA 可显著放大类似 RowHammer 的安全与可靠性风险。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：PuD 操作通常需要 consecutive 或 simultaneous multiple-row activation，而现代 DRAM 已知存在 RowHammer/RowPress 等 read disturbance 问题；此前没有工作研究 PuD 多行激活是否会加剧读扰动，见 Page 1。 作者把用于 in-DRAM copy 的 consecutive multiple-row activation 称为 CoMRA，把用于 bitwise operations 的 simultaneous multiple-row activation 称为 SiMRA，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：multiple-row activation-based PuD 是否会比传统 RowHammer 更容易诱发 bitflip。; data pattern、temperature、timing、row-on time、spatial variation 等因素如何影响 PuDHammer。; 现有 TRR/PRAC 类 RowHammer mitigation 能否防住 PuDHammer，代价多大。

作者随后给出贡献：首次在 316 个真实 DDR4 chips、40 个 modules、4 个制造商上表征 PuD 多行激活导致的 read disturbance，见 Page 1-2。; 分别分析 CoMRA 和 SiMRA 的 HCfirst 分布，并与 RowHammer/RowPress 对比，见 Page 5-10。; 分析 RowHammer 与 PuDHammer 组合 access pattern 的效果，见 Page 11, Section 6。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Read disturbance; PuD security/reliability; RowHammer; CoMRA; SiMRA; PRAC mitigation。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 PuDHammer、CoMRA。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- 使用 HCfirst 作为主要 vulnerability metric，即诱发首个 bitflip 所需 hammer cycles；越低表示越脆弱，见 Page 5, Section 4.2。
- CoMRA 实验反复执行 in-DRAM copy 风格的 src/dst 连续激活；SiMRA 实验同时激活 2/4/8/16/32 行并测量 victim rows，见 Page 5-10。
- 作者使用 bisection-method algorithm 搜索每个 victim row 的 HCfirst，并对每行重复 5 次报告最小值，见 Page 5。
- mitigation 部分将 PRAC 扩展到多行同时计数，并提出 area-optimized、performance-optimized 与 weighted counting，见 Page 13-14。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- CoMRA 与 RowHammer 比较、data pattern、temperature、single/double-sided、RowPress、timing delay、copy direction、spatial variation 等实验见 Page 5-8。
- SiMRA 的 double/single-sided、data pattern、temperature、row-on time、voltage、activated row count 等实验见 Page 8-10。
- TRR 与 PRAC mitigation 在真实芯片和 Ramulator 2.0 cycle-level simulation 中评估，见 Page 12-14。

主要结果如下：

- CoMRA 与 SiMRA 分别使最低 HCfirst 相比 RowHammer 低 13.98x 和 158.58x，见 Page 2 与 Page 5/9。
- double-sided CoMRA 中，99% DRAM rows 相比 RowHammer 用更少 activation counts 发生首个 bitflip，见 Page 5-6, Figure 4。
- SiMRA 的数据模式和 row-on time 可使平均 HCfirst 分别变化最高 57.80x 和 270.27x，见 Page 9-10, Figures 14/17。
- RowHammer 与 CoMRA/SiMRA 组合比 RowHammer 单独更有效；三者组合使 average HCfirst 降低 1.66x，见 Page 2 与 Page 11。
- 在开启 TRR 的测试模块中，SiMRA 和 CoMRA 分别比 RowHammer 平均诱发 11340x 和 1.10x 更多 bitflips，见 Page 2 与 Page 12, Figure 24。
- 改造后的 PRAC-PO-WC 对 PuDHammer 的平均/最大性能开销为 48.26%/98.83%；4µs period 下开销为 19.26%，而 naive 方案为 69.15%，见 Page 14, Figure 25。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。
- 作者只 sketch 部分 countermeasures，详细设计和面积/能耗评估留给未来工作，见 Page 13。
- PRAC-PO 的面积开销没有完整评估；多 counter simultaneous update 可能需要大量 incrementers 和 counter access，见 Page 14。
- device-level physical causes 仍需后续研究，见 Page 2 与 Page 14-15。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- 未来支持 PuD 的 DRAM 标准应如何同时保证计算能力和 read disturbance isolation？
- 是否能设计比 PRAC-PO-WC 开销更低的 PuDHammer-specific mitigation？
- PuDHammer 的物理机制与 RowHammer/RowPress 是否相同，还是存在新的耦合路径？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：PuDHammer 首次系统表征 multiple-row activation-based PuD operations 对 DRAM read disturbance 的影响，发现 CoMRA/SiMRA 可显著放大类似 RowHammer 的安全与可靠性风险。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
