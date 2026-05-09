# Limitations and Questions

## 1. 作者明确承认的局限
- QoS guarantees/multiprogrammed fairness 不是本文目标，留给 future work。（Page 11, Section 5.4）
- RL 的 reward 主要优化 data bus utilization，不能直接覆盖所有公平性或服务质量目标。（Page 3-4, reward definition; Page 11）

## 2. 论文中隐含的局限
- 评估基于 2008-era DDR2、4-16 core 模拟环境，现代 DDR5/HBM/CXL 系统需重新验证。（推断，基于 Section 4 setup）
- 硬件学习参数、feature selection 和 convergence 在极端 workload phase changes 下仍需工程验证。（推断，基于 Sections 3 and 5.1.4）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何把 DRAM scheduling 表述为 Markov Decision Process？
- memory controller 的 state、action 和 reward 应该如何定义？
- 在线 RL 是否能在硬件可实现的结构中收敛并提升性能？
- 提升来自额外状态信息还是来自 RL 的表达能力与在线学习？
- 多 memory controllers 情况下是否需要显式协调？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
