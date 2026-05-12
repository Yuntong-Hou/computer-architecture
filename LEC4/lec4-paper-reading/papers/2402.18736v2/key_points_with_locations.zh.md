# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | COTS DRAM 芯片是否能执行功能完备的布尔操作集合，而不修改芯片或接口。 | Page 1-2 / Introduction | Processing-using-DRAM (PuD) 利用 DRAM 电路的模拟操作特性在内存内部执行大规模 bitwise computation，从而减少 CPU/GPU 与主存之间的数据搬移，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 已有真实芯片实验主要展示 MAJ3、AND 和 OR，但还没有在 COTS DRAM 中展示 functionally-complete operation set，例如 NOT 与 NAND/NOR，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | NOT 的核心假设是：在 open-bitline 架构中，同时连接 sense amplifier 两端的两个 DRAM cell，可利用反相端把一个 cell 的值取反并写入另一个 cell，见 Page 2, Figure 1a 与 Page 7, Section 5.1。 | 方法章节 / Page 2 及后续对应 section | NOT 的核心假设是：在 open-bitline 架构中，同时连接 sense amplifier 两端的两个 DRAM cell，可利用反相端把一个 cell 的值取反并写入另一个 cell，见 Page 2, Figure 1a 与 Page 7, Section 5.1。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 实验覆盖 row distance、data pattern、temperature、speed rate、chip density 和 die revision 等因素，见 Page 8-14。 | 方法章节后半部分 | 实验覆盖 row distance、data pattern、temperature、speed rate、chip density 和 die revision 等因素，见 Page 8-14。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | COTS DRAM 可执行 NOT，平均 success rate 为 98.37%，见 Page 1-2 与 Page 8-9。 | Evaluation / Results | COTS DRAM 可执行 NOT，平均 success rate 为 98.37%，见 Page 1-2 与 Page 8-9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 16-input AND、NAND、OR、NOR 的平均 success rate 分别为 94.94%、94.94%、95.85%、95.87%，见 Page 12, Figure 15。 | Evaluation / Results | 16-input AND、NAND、OR、NOR 的平均 success rate 分别为 94.94%、94.94%、95.85%、95.87%，见 Page 12, Figure 15。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 首次实验展示 unmodified off-the-shelf DRAM chips 能执行 NOT、NAND、NOR，以及多输入 NAND/NOR/AND/OR，见 Page 2。 | Introduction / Contributions | 首次实验展示 unmodified off-the-shelf DRAM chips 能执行 NOT、NAND、NOR，以及多输入 NAND/NOR/AND/OR，见 Page 2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。 | Limitations / Discussion / Future Work | 并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 为什么 Micron/Samsung 芯片不完整支持这些操作，是否由命令过滤或 row decoder 设计造成？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
