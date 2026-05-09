# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | DRAM cells | 说明 cell/wordline/bitline 与 disturbance 根因。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 3 | Page 5 | errors by manufacturing date | 展示新芯片更脆弱。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 6 | Page 7 | errors vs activations | 确定触发 bitflip 所需 activation 数。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 8 | Page 8 | affected rows | 展示 victim rows 与 aggressors 的位置关系。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 9 | Page 8 | victim row offsets | 说明邻近行受影响最明显。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 2 | Page 4 | real-system bit flips | 展示 Intel/AMD 系统中用户态程序诱发错误。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 3 | Page 5 | sample population | 列出 modules/chips 与出错数量。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 5 | Page 8 | ECC implications | 说明 SECDED 难以覆盖多 bit flips。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |
| Table 7 | Page 10 | PARA failure probability | 量化 PARA 概率参数的可靠性。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| PARA probability | Page 9-10, Section 7.4/Table 7 | 概率相邻行刷新可靠性估计 | row close 后以 probability p refresh adjacent rows | p 越大，攻击窗口内漏刷 victim rows 的概率指数下降，但 refresh 开销上升。 | 是 |
