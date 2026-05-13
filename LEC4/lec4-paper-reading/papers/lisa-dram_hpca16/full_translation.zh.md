# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：Low-Cost Inter-Linked Subarrays (LISA): Enabling Fast Inter-Subarray Data Movement in DRAM

中文标题：LISA：用低成本互连 subarray 实现快速 DRAM 子阵列间数据移动

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：LISA 在相邻 DRAM subarray 的 bitlines 之间加入低成本 isolation transistors，使 row buffer movement 能跨 subarray 快速传输整行数据，并由此支持快速 copy、in-DRAM cache 和更短 precharge latency。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：bulk data movement 在 OS 和应用中很常见，但传统 memcpy 需要经由窄 off-chip channel；RowClone 虽能在 DRAM 内复制，但快速路径受限于同一 subarray，见 Page 1, Section 1。 作者观察到 subarray 内 bitlines 天然是极宽的数据通路，且相邻 subarrays 物理距离很近；LISA 的关键是把这些 bitlines 用低成本 link 接起来，见 Page 2-3, Section 3。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何让不同 subarray 之间也能像同一 subarray 内那样快速移动整行数据。; 如何以低面积开销提供新的 DRAM substrate，而不是为每个应用单独设计复杂机制。; 如何把快速 inter-subarray movement 用于 copy、caching 和 precharge 等多个场景。

作者随后给出贡献：提出 Low-Cost Inter-Linked SubArrays (LISA)，在相邻 subarrays 的 bitlines 间加入 isolation transistors，见 Page 2-4, Section 3。; 提出 Row Buffer Movement (RBM)，让已激活 row buffer 驱动相邻 precharged row buffer，从而跨 subarray 移动数据，见 Page 4, Section 3.2。; 提出 LISA-RISC，用 RBM 实现 Rapid Inter-Subarray Copy，将 8KB inter-subarray copy latency 降低 9.2x，见 Page 5-7, Section 4。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Inter-subarray data movement; DRAM substrate; Row Buffer Movement; in-DRAM copy and caching。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 Low-Cost Inter-Linked Subarrays (LISA)、Row Buffer Movement (RBM)。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- LISA 的硬件核心是给相邻 subarrays 的同列 bitlines 增加 link；当 link 打开时，一个 row buffer 可通过 bitlines 驱动相邻 row buffer，见 Page 3, Figure 3。
- RBM 是新的数据移动操作：源 row buffer 已激活，目标 subarray 处于 precharged 状态，打开 link 后目标 row buffer 感测并锁存源数据，见 Page 4, Section 3.2。
- LISA-RISC 用两次 RBM 和写回步骤复制 open-bitline 架构中的两半 row；其 latency 随 hop count 线性增长但仍远低于 RC-InterSA，见 Page 5-7, Figure 7/Table 1。
- LISA-VILLA 设计 fast subarrays 并用 LISA-RISC 把 hot rows 快速复制到 fast region；LISA-LIP 则把两个 precharge units 联合起来加快 bitline precharge，见 Page 7-8。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 用符合 JEDEC/ITRS 的 SPICE circuit model 估计 RBM 和 linked precharge timing，并加入 60%/42.9% guardband，见 Page 4 与 Page 8。
- copy 评估比较 memcpy、RowClone variants 和 LISA-RISC，包含 single-core bootup/forkbench/shell 与 50 个 four-core mixed workloads，见 Page 9-10。
- VILLA/LIP 评估使用 memory-intensive four-core workloads，并报告 weighted speedup、row-buffer hit rate、energy 和 sensitivity，见 Page 10-11。
- 硬件成本通过 prior area models、Micron power calculator、DRAMPower/Ramulator 等工具估计，见 Page 7-9。

主要结果如下：

