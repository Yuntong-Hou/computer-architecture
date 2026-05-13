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

---

# 2026-05-12 高完整度扩写版

说明：以下按论文主体扩写，覆盖 motivation、functionally-complete Boolean logic、open-bitline NOT 假设、reference-side voltage 操控、实验平台、success rate、data pattern/temperature/speed/die revision 影响、vendor 差异、局限与工程启发。本文是 COTS DDR4 PuD 真实芯片表征论文，建议重点看 Page 2 Figure 1、Page 12 Figure 15、Page 13-14 Figures 18-21。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
这篇论文研究未修改商用 DDR4 DRAM 是否能执行 functionally-complete Boolean logic。已有 PuD/ComputeDRAM/MAJ3 类工作主要展示 row copy、AND、OR 或 majority operation，但如果缺少 NOT 或 NAND/NOR，就难以构成通用布尔计算能力。作者在 256 个 COTS DDR4 chips、22 个 modules 上实验，证明部分芯片可执行 NOT、NAND、NOR 以及多输入 AND/OR/NAND/NOR。

论文提出两个底层物理假设。第一，在 open-bitline sense amplifier 架构中，sense amplifier 的两个互补端天然保存相反值。如果能同时连接相关 cells，就可能把一个 cell 的值取反写入另一个 cell，实现 NOT。第二，通过初始化 reference-side cells 改变 reference terminal voltage，可让 compute-side cells 的结果表现为 AND/OR；互补端自然提供 NAND/NOR。

作者用 success rate 衡量可靠性，即在 10000 trials 中某个 cell 正确执行操作的比例。结果显示，NOT 平均 success rate 为 98.37%；16-input AND/NAND/OR/NOR 的平均 success rate 也在约 95% 左右。但不同厂商、speed grade、density、die revision 和物理位置会显著影响成功率。

### 硬件工程师思考
这篇论文的意义在于把 “DRAM 内逻辑是否 functionally complete” 从修改芯片设计推进到 COTS DDR4 表征。工程上必须注意，它不是标准功能，也不是所有 DDR4 都支持。它更像一种 silicon behavior characterization：可用性取决于 vendor 内部 row decoder、sense amp、open-bitline layout 和 timing guard。

## 1. Introduction / 引言

### 原文位置
Page 1-2, Section 1

### 中文翻译
Processing-using-DRAM (PuD) 试图利用 DRAM 内部模拟电路行为，在数据所在的 DRAM array 中直接执行大规模 bitwise computation，从而减少 CPU/GPU 与主存之间的数据搬移。过去工作已经在真实 DRAM 中展示了一些 primitive，例如 ComputeDRAM 的 AND/OR、Simultaneous Many-Row Activation 的 MAJX、FracDRAM 的 fractional values。但 functionally-complete operation set 仍缺口明显。

作者的核心问题是：不修改 DRAM chip 和接口，是否能在 COTS DRAM 中执行 NOT、NAND、NOR？如果能，PuD 就不再只是特定 AND/OR primitive，而能理论上构造任意 Boolean logic。论文还关注这些操作是否能扩展到多输入逻辑，以及在不同温度、数据模式、芯片位置和产品参数下是否稳定。

本文贡献包括：首次展示 COTS DRAM 中的 NOT/NAND/NOR；系统表征 256 个 DDR4 chips；提出底层操作假设；分析 data pattern、temperature、speed rate、chip density 和 die revision；开源 FCDRAM infrastructure。

### 硬件工程师思考
功能完备性很重要，但不要把它等同于高性能通用计算。Functionally complete 说明“能表达”，不说明“高效、可靠、易编程”。实际系统还要考虑 bit-serial 命令数、数据布局、错误表、ECC、refresh、RowHammer 和调度开销。

## 2. Proposed Operation Mechanisms / 操作机制假设

### 原文位置
Page 2, Figure 1; Page 7-11, Sections 5-6

### 中文翻译
NOT 的物理直觉来自 open-bitline sense amplifier。Open-bitline 结构中，sense amplifier 的两端连接相邻 subarrays 的 bitlines，放大时一端被推高，另一端被推低，形成互补值。若通过特殊时序同时连接两个相关 cells，就可能让一个 cell 读取/写入另一端的反相值。论文将此作为 COTS DRAM 中 NOT 的主要解释。

AND/NAND 和 OR/NOR 的假设与 reference-side voltage 有关。普通感测中，sense amplifier 比较 compute-side cell 导致的 bitline 偏移与 reference-side 电压。若 reference side 由多个初始化 cells 共同影响，则 reference voltage 可被调节。通过选择 reference-side cells 的初值，可以使 compute-side 多输入组合被判定为 AND 或 OR；由于 sense amplifier 两端互补，另一端同时产生 NAND 或 NOR。

多输入逻辑通过同时影响 bitline/reference voltage 扩展。2/4/8/16-input operations 的 success rate 反映出输入数增加后 sense margin 和 timing 控制难度上升，但论文显示部分芯片仍能在 16-input 情况下保持较高平均 success rate。

