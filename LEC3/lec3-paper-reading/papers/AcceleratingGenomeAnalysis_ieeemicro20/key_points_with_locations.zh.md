# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | read mapping 是 genome analysis pipeline 的主要瓶颈 | Page 1-2 | sequencing 速度增长快于计算分析能力 | 高 | 解释为什么需要专用加速 |
| 2 | read mapping 包含 indexing、pre-alignment filtering、sequence alignment | Page 3, Figure 1 | 图示三阶段及对应加速方向 | 高 | 全文组织框架 |
| 3 | ASM/DP alignment 准确但复杂度高 | Page 2-3 | DP 通常为 O(m²) 或 O(mn) | 高 | alignment 加速的算法根源 |
| 4 | data movement 是第一类核心挑战 | Page 2, Challenge 1; Page 8-9 | CPU-memory、accelerator、sequencer-computer 之间移动代价高 | 高 | 与 memory-centric computing 主题一致 |
| 5 | pre-alignment filtering 可大幅减少进入 alignment 的候选 | Page 4-6 | pigeonhole、base counting、q-gram、sparse DP 等 | 中 | 过滤准确性影响后续总成本 |
| 6 | GenASM 跨多个 ASM use case 加速 | Page 9 | short/long alignment 111x/116x speedup | 高 | 与下一篇 GenASM 论文衔接 |
| 7 | 单点加速会受 Amdahl 限制 | Page 8-9 challenges | 需要加速整个 read mapping 而非单阶段 | 高 | 端到端设计比局部 kernel 更重要 |
| 8 | 硬件必须支持变化的 read length 和 edit distance | Page 9 | sequencing technologies 快速变化 | 高 | 专用硬件过窄会很快过时 |
| 9 | FASTQ/FASTA 8-bit/base 表示低效 | Page 9 | DNA base 理论只需 2-3 bits | 中 | 数据格式本身也是系统瓶颈 |
| 10 | 采用挑战包括标准化接口和硬件友好格式 | Page 9 | 作者呼吁更灵活模块化架构 | 中 | 这影响真实部署 |