- RBM 在保守 60% margin 后仍达到 8ns latency 和 500 GB/s data transfer bandwidth，相当于 DDR4-2400 64-bit channel 的 26x，见 Page 2 与 Page 4。
- 8KB copy 中，memcpy latency/energy 为 1366.25ns/6.2µJ，RC-InterSA 为 1363.75ns/4.33µJ，LISA-RISC 1/7/15-hop 为 148.5/196.5/260.5ns 和 0.09/0.12/0.17µJ，见 Page 7, Table 1。
- four-core copy-intensive workloads 中，LISA-RISC-1 平均 weighted speedup 比 memcpy 高 66.2%，比 RC-InterSA 高 2.2x；memory energy per instruction 平均降低 55.4%，见 Page 10, Figure 13。
- LISA-VILLA 在四核 workload 上平均性能提升 5.1%、最高 16.1%；若用 RC-InterSA 搬 hot rows，反而降低 52.3%，见 Page 10-11, Figure 14。
- LISA-LIP 使 precharge latency 从 13.1ns 降至 guardband 后 5ns，即 2.6x 更低；平均性能提升 8.1%，最高 13.2%，见 Page 8 与 Page 11, Figure 15。
- 三种应用组合平均性能提升 94.8%，memory energy reduction 为 49.0%，见 Page 11, Figure 16。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- LISA 需要修改 DRAM array/subarray 间连接和控制逻辑，虽面积开销小但仍需 DRAM 厂商采纳，见 Page 8, Section 7。
- LISA-RISC copy latency 随 copy distance/hop count 增长；Table 4 显示 1 到 63 hops 的 latency 从 148.5ns 到 644.5ns，见 Page 11。
- VILLA 的收益依赖 hot-row detection/caching policy，作者承认 hit rate 可由更好策略提升，见 Page 10-11, Section 9.2。
- coherence、cache dirty blocks 和 OS/software 对 copy 的可见性仍需系统支持，见 Page 6, Section 4.3。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- LISA links 在 DDR5/HBM bank/subarray 组织中是否仍能以相似面积和 timing 成本实现？
- LISA-RISC 与 cache coherence/dirty data 结合时，端到端 OS copy 加速会下降多少？
- VILLA 的 hot-row caching policy 如果换成现代 learned/prefetch-aware policy，收益是否显著提高？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：LISA 在相邻 DRAM subarray 的 bitlines 之间加入低成本 isolation transistors，使 row buffer movement 能跨 subarray 快速传输整行数据，并由此支持快速 copy、in-DRAM cache 和更短 precharge latency。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下内容按原文 Page 1-12 的结构重新扩写，覆盖 LISA substrate、RBM、LISA-RISC、LISA-VILLA、LISA-LIP、hardware cost、methodology、evaluation、other applications、related work 和 conclusion。参考文献不逐条翻译。原文双栏抽取有少量行交错，核心时序建议回到 Page 4-7 的 Figure 4-8 和 Page 10-11 的 Figure 13-17 核对。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的是 DRAM 内部跨 subarray 的高速数据移动。大量系统操作都需要 bulk data movement，例如 page copy、process fork、checkpoint、数据库扫描和内存初始化。传统系统通过处理器和 memory channel 搬移数据，即使只是把 DRAM 中的一块数据复制到 DRAM 另一处，也要先读到 CPU/cache 再写回。RowClone 已经证明同一 subarray 内可以利用 row buffer 快速复制整行，但它的 fast mode 无法跨 subarray。跨 subarray 时，已有机制只能通过窄内部 data bus 或外部 memory channel，速度和能耗都不理想。

LISA 的核心思想是利用相邻 subarrays 的 bitlines 物理上非常接近这一事实。作者在相邻 subarrays 的 bitlines 之间加入低成本 isolation transistors，形成可以被控制打开/关闭的 links。打开 link 时，一个已激活 row buffer 可以驱动邻近 precharged row buffer；目标 row buffer 感测并锁存源数据。这种 Row Buffer Movement (RBM) 绕过了窄内部 bus，以接近整行并行的方式跨 subarray 移动数据。

论文展示 LISA 作为 substrate 可以支持三类应用。第一，LISA-RISC 用 RBM 实现 rapid inter-subarray copy，将 8KB 跨 subarray copy 的 latency 和 energy 大幅降低。第二，LISA-VILLA 用快速行移动支持 heterogeneous DRAM 中的 hot-row caching。第三，LISA-LIP 把相邻 subarray 的 precharge units 联合起来，加速 precharge。三者组合在四核 copy-intensive workloads 中可显著提升 performance 并降低 memory energy。

### 硬件工程师思考
LISA 最重要的工程启发是：DRAM 内部其实有超宽的数据路径，但多数路径被 subarray 边界隔开。只要用很小的连接结构跨过这个边界，很多“必须经过 CPU/memory channel”的数据移动就可以留在 bank 内完成。它的难点不是逻辑复杂，而是模拟电路边界、bitline coupling、timing margin、repair/remapping 和 command protocol。

