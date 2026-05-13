# Full Chinese Translation

说明：本文件基于已下载 PDF 的抽取文本生成。`full_translation.zh.md` 采用逐节中文详译/学习译文形式，覆盖论文主要结构、方法、实验、结果、讨论与局限；专业术语保留英文，关键结论均给出原文页码或图表位置。

## Title
原文标题：FIGARO: Improving System Performance via Fine-Grained In-DRAM Data Relocation and Caching

中文标题：FIGARO：通过细粒度 DRAM 内数据重定位和缓存提升系统性能

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文关注的核心是：FIGARO 复用 DRAM bank 内共享 global row buffer，以 cache-block/row-segment 粒度在 subarrays 间重定位数据，并构建 FIGCache 来提升 DRAM row buffer locality 和系统性能。 摘要部分强调，传统系统在处理目标操作或目标平台时存在明显的数据搬移、带宽、能耗或可编程性开销；作者提出的方案通过新的硬件/软件机制缓解该问题，并在真实应用、模拟或原型系统中展示收益。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先说明研究背景：DRAM 容量提升远快于访问延迟改善；in-DRAM cache 用小而快的 DRAM 区域缓存慢区域数据，但现有方案以整行 8KB 粒度迁移，浪费空间且迁移延迟受物理距离影响，见 Page 1-2。 现代 DRAM bank 中所有 subarrays 共享 global row buffer，作者发现它可作为跨 subarray 细粒度 relocation 的通道，见 Page 1-2。 这部分的重点不是某个单独优化技巧，而是说明为什么传统 processor-centric 或 coarse-grained memory system 无法高效支撑目标场景。由此，论文提出的主要研究问题可以概括为：如何避免 in-DRAM cache 以整行粒度搬移大量不会被访问的数据。; 如何让跨 subarray relocation latency 与物理距离无关，避免大量 fast subarrays 交错布局。; 如何在 heterogeneous 和 homogeneous DRAM banks 中都获得 in-DRAM cache 收益。

作者随后给出贡献：提出 FIGARO substrate，支持 bank 内 subarrays 之间 column/cache-block granularity data relocation，且 latency distance-independent，见 Page 2-6。; 提出 FIGCache，把 DRAM row 的 small fragments/row segments 缓存在 in-DRAM cache row 中，而非整行缓存，见 Page 2 与 Page 6-8。; FIGCache 可在有 fast subarrays 的 heterogeneous bank 和仅有 slow subarrays 的 conventional bank 中工作，见 Page 1-2。 这些贡献共同构成论文的技术路线，也决定了后续方法和实验的组织方式。

---

## 2. Background / 背景

### 原文位置
Background 相关章节，页码见 extraction_log.md 的章节列表

### 中文翻译
背景部分主要补足理解论文所需的系统与硬件知识。对本文来说，关键背景包括：Fine-grained in-DRAM data relocation; in-DRAM cache; DRAM latency reduction。读这部分时应保留英文术语，因为后文方法直接使用这些术语组织设计，例如 FIGARO、FIGCache。

这部分还解释了为什么原有方案不足：要么抽象层次过低、需要大量手工管理；要么只能在模拟器中评估；要么需要传输或激活过多无用数据；要么缺乏对真实 DRAM/PIM 设备行为的控制。论文后续方法就是围绕这些不足展开。

---

## 3. Method / 方法

### 原文位置
方法章节，见 metadata.md 中 Sections Detected

### 中文翻译
方法部分可以分成以下几个核心设计：

- FIGARO 允许两个 local row buffers 通过 global row buffer 进行 unaligned data transfer，使源列可写入目标不同列，不经过 off-chip memory channel，见 Page 2 与 Section 4。
- FIGCache 使用 row segment granularity，把来自不同 DRAM rows 的 hot segments co-locate 到同一 cache row，提高 cache utilization 和 row buffer hit rate，见 Page 2 与 Page 6-8。
- memory controller 维护 FIGCache Tag Store (FTS)，记录 row segment tags、benefit counters、dirty/valid bits，并用 benefit-based replacement 选择缓存内容，见 Page 7-8 与 Page 11。
- FIGCache-Fast 使用少量 fast subarrays；FIGCache-Slow 只保留 slow subarray 中少量 rows 作为 cache，见 Page 8-9。

