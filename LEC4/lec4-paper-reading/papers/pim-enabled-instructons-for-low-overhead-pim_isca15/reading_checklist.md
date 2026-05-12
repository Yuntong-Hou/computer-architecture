# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何让 PIM operation 像普通 host instruction 一样使用，而不是引入全新的 PIM 编程模型。
- [ ] 我能解释作者的方法：PEI 是可以由 host-side PCU 或 memory-side PCU 执行的同一条指令；程序员或编译器只需替换普通操作为 PEI，硬件决定执行位置，见 Page 3, Section 3.1。
- [ ] 我能指出核心创新：提出 PIM-enabled Instructions (PEIs)，把简单 PIM operation 表示为 host ISA extension，见 Page 2-4, Section 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 12` / `Table 1`
- [ ] 我能复述最重要结果：PageRank 中单个 in-memory atomic add 最高带来 53% speedup，但在高 cache locality 图上也会导致最高 20% performance degradation，并可造成 50x DRAM accesses，见 Page 3, Figure 2。
- [ ] 我知道这篇文章的局限：单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。
- [ ] 我知道这篇文章和其他工作的关系：这篇论文属于 processing-near-memory/PIM interface 路线，与 RowClone/Ambit/SIMDRAM 的 DRAM-array primitive 不同；它解决的是如何把简单 memory-side operations 融入 ISA、cache coherence 和 locality-aware scheduling。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