### 硬件工程师思考
这篇论文的操作不是通过显式数字门实现，而是通过 sense amplifier 的模拟比较边界实现。你应把它理解成“操控比较器输入和参考端”，而不是常规 combinational logic。任何电压噪声、process variation、temperature、内部 timing guard 都可能改变边界。

## 3. Experimental Methodology / 实验方法

### 原文位置
Page 8-14

### 中文翻译
作者使用真实 DDR4 modules 进行实验，总计 256 个 chips、22 个 modules。测试覆盖多家厂商，不同 speed rates、density 和 die revision。每个 operation 通过大量 trials 统计 success rate。Success rate 定义为某 cell 在 10000 次尝试中产生正确结果的比例。

实验变量包括 row distance、physical location、data pattern、temperature、speed grade、chip density 和 die revision。NOT 在不同 row distance 和温度下评估；AND/NAND/OR/NOR 在 2/4/8/16-input 设置下评估；data pattern 比较 all-0/all-1 与 random；temperature 从低到高测试热敏感性。

### 硬件工程师思考
真实芯片表征的价值在于覆盖 variation。单个 module 成功没有说服力，必须看跨 chips、跨 dies、跨 speed bins 的分布。对产品团队来说，最重要的是 worst-case 和 tail behavior，而不是平均 success rate。

## 4. Results / 主要结果

### 原文位置
Page 8-14; Figures 7-21

### 中文翻译
NOT operation 的平均 success rate 为 98.37%。这说明在部分 COTS DDR4 中，open-bitline/sense amplifier 的互补端确实可被特殊时序利用。但 NOT 的成功率受 row distance、位置和厂商内部结构影响，并非均匀分布。

多输入逻辑结果集中在 Page 12 Figure 15。16-input AND、NAND、OR、NOR 的平均 success rate 分别为 94.94%、94.94%、95.85%、95.87%。这说明即使输入数增加到 16，部分 chips 仍可执行高成功率的多输入逻辑。NAND/NOR 的存在尤其重要，因为它们本身就是 functionally complete。

Data pattern 对成功率有影响但不是主导因素。随机数据模式相比 all-1s/0s 只让 NAND/NOR/AND/OR 平均 success rate 下降约 1.39%-1.98%。Temperature 从 50°C 到 95°C 时，AND/NAND/OR/NOR 平均 success rate 最大变化约 1.63%-1.66%，说明这些操作对温度在测试范围内相对稳定。

更显著的影响来自 speed rate、density、die revision 和 physical location。例如 4-input NAND 在 2133 到 2400 MT/s 间可下降 29.89%。这提示内部设计和 timing margin 差异比外部温度/数据模式更关键。

厂商差异非常明显。SK Hynix 支持最完整；Samsung 主要观察到 NOT；Micron 未观察到这些 bitwise operations。这说明不能把 COTS DDR4 看成统一抽象，不同 vendor 的内部保护逻辑和 subarray design 会决定能力。

### 硬件工程师思考
平均 95%-98% success rate 对研究很高，但对计算正确性仍不够。没有 ECC/error correction、bad-cell masking 或重复执行投票，1%-5% 错误率不可用于普通计算。真正可用系统需要 per-bit reliability map、配置筛选、操作重复、或把这些 primitive 用在容错算法中。

## 5. Discussion and Limitations / 讨论与局限

### 原文位置
Page 14-15, Section 7

### 中文翻译
作者明确指出，并非所有厂商芯片都支持这些 operations。某些芯片可能有内部 timing check 或 row decoder 保护，阻止非标准多行/互补端访问。由于商用 DRAM 内部设计不公开，论文只能提出合理假设，不能完全验证电路原因。

当前测试最多到 16-input Boolean operations。是否可扩展到更多输入，取决于 row decoder、sense margin 和 timing precision。本文也没有给出完整系统/应用级加速评估，主要贡献是能力表征。

这些 operations 依赖违反厂商推荐 timing parameters 和未文档化行为，因此不是 JEDEC 标准功能。实际部署还需处理 refresh、ECC、RowHammer、安全隔离、错误恢复和 memory controller support。

### 硬件工程师复习重点

- Page 2 Figure 1：NOT 与 AND/NAND 的物理假设。
- Page 8-9：NOT success rate 与 row distance/temperature。
- Page 12 Figure 15：2/4/8/16-input Boolean success rate。
- Page 13-14 Figures 18-21：data pattern、temperature、speed、die revision 的影响。
- Page 14-15：vendor 差异和不可标准化风险。

### 对未来工作的启发
FCDRAM 告诉我们，COTS DRAM 的真实行为空间比标准接口更丰富。但从“可观察到”到“可依赖”之间还有很长距离。硬件工程上，下一步不是简单扩大 operation set，而是建立可靠性模型、筛选流程、错误控制和系统接口。
