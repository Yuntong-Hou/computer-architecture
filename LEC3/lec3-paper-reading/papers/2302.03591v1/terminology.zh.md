# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| DSAC | DRAM 内随机与近似计数算法 | Page 1 | 用 Stochastic Replacement + Approximate Counting 的 RowHammer mitigation | 是 |
| RowHammer | RowHammer 行锤击 | Page 1 | 高频 activation 导致 victim row bit-flip | 是 |
| TRR | Target-Row-Refresh | Page 1 | 刷新可能受影响 victim rows 的防护机制 | 是 |
| decoy-row | 诱饵行 | Page 1, Page 5 | 访问次数不足以成为真正 RowHammer 但会污染 count table 的 row | 是 |
| Stochastic Replacement | 随机替换 | Page 1, Page 6 | 以概率决定新 row 是否替换 min-count row | 是 |
| Approximate Counting | 近似计数 | Page 1, Page 6 | 用低成本结构近似保留计数信息 | 是 |
| Passing Gate Effect | 传递栅效应 | Page 2-3 | row activation time 过长导致邻近 cell bit-flip | 是 |
| Time-Weighted Counting | 时间加权计数 | Page 2, Page 5 | 根据 activation time 增加 count weight | 是 |
| RHTH | RowHammer threshold | Page 1 | 触发 RowHammer bit-flip 的 activation 阈值 | 是 |
| MR4 | Mode Register 4 | Page 3-4 | 控制 refresh command interval 的标准特性 | 中 |
| MPA | Maximum Possible Activations | Page 4 | 一个 refresh window 内可能发生的最大 activation 数 | 中 |
| Maximum Disturbance | 最大扰动 | Page 1, Page 10 | observation period 内最大累积 activation | 是 |
| Graphene | Graphene RowHammer defense | Page 10-11 | state-of-the-art counter-based mitigation baseline | 是 |
| CACTI | CACTI 6.0 | Page 11 | 用于估算 area/energy/power 的建模工具 | 中 |
