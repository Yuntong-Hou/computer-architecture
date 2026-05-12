# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何在真实系统中发出 PuM 所需的 DRAM command sequence 与 violated timing parameters。
- [ ] 我能解释作者的方法：PiDRAM 的硬件由可扩展 memory controller 和 POC 组成；POC 通过 memory-mapped interface 让软件用普通 LOAD/STORE 触发 PuM operation，见 Page 2, Page 4-6。
- [ ] 我能指出核心创新：提出 PiDRAM，这是首个面向 commodity DRAM based PuM 的 flexible end-to-end open-source framework，见 Page 2-3。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 9-11` / `Table 2`
- [ ] 我能复述最重要结果：Bare-Metal RowClone-Copy 相对 CPU-copy 提升 317.5x-364.8x，RowClone-Initialize 提升 172.4x-182.4x，见 Page 12, Figure 9。
- [ ] 我知道这篇文章的局限：prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。
- [ ] 我知道这篇文章和其他工作的关系：PiDRAM 更像 Ambit/RowClone/D-RaNGe 之后的系统原型平台论文：它不主要提出新 DRAM 计算 primitive，而是解决如何把这些 primitive 端到端接入真实系统。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
