# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何不让程序员手动标注 offloading code。
- [ ] 我能解释作者的方法：编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。
- [ ] 我能指出核心创新：提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 11-13` / `Table 2`
- [ ] 我能复述最重要结果：TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。
- [ ] 我知道这篇文章的局限：TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。
- [ ] 我知道这篇文章和其他工作的关系：TOM 属于 processing-near-memory/3D-stacked memory logic layer 路线，与 Ambit/PuD 不同：它在 memory stack logic layer 放计算单元，而不是用 DRAM cell/sense amplifier 本身计算。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
