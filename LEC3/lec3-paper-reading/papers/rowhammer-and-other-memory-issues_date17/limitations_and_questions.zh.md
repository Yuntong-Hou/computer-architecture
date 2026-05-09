# Limitations and Questions

## 1. 作者明确承认的局限
- PARA 不能立即部署，因为需要 memory controller 或 DRAM chip 修改，并需要知道物理相邻 rows。（Page 3, Section II-C）
- 提高 refresh rate 是现实 immediate solution，但会增加能耗、降低性能和 QoS。（Page 2, Section II-C）

## 2. 论文中隐含的局限
- 本文是 invited/survey-style 论文，很多结论依赖引用的先前实验和攻击论文，而非新实验。（推断，基于全文结构）
- 对 NAND/PCM 等潜在漏洞的讨论属于研究方向判断，不能视作已实证的完整攻击链。（推断，基于 Section III）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 为什么 RowHammer 是电路级 failure 变成系统级安全漏洞的典型例子？
- 用户态程序如何通过 repeated activation 破坏相邻 rows？
- 已有 immediate/long-term solutions 各有什么缺点？
- PARA 为什么被认为是低成本长期方案？
- 除了 RowHammer，retention 和 NAND flash disturb 还可能带来哪些安全风险？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
