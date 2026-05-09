# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | POWER9 roofline 与 FPGA roofline | SneakySnake、vadvc、hdiff 在 CPU 上受 memory bandwidth / hierarchy 限制 | 支撑全文动机：瓶颈是数据搬移 | 先读此图，理解 arithmetic intensity 和 attainable performance |
| Figure 2 | Page 3 | POWER9 + HBM FPGA 系统结构 | FPGA 连接两个 HBM2 stacks，并通过 OCAPI 与 POWER9 通信 | 解释 near-memory accelerator 的硬件基础 | 重点看 HBM channels、AFU、PE、URAM/BRAM |
| Figure 3 | Page 4 | SneakySnake chip maze 示例 | 将 pre-alignment filtering 转化为 chip maze / SNR-like problem | 帮助理解为什么访问模式不规则 | 结合 Case Study 1 阅读 |
| Figure 4 | Page 5 | Horizontal diffusion kernel composition | 展示 hdiff stencil 中 grid point 的依赖 | 说明 weather kernel 的数据复用和访存复杂性 | 初学者可先把它看作 3D stencil |
| Figure 5 | Page 6 | Host DRAM 到 FPGA memory 的 data transfer flow | 描述数据从 host 到 FPGA/HBM 再回写的路径 | 说明加速不只是 PE 计算，还包括搬运路径 | 关注 transfer engine 和 HBM write/read |
| Figure 6 | Page 8 | Runtime 与 energy efficiency 结果 | 比较不同 PE 数、HBM/DDR4、CAPI2/OCAPI、POWER9 | 全文最重要实验图 | 重点看 HBM+OCAPI、DDR4 饱和和能效峰值 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 10 | FPGA resource utilization | BRAM 使用率很高；vadvc 资源消耗大；SneakySnake 不用 DSP | 展示可扩展性的硬件资源约束 | 与 Figure 6 一起看，理解为什么 PE 数有限 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 无核心编号公式 | 全文 | 本文主要是系统设计与实测评估 | 涉及 roofline、runtime、energy efficiency，但未依赖新公式 | 关注图表和实验设计即可 | 否 |
