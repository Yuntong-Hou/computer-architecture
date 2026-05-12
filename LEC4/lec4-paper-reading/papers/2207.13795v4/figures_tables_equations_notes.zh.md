# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 2 | Page 5 | cache block 在 mats/sectors 中的放置与 burst transfer | 说明为什么可以按 word/sector 细粒度传输 | 方法背景图 |
| Figure 3 | Page 5 | normalized DRAM access/activation energy | 支撑细粒度化动机 | 建议回看 |
| Figure 7 | Page 10 | DRAM command power and energy | 量化 VBL/SA 对 ACT/READ/WRITE 的能耗影响 | 核心结果图 |
| Figure 8 | Page 11 | LLC MPKI under configurations | 展示 Basic、LA、SP 的 miss 影响 | 系统集成关键 |
| Figure 9-12 | Page 11-13 | performance and energy results | 展示不同 workload 和比较对象下的性能/能耗 | 核心评估图 |
| Figure 13-15 | Page 14-16 | multi-channel、dynamic、prefetching 讨论 | 解释边界场景 | 讨论部分 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 3 | Page 9 | workload classification | 按 LLC MPKI 组织 41 个 workload | 实验设计关键 |
| Table 2 | Page 9 附近 | modeled DRAM chip parameters | 用于面积/能耗建模 | 复现需要 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文重点在架构机制和模拟评估 | 公式不是主要阅读对象 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
