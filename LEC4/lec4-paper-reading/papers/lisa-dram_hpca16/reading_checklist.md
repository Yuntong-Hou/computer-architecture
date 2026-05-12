# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何让不同 subarray 之间也能像同一 subarray 内那样快速移动整行数据。
- [ ] 我能解释作者的方法：LISA 的硬件核心是给相邻 subarrays 的同列 bitlines 增加 link；当 link 打开时，一个 row buffer 可通过 bitlines 驱动相邻 row buffer，见 Page 3, Figure 3。
- [ ] 我能指出核心创新：提出 Low-Cost Inter-Linked SubArrays (LISA)，在相邻 subarrays 的 bitlines 间加入 isolation transistors，见 Page 2-4, Section 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 16` / `Table 1`
- [ ] 我能复述最重要结果：RBM 在保守 60% margin 后仍达到 8ns latency 和 500 GB/s data transfer bandwidth，相当于 DDR4-2400 64-bit channel 的 26x，见 Page 2 与 Page 4。
- [ ] 我知道这篇文章的局限：LISA 需要修改 DRAM array/subarray 间连接和控制逻辑，虽面积开销小但仍需 DRAM 厂商采纳，见 Page 8, Section 7。
- [ ] 我知道这篇文章和其他工作的关系：LISA 补上 RowClone/Ambit 的 inter-subarray 数据移动短板：RowClone 负责同 subarray 快速复制，LISA 负责跨 subarray 高带宽搬移，因此它也是后续 FIGARO、NoM 等数据移动论文的重要前序。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
