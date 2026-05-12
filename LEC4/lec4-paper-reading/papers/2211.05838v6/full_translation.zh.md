# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips

中文标题：DRAM Bender：用于便捷测试先进 DRAM 芯片的可扩展 FPGA 基础设施

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：DRAM Bender 提供无接口限制、易用、可扩展的 FPGA DRAM 测试基础设施，使研究者能对 DDR3/DDR4 芯片发出任意低层 DRAM 命令并开展 RowHammer 与 in-DRAM computation 实验。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：理解 DRAM scaling、RowHammer、retention failures 与 undocumented functionality 必须测试真实芯片；普通系统 memory controller 不允许任意违反 timing parameters，见 Page 1, Section 1。 现有开源平台 SoftMC 和 LiteX RowHammer Tester 存在接口限制、难用或难扩展问题，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何完全暴露 DRAM command/data interface，让实验程序自由安排 ACT/PRE/READ/WRITE 与时序。; 如何让非 HDL 专家通过 C++/Python 快速写 DRAM 实验。; 如何支持新的 FPGA board 和 DDR3/DDR4/未来接口，避免测试平台快速过时。

作者随后给出贡献：提出 DRAM Bender，拥有 nonrestrictive instruction set architecture、C++/Python API 和 modular FPGA design，见 Page 1-2 与 Page 4-8。; 在五种 FPGA board 上实现 DDR4/DDR3 支持，并说明移植到新板只需较小代码修改，见 Page 2 与 Page 8。; 通过 RowHammer interleaving pattern 发现 double-sided attack 有效性强依赖 aggressor activation/precharge 顺序，见 Page 9-11。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：DRAM testing infrastructure; FPGA; RowHammer; DDR4; in-DRAM bitwise operations。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 DRAM Bender、RowHammer。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- DRAM Bender 通过 FPGA 直接连接 DRAM PHY/DFI，提供 program memory、data buffers、readback FIFO、periodic operation scheduler 等模块，见 Page 4-7, Section 3。
- 用户用 C++/Python 构造 command sequence，可加入 label、branch、loop 与精细 timing，随后在 FPGA 上执行并读回结果，见 Page 6-9, Section 3.5。
- 案例研究分别构造 double-sided RowHammer、多种 data pattern 和 in-DRAM AND/OR 实验，用真实 DDR4 module 观测 bit flips 与 BER，见 Page 9-12。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 测试 Micron、Hynix、Samsung 三类 DDR4 module，模块信息见 Page 10, Table 6。
- RowHammer interleaving study 扫描 T=1 到 64K，总 ACT command 数固定为 1M，见 Page 9-10。
- in-DRAM bitwise study 测量不同 reduced timing 组合下 AND/OR 的 bit error rate，见 Page 12, Figure 12。

主要结果如下：

- double-sided RowHammer 中 T 越接近 1，bit-flips 越多；V2 行在 T=64K 时三家厂商平均 bit-flips 为 31.9/9.9/71.2，而 T=1 时为 314.8/50.7/604.9，见 Page 10, Figures 8-9。
- HCfirst 也受 interleaving 影响：T=1 时为 99K/80K/16K，T=64K 时为 130K/108K/23K，见 Page 10-11, Figures 10-11。
- DRAM Bender 支持的数据模式能发现更多 victim-row bit-flips，见 Page 11-12, Section 4.2。
- DDR4 芯片支持 in-DRAM AND/OR，但没有发现 0% BER segment；35 个 segment 在 <3% BER 下只支持 AND，最小 AND BER 为 1.9%，160 个 segment <5% BER，4546 个 segment <10% BER，见 Page 12, Figure 12。
- RowHammer 实验可用 12 行 C++ 编写，bulk bitwise AND/OR 可用 3 行 C++ 编写；移植到另一 FPGA board 只需约 230 行 Verilog 和 30 行 C++，见 Page 2。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。
- 功耗测量 setup 仍在进行中，尚未完整发布，见 Page 13, Section 7。
- packetized interfaces 的 3D-stacked DRAM 可能无法完全暴露低层 DRAM interface，限制 DRAM Bender 的适用性，见 Page 13-14。
- GUI 只是未来方向，目前仍偏向程序化实验，见 Page 14。
- in-DRAM AND/OR 在 DDR4 上存在 BER，不能直接当作可靠计算机制，见 Page 12。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- DDR5 RFM 是否能真正缓解 RowHammer，DRAM Bender 扩展后能否系统验证？
- DDR4 in-DRAM AND/OR 的 BER 是否能通过数据布局、温度、电压或选择 segment 降到可用范围？
- DRAM Bender 与 PiDRAM 是否可以组合，既做底层 characterization 又做端到端应用评估？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：DRAM Bender 提供无接口限制、易用、可扩展的 FPGA DRAM 测试基础设施，使研究者能对 DDR3/DDR4 芯片发出任意低层 DRAM 命令并开展 RowHammer 与 in-DRAM computation 实验。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
