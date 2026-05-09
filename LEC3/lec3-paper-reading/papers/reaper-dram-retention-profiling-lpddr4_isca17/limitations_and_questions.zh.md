# Limitations and Questions

## 1. 作者明确承认的局限
- 结果依赖具体假设：45C、reach profiling 2.5x speedup、32 chips/module、100% coverage 假设和 20 个 workload mixes。（Page 13, Section 7.3.2 caveat）
- 真正可靠 relaxed-refresh operation 需要实际芯片的 characterization data；DRAM vendors 当前通常不提供。（Page 9, Section 6.3）

## 2. 论文中隐含的局限
- profiling 本身仍依赖 retention failure mitigation，如 ECC、bit repair 或 remapping；单独 REAPER 不等于完整可靠性方案。（推断，基于 Sections 6-7）
- DPD/VRT 导致 profile 会过期，不同工艺或工作温度下需要重新调参。（推断，基于 Sections 5-6）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何定义 retention profiling 的 coverage、false positive rate 和 runtime？
- 为什么在更长 refresh interval 或更高温下 profiling 能发现目标条件下的失败 cells？
- 在线 profiling 需要多频繁运行才可维持可靠性？
- ECC 的 UBER/RBER 约束如何转化为 profile longevity？
- REAPER 相比 brute-force profiling 对系统性能和 DRAM power 有多少改善？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
