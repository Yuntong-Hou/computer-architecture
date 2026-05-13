# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 GenASM 的问题背景、Bitap 改造、GenASM-DC、GenASM-TB、硬件架构、3D-stacked memory/PIM 映射、评估结果、局限和硬件工程师视角。保留 approximate string matching、Bitap、GenASM-DC、GenASM-TB、systolic array、traceback、PIM 等术语。

## Title

原文标题：GenASM: A High-Performance, Low-Power Approximate String Matching Acceleration Framework for Genome Sequence Analysis

中文标题：GenASM：面向基因组序列分析的高性能低功耗近似字符串匹配加速框架

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

Genome sequence analysis 的多个核心步骤都依赖 approximate string matching（ASM）。传统 dynamic programming（DP）方法准确但计算和存储成本高，成为 read mapping、alignment、edit distance 计算的瓶颈。Bitap 算法用 bitwise operations 实现 ASM，天然更适合硬件，但原始 Bitap 存在三个限制：不适合 long reads 和高 edit distance，内部 loop-carried dependencies 限制并行度，且缺少实用 traceback 支持。

GenASM 的目标是把 Bitap 改造成可实用部署的 genome analysis acceleration framework。它提出 GenASM-DC 进行 bitvector generation 和 distance calculation，提出 GenASM-TB 支持 traceback，并设计基于 systolic array、local SRAM 和 3D-stacked memory vault-level parallelism 的硬件架构。

评估显示，GenASM 在 long-read alignment、short-read alignment、pre-alignment filtering 和 edit distance 计算上都显著优于 CPU software 和多个硬件 baseline。论文的价值不仅是“做了一个 alignment accelerator”，而是展示了 algorithm-hardware-memory co-design 如何把 bitvector ASM 扩展成跨 pipeline 阶段的通用框架。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

测序技术不断提高吞吐，计算分析成为瓶颈。Read alignment、pre-alignment filtering、edit distance 等步骤需要比较 read 和 reference sequence，在 substitutions、insertions、deletions 存在时寻找近似匹配。DP-based alignment 准确但复杂度高，特别是 long reads 和高错误率 reads 会放大计算成本。

已有硬件加速器通常针对某个具体阶段或某种 read 类型优化，难以跨 short reads、long reads、filtering 和 edit distance 通用。GenASM 试图找到一个统一的 ASM primitive，使同一硬件架构能服务多个 genome analysis tasks。

作者选择 Bitap 作为基础，因为它将字符串匹配转换成 bitvector operations，适合硬件并行。但原始 Bitap 不直接满足现代 genome workloads：read 很长，允许 edit distance 较大，需要输出 CIGAR/traceback，还要在硬件中高效存储和调度。

## 2. Background: ASM, DP, and Bitap / 背景：ASM、DP 与 Bitap

### 原文位置

Page 2 - Page 4

### 中文翻译

Approximate string matching 要在允许一定 edit distance 的情况下判断 pattern 是否匹配 text。经典 DP 算法构造矩阵，每个 cell 表示 prefix 之间的最优编辑距离。DP 能处理复杂 scoring 和 traceback，但矩阵规模大，访存和计算成本都高。

Bitap 使用 bit vectors 表示 DP 状态。每个 bit 对应 pattern 的一个位置，bitwise shift/AND/OR/XOR 等操作可同时更新多个位置。它在短 pattern 和低 edit distance 下效率很高。

原始 Bitap 的问题是：pattern 长度受机器字宽限制；edit distance 越大，需要维护更多状态；循环之间有依赖，阻碍 pipeline；traceback 不像 DP 矩阵那样自然。GenASM 的算法贡献就是针对这些问题重构 Bitap。

## 3. GenASM Algorithmic Extensions / GenASM 算法扩展

### 原文位置

Page 4 - Page 7 / Figures 4-6

### 中文翻译

GenASM 首先扩展 Bitap 支持 long reads。它把长 pattern 分块，使用 divide-and-conquer 和 bitvector generation 处理超过单机器字宽的序列。这样可以避免完整 DP 矩阵的巨大存储成本。

其次，GenASM 消除 loop-carried dependencies。通过重排计算、展开和硬件友好的数据流，GenASM 让多个 bitvector operations 可以在 systolic array 中并行推进，而不是严格串行等待前一次迭代结果。

第三，GenASM 增加 traceback。传统 Bitap 只告诉是否匹配或距离，不能直接输出 alignment path。GenASM-TB 设计 Bitap-compatible traceback 机制，使框架能够生成 CIGAR/optimal alignment，而不只是做过滤。

这些扩展把 Bitap 从一个轻量算法变成能覆盖 read alignment、pre-alignment filtering 和 edit distance 的框架。

## 4. Hardware Architecture / 硬件架构

### 原文位置

