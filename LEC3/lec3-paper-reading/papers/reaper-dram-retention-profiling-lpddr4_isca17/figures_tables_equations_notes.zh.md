# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM array and retention failure | 解释 refresh interval 延长如何产生 retention failure。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 5 | retention failure rates | 展示 refresh interval 增大导致 BER 上升。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 5 | Page 6 | brute-force coverage over iterations | 说明 brute-force 在短时间内 coverage 不足。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 9 | Page 8 | coverage and false positive tradeoff | 展示 reach conditions 对 coverage/false positives 的影响。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 10 | Page 8 | profiling runtime | 展示 reach conditions 如何带来 2.5x/3.5x speedup。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 13 | Page 12 | end-to-end performance/power | 展示 REAPER 对系统性能和 DRAM power 的收益。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 9 | tolerable RBER | 把 UBER 目标和 ECC 强度映射为可容忍 bit errors。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 10 | evaluated system configuration | 列出系统模拟配置。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Equation 2-6 | Page 8-9 | UBER/RBER model | UBER as probability of uncorrectable ECC word error | 用 raw bit failure rate 推导系统不可纠错错误率。 | 是 |
| Equation 7 | Page 9 | profile longevity | T from tolerable missed/new failures | 估计 profile 何时需要重新运行。 | 是 |
