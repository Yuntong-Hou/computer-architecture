# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何把 PUD 操作粒度从完整 DRAM row 缩小到 mat/segment，以匹配应用实际 SIMD parallelism。
- [ ] 我能解释作者的方法：MIMDRAM 在硬件上增加 latches、isolation transistors 和 selection logic，使单个 DRAM mat 可被独立寻址并执行 PUD operation，见 Page 4-6, Section 4.1。
- [ ] 我能指出核心创新：提出首个面向 general-purpose applications 的端到端 MIMD PUD 系统，见 Page 3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 14` / `Table 2`
- [ ] 我能复述最重要结果：MIMDRAM 平均提供 SIMDRAM 的 15.6x SIMD utilization、14.3x energy efficiency 和 34x performance，见 Page 12, Figure 9。
- [ ] 我知道这篇文章的局限：若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。
- [ ] 我知道这篇文章和其他工作的关系：MIMDRAM 与 SIMDRAM、DRISA、Fulcrum 直接相关；它不是证明某个 DRAM primitive 能工作，而是提出更灵活的 PuD 系统架构与编译支持。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
