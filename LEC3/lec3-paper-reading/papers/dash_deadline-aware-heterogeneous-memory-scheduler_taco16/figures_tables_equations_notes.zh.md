# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | heterogeneous SoC | 展示 CPU/GPU/HWA 共享 DRAM 场景。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 2 | Page 3 | Sobel HWA | 说明 HWA frame processing 与 deadline。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 3 | Page 4 | execution timelines | 展示不同调度策略如何错过或满足 deadline。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 5 | Page 15 | CPU performance | 展示 DASH 与 baselines 的核心对比。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 9 | Page 20 | CPU-GPU-HWA | 展示复杂异构场景。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table V | Page 16 | deadline-met ratio/frame rate | 证明 DASH 保持 deadlines。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table VI | Page 18 | system performance and max slowdown | 展示系统性能与公平性影响。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Progress/on-track estimate | Page 7-9, Section 4 | 判断 HWA 是否能在 deadline 前完成 | 基于 elapsed time、period/deadline、remaining requests 与 worst-case memory access time | 若预计赶不上 deadline，提升 HWA priority。 | 是 |