## 1. Introduction / 引言

### 原文位置
Page 1-2, Section 1

### 中文翻译
作者指出 bulk data movement 是现代系统中的常见瓶颈。memcpy/memmove、fork 时的 page copy、OS boot、shell 操作、数据库和图计算都可能触发大块数据复制。Google datacenter cycles 中有可观比例消耗在 memcpy/memmove 上，这说明数据移动不是边缘问题。

传统 copy 通过 memory channel：source DRAM row 被读出，经由 channel 到 processor cache，再写回 destination。这个路径受限于 off-chip channel 宽度，且会污染 cache、占用 memory controller 队列、增加 DRAM I/O 能耗。RowClone 解决了同一 subarray 内 copy：用 source row 激活 row buffer，再激活 destination row，使 row buffer 数据写回 destination。但现代 DRAM bank 有很多 subarrays，一个 subarray 容量只有几 MB，任意两个 pages 同属一个 subarray 的概率有限。跨 subarray 时 RowClone fast mode 失效。

作者的关键观察是，subarray 内 bitlines 提供极宽并行带宽，而相邻 subarrays 的 bitlines 在版图上距离很近。LISA 在相邻 bitlines 之间加入 isolation transistor，允许一个 subarray 的 row buffer 通过 bitlines 影响另一个 subarray 的 row buffer。这形成了新的 high-bandwidth inter-subarray datapath。

作者将 LISA 定位为 substrate，而不是单一优化。它先提供 RBM primitive，再在其上构建 copy、cache、precharge 三类机制。论文报告 RBM 在加入 60% timing guardband 后仍有约 8ns latency 和 500GB/s data transfer bandwidth，约为 DDR4-2400 64-bit channel 的 26x。

### 硬件工程师思考
引言里最值得记的不是具体 speedup，而是架构层次：LISA 没有把计算放到 DRAM，也没有加入复杂 logic layer；它只增强数据移动能力。很多 PIM/PuM primitive 的实际瓶颈是操作数需要共址。LISA 这种 substrate 可以作为 Ambit/RowClone/FIGARO/NoM 等机制的基础互连补强。

## 2. DRAM Subarrays and Operation / DRAM subarray 与操作背景

### 原文位置
Page 2-3, Section 2

### 中文翻译
背景部分解释 DRAM bank 由多个 subarrays 组成。每个 subarray 有大量 rows 和 columns，bitline 连接一列 cells，sense amplifier/row buffer 位于 bitline 端部。DRAM 常用 open-bitline organization，一行数据实际上由上下两个 row buffer halves 共同服务，因此复制整行时要考虑上下两半。

普通 DRAM 操作包括 ACTIVATE、READ/WRITE 和 PRECHARGE。ACTIVATE 将 cell 数据通过 charge sharing 放大到 row buffer；READ/WRITE 只通过内部 bus 传输少量 column 数据；PRECHARGE 把 bitlines 拉回 Vdd/2。row buffer 是宽的，但 bank 内用于 I/O 的数据路径很窄，这就是跨 subarray copy 慢的根本原因。

作者强调，相邻 subarray 的 bitlines 已经物理相邻，但传统设计中它们互相隔离。LISA 通过可控 link 暂时连接相邻 bitlines，在需要 RBM 或 linked precharge 时打开，在普通访问时关闭，从而保持普通 DRAM 行为基本不变。

### 硬件工程师思考
读 LISA 必须先理解 open-bitline 的 row buffer halves。LISA-RISC 为什么要两次 RBM？因为一整行跨两个 row buffer halves；一次 RBM 只能移动其中一半。这类细节在系统仿真中很容易被抽象掉，但对真实 command sequence 和 latency 计算非常关键。

## 3. LISA Substrate and RBM / LISA 底层结构与 Row Buffer Movement

### 原文位置
Page 3-5, Section 3; Figure 3-5

### 中文翻译
LISA 在相邻 subarrays 的同列 bitlines 之间加入 isolation transistors。正常访问时，links 关闭，subarray 像普通 DRAM 一样工作。执行 RBM 时，source subarray 的 row buffer 已经激活，destination subarray 处于 precharged 状态。打开 link 后，source row buffer 的强驱动通过 bitline 连接扰动 destination bitline；destination sense amplifier 检测并锁存相同数据。

