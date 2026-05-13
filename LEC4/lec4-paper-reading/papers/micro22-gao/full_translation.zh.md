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

---

# 2026-05-12 高完整度扩写版

说明：以下扩写按原文 Page 1-13 结构重新整理，覆盖 fractional values 的动机、Frac/Half-m primitives、验证方法、真实芯片评估、F-MAJ、Frac-based PUF、其他用途、相关工作与结论。参考文献不逐条翻译。由于 fractional value 无法普通读出，Page 5-8 的验证逻辑尤其重要，建议结合原图 Figure 6-8 阅读。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
FracDRAM 的核心思想是：DRAM cell 本质上是 capacitor，不只能保存逻辑 0 或逻辑 1，也可以处在 0 到 Vdd 之间的中间电压。传统 DRAM 接口会在 read 时把 cell 放大为 0/1，因此系统通常看不到这些中间状态。作者提出用特殊 timing command sequence 在 off-the-shelf, unmodified DRAM 中生成并利用 fractional values。

论文提出两个 primitive。Frac operation 用 ACTIVATE 后立即 PRECHARGE 的方式打断 sense amplification，使整行 cells 被拉向 Vdd/2 附近的 fractional voltage。Half-m operation 用四行同时激活和 trailing PRECHARGE，在一行中对 masked bits 生成 Half value、weak zero 或 weak one。作者用 retention time profile 和 MAJ3 with fractional value 间接证明 fractional values 的存在，因为普通 read 会破坏这些状态。

基于 fractional values，作者展示两个主要用例。第一，F-MAJ 用 fractional row 参与四行激活，把四行 charge sharing 转化为 majority-of-three，扩展 ComputeDRAM-style majority operation 到更多 DRAM modules，并把 average majority error rate 从 9.1% 降到 2.2%。第二，Frac-based PUF 通过多次 Frac 把 cell 拉近 Vdd/2，再由 sense amplifier variation 决定读出 0/1，生成稳定且可区分的 device response。

### 硬件工程师思考
FracDRAM 的意义在于打破“DRAM cell 是二值存储”的抽象。对电路工程师来说，cell 电压本来连续；对系统来说，它被接口离散化。FracDRAM 把连续电压状态暴露为可利用资源。但这种资源是 destructive、环境敏感、难直接读出的，因此更适合做辅助 primitive、PUF 或可靠性调节，而不是直接替代常规二值存储。

## 1. Introduction / 引言

### 原文位置
Page 1-2, Section I

### 中文翻译
作者从 DRAM capacitor 的物理性质出发。一个 DRAM cell 存 1 时接近 Vdd，存 0 时接近 0，但这只是逻辑抽象。实际电压可以位于中间，例如 Vdd/2 附近。PRECHARGE 电路本来就会把 bitlines 拉到 Vdd/2；如果在 activation 或 restoration 完成前打断操作，cell 可能保留一个中间电压。

ComputeDRAM 已经证明，违反 DRAM timing specification 的 command sequence 可以在未修改商用 DRAM 中触发 row copy 和 majority-like behavior。FracDRAM 进一步提出：不仅可以让多个 rows charge sharing，还可以把 fractional voltage 当作新的工具，用于控制 charge sharing 结果或生成 PUF response。

本文贡献包括：首次在未修改商用 DRAM 中展示 fractional value storage；提出 Frac 和 Half-m 两个 primitive；用真实 582 个 DDR3 chips 进行实验；用 fractional values 扩展和稳定 in-memory majority；提出无需修改 DRAM 的高吞吐 PUF。

### 硬件工程师思考
这篇文章是 ComputeDRAM 的自然延伸：ComputeDRAM 用 out-of-spec timing 产生“多行同时影响 bitline”；FracDRAM 用 out-of-spec timing 产生“介于 0/1 之间的 cell voltage”。前者偏计算 primitive，后者偏模拟状态控制。两者都提示：控制器时序和 DRAM 模拟状态之间有丰富交互。

## 2. Background / 背景

### 原文位置
Page 2-3, Section II; Figure 2

### 中文翻译
背景部分回顾 DRAM cell、bitline、sense amplifier 和 PRECHARGE。bitline 被 precharge 到 Vdd/2 后，ACTIVATE 打开 wordline，让 cell 与 bitline 共享电荷。若 cell 初始为 1，bitline 略高于 Vdd/2；若为 0，略低于 Vdd/2。sense amplifier 随后将这个小偏移放大到完整 Vdd 或 0，并把 cell 恢复为对应逻辑值。

作者还说明 true cells 和 anti-cells 的区别。不同 cell layout 中，逻辑 1 对应的物理电压可能相反。为了简化讨论，论文在处理后按 true-cell 语义描述，即 1 对应高电压，0 对应低电压。

