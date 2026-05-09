# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | cache access rate vs performance | 说明 CAR 可作为性能代理。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 2 | Page 7 | slowdown estimation accuracy | 比较 ASM/PTCA/FST。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 4 | Page 8 | error distribution | 展示不同 workloads 的误差分布。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 9 | Page 10 | ASM-Cache | 展示 slowdown-aware cache partitioning 的公平性收益。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 11 | Page 12 | ASM-QoS | 展示 soft slowdown guarantee。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 5 | metrics measured by ASM | 列出 CAR、miss rate、contention misses 等计数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 6 | simulation configuration | 列出核心、cache、DRAM 参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Slowdown estimate | Page 3-4, Section 3 | 估计 slowdown | Slowdown ≈ CARalone / CARshared | 若共享状态下 CAR 降低，则应用相对独占运行变慢。 | 是 |
