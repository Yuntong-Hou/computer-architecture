# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Proteus: Enabling High-Performance Processing-Using-DRAM with Dynamic Bit-Precision, Adaptive Data Representation, and Flexible Arithmetic

中文标题：Proteus：通过动态位精度、自适应数据表示和灵活算术实现高性能 Processing-Using-DRAM

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：现有 PUD 多采用 bulk bit-serial execution model，用固定 two's complement 和固定 bit-precision 处理整行数据，导致大量 inconsequential bits 被无谓计算，见 Page 1-2。 PUD 还面临 throughput-oriented execution 难隐藏低并行场景下的单操作延迟，以及高精度操作延迟随 bit-width 线性或二次增长的问题，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。; 如何在 PUD operation 内并行执行独立 in-DRAM primitives，缓解单操作延迟。; 如何为不同 bit-precision 自动选择最合适的 data representation 和 arithmetic algorithm。

作者随后给出贡献：提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。; 利用 narrow values 动态降低 PUD operation bit-precision，减少 latency 和 energy，见 Page 2。; 利用 SALP 将一个 data word 的不同 bits 分散到多个 subarrays，跨 bit 并行执行独立 primitives，见 Page 2 与 Page 4-5。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Dynamic bit precision; PUD arithmetic; redundant binary representation; runtime µProgram selection。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Dynamic bit-precision、Narrow values。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。
- Parallelism-Aware µProgram Library 保存不同 bit-precision、two's complement/RBR、bit-serial/bit-parallel 算法的 µPrograms 及 cost model LUTs，见 Page 2 与 Page 8-10。
- µProgram Select Unit 在发出 PUD operation 时查询 bit-precision 和 cost LUT，选择最低延迟或最低能耗的 µProgram，见 Page 2 与 Page 8-10。
- Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 使用 12 个真实应用，来自 Phoenix、Polybench、Rodinia、SPEC2017；系统配置见 Page 12, Tables 2-3。
- 比较 CPU、A100 GPU、SIMDRAM-SP、SIMDRAM-DP、Proteus LT/EN with static/dynamic precision，见 Page 12-13。
- 额外分析 data mapping/representation conversion overhead、floating-point synthetic throughput、GPU tensor cores 对比和面积开销，见 Page 13-14。

主要结果如下：

- Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。
- SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。
- Dynamic Bit-Precision Engine 使 Proteus 相比 static bit-precision 性能提升 46%，energy consumption 降低 58%，见 Page 12-13, Figures 11-12。
- Proteus 平均比 CPU/GPU/SIMDRAM 分别降低 90.3x、21x、8.1x energy consumption，见 Page 1 与 Page 13。
- 在 int8/int4 GEMM-heavy workloads 上，Proteus 相对 A100 tensor cores 提供 20x/43x performance per mm² 和 484x/767x performance per Watt，见 Page 14, Figure 14。
- 面积开销低：DRAM chip 1.6%，CPU die 0.03%，见 Page 1 与 Page 14-15。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。
- baseline PUD substrate 不支持 floating-point，浮点评估使用 synthetic analysis 而非完整真实应用，见 Page 13-14。
- Proteus 依赖 Ambit、LISA、SALP 等底层机制，真实硬件实现需要这些机制可靠可用，见 Page 14-15。
- 动态 bit-precision 需要对象追踪、转置缓冲和元数据维护；短任务上的 runtime/metadata 开销仍需进一步验证。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- Proteus 与 MIMDRAM 是否可以结合，同时解决位精度和资源粒度问题？
- 如果应用包含大量 floating-point 或不规则数据结构，Proteus 的收益还剩多少？
- 动态 bit-precision metadata 在多线程、多进程和虚拟内存环境中如何维护一致性？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下按 Proteus 论文结构扩写，覆盖 bit-serial PUD 短板、dynamic bit precision、SALP-based bit parallelism、redundant binary representation、Dynamic Bit-Precision Engine、Parallelism-Aware µProgram Library、µProgram Select Unit、evaluation、floating-point synthetic analysis、tensor core comparison、area/limitations。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
Proteus 解决 bulk bitwise PUD 的数据不敏感问题。传统 SIMDRAM/Ambit-style PUD 通常使用固定 two's complement representation 和固定 bit-width 对整行数据执行 bit-serial operations。若实际数据值很窄，例如高位只是 leading zeros 或 leading ones，系统仍会对所有 bits 执行同样长的 computation，浪费 latency 和 energy。

