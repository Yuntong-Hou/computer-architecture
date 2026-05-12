# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 2 | DRAM chip organization | 展示 banks、subarrays、row buffer 和 internal bus | 背景图 |
| Figure 3 | Page 3 | DRAM subarray access steps | 解释 ACTIVATE/READ/PRECHARGE | 背景核心图 |
| Figure 4 | Page 4 | Fast Parallel Mode | 展示同 subarray row copy 的电路状态 | 核心方法图 |
| Figure 5 | Page 5 | Pipelined Serial Mode | 展示 source/destination bank 和 TRANSFER 数据流 | 核心方法图 |
| Figure 8 | Page 9 | forkbench performance | 展示 FPM/PSM 在不同 N/S 下的 IPC 提升 | 核心结果图 |
| Figure 9 | Page 10 | forkbench DRAM energy | 展示 FPM/PSM 能耗降低 | 核心结果图 |
| Figure 11 | Page 10 | application IPC with RowClone-ZI | 展示 RowClone-ZI 解决初始化后 cache miss 问题 | 关键结果图 |
| Figure 12-13 | Page 11 | multi-core evaluation | 展示多核 weighted speedup 与 copy intensity 关系 | 核心结果图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Page 5 | memcopy/meminit semantics | 定义 RowClone 暴露给软件的 ISA 指令 | 系统接口 |
| Table 3 | Page 9 | 4KB latency and energy | FPM/PSM 相对 baseline 的 raw benefit | 核心表 |
| Table 4 | Page 10 | copy/initialization-intensive benchmarks | 列出六个应用 | 实验设计 |
| Table 5 | Page 11 | energy and bandwidth reduction | RowClone-ZI 在所有六个应用上降低 energy/bandwidth | 核心表 |
| Table 7 | Page 11 | multi-core metrics | 2/4/8-core 下 speedup、fairness、bandwidth、energy | 核心表 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文主要是 DRAM 操作机制与系统评估 | 公式不是主要学习重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
