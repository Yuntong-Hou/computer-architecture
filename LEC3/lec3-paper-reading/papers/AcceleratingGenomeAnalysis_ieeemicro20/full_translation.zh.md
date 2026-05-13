# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。本文是 IEEE Micro primer/survey，翻译按 read mapping pipeline 和硬件加速脉络展开。保留 genome analysis、read mapping、approximate string matching、pre-alignment filtering、sequence alignment、DP、FPGA、ASIC、PIM、GenASM 等术语。参考文献保留英文。

## Title

原文标题：Accelerating Genome Analysis: A Primer on an Ongoing Journey

中文标题：加速基因组分析：一段持续旅程的入门综述

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

基因测序技术可以快速产生大量 DNA reads，但将这些 reads 分析成有用生物信息仍然计算成本高昂。Genome analysis pipeline 中，read mapping 是核心阶段之一：它将测序 reads 对齐到 reference genome 上，为 variant calling、疾病分析和个性化医疗提供基础。

本文用 read mapping 作为主线，解释 genome analysis 为什么需要硬件加速。Read mapping 包括 indexing、pre-alignment filtering 和 sequence alignment。其核心计算是 approximate string matching（ASM）和 dynamic programming（DP）式 alignment。由于 reads 数量巨大、reference genome 大、错误模式复杂，传统 CPU 软件难以跟上测序吞吐。

文章综述算法、CPU/GPU/FPGA/ASIC/PIM 加速器、数据移动瓶颈和采用挑战。结论是，未来 read mappers 不能只加速单个 kernel，而需要端到端 algorithm-hardware co-design、减少 data movement、支持不同 sequencing technologies，并使用更硬件友好的数据表示。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

测序成本快速下降，使 genome analysis 从研究实验室走向临床和大规模人群分析。然而，数据产生速度提升后，计算分析成为瓶颈。测序机器可以输出海量 short reads 或 long reads，计算系统需要把它们映射到 reference genome，识别突变、插入、删除和结构变异。

Read mapping 的难点来自两个方面。第一，reads 并不完全等于 reference genome 的某段。测序错误、个体差异、插入删除和重复区域都会导致 approximate matching。第二，数据规模巨大。一个 human genome 可能需要处理数十亿 bases，mapping 可消耗大量 CPU hours。

本文的定位是 primer：帮助读者理解 genome analysis acceleration 的问题结构、已有加速方向和未来挑战。对计算机体系结构研究者而言，genome analysis 是典型 data-intensive workload，兼具复杂算法和严重 data movement。

## 2. Read Mapping Pipeline / Read mapping 流水线

### 原文位置

Page 2 - Page 3 / Figure 1

### 中文翻译

Read mapping 通常分三阶段。

第一阶段是 indexing。系统为 reference genome 或 reads 构建 index，使候选匹配位置能被快速查找。常见方法包括 hash-based index、suffix array、Burrows-Wheeler Transform（BWT）等。Indexing 的目标是减少全基因组扫描。

第二阶段是 pre-alignment filtering。由于完整 alignment 很贵，mapper 会先用快速过滤器排除明显不相似的 read-reference pairs。过滤器必须低成本、低 false negative，同时尽量减少进入 alignment 的候选数量。

第三阶段是 sequence alignment。对未被过滤掉的候选 pairs，系统使用 dynamic programming 或 bitvector-based approximate string matching 计算编辑距离、得分和最终对齐。这个阶段最精确，也通常最昂贵。

硬件加速设计必须理解三阶段之间的数据流。如果只加速 alignment，但 indexing/filtering 或 host-device data movement 成为瓶颈，端到端收益会被削弱。

## 3. Approximate String Matching and Alignment / 近似字符串匹配与对齐

### 原文位置

Page 3 - Page 5

### 中文翻译

Read mapping 的核心是 approximate string matching。短读通常错误率低，但因为短，可能在 reference 中出现多个候选位置；长读更容易唯一定位，但错误率更高，尤其需要处理 insertions/deletions。

Dynamic programming alignment 可以精确计算 edit distance 或 alignment score，但复杂度高。Smith-Waterman、Needleman-Wunsch、edit distance DP 等方法需要填充矩阵，计算量与 read 长度和候选 reference 区间长度相关。大量 reads 和候选位置使 DP 成为主要瓶颈。

Bitvector algorithms 通过位并行方式加速 approximate matching。它们把多个 DP 状态压缩到机器字或硬件 bit vectors 中，适合 SIMD、FPGA、ASIC 和 PIM 实现。GenASM 就是基于这种思想，提供跨 read mapping 多阶段的 ASM framework。

## 4. Pre-Alignment Filtering / 预对齐过滤

### 原文位置

Page 5 - Page 6

### 中文翻译

Pre-alignment filtering 的目标是用很低成本排除不可能匹配的 pairs，从而减少昂贵 alignment 次数。文章总结 q-gram、pigeonhole principle、base counting、sparse DP 等方法。

