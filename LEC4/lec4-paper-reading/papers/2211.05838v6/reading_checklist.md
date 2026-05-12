# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何完全暴露 DRAM command/data interface，让实验程序自由安排 ACT/PRE/READ/WRITE 与时序。
- [ ] 我能解释作者的方法：DRAM Bender 通过 FPGA 直接连接 DRAM PHY/DFI，提供 program memory、data buffers、readback FIFO、periodic operation scheduler 等模块，见 Page 4-7, Section 3。
- [ ] 我能指出核心创新：提出 DRAM Bender，拥有 nonrestrictive instruction set architecture、C++/Python API 和 modular FPGA design，见 Page 1-2 与 Page 4-8。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 12` / `Table 1`
- [ ] 我能复述最重要结果：double-sided RowHammer 中 T 越接近 1，bit-flips 越多；V2 行在 T=64K 时三家厂商平均 bit-flips 为 31.9/9.9/71.2，而 T=1 时为 314.8/50.7/604.9，见 Page 10, Figures 8-9。
- [ ] 我知道这篇文章的局限：DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。
- [ ] 我知道这篇文章和其他工作的关系：DRAM Bender 与 PiDRAM 都是 FPGA-based real-DRAM infrastructure；PiDRAM 更偏端到端系统/PuM 集成，DRAM Bender 更偏底层 DRAM command-level characterization 和测试。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
