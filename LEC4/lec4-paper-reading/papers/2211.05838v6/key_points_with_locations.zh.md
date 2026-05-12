# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何完全暴露 DRAM command/data interface，让实验程序自由安排 ACT/PRE/READ/WRITE 与时序。 | Page 1-2 / Introduction | 理解 DRAM scaling、RowHammer、retention failures 与 undocumented functionality 必须测试真实芯片；普通系统 memory controller 不允许任意违反 timing parameters，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 现有开源平台 SoftMC 和 LiteX RowHammer Tester 存在接口限制、难用或难扩展问题，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | DRAM Bender 通过 FPGA 直接连接 DRAM PHY/DFI，提供 program memory、data buffers、readback FIFO、periodic operation scheduler 等模块，见 Page 4-7, Section 3。 | 方法章节 / Page 2 及后续对应 section | DRAM Bender 通过 FPGA 直接连接 DRAM PHY/DFI，提供 program memory、data buffers、readback FIFO、periodic operation scheduler 等模块，见 Page 4-7, Section 3。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 案例研究分别构造 double-sided RowHammer、多种 data pattern 和 in-DRAM AND/OR 实验，用真实 DDR4 module 观测 bit flips 与 BER，见 Page 9-12。 | 方法章节后半部分 | 案例研究分别构造 double-sided RowHammer、多种 data pattern 和 in-DRAM AND/OR 实验，用真实 DDR4 module 观测 bit flips 与 BER，见 Page 9-12。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | double-sided RowHammer 中 T 越接近 1，bit-flips 越多；V2 行在 T=64K 时三家厂商平均 bit-flips 为 31.9/9.9/71.2，而 T=1 时为 314.8/50.7/604.9，见 Page 10, Figures 8-9。 | Evaluation / Results | double-sided RowHammer 中 T 越接近 1，bit-flips 越多；V2 行在 T=64K 时三家厂商平均 bit-flips 为 31.9/9.9/71.2，而 T=1 时为 314.8/50.7/604.9，见 Page 10, Figures 8-9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | HCfirst 也受 interleaving 影响：T=1 时为 99K/80K/16K，T=64K 时为 130K/108K/23K，见 Page 10-11, Figures 10-11。 | Evaluation / Results | HCfirst 也受 interleaving 影响：T=1 时为 99K/80K/16K，T=64K 时为 130K/108K/23K，见 Page 10-11, Figures 10-11。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 DRAM Bender，拥有 nonrestrictive instruction set architecture、C++/Python API 和 modular FPGA design，见 Page 1-2 与 Page 4-8。 | Introduction / Contributions | 提出 DRAM Bender，拥有 nonrestrictive instruction set architecture、C++/Python API 和 modular FPGA design，见 Page 1-2 与 Page 4-8。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。 | Limitations / Discussion / Future Work | DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | DDR5 RFM 是否能真正缓解 RowHammer，DRAM Bender 扩展后能否系统验证？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