从学习角度看，方法章节最重要的是把“机制如何工作”和“系统如何调用它”分开。前者说明 primitive 或 abstraction 本身；后者说明 memory controller、runtime、API、allocator、coherence、prediction 或 code generation 如何让 primitive 在端到端系统中真正可用。

---

## 4. Evaluation / 实验

### 原文位置
Evaluation / Results 章节

### 中文翻译
实验设计如下：

- 评估 Base、LISA-VILLA、FIGCache-Slow、FIGCache-Fast、FIGCache-Ideal 和 LL-DRAM，见 Page 9, Section 8。
- 包括 single-thread applications、eight-core multiprogrammed workloads 和 multithreaded applications，并按 memory intensity 分类，见 Page 9。
- 指标包括 speedup、in-DRAM cache hit rate、DRAM row buffer hit rate、system energy breakdown、area/power overhead 和 sensitivity studies，见 Page 9-12。

主要结果如下：

- FIGCache-Fast 在 20 个 eight-core workloads 上平均提升 16.3% performance；100% memory-intensive workloads 平均提升 27.1%，见 Page 9, Figure 8。
- FIGCache-Slow 即使没有 fast subarrays，也在 multiprogrammed workloads 上平均提升 12.4% performance，见 Page 9。
- FIGCache-Fast 比 LISA-VILLA 平均高 4.7% performance，且只用两个 fast subarrays，而 LISA-VILLA 使用 16 个，见 Page 9。
- FIGCache-Slow/Fast 的整个 DRAM system row buffer hit rate 比 LISA-VILLA 平均高 18%，见 Page 10, Figure 10。
- memory-intensive single-core applications 中，FIGCache-Slow/Fast 分别降低 system energy 6.9%/11.1%；摘要报告 8-core workloads 上 DRAM energy 平均降低 7.8%，见 Page 10-11 与 Page 1。
- FIGARO DRAM chip area overhead <0.3%；FIGCache-Fast 额外 fast subarrays 面积 0.7%，低于 LISA-VILLA 的 5.6%；FIGCache-Slow 仅 0.2%，见 Page 11。

这些结果说明，作者提出的方法在其目标场景下有明显收益。不过阅读时需要注意：实验收益通常依赖 workload、baseline、系统参数和实现假设，不能直接泛化到所有内存系统或所有应用。

---

## 5. Discussion, Limitations, and Future Work / 讨论、局限与未来工作

### 原文位置
Discussion / Future Work / Limitations / Conclusion 相关章节

### 中文翻译
论文明确或隐含的局限包括：

- 需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。
- FIGCache 效果依赖 temporal locality、row segment size、replacement policy 和 hot data identification，见 Page 11-12 Sensitivity Studies。
- row segment 太大退化为整行缓存，relocation latency 和 cache underutilization 上升，见 Page 11, Section 9.2。
- RowHammer/side-channel mitigation 只是其他用例讨论，不是主要实验验证对象，见 Page 8。

这些局限提示我们：本文贡献很重要，但更适合放在特定研究脉络中理解，而不是当作通用解决方案。后续可围绕以下问题继续阅读或复现：

- FIGARO 的 RELOC 操作在真实 DDR4/DDR5 芯片上能否以论文时序安全实现？
- FIGCache 与 Sectored DRAM 的 fine-grained access 思路能否结合？
- FIGCache 在现代多租户安全攻击和 RowHammer mitigation 中的实际收益需要怎样验证？

---

## 6. Conclusion / 结论

### 原文位置
Conclusion

### 中文翻译
论文最终强调：FIGARO 复用 DRAM bank 内共享 global row buffer，以 cache-block/row-segment 粒度在 subarrays 间重定位数据，并构建 FIGCache 来提升 DRAM row buffer locality 和系统性能。 对这组 LEC4 文献而言，这篇文章提供了一个重要视角：DRAM/PIM 研究不仅包含底层电路 primitive，也包含系统集成、编程模型、实验平台和 workload 适配。建议结合 `reading_summary.zh.md` 和 `figures_tables_equations_notes.zh.md` 复习。

---

# 2026-05-12 高完整度扩写版

