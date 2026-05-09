# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | memory error outcomes | 定义 overwrite/logic masking、incorrect response、crash。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 3 | Page 6 | inter-application vulnerability | 展示三类应用差异。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 4 | Page 6 | memory region vulnerability | 展示同一应用内部区域差异。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 7 | Page 9 | heterogeneous mapping flow | 展示 design-space exploration。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 8 | Page 11 | tolerable errors/month | 比较应用可容忍错误数。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 1 | ECC techniques and cost | 比较 Parity/SECDED/Chipkill/RAIM/Mirroring 的容量开销。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 4 | Page 8 | design dimensions | 列出硬件技术、软件响应和使用粒度。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 5 | Page 7 | recoverable memory | 量化 WebSearch 可恢复数据比例。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 6 | Page 10 | cost/availability tradeoff | 展示 Detect&Recover/L 的成本收益。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Safe ratio | Page 3-4, Section III-B | 衡量某地址错误被 overwrite masking 的机会 | safe duration / total duration | 写多读少的数据更可能覆盖错误而不暴露。 | 是 |