Proteus 提出 data-aware hardware runtime framework。它在数据转置到 PUD vertical layout 时检测每个对象实际需要的 bit precision；在执行 PUD operation 时，根据 bit precision、data representation 和 cost model 选择最低延迟或最低能耗的 µProgram。它还使用 SALP 将一个 data word 的不同 bits 分布到多个 subarrays，从而并行执行部分 bit-level primitives。

为支持高精度 arithmetic，Proteus 引入 redundant binary representation (RBR)，减少 carry propagation 带来的串行依赖。它通过 Parallelism-Aware µProgram Library 保存不同 bit-width、representation 和算法实现，并由 µProgram Select Unit 动态选择。

### 硬件工程师思考
Proteus 的核心不是新的 DRAM primitive，而是 runtime adaptation。它说明 PUD 的性能瓶颈已经从“能不能在 DRAM 中算”转向“能不能按数据特征选择合适算法”。这和 CPU/GPU 上的 mixed precision、sparsity、dynamic quantization 思路一致。

## 1. Motivation / 动机

### 原文位置
Page 1-2

### 中文翻译
Bit-serial PUD 的延迟随 bit-width 增长，某些操作甚至随 bit-width 二次增长。固定 32-bit 或 64-bit precision 会让许多低有效位宽数据承担不必要成本。数据中常见 narrow values，例如 small integers、quantized ML tensors、indices、counters、sparse metadata 等。

另一个问题是单操作 latency。PUD 通常依靠 massive throughput 摊薄延迟，但当并行度不足或操作链有依赖时，bit-serial latency 会变成瓶颈。Proteus 因此尝试在 operation 内部并行执行独立 primitives，并根据 bit-width 选择更适合的 representation。

### 硬件工程师思考
动态位宽优化在硬件中常见，但在 PUD 中更重要，因为每多一位都可能意味着多轮 DRAM commands。对 memory-side arithmetic，避免无用高位计算往往比提升单个 primitive 速度更有效。

## 2-4. Proteus Mechanisms / 机制

### 原文位置
Page 4-10

### 中文翻译
Dynamic Bit-Precision Engine 在 LLC evicted cache lines 被转置为 PUD vertical layout 时扫描对象，记录实际所需 bit precision。它可识别 leading zeros/ones，记录对象元数据，供后续 PUD operation 查询。这样 runtime 不必每次 operation 重新扫描数据。

SALP-based bit parallelism 将一个 data word 的不同 bits 分布到多个 subarrays。某些 bit-level primitives 彼此独立，可在不同 subarrays 并行执行，从而降低单 operation latency。但这要求数据 mapping 与 subarray organization 协调，也依赖 SALP 允许多个 subarrays 并发激活。

Redundant Binary Representation (RBR) 用冗余位表示数值，减少 carry propagation。传统 two's complement addition/multiplication 中，carry 依赖会造成串行链；RBR 可将部分 carry 延迟或局部化，使高精度 arithmetic 更适合 PUD。

Parallelism-Aware µProgram Library 保存不同 bit-precision、representation 和算法版本的 µPrograms，并为每个版本维护 latency/energy cost model LUT。µProgram Select Unit 在发出 PUD operation 时查询 bit precision 和 cost LUT，选择 Proteus-LT（最低延迟）或 Proteus-EN（最低能耗）策略下的最优 µProgram。

### 硬件工程师思考
Proteus 的硬件复杂度主要在元数据和选择逻辑，而不在 DRAM array。工程上要关注 bit-precision metadata 的生命周期、对象粒度、cache eviction/transposition 时机、metadata consistency，以及错误时如何 fallback 到保守 precision。