说明：以下扩写按论文结构重新组织，覆盖 Abstract、Introduction、Background、现有 in-DRAM cache 问题、FIGARO substrate、FIGCache design、其他用例、实验、硬件开销、敏感性分析、相关工作与结论。专业术语保留英文；参考文献列表不逐条翻译。由于原文为双栏 PDF，抽取文本中个别行有交错，图表细节建议回到 PDF 原图核对。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
论文研究的核心问题是 DRAM latency。随着 DRAM 容量和系统并行度提高，内存访问延迟仍然是很多应用的主要瓶颈。已有 in-DRAM cache 方案尝试在同一 DRAM chip/bank 内加入较快区域，把热点数据从慢区域搬到快区域，从而降低访问延迟。但作者指出现有设计存在两个关键低效点：第一，数据搬移粒度通常是整条 DRAM row，往往是多个 KB；而很多 workload 在一次 row activation 后只会访问其中很小一部分 cache blocks。第二，现有 across-subarray relocation 的延迟和源/目标物理距离相关，因此需要把 fast regions 和 slow regions 交错布局，增加面积和制造复杂度。

FIGARO 提出一种新的 DRAM 内细粒度数据重定位 substrate。它复用 bank 内所有 subarrays 已经共享的 global row buffer，使数据可以在 subarrays 的 local row buffers 之间以 column/cache-block granularity 搬移。这个 RELOC 操作在 bank 内具有 distance-independent latency，因此不必为降低距离而密集交错 fast subarrays。

基于 FIGARO，作者构建 FIGCache。FIGCache 不缓存整行，而缓存 row segments：把多个来自不同 DRAM rows 的热点片段放进同一 cache row，提高 cache utilization 和 row buffer locality。论文报告，在 DDR4 八核 workload 上，FIGCache-Fast 平均提升 16.3% performance，并平均降低 7.8% DRAM energy；硬件面积开销低于已有 in-DRAM cache 方案。

### 硬件工程师思考
FIGARO 的工程价值在于把“缓存什么粒度”和“怎么搬”解耦。传统 in-DRAM cache 的问题不是 cache 思路错，而是 row 粒度太粗，导致带宽、cache capacity 和 relocation latency 都被浪费。对硬件工程师来说，这篇文章尤其值得关注 global row buffer、local row buffer、column mux、row decoder latch 这些外围电路如何被重新利用。

## 1. Introduction / 引言

### 原文位置
Page 1-2, Section 1; Figure 1; Figure 2

### 中文翻译
作者首先解释 DRAM latency 为什么难以继续降低。DRAM subarray 中的 bitline 越长，连接的 cells 越多，电容越大，ACTIVATE、RESTORE、PRECHARGE 的时序就越长。为了降低延迟，已有研究使用 shorter bitlines 或 heterogeneous DRAM，把一部分 rows/subarrays 设计得更快。in-DRAM cache 进一步利用这些快区域，把热点数据缓存到低延迟位置。

但是现有 in-DRAM cache 有明显粒度问题。DRAM row 可能是 8KB，而处理器 cache line 通常是 64B。即使应用只反复访问某一行中的几个 cache lines，整行缓存仍要搬移和占用 cache capacity。这导致 cache row 中大量 bytes 从未被使用，实际有效容量远低于物理容量。Figure 1/2 展示的正是这种整行缓存下的数据浪费。

第二个问题是搬移路径。LISA-VILLA、DAS-DRAM 等方案可以在 DRAM 内移动整行，但延迟与源/目标 subarray 距离有关。为了让热点行能快速迁移到 fast subarray，系统不得不布置很多 fast subarrays 或将它们与 slow subarrays 交错。这种设计增加面积、布线和制造复杂度，也使 fast region 的管理更麻烦。

作者的观察是，现代 DRAM bank 已经有 global row buffer/global bitline，用于连接各 subarray 的 local row buffers 和 I/O。虽然普通 READ/WRITE 只用它传输一个 column 到外部接口，但它本质上连接了 bank 内各 subarrays 的数据通路。FIGARO 就把这个已有结构转化为细粒度 relocation path。

