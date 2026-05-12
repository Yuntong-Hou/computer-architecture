# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：ComputeDRAM: In-Memory Compute Using Off-the-Shelf DRAMs

中文标题：ComputeDRAM：使用现成商用 DRAM 的内存内计算

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：ComputeDRAM 证明无需修改商用 DDR3 DRAM 芯片，只要由可编程 memory controller 发出违反 JEDEC timing 的命令序列，就能在部分模块中实现 row copy、AND 和 OR，并进一步构造 bit-serial 计算框架。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：传统 in-memory compute 往往要求修改 DRAM array 或加入额外电路，而 DRAM 行业成本敏感、利润率低，导致这类设计难以商业落地，见 Page 1, Abstract/Introduction。 作者重新审视 memory controller 对 DRAM commands/timing 的控制，发现快速连续 ACTIVATE/PRECHARGE/ACTIVATE 可让多个 rows 在未改动芯片中同时打开并发生 charge sharing，见 Page 3, Section 3。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：是否可以在 off-the-shelf, unmodified, commercial DRAM 中实现 in-memory row copy 与逻辑 AND/OR。; 哪些 vendor/configuration 的 DRAM 能可靠执行这些非标准操作，稳定性受 voltage/temperature 影响如何。; 只具备 non-inverting AND/OR/row-copy primitives 时，如何构造任意 bit-serial computation。

作者随后给出贡献：首次展示在未修改商用 DRAM 中实现 row copy，见 Page 1-2 与 Page 3-4。; 首次展示在未修改商用 DRAM 中实现 bit-wise logical AND 和 OR，见 Page 1-2 与 Page 4-5。; 系统刻画 DDR3 modules from all major DRAM vendors 的可行 timing windows 和可靠性，见 Page 8-11, Figures 10-13。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Off-the-shelf DRAM computation; timing-violating command sequences; bit-serial processing。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 ComputeDRAM、Timing-violating command sequence。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- ComputeDRAM 用 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 等 timing-violating command sequence 让多行在同一 subarray 中同时影响 bitline，从而实现 row copy 或 AND/OR，见 Page 3-5, Figures 3-6。
- row copy 利用短 T2 让 R1 的 bitline 状态覆盖 R2；AND/OR 进一步缩短 T1/T2，使三行 charge sharing，第三行作为常量选择 AND 或 OR，见 Page 3-5。
- 软件框架把每个值和其逻辑反相值一起存储；用 AND/OR 的 De Morgan 关系构造 NAND、XOR 和 ADD，见 Page 6, Equations 2-5。
- 系统通过 SoftMC/FPGA 自定义 memory controller 发出精确命令序列，并用 error table 避免坏 columns/rows，见 Page 7-8, Figure 9。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 实验平台基于 Xilinx ML605 FPGA 和 SoftMC，测试 32 个 DDR3 modules、13 个 DRAM groups，见 Page 8, Section 5。
- exploratory timing scan 在 T1/T2 空间中寻找 row copy 与 AND/OR 成功区域，见 Page 9, Figure 10。
- robustness test 对 row copy 执行 1000 次随机复制，对 AND/OR 执行 10000 次随机操作，并统计 column success ratio，见 Page 10, Figure 11。
- supply voltage 从 1.2V 到 1.6V，temperature 从 30°C 到 80°C，测试环境变化对成功列比例的影响，见 Page 10-11, Figure 12。
- discussion 中估算 bit-serial vector operations 的 cycles、throughput 和 energy efficiency，见 Page 11-12, Table 2。

主要结果如下：

- Figure 10 显示至少存在 off-the-shelf unmodified commercial DRAM modules 可同时执行 row copy 与 logical AND/OR；几乎所有 configuration groups 至少有部分 columns 能执行 row copy，见 Page 9。
- 逻辑 AND/OR 主要在 SKhynix_2G_1333 与 SKhynix_4G_1333B groups 中可跨 subarray 全列执行；SKhynix_4G_1600 也能执行但不是所有 columns，见 Page 9。
- row copy 中，53.9%-96.9% 的 columns 在测试 modules 中达到 100% success ratio；AND/OR 中，92.5%-99.98% columns 达到 100% success ratio，见 Page 10, Figure 11。
- 在合理的 supply voltage variation (±0.1V) 与 temperature 范围内系统可继续工作，但不同 vendor 对 voltage/temperature 的最优 timing 偏好不同，见 Page 11, Section 6.3。
- 单个 DDR3 module 中 row copy 需要 18 memory cycles、peak bandwidth 182 GB/s；8-bit AND/OR 需要 1376 cycles、peak throughput 19 GOPS；8-bit ADD 需要 10656 cycles、peak throughput 2.46 GOPS，见 Page 12, Section 7.1。
- 若数据原本需要从 DRAM 到 CPU 再写回，ComputeDRAM 相比 vector unit 的 energy efficiency 对 row copy 为 347x，对 8-bit AND/OR 为 48x，对 ADD 为 9.3x，见 Page 12, Section 7.2。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。
- 可靠使用需要 error table 排除坏 columns/rows，这会降低可用容量并增加软件/地址转换复杂度，见 Page 6-7 与 Page 10。
- 操作对 voltage/temperature 敏感，实际产品可能需要 binning，以标定哪些模块在什么环境下可靠，见 Page 11, Section 6.3。
- ComputeDRAM 适合 massive vector/bit-serial workloads；单个标量 ADD 需要上千 cycles，不适合低并行度计算，见 Page 12, Section 7.1。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- DDR4/DDR5 是否仍保留类似可利用的 timing-violation 行为，还是控制逻辑会过滤这些命令？
- error table、binning 与温度/电压监控的系统成本是否会抵消无需改 DRAM 的优势？
- 如何把 ComputeDRAM 的不稳定 primitive 包装成可由 OS/编译器安全使用的接口？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：ComputeDRAM 证明无需修改商用 DDR3 DRAM 芯片，只要由可编程 memory controller 发出违反 JEDEC timing 的命令序列，就能在部分模块中实现 row copy、AND 和 OR，并进一步构造 bit-serial 计算框架。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
