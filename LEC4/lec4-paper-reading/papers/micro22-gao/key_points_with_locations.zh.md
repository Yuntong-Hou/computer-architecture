# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 是否能在 off-the-shelf DRAM cell 中稳定写入并验证 fractional value。 | Page 1-2 / Introduction | DRAM cell 本质是 capacitor，电压可处于 0 到 Vdd 之间；传统接口只把它抽象成 0/1，见 Page 1, Introduction。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | ComputeDRAM 已显示 out-of-spec command timing 能在商用 DRAM 中产生新行为；FracDRAM 进一步利用 PRECHARGE 的 Vdd/2 电路，把中间电压作为可用状态，见 Page 1-3。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | Frac operation 先 PRECHARGE bitline 到 Vdd/2，再 ACTIVATE target row，并在 sense amplifier 完全放大前立刻 PRECHARGE 中断，使 cell 保留介于 Vdd/2 与初始值之间的电压，见 Page 3, Figure 3。 | 方法章节 / Page 2 及后续对应 section | Frac operation 先 PRECHARGE bitline 到 Vdd/2，再 ACTIVATE target row，并在 sense amplifier 完全放大前立刻 PRECHARGE 中断，使 cell 保留介于 Vdd/2 与初始值之间的电压，见 Page 3, Figure 3。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | F-MAJ 在四行激活中让一行存 fractional value，使其等效调节 charge sharing 的偏置；PUF 则用 10 次 Frac 把 row 拉近 Vdd/2，再读取 sense amplifier variation 形成 response，见 Page 8-12。 | 方法章节后半部分 | F-MAJ 在四行激活中让一行存 fractional value，使其等效调节 charge sharing 的偏置；PUF 则用 10 次 Frac 把 row 拉近 Vdd/2，再读取 sense amplifier variation 形成 response，见 Page 8-12。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Frac 使平均约 55% cells 的 retention time 随 Frac 次数单调下降，支持其电压被逐步拉向 Vdd/2 的解释，见 Page 6, Figure 6。 | Evaluation / Results | Frac 使平均约 55% cells 的 retention time 随 Frac 次数单调下降，支持其电压被逐步拉向 Vdd/2 的解释，见 Page 6, Figure 6。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | F-MAJ 可在所有能打开四行的 DRAM chips 上执行；group B 最佳配置达到 99.8% coverage，而原始 MAJ3 coverage 为 98.0%，见 Page 9, Figure 9。 | Evaluation / Results | F-MAJ 可在所有能打开四行的 DRAM chips 上执行；group B 最佳配置达到 99.8% coverage，而原始 MAJ3 coverage 为 98.0%，见 Page 9, Figure 9。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 首次展示在未修改商用 DRAM 中存储 fractional values，见 Page 1-2, Introduction。 | Introduction / Contributions | 首次展示在未修改商用 DRAM 中存储 fractional values，见 Page 1-2, Introduction。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。 | Limitations / Discussion / Future Work | retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | fractional value 如果需要长期保存或可恢复读取，需要怎样的 sense amplifier 或 refresh 支持？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