背景还回顾 ComputeDRAM 的 multiple-row activation。ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 之间不留 idle cycles 时，可能同时打开多行，产生三行或四行 charge sharing。FracDRAM 的 Half-m 和 F-MAJ 都基于这个能力。

### 硬件工程师思考
Fractional value 的读出是 destructive，这是理解全文的关键。普通 READ 会启动 sense amplifier，把中间值强行推到 0 或 1，同时原 fractional state 消失。因此作者不能直接“读出电压”，只能用 retention 或 majority behavior 间接证明。

## 3. Primitive Operations / Frac 与 Half-m

### 原文位置
Page 3-4, Section III; Figure 3-4

### 中文翻译
Frac operation 的流程是：先让 bitline 处于 precharged Vdd/2；然后 ACTIVATE target row，使 cell 和 bitline 开始 charge sharing；在 sense amplifier 完全放大前立即 PRECHARGE，打断 activation/restoration。此时 cell 没有被恢复到完整 Vdd 或 0，而是被拉向 Vdd/2 附近。如果初始为 1，Frac 后电压位于 Vdd 和 Vdd/2 之间；如果初始为 0，电压位于 0 和 Vdd/2 之间。

多次 Frac 会让 cell 电压更接近 Vdd/2，并且逐渐减弱对初始值的依赖。作者把一次 Frac 的 command cost 估为 7 memory cycles。需要注意的是，Frac 作用于整行；它适合生成整行 fractional values。

Half-m operation 目标是在一行中对部分 bits 生成 Half value，而不是整行统一处理。它利用四行同时激活和 trailing PRECHARGE。通过在四行中为某列设置两 1 两 0，charge sharing 后该列可接近 Vdd/2；若四行全 1 或全 0，则产生 weak one 或 weak zero。这样可以在同一 row 中混合 normal/weak/fractional states。Half-m 的难点是需要四行同时激活，因此只适用于支持这种行为的 DRAM groups。

作者还讨论 refresh。Fractional values 不是普通长期存储状态，refresh/read 都会破坏或改变它们。应用必须在 64ms refresh window 内使用，且避免对含 fractional values 的 row 做普通 refresh。

### 硬件工程师思考
Frac 是“整行模拟偏置生成器”，Half-m 是“带 mask 的部分中间值生成器”。它们都不是常规写操作，不能用普通 memory consistency 模型理解。工程上要关心：哪些 rows 暂存 fractional values、多久必须消费、是否会被 refresh controller 破坏、读出后是否可恢复、ECC 是否会误认为数据错误。

## 4. Evaluation Methodology and Verification / 实验方法与验证逻辑

### 原文位置
Page 4-5, Section IV; Figure 5; Table I

### 中文翻译
实验平台基于 SoftMC 和 Xilinx ML605 FPGA，通过 PCIe 连接 host，FPGA 控制 DDR3 module。命令周期为 2.5ns。作者测试 582 个 DDR3 chips，来自七个 vendors/模块品牌，并按 group A-L 分类。不同 group 对 Frac、three-row activation、four-row activation 的支持不同。

Fractional value 不能直接读取，因此作者设计两类间接验证。第一是 retention time profile。对于高电压 cell，初始电压越高，泄漏到被读作 0 所需时间越长。如果 Frac 让 cell 电压从 Vdd 降向 Vdd/2，则 retention time 应随 Frac 次数增加而下降。

第二是 MAJ3 with fractional value。作者把同样的 fractional value 放入两个 operands，再让第三个 operand 分别为 1 或 0，执行 MAJ3。如果 fractional value 确实接近 Vdd/2，那么它对多数结果的影响应介于 0/1 之间，表现为特定的 X1/X2 组合。这个方法可以证明 fractional state 是否在几乎所有 bits 上可重复生成，并且可测试初始值为 0 和 1 的情况。

### 硬件工程师思考
验证方法比 primitive 本身更值得学。对于无法直接观测的模拟状态，作者没有简单声称“我们写入了 Vdd/2”，而是用 retention 和后续逻辑行为作为侧证。这是硬件实验论文的关键能力：把不可见状态转化为可测量结果。

## 5. Evaluation of Frac and Half-m / Frac 与 Half-m 评估

### 原文位置
Page 5-8, Section V; Figure 6-8

### 中文翻译
Retention experiment 中，作者在每个 chip 中随机采样 rows，先写入全 1，再执行 0-5 次 Frac，随后测 retention time。Figure 6 将 retention time 分成多个范围：0、0-10min、10-30min、30-60min、1-12h、>12h。对于 groups A-I，约 55% cells 平均表现出 retention time 随 Frac 次数单调下降。这支持 Frac 将 cell voltage 逐步拉向 Vdd/2 的解释。

