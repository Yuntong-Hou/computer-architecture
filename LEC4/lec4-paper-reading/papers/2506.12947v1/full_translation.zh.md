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

---

# 2026-05-12 高完整度扩写版

说明：以下按 PuDHammer 论文结构扩写，覆盖 motivation、CoMRA/SiMRA 定义、HCfirst metric、真实 DDR4 表征、RowHammer/RowPress 对比、data pattern/temperature/voltage/timing/row-on time、组合攻击、TRR bypass、PRAC countermeasures、limitations。本文是 PuD 安全可靠性补充论文，建议和 FCDRAM/Many-Row Activation 一起读。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
PuDHammer 研究 multiple-row activation-based PuD operations 是否会加剧 DRAM read disturbance。现代 DRAM 已知存在 RowHammer：反复激活 aggressor rows 会在相邻 victim rows 中诱发 bitflips。PuD 操作为了实现 row copy 或 bitwise logic，常常需要 consecutive 或 simultaneous multiple-row activation。这些访问模式可能比传统 RowHammer 更强烈扰动相邻 cells。

作者将用于 in-DRAM copy 的连续多行激活称为 CoMRA，将用于 bitwise operations 的同时多行激活称为 SiMRA。论文在 316 个 DDR4 chips、40 个 modules、4 个制造商上系统测试，发现 CoMRA 与 SiMRA 可显著降低诱发首个 bitflip 所需 hammer cycles (HCfirst)，其中 SiMRA 风险尤其高。

论文还测试 data pattern、temperature、timing delay、row-on time、voltage、spatial variation，并分析 RowHammer 与 PuDHammer 组合的效果。最后，作者评估 TRR/PRAC 类 mitigation，发现现有 in-DRAM TRR 可能被绕过，而扩展 PRAC 虽可防护但性能开销很高。

### 硬件工程师思考
PuDHammer 是对 PuD 能力论文的必要反面。前面很多论文证明“多行激活能算”；这篇提醒“多行激活也可能更危险”。任何将 PuD 放入产品的计划，都必须把 read disturbance 作为一等设计约束，而不是事后补丁。

## 1. Background and Definitions / 背景与定义

### 原文位置
Page 1-4

### 中文翻译
RowHammer 是反复激活 aggressor rows 导致邻近 victim rows bitflips 的现象。RowPress 则强调 row-on time，即行保持打开时间过长也可能加剧扰动。现代 DRAM 使用 TRR 等 mitigation，但实际防护能力有限且 vendor-specific。

PuDHammer 定义两类 PuD-triggered disturbance。CoMRA (consecutive multiple-row activation) 来自 in-DRAM copy 类操作，例如连续打开 source/destination rows。SiMRA (simultaneous multiple-row activation) 来自 bitwise/majority operations，同时打开多行进行 charge sharing。

主要指标是 HCfirst：诱发第一个 bitflip 所需 hammer cycles。HCfirst 越低，表示 vulnerability 越高。作者用 bisection-method algorithm 搜索 victim row 的 HCfirst，并对每行重复 5 次取最小值，以捕获最脆弱情况。

### 硬件工程师思考
HCfirst 是比“总 bitflips”更保守的安全指标，因为攻击者只需要第一次错误就可能利用。做硬件安全评估时，tail vulnerability 比平均值更重要。

## 2. CoMRA Characterization / CoMRA 表征

### 原文位置
Page 5-8

### 中文翻译
CoMRA 实验反复执行 in-DRAM copy 风格的 source/destination 连续激活，并观察 victim rows 的 bitflips。作者比较 single-sided 和 double-sided 模式、data pattern、temperature、RowPress、timing delay、copy direction 和 spatial variation。

结果显示，CoMRA 的最低 HCfirst 相比传统 RowHammer 低 13.98x。Double-sided CoMRA 中，99% DRAM rows 相比 RowHammer 用更少 activation counts 发生首个 bitflip。这说明 PuD copy primitive 的访问模式比普通 RowHammer 更容易触发 disturbance。

Data pattern 和温度会影响 CoMRA，但不是唯一因素。Physical location/spatial variation 也重要，说明某些 rows/subarrays 天然更脆弱。

### 硬件工程师思考
RowClone 类机制如果被频繁用于 copy/zeroing，不能只看性能。它们可能改变 row activation pattern，使原本安全的 refresh/TRR 假设失效。OS 或 controller 需要限制同一区域连续 PuD copy 的频率。

