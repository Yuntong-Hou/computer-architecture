# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 2 | DRAM hierarchy | 说明 bank/subarray/row buffer 层次 | 背景图 |
| Figure 3 | Page 3 | command sequence for in-memory operations | 定义 T1/T2 timing intervals | 核心方法图 |
| Figure 4 | Page 4 | row copy timeline | 解释如何用越界命令完成 row copy | 核心方法图 |
| Figure 5-6 | Page 4-5 | logical AND/OR timeline | 展示 AND/OR 的 charge sharing 过程 | 核心方法图 |
| Figure 9 | Page 8 | testing framework | 展示 FPGA/SoftMC 测试平台 | 实验平台图 |
| Figure 10 | Page 9 | timing heatmap | 展示不同 DRAM groups 的成功 timing windows | 核心结果图 |
| Figure 11 | Page 10 | CDF of column success ratio | 展示 row copy 与 AND/OR 稳定性 | 核心结果图 |
| Figure 12-13 | Page 11 | voltage/temperature sensitivity | 展示环境变化对成功率和 timing 的影响 | 鲁棒性结果 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 2 | Page 11 | memory command cycles for 1-bit operation | row copy/SHIFT/AND/OR/XOR/ADD 的 command cycles | 理解 bit-serial 成本必读 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| Equations 2-5 | Page 6, Section 4 | 用 AND/OR 和 complement pairs 构造 AND/OR/NAND/XOR | 展示 non-inverting primitives 的计算完备性路线 | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
