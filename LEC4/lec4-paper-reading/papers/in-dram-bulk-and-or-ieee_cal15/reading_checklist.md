# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何在 DRAM 内部完成 bulk bitwise AND/OR，而不是经由 CPU 和外部内存通道搬运大量数据。
- [ ] 我能解释作者的方法：核心 primitive 是 triple-row activation：同时激活三行后，bitline 偏移由三颗 cell 的多数值决定；令控制行 R=0 得到 A AND B，R=1 得到 A OR B，见 Page 2, Section 3 与 Figure 4。
- [ ] 我能指出核心创新：提出三行同时连接到 bitline 的机制，使 sense amplifier 输出三者多数值；第三行为 0 时得到 AND，为 1 时得到 OR，见 Page 2, Section 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 6` / `Table 1`
- [ ] 我能复述最重要结果：当 working set 不适合任何 on-chip cache 时，baseline AVX throughput 下降到 3.9 GB/s；conservative 机制达到 22.4 GB/s，aggressive 机制达到 38.2 GB/s，见 Page 3, Section 4 与 Figure 5。
- [ ] 我知道这篇文章的局限：最佳情形依赖 A/B/C 与临时行位于同一 subarray；跨 subarray/bank copy 需要 RowClone-PSM 或更慢路径，见 Page 2, Section 3。
- [ ] 我知道这篇文章和其他工作的关系：这篇 IEEE CAL 短文是 Ambit/MICRO 2017 的早期核心机制版本，重点更集中在 AND/OR 和 FastBit；后续 Ambit 扩展了 NOT、系统集成、SPICE 验证和更多应用。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
