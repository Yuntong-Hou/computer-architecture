# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Data-dependent failure | 数据相关失效 | Page 1 | DRAM cell 是否失效依赖邻近 cell 中存储的数据内容。 | 是 |
| MEMCON | 基于内存内容的检测/缓解机制 | Page 1 | 运行时只测试当前内容触发的失效，并据此调节 refresh。 | 是 |
| MinWriteInterval | 最小写间隔 | Page 2 and Section 3.3 | 测试成本能被后续低刷新收益摊销所需的最短内容保持时间。 | 是 |
| PRIL | 概率式剩余间隔长度预测器 | Page 2 and Section 4 | 利用 Pareto 分布性质预测页面写后还会保持多久。 | 是 |
| Aggressive refresh | 激进刷新 | Page 1 | 用更短刷新间隔保护所有行，可靠但性能/能耗成本高。 | 是 |
