# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：DRAM 缩放让 cell 更小、更易互相耦合；传统接口假设只访问目标地址不会改变其他地址，但 disturbance errors 破坏了内存隔离和可靠性。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：作者先用 FPGA platform 精确控制 DRAM commands，扫 data pattern、refresh interval、activation interval 和 rows；再用真实系统上的用户态程序通过 clflush 和交替访问绕过 cache，反复打开/关闭 aggressor rows；最后分析 ECC/refresh/PARA 的缓解能力。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：129 个 modules 中 110 个、972 chips 中 836 个出现 disturbance errors。 | Page 1, Abstract; Page 5, Table 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：2012/2013 年制造的所有测试 modules 都存在错误。 | Page 5, Figure 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：最少约 139K 次 wordline toggles/reads 就可诱发 disturbance error。 | Page 1 and Page 7, Figure 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：某些模块中最多每 1.7K cells 就有一个 susceptible cell。 | Page 1, Abstract/Introduction | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：SECDED ECC 不能完全防护，因为可能出现同一 64-bit word 内多 bit errors。 | Page 8, Table 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：提高 refresh rate 可以消除测试错误，但需要大幅增加 refresh，带来功耗/性能开销。 | Page 9, Section 7.2 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：本文主要研究 DDR3-era modules；DDR4/DDR5/HBM 的表现需要后续论文重新测量。 | 推断，基于 sample scope | 基于范围的推断。 | 中 | 后续阅读方向。 |
