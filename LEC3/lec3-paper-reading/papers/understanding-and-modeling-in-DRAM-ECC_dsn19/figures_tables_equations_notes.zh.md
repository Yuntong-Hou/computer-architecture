# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | observed vs pre-correction BER | 说明不同 ECC schemes 造成不同观测 BER 曲线。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 2 | Page 3 | DRAM organization | 提供 cell/subarray/device 背景。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 3 | Page 4 | on-die ECC mechanism | 展示 dataword/codeword/post-correction word。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 4 | Page 7 | EINSim flow | 展示 word generator、ECC encoder、error injector、decoder、checker。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 8 | Page 9 | likelihoods of ECC schemes | 反推 ECC scheme 的核心证据。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 10 | Page 10 | retention error rates | 比较 observed post-correction 与 inferred pre-correction。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |
| Figure 11 | Page 11 | temperature dependence | 展示 EIN 恢复 exponential relationship。 | 支撑核心论证 | 建议回到 PDF 查看图中细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 9 | experiment/simulation setup | 列出 reverse-engineering ECC scheme 的实验与仿真参数。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 2 | Page 9 | highest-likelihood models | 列出最可能 ECC models 及 likelihood。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Equation 5-10 | Page 6 | MAP inference objectives | argmax P[model|observations] | 用观测 post-correction errors 反推 ECC scheme 与 pre-correction error rate。 | 是 |
| Equation 3-4 | Page 5 | post-correction PMF model | probability over error-count subsets | 把 ECC 变换和 error distribution 联系起来。 | 是 |
