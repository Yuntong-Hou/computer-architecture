# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何避免 in-DRAM cache 以整行粒度搬移大量不会被访问的数据。
- [ ] 我能解释作者的方法：FIGARO 允许两个 local row buffers 通过 global row buffer 进行 unaligned data transfer，使源列可写入目标不同列，不经过 off-chip memory channel，见 Page 2 与 Section 4。
- [ ] 我能指出核心创新：提出 FIGARO substrate，支持 bank 内 subarrays 之间 column/cache-block granularity data relocation，且 latency distance-independent，见 Page 2-6。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 12-14` / `Table 1`
- [ ] 我能复述最重要结果：FIGCache-Fast 在 20 个 eight-core workloads 上平均提升 16.3% performance；100% memory-intensive workloads 平均提升 27.1%，见 Page 9, Figure 8。
- [ ] 我知道这篇文章的局限：需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。
- [ ] 我知道这篇文章和其他工作的关系：FIGARO 与 RowClone/LISA 同属 DRAM 内数据移动路线；与 Ambit/PuD 计算不同，它主要解决 DRAM 内缓存和 relocation 粒度问题，但同样利用 subarray/global row buffer 结构。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