作者也说明 retention 方法的限制。第一，只在平均 55% cells 上清晰证明，因为很多 cells retention time 超过 12h，实验时间无法继续细分。第二，retention 受 process variation、环境和 variable retention time 影响。第三，charge leakage 只能从高电压向低电压观察，因此 retention 方法主要验证初始值为 1 的情况。

MAJ3 experiment 补足这些限制。在 group B 上，作者把 fractional values 放入不同 row 组合，并测试初始值全 1 或全 0。结果显示，执行两次或更多 Frac 后，预期的 X1=1/X2=0 组合成为唯一结果，说明 fractional values 可以在几乎所有 bits 中稳定生成，并且初始值为 0 或 1 都可工作。

Half-m evaluation 只在 group B 详细进行，因为其他 groups 对 MAJ3 支持有限。retention profile 显示 Half values 与多次 Frac 生成的 fractional values 有相似分布；但 MAJ3 结果显示只有约 16% bits 能生成可区分 Half value。weak one/weak zero 质量较好。作者因此把 Half-m 定位为 proof-of-concept：它显示同一 row 中可生成三种可区分状态，但 readout 和稳定性尚不足以作为成熟多值存储。

### 硬件工程师思考
这里需要区分“存在性证明”和“工程可用”。Frac 在 group B 上表现稳定，F-MAJ/PUF 也有清晰用途；Half-m 只有约 16% bits 可区分，更多是未来多值存储方向的探索。不要把 Half-m 解读成已经可直接把 DRAM 容量提升到 ternary storage。

## 6A. F-MAJ: Extending Majority Operation / 用 fractional value 扩展 majority

### 原文位置
Page 8-10, Section VI-A; Figure 9-10

### 中文翻译
ComputeDRAM 的 MAJ3 只在少数 SK hynix DDR3 groups 上可靠工作，因为它依赖三行同时激活。FracDRAM 发现另一些 groups 更自然地打开四行，而不是三行。如果直接四行 charge sharing，普通 majority-of-three 不成立。F-MAJ 的想法是让第四行保存 fractional value，使它接近 Vdd/2，对 bitline 影响最小，从而让其余三行决定结果。

F-MAJ 流程是：选择四条可同时打开的 rows；将其中一行用 Frac 写成 fractional value；将三个 operands 写入其余三行；执行 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2)，四行同时参与 charge sharing，最终结果写入所有四行。

F-MAJ 的额外开销是生成 fractional row。若按 ComputeDRAM 的 reserved-row 方式执行，F-MAJ 比原始 MAJ3 多约 29% memory cycles。但它能让支持四行激活的 modules 也执行 majority-of-three，并可能扩展到 DDR4。

Figure 9 显示 F-MAJ coverage 随 Frac 次数、fractional row 位置和初始值变化。不同 groups 偏好不同 configuration，例如 group C 更适合在 R1 放大于 Vdd/2 的 fractional value，group D 偏好 R4 和小于 Vdd/2 的 fractional value。由于商用 DRAM 是黑盒，作者用实验结果选择最佳配置。

对 group B，最佳 F-MAJ coverage 达到 99.8%，高于原始 MAJ3 的 98.0%。原因是原始 MAJ3 中三行并非完全同时打开，总有 primary row 对 bitline 影响更大。将 fractional value 放在影响过强的位置可增强操作对称性。稳定性测试中，group B 至少 95.4% columns 可可靠执行 F-MAJ，平均 majority error rate 从 9.1% 降到 2.2%。

### 硬件工程师思考
F-MAJ 是 FracDRAM 最有工程意义的部分。它不是为了存储三值数据，而是用 fractional value 调节模拟计算的偏置，让原本不稳定/不可用的 majority primitive 更可靠或适用范围更广。这种思想类似 analog calibration：用一个可控中间状态补偿电路不对称。

## 6B. Frac-Based PUF / 基于 Frac 的物理不可克隆函数

### 原文位置
Page 10-12, Section VI-B; Figure 11-12

### 中文翻译
PUF 接收 challenge，基于设备制造差异生成 response。理想 PUF 对同一设备同一 challenge 稳定，对不同设备 response 区分明显，并且 response 近似随机。DRAM 很适合 PUF，因为容量大、地址空间天然提供大量 challenge-response pairs。

已有 DRAM PUF 使用 start-up values、retention failures 或降低 timing 参数，但常有 evaluation time 长、环境敏感、需要 error correction 等问题。CODIC-based PUF 通过修改 DRAM substrate，把 cell 驱到 Vdd/2，再由 sense amplifier variation 决定读出结果，具有较好特性，但需要硬件修改。FracDRAM 用多次 Frac 在未修改 DRAM 中近似实现这个过程。

