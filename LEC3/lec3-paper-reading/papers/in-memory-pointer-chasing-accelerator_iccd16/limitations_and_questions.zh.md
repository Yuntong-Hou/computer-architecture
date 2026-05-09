# Limitations and Questions

## 1. 作者明确承认的局限
- IMPICA 要求可加速数据结构放入连续 virtual regions，并使用专门的 region-based translation。（Page 2 and Page 4, Section 4.2）
- 获取整个 node 可能带来部分无用字段访问，B-tree 等结构会受到影响。（Page 6-7, evaluation discussion）

## 2. 论文中隐含的局限
- 需要编程接口/offload support，且适合 pointer chasing 占比较高、数据结构相对明确的应用。（推断，基于 API/design）
- 真实 HMC/HBM 系统中 coherence、OS integration 和 multi-tenant isolation 需要额外工程。（推断，基于 PIM accelerator）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 为什么 pointer chasing 适合在 memory side 加速？
- 串行 pointer traversal 如何在简单 accelerator 中获得并行性？
- PIM accelerator 如何低成本完成 virtual-to-physical translation？
- IMPICA 对 linked list/hash table/B-tree/DBx1000 的性能和能耗收益如何？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。