Page 7 - Page 10 / Figures 7-8, Table 1

### 中文翻译

GenASM 硬件由 GenASM-DC 和 GenASM-TB 组成。GenASM-DC 负责 distance calculation，使用 systolic array 执行大量 bitvector operations。Systolic array 适合规则、局部通信的数据流，可降低控制复杂度并提高能效。

GenASM-TB 负责 traceback。Traceback 通常需要访问中间状态，容易造成存储压力。GenASM 通过局部 SRAM（DC-SRAM/TB-SRAM）保存必要状态，并在硬件中调度 traceback 数据访问。

论文将 GenASM 映射到 3D-stacked memory 的 vault-level parallelism。每个 vault 集成一个 accelerator，多个 vault 并行处理不同 reads 或任务。这样做的动机是 genome workloads 数据量大，靠近 memory 可降低 data movement。

单个 GenASM accelerator 面积约 0.334 mm²、功耗约 101 mW；32 vaults 总面积约 10.69 mm²、总功耗约 3.23 W。作者据此认为它适合 near-memory/PIM 集成。

## 5. Evaluation Methodology / 评估方法

### 原文位置

Page 10 - Page 12

### 中文翻译

作者使用 synthesized SystemVerilog model 和 detailed simulation-based performance modeling。比较对象包括 Minimap2、BWA-MEM、GASAL2、GACT/Darwin、SillaX/GenAx、Shouji、Edlib、ASAP 等。

数据集包括 human reference genome GRCh38、PacBio/ONT long reads、Illumina short reads，以及 edit distance benchmark datasets。评估 use cases 包括 long read alignment、short read alignment、end-to-end read mapping pipeline、pre-alignment filtering 和 edit distance。

这种多 use-case 评估是本文亮点，因为 GenASM 的主张是通用 ASM framework，而不是单点 kernel。

## 6. Results / 主要结果

### 原文位置

Page 10 - Page 13 / Figures 9-14

### 中文翻译

Long-read alignment 中，GenASM 相比 12-thread Minimap2 speedup 116x，power 降低 37x；相比 GACT speedup 3.9x，power 降低 2.7x。Short-read alignment 中，相比 12-thread BWA-MEM/Minimap2 speedup 111x/158x，相比 SillaX speedup 1.9x。

端到端 pipeline 中，相对 BWA-MEM/Minimap2，GenASM 对 Illumina workload speedup 约 2.4x/1.9x，对 PacBio 约 6.5x/3.4x，对 ONT 约 4.9x/2.1x。端到端收益低于 kernel speedup，说明 pipeline 还有其它瓶颈。

Pre-alignment filtering 中，GenASM 相比 Shouji 在 100bp 上 speedup 3.7x、power 降低 1.7x，并且 false accept 更低、false reject 为 0%。Edit distance 中，相比 Edlib speedup 22-12501x、power 降低 548-582x；相比 ASAP speedup 9.3-400x、power 降低 67x。

## 7. Discussion and Limitations / 讨论与局限

### 原文位置

Discussion / Limitations

### 中文翻译

GenASM 的局限包括：许多结果来自综合和模拟，不是完整芯片实测；部分 baseline 数据来自原论文，平台和参数可能不同；pre-alignment filtering 对更长 reads 的 speedup 下降；复杂 scoring、affine gap penalty 和更多生物信息学 pipeline 需求仍需扩展。

此外，PIM/3D-stacked memory 集成需要软件栈、调度、数据布局和内存接口支持。加速 ASM kernel 只是第一步，真正产品化需要和 mapper、variant caller、storage pipeline、host runtime 结合。

## 8. 硬件工程师视角

GenASM 对硬件工程师的启发是：好的加速器不是把软件照搬成 RTL，而是先重构算法的数据依赖和数据表示。Bitap 原始形式不够硬件友好，GenASM 通过 dependency removal、systolic dataflow 和 local SRAM 才获得效率。

对 PIM/near-memory 设计，GenASM 展示了一个合理 workload：数据量大、操作规则、bit-level parallelism 强、对 host-memory data movement 敏感。设计时要重点关注 host-to-PIM 数据布局、vault load balance、SRAM 容量、traceback 状态存储和 pipeline backpressure。

验证重点包括：long read 分块边界、edit distance 阈值、traceback correctness、CIGAR 输出、不同 read length/error rate、SRAM overflow、multi-vault scheduling 和与软件 mapper 的结果一致性。

## 9. 不确定与需回原文核对

- Figures 4-8 的算法数据流和硬件结构需回 PDF 对照；
- Table 1 的面积/功耗是综合估算，产品化需重做 PPA；
- Figures 9-14 的 speedup/power 数值建议结合 baseline 设置核对；
- 对复杂 alignment scoring 的支持需要阅读原文细节。
