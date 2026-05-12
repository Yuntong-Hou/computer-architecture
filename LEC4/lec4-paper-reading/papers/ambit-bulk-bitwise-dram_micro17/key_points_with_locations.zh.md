# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何在 DRAM array 内实现 AND/OR/NOT 且保持低面积开销。 | Page 1-2 / Introduction | bitmap indices、BitWeaving、BitFunnel、DNA、encryption、graph 和 networking 等应用大量使用 bulk bitwise operations，传统 CPU/GPU/HMC 受外部内存带宽限制，见 Page 1-2。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | Ambit 的目标是使用 DRAM analog operation 和内部 row buffer/bank parallelism，而不是在 logic layer 增加普通计算单元，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | TRA 同时激活三行共享同一组 sense amplifiers 的 rows，产生三输入 majority；将其中一行初始化为 0 得到 AND，初始化为 1 得到 OR，见 Page 4-5。 | 方法章节 / Page 2 及后续对应 section | TRA 同时激活三行共享同一组 sense amplifiers 的 rows，产生三输入 majority；将其中一行初始化为 0 得到 AND，初始化为 1 得到 OR，见 Page 4-5。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 系统接口包括 bbop instructions/API、cache coherence handling、ECC/data scrambling 处理，见 Page 8-9。 | 方法章节后半部分 | 系统接口包括 bbop instructions/API、cache coherence handling、ECC/data scrambling 处理，见 Page 8-9。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 比 HMC 2.0 高 9.7x，见 Page 10, Figure 9。 | Evaluation / Results | Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 比 HMC 2.0 高 9.7x，见 Page 10, Figure 9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | bitwise operations 的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 11, Table 3。 | Evaluation / Results | bitwise operations 的 DRAM/channel energy 降低 25.1x-59.5x，见 Page 11, Table 3。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 Ambit-AND-OR，通过 triple-row activation 实现 majority function 并由控制行得到 AND/OR，见 Page 4-6, Section 3。 | Introduction / Contributions | 提出 Ambit-AND-OR，通过 triple-row activation 实现 majority function 并由控制行得到 AND/OR，见 Page 4-6, Section 3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | Ambit 要求操作数映射到同一 subarray，并需要 RowClone 在 designated rows 间搬移，见 Page 5-8。 | Limitations / Discussion / Future Work | Ambit 要求操作数映射到同一 subarray，并需要 RowClone 在 designated rows 间搬移，见 Page 5-8。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | Ambit 在真实 DDR4/DDR5 芯片上的错误率与 PuDHammer 风险如何权衡？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