Frac-based PUF 的 challenge 是 memory segment 地址和大小，response 是读出的数据。作者固定 segment length 为 8KB，即一条 row。流程是：选择 bank/row，写入全 1；执行 10 次 Frac，让 cell voltage 接近 Vdd/2；读取整行。由于 sense amplifier threshold 和电路制造差异，不同 modules 会把这些接近 Vdd/2 的 cells 放大成不同 0/1 pattern。

评估使用 Intra-HD 和 Inter-HD。Intra-HD 表示同一 module 对同一 challenge 多次 response 的 Hamming Distance，理想接近 0；Inter-HD 表示不同 modules response 之间的 Hamming Distance，理想接近 0.5。Figure 11 显示所有 Intra-HD 都集中在接近 0，最大约 0.051；Inter-HD 最小约 0.27，明显大于 Intra-HD，说明稳定性和区分性良好。部分 groups 的 Hamming Weight 偏离 0.5，导致原始 response 有 bias。

作者在 10 天后以 1.4V 重新采集 response，又在 3 个月后不同温度下采集。Figure 12 显示 maximum Intra-HD 仍远低于 minimum Inter-HD，说明环境变化下仍可区分。随机性方面，作者使用 modified Von Neumann extractor 去 bias，再用 NIST 15 项 random tests 测试，全部通过。8KB segment evaluation time 约 1.5us，优化 controller 后可降到 0.7us。

### 硬件工程师思考
PUF 是 FracDRAM 最接近应用落地的场景，因为它不要求 fractional value 长期保存，也不需要恢复原数据；它只需要生成稳定但设备特异的 response。工程上要继续考虑 enrollment、helper data、环境范围、aging、攻击者是否可重复查询、response privacy，以及 memory region 是否能隔离给 PUF 使用。

## 6C. Other Uses / 其他用途

### 原文位置
Page 12, Section VI-C

### 中文翻译
作者讨论 fractional values 的其他可能用途。第一是扩展 DRAM storage capability。Half-m 理论上可在 cell 中表示 zero、one、Half 三种状态，形成 ternary bit。但目前 readout 机制不成熟，需要四份数据辅助 MAJ3 读取，且读取会破坏 fractional value，作者将 data recovery 留给未来工作。

第二是辅助 retention-time characterization。通过不同 Frac 次数、Half-m 初始值或打断多行激活，可以生成不同电压水平，进而测量泄漏过程，推断 cell retention behavior。

第三是 reverse-engineering DRAM design parameters，例如 sense amplifier threshold。fractional values 提供了探测比较器边界和内部电路差异的工具。

### 硬件工程师思考
这些用途更偏研究工具。对实际产品，PUF 和 F-MAJ 比 ternary storage 更现实。若要做多值 DRAM，必须解决非破坏读取、刷新、ECC、温度漂移和良率，这远超本文范围。

## 7-8. Related Work and Conclusions / 相关工作与结论

### 原文位置
Page 12-13, Sections VII-VIII

### 中文翻译
作者把 FracDRAM 与 near-memory/in-memory/with-memory computing、DRAM timing violation、ComputeDRAM、DRAM PUF、QUAC-TRNG、多值 DRAM 等工作比较。FracDRAM 与 ComputeDRAM 共享 out-of-spec timing 思路，但扩展为 fractional storage；与 CODIC PUF 目标相似，但不需要修改 DRAM substrate；与过去 weak value/降低 latency 工作不同，FracDRAM 将中间电压明确作为新的逻辑状态。

结论强调，本文提出并评估两个 primitive，可在整行或 masked bits 中存储 fractional values。作者首次在 off-the-shelf, unmodified DRAM chips 中展示 fractional value storage 和 destructive readout。Fractional values 可扩展 majority operation 到更多 modules、降低 existing majority error rate，也可构造高吞吐 DRAM PUF。

### 硬件工程师复习重点

- Page 3-4：Frac/Half-m 的命令序列和物理直觉。
- Page 5-8：retention time 与 MAJ3 验证方法，理解为什么不能直接 read fractional value。
- Page 8-10：F-MAJ 如何用 fractional row 抵消四行激活/不对称激活问题。
- Page 10-12：PUF 评估中的 Intra-HD、Inter-HD、Hamming Weight、NIST tests。
- 工程上必须记住：fractional values 是 destructive、短期、环境相关状态，不能当普通可靠数据位使用。

### 对未来工作的启发
FracDRAM 最值得带走的思想是“用模拟中间态校准数字 primitive”。在 DRAM、SRAM、NVM 或高速 SerDes 中，很多边界状态通常被规避；但如果能被控制、验证、隔离和建模，它们可能成为安全、测试、校准或近数据计算的新工具。工程落地时，关键不是发现状态，而是为状态建立可靠使用边界。