这个过程本质上是 row-buffer-to-row-buffer transfer。它不通过 off-chip channel，也不通过窄 internal data bus。由于每列 bitline 都可并行连接，RBM 的有效带宽接近 row-wide transfer。作者用 SPICE model 估计，在保守 timing margin 后，RBM latency 约 8ns。

作者不允许一次 RBM 跨越任意多个 subarrays。为了保守处理信号完整性和 timing，LISA 只允许在相邻 subarrays 或隔一个 subarray 的范围内执行一个 RBM。长距离移动通过多次 RBM hops 完成，因此 latency 随 hop count 线性增加。

作者还讨论 process/temperature variation。除了使用 worst-case cells，还额外加入 60% latency guardband。即便如此，RBM 仍明显快于通过 channel 或 internal bus 的复制。这个 guardband 处理方式反映了 DRAM 产品设计中必须为 PVT variation 保留余量。

### 硬件工程师思考
LISA 的模拟风险集中在 link 打开后的 bitline charge sharing 和 sense margin。你要关心的问题包括：source row buffer 的 drive strength 是否足够，destination sense amplifier 何时 enable，link transistor 的 parasitic capacitance/resistance 如何影响普通访问，PVT corner 下是否会误写相邻 subarray。论文用 SPICE 和 guardband 给出初步答案，但真实产品还需要 silicon characterization。

## 4. Application 1: LISA-RISC / 快速跨 subarray copy

### 原文位置
Page 5-7, Section 4; Figure 6-8; Table 1

### 中文翻译
LISA-RISC 的目标是在同一 bank 的不同 subarrays 之间低延迟、低能耗复制一整行。高层步骤是：第一，ACTIVATE source row，使数据进入 source row buffers；第二，用 RBM 将 source row buffer 内容移动到 destination subarray 的 row buffers；第三，ACTIVATE destination row，把目标 row buffer 中的数据写入 destination cells；最后 PRECHARGE。

因为 open-bitline 结构中一行分成两个 row buffer halves，LISA-RISC 要分两半复制。以从 SA0 到 SA2 为例，先移动 RB1 到 RB3，并用 ACTIVATE 将这一半写入 destination；然后需要 precharge 相关 row buffers 但保持 RB0 仍激活，以便复制另一半。为此作者引入 precharge-exception command (PREE)，允许 bank-wide precharge 时保留指定 row buffer 的状态。之后再执行 RBM0→2，并 ACTIVATE destination 写入第二半。

这套 sequence 比 RC-InterSA 短很多。RC-InterSA 跨 subarray copy 需要通过另一个 bank 的临时 row，以 cache line 粒度串行 read/write，8KB row 需要 128 次读和 128 次写。LISA-RISC 则用 row-buffer-wide RBM 移动半行，避免大量串行 column transfers。

Table 1 给出 8KB copy 的 latency/energy。memcpy 约 1366.25ns/6.2uJ，RC-InterSA 约 1363.75ns/4.33uJ，RowClone intra-subarray 约 83.75ns/0.06uJ。LISA-RISC 1/7/15 hops 分别约 148.5/196.5/260.5ns 和 0.09/0.12/0.17uJ。即使 15 hops，LISA-RISC 也明显快于 memcpy 和 RC-InterSA。

作者也讨论 coherence。若 CPU cache 中存在 dirty lines，DRAM 内 copy 看到的 DRAM 数据可能不是最新版本。已有工作可通过 flush/invalidate、Dirty-Block Index 或 OS 协作解决。本文不把 coherence 作为主要贡献，但承认这是系统落地必须处理的问题。

### 硬件工程师思考
LISA-RISC 是典型“primitive 很快，系统边界复杂”的机制。真实 OS copy 加速必须处理 page mapping、dirty cache lines、TLB/page allocator、NUMA/channel placement、ECC 和 row remapping。尤其是 PREE 命令改变了 bank 内 row buffer 状态机，验证复杂度不可低估。

## 5. Application 2: LISA-VILLA / 基于 LISA 的 DRAM 内缓存

### 原文位置
Page 7-8, Section 5; Figure 9

### 中文翻译
LISA-VILLA 解决 heterogeneous DRAM 中 hot-row caching 的移动成本。已有 CHARM 使用 fast banks，但动态迁移热点数据成本高；TL-DRAM 在 subarray 内提供 near/far segments，但会出现 near segment underutilization，且需要侵入式 bitline 分割。VILLA-DRAM 设计少量 fast subarrays 作为 cache，但如果没有低成本搬移机制，把 hot rows 搬到 fast subarray 的开销会抵消低延迟收益。