本文贡献可以概括为三层。第一，提出 FIGARO substrate，在不经 off-chip channel 的情况下，以 cache-block granularity 在 subarrays 间搬移数据。第二，提出 FIGCache，将 row segment 而非整行作为 cache insertion granularity，提高利用率。第三，系统性评估 FIGCache-Fast 和 FIGCache-Slow，证明即使没有新增 fast subarray，细粒度缓存也能通过提升 row buffer locality 获得收益。

### 硬件工程师思考
这一节非常适合和 LISA 对照。LISA 解决的是“整行跨 subarray 搬移太慢”；FIGARO 进一步问：“为什么一定要整行搬？”实际工程中，很多内存优化失败不是因为机制没有带宽，而是粒度与 workload locality 不匹配。设计缓存、prefetch、DMA、PIM primitive 时都要先确认数据复用粒度。

## 2. Background / 背景

### 原文位置
Page 3, Section 2

### 中文翻译
背景部分回顾 DRAM 组织层次：channel、rank、chip、bank、subarray、row、column。一个 rank 常由多个 x8 DRAM chips 组成；每个 chip 提供 8-bit 数据，八个 chip 共同组成 64B cache line 的一次访问。每个 bank 内包含多个 subarrays，每个 subarray 有自己的 local row buffer/sense amplifiers。

访问一行时，memory controller 发出 ACTIVATE，目标 wordline 被拉高，整行 cells 与 bitlines 共享电荷，local row buffer 感测并锁存整行数据。随后 READ/WRITE 根据 column address 选择一部分数据，经由 global row buffer/global bitlines 送往 I/O。最后 PRECHARGE 关闭当前 row，将 bitlines 重新拉回 Vdd/2。

作者强调 local row buffer 和 global row buffer 的区别。local row buffer 宽度等于整行，是 subarray 内超宽并行结构；global row buffer 较窄，通常只服务当前 column 传输。FIGARO 的关键是让 global row buffer 在两个 local row buffers 之间承担细粒度转发功能，而不把数据送出 chip。

### 硬件工程师思考
这里要记住：FIGARO 不是新增一个巨大 crossbar，而是复用本来就存在的 global buffer path。因此面积小于“给每个 subarray 加宽互连”的方案。但复用路径也带来限制：一次 RELOC 的粒度是 column/cache block，不是整行；搬一个 row segment 需要多次 RELOC。粒度变小降低无效搬移，但也增加 command count，需要在 row segment size 上折中。

## 3. Existing In-DRAM Caches and Their Limits / 既有 DRAM 内缓存的局限

### 原文位置
Page 3-4, Section 3

### 中文翻译
作者比较三类已有 in-DRAM latency optimization。TL-DRAM 在 subarray 内加入 isolation transistors，把 bitline 分成 near segment 和 far segment。near segment 较短，访问延迟低，可作为 fast region。但 TL-DRAM 需要侵入式修改 subarray bitline，且在 open-bitline organization 下有面积和制造成本问题。

CHARM 使用靠近 I/O 的 fast banks/subarrays，静态地把热点数据分配到快区域。问题是热点会随程序 phase 改变；如果需要动态迁移，数据要经过窄内部 bus 或 memory channel，迁移成本高。

DAS-DRAM 和 LISA-VILLA 支持 DRAM 内 bulk data relocation，但搬移粒度是整行，且延迟与距离有关。它们在热点行访问密集且整行有用时有效；但当热点只是 row 中小片段时，整行缓存造成严重 underutilization。FIGARO 因此把关注点从“更快整行搬移”转向“细粒度搬移和缓存”。

### 硬件工程师思考
这部分给实际架构评审一个模板：评价一个 memory substrate 时，不只看单次 primitive latency，还要问数据粒度、热点变化速度、metadata 成本、replacement policy、布局约束和制造复杂度。FIGARO 的主张是：比起让整行搬得更快，更重要的是避免搬没用的数据。

## 4. FIGARO Substrate / FIGARO 底层机制

### 原文位置
Page 4-6, Section 4; Figure 3-6

### 中文翻译
FIGARO 提供新的 RELOC command，用于把已激活 source row 的一个 column/cache block 复制到 destination subarray 的某个 row/column。操作分几步：先 ACTIVATE source row，使其数据进入 source local row buffer；然后 RELOC 选择 source column，把该 column 通过 global row buffer 转发到 destination local row buffer 的目标 column；随后 ACTIVATE destination row，使 destination local row buffer 中的目标 column 被写入目标 cells；最后 PRECHARGE。

