# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 阅读建议 |
|---|---|---|---|---|
| Figure 1 | Page 3 | 现代 memory subsystem 层次 | 帮助读者把 channel/module/chip/bank/subarray 放到同一结构中 | 背景图，建议快速看 |
| Figure 16 | Page 15-16 | TRA 电荷共享与 majority operation | 解释 AND/OR 为什么可以在 DRAM sense amplifier 中实现 | 核心图，必须回看 PDF |
| Figure 17 | Page 17 | Dual-contact cell (DCC) | 说明 NOT 的硬件支持 | 理解 Ambit-NOT 的关键 |
| Figure 19 | Page 19-20 | Row address grouping | 说明计算行、控制行、数据行如何组织 | 理解系统集成必读 |
| Figure 20 | Page 21 | AAP primitive 步骤 | 把复制、TRA、结果写回串成可执行序列 | 核心流程图 |
| Figure 21 | Page 27 | bulk bitwise throughput | Ambit 与 CPU/GPU/HMC 的吞吐对比 | 核心结果图 |
| Figure 22-24 | Page 29-31 | 真实应用加速 | bitmap index、BitWeaving、set operations 的端到端效果 | 用于判断实用价值 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 阅读建议 |
|---|---|---|---|---|
| Table 4 | Page 27 | bitwise operation energy | Ambit 将 DRAM/channel energy 降低 25.1x-59.5x | 核心能耗结果 |
| Table 5 | Page 28 | Gem5 simulation parameters | 列出 CPU/cache/memory controller/DRAM 配置 | 复现实验时需要 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号/直观解释 | 是否需要重点掌握 |
|---|---|---|---|---|
| Equation 1 | Page 15, Section 3.1.2 | TRA 中 bitline 电压/多数函数的直观推导 | 三个 cell 的多数值决定 sense amplifier 最终稳定态 | 是 |

## 图表提取说明

- PDF 中的图表图像未单独裁剪导出；本文件基于抽取文本、图表标题和正文解释整理。
- 建议对标注为“核心结果图”或“核心流程图”的项目回到 PDF 查看原图。