LISA-VILLA 使用 LISA-RISC 将热点 rows 快速复制到 fast subarrays。作者设计简单 epoch-based caching policy：每个 bank 用 1024 个 saturating counters 追踪访问频率，每个 epoch 将 counter 减半以避免陈旧信息；epoch 末选择 16 个最频繁访问 rows 作为 hot rows，并在下次访问时缓存。替换策略使用 benefit counter，访问缓存行则增加 benefit，替换 benefit 最低者。

实验显示，LISA-VILLA 平均性能提升 5.1%，最高 16.1%。重要对比是，如果用 RC-InterSA 而不是 LISA-RISC 迁移 hot rows，VILLA-DRAM 反而性能下降约 52.3%，因为慢迁移成本超过了缓存命中收益。

### 硬件工程师思考
这部分说明 cache substrate 和 cache policy 必须一起看。一个 fast region 本身不等于性能提升；如果把数据搬进去太慢，cache 会变成负优化。对硬件项目，任何“近端快速存储”都要同时评估 fill cost、replacement cost、metadata cost 和 phase behavior。

## 6. Application 3: LISA-LIP / Linked Precharge

### 原文位置
Page 8, Section 6; Figure 10-11

### 中文翻译
第三个应用是加速 precharge。普通 DRAM 中，一个 subarray precharge 时，其他 subarrays 的 precharge units 通常空闲。LISA-LIP 打开相邻 subarray 的 links，让被 precharge 的 bitlines 同时由本 subarray 和相邻 subarray 的 precharge units 拉回 Vdd/2。

Figure 10 展示 linked precharge 过程：一个 subarray 处于 activated 状态，邻近 subarray 处于 precharged 状态；开始 precharge 时关闭 sense amplifier、打开 precharge unit，并打开 links；两个 precharge units 共同重置 bitlines。SPICE 结果显示，precharge latency 可从 baseline 13.1ns 降到约 3.5ns；加入 42.9% guardband 后按 5ns 使用，仍有 2.6x 改善。

实验中 LISA-LIP 在四核 workloads 上平均提升约 8.1%，最高 13.2%。row buffer hit rate 越低，precharge 越频繁，LISA-LIP 的收益越高。

### 硬件工程师思考
LISA-LIP 展示了 substrate 的复用价值：同一个 bitline link 不只做 copy，还能做 precharge 加速。工程上要注意，linked precharge 会影响 bitline settling、邻近 subarray noise 和 timing closure；同时它的收益依赖 workload 是否频繁 row miss。如果调度器已经高度优化 row hits，LIP 收益会下降。

## 7. Hardware Cost and Methodology / 硬件成本与实验方法

### 原文位置
Page 8-9, Sections 7-8; Table 2-3

### 中文翻译
面积方面，作者引用已有 isolation transistor area model，估计每根 bitline 加 isolation transistor 带来约 0.8% die area overhead。LISA 还需要少量 bank 外控制逻辑来控制 links。LISA-VILLA 的访问计数器位于 memory controller 中，每 rank 约 6KB storage。

作者还讨论 repaired rows。DRAM 厂商会用 spare rows 修复 faulty rows，因此 controller 看到的连续逻辑 row address 未必对应连续物理位置。LISA-RISC/RowClone 等需要知道物理 subarray 的机制必须处理 remapping。作者建议通过 SPD 在 boot 时暴露 repaired row 信息，让 memory controller 正确判断物理位置。

评估使用 Ramulator 变体，Pin traces，FR-FCFS memory scheduler。默认处理器是 1-4 个 OoO cores、4GHz、L1 64KB、L2 512KB/core、L3 4MB、DDR3-1600、每 rank 8 banks、每 bank 16 subarrays。copy workloads 包括 bootup、forkbench、Unix shell；多核 workload 随机组合 50% copy-intensive 和 50% non-copy-intensive 程序。

### 硬件工程师思考
repaired rows 是这类论文中经常被忽略但实际很重要的点。只要机制依赖“两个逻辑地址在同一 subarray/相邻 subarray”，row remapping 就会破坏假设。真实控制器若拿不到物理 remap 信息，可能发出错误 primitive，轻则性能下降，重则数据损坏。

