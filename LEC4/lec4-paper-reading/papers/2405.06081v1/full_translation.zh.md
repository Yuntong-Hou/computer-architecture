# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Simultaneous Many-Row Activation in Off-the-Shelf DRAM Chips: Experimental Characterization and Analysis

中文标题：商用 DRAM 芯片中的同时多行激活：实验表征与分析

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：这篇论文表征了 COTS DDR4 中 simultaneous many-row activation，证明真实芯片可同时激活最多 32 行、执行 MAJ5/7/9，并将一行并发复制到最多 31 行。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：PUD 操作常依赖 multiple-row activation；此前真实芯片工作主要研究两行、三行或四行激活，尚不清楚更多行是否能被稳健地同时激活，见 Page 1-2。 作者提出 Q1-Q5，系统询问 many-row activation 的可行性、可实现操作、鲁棒性、改善方式以及 data pattern/temperature/voltage/timing 的影响，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：COTS DRAM 是否能稳健地同时激活超过四行，甚至 32 行。; 这种能力能否实现 MAJX 和 Multi-RowCopy 等新的 PuD operations。; 如何提高 MAJX 成功率，并理解数据模式、温度、电压和 timing 对可靠性的影响。

作者随后给出贡献：在 120 个 COTS DDR4 chips 上展示可同时激活 2/4/8/16/32 行，见 Page 2 与 Section 4。; 展示 MAJ5、MAJ7、MAJ9 以及 Multi-RowCopy：将一行内容同时复制到最多 31 行，见 Page 2, Sections 5-6。; 提出 input replication 能显著提升 MAJX success rate，见 Page 2 与 Page 10, Section 7.2。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Simultaneous many-row activation; MAJX; Multi-RowCopy; COTS DDR4 characterization。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Simultaneous many-row activation、MAJX。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- 作者用 DRAM Bender 精细调度 ACT/PRE 等命令，违反标准 timing parameters，以触发 simultaneous many-row activation，见 Page 3-5。
- MAJX 通过同时激活奇数个输入行实现多数函数；Multi-RowCopy 通过多行同时激活把一个源行并发写入多个目标行，见 Page 5-9。
- input replication 把 MAJX 输入操作数的多个副本放到所有激活行中，提高 bitline voltage perturbation 的 sensing margin，见 Page 10, Section 7.2。
- success rate、温度、电压、data pattern 和 row decoder 假设共同用于解释真实芯片行为，见 Page 4-10。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 测试 120 个 DDR4 chips、18 个 DRAM modules，来自两个主要制造商；部分 Samsung 芯片作为限制讨论，见 Page 2 与 Page 12。
- MAJ3/5/7/9 与 Multi-RowCopy 的可靠性在多种 timing、data pattern、temperature、voltage 下评估，见 Sections 4-7。
- 七个 microbenchmarks 包括 AND/OR/XOR/ADD/SUB/MUL/DIV；cold-boot prevention 比较 RowClone、Frac 和 Multi-RowCopy，见 Page 10-12, Section 8。

主要结果如下：