## 3. SiMRA Characterization / SiMRA 表征

### 原文位置
Page 8-10

### 中文翻译
SiMRA 实验同时激活 2/4/8/16/32 行，测试 victim rows。结果比 CoMRA 更严重：最低 HCfirst 相比 RowHammer 低 158.58x。SiMRA 的 data pattern 和 row-on time 影响极大，平均 HCfirst 可分别变化最高 57.80x 和 270.27x。

SiMRA 同时打开多个 rows，使 bitline 和相邻 cells 经历更复杂、更强的电气扰动。随着 activated row count 和 row-on time 增加，victim rows 更容易产生 bitflips。Voltage/temperature 也有影响，但在论文报告中不如 row-on time 和 pattern 显著。

### 硬件工程师思考
SiMRA 是 Ambit/MAJX/FCDRAM 类 bitwise PuD 的核心操作，因此这部分直接影响所有基于 simultaneous activation 的方案。若没有专门 mitigation，高性能 PuD logic 可能同时成为高强度 RowHammer primitive。

## 4. Combination Patterns and TRR Bypass / 组合模式与 TRR 绕过

### 原文位置
Page 11-12

### 中文翻译
作者测试 RowHammer、CoMRA、SiMRA 组合 access pattern。结果显示，组合比单独 RowHammer 更有效；三者组合使 average HCfirst 降低 1.66x。这说明攻击者可能把传统 hammering 和 PuD operations 组合，形成更强 disturbance pattern。

在开启 TRR 的测试模块中，SiMRA 和 CoMRA 分别比 RowHammer 平均诱发 11340x 和 1.10x 更多 bitflips。尤其 SiMRA 能显著绕过某些 in-DRAM TRR mitigation，因为 TRR 可能只跟踪传统 row activation pattern，而不理解 PuD 多行激活的真实扰动强度。

### 硬件工程师思考
这是安全影响最强的结果。Mitigation 不能只数标准 ACTIVATE；必须理解 PuD command 语义，按实际同时受扰 rows 更新 counters。否则新功能会绕过旧防护。

## 5. Countermeasures / 防护

### 原文位置
Page 13-14

### 中文翻译
作者提出三类 countermeasure，并重点改造 PRAC。Naive 方案可对每个被激活/受影响 row 都计数，但多行同时更新会带来大量 counter accesses 和 incrementers，性能开销高。

优化方案包括 area-optimized、performance-optimized 和 weighted counting。Weighted counting 根据不同 PuD operation 的扰动强度给不同权重，而不是简单把每行激活视为相同事件。PRAC-PO-WC 在 4us period 下性能开销为 19.26%，比 naive 69.15% 低很多；但平均/最大开销仍可达 48.26%/98.83%，说明防护代价很高。

### 硬件工程师思考
PuD mitigation 的难点是计数规模。SiMRA 一次操作可能影响多行和邻近 victim rows，如果每个都更新 counter，带宽和面积都会爆炸。实际方案需要在安全性、性能、面积和误报之间折中。

## 6. Limitations and Conclusion / 局限与结论

### 原文位置
Page 14-15

### 中文翻译
论文表征的是当前 COTS DRAM 中非标准 PuD 操作。未来如果 DRAM 正式支持 PuD，电路和 mitigation 可能不同。但这不削弱结论：多行激活本身会改变 read disturbance 风险，必须被设计者考虑。

作者承认 countermeasure 仍是 sketch，详细面积/能耗评估、device-level physical causes、transient error 影响等需要后续研究。结论强调，PuD 能力与可靠性/安全风险必须一起评估。

### 硬件工程师复习重点

- Page 1-2：CoMRA/SiMRA 定义。
- Page 5 Figure 4：CoMRA 相比 RowHammer 的 HCfirst 风险。
- Page 9 Figures 13-14：SiMRA/data pattern 风险。
- Page 12 Figure 24：TRR bypass 是最关键安全证据。
- Page 13-14 Figure 25：mitigation 性能代价很高。

### 对未来工作的启发
PuDHammer 给所有 PuD 设计一个硬性要求：任何利用 multiple-row activation 的机制，都必须在论文和产品设计中同时给出 disturbance model 与 mitigation。性能收益不能脱离可靠性和安全成本单独评估。
