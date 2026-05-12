# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 1 | RowClone vs LISA transfer path | 对比窄 internal data bus 与 LISA bitline links | 动机图 |
| Figure 3 | Page 4 | LISA subarray links | 展示 isolation transistors 如何连接相邻 bitlines | 核心架构图 |
| Figure 7 | Page 6 | LISA-RISC command timeline | 对比 LISA-RISC 与 RC-InterSA 的 row copy 步骤 | 核心流程图 |
| Figure 8 | Page 7 | 8KB copy latency and energy | 展示 LISA-RISC 的低 latency/energy | 核心结果图 |
| Figure 13 | Page 10 | four-core copy evaluation | 展示 LISA-RISC weighted speedup 和 energy | 核心结果图 |
| Figure 14 | Page 11 | LISA-VILLA performance | 展示 fast-subarray caching 的效果和 RC-InterSA 反例 | 核心结果图 |
| Figure 15 | Page 11 | LISA-LIP speedup | 展示 precharge 加速收益 | 结果图 |
| Figure 16 | Page 11 | combined LISA applications | 展示 RISC/VILLA/LIP 的叠加收益 | 综合结果图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Page 7 | 8KB copy latency and energy | LISA-RISC 1/7/15-hop 大幅低于 memcpy 与 RC-InterSA | 核心表 |
| Table 4 | Page 11 | copy distance sensitivity | hop 数越大收益越小，但 63-hop 仍有 42.4% WS improvement | 敏感性分析 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文核心是 DRAM substrate、电路 timing 与系统评估 | 公式不是主要学习重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
