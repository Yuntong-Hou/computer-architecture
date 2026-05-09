# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 核心问题是数据搬移瓶颈，而不是单纯算力不足 | Page 1, Abstract; Page 1, Introduction | 作者指出 data-intensive applications 在当前系统中浪费 execution cycles 和 energy，原因是 computation units 和 memory units 之间的数据移动昂贵 | 高 | 这奠定了近内存计算的动机 |
| 2 | 目标应用是 genome analysis 和 weather modeling | Page 1-2, Introduction | 文中明确选择 SneakySnake pre-alignment filtering 与 COSMO 的 vadvc/hdiff kernels | 高 | 两个案例分别代表不规则访问和 stencil-like 访问 |
| 3 | POWER9 roofline 显示三个 kernel 受 memory hierarchy 限制 | Page 2, Figure 1 | Figure 1 把 POWER9 roofline 与 FPGA roofline 放在一起，三个 workload 的点远低于 CPU peak | 高 | 这是“为什么要用 HBM-FPGA”的主要证据 |
| 4 | FPGA-HBM 平台结构 | Page 3, Figure 2 | FPGA 连接两个 HBM stacks，共 32 个 pseudo channels，并通过 OCAPI 连接 POWER9 | 高 | 说明近内存不是抽象概念，而是具体硬件拓扑 |
| 5 | SneakySnake 的算法特征是不规则 chip maze 访问 | Page 3-4, Case Study 1; Figure 3 | 作者解释它把 ASM 转换为 SNR 问题，只计算部分 chip maze | 中 | 这种不规则访问解释了 cache 效果有限 |
| 6 | COSMO kernels 代表 compound stencil | Page 5, Case Study 2; Figure 4 | hdiff/vadvc 访问 3D grid，涉及多次 element-wise/stencil 计算 | 中 | stencil 可并行但容易受内存带宽和复用策略影响 |
| 7 | 设计利用 HBM、BRAM、URAM 和 PE 并行 | Page 6-7, Accelerator Design | 使用 greedy algorithm 选择 memory hierarchy，并通过 HLS pipeline、array partitioning、data partitioning 优化 PE | 高 | 这是方法部分的核心工程设计 |
| 8 | 主要性能结果 | Page 7-8, Figure 6 | HBM+OCAPI 对 SneakySnake/vadvc/hdiff 分别比 POWER9 快 27.4x/5.3x/12.7x | 高 | 结论最直接的支撑 |
| 9 | 主要能效结果 | Page 9, Energy Efficiency Analysis | HBM+OCAPI 对三者能效分别提升 133x/12x/35x | 高 | NMC 的价值不只是速度，也包括能耗 |
| 10 | HBM channel 与 PE 数不是越多越好 | Page 8-10, Performance and Energy Analysis | multi-channel-single PE 有时低于 single-channel-single PE；能效可能在增加 PE 后下降 | 高 | 这提醒读者关注资源、带宽和功耗的交互 |
| 11 | FPGA resource 是现实约束 | Page 10, Table 1 | BRAM 使用率在三个设计中都很高，hdiff 达 96% BRAM | 中 | 资源瓶颈决定架构方案能否扩展 |
| 12 | 局限在 kernel-level 和平台特定性 | Page 10, Discussion | 作者讨论 timing closure、SLR 到 HBM 连接、PE 数和能效饱和 | 中 | 结果不能无条件外推到所有应用 |