## 9. Evaluation / 实验结果

### 原文位置
Page 9-11, Section 9; Figure 12-17; Table 4

### 中文翻译
单核 copy workloads 中，LISA-RISC 显著优于 RC-InterSA，并大幅降低 memory energy。对 bootup、forkbench、shell，LISA-RISC-1 相比 memcpy 分别提升约 12.6%、4.9x 和 1.8%。forkbench 收益最大，因为它执行大量 page copy。RC-InterSA 在某些 workload 上反而慢于 memcpy，因为长时间阻塞 memory controller，导致其他请求排队。

多核 copy workloads 中，LISA-RISC-1 相比 memcpy 平均提升 66.2%，相比 RC-InterSA 提升 2.2x；memory energy per instruction 平均降低 55.4%。这说明在有并发内存请求的系统中，长阻塞 copy primitive 即使省能，也可能伤害整体吞吐。

LISA-VILLA 在四核 memory-intensive workloads 上平均提升 5.1%，最高 16.1%，性能与 fast subarray hit rate 强相关。若使用 RC-InterSA 搬 hot rows，性能降低 52.3%，再次说明快速 fill 是 DRAM 内 cache 能否成立的前提。

LISA-LIP 平均提升 8.1%，最高 13.2%。当 row-buffer hit rate 低、PRECHARGE 命令频繁时收益更大。LISA-VILLA 与 LISA-LIP 组合在无 bulk copy workloads 上平均提升约 12.2%，最高 23.8%。

三种机制组合时，LISA-RISC 提供主要收益，LISA-VILLA 和 LISA-LIP 进一步叠加。最终组合平均性能提升 94.8%，memory energy 降低 49.0%。敏感性分析显示，copy distance 增加会降低 LISA-RISC 收益：1/3/7/15/31/63 hops 的 latency 从 148.5ns 增至 644.5ns，但即使 63 hops 仍有 42.4% weighted speedup 和 48.9% DRAM energy savings。

### 硬件工程师思考
LISA 的实验最重要的是“blocking behavior”。有些 DRAM 内复制虽然省能，但如果占用 bank/internal bus 太久，会拖慢系统。LISA-RISC 的优势不仅是单次 copy latency 低，还在于它保持其他 banks 可服务请求，降低排队延迟。评估类似机制时必须看 queueing latency，而不只是 primitive latency。

## 10-12. Other Applications, Related Work, Conclusion / 其他应用、相关工作与结论

### 原文位置
Page 11-12, Sections 10-12

### 中文翻译
作者还提出 LISA 可用于减少 subarray conflicts。若热点 rows 集中在同一 subarray，即使有 SALP 类 subarray-level parallelism，也会产生冲突。LISA 可快速把冲突 rows remap/move 到不同 subarrays，从而改善并行性。

LISA 还可扩展 in-DRAM bulk bitwise operations 的适用范围。Ambit/早期 triple-row activation 需要操作数在同一 subarray；若源 rows 分散在不同 subarrays，搬移成本会限制收益。LISA-RISC 可低成本把 rows 聚到同一 subarray，再执行 bitwise operation。

相关工作方面，作者把 LISA 与 RowClone、CHARM、TL-DRAM、DAS-DRAM、SALP、cached DRAM 和 precharge optimization 等比较。LISA 的独特性是提供 bank 内跨 subarray 的低成本高带宽 datapath，并用同一 substrate 支持多个机制。

结论强调，LISA 通过少量 isolation transistors 在相邻 subarrays 间建立新的高带宽路径，显著降低跨 subarray bulk copy 的 latency/energy，也支持更实用的 in-DRAM cache 和 linked precharge。作者认为这种 substrate 可以启发更多 DRAM 内数据移动和性能/能耗优化。

### 硬件工程师复习重点

- Page 3-5：RBM 的模拟机制和 8ns/500GB/s 的含义。
- Page 5-7：LISA-RISC command timeline，尤其是为什么需要两次 RBM 和 PREE。
- Page 7-8：LISA-VILLA 展示 fill cost 对 cache 是否有效的决定性作用。
- Page 8：LISA-LIP 展示同一 substrate 可复用到 precharge latency。
- Page 9：row remapping/SPD 暴露 physical repair 信息是实际控制器必须解决的问题。
- Page 10-11：看 queueing latency 和 multi-core weighted speedup，不只看单次 copy latency。