这与普通 READ/WRITE 不同。普通访问把 column 数据送到 I/O；FIGARO 则让数据停留在 DRAM chip 内部，从 source local row buffer 经 global row buffer 到 destination local row buffer。由于 global row buffer 连接 bank 内所有 subarrays，RELOC latency 对源/目标物理距离基本无关。

FIGARO 支持 unaligned relocation，即 source column A 可以写入 destination column B。这需要 column address mux 和扩展的地址编码，使 RELOC command 能同时携带 source column、destination subarray 和 destination column 等信息。论文指出一个 RELOC 可用约 21 bits 表达这些字段。

为了支持在一个 bank 中保持 source row active 同时操作 destination subarray，FIGARO 需要对 DRAM peripheral logic 做小改动，包括 per-subarray row address latch、row/column address mux 和对 local row decoder 的扩展。这些改动位于外围逻辑，不改 cell array。

作者用 SPICE/22nm model 估计 RELOC 时序。考虑 guardband 后，单个 RELOC 的数据转发约 1ns；完整一列 relocation 包含两个 ACTIVATE、一个 RELOC 和一个 PRECHARGE，总延迟约 63.5ns，能耗约 0.03uJ。这里的关键不是 1ns 本身，而是距离无关且粒度小。

### 硬件工程师思考
FIGARO 的可靠性风险集中在两个地方。第一，global row buffer 原本服务 READ/WRITE，现在要驱动另一个 local row buffer 的写入路径，必须验证 drive strength、signal integrity 和 timing margin。第二，允许 bank 内多 subarray 状态参与操作，会触及 DRAM command scheduling 和 bank state machine。实际产品化需要重新定义 controller 对 ACTIVATE/PRECHARGE 的合法序列，并确保不会破坏 refresh、power-down、training 和 error handling。

## 5. FIGCache Design / FIGCache 设计

### 原文位置
Page 6-8, Section 5; Figure 7

### 中文翻译
FIGCache 是基于 FIGARO 的 in-DRAM cache。它的核心设计是 row segment granularity。一个 DRAM row 被分成多个 row segments，例如默认 1KB，即 16 个 64B cache blocks。FIGCache 在 cache miss 时不搬整行，而只把被访问的 row segment 搬进 in-DRAM cache。

cache row 可以容纳来自不同 source rows 的多个 row segments。这样做有两个好处：第一，避免把不访问的 row bytes 搬进 cache，提高 cache capacity utilization；第二，把近期访问的多个 row segments 打包到同一 cache row，提高后续访问的 row buffer hit rate。当多个热点片段共处一行时，打开 cache row 后可以命中更多请求。

memory controller 维护 FIGCache Tag Store (FTS)。每个 entry 记录 row segment tag、valid bit、dirty bit 和 benefit counter。访问时，controller 查询 FTS 判断目标 row segment 是否在 FIGCache 中；若命中，则访问 cache row；若 miss，则根据 insertion/replacement policy 使用 FIGARO RELOC 将目标 segment 搬入 cache。

FIGCache 的 replacement 粒度是 row，而 insertion 粒度是 row segment。也就是说，cache miss 插入一个 segment，但替换时可能以整条 cache row 为单位，配合 benefit counter 选择收益最低的 cache row。这种设计是为了保留 row 内多个 segment 的 temporal locality。

作者提出两种实现。FIGCache-Fast 在每个 bank 增加少量 fast subarrays，作为低延迟 cache region；默认只用两个 fast subarrays。FIGCache-Slow 不增加 fast subarrays，而是在普通 slow subarray 中保留一些 rows 作为 cache。FIGCache-Slow 不降低 cell sensing latency，但能通过提升 row buffer locality 减少 ACTIVATE/PRECHARGE 次数，因此仍有性能和能耗收益。

