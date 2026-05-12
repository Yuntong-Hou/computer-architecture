# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。 | Page 1-2 / Introduction | 现有 PUD 多采用 bulk bit-serial execution model，用固定 two's complement 和固定 bit-precision 处理整行数据，导致大量 inconsequential bits 被无谓计算，见 Page 1-2。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | PUD 还面临 throughput-oriented execution 难隐藏低并行场景下的单操作延迟，以及高精度操作延迟随 bit-width 线性或二次增长的问题，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。 | 方法章节 / Page 2 及后续对应 section | Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。 | 方法章节后半部分 | Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。 | Evaluation / Results | Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。 | Evaluation / Results | SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。 | Introduction / Contributions | 提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。 | Limitations / Discussion / Future Work | 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | Proteus 与 MIMDRAM 是否可以结合，同时解决位精度和资源粒度问题？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
