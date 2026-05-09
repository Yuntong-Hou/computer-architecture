# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | ASM 是 genome sequence analysis 多个步骤的瓶颈 | Page 1-2 | read mapping、WGA、MSA 都需要 ASM | 高 | GenASM 的适用范围大 |
| 2 | 原始 Bitap 硬件友好但有五个限制 | Page 3-4 | 不支持长读、依赖、traceback、memory footprint 等 | 高 | 设计动机 |
| 3 | GenASM-DC 支持 long reads 并消除依赖 | Page 5, Figure 5 | loop unrolling 和 parallel bitvectors | 高 | 性能核心 |
| 4 | GenASM-TB 提供 Bitap-compatible traceback | Page 6, Algorithm 2, Figure 6 | 利用 intermediate bitvectors 生成 alignment | 高 | 让结果可用于 read alignment |
| 5 | 硬件采用 systolic array + local SRAM | Page 7-8, Figure 7-8 | 64 PEs、DC-SRAM、TB-SRAM | 高 | 降低数据移动和带宽压力 |
| 6 | 3D-stacked memory vault-level parallelism 提供 32x 并行 | Page 8 | 每 vault 一个 accelerator | 高 | PIM/near-memory 设计关键 |
| 7 | 面积功耗很小 | Page 10, Table 1 | 单 accelerator 0.334mm²/101mW，32 vaults 3.23W | 中 | 支持能效主张 |
| 8 | alignment 对软件和硬件 baseline 都大幅提升 | Page 10-11, Figure 9-13 | long/short reads 多项 speedup/power improvement | 高 | 主要实验结果 |
| 9 | filtering accuracy 优于 Shouji | Page 12 | false accept 0.02%/0.002%，false reject 0% | 高 | 不只是快，还减少后续 alignment |
| 10 | edit distance speedup 极大 | Page 12, Figure 14 | 22-12501x vs Edlib, 9.3-400x vs ASAP | 高 | 说明 GenASM 作为通用 ASM kernel 的价值 |
| 11 | 未评估的用例包括 de novo overlap、indexing、WGA、generic text search | Page 13, Section 11 | 作者列为 future use cases | 中 | 框架潜力但需验证 |
