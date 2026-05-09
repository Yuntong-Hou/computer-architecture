# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 3 | Page 4 | testing infrastructure | 展示 FPGA board、temperature controller、heat chamber。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 5-7 | Page 5-6 | testing rounds efficacy | 显示 testing 能快速降低但不能消除新 failure 概率。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 9-12 | Page 7-8 | VRT behavior | 展示 cells 在不同轮次/状态间切换。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 15-16 | Page 9 | guardband coverage | 量化 2X 到 5X guardband 的覆盖率。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 17-18 | Page 10-11 | ECC and prior techniques | 展示 ECC 组合与 VS-ECC/Hi-ECC 的可靠性。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 4 | tested DRAM modules | 列出测试模块与厂商信息。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| ECC failure probability | Appendix / Page 13-14 | 估计 ECC 下 uncorrectable failure probability | 基于 per-cell failure probability 与 ECC block correction strength | ECC 强度和错误粒度决定 residual risk。 | 中 |
