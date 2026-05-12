# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何把 PUD 操作粒度从完整 DRAM row 缩小到 mat/segment，以匹配应用实际 SIMD parallelism。 | Page 1-2 / Introduction | PUD 可利用 DRAM 阵列内部并行性执行 16K 到 262K-bit-wide 的 SIMD 操作，但 DRAM row 粒度过大且固定，导致 SIMD 利用率低、难支持 reduction、编程困难，见 Page 1-2。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 传统 PUD 往往要求程序员手工提取极宽数据并行性并映射到 DRAM row，缺少编译器支持，见 Page 2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | MIMDRAM 在硬件上增加 latches、isolation transistors 和 selection logic，使单个 DRAM mat 可被独立寻址并执行 PUD operation，见 Page 4-6, Section 4.1。 | 方法章节 / Page 2 及后续对应 section | MIMDRAM 在硬件上增加 latches、isolation transistors 和 selection logic，使单个 DRAM mat 可被独立寻址并执行 PUD operation，见 Page 4-6, Section 4.1。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 软件侧通过 compiler passes 自动 vectorize PUD-friendly regions、选择 SIMD granularity，并调度独立 PUD operations，见 Page 8-11。 | 方法章节后半部分 | 软件侧通过 compiler passes 自动 vectorize PUD-friendly regions、选择 SIMD granularity，并调度独立 PUD operations，见 Page 8-11。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | MIMDRAM 平均提供 SIMDRAM 的 15.6x SIMD utilization、14.3x energy efficiency 和 34x performance，见 Page 12, Figure 9。 | Evaluation / Results | MIMDRAM 平均提供 SIMDRAM 的 15.6x SIMD utilization、14.3x energy efficiency 和 34x performance，见 Page 12, Figure 9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 相对 CPU/GPU，MIMDRAM 平均提供 30.6x/6.8x energy efficiency，但在只用单 subarray/bank 时平均性能仍可能低于 CPU/GPU，见 Page 12。 | Evaluation / Results | 相对 CPU/GPU，MIMDRAM 平均提供 30.6x/6.8x energy efficiency，但在只用单 subarray/bank 时平均性能仍可能低于 CPU/GPU，见 Page 12。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出首个面向 general-purpose applications 的端到端 MIMD PUD 系统，见 Page 3。 | Introduction / Contributions | 提出首个面向 general-purpose applications 的端到端 MIMD PUD 系统，见 Page 3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。 | Limitations / Discussion / Future Work | 若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | MIMDRAM 的 compiler passes 在更复杂控制流或 pointer-heavy 应用上效果如何？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
