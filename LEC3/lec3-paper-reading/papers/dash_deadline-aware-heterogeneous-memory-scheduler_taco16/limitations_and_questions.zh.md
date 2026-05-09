# Limitations and Questions

## 1. 作者明确承认的局限
- DASH 假设 HWA 的 deadline、period 和 memory request demand 可由系统获知或估计。（Page 6-9, design）
- 研究重点是 soft real-time frame deadlines；hard real-time worst-case guarantee 不是本文目标。（Page 4 and Page 8-10）

## 2. 论文中隐含的局限
- 真实 SoC 中不同 HWA 的 burstiness、QoS contract 和 memory controller 实现会影响策略迁移。（推断，基于 simulator evaluation）
- DASH 需要额外硬件监控和 scheduler 逻辑，复杂度高于 FRFCFS。（推断，基于 scheduler design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- memory scheduler 如何判断 HWA 是否 on track 满足 deadline？
- 为什么应优先打断 memory-intensive CPU 而保护 memory-nonintensive CPU？
- 短 deadline HWA 是否需要与长 deadline HWA 不同的调度？
- DASH 相比 FRFCFS 和 dynamic threshold scheduler 性能/deadline tradeoff 如何？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
