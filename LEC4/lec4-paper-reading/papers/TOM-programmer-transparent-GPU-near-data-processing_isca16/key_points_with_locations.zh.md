# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何不让程序员手动标注 offloading code。 | Page 1-2 / Introduction | GPU 应用常受 off-chip memory bandwidth 限制；3D-stacked memory 的 logic layer 可以放置 SMs 并靠 TSV 获得高内部带宽，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | NDP 系统面临两个核心问题：哪些代码应在 main GPU 还是 memory stack SMs 执行，以及数据如何映射到多个 memory stacks，见 Page 1。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。 | 方法章节 / Page 2 及后续对应 section | 编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 实现上增加 offloading metadata table、memory allocation table 和 memory map analyzer 等结构，见 Page 6-7。 | 方法章节后半部分 | 实现上增加 offloading metadata table、memory allocation table 和 memory map analyzer 等结构，见 Page 6-7。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。 | Evaluation / Results | TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | programmer-transparent data mapping 相比 baseline memory mapping 平均额外提升 10%；例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，见 Page 9。 | Evaluation / Results | programmer-transparent data mapping 相比 baseline memory mapping 平均额外提升 10%；例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，见 Page 9。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。 | Introduction / Contributions | 提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。 | Limitations / Discussion / Future Work | TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | TOM 的 mapping predictor 如何适应 phase behavior 更剧烈的现代 GPU workloads？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
