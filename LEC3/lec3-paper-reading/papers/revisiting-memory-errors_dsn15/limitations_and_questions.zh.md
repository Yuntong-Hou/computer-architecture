# Limitations and Questions

## 1. 作者明确承认的局限
- page offlining 会降低可用物理内存，需要达到阈值后维修机器。（Page 11, Section VI-C）
- page offlining 并不总能立即成功；Linux kernel 中约 6% 初始 attempts 失败。（Page 11, Section VI-C）

## 2. 论文中隐含的局限
- 数据来自 Facebook 特定时期、DDR3 设备和生产 workload，不能直接外推到 DDR5/HBM 或其他数据中心。（推断，基于 Methodology）
- UCE 缺少 CE 那样细粒度信息，因此 UCE 源因分析能力有限。（推断，基于 Page 3 methodology）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 内存错误在服务器之间如何分布，平均值是否有代表性？
- 错误来源是否主要是 DRAM chip，还是 memory controller/channel/socket？
- 更高 chip density、DIMM 架构、工作负载、年龄和利用率如何影响 failure rate？
- 能否建立用于系统设计的 failure model？
- page offlining 在真实数据中心部署时实际效果如何？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
