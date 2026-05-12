# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：FracDRAM: Fractional Values in Off-the-Shelf DRAM

中文标题：FracDRAM：在现成商用 DRAM 中存储分数电压值

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：FracDRAM 打破 DRAM 只能存 0/1 的二值抽象，通过特殊时序命令在未修改商用 DRAM 中产生接近 Vdd/2 的 fractional values，并用它增强 majority operation 与构造高吞吐 DRAM PUF。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：DRAM cell 本质是 capacitor，电压可处于 0 到 Vdd 之间；传统接口只把它抽象成 0/1，见 Page 1, Introduction。 ComputeDRAM 已显示 out-of-spec command timing 能在商用 DRAM 中产生新行为；FracDRAM 进一步利用 PRECHARGE 的 Vdd/2 电路，把中间电压作为可用状态，见 Page 1-3。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：是否能在 off-the-shelf DRAM cell 中稳定写入并验证 fractional value。; fractional value 能否扩大 ComputeDRAM-style majority operation 的适用模块范围并提高稳定性。; fractional value 能否构造无需改 DRAM 的高吞吐、环境鲁棒 PUF。

作者随后给出贡献：首次展示在未修改商用 DRAM 中存储 fractional values，见 Page 1-2, Introduction。; 提出 Frac operation，用 ACTIVATE 后立即 PRECHARGE 中断 sense amplification，把整行 cell 拉向 Vdd/2，见 Page 3, Section III-A。; 提出 Half-m operation，通过四行激活与 trailing PRECHARGE 在一行中混合写入 normal 和 Half values，见 Page 3-4, Section III-B。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Fractional DRAM values; off-the-shelf DRAM; F-MAJ; DRAM PUF。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Fractional value、Frac operation。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- Frac operation 先 PRECHARGE bitline 到 Vdd/2，再 ACTIVATE target row，并在 sense amplifier 完全放大前立刻 PRECHARGE 中断，使 cell 保留介于 Vdd/2 与初始值之间的电压，见 Page 3, Figure 3。
- 多次 Frac 会把 cell voltage 更接近 Vdd/2，且更少依赖初始值；Half-m 则通过四行同时打开和中断，在同一 row 生成 weak zero、weak one 与 Half，见 Page 3-4, Figures 3-4。
- 验证 fractional value 不能直接普通 read，因为 read 会破坏/放大它；作者用 retention time 变化和 MAJ3 操作结果间接证明，见 Page 5, Section IV-B。
- F-MAJ 在四行激活中让一行存 fractional value，使其等效调节 charge sharing 的偏置；PUF 则用 10 次 Frac 把 row 拉近 Vdd/2，再读取 sense amplifier variation 形成 response，见 Page 8-12。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 评估 582 个 DDR3 chips，来自 7 个 major vendors，并按 vendor/configuration 分为多个 groups，见 Page 1 与 Page 4-5。
- Frac 评估包括 retention time profile、MAJ3 with fractional value；Half-m 评估包括 retention 与 MAJ3 结果，见 Page 5-8, Figures 6-8。
- F-MAJ 在可四行激活的 groups 上测试 coverage，并在 group B/C 上进行 10000 次随机输入稳定性测试，见 Page 8-10, Figures 9-10。
- PUF 评估用 normalized Hamming Distance、Hamming Weight、NIST random tests，以及不同电压/温度和跨三个月采样，见 Page 10-12, Figures 11-12。

主要结果如下：

- Frac 使平均约 55% cells 的 retention time 随 Frac 次数单调下降，支持其电压被逐步拉向 Vdd/2 的解释，见 Page 6, Figure 6。
- F-MAJ 可在所有能打开四行的 DRAM chips 上执行；group B 最佳配置达到 99.8% coverage，而原始 MAJ3 coverage 为 98.0%，见 Page 9, Figure 9。
- F-MAJ 稳定性测试中，group B 至少 95.4% columns 可可靠执行；in-memory majority 平均错误率从 9.1% 降到 2.2%，见 Page 10, Figure 10。
- Frac-based PUF 中，Intra-HD 最大为 0.051，Inter-HD 最小为 0.27，说明同一模块响应稳定而不同模块区分明显，见 Page 11, Figure 11。
- 在 1.4V 与不同温度、跨 10 天/3 个月的数据中，maximum Intra-HD 仍远低于 minimum Inter-HD，说明 PUF 对环境变化较鲁棒，见 Page 11, Figure 12。
- PUF 响应经 modified Von Neumann extractor 后通过 NIST 15 项 randomness tests；8KB segment evaluation time 为 1.5µs，优化 memory controller 可降到 0.7µs，见 Page 12。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。
- fractional value 的普通 readout 是 destructive，作者指出 Half-m/ternary storage 的 readout 与 data recovery 仍不成熟，见 Page 12, Section VI-C。
- 不同 DRAM groups 偏好的 F-MAJ 配置不同，黑盒商用 DRAM 让原因难以确定，见 Page 9。
- 实验平台主要覆盖 DDR3；DDR4 只在相关工作/潜力中讨论，完整支持仍需更多验证，见 Page 12-13。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- fractional value 如果需要长期保存或可恢复读取，需要怎样的 sense amplifier 或 refresh 支持？
- FracDRAM 在 DDR4/DDR5/HBM 上的可行性与稳定性如何？
- 把 fractional states 用于 ternary computation 或密度提升时，错误模型和 ECC 如何设计？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：FracDRAM 打破 DRAM 只能存 0/1 的二值抽象，通过特殊时序命令在未修改商用 DRAM 中产生接近 Vdd/2 的 fractional values，并用它增强 majority operation 与构造高吞吐 DRAM PUF。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。
