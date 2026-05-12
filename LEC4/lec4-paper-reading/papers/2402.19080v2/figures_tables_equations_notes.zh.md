# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM module/subarray/mat 结构 | 说明 MIMDRAM 利用 mat 作为细粒度执行资源 | 背景关键图 |
| Figure 6 | Page 7 | PUD vector reduction 示例 | 展示 MIMDRAM 如何在 DRAM 内支持 reduction | 核心方法图 |
| Figure 9 | Page 12 | single-application SIMD utilization/performance/energy | 展示对 SIMDRAM、CPU、GPU 的核心收益 | 核心结果 |
| Figure 10 | Page 13 | multi-programmed workload results | 展示 throughput、turnaround、fairness | 核心结果 |
| Figure 11 | Page 13 | CPU multi-programmed comparison | 说明 MIMDRAM 相对 CPU 的 throughput 提升 | 建议查看 |
| Figure 14 | Page 14 | SALP/BLP scalability | 说明利用更多 subarrays/banks 后的潜力 | 理解边界必读 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 11 | system configuration | 给出 CPU/GPU/SIMDRAM/MIMDRAM 模型参数 | 复现实验需要 |
| Table 3 | Page 11 | evaluated applications | 列出 12 个应用、benchmark suite 和 PUD 指令类型 | 实验设计关键 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文重点是架构、编译和系统评估 | 公式不是重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
