# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何减少传输未使用 cache-block word 的能耗。
- [ ] 我能解释作者的方法：VBL 复用 DRAM I/O 中每个 burst cycle 选择一个 word 的既有机制，让一次 cache block transfer 可以只包含所需 word，见 Page 2, Page 6。
- [ ] 我能指出核心创新：提出 Variable Burst Length (VBL)，按请求 sector 数动态调整 burst cycle 数，见 Page 2 与 Page 6, Section 4.2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 13-15` / `Table 3`
- [ ] 我能复述最重要结果：读/写一个 sector 相比读/写全部 sector，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%，见 Page 10, Figure 7。
- [ ] 我知道这篇文章的局限：stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。
- [ ] 我知道这篇文章和其他工作的关系：与 Ambit/RowClone 等 in-DRAM computation 不同，Sectored DRAM 主要解决常规内存访问的能耗浪费；但它同样利用 DRAM 内部 mat/row 组织，是更广义 DRAM architecture optimization 研究线的一部分。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
