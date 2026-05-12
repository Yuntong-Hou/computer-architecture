# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何避免 in-DRAM cache 以整行粒度搬移大量不会被访问的数据。 | Page 1-2 / Introduction | DRAM 容量提升远快于访问延迟改善；in-DRAM cache 用小而快的 DRAM 区域缓存慢区域数据，但现有方案以整行 8KB 粒度迁移，浪费空间且迁移延迟受物理距离影响，见 Page 1-2。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 现代 DRAM bank 中所有 subarrays 共享 global row buffer，作者发现它可作为跨 subarray 细粒度 relocation 的通道，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | FIGARO 允许两个 local row buffers 通过 global row buffer 进行 unaligned data transfer，使源列可写入目标不同列，不经过 off-chip memory channel，见 Page 2 与 Section 4。 | 方法章节 / Page 2 及后续对应 section | FIGARO 允许两个 local row buffers 通过 global row buffer 进行 unaligned data transfer，使源列可写入目标不同列，不经过 off-chip memory channel，见 Page 2 与 Section 4。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | FIGCache-Fast 使用少量 fast subarrays；FIGCache-Slow 只保留 slow subarray 中少量 rows 作为 cache，见 Page 8-9。 | 方法章节后半部分 | FIGCache-Fast 使用少量 fast subarrays；FIGCache-Slow 只保留 slow subarray 中少量 rows 作为 cache，见 Page 8-9。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | FIGCache-Fast 在 20 个 eight-core workloads 上平均提升 16.3% performance；100% memory-intensive workloads 平均提升 27.1%，见 Page 9, Figure 8。 | Evaluation / Results | FIGCache-Fast 在 20 个 eight-core workloads 上平均提升 16.3% performance；100% memory-intensive workloads 平均提升 27.1%，见 Page 9, Figure 8。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | FIGCache-Slow 即使没有 fast subarrays，也在 multiprogrammed workloads 上平均提升 12.4% performance，见 Page 9。 | Evaluation / Results | FIGCache-Slow 即使没有 fast subarrays，也在 multiprogrammed workloads 上平均提升 12.4% performance，见 Page 9。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 FIGARO substrate，支持 bank 内 subarrays 之间 column/cache-block granularity data relocation，且 latency distance-independent，见 Page 2-6。 | Introduction / Contributions | 提出 FIGARO substrate，支持 bank 内 subarrays 之间 column/cache-block granularity data relocation，且 latency distance-independent，见 Page 2-6。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。 | Limitations / Discussion / Future Work | 需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | FIGARO 的 RELOC 操作在真实 DDR4/DDR5 芯片上能否以论文时序安全实现？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
