# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖文章主体内容；不提供逐字长篇翻译。

## Title
原文标题：Accelerating Genome Analysis: A Primer on an Ongoing Journey

中文标题：加速基因组分析：一段持续旅程的入门综述

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
文章说明 genome analysis 的第一步通常是 read mapping，即把测序得到的 read fragments 与 reference genome 比较。由于测序技术产生数据的速度已经超过 CPU-based 分析技术，read mapping 成为 pipeline 瓶颈。作者介绍算法优化和硬件加速两个方向，并讨论硬件加速 read mapper 的采用挑战。

## 1. Motivation / 动机

### 原文位置
Page 1 - Page 2

### 中文翻译
测序设备无法一次读完整 genome，只能产生大量短片段 reads。计算系统需要把这些 reads 重新定位到 reference genome 中，以便后续 variant calling。由于 sequencing error 和个体 genetic variation，read 与 reference 并不完全相同，因此需要 approximate string matching。

read mapping 的 ASM 常用动态规划，准确但开销高。作者列出四类挑战：数据集大导致 CPU-memory data movement 高；测序机器产出 reads 的速度增长快；metagenomic sample 需要匹配大量 reference genomes；临床和疫情监控需要快速分析。

## 2. Read Mapping / 读段映射

### 原文位置
Page 2 - Page 3; Figure 1

### 中文翻译
read mapping 的目标是在允许最多 E 个 edits 的情况下，找到 reference genome 中与 read 相似的位置。常见 edits 包括 deletion、insertion 和 substitution。典型 pipeline 有三步：indexing、pre-alignment filtering、sequence alignment。

indexing 利用 seeds 快速找到潜在 mapping locations；filtering 快速检查候选 read-reference pair 是否可能相似；alignment 对剩余候选执行更精确的 DP-based ASM，并输出 alignment score、edit distance、edit 类型和位置。

## 3. Accelerating Indexing / 加速索引

### 原文位置
Page 3 - Page 4

### 中文翻译
indexing 的主要问题是 reference genome 很大，seed 查询会产生大量随机访问。加速方法包括减少 seed 数、优化 FM-index 或 hash-based index 查询、减少内存访问和数据移动。硬件加速 indexing 需要兼顾压缩表示、随机访问和并行查询。

## 4. Accelerating Pre-Alignment Filtering / 加速预比对过滤

### 原文位置
Page 4 - Page 6

### 中文翻译
pre-alignment filtering 的目标是在昂贵 alignment 前快速丢弃明显不相似的候选。常用方法包括 pigeonhole principle、base counting、q-gram filtering 和 sparse DP。硬件实现包括 GateKeeper、SHD、Shouji、GRIM-Filter、SneakySnake 等。

过滤器的关键指标是速度、功耗、false accept rate 和 false reject rate。false reject 会错误丢掉真实相似序列，因此必须避免；false accept 会把无用候选送入 alignment，增加后续成本。

## 5. Accelerating Sequence Alignment / 加速序列比对

### 原文位置
Page 6 - Page 8

### 中文翻译
sequence alignment 是最准确但最昂贵的阶段。传统 Smith-Waterman、Needleman-Wunsch、Levenshtein 等 DP 算法需要填充大量矩阵项。软件优化使用 SIMD、多线程和 GPU；硬件优化使用 FPGA、ASIC、PIM 和 specialized systolic arrays。

作者讨论 Darwin、DRAGEN、GenAx、GASAL2、ASAP 等方案，并指出许多工作只优化一个子步骤，因此端到端收益会被其他阶段限制。

## 6. Adoption Challenges / 采用挑战

### 原文位置
Page 8 - Page 9

### 中文翻译
作者总结未来 read mapper 加速面临四个挑战。第一，需要加速整个 read mapping，而不只是单个阶段。第二，需要减少数据在 CPU-memory、accelerators 和 sequencing machine 与分析计算机之间的移动。第三，硬件必须灵活支持不同 read length、edit distance threshold 和 scoring function，否则会被快速变化的测序技术淘汰。第四，需要更硬件友好的数据格式；FASTQ/FASTA 用 8 bits 表示一个 base，而 DNA base 只需 2-3 bits，格式转换本身会浪费时间。

## 7. Conclusion / 结论性观点

### 原文位置
Page 9

### 中文翻译
作者认为，当前加速努力为未来 genome analysis tools 提供了基础。真正高效的 read mapper 应该结合算法、硬件和数据格式设计，减少 data movement，并保持对新测序技术的适应性。
