# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | DRAM organization | 复习 channel/rank/chip/bank 结构。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 5 | SoftMC infrastructure | 展示 host/API/driver/FPGA/DRAM 关系。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 3 | Page 5 | instruction types | 展示 SoftMC DDR/WAIT/BUSDIR/END instruction encoding。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 4 | Page 6 | hardware architecture | 展示 instruction receiver/dispatcher/executor/read capture/calibration。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 5 | Page 7 | retention failures | 复现 retention behavior。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figures 7-8 | Page 9 | tRCD/tRAS latency experiments | 验证 latency reduction effect 不可观察。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| 未检测到核心编号表 | - | 论文主要用架构图、代码片段和实验图展示结果。 | 建议回到 PDF 查看 Program 1/2 和 Figures 2-8。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| DDR timing constraints | Page 3 | timing parameter constraints | tRCD/tRAS/tRP/tWR/tWTR/tRTW/tREFI/tRFC | SoftMC 通过 WAIT instruction 显式控制这些 timing。 | 是 |
