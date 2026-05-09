# Limitations and Questions

## 1. 作者明确承认的局限
- 使用 less reliable/no-ECC memory 的前提是数据多为 read-only/transient，且错误不会长期传播到 persistent storage。（Page 11, Section VI-C）
- 本文没有完整建模 hard error 出现过程，只分析其 ongoing effects。（Page 10, Table 6 assumptions）

## 2. 论文中隐含的局限
- 业务可接受的 incorrect results per million queries 取决于应用和 SLA，不能直接推广到所有服务。（推断，基于 WebSearch case study）
- 需要 OS/runtime 支持 memory region classification、recovery 和 heterogeneous memory provisioning。（推断，基于 Figure 7/9 design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何量化应用对 memory errors 的 tolerance/vulnerability？
- WebSearch、Memcached、GraphLab 在 crash 和 incorrect results 上差异多大？
- 应用内部 heap/stack/private memory 是否需要同等保护？
- heterogeneous-reliability mapping 能降低多少 server hardware cost？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。
