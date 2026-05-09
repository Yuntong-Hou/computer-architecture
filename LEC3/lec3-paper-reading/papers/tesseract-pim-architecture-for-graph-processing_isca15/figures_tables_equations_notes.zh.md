# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | PageRank pseudocode | 展示图处理的邻居遍历和 shared updates。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 3 | conventional systems bottleneck | 说明增加 cores/HMC 外部带宽仍不足。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 3 | Page 4 | Tesseract architecture | 展示 cubes/vault/core/message queue/prefetchers。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 4 | Page 6 | message-triggered prefetching | 解释消息到达和处理间 slack 如何用于预取。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 6 | Page 9 | performance comparison | 主性能结果。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 10 | Page 10 | prefetch efficiency | 展示 timeliness 和 coverage。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 14 | Page 11 | energy | 展示能耗收益。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| 未检测到核心编号表 | - | 论文主要通过图、伪代码和系统描述展示。 | 建议回到 PDF 查看 Section 4 methodology 的参数描述。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Bandwidth scaling relation | Page 3 | internal vs external bandwidth | 16 HMCs expose 8TB/s internal vs 320GB/s external | PIM 的核心来自 memory-capacity-proportional bandwidth。 | 是 |