### 硬件工程师思考
FIGCache-Slow 是这篇文章很值得关注的点：即使没有更快的 bitline，只要改变数据布局和 row buffer locality，也能提升系统性能。这对工程实践有启发：很多 DRAM 优化不一定要靠更快 cell，而可以靠更好的 placement、packing 和 controller policy。对硬件架构师来说，FTS 的查询路径是否影响 memory controller critical path、dirty segment 如何写回、cache metadata 如何恢复，是需要继续追问的问题。

## 6. Other Use Cases / 其他用例

### 原文位置
Page 8, Section 6

### 中文翻译
作者讨论 FIGARO/FIGCache 的其他潜在用途。对于 HBM、GDDR 等高带宽 DRAM 技术，如果 bank/subarray 结构类似，global row buffer 路径也可能支持类似细粒度 relocation。论文没有做完整评估，但指出这种 substrate 不限于传统 DDR4。

作者还提到安全用途。FIGCache 可以把频繁访问的 row segment 缓存在 cache row，减少对原始 row 的反复 ACTIVATE/PRECHARGE，从而可能缓解 RowHammer 风险。它也可能扰乱 row-buffer timing side channel，因为访问是否命中 cache row 会改变原本可观察的 row hit/miss pattern。不过这些只是 potential use cases，并非本文实验验证的主要结论。

### 硬件工程师思考
安全用途必须谨慎理解。减少热点原始行激活确实可能降低某些 RowHammer 触发，但 cache 本身也会引入新的状态和 timing channel。若要把 FIGCache 用于安全，需要 threat model、攻击实验和 isolation policy，而不能只依赖直觉。

## 7. Evaluation Methodology / 实验方法

### 原文位置
Page 8-9, Section 7

### 中文翻译
实验使用 Ramulator 和 in-house processor simulator，trace 来自 Pin。默认系统是 8-core、3.2GHz、DDR4 800MHz，四个 memory channels；DRAM 配置包括每 bank 64 个 subarrays、8KB row size、每 channel 4GB。FIGARO 的 RELOC 粒度是 64B cache block，RELOC latency 为 1ns；FIGCache 默认 row segment 为 1/8 row，即 16 个 cache blocks/1KB；每 bank 的 in-DRAM cache 为 64 rows。

工作负载包括 TPC、MediaBench、MSC、BioBench、SPEC 等 20 个 single-thread applications，并按 memory intensity 分类；还构造 20 个 eight-core multiprogrammed workloads，并包含 canneal、fluidanimate、radix 等 multithreaded workloads。

对比对象包括 Base、LISA-VILLA、FIGCache-Slow、FIGCache-Fast、FIGCache-Ideal 和 LL-DRAM。FIGCache-Ideal 用于显示理想 cache/relocation 条件下的上界；LL-DRAM 代表所有 subarrays 都低延迟的理想化方案。

### 硬件工程师思考
评价 FIGCache 时，baseline 选择很重要。与 Base 比能看到 cache 的绝对收益；与 LISA-VILLA 比才能看到 fine-grained relocation 的价值；与 LL-DRAM 比能看到离理想低延迟 DRAM 还有多远。实际阅读 Figure 8-15 时要始终问：这个收益来自更低 sensing latency、更多 row buffer hits、减少 relocation latency，还是减少 useless cached bytes？

## 8. Evaluation Results / 实验结果

### 原文位置
Page 9-11, Section 8; Figures 8-11

### 中文翻译
性能结果显示，FIGCache-Fast 对 memory-intensive workload 收益最大。single-thread intensive applications 平均提升约 16.1%，non-intensive 只提升约 1.5%。在 eight-core multiprogrammed workloads 中，随着 memory-intensive 程序比例从 25% 到 100% 增加，FIGCache-Fast 的平均提升从 3.9%、12.9%、21.8% 到 27.1%；总体平均 16.3%。这说明 FIGCache 本质上缓解 memory stall，而不是提升 compute-bound workload。

FIGCache-Slow 也有效。虽然它没有 fast subarray 的低延迟优势，但通过把热点 segments 聚集到 cache rows，提高 row buffer locality，在 multiprogrammed workloads 上平均提升约 12.4%。这也解释了为什么它可以超过 LISA-VILLA：LISA-VILLA 搬整行且需要更多 fast subarrays，而 FIGCache 用更细粒度提升 cache utilization。

