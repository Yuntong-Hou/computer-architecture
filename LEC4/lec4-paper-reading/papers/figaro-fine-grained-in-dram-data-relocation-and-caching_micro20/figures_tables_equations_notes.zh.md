# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 1 | DRAM chip organization | 说明 subarray、local row buffer、global row buffer 关系 | 背景核心图 |
| Figure 2 | Page 2 | state-of-the-art cache vs FIGCache | 展示 FIGCache-Fast/Slow 与传统 in-DRAM cache 的差异 | 方法入口 |
| Figure 3 | Page 3 | DRAM bank/subarray detail | 说明 FIGARO 依赖的 LRB/GRB 路径 | 机制背景 |
| Figure 7-8 | Page 9 | single-thread/eight-core performance | FIGCache 核心性能结果 | 核心结果 |
| Figure 9-10 | Page 10 | cache hit rate and row buffer hit rate | 解释性能提升来源 | 核心分析 |
| Figure 11 | Page 10-11 | energy breakdown | 展示 energy reduction 来源 | 核心结果 |
| Figure 12-14 | Page 11-12 | sensitivity studies | 分析 capacity、segment size、replacement policy | 参数边界 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Methodology section | system configuration | 用于 Base/LISA/FIGCache 参数设置 | 复现实验需要 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文重点在 DRAM 操作序列与缓存机制 | 公式不是重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
