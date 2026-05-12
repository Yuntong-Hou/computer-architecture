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
