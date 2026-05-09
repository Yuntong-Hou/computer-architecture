# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、设计、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：GenASM: A High-Performance, Low-Power Approximate String Matching Acceleration Framework for Genome Sequence Analysis

中文标题：GenASM：面向基因组序列分析的高性能低功耗近似字符串匹配加速框架

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
Genome sequence analysis 的第一步 read mapping 需要把 reads 匹配到 reference genome 中。ASM 能处理 sequencing errors 和 genetic variations，但计算开销大。GenASM 是首个面向 genome analysis 的 ASM acceleration framework。它修改 Bitap 算法以提升并行性、降低 memory footprint，并设计硬件 accelerator。评估显示 GenASM 在 read alignment、pre-alignment filtering 和 edit distance 三个 use cases 中都显著优于软件和硬件 baselines。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
现代 sequencing machines 产生大量 reads，short reads 错误率低但短，long reads 更长但错误率高。read mapping 必须处理 insertion、deletion 和 substitution，因此需要 approximate string matching。传统 DP-based ASM 时间和空间复杂度高，增长速度跟不上 sequencing throughput。

GenASM 的目标是为 short/long reads 提供快速、低功耗、可复用的 ASM 框架，并能加速 genome analysis pipeline 中多个步骤。

## 2. Background / 背景

### 原文位置
Page 2 - Page 4

### 中文翻译
典型 read mapping 包含 indexing、seeding、pre-alignment filtering 和 read alignment。ASM 的目标是在允许最多 E 个 edits 的情况下找出 read 与 reference text 的相似位置。Bitap 是一种 bitvector-based ASM algorithm，使用简单 bitwise operations，因此适合硬件。

原始 Bitap 的限制包括：对 long reads 支持不足、loop-carried dependencies 限制并行、不能执行 traceback、memory footprint 随参数增大、在通用处理器上受 register/cache 限制。

## 3. GenASM Overview / GenASM 概览

### 原文位置
Page 4 - Page 5; Figure 4

### 中文翻译
GenASM 包含两个硬件/算法组件。GenASM-DC 负责执行修改后的 Bitap，生成 match/insertion/deletion/substitution bitvectors 并计算 minimum edit distance。GenASM-TB 使用这些 bitvectors 进行 traceback，输出 optimal alignment。

设计目标是让 compute resources 与 SRAM capacity/bandwidth 匹配，避免资源浪费，并利用 3D-stacked memory logic layer 的 vault-level parallelism。

## 4. GenASM-DC Algorithm / GenASM-DC 算法

### 原文位置
Page 5; Figure 5

### 中文翻译
GenASM-DC 修改 Bitap 以支持 long reads，并通过 loop unrolling 消除邻近 bitvector 的依赖，使多个 non-neighbor bitvectors 可以并行计算。它还把 text 划分为 overlapping sub-texts，以支持 text-level parallelism 和 arbitrary-length sequences。

这种 divide-and-conquer 思路降低了 memory footprint，并使硬件可以用固定大小 windows 处理长序列。

## 5. GenASM-TB Algorithm / GenASM-TB 算法

### 原文位置
Page 6; Algorithm 2; Figure 6

### 中文翻译
GenASM-TB 是 Bitap-compatible traceback algorithm。它从 GenASM-DC 保存的 intermediate bitvectors 出发，反向追踪 match、substitution、insertion 和 deletion，生成 CIGAR-like alignment。为了避免存储全部 bitvectors，GenASM-TB 也采用 divide-and-conquer 和 window overlap。

## 6. Hardware Design / 硬件设计

### 原文位置
Page 7 - Page 8; Figure 7-8

### 中文翻译
GenASM-DC 被实现为 linear cyclic systolic array，包含 64 PEs。每个 accelerator 配有 DC-SRAM 和多个 TB-SRAMs，以减少外部带宽需求。GenASM-TB 使用简单控制逻辑读取 per-PE TB-SRAM 并执行 traceback。

在 3D-stacked memory 配置中，每个 vault 放置一个 GenASM accelerator，32 vaults 可并行处理 32 个 alignments。这样把计算放在 memory logic layer，减少 reference/read 数据移动。

## 7. Evaluation Methodology / 评估方法

### 原文位置
Page 9

### 中文翻译
作者综合 SystemVerilog synthesis、memory estimation 和 cycle-accurate simulation。比较对象包括 BWA-MEM、Minimap2、GASAL2、GACT/Darwin、SillaX/GenAx、Shouji、Edlib 和 ASAP。数据集覆盖 human genome GRCh38、PacBio/ONT/Illumina reads 和 edit distance datasets。

## 8. Results / 结果

### 原文位置
Page 10 - Page 12

### 中文翻译
面积和功耗方面，单个 GenASM accelerator 面积 0.334 mm²、功耗 101 mW；32 vaults 总面积 10.69 mm²、总功耗 3.23 W。

read alignment 方面，long reads 上 GenASM 相比 Minimap2 12-thread alignment step speedup 116x，相比 BWA-MEM 12-thread speedup 648x，并大幅降低 power。short reads 上，相比 BWA-MEM/Minimap2 12-thread speedup 111x/158x。端到端 pipeline 中替换 alignment step 后，Illumina/PacBio/ONT 也获得 1.9x 到 6.5x 的 speedup。

硬件比较中，GenASM 比 Darwin 的 GACT 平均 throughput 高 3.9x、power 低 2.7x；相比 SillaX short read alignment throughput 高 1.9x。pre-alignment filtering 中，GenASM 在 100bp 数据上比 Shouji 快 3.7x、power 低 1.7x，并将 false accept rate 降到很低且 false reject 为 0。edit distance 中，GenASM 相比 Edlib 和 ASAP 也有数量级 speedup 和 power reduction。

## 9. Sources of Improvement / 改进来源

### 原文位置
Page 12 - Page 13

### 中文翻译
GenASM 的收益来自三层。算法层面，divide-and-conquer 大幅降低 GenASM-DC 执行时间，尤其是 long reads。硬件层面，systolic array 提供 64x parallelism，per-PE SRAM 降低 traceback bandwidth。技术层面，3D-stacked memory 的 vault-level parallelism 提供 32x 并行。

## 10. Other Use Cases / 其他用例

### 原文位置
Page 13

### 中文翻译
作者讨论四个未评估但潜在适用的用例：de novo assembly 的 read-to-read overlap finding、hash-table based indexing、whole genome alignment 和 generic text search。由于 GenASM 可处理 arbitrary-length sequences 并可扩展 alphabet，它也可能用于 RNA/protein sequence alignment。

## 11. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
GenASM 展示了基于修改 Bitap 的 ASM framework 如何通过算法、硬件和 memory 共同设计，在多个 genome analysis use cases 中达到高性能和低功耗。作者希望这种方法启发更多 bioinformatics 和 emerging applications 的 co-design。
