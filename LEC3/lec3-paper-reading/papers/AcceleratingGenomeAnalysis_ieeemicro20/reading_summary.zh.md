# 中文阅读摘要

## 1. 一句话总结
这篇 IEEE Micro 综述用 read mapping 作为主线，解释 genome analysis 为什么受 approximate string matching 和 data movement 限制，并总结算法、硬件和 PIM 加速 read mapper 的主要方向与采用挑战。

## 2. 研究背景
测序机器能快速产生大量 reads，但计算系统将这些 reads 映射到 reference genome 的速度跟不上。read mapping 包含 indexing、pre-alignment filtering 和 sequence alignment，其中 ASM/DP-based alignment 通常占据大量时间。短读有低错误率但定位困难，长读更唯一但错误率高，二者都需要高效 approximate matching。

## 3. 核心问题
- read mapping 的三个阶段分别有什么瓶颈。
- 为什么 ASM/DP alignment 会成为主要计算热点。
- indexing、filtering、alignment 各有哪些加速方向。
- 为什么单点加速不足以让整个 genome analysis pipeline 跟上测序速度。
- 硬件加速 read mapper 的实际采用障碍是什么。

## 4. 核心贡献
- 用通俗结构解释 read mapping 的 indexing、pre-alignment filtering、sequence alignment 三阶段。
- 总结 q-gram、pigeonhole、base counting、sparse DP 等 filtering 方法。
- 总结 CPU/GPU/FPGA/ASIC/PIM 上的 alignment 加速方式。
- 强调 data movement 是 genome analysis 加速的关键问题。
- 讨论 GenASM 作为 bitvector-based ASM 框架如何跨多个阶段加速。
- 提出四个采用挑战：端到端加速、减少数据移动、灵活硬件、硬件友好数据格式。

## 5. 方法概述
本文是 primer/survey。它不是提出一个新系统，而是组织已有工作，解释 read mapping pipeline 中每一步的计算模式、算法选择和硬件适配方式，并指出未来设计 read mappers 的原则。

## 6. 实验设计
本文没有独立新实验。它引用现有工具和论文结果，例如 Illumina NovaSeq 6000 的测序吞吐、CPU 分析时间、GateKeeper/Shouji/SneakySnake/GRIM-Filter/GenASM/Darwin/DRAGEN 等加速器或工具的结果。

## 7. 主要结果
- read mapping 可占 genome analysis 大部分时间，单个 human genome 分析中 mapping 可消耗 23/32 CPU hours；见 Page 2。
- pre-alignment filtering 通过快速排除 dissimilar pairs 降低昂贵 alignment 次数；见 Page 3-6。
- GenASM 可对 short/long read alignment 达到 111x/116x software speedup，并降低 33x/37x power；见 Page 9。
- adoption challenges 包括端到端 pipeline、data movement、参数灵活性和 FASTQ/FASTA 格式低效；见 Page 8-9。

## 8. 关键结论
genome analysis acceleration 不能只加速一个 kernel；未来 read mapper 需要 algorithm-hardware co-design、减少跨层 data movement、支持不同 sequencing technologies，并采用更硬件友好的数据表示。

## 9. 局限性
作为综述，本文没有统一复现实验；不同引用结果来自不同平台和假设。它对后续 LRS、pangenome、graph genome 和 cloud privacy/security 的新趋势覆盖有限。

## 10. 适合我重点关注的内容
先读 Figure 1 理解 pipeline，再读 pre-alignment filtering 和 sequence alignment 两节，最后读 Page 8-9 的 adoption challenges。

## 11. 和其他文献的关系
这篇是 GenASM、NERO、PIM genome acceleration 等工作的背景入口；与 GenASM 深度论文直接相连。
