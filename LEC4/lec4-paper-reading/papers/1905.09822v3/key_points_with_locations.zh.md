# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何让 DRAM 阵列内部直接完成 AND/OR/NOT 等批量按位操作，而不是把数据搬到处理器。 | Page 1-2 / Introduction | 论文指出 bitmap indices、BitWeaving、BitFunnel、DNA sequence mapping、encryption、graph processing 与 binary neural networks 等工作负载都大量使用大 bitvector 上的按位操作；传统 CPU/GPU 执行这些操作时受内存通道带宽与能耗限制，见 Page 1-2, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 作者将 Ambit 放在 Processing using Memory 语境中理解：不同于在内存附近增加逻辑的 Processing-in-Memory，Ambit 尽量复用 DRAM 既有结构与模拟操作特性，见 Page 2, Section 1。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | TRA 同时激活三行，利用三个 cell 与 bitline 的电荷共享，使 sense amplifier 收敛到多数值；当一条控制行为 0 时得到 AND，当控制行为 1 时得到 OR，见 Page 14-16, Section 3.1.1-3.1.3。 | 方法章节 / Page 2 及后续对应 section | TRA 同时激活三行，利用三个 cell 与 bitline 的电荷共享，使 sense amplifier 收敛到多数值；当一条控制行为 0 时得到 AND，当控制行为 1 时得到 OR，见 Page 14-16, Section 3.1.1-3.1.3。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | Ambit 需要在 subarray 内安排 D-group、B-group、C-group 等行组，并通过控制器把应用地址转换为对应 DRAM 行操作，见 Page 18-20, Section 4.1, Figure 19。 | 方法章节后半部分 | Ambit 需要在 subarray 内安排 D-group、B-group、C-group 等行组，并通过控制器把应用地址转换为对应 DRAM 行操作，见 Page 18-20, Section 4.1, Figure 19。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 相对 HMC 2.0 提升 9.7x，见 Page 27, Figure 21。 | Evaluation / Results | Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 相对 HMC 2.0 提升 9.7x，见 Page 27, Figure 21。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 按位操作的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 27, Table 4。 | Evaluation / Results | 按位操作的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 27, Table 4。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 Ambit-AND-OR：通过 Triple-Row Activation (TRA) 让 sense amplifier 实现 majority function，再用控制行得到 AND/OR，见 Page 14-16, Section 3.1。 | Introduction / Contributions | 提出 Ambit-AND-OR：通过 Triple-Row Activation (TRA) 让 sense amplifier 实现 majority function，再用控制行得到 AND/OR，见 Page 14-16, Section 3.1。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 许多操作要求源/目标行位于同一 subarray，数据布局与地址映射压力较大，见 Page 18-21, Sections 4.1-4.2。 | Limitations / Discussion / Future Work | 许多操作要求源/目标行位于同一 subarray，数据布局与地址映射压力较大，见 Page 18-21, Sections 4.1-4.2。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 真实 DDR4/DDR5 芯片中 Ambit 操作的 bit error rate 与数据位置、温度、电压如何变化？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
