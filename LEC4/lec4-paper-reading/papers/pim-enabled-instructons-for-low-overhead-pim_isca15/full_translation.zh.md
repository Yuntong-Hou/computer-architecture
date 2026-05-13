# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：PIM-Enabled Instructions: A Low-Overhead, Locality-Aware Processing-in-Memory Architecture

中文标题：PIM-enabled Instructions：低开销、局部性感知的 Processing-in-Memory 架构

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：这篇论文把简单 PIM operations 封装为主机 ISA 中的 PIM-enabled instructions，并用硬件局部性监控在 host-side 和 memory-side 执行之间动态选择，从而兼顾 PIM 带宽优势与 cache locality。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：作者指出早期和现代 PIM 往往需要新的编程模型、非 cacheable memory region 或显式 cache flush，难以无缝接入现有系统，见 Page 1, Section 1。 3D-stacked DRAM/HMC 提供 logic die、TSV 内部高带宽和低能耗传输，但如果所有操作都强制在 memory side 执行，高局部性数据反而会失去 on-chip cache 优势，见 Page 2-3, Sections 2.1-2.2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何让 PIM operation 像普通 host instruction 一样使用，而不是引入全新的 PIM 编程模型。; 如何让 PIM operation 与现有 cache coherence 和 virtual memory 机制兼容。; 如何根据数据局部性动态决定 PEI 在 host processor 还是 memory-side logic 上执行。

作者随后给出贡献：提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。; 提出 single-cache-block restriction，使 PEI 的目标内存范围限制在一个 LLC cache block 内，以简化 localization、coherence 和 locality profiling，见 Page 3-4, Section 3.1。; 设计 PEI Computation Unit (PCU) 与 PEI Management Unit (PMU)，支持 host-side/memory-side PEI execution、atomicity、coherence 和 locality monitoring，见 Page 5-7, Section 4。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Processing-in-memory ISA interface; locality-aware PIM execution; 3D-stacked DRAM。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 PIM-enabled instruction (PEI)、PEI Computation Unit (PCU)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。
- single-cache-block restriction 限制单个 PEI 只访问一个 LLC block，并把 input/output operands 也限制在一个 cache block 内，从而使 coherence、translation 和 locality profiling 都落在现有粒度上，见 Page 3-4。
- PMU 在 LLC 附近维护 PIM directory 与 locality monitor：前者管理 in-flight PEI 的 reader-writer atomicity，后者以 cache-like partial tags 监控目标 cache block 的局部性，见 Page 5-7。
- Locality-Aware policy 根据目标数据是否可能在 cache 中受益，选择 host-side 或 memory-side PCU；balanced dispatch 进一步根据 request/response bandwidth 平衡执行位置，见 Page 9-11。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 在 HMC-based 系统模型上模拟 10 个 workload：图处理、hash join、histogram、R-probe、streamcluster、SVM 等，输入分为 small/medium/large，见 Page 8-9, Table 3。
- 比较 Host-Only、PIM-Only、Ideal-Host 和 Locality-Aware 四种配置，指标包括 normalized IPC、off-chip transfer、multiprogrammed throughput、energy、area 和敏感性，见 Page 9-12。
- PageRank motivation 中用 9 个真实 graph 评估 in-memory atomic add 的收益/风险，见 Page 3, Figure 2。
- multiprogrammed evaluation 随机组合 200 个 workload，测试动态 locality-aware 机制在混合局部性下的表现，见 Page 10, Figure 9。

主要结果如下：

- PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。
- large inputs 中 PIM-Only 相比 Ideal-Host 平均快 44%；small inputs 中 PIM-Only 平均慢 20%，因为即使数据适合 cache 也访问 DRAM，见 Page 9, Figure 6。
- Locality-Aware 在 large inputs 中通过把 79% PEIs offload 到 memory-side，相比 Host-Only 提升 47%；在 small inputs 中通过让 86% PEIs host-side 执行，相比 PIM-Only 提升 32%，见 Page 9, Section 7.1。
- medium graph workloads 中，Locality-Aware 同时利用 host-side 与 memory-side PCUs，分别比 Host-Only 和 PIM-Only 快 12% 和 11%，见 Page 9-10。
- balanced dispatch 在 SC/SVM 上最多进一步提升 25%，见 Page 11, Figure 10。
- Locality monitor storage overhead 为 512KB，即 LLC capacity 的 3.1%；理想化 PIM directory/locality monitor 只分别带来 0.13%/0.31% 性能提升，说明 PMU overhead 很小，见 Page 9 与 Page 11。
- Locality-Aware 在所有输入规模下 memory hierarchy energy 最低；memory-side PCUs 只占 HMC energy 的 1.4%，area overhead 估计为 logic die area 的 1.85%，见 Page 12, Section 7.7。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。
- 软件仍需把目标代码改写为 PEIs；作者认为编译器未来可自动识别，但本文主要假设程序员手动修改，见 Page 4, Section 3.3。
- PEI 与普通 load/store 之间的 atomicity 不是自动保证的，需要 pfence 等同步，见 Page 4, Section 3.2。
- 评估基于模拟 HMC/PCU 模型，真实 HMC/HBM 产品中的接口、timing 和 coherence 支持可能不同。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- single-cache-block restriction 是否会限制现代图分析/数据库中更复杂的 PIM primitives？
- PEI 的 locality monitor 能否迁移到 HBM/CXL memory expander 场景？
- 编译器如何自动识别 PEI 插入点并和 ordinary vectorization/pass ordering 协同？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：这篇论文把简单 PIM operations 封装为主机 ISA 中的 PIM-enabled instructions，并用硬件局部性监控在 host-side 和 memory-side 执行之间动态选择，从而兼顾 PIM 带宽优势与 cache locality。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下按论文结构扩写，覆盖 motivation、3D-stacked DRAM/PIM 背景、PageRank atomic add 例子、PEI abstraction、memory model、PCU/PMU、locality monitor、workloads、evaluation、balanced dispatch、energy/area、related work 和 conclusion。原文中的 Page 3 Figure 2、Page 5-7 PCU/PMU、Page 9-12 评估图是重点。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文提出 PIM-enabled Instructions (PEIs)：把一组简单但高频的数据操作封装为 host processor ISA 的扩展指令，使程序员可以像使用普通指令一样使用 PIM capability。与要求新编程模型、显式数据搬移、非 cacheable memory region 或大规模软件重写的 PIM 方案不同，PEI 试图把 PIM 集成到现有虚拟内存、cache coherence 和主机指令流中。

论文的核心问题是 locality。3D-stacked memory/HMC 提供 logic die 和高内部带宽，适合把数据附近的操作放到 memory side。但如果数据具有强 cache locality，强制把操作 offload 到 memory-side PCU 会绕过 on-chip cache，造成更多 DRAM accesses，反而降低性能。作者因此提出同一条 PEI 可在 host-side PCU 或 memory-side PCU 执行，并由硬件 locality monitor 动态选择执行位置。

PEI 的关键约束是 single-cache-block restriction：一个 PEI 的输入、输出和目标数据限制在一个 LLC cache block 内。这降低了 coherence、atomicity、address translation 和 locality profiling 的复杂度。评估显示 Locality-Aware PEI 在 large inputs 中大量 offload 到 memory-side，在 small inputs 中保留 host-side 执行，从而避免 PIM-only 的反效果。

### 硬件工程师思考
这篇论文非常适合用来纠正“PIM 一定更快”的误解。PIM 的收益取决于数据是否值得离开 cache hierarchy。如果数据已经在 cache 中，host-side SIMD/atomic 可能更好；如果数据分散且必须访问 DRAM，memory-side logic 才有优势。PEI 的价值是把这个选择交给硬件 runtime，而不是由程序员静态决定。

## 1. Introduction / 引言

### 原文位置
Page 1-2, Section 1

### 中文翻译
作者指出，PIM 的历史很长，但推广一直受限。许多 PIM 设计要求程序员显式管理 memory-side operations，或者要求数据放在特殊 non-cacheable regions 中，或者需要手动 flush/invalidate cache。这会破坏现有编程模型，让 PIM 很难被普通软件采用。

3D-stacked DRAM 让 PIM 再次具有吸引力。HMC/HBM 通过 TSV 把 DRAM layers 与 logic layer 连接，提供高内部带宽和较低能耗的数据移动。Memory-side logic 可在数据附近执行简单操作，例如 atomic add、comparison、scatter/gather、reduction 等。

但作者强调，memory-side execution 并非总是好。PageRank 的例子显示，in-memory atomic add 在某些图上最高提升 53%，但在高 cache locality 图上也可导致最高 20% performance degradation，并引起 50x DRAM accesses。根本原因是 PIM-only 会把本可在 cache 中完成的高局部性操作强行送回 memory side。

本文因此提出 PEI：程序只表达“这个操作可由 PIM 加速”，但硬件根据 locality 动态决定在 host-side 还是 memory-side 执行。这样既保留 PIM 的高带宽优势，又避免破坏 cache locality。

### 硬件工程师思考
PEI 的设计思想和现代 heterogeneous execution 很接近：同一语义可在多个 execution sites 执行，调度器根据数据位置和资源状态选择位置。对硬件工程师来说，PIM 不应被设计成“一旦标记就强制 offload”，而应成为 memory hierarchy 中可选择的执行资源。

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 2-3, Section 2; Figure 2