- COTS DRAM 可同时激活最多 32 行；MAJ3/MAJ5/MAJ7/MAJ9 平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%，见 Page 2。
- 将一行复制到 1/3/7/15/31 个目标行的平均 success rate 分别为 99.996%、99.989%、99.998%、99.999%、99.982%，见 Page 2。
- MAJ3 使用 32-row activation 并复制每个输入 10 次时，平均 success rate 比 4-row activation 高 30.81%，见 Page 1-2 与 Page 10。
- data pattern 对 MAJX 与 Multi-RowCopy 的平均影响分别为 11.52% 和 0.07%；temperature/voltage 变化导致最大 success rate 变化为 2.13%/1.32%，见 Page 1-2。
- MAJ5/7/9 在七个 microbenchmarks 中相对 MAJ3 平均提升 121.61% (Mfr. M) 和 46.54% (Mfr. H)，见 Page 11, Figure 16。
- Multi-RowCopy content destruction 相对 RowClone 和 Frac 最多分别加速 20.87x 和 7.55x，见 Page 11-12, Figure 17。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。
- 当前只能控制 consecutive two-row activation 或 simultaneous 2/4/8/16/32-row activation，无法任意选择激活行数，可能受 1.5ns timing granularity 限制，见 Page 12。
- PUD operations 对 transient errors 的潜在影响没有完全探索，见 Page 12。
- MAJ9 在某些厂商上因 success rate 差可能导致性能退化，见 Page 11。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- 能否设计标准化 DRAM 接口，让行数和 row group 更可控地执行 SiMRA？
- MAJ9 等低 success rate 操作是否能通过 input replication、ECC 或重试策略变得实用？
- simultaneous many-row activation 是否会加剧 read disturbance，这与 PuDHammer 论文直接相关。

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：这篇论文表征了 COTS DDR4 中 simultaneous many-row activation，证明真实芯片可同时激活最多 32 行、执行 MAJ5/7/9，并将一行并发复制到最多 31 行。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下扩写覆盖 simultaneous many-row activation 的研究问题、DRAM Bender 实验方法、MAJX、Multi-RowCopy、input replication、data pattern/temperature/voltage/timing 影响、microbenchmarks、cold-boot prevention case study、limitations。本文与 FCDRAM/PuDHammer 关系紧密。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文系统表征 COTS DDR4 中 simultaneous many-row activation。此前真实芯片研究主要关注两行、三行或四行激活，而本文询问：真实 DDR4 能否同时激活更多行，例如 8、16、32 行？如果能，是否可以实现更高输入数的 majority operation 和并发复制？

作者使用 DRAM Bender 精细控制 ACT/PRE 等命令，违反标准 timing parameters，触发 multiple-row activation。实验覆盖 120 个 COTS DDR4 chips。结果显示，部分芯片可同时激活最多 32 行；可执行 MAJ5、MAJ7、MAJ9；也可将一行内容同时复制到最多 31 个目标行，即 Multi-RowCopy。

论文还提出 input replication。通过在多行激活中放置多个输入副本，可增强 bitline voltage perturbation 和 sensing margin，从而提高 MAJX success rate。作者进一步分析 data pattern、temperature、voltage、timing delay、row-on time 和激活行数对可靠性的影响。

### 硬件工程师思考
这篇文章展示 COTS DDR4 中 row decoder/timing 边界的能力上限，但也暴露可靠性随输入数急剧下降。它告诉我们：更多行激活带来更强表达能力和并发复制能力，但 analog margin 会变窄，必须用 replication、筛选和错误控制支撑。

## 1. Motivation and Questions / 动机与问题

### 原文位置
Page 1-2

### 中文翻译
PuD operations 常依赖 multiple-row activation。Ambit/ComputeDRAM/FCDRAM 使用三行或少量多行激活来实现 majority/AND/OR/NAND/NOR。但如果能同时激活更多行，就能实现 MAJ5/7/9，减少 bit-serial logic depth；也能一次将 source row 复制到多个 destination rows，加速数据初始化或安全清除。

作者提出 Q1-Q5：COTS DRAM 是否能 simultaneous activate many rows？能实现什么 operations？这些 operations 鲁棒性如何？能否通过 input replication 改善？data pattern、temperature、voltage、timing 如何影响？

### 硬件工程师思考
多行激活不是越多越好。它增加可表达性，但每个 cell 对 bitline 的贡献更小，sense margin 更难控制。硬件设计需要在 operation count reduction 和 reliability degradation 之间折中。

## 2. Methodology / 实验方法

### 原文位置
Page 3-5

### 中文翻译
作者使用 DRAM Bender 对 DDR4 modules 发出低层命令，控制 ACTIVATE/PRECHARGE 的时序间隔。通过缩短命令间隔，DRAM 内部可能在尚未完全关闭前打开更多 rows，从而产生 simultaneous many-row activation。

实验使用 success rate 衡量操作正确性，并在不同 row counts、data patterns、temperatures、voltages、row-on times 和 timing delays 下测试。MAJX 需要奇数输入行，输出为多数值；Multi-RowCopy 则让 source 行影响多个 destination rows，使源数据并发写入多个目标。

### 硬件工程师思考
这类实验高度依赖 controller timing resolution。论文也承认当前只能控制 2/4/8/16/32-row 等模式，无法任意选择激活行数，可能受 1.5ns timing granularity 限制。对实验平台能力的理解会影响结论解释。

