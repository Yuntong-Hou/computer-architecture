# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：传统图加速多关注 BFS/PageRank 等低复杂度 vertex-centric 算法，而 clique listing、pattern matching、graph learning 等 graph mining 更复杂、更 memory-bound，且并行性不直观。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：SISA 在软件层提供 set-centric formulations 和 thin wrappers，在 ISA 层定义 set instructions，在硬件层由 SISA Controller Unit 选择 sparse array/dense bitvector、merge/galloping/bitwise 等实现，并把操作映射到 PUM 或 PNM。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：SISA-enhanced algorithms 对 established Bron-Kerbosch maximal clique listing 在许多真实图上超过 10x speedup。 | Page 1 and Page 6, contributions | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：Figure 6 显示 full parallelism 下 SISA 对 non-set/set-based baselines 的显著加速，部分任务 >10x。 | Page 11-12, Figure 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：Figure 8 在 large graphs 上继续显示 SISA-PNM/SISA 维持高性能。 | Page 13, Figure 8 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：Table 1 比较 set-centric/SISA 与 vertex-centric、edge-centric、linear algebra、joins 等图抽象的覆盖范围。 | Page 2, Table 1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：Table 4 总结 SISA instructions，覆盖 set union/intersection/difference/count 等操作变体。 | Page 8, Table 4 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：SISA 需要算法以 set-centric 形式重写或包装，软件生态有迁移成本。 | Page 4-8, design sections | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：PUM/PNM 硬件假设较强，真实商业内存系统中部署需要 ISA、runtime 和 memory substrate 支持。 | 推断，基于 PIM design | 基于范围的推断。 | 中 | 后续阅读方向。 |
