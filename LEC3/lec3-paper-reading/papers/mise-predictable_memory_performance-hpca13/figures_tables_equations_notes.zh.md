# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | request service rate vs performance | 证明 RSR 可作为 memory-bound 性能代理。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 2-3 | Page 5-6 | MISE vs STFM accuracy | 比较 memory-bound 和 non-memory-bound 应用估计。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 5 | Page 9 | MISE-QoS performance/fairness | 展示 QoS 下的吞吐与公平性。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 8 | Page 10 | fairness vs core count | 展示 MISE-Fair 降低 maximum slowdown。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 10 | Page 11 | harmonic speedup | 说明公平性收益未显著牺牲性能。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 5 | simulation configuration | 列出 DDR3/cache/core 参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 5 | average error per benchmark | 显示 MISE 平均误差低于 STFM。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 3 | Page 6 | epoch/interval sensitivity | 确定 5M/10K 参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 5 | Page 8 | MISE-QoS effectiveness | 量化 bound meet/prediction correctness。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 6 | Page 9 | STFM-QoS effectiveness | 说明 STFM 估计用于 QoS 较差。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Slowdown for memory-bound apps | Page 3, Equation 1 | 估计 slowdown | Slowdown = ARSR / SRSR | 独占请求服务率与共享请求服务率的比值表示被干扰程度。 | 是 |
| Alpha-adjusted slowdown | Page 3-4, Equation 3 | 修正 non-memory-bound 应用 | 结合 stall fraction alpha | compute phase 不受 memory interference，需降低 memory service-rate 对总性能的影响。 | 是 |
