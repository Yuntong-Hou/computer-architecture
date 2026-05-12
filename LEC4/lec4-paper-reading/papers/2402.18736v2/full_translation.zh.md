# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Functionally-Complete Boolean Logic in Real DRAM Chips: Experimental Characterization and Analysis

中文标题：真实 DRAM 芯片中的功能完备布尔逻辑：实验表征与分析

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：这篇论文证明部分未改动 COTS DDR4 芯片能够执行 NOT、NAND、NOR 以及多输入 AND/OR，从而在真实 DRAM 中形成 functionally-complete Boolean logic。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：Processing-using-DRAM (PuD) 利用 DRAM 电路的模拟操作特性在内存内部执行大规模 bitwise computation，从而减少 CPU/GPU 与主存之间的数据搬移，见 Page 1, Section 1。 已有真实芯片实验主要展示 MAJ3、AND 和 OR，但还没有在 COTS DRAM 中展示 functionally-complete operation set，例如 NOT 与 NAND/NOR，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：COTS DRAM 芯片是否能执行功能完备的布尔操作集合，而不修改芯片或接口。; 这些操作在不同数据模式、温度、位置、速度等级和 die revision 下是否可靠。; 如何解释 NOT、NAND/NOR 和多输入 AND/OR 在真实 DRAM 中出现的底层原因。

作者随后给出贡献：首次实验展示 unmodified off-the-shelf DRAM chips 能执行 NOT、NAND、NOR，以及多输入 NAND/NOR/AND/OR，见 Page 2。; 在 256 个现代 DDR4 chips、22 个 DRAM modules 上系统表征这些操作的 success rate，见 Page 1-2。; 提出两个底层操作假设：open-bitline sense amplifier 可产生 NOT，操控 reference terminal voltage 可产生 AND/NAND 与 OR/NOR，见 Page 2, Figure 1。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Processing-using-DRAM; functionally-complete Boolean logic; COTS DDR4 characterization。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Functionally-complete Boolean logic、Success rate。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- NOT 的核心假设是：在 open-bitline 架构中，同时连接 sense amplifier 两端的两个 DRAM cell，可利用反相端把一个 cell 的值取反并写入另一个 cell，见 Page 2, Figure 1a 与 Page 7, Section 5.1。
- AND/NAND 与 OR/NOR 的核心假设是：通过初始化 reference-side cells 改变 reference voltage，使 compute-side cells 的电压关系表达 AND 或 OR；相反端自然得到 NAND 或 NOR，见 Page 2, Figure 1b 与 Page 10-11, Section 6.1。
- 作者用 success rate 衡量可靠性，即一个 DRAM cell 在 10000 trials 中正确执行 bitwise operation 的比例，见 Page 1-2 与 Page 8。
- 实验覆盖 row distance、data pattern、temperature、speed rate、chip density 和 die revision 等因素，见 Page 8-14。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- NOT operation 在不同 row distance 和 temperature 下评估，结果见 Page 8-9, Figures 7-10。
- 2/4/8/16-input AND、NAND、OR、NOR 的 success rate 分布见 Page 12, Figure 15。
- data pattern、temperature、speed rate、chip density/die revision 的影响分别见 Page 13-14, Figures 18-21。

主要结果如下：

- COTS DRAM 可执行 NOT，平均 success rate 为 98.37%，见 Page 1-2 与 Page 8-9。
- 16-input AND、NAND、OR、NOR 的平均 success rate 分别为 94.94%、94.94%、95.85%、95.87%，见 Page 12, Figure 15。
- 随机数据模式相比 all-1s/0s 只使 NAND、NOR、AND、OR 平均 success rate 分别下降 1.39%、1.97%、1.43%、1.98%，见 Page 13, Figure 18。
- 温度从 50°C 升到 95°C 时，AND、NAND、OR、NOR 的平均 success rate 最大变化分别为 1.66%、1.65%、1.63%、1.64%，见 Page 14, Figure 19。
- 物理位置、speed rate、chip density 与 die revision 会显著影响 success rate；例如 4-input NAND 在 2133 到 2400 MT/s 间可下降 29.89%，见 Page 13-14, Figures 17/20/21。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。
- 测试芯片最多支持到 16-input Boolean operations；是否能更多输入取决于未公开 row decoder 设计，见 Page 15, Section 7。
- 这些操作依赖违反厂商推荐 timing parameters 和未文档化内部行为，现阶段不等价于标准、可靠的商用功能，见 Page 14-15。
- 论文主要是芯片能力表征，没有完整系统/应用级加速评估。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- 为什么 Micron/Samsung 芯片不完整支持这些操作，是否由命令过滤或 row decoder 设计造成？
- 如果把这些行为正式做进 DRAM 标准，需要增加哪些接口和校验机制？
- 在包含 ECC、refresh、温度变化和真实工作负载的系统里，success rate 能否满足应用要求？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：这篇论文证明部分未改动 COTS DDR4 芯片能够执行 NOT、NAND、NOR 以及多输入 AND/OR，从而在真实 DRAM 中形成 functionally-complete Boolean logic。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
