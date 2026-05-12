# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 是否可以在 off-the-shelf, unmodified, commercial DRAM 中实现 in-memory row copy 与逻辑 AND/OR。 | Page 1-2 / Introduction | 传统 in-memory compute 往往要求修改 DRAM array 或加入额外电路，而 DRAM 行业成本敏感、利润率低，导致这类设计难以商业落地，见 Page 1, Abstract/Introduction。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 作者重新审视 memory controller 对 DRAM commands/timing 的控制，发现快速连续 ACTIVATE/PRECHARGE/ACTIVATE 可让多个 rows 在未改动芯片中同时打开并发生 charge sharing，见 Page 3, Section 3。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | ComputeDRAM 用 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 等 timing-violating command sequence 让多行在同一 subarray 中同时影响 bitline，从而实现 row copy 或 AND/OR，见 Page 3-5, Figures 3-6。 | 方法章节 / Page 2 及后续对应 section | ComputeDRAM 用 ACTIVATE(R1)-PRECHARGE-ACTIVATE(R2) 等 timing-violating command sequence 让多行在同一 subarray 中同时影响 bitline，从而实现 row copy 或 AND/OR，见 Page 3-5, Figures 3-6。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | 系统通过 SoftMC/FPGA 自定义 memory controller 发出精确命令序列，并用 error table 避免坏 columns/rows，见 Page 7-8, Figure 9。 | 方法章节后半部分 | 系统通过 SoftMC/FPGA 自定义 memory controller 发出精确命令序列，并用 error table 避免坏 columns/rows，见 Page 7-8, Figure 9。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Figure 10 显示至少存在 off-the-shelf unmodified commercial DRAM modules 可同时执行 row copy 与 logical AND/OR；几乎所有 configuration groups 至少有部分 columns 能执行 row copy，见 Page 9。 | Evaluation / Results | Figure 10 显示至少存在 off-the-shelf unmodified commercial DRAM modules 可同时执行 row copy 与 logical AND/OR；几乎所有 configuration groups 至少有部分 columns 能执行 row copy，见 Page 9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 逻辑 AND/OR 主要在 SKhynix_2G_1333 与 SKhynix_4G_1333B groups 中可跨 subarray 全列执行；SKhynix_4G_1600 也能执行但不是所有 columns，见 Page 9。 | Evaluation / Results | 逻辑 AND/OR 主要在 SKhynix_2G_1333 与 SKhynix_4G_1333B groups 中可跨 subarray 全列执行；SKhynix_4G_1600 也能执行但不是所有 columns，见 Page 9。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 首次展示在未修改商用 DRAM 中实现 row copy，见 Page 1-2 与 Page 3-4。 | Introduction / Contributions | 首次展示在未修改商用 DRAM 中实现 row copy，见 Page 1-2 与 Page 3-4。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。 | Limitations / Discussion / Future Work | 不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | DDR4/DDR5 是否仍保留类似可利用的 timing-violation 行为，还是控制逻辑会过滤这些命令？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
