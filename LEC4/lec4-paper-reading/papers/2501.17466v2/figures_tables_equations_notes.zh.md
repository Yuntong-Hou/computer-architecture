# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 2 | Page 4 | required bit-precision distribution | 说明 narrow values 普遍存在，支撑动态位精度 | 动机关键图 |
| Figure 3 | Page 5 | bit-serial PUD addition | 展示哪些步骤必须串行、哪些可并行 | 方法关键图 |
| Figure 10 | Page 10 | Pareto analysis | 展示不同 µPrograms 的 throughput/energy tradeoff | 选择逻辑关键图 |
| Figure 11 | Page 12 | performance per mm² | Proteus 对 CPU/GPU/SIMDRAM 的核心性能比较 | 核心结果 |
| Figure 12 | Page 13 | energy reduction | 展示 Proteus 能耗收益 | 核心结果 |
| Figure 13 | Page 13 | mapping/format conversion overhead | 说明转换成本 | 开销分析 |
| Figure 14 | Page 14 | tensor core comparison | 窄精度 GEMM 下与 A100 tensor cores 比较 | 重点看 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 12 | evaluated system configurations | 列出 CPU/GPU/SIMDRAM/Proteus 参数 | 复现关键 |
| Table 3 | Page 12 | evaluated applications | 列出应用、内存 footprint、bit-precision 和 PUD instructions | 实验设计关键 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文重点是 runtime/µProgram 选择和系统评估 | 公式不是重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
