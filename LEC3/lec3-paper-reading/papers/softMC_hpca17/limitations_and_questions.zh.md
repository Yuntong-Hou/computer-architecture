# Limitations and Questions

## 1. 作者明确承认的局限
- SoftMC 不能直接作为主存控制器评估系统性能，因为 PCIe latency 约 1us，而 DRAM access latency 约 15-80ns。（Page 10, Section 7）
- 当前 prototype 的 instruction queue 大小限制一次原子执行序列长度，循环控制流仍是未来改进方向。（Page 10, Section 7）

## 2. 论文中隐含的局限
- 原型基于 ML605/DDR-era 平台，迁移到 DDR5/HBM/CXL 或 vendor-specific features 需要新 PHY/板卡支持。（推断，基于 Section 5.5）
- SoftMC 暴露的是 DDR command-level 控制，无法访问芯片内部不可暴露的 sense amplifier timing 或厂商 remapping 细节。（推断，基于 Section 6.2 discussion）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、芯片样本、工艺节点、workload、模拟器或 field environment；迁移到新硬件/新数据中心时需复核。（推断）

## 4. 方法可能不适用的场景
- 当 DRAM generation、控制器接口、温度/工作负载、错误模型或系统软件机制与论文假设明显不同，方法收益或风险可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 一个实用 DRAM testing infrastructure 为什么必须同时具备 flexibility 和 ease of use？
- SoftMC 如何把 DDR commands 和 timing 控制暴露给用户？
- 高层 API 如何映射到 FPGA 中的 programmable memory controller？
- SoftMC 能否复现 retention time 既有结果？
- SoftMC 如何验证或反驳 ChargeCache/NUAT 等 latency reduction 假设？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：retention-aware profiling、field reliability modeling、adaptive memory scheduling、RowHammer security、open-source DRAM testing infrastructure。
