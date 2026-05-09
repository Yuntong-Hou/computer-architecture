# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | RowHammer vs RowPress | RowPress 用更长 open time 显著降低 ACmin | 说明 DRAM scaling 问题不只 activation count | 和 RowPress 论文联读 |
| Figure 2 | Page 2 | VRD 阈值变化 | 同一 row 的 read disturbance threshold 会变化 | 支撑 self-managing/dynamic mitigation 需求 | 和 VRD 论文联读 |
| Figure 3 | Page 3 | SMD 概览 | DRAM 能对维护区域返回 nack 并自主维护 | memory-centric maintenance 的关键接口 | 重点看 MC/DRAM 分工 |
| Figure 4 | Page 4 | Tesseract | 3D-stacked memory logic layer 执行 graph analytics | PNM 代表案例 | 与 Tesseract 论文联读 |
| Figure 5 | Page 4 | PAPI LLM inference | 不同 PIM units 处理 FC 和 attention/KV-cache | 连接 PIM 与 LLM | 看 kernel-to-PIM mapping |
| Figure 6 | Page 5 | CENT | CXL + GDDR6-PIM 协同 LLM inference | 显示可扩展 PNM 系统 | 关注 disaggregated PIM |
| Figure 7 | Page 5 | COTS DRAM PUM 成功率 | 未修改 DRAM 可执行多种 bulk operations | 支撑 PUM 可行性 | 重点看成功率与鲁棒性 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| 未发现核心表格 | 全文 | 本文以概念图和引用结果为主 | 无独立实验表 | 不是实验论文 | 重点读图和引用案例 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 无核心公式 | 全文 | 路线图/综述文章 | 不适用 | 重点是系统设计思想 | 否 |
