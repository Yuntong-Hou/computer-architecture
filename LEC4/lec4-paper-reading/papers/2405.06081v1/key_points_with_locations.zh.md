# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | COTS DRAM 是否能稳健地同时激活超过四行，甚至 32 行。 | Page 1-2 / Introduction | PUD 操作常依赖 multiple-row activation；此前真实芯片工作主要研究两行、三行或四行激活，尚不清楚更多行是否能被稳健地同时激活，见 Page 1-2。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 作者提出 Q1-Q5，系统询问 many-row activation 的可行性、可实现操作、鲁棒性、改善方式以及 data pattern/temperature/voltage/timing 的影响，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 作者用 DRAM Bender 精细调度 ACT/PRE 等命令，违反标准 timing parameters，以触发 simultaneous many-row activation，见 Page 3-5。 | 方法章节 / Page 2 及后续对应 section | 作者用 DRAM Bender 精细调度 ACT/PRE 等命令，违反标准 timing parameters，以触发 simultaneous many-row activation，见 Page 3-5。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | success rate、温度、电压、data pattern 和 row decoder 假设共同用于解释真实芯片行为，见 Page 4-10。 | 方法章节后半部分 | success rate、温度、电压、data pattern 和 row decoder 假设共同用于解释真实芯片行为，见 Page 4-10。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | COTS DRAM 可同时激活最多 32 行；MAJ3/MAJ5/MAJ7/MAJ9 平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%，见 Page 2。 | Evaluation / Results | COTS DRAM 可同时激活最多 32 行；MAJ3/MAJ5/MAJ7/MAJ9 平均 success rate 分别为 99.00%、79.64%、33.87%、5.91%，见 Page 2。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 将一行复制到 1/3/7/15/31 个目标行的平均 success rate 分别为 99.996%、99.989%、99.998%、99.999%、99.982%，见 Page 2。 | Evaluation / Results | 将一行复制到 1/3/7/15/31 个目标行的平均 success rate 分别为 99.996%、99.989%、99.998%、99.999%、99.982%，见 Page 2。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 在 120 个 COTS DDR4 chips 上展示可同时激活 2/4/8/16/32 行，见 Page 2 与 Section 4。 | Introduction / Contributions | 在 120 个 COTS DDR4 chips 上展示可同时激活 2/4/8/16/32 行，见 Page 2 与 Section 4。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。 | Limitations / Discussion / Future Work | 部分 Samsung 芯片未观察到同一 subarray 中多于一行的同时激活，因此不支持测试的 PUD operations，见 Page 12, Section 9。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 能否设计标准化 DRAM 接口，让行数和 row group 更可控地执行 SiMRA？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
