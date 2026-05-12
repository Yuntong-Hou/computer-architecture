# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM subarray organization | 解释 rows 与 sense amplifiers 的共享关系 | 背景图 |
| Figure 5 | Page 6 | dual-contact cell | 展示 NOT 的硬件机制 | 核心方法图 |
| Figure 7 | Page 7 | row address grouping | 展示 designated rows 与控制行组织 | 系统实现关键 |
| Figure 8 | Page 8 | bitwise command sequences | 展示不同 bitwise operations 的命令序列 | 核心流程 |
| Figure 9 | Page 10 | throughput comparison | 展示 Ambit 与 CPU/GPU/HMC 的吞吐差距 | 核心结果 |
| Figure 10-12 | Page 11-12 | application performance | 展示 bitmap、BitWeaving、set operations 的端到端收益 | 核心结果 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Page 7 | B-group address mapping | 说明保留地址如何映射到 ACTIVATE/PRECHARGE 控制 | 实现细节 |
| Table 2 | Page 10 | process variation effect | TRA 在不同 variation 下错误率 | 可靠性证据 |
| Table 3 | Page 11 | energy of bitwise operations | Ambit 能耗降低 25.1x-59.5x | 核心结果 |
| Table 4 | Page 11 | simulation parameters | Gem5/full-system 参数 | 复现实验 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| Equation 1 | Page 5 | TRA 电荷共享/多数函数 | 解释三行激活时 sense amplifier 为什么输出 majority | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
