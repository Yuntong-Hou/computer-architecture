# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 1 | FR-FCFS vs optimistic | 说明传统调度造成带宽和性能损失。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 3 | RL agent mapping | 把 DRAM scheduler 映射为 RL agent。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 4 | Page 4 | RL scheduler overview | 展示 Q-value 估计和动作选择。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 6 | Page 7 | Q-value estimation pipeline | 展示 CMAC/hashing 硬件结构。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 7 | Page 9 | performance comparison | 核心性能结果。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 15 | Page 11 | bandwidth efficiency | 展示 RL 与双通道配置的关系。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 8 | core parameters | 列出 CMP core 模型。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 8 | L2/DRAM subsystem | 列出 DDR2-800 memory system 参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 3 | Page 8 | applications/input sizes | 列出 9 个 parallel workloads。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Discounted reward | Page 3 | RL objective | sum of discounted future rewards with gamma | 用未来 reward 把调度长期影响纳入决策。 | 是 |
| Q-value update | Page 5 | temporal-difference learning | Q(sprev, aprev) updated from reward and next-state max Q | 把当前动作归因到未来带宽利用收益。 | 是 |
