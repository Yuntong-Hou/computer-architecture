# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM organization | 说明 SIMDRAM 依赖的 subarray/bitline/row buffer 结构 | 背景图 |
| Figure 2 | Page 4 | SIMDRAM subarray organization | 展示 D-group/C-group/B-group rows 与 DCC | 核心结构图 |
| Figure 3 | Page 5 | SIMDRAM framework | 展示 MAJ/NOT synthesis、row allocation、µProgram execution 三步 | 核心总览图 |
| Figure 9 | Page 12 | throughput of 16 operations | 比较 CPU/GPU/Ambit/SIMDRAM | 核心结果图 |
| Figure 10 | Page 13 | energy efficiency of 16 operations | 展示 SIMDRAM throughput per watt 优势 | 核心结果图 |
| Figure 11 | Page 13 | real-world kernel speedup | 展示 7 个 kernels 的端到端收益 | 核心结果图 |
| Figure 12 | Page 13 | DualityCache comparison | 展示考虑 DRAM-to-cache movement 后 SIMDRAM 优势 | 对比图 |
| Figure 13 | Page 14 | data movement overhead | 展示 intra/inter-bank movement overhead | 开销图 |
| Figure 14 | Page 15 | data transposition overhead | 展示 vertical layout 转置成本 | 开销图 |
| Figure 15 | Page 19 | full addition MIG synthesis | 展示 MAJ/NOT transformation 过程 | 方法细节图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 11 | evaluated system configurations | 列出 CPU/GPU/Ambit/SIMDRAM 参数 | 实验设计 |
| Table 3 | Page 14 | TRA/QRA failure rates | TRA/TRAb2b 比 QRA 更可靠，±5% 无错误 | 可靠性核心表 |
| Table 4 | Page 19 | MAJ/NOT transformation rules | MIG 优化规则 | 方法核心表 |
| Table 5 | Page 21 | evaluated SIMDRAM operations | 16 operations 的 latency scaling 和表达式 | 操作覆盖表 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| MAJ(A,B,C)=A·B+A·C+B·C | Page 3, Section 2.2.2 | 三输入 majority operation 定义 | TRA 的逻辑抽象 | 是 |
| MIG transformation rules | Page 19, Table 4 | 把 AND/OR/NOT graph 转成 MAJ/NOT graph | SIMDRAM synthesis 的形式化基础 | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