### 中文翻译
背景部分介绍 3D-stacked DRAM 和 PIM。HMC 类架构中，DRAM die 堆叠在 logic die 上，vault controllers 管理多个 vaults/banks。Logic die 可容纳简单 computation units，并通过 TSV 访问 DRAM banks，比 processor 通过 off-chip channel 访问更高带宽、低能耗。

作者分析 PIM 的两个挑战。第一是编程模型。若 PIM 要求程序员显式划分 host code 与 memory-side code，并管理数据移动/同步，使用门槛很高。第二是 locality。即使 memory-side 带宽高，如果目标数据近期在 LLC 中被反复访问，host-side execution 更有利。

PageRank motivation 展示同一 PIM operation 在不同输入图上表现相反。图结构影响 locality；低 locality 图受益于 in-memory atomic add，高 locality 图则因为绕过 cache 而增加 DRAM traffic。这个例子支撑论文的核心判断：PIM execution site 应该根据数据 locality 动态选择。

### 硬件工程师思考
硬件设计中经常出现“平均 workload 有收益”的陷阱。PEI 的 motivation 明确告诉我们：要看输入规模和 locality distribution。Graph workload 尤其敏感，同一个算法在 road network、social graph、web graph 上的 memory behavior 可能完全不同。

## 3. PIM-Enabled Instructions / PEI 抽象

### 原文位置
Page 3-4, Section 3

### 中文翻译
PEI 是 host ISA extension。程序员或编译器把某些普通操作替换为 PEI，例如 atomic add、bitwise operation、comparison 或 reduction-like operation。PEI 的语义对程序可见，但执行地点对程序透明：同一条 PEI 可以由 host-side PCU 或 memory-side PCU 执行。

single-cache-block restriction 是本文最重要的设计约束。每条 PEI 的 memory operands 必须位于同一个 LLC cache block 内，输出也限制在同一 cache block 粒度。这让系统可以用现有 cache block 作为 coherence、locality monitoring 和 data transfer 的基本单位。它也让 PEI 更像一个“cache block 内操作”，而不是任意大范围 memory kernel。

Memory model 方面，PEI 与其他 PEIs 之间可通过硬件保证 reader-writer atomicity；但 PEI 与普通 load/store 之间的顺序和 atomicity 需要程序员使用 pfence 等同步指令。作者认为这种模型类似已有 atomic/SIMD 指令，需要程序或编译器正确插入同步。

Programming interface 方面，本文主要假设程序员手动用 PEI 替换目标代码，但指出未来编译器可识别 PEI-friendly patterns 自动生成 PEIs。

### 硬件工程师思考
single-cache-block restriction 是典型的工程化取舍。它限制了 PEI 表达能力，但让 coherence 和 locality profiling 可控。很多硬件机制要落地，必须先牺牲一部分通用性，把问题限制在现有系统已经理解的粒度上。

## 4. Hardware Support: PCU and PMU / 硬件支持

### 原文位置
Page 5-7, Section 4

### 中文翻译
PEI Computation Unit (PCU) 有两类：host-side PCU 靠近 processor/cache hierarchy，memory-side PCU 位于 3D-stacked memory logic die。二者支持同一组 PEI operations。Host-side PCU 适合处理 cache-resident 或高局部性数据；memory-side PCU 适合处理需要从 DRAM 读取的大量低局部性数据。

PEI Management Unit (PMU) 位于 LLC 附近，负责管理 PEI 请求、atomicity、coherence 和 locality monitoring。PMU 维护 PIM directory，记录 in-flight PEIs 涉及的 cache blocks，防止读写冲突破坏 atomicity。对于 memory-side PEI，PMU 还要确保目标 cache block 的 dirty copy 被写回，避免 memory-side PCU 看到旧数据。

Locality monitor 是 PMU 的核心。它用类似 cache tag 的 partial tags 跟踪目标 cache blocks 的近期 locality。硬件根据 locality monitor 判断某个 PEI 若在 host-side 执行是否可能命中 cache，或者若 offload 到 memory-side 是否会浪费 cache locality。Locality-Aware policy 基于这些信息动态选择执行位置。

作者还提出 balanced dispatch。当 memory-side 和 host-side 都有能力执行 PEI 时，系统不仅考虑 locality，还考虑 request/response bandwidth 和执行资源压力，把部分 PEIs 分配到另一侧以平衡瓶颈。

