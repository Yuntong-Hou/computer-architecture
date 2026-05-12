# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何减少传输未使用 cache-block word 的能耗。 | Page 1-2 / Introduction | 现代 DRAM 以 cache block 粒度传输、以整行/大范围 cell 激活；但很多 workload 的 spatial locality 较差，cache block 中大量 word 在驻留期间未被使用，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 已有 fine-grained DRAM 方案往往吞吐低、面积开销高或没有完整支持细粒度传输和激活，见 Page 1-2, Section 1。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | VBL 复用 DRAM I/O 中每个 burst cycle 选择一个 word 的既有机制，让一次 cache block transfer 可以只包含所需 word，见 Page 2, Page 6。 | 方法章节 / Page 2 及后续对应 section | VBL 复用 DRAM I/O 中每个 burst cycle 选择一个 word 的既有机制，让一次 cache block transfer 可以只包含所需 word，见 Page 2, Page 6。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | LSQ Lookahead 从 younger load/store 指令中收集同一 cache block 的未来 word 需求；Sector Predictor 基于过去访问模式预测会被使用的 sector，见 Page 2 与 Page 7。 | 方法章节后半部分 | LSQ Lookahead 从 younger load/store 指令中收集同一 cache block 的未来 word 需求；Sector Predictor 基于过去访问模式预测会被使用的 sector，见 Page 2 与 Page 7。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | 读/写一个 sector 相比读/写全部 sector，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%，见 Page 10, Figure 7。 | Evaluation / Results | 读/写一个 sector 相比读/写全部 sector，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%，见 Page 10, Figure 7。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 只激活一个 sector 可使 DRAM array activation power 降低 66.5%，但整体 ACT power 只降低 12.7%；SA 额外 activation power 开销仅 0.26%，见 Page 10, Section 7.1。 | Evaluation / Results | 只激活一个 sector 可使 DRAM array activation power 降低 66.5%，但整体 ACT power 只降低 12.7%；SA 额外 activation power 开销仅 0.26%，见 Page 10, Section 7.1。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 Variable Burst Length (VBL)，按请求 sector 数动态调整 burst cycle 数，见 Page 2 与 Page 6, Section 4.2。 | Introduction / Contributions | 提出 Variable Burst Length (VBL)，按请求 sector 数动态调整 burst cycle 数，见 Page 2 与 Page 6, Section 4.2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。 | Limitations / Discussion / Future Work | stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 更强 predictor 是否能显著降低 sector miss，又不会引入过高面积和能耗？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