cache hit rate 和 row buffer hit rate 的分析进一步说明机制来源。FIGCache 的 in-DRAM cache hit rate 不一定总是最高，但整个 DRAM system row buffer hit rate 比 LISA-VILLA 平均高约 18%。原因是细粒度 row segments 让多个热点片段共处同一 cache row，后续访问更容易成为 row hit。

能耗结果显示，FIGCache-Slow 和 FIGCache-Fast 都降低 system energy。对 memory-intensive single-core applications，FIGCache-Slow 平均降低 6.9%，FIGCache-Fast 平均降低 11.1%。能耗下降来自三个方面：更多 row buffer hits 摊薄 ACTIVATE/PRECHARGE energy；执行时间缩短降低静态能耗；FIGCache-Fast 的 fast subarrays 还降低 ACTIVATE/PRECHARGE 动态和静态成本。

### 硬件工程师思考
这里要避免一个常见误读：FIGCache 的收益不只是“cache hit 更快”。对 Slow 版本来说，它并没有更快 cell；收益来自 row locality 重排。这对服务器系统很重要，因为增加 fast subarray 需要 DRAM 厂商改工艺/布局，而 controller-managed data placement 可能更可行。另一方面，FTS 和 relocation command 都需要新 controller/DRAM 协议，仍不是纯软件方案。

## 8.3 Hardware Overhead / 硬件开销

### 原文位置
Page 11, Section 8.3

### 中文翻译
FIGARO 在每个 subarray 添加 column address MUX、row address MUX 和 row address latch。RTL-level evaluation 显示，这些组件面积和功耗很小；在论文默认 DRAM 配置下，FIGARO substrate 的整体 DRAM chip area overhead 小于 0.3%，功耗相对一次 ACTIVATE 的 51.2mW 可忽略。

FIGCache-Fast 每个 bank 增加两个 fast subarrays，每个 fast subarray 只有 32 rows。估计面积开销约 0.7%。相比之下，LISA-VILLA 每个 bank 使用 16 个 fast subarrays，面积开销约 5.6%。FIGCache-Slow 不增加新 fast subarrays，只用现有 rows 作为 cache，因此 DRAM chip area overhead 约 0.2%。

memory controller 侧增加 FTS。默认每 bank 512 entries，每个 entry 包含 19-bit tag、5-bit benefit counter、dirty/valid bits，共 26 bits。每 channel 的 FTS storage 为 26.0KB。CACTI 估计 access time 约 0.11ns，平均功耗约 0.187mW，占 LLC 平均功耗约 0.07%。

### 硬件工程师思考
面积数字很低，但工程评估不能只看面积。还要看验证成本和接口成本：新 DRAM command、controller state machine、FTS lookup timing、错误恢复、刷新交互、power management、ECC 和 address remapping。0.3% die area 不等于 0.3% 产品复杂度。对硬件项目，验证复杂度可能比单元面积更关键。

## 9. Sensitivity Studies / 敏感性分析

### 原文位置
Page 11-12, Section 9; Figures 12-15

### 中文翻译
cache capacity 分析显示，更多 fast subarrays 会提升 FIGCache-Fast 性能，但收益递减。默认选择每 bank 两个 fast subarrays，是在性能和 in-DRAM storage overhead 之间折中。对 100% memory-intensive eight-core workloads，从 2 个增加到 4 个 fast subarrays 只带来不到 2.7% 额外提升，从 4 到 8 个不到 0.8%。

row segment size 分析显示，1KB/16 cache blocks 是较好折中。太小的 segment 可能无法利用 row 内 spatial locality；太大的 segment 会退化成整行缓存，导致 cache underutilization、更多 RELOC commands 和更少可缓存 segments。当 segment size 变成 8KB 整行时，FIGCache 甚至略差于 LISA-VILLA，因为 FIGARO 要用许多 RELOC 复制整行。

replacement policy 分析比较 RowBenefit、SegmentBenefit、LRU 和 Random。所有策略都比 Base 好，说明细粒度缓存本身有效；但 RowBenefit 在 memory-intensive workloads 中最好，因为它以 row 为 eviction 粒度，能保留同一 cache row 内多个近期有用 segments 的 temporal locality。

