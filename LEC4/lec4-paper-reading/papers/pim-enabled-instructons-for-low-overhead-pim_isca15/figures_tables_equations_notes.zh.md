# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | PageRank pseudocode | 说明 PEI atomic add 的目标代码位置 | 动机图 |
| Figure 2 | Page 3 | in-memory atomic add speedup | 展示 PIM 在不同 graph locality 下既可能加速也可能减速 | 核心动机图 |
| Figure 3 | Page 5 | architecture overview | 展示 PCU、PMU、HMC/vault 结构 | 核心架构图 |
| Figure 6 | Page 9 | speedup comparison by input size | 展示 Host-Only/PIM-Only/Locality-Aware 的 trade-off | 核心结果图 |
| Figure 7 | Page 10 | normalized off-chip transfer | 解释 PIM-Only 为什么在大输入有用、小输入有害 | 关键结果图 |
| Figure 8 | Page 10 | PageRank graph-size sensitivity | 展示 Locality-Aware 随 graph size 逐步增加 memory-side PEI 比例 | 敏感性图 |
| Figure 9 | Page 10 | multiprogrammed workloads | 证明混合 workload 下动态选择仍有效 | 核心结果图 |
| Figure 10 | Page 11 | balanced dispatch | 展示 bandwidth-balance policy 的额外收益 | 优化图 |
| Figure 12 | Page 12 | energy consumption | 展示 Locality-Aware 能耗最低 | 能耗结果图 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 1 | Page 8 | implemented PIM operations | 列出 PEI operation 类型及读写属性 | 实验基础 |
| Table 3 | Page 9 | input sets | 列出 10 个 workloads 的 small/medium/large 输入 | 复现实验重要 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| 未检测到核心编号公式 | 全文 | 本文核心是系统架构、执行策略和模拟评估 | 公式不是主要学习重点 | 否 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
