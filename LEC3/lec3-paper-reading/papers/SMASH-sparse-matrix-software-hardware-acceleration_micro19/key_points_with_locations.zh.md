# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：稀疏线性代数广泛用于 ML、图分析和 HPC；压缩可以省存储和跳过零元素，但 CSR/COO 等格式引入 pointer chasing 和 index matching，抵消部分收益。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：软件把 sparse matrix 转成多层 bitmap hierarchy；每个 bitmap bit 表示下层或数据块是否含 non-zero。BMU 缓存并扫描 bitmap buffers，返回 non-zero block 的 row/column indices；CPU 只处理真实非零值，减少 pointer chasing。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：SMASH 对 SpMV 平均提升 38%，对 SpMM 平均提升 44%，相对 state-of-the-art CSR。 | Page 1, Abstract; Page 10-11 evaluation | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：跨 SpMV/SpMM 15 个矩阵平均提升 41.5%，PageRank/BC 平均提升 20%。 | Page 2, contributions | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：理想化去除 CSR indexing 可带来 2.21x/2.13x/2.81x（SpMatAdd/SpMV/SpMM）收益，说明 indexing 是关键瓶颈。 | Page 3, Figure 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：BMU 硬件面积最多仅为 OoO CPU core 的 0.076%。 | Page 1 and Page 13, area evaluation | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：software-only SMASH 即使没有 BMU 也平均优于 CSR，但硬件 BMU 才能充分发挥 bitmap encoding。 | Page 6 and evaluation discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：转换为 SMASH hierarchical bitmap format 有软件预处理成本。 | Page 5, Section 4.1.3 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：对动态更新频繁的 sparse matrix，格式转换和 bitmap 维护成本可能降低收益。 | 推断，基于 conversion process | 基于范围的推断。 | 中 | 后续阅读方向。 |