insertion threshold 分析显示，简单的 insert-any-miss policy 已经有效。提高 threshold 可能过滤一次性访问，但也会延迟真正热点 segment 的缓存，并需要更多 metadata。对 memory-intensive workloads，较高 threshold 反而降低性能。

### 硬件工程师思考
敏感性分析是学习这篇文章的重点。它告诉你设计空间中哪些参数敏感：row segment size、cache capacity、replacement/insertion policy。工程上如果把 FIGCache 类似思想移植到 DDR5/HBM/LPDDR，不能直接沿用 1KB；必须基于 row size、burst length、bank group、workload locality 和 command timing 重新搜索。

## 10. Related Work / 相关工作

### 原文位置
Page 12-13, Section 10

### 中文翻译
作者把相关工作分成几类。第一类是 in-DRAM caches，包括 TL-DRAM、CHARM、DAS-DRAM、LISA-VILLA 等。它们同样试图用 DRAM cells 构建低延迟 cache，但多数以整行为单位搬移数据，或需要高面积的 heterogeneous layout。FIGCache 的差异在于细粒度 relocation 和 row segment packing。

第二类是 in-DRAM data relocation，包括 RowClone、LISA、DAS-DRAM 和 NoM。RowClone-FPM 只能同 subarray 内整行复制；RowClone-PSM 通过 global data bus 串行传输，会阻塞 banks；LISA 支持跨 subarray 整行移动；NoM 关注 3D-stacked DRAM 中 inter-bank copy。FIGARO 与这些方案正交，侧重 bank 内 column/cache-block 粒度 relocation。

第三类是提升 row buffer hit rate 的方法，包括 partial row activation、sub-row buffer、data reorganization、memory scheduling 和 page allocation 等。FIGCache 与这些方法可以组合，因为它同时改变缓存粒度和数据布局。

第四类是 DRAM latency/power reduction，包括 exploiting charge level、reduced timing parameters、CROW、CLR-DRAM、voltage/frequency scaling 等。FIGCache 是从 cache/data movement 角度降低有效延迟和能耗。

### 硬件工程师思考
相关工作说明 FIGARO 处在“DRAM data movement substrate”主线，而不是 pure PIM arithmetic 主线。它与 Ambit/ComputeDRAM 的关系是互补：Ambit/ComputeDRAM 需要操作数共址或在同一 subarray，FIGARO/LISA/NoM 解决数据如何在 DRAM 内移动。真实 PIM 系统最终可能需要两者结合。

## 11. Conclusion / 结论

### 原文位置
Page 13, Section 11

### 中文翻译
论文结论重申，现有 in-DRAM cache 的低效来自两个方面：缓存粒度过粗，通常是整条 DRAM row；硬件设计为了降低搬移距离而带来面积和制造复杂度。FIGARO 通过已有 global row buffer 支持 column/cache-block 粒度 relocation，以很低外围电路开销解决第一类问题，并降低第二类问题的布局压力。

FIGCache 在 FIGARO 上实现 fine-grained in-DRAM cache，把来自不同 rows 的热点 segments 组合进 cache rows，提高 cache utilization 和 row buffer locality。实验显示，它能在多核 memory-intensive workloads 上明显提升性能、降低能耗，并且比 LISA-VILLA 使用更少 fast subarrays。

### 硬件工程师复习重点

- Page 4-6：RELOC command 的数据路径，尤其是 source local row buffer、global row buffer、destination local row buffer 的关系。
- Page 6-8：FIGCache 为什么使用 row segment insertion + row granularity replacement。
- Page 9-10：FIGCache-Fast/Slow 的性能来源不同，Fast 靠低延迟 + locality，Slow 主要靠 locality。
- Page 11：硬件开销小，但接口和验证复杂度仍需单独评估。
- Page 11-12：row segment size 是最关键参数之一，不能机械照搬。

### 对未来工作的启发
如果你以硬件工程师身份看这篇文章，最值得带走的是“粒度匹配”原则。无论做 DRAM cache、PIM、DMA 还是 near-memory accelerator，都必须让硬件操作粒度贴近应用实际复用粒度。过粗会浪费带宽和容量；过细会增加 metadata 和 command overhead。FIGARO 的贡献就是在 DRAM 内提供一个更合适的中间粒度。