q-gram 方法统计短子串匹配情况。Pigeonhole principle 利用“若两个字符串足够相似，则某些分段必须匹配”的性质。Base counting 比较 A/C/G/T 计数差异，快速排除差异过大的 pairs。Sparse DP 只计算部分矩阵或关键区域，减少工作量。

硬件过滤器如 GateKeeper、Shouji、SneakySnake、GRIM-Filter 等展示了不同 tradeoff：有些追求极低能耗，有些追求低 false negative，有些利用 bit-parallel 或 memory-side representation。过滤器的价值取决于它是否显著降低 alignment 输入规模。

## 5. Hardware Acceleration / 硬件加速

### 原文位置

Page 6 - Page 8

### 中文翻译

文章综述 CPU、GPU、FPGA、ASIC 和 PIM 上的 genome analysis acceleration。CPU 具有灵活性和成熟软件生态，但能效有限。GPU 提供大规模并行性，适合批量 alignment，但 irregular memory access 和分支会影响效率。FPGA 可定制 pipeline 和 bit-level operations，适合过滤和 bitvector alignment。ASIC 可提供最佳能效，但灵活性和开发成本是挑战。

PIM/NDP 方向试图减少 read/reference/index 在 host 和 accelerator 之间移动。Genome analysis 的数据量大、访问模式复杂，data movement 是主要成本之一。把过滤或 alignment 的部分计算放近 memory，可以节省带宽和能耗。

文章强调，硬件加速 read mapper 不能只看 kernel speedup。若加速器只处理 alignment，但数据准备、格式转换、index lookup 或 PCIe 传输占据时间，端到端收益有限。

## 6. GenASM and Cross-Stage Acceleration / GenASM 与跨阶段加速

### 原文位置

Page 8 - Page 9

### 中文翻译

GenASM 被文章作为代表性方向讨论。它基于 bitvector approximate string matching，可用于 pre-alignment filtering 和 sequence alignment 等多个阶段。论文引用结果显示，GenASM 对 short-read/long-read alignment 可达到 111x/116x software speedup，并降低 33x/37x power。

GenASM 的重要性在于跨阶段复用同一类硬件友好 primitive。相比只加速某个孤立 kernel，跨阶段设计更可能获得端到端收益。它也说明 algorithm-hardware co-design 的价值：算法形式若天然适合 bit-level parallelism，硬件实现会更简单高效。

## 7. Adoption Challenges / 采用挑战

### 原文位置

Page 8 - Page 9

### 中文翻译

文章提出四个采用挑战。

第一，端到端加速。实际用户关心完整 genome analysis pipeline 的时间，而不是某个 kernel 的峰值 speedup。加速器必须与 mapper、variant caller、I/O 和软件生态配合。

第二，减少 data movement。基因组数据量巨大，移动 reads、reference、indices 和 intermediate results 会消耗大量能耗和时间。PIM/NDP、压缩和硬件友好格式都很重要。

第三，灵活硬件。Sequencing technologies 快速变化，short reads、long reads、error profiles 和 alignment scoring 都会变化。硬件若过度固定，可能很快过时。

第四，硬件友好数据格式。FASTQ/FASTA 是人类和软件友好的文本格式，但对硬件不友好。压缩、二进制编码、streaming layout 和 alignment-aware representation 可以降低解析和传输开销。

## 8. Conclusion / 结论

### 原文位置

Page 9 / Conclusion

### 中文翻译

Genome analysis acceleration 是持续旅程。测序技术、算法和硬件都在变化。Read mapping 作为核心瓶颈，需要 indexing、filtering、alignment 和 data movement 的协同优化。未来系统应采用 algorithm-hardware co-design，减少数据移动，支持多种 reads 和错误模型，并关注端到端 pipeline。

## 9. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文 pipeline 和 adoption challenges 的工程化解读

### 中文学习笔记

1. 对加速器设计：不要只优化 DP kernel。需要先画出完整数据流，找出 index lookup、filtering、alignment、host-device movement 的真实瓶颈。

2. 对存储/内存系统：genome analysis 是 PIM/NDP 的典型 workload，因为数据量大、算术强度低、过滤和匹配可位并行。

3. 对 FPGA/ASIC：bitvector ASM、q-gram/filtering、base-counting 都适合硬件 pipeline。关键是支持参数变化和错误模型变化。

4. 对软件接口：加速器必须支持主流 mapper 和 pipeline，输入输出格式不能成为隐藏瓶颈。

5. 对行业：临床基因组分析要落地，硬件加速必须可靠、可解释、可维护，并能跟随测序技术更新。

6. 对个人学习：这篇是 GenASM 和 genome PIM 论文的入口。先掌握 read mapping 三阶段，再读具体加速器。

## 10. 不确定与需回原文核对

- 本文是综述，引用结果来自不同平台和假设，不适合直接横向比较绝对数值。
- 后续 pangenome、graph genome、long-read-only pipeline 和云隐私趋势需要补充最新资料。
