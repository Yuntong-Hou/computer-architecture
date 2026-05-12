# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何在 DRAM 内部完成 bulk bitwise AND/OR，而不是经由 CPU 和外部内存通道搬运大量数据。 | Page 1-2 / Introduction | 作者指出 bitwise AND/OR 广泛用于 masking、initialization 和 bitmap indices；传统系统必须把源数据从 DRAM 读到处理器再写回，带来高 latency、bandwidth 和 energy，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 论文建立在 DRAM cell、bitline、sense amplifier 与 RowClone 的背景上：如果能在 subarray 内快速复制临时行，就能把三行激活组织成完整的 AND/OR 操作，见 Page 1-2, Sections 2-3。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 核心 primitive 是 triple-row activation：同时激活三行后，bitline 偏移由三颗 cell 的多数值决定；令控制行 R=0 得到 A AND B，R=1 得到 A OR B，见 Page 2, Section 3 与 Figure 4。 | 方法章节 / Page 2 及后续对应 section | 核心 primitive 是 triple-row activation：同时激活三行后，bitline 偏移由三颗 cell 的多数值决定；令控制行 R=0 得到 A AND B，R=1 得到 A OR B，见 Page 2, Section 3 与 Figure 4。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 软件侧需要暴露新的 bulk bitwise instructions 或库接口；作者建议可先在 FastBit 等共享库中利用硬件加速，见 Page 3, Section 3.3。 | 方法章节后半部分 | 软件侧需要暴露新的 bulk bitwise instructions 或库接口；作者建议可先在 FastBit 等共享库中利用硬件加速，见 Page 3, Section 3.3。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | 当 working set 不适合任何 on-chip cache 时，baseline AVX throughput 下降到 3.9 GB/s；conservative 机制达到 22.4 GB/s，aggressive 机制达到 38.2 GB/s，见 Page 3, Section 4 与 Figure 5。 | Evaluation / Results | 当 working set 不适合任何 on-chip cache 时，baseline AVX throughput 下降到 3.9 GB/s；conservative 机制达到 22.4 GB/s，aggressive 机制达到 38.2 GB/s，见 Page 3, Section 4 与 Figure 5。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 论文摘要报告该方法可使 bulk bitwise AND/OR throughput 提升 9.7x、energy 降低 50.5x，见 Page 1, Abstract。 | Evaluation / Results | 论文摘要报告该方法可使 bulk bitwise AND/OR throughput 提升 9.7x、energy 降低 50.5x，见 Page 1, Abstract。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出三行同时连接到 bitline 的机制，使 sense amplifier 输出三者多数值；第三行为 0 时得到 AND，为 1 时得到 OR，见 Page 2, Section 3。 | Introduction / Contributions | 提出三行同时连接到 bitline 的机制，使 sense amplifier 输出三者多数值；第三行为 0 时得到 AND，为 1 时得到 OR，见 Page 2, Section 3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 最佳情形依赖 A/B/C 与临时行位于同一 subarray；跨 subarray/bank copy 需要 RowClone-PSM 或更慢路径，见 Page 2, Section 3。 | Limitations / Discussion / Future Work | 最佳情形依赖 A/B/C 与临时行位于同一 subarray；跨 subarray/bank copy 需要 RowClone-PSM 或更慢路径，见 Page 2, Section 3。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 真实芯片中 triple-row activation 在 process/temperature/voltage variation 下错误率是多少？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
