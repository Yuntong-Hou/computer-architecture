# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何在 DRAM array 内实现 AND/OR/NOT 且保持低面积开销。
- [ ] 我能解释作者的方法：TRA 同时激活三行共享同一组 sense amplifiers 的 rows，产生三输入 majority；将其中一行初始化为 0 得到 AND，初始化为 1 得到 OR，见 Page 4-5。
- [ ] 我能指出核心创新：提出 Ambit-AND-OR，通过 triple-row activation 实现 majority function 并由控制行得到 AND/OR，见 Page 4-6, Section 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 10-12` / `Table 1`
- [ ] 我能复述最重要结果：Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 比 HMC 2.0 高 9.7x，见 Page 10, Figure 9。
- [ ] 我知道这篇文章的局限：Ambit 要求操作数映射到同一 subarray，并需要 RowClone 在 designated rows 间搬移，见 Page 5-8。
- [ ] 我知道这篇文章和其他工作的关系：Ambit 是 LEC4 多篇 PuD 论文的关键源头：后续 DRAM Bender、FCDRAM、SiMRA、PuDHammer 等都在不同方向验证、扩展或审视 Ambit 类多行激活机制。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
