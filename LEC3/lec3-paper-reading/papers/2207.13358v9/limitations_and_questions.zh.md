# Limitations and Questions

## 1. 作者明确承认的局限

- ACT_NACK divergence across chips 可能造成 partial row activation 和额外开销。原文位置：Page 18, Section 9.9。
- SMD-FR 在 worst-case divergence 下可能平均慢 2.6%，个别 workload slowdown 可到 12.8%。原文位置：Page 18。
- SMD-PMP 等 prioritization 机制需要进一步设计，论文主要估算其性能影响。原文位置：Page 15, Section 9.1。

## 2. 论文中隐含的局限

- 需要 DRAM chip 和 memory controller 都支持新接口，不适合直接部署在现有 commodity DRAM。
- 评估基于 Ramulator simulation，尚未有真实 SMD 芯片。
- RowHammer protection 的安全性仍取决于具体检测/刷新机制和未来 RowHammer threshold。
- DRAM vendor 内部策略不可见可能有利于 IP 保护，但也可能降低外部验证透明度。

## 3. 实验设计可能存在的问题

- 工作负载选择和 memory intensity 分类影响结果，非 memory-intensive workloads 收益较小。
- 能耗使用 DRAMPower 建模，和真实芯片在不同温度、电压、工艺下可能有差异。
- 对 DDR5、HBM 或 CXL-attached memory 的直接外推需要更多实验。

## 4. 方法可能不适用的场景

- 系统无法修改 DRAM interface 或 MC retry logic。
- workload 访问集中于正在维护的 hot region，ACT_NACK 频繁导致重试开销。
- rank 内多个 chips 的维护行为高度不同步，造成 divergence。

## 5. 我阅读时应该追问的问题

- SMD 的 ACT_NACK 是否会打破现有实时性或 QoS 假设？
- DRAM vendor 自主维护是否会降低系统软件可观测性？
- SMD 与 DDR5 RFM、PRAC 的关系是替代、补充还是更通用抽象？
- SMD 是否能成为 CXL memory devices 的内部维护接口？

## 6. 后续可以继续阅读的方向

- `raidr-dram-refresh_isca12`：retention-aware refresh。
- `RowPress_isca23`、`RowHammer-Retrospective`：读干扰问题背景。
- `DSAC`：具体 in-DRAM stochastic counting RowHammer mitigation。