### 硬件工程师思考
PMU 是 PEI 成败的关键。没有 PMU，PEI 只是新指令；有了 PMU，PEI 才能进入真实 cache-coherent system。工程上要重点检查 PMU 的 critical path、directory capacity、deadlock/livelock、异常/中断、context switch 和 page fault 处理。

## 5. Operations and Workloads / 操作与工作负载

### 原文位置
Page 7-9, Sections 5-6; Table 1; Table 3

### 中文翻译
论文实现了一组简单 PIM operations，覆盖图处理、数据库、机器学习和数据挖掘中的常见模式。例如 atomic add 可用于 PageRank 和 graph analytics；comparison/filter 可用于 database scan；histogram、hash join、R-probe、streamcluster、SVM 等 workload 也能从 PEI 中受益。

实验在 HMC-based system model 上进行，输入规模分为 small、medium、large。这个划分很重要，因为 small inputs 更可能被 cache 捕获，large inputs 更可能持续访问 DRAM。比较配置包括 Host-Only、PIM-Only、Ideal-Host、Locality-Aware 等。

### 硬件工程师思考
PEI 的评估维度设计得很合理：不能只用 large inputs 展示 PIM 好处，也必须用 small inputs 暴露 PIM-only 的风险。做硬件方案评估时，应主动构造对自己不利的 locality cases，否则结论不完整。

## 7. Evaluation Results / 评估结果

### 原文位置
Page 9-12, Section 7; Figure 6-10

### 中文翻译
Performance evaluation 显示，PIM-Only 在 large inputs 上表现好，但在 small inputs 上表现差。large inputs 中，PIM-Only 比 Ideal-Host 平均快 44%；small inputs 中，PIM-Only 平均慢 20%，因为它即使对 cache-friendly 数据也访问 DRAM。

Locality-Aware policy 能同时适应两端。large inputs 中，它将 79% PEIs offload 到 memory-side，相比 Host-Only 提升 47%。small inputs 中，它让 86% PEIs 在 host-side 执行，相比 PIM-Only 提升 32%。medium graph workloads 中，Locality-Aware 同时利用两类 PCUs，比 Host-Only 和 PIM-Only 分别快 12% 和 11%。

多程序评估中，作者随机组合 200 个 workloads，测试混合 locality 情况。Locality-Aware 能在不同应用共存时仍选择合适执行位置，而非被单一静态策略拖累。

Balanced dispatch 在 SC/SVM 等 workload 中最多进一步提升 25%，说明 locality 不是唯一调度目标；当某侧 bandwidth 或 PCU 资源成为瓶颈时，适度分散执行也有价值。

Overhead 方面，locality monitor storage 为 512KB，占 LLC capacity 的 3.1%。理想化无限 PIM directory/locality monitor 只带来 0.13%/0.31% 性能提升，说明实际结构足够接近理想。Memory hierarchy energy 在 Locality-Aware 下最低。Memory-side PCUs 只占 HMC energy 的 1.4%，area overhead 估计为 logic die area 的 1.85%。

### 硬件工程师思考
这部分最重要的是“动态策略胜过静态 PIM-only”。当你在行业里评估 PIM、CXL.mem near-data offload、HBM logic-layer acceleration 时，也应采用类似决策：如果数据在 cache/local memory，留在 host；如果数据分散且搬运昂贵，offload。硬件监控器的准确性和开销决定最终收益。

## 8. Related Work and Conclusion / 相关工作与结论

### 原文位置
Page 12-13, Sections 8-9

### 中文翻译
作者将 PEI 与传统 PIM、atomic memory operations、near-memory processing、3D-stacked memory acceleration 和 SIMD/vector ISA 进行比较。与固定 memory-side AMO 不同，PEI 可在 host 或 memory side 执行；与完整 PIM programming model 不同，PEI 尽量保持 host ISA 和现有软件生态。

结论强调，PEI 通过 ISA extension、single-cache-block restriction、PCU/PMU 和 locality-aware scheduling，在 PIM 带宽优势与 cache locality 之间取得平衡。它让 PIM 更接近可被现有系统采用的形式，而不是要求软件完全重写。

### 硬件工程师复习重点

- Page 3 Figure 2：PIM-only 可正可负，是全文动机核心。
- Page 3-4：single-cache-block restriction 是系统集成关键。
- Page 5-7：PCU/PMU/locality monitor 是硬件实现核心。
- Page 9 Figure 6：small/large input 的反向趋势必须记住。
- Page 11-12：balanced dispatch、energy 和 area 说明 PEI 是否工程可行。

### 对未来工作的启发
PEI 提供一个通用经验：不要让加速器绕过已有层次结构的优势。PIM 的最佳形态可能不是“所有相关操作都下推到内存”，而是让系统根据 locality、带宽、队列压力和一致性成本动态选择执行位置。
