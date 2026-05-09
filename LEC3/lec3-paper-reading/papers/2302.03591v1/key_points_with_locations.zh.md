# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | RowHammer threshold 随 DRAM scaling 降低 | Page 1, Abstract/Introduction | scaling decreases Rowhammer threshold | 高 | 背景动机 |
| 2 | MC-based TRR 有信息不足和性能开销 | Page 1, Introduction; Page 3-4 | MC 缺少 RHTH/内部物理信息，可能 TRR 不足或过多 | 高 | 说明为何要 in-DRAM TRR |
| 3 | 两类 activation-induced bit-flips | Page 2-3, Section III | Passing Gate Effect 关注 long activation time；RowHammer 关注 frequent activation | 高 | DSAC 同时提出 Time-Weighted Counting 和 TRR algorithm 的原因 |
| 4 | MR4 增大 refresh interval 不利于 RowHammer mitigation | Page 3-4, Section IV.C | MR4 可把 tREFI/tREFW 放大到 4x，降低普通 refresh 缓解机会 | 中 | 标准低功耗特性会增加防护难度 |
| 5 | decoy-rows 是 counter-based algorithms 的关键问题 | Page 5, Figure 10 | decoy-rows 替换 count table 中的 RowHammer rows，夺走 TRR 机会 | 高 | 本文最重要的问题定义 |
| 6 | Time-Weighted Counting 缓解 Passing Gate Effect | Page 5-6, Figure 8 | activation time 越长，row count 权重越高 | 中 | 与 RowHammer frequency-based counting 互补 |
| 7 | DSAC 使用 Stochastic Replacement | Page 6, Figure 11; Algorithm 1 | 新 row 替换 min-count row 的概率与 min count 相关 | 高 | 核心算法设计 |
| 8 | Approximate Counting 降低面积 | Page 6-7, Figures 12-14 | 保留 replaced row 的 count 信息并减少 counter 成本 | 中 | 使 in-DRAM 实现可行 |
| 9 | Maximum Disturbance 是评估指标 | Page 10, Section VII | 统计 observation period 内最大累积 activation | 高 | 比单纯 detection rate 更贴近安全风险 |
| 10 | DSAC 在 20 counters 下 disturbance 低 | Page 10-11, Table V | DSAC average disturbance 2196/2211，低于 Graphene 19450/10822 | 高 | 主要实验结果 |
| 11 | DSAC 缩放 counters 时仍优 | Page 11, Figure 19/Table VI | DSAC 比 Graphene 低 133x average disturbance | 高 | 支撑 area-limited 场景 |
| 12 | DSAC area/energy 较低 | Page 11, Table VII | per-rank area 0.01 mm2，static power 0.71 mW | 中 | 实现可行性证据 |
