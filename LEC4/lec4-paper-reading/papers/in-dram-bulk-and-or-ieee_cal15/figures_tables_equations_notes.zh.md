# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 1 | DRAM subarray | 说明多个 rows 共享 bitlines 和 sense amplifiers | 背景图 |
| Figure 3 | Page 2 | DRAM cell access steps | 解释 precharge、charge sharing、sense amplification | 理解电路行为必读 |
| Figure 4 | Page 2 | simultaneously connecting three cells | 展示三行激活为什么得到多数值 | 核心方法图 |
| Figure 5 | Page 3 | throughput comparison with Intel AVX | 展示 cache 容量变化下 baseline 与 in-DRAM 机制吞吐差异 | 核心结果图 |
| Figure 6 | Page 4 | FastBit range query performance | 展示真实 bitmap range query 的端到端提升 | 应用结果图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Page 4 | FastBit OR time fraction | range query 中 29%-34% 时间花在 OR，平均 31% | 应用动机和收益边界 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| majority expression | Page 2, Section 3 | RA + RB + AB = R(A + B) + R(AB) | R=1 得到 OR，R=0 得到 AND | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
