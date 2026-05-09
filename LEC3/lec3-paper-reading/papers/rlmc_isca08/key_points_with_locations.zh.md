# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：CMP 核数增长快于 off-chip bandwidth 增长，传统 memory controllers 采用固定、人工设计的 scheduling policy，缺少长期规划和对 workload phase changes 的自适应能力。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：RL-based scheduler 每个 DRAM cycle 观察 transaction queue、request type、row hit、criticality 等 state attributes，从合法 precharge/activate/read/write actions 中选择 Q-value 最高动作；执行后根据 data bus utilization reward 更新 state-action Q-values，持续适应 workload 行为。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：4-core single-channel 下，RL 平均性能比 FR-FCFS 提升 19%，最高 33%。 | Page 1-2 Abstract/Introduction; Page 8-9, Figure 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：RL 将 DRAM data bus utilization 从 46% 提升到 56%，平均提升 22%。 | Page 1 and Page 9, Figure 8 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：RL 将 average L2 load miss penalty 从 FR-FCFS 的 824 cycles 降到 562 cycles。 | Page 9, Figure 9 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：仅把额外 state information 加到 FR-FCFS derivatives 平均只提升 5%，online RL 达到 19%。 | Page 9, Figure 10 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：offline RL 平均仅提升 8%，显著弱于 online adaptive RL。 | Page 10, Figure 11 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：8-core/16-core 多控制器下 RL 仍平均提升 15%/14%，不需要显式 controller coordination。 | Page 10, Figure 14 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：QoS guarantees/multiprogrammed fairness 不是本文目标，留给 future work。 | Page 11, Section 5.4 | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：评估基于 2008-era DDR2、4-16 core 模拟环境，现代 DDR5/HBM/CXL 系统需重新验证。 | 推断，基于 Section 4 setup | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
