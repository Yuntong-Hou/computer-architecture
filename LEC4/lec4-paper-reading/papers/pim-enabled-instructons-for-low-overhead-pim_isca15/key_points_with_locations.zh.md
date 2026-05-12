# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何让 PIM operation 像普通 host instruction 一样使用，而不是引入全新的 PIM 编程模型。 | Page 1-2 / Introduction | 作者指出早期和现代 PIM 往往需要新的编程模型、非 cacheable memory region 或显式 cache flush，难以无缝接入现有系统，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 3D-stacked DRAM/HMC 提供 logic die、TSV 内部高带宽和低能耗传输，但如果所有操作都强制在 memory side 执行，高局部性数据反而会失去 on-chip cache 优势，见 Page 2-3, Sections 2.1-2.2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。 | 方法章节 / Page 2 及后续对应 section | PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | Locality-Aware policy 根据目标数据是否可能在 cache 中受益，选择 host-side 或 memory-side PCU；balanced dispatch 进一步根据 request/response bandwidth 平衡执行位置，见 Page 9-11。 | 方法章节后半部分 | Locality-Aware policy 根据目标数据是否可能在 cache 中受益，选择 host-side 或 memory-side PCU；balanced dispatch 进一步根据 request/response bandwidth 平衡执行位置，见 Page 9-11。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。 | Evaluation / Results | PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | large inputs 中 PIM-Only 相比 Ideal-Host 平均快 44%；small inputs 中 PIM-Only 平均慢 20%，因为即使数据适合 cache 也访问 DRAM，见 Page 9, Figure 6。 | Evaluation / Results | large inputs 中 PIM-Only 相比 Ideal-Host 平均快 44%；small inputs 中 PIM-Only 平均慢 20%，因为即使数据适合 cache 也访问 DRAM，见 Page 9, Figure 6。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。 | Introduction / Contributions | 提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。 | Limitations / Discussion / Future Work | 单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | single-cache-block restriction 是否会限制现代图分析/数据库中更复杂的 PIM primitives？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
