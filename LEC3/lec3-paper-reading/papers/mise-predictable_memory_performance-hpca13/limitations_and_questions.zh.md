# Limitations and Questions

## 1. 作者明确承认的局限
- MISE 主要估计 main memory interference，其他共享资源 slowdown 留作未来工作。（Page 12, Conclusion）
- MISE 不显式建模 bank-level parallelism 或 row-buffer interference，但作者观察其对准确性影响有限。（Page 4, Section 4.3）

## 2. 论文中隐含的局限
- highest-priority sampling 会改变短期调度行为，在实时或极短 phase workload 中需重新评估。（推断，基于 epoch/interval design）
- MISE 只在仿真 SPEC workloads 上系统评估，现代 server workloads/NUMA/HBM 需要新验证。（推断，基于 methodology）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何在线估计应用独占运行时的 request-service-rate？
- request-service-rate 为什么能作为 memory-bound 应用性能代理？
- 非 memory-bound 应用如何加入 compute phase/stall fraction 修正？
- MISE-QoS/MISE-Fair 相对 STFM/ATLAS/TCM 效果如何？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。
