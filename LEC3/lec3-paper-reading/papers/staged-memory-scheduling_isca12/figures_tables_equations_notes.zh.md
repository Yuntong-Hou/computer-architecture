# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 1 | limited visibility | 说明 GPU requests 占据 buffer 后 CPU 可见性下降。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 4 | Page 4 | SMS organization | 展示三阶段结构和 FIFO 组织。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 5 | Page 8 | CPU/GPU performance | 主结果：CPU 提升与 GPU frame rate tradeoff。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 7 | Page 9 | CGWS/fairness with GPUweight=1 | 展示 CPU 重要场景下的系统收益。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 8 | Page 10 | CGWS with GPUweight=1000 | 展示 GPU 重要场景下 SMS0 的配置收益。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figures 9-10 | Page 10 | scalability | 展示 core/channel 扩展下性能和公平性。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 6 | SMS hardware storage | 列出每阶段硬件存储开销。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 7 | simulation parameters | 列出 CPU/GPU/DRAM 参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 5 | Page 11 | power and area | SMS 低 leakage/area。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Equation 1 | Page 7 | CPU weighted speedup | sum of IPC_shared/IPC_alone | 衡量 CPU 多程序性能。 | 是 |
| Equation 2 | Page 7 | GPU speedup/frame rate | shared frame rate / alone frame rate | 衡量 GPU 性能。 | 是 |
| Equation 3 | Page 8 | CGWS | CPUWS + GPUweight * GPUSpeedup | 用 GPUweight 表示 CPU/GPU 重要性。 | 是 |
| Equation 4 | Page 8 | Unfairness | max slowdown across CPU cores and GPU | 衡量最差 slowdown。 | 是 |