## 5. System Substrate / 系统基础

### 原文位置
Page 10-12

### 中文翻译
Proteus 建立在 Ambit、LISA、SALP 等底层机制之上。Ambit 提供 MAJ/NOT 或 bulk bitwise primitive，LISA 支持数据移动，SALP 提供 subarray-level parallelism。Proteus control unit 和 data transposition unit 负责在这些机制之上执行动态 µProgram。

软件侧需要标记 PUD-friendly loops 和 fixed-point data arrays。论文尚未提供完全自动编译器，因此真实应用需要手动修改。Proteus 也主要支持 fixed-point/integer；floating-point 评估以 synthetic analysis 为主。

### 硬件工程师思考
Proteus 的收益依赖底层 PuD substrate 全部可靠可用。若 Ambit/LISA/SALP 任一机制在真实芯片中不可用或可靠性不足，Proteus 的 runtime 再聪明也无法落地。这类 layered architecture 要逐层验证。

## 6-7. Evaluation / 评估

### 原文位置
Page 12-15; Figures 11-14

### 中文翻译
评估使用 12 个真实应用，来自 Phoenix、Polybench、Rodinia、SPEC2017。比较对象包括 CPU、A100 GPU、SIMDRAM-SP、SIMDRAM-DP、Proteus LT/EN with static/dynamic precision。

Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别提供 11.2x、4.8x、6.8x。SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus 的 µProgram adaptation 又在 SIMDRAM-DP 上提升 1.6x。

Dynamic Bit-Precision Engine 相比 static precision 提升性能 46%，降低 energy 58%。整体上，Proteus 平均比 CPU/GPU/SIMDRAM 分别降低 90.3x、21x、8.1x energy consumption。

在 int8/int4 GEMM-heavy workloads 上，Proteus 相对 A100 tensor cores 提供 20x/43x performance per mm² 和 484x/767x performance per Watt。需要注意，这是特定低精度、data movement dominated 场景下的 per-area/per-watt 对比，不代表 Proteus 在所有 ML workload 中胜过 tensor cores。

面积开销低：DRAM chip 约 1.6%，CPU die 约 0.03%。这主要因为 Proteus 重用既有 PuD substrate，新增的是 runtime metadata/control structures。

### 硬件工程师思考
Proteus 的评估要看 metric。performance per mm²/per Watt 很亮眼，但绝对 latency、数据准备、转置、metadata 和应用修改成本也要看。对行业应用，Proteus 更适合低精度、内存驻留、批量 bit-serial 运算，而不是 GPU tensor cores 擅长的 dense compute pipeline 全场景替代。

## Limitations and Conclusion / 局限与结论

### 原文位置
Page 14-15

### 中文翻译
局限包括：真实应用需要手动标记 PUD-friendly loops；floating-point 支持不是完整真实应用评估；动态 bit precision 需要对象追踪和元数据；短任务或频繁变化对象上的 metadata overhead 需要进一步验证；底层 Ambit/LISA/SALP 必须可靠。

结论强调，Proteus 用 data-aware runtime 降低 PUD arithmetic 的 latency/energy。它根据数据实际位宽、representation 和 parallelism 选择 µProgram，使 PUD 不再固定执行一种 bit-serial 算法。

### 硬件工程师复习重点

- Page 1-2：inconsequential bits 是核心浪费来源。
- Page 4-5：哪些 primitive 可并行，哪些受 carry 依赖限制。
- Page 6-10：Dynamic Bit-Precision Engine 和 µProgram Library 是方法核心。
- Page 12-14：注意 performance per area/watt 的适用场景。

### 对未来工作的启发
Proteus 说明 PuD 未来需要 runtime specialization。硬件工程师可以把它看作 DRAM 内计算的“动态编译/调度层”：根据数据值、精度和目标优化指标选择执行方案，而不是静态绑定算法。
