# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | CE/UCE timeline | 展示每月服务器受影响比例。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 4 | error distribution | 说明错误高度集中、平均值误导。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figures 3-4 | Page 5 | socket/channel/bank failures | 说明 non-DRAM failure 对错误数的贡献。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figures 5-10 | Page 6-8 | capacity/density/vendor/architecture | 比较硬件因素对 failure rate 的影响。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 13 | Page 8 | workload effect | 说明不同 workload failure rate 可差异很大。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 18 | Page 11 | page offlining effect | 展示真实部署后错误下降。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table I | Page 2 | workload resource requirements | 列出 Web/Hadoop/Ingest/Database/Memcache/Media。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table II | Page 9 | regression factors/model | 列出模型变量、p-value、系数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table III | Page 10 | predicted relative failure rates | 比较低端/高端及设计变体。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Failure model | Page 9, Table II | logistic regression | ln(F/(1-F)) = intercept + feature coefficients | 把硬件/workload/age 等特征映射到 failure probability。 | 是 |
