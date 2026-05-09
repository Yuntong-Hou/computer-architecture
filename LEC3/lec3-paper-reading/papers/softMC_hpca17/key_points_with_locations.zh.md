# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：DRAM 缩放带来可靠性和 latency 难题，而许多现象无法只靠模拟准确建模；已有商业 tester、FPGA 平台或 BIST 要么不灵活、不开源，要么难用，缺少面向架构研究者的可编程实验平台。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：用户在 host 端用 SoftMC API 生成 instruction sequence；driver 通过 PCIe 将 sequence 发送到 FPGA；SoftMC hardware decode/execute DDR commands，控制 DDR PHY 和 DRAM module，并把读回数据返回 host。API 支持显式 wait cycles，从而可调整 tRCD、tRAS、tRP、tREFI 等 timing。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：SoftMC 是 first open-source FPGA-based experimental memory testing infrastructure，并提供 high-level programming interface。 | Page 1-2, Abstract/Contributions | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：prototype 在 Xilinx ML605/Virtex-6 上实现，当前 DDR interface 400MHz，可连续 issue 两个 commands 间最小 2.5ns。 | Page 6 and Page 10, Section 5.5/7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：retention test 在 refresh interval 达到 1s 前未观察到 retention failures，说明许多 cells retention time 远高于 64ms 标准。 | Page 7, Figure 5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：SoftMC 的 retention results 与 prior studies 一致，验证了平台正确性。 | Page 8, Section 6.1.3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：在 24 modern DRAM chips、三大 manufacturers 上，recently-refreshed/accessed rows 的预期 latency reduction effect 不可观察。 | Page 1-2 and Page 9, Figures 7-8 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：SoftMC limitation：不适合直接评估系统性能，因为 PCIe latency 远高于 DRAM access latency。 | Page 10, Section 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：SoftMC 不能直接作为主存控制器评估系统性能，因为 PCIe latency 约 1us，而 DRAM access latency 约 15-80ns。 | Page 10, Section 7 | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：原型基于 ML605/DDR-era 平台，迁移到 DDR5/HBM/CXL 或 vendor-specific features 需要新 PHY/板卡支持。 | 推断，基于 Section 5.5 | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
