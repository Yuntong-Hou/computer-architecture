# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何让 DRAM 阵列内部直接完成 AND/OR/NOT 等批量按位操作，而不是把数据搬到处理器。
- [ ] 我能解释作者的方法：TRA 同时激活三行，利用三个 cell 与 bitline 的电荷共享，使 sense amplifier 收敛到多数值；当一条控制行为 0 时得到 AND，当控制行为 1 时得到 OR，见 Page 14-16, Section 3.1.1-3.1.3。
- [ ] 我能指出核心创新：提出 Ambit-AND-OR：通过 Triple-Row Activation (TRA) 让 sense amplifier 实现 majority function，再用控制行得到 AND/OR，见 Page 14-16, Section 3.1。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 22-24` / `Table 4`
- [ ] 我能复述最重要结果：Ambit 平均吞吐比 Skylake 高 44.9x、比 GTX 745 高 32.0x、比 HMC 2.0 高 2.4x；Ambit-3D 相对 HMC 2.0 提升 9.7x，见 Page 27, Figure 21。
- [ ] 我知道这篇文章的局限：许多操作要求源/目标行位于同一 subarray，数据布局与地址映射压力较大，见 Page 18-21, Sections 4.1-4.2。
- [ ] 我知道这篇文章和其他工作的关系：Ambit 与 RowClone、SIMDRAM、ComputeDRAM、PiDRAM 和 DRAM Bender 形成同一条 in-DRAM computation/PuM 研究线：Ambit 提供机制，后续论文更多关注实芯片验证、系统集成与编程框架。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
