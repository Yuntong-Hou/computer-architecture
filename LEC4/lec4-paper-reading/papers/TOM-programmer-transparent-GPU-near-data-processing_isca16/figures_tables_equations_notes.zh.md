# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 1 | NDP GPU system overview | 展示 main GPU、memory stacks、logic-layer SMs 和 cross-stack links | 架构入口 |
| Figure 2 | Page 2 | ideal offloading speedup | 说明静态 offload selection 的潜在收益 | 动机图 |
| Figure 3 | Page 2 | ideal memory mapping speedup | 说明数据映射也很重要 | 动机图 |
| Figure 7 | Page 6 | NDP hardware block diagram | 展示 TOM 需要的硬件/软件结构 | 实现图 |
| Figure 8 | Page 10 | speedup under policies | TOM 核心性能结果 | 核心结果 |
| Figure 9-10 | Page 10 | memory traffic and energy | 展示 traffic/energy 降低 | 核心结果 |
| Figure 11-13 | Page 11 | warp capacity/internal bandwidth sensitivity | 说明设计参数影响 | 敏感性分析 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 8-9 | evaluated workloads | 列出 10 个 memory-intensive GPU workloads | 实验设计 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| Equations 1-4 | Page 3 | offloading bandwidth cost-benefit | 估计 live-in/out register transfer 与 load/store traffic 节省 | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
