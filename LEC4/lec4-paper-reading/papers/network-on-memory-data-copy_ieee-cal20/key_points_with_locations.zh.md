# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何在 3D-stacked memory 的多个 banks 之间直接、快速地复制数据。 | Page 1-2 / Introduction | bulk data copy 在程序和 OS 服务中很常见，传统系统需要 DRAM 与处理器之间来回复制；RowClone/LISA 减少了部分搬移，但 inter-bank copy 仍受共享 internal bus 限制，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 3D-stacked memories 如 HMC/HBM 有数百个 banks 和多个 memory controllers，跨 bank copy 更常见，也更不适合单一共享 bus，见 Page 1, Section 1。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | NoM 给每个 bank 增加简单 circuit-switched router，包括 crossbar、single-cycle latch、local slot table/controller 和 links；bank 可通过 NoM links 或传统 bus 发送/接收数据，见 Page 2, Figure 1。 | 方法章节 / Page 2 及后续对应 section | NoM 给每个 bank 增加简单 circuit-switched router，包括 crossbar、single-cycle latch、local slot table/controller 和 links；bank 可通过 NoM links 或传统 bus 发送/接收数据，见 Page 2, Figure 1。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | NoM full 3D mesh 使用 X/Y/Z 邻接 links；NoM-Light 删除额外 vertical mesh links，并复用 HMC 既有 TSVs，见 Page 3, Section 2.3。 | 方法章节后半部分 | NoM full 3D mesh 使用 X/Y/Z 邻接 links；NoM-Light 删除额外 vertical mesh links，并复用 HMC 既有 TSVs，见 Page 3, Section 2.3。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | NoM 相比 RowClone 平均 IPC 高 75%，因为它加速 inter-bank copies 并允许多个 inter-bank copies 与其他 memory accesses 并发执行，见 Page 4, Section 3/Figure 4。 | Evaluation / Results | NoM 相比 RowClone 平均 IPC 高 75%，因为它加速 inter-bank copies 并允许多个 inter-bank copies 与其他 memory accesses 并发执行，见 Page 4, Section 3/Figure 4。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 摘要和结论报告 NoM 相比 conventional 3D-stacked DRAM 平均性能提升 3.8x，相比 RowClone 提升 75%，见 Page 1, Abstract 与 Page 4, Conclusion。 | Evaluation / Results | 摘要和结论报告 NoM 相比 conventional 3D-stacked DRAM 平均性能提升 3.8x，相比 RowClone 提升 75%，见 Page 1, Abstract 与 Page 4, Conclusion。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 Network-on-Memory (NoM)，用 3D mesh links 连接 highly-banked memory 中相邻 banks，见 Page 1-2, Section 2。 | Introduction / Contributions | 提出 Network-on-Memory (NoM)，用 3D mesh links 连接 highly-banked memory 中相邻 banks，见 Page 1-2, Section 2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | NoM 主要针对 highly-banked 3D-stacked memory；传统低 bank 数 DDR 系统的收益和实现形态不一定相同，见 Page 1-2。 | Limitations / Discussion / Future Work | NoM 主要针对 highly-banked 3D-stacked memory；传统低 bank 数 DDR 系统的收益和实现形态不一定相同，见 Page 1-2。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | NoM 在真实 HBM3/HBM4 的 bank group、pseudo-channel 和 TSV 组织上如何映射？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