## 3. MAJX and Multi-RowCopy / 多输入 majority 与多行复制

### 原文位置
Page 5-10

### 中文翻译
MAJX 是 MAJ3 的扩展，同时激活 X 条输入行，让 sense amplifier 输出 X 个输入的多数值。论文报告，MAJ3/MAJ5/MAJ7/MAJ9 的平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%。随着输入数增加，成功率快速下降，说明多行 charge sharing 的电压 margin 变小。

Multi-RowCopy 利用多行同时激活，将一行复制到多个目标行。复制到 1/3/7/15/31 个目标行的平均 success rate 分别为 99.996%、99.989%、99.998%、99.999%、99.982%。这说明复制场景比 MAJX 更可靠，因为源行数据可强力主导目标写入，逻辑判断边界更简单。

Input replication 是提高 MAJX 的核心方法。对于 MAJ3，可在 32-row activation 中复制每个输入多次，例如每个输入放 10 个副本。这样多数关系在电荷共享中被放大，平均 success rate 相比 4-row activation 提升 30.81%。这类似模拟投票中的权重放大。

### 硬件工程师思考
Multi-RowCopy 比 MAJX 更接近工程可用，因为可靠性高且用途明确。MAJX 虽能减少逻辑层数，但高输入数成功率很低；实际系统可能更应使用 MAJ3/MAJ5 加 replication，而不是盲目追求 MAJ9。

## 4. Robustness Factors / 鲁棒性因素

### 原文位置
Page 7-10

### 中文翻译
Data pattern 对 MAJX 影响较大，平均可改变 11.52%；对 Multi-RowCopy 影响只有 0.07%。原因是 MAJX 的输出取决于多个输入组合的细微电压差，而 copy 操作主要由源数据覆盖目标。

Temperature 和 voltage 在测试范围内影响较小，最大 success rate 变化分别约 2.13% 和 1.32%。Row-on time、timing delay 和激活行数则会显著影响可靠性。尤其 row-on time 会影响 cell/bitline 共享与 sense amplifier 放大的持续时间。

某些 Samsung 芯片未观察到同一 subarray 中多于一行同时激活，因此不支持测试 PuD operations。这再次说明 COTS DRAM 行为高度 vendor-specific。

### 硬件工程师思考
数据模式敏感性是实际计算的大问题。若某 operation 对 random input 的错误率比 all-0/all-1 高很多，benchmark 中用简单 pattern 会高估可靠性。真实系统必须用应用真实数据分布评估。

## 5. Applications and Limitations / 应用与局限

### 原文位置
Page 10-12, Sections 8-9; Figures 16-17

### 中文翻译
作者用七个 majority-based microbenchmarks 分析 MAJ5/7/9 的潜在收益，包括 AND/OR/XOR/ADD/SUB/MUL/DIV。MAJ5/7/9 相比 MAJ3 可减少 operation depth，在部分厂商上平均提升 121.61% 或 46.54%。但当 MAJ9 success rate 太低时，性能可能因错误恢复或不可用而下降。

Cold-boot attack prevention case study 比较 RowClone、Frac 和 Multi-RowCopy。Multi-RowCopy 可把某一内容快速写入大量 rows，用于内容破坏或清除，最多相对 RowClone 加速 20.87x，相对 Frac 加速 7.55x。

局限包括：部分芯片不支持；无法任意控制行数；transient errors 和物理原因仍需研究；更多行激活可能带来 read disturbance 风险，这正是 PuDHammer 等后续安全研究关注的问题。

### 硬件工程师复习重点

- Page 1-2：Q1-Q5 和 summary answers。
- Page 5-9：MAJX vs Multi-RowCopy，注意成功率差异。
- Page 10：input replication 是改善 MAJX 的关键。
- Page 11：microbenchmarks 显示高输入 MAJ 的潜在收益与风险。
- Page 12：vendor limitation 和 row-count controllability 是实际边界。

### 对未来工作的启发
Many-row activation 让 DRAM 内 primitive 更强，但也更接近可靠性和安全边界。未来设计应把 operation synthesis、input replication、error model 和 disturbance mitigation 一起考虑，而不是孤立追求更多同时激活行。
