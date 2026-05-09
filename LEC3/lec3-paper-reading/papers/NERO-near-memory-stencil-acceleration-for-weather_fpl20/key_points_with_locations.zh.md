# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：天气/气候模型中的 vadvc 和 hdiff 等 compound stencil 具有复杂不规则访问和低算术强度，在 POWER9 CPU 上受 DRAM bandwidth 限制，常规 CPU 优化难以突破 roofline。 | Page 1, Abstract/Introduction | 论文开头明确给出动机。 | 高 | 这是后续方法的出发点。 |
| 2 | 核心方法：NERO 将 HBM-based FPGA 作为 CAPI2 coherent accelerator 接入 POWER9。host 通过 SNAP API 发起任务，数据经 DMA 到 FPGA/HBM；多个 PE 使用独立 HBM ports，并结合 URAM/BRAM/HBM 层次缓存 compound stencil 所需邻域数据。 | Method/design or survey sections | 正文方法/综述结构支撑。 | 高 | 关注作者如何把问题切成可执行机制。 |
| 3 | 关键结果：POWER9 roofline 显示 vadvc/hdiff 受 host DRAM bandwidth 限制，64-thread 性能仅 29.1/58.5 GFLOP/s。 | Page 1, Figure 1 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 4 | 关键结果：HBM-based NERO 对 vadvc 和 hdiff 分别比 16-core POWER9 快 4.2x 和 8.3x。 | Page 1-2; Page 6, Figure 6 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 5 | 关键结果：相同两个 kernel 的能耗分别降低 22x 和 29x。 | Page 1-2; Page 7, Figure 7 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 6 | 关键结果：能效达到约 1.5 GFLOPS/Watt 和 17.3 GFLOPS/Watt。 | Page 1 and Page 7 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 7 | 关键结果：HBM ports 与 PE 数量线性扩展有助于 hdiff/vadvc，但资源和 window size 选择决定面积-性能权衡。 | Page 4-6, Figures 3 and 5-6 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 8 | 局限：本文聚焦 COSMO 的 vadvc/hdiff 两个代表 kernel，不等于完整天气模型端到端加速。 | Page 1-2 and Section 2 | 作者边界或设计假设体现。 | 中 | 迁移/复现时要先检查。 |
| 9 | 追问：CAPI2/POWER9/HBM FPGA 平台特定，迁移到 CXL/CCIX 或不同 FPGA 需重新调优。 | 推断，基于 platform setup | 基于实验范围的推断。 | 中 | 适合后续补读。 |
