# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | read mapping 四步 | indexing/seeding/filtering/alignment 流程 | 背景框架 | 先读 |
| Figure 2 | Page 3 | edit 类型 | deletion/substitution/insertion | ASM 基础 | 简单看 |
| Figure 3 | Page 4 | Bitap example | 原始 Bitap 如何计算 | 理解改进前算法 | 结合 Algorithm 1 |
| Figure 4 | Page 5 | GenASM overview | GenASM-DC/TB 数据流 | 核心架构图 | 必读 |
| Figure 5 | Page 5 | loop unrolling | 消除依赖实现并行 | GenASM-DC 核心 | 必读 |
| Figure 6 | Page 6 | traceback example | GenASM-TB 如何恢复 alignment | correctness 关键 | 细读 |
| Figure 7-8 | Page 7-8 | DC/TB hardware | systolic array、SRAM、TB logic | 硬件实现 | 结合 Table 1 |
| Figure 9-11 | Page 10 | software baseline results | alignment/pipeline speedups | 主要性能结果 | 必读 |
| Figure 12-13 | Page 11 | hardware baseline results | vs GACT/SillaX | 硬件对比 | 看 iso conditions |
| Figure 14 | Page 12 | edit distance | vs Edlib | 通用 ASM 价值 | 重点 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 10 | area/power breakdown | 单 accelerator 0.334mm²/101mW，32 vaults 3.23W | 支撑低功耗 | 必读 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 4 | Bitap baseline | R[d], PM, k, edit distance | GenASM 改进对象 | 是 |
| Algorithm 2 | Page 6 | GenASM-TB traceback | W/O/window/bitvectors/CIGAR | 输出 alignment 的方法 | 是 |
| Complexity expression | Page 12 | 改进来源分析 | m,k,P,w,W,O | divide-and-conquer 降低 DC cycles | 中 |
