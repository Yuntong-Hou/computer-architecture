# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何减少 bulk copy/initialization 经过 memory channel 带来的 latency、bandwidth 和 energy。
- [ ] 我能解释作者的方法：FPM 对同一 subarray 的 src/dst 先 ACTIVATE src 把数据装入 row buffer，再 ACTIVATE dst 让已稳定 bitlines 覆盖 dst cells，最后 PRECHARGE；这相当于一次整行 copy，见 Page 4, Figure 4。
- [ ] 我能指出核心创新：提出 Fast Parallel Mode (FPM)，通过 source ACTIVATE 后紧接 destination ACTIVATE，在同 subarray 内复制整行，见 Page 4, Section 3.1。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 12-13` / `Table 1`
- [ ] 我能复述最重要结果：4KB copy 中，baseline latency/energy 为 1046ns/3.6µJ，FPM 为 90ns/0.04µJ，即 latency 降低 11.62x、energy 降低 74.4x；4KB zeroing 中 FPM latency/energy 降低 6.06x/41.5x，见 Page 9, Table 3。
- [ ] 我知道这篇文章的局限：FPM 要求 source/destination 在同一 subarray、操作整行对齐，不能部分复制，见 Page 4, Section 3.1。
- [ ] 我知道这篇文章和其他工作的关系：RowClone 是 LEC4 很多论文的基础 primitive：Ambit 用它复制临时行，LISA/FIGARO 扩展数据移动范围，SIMDRAM 用它做 vertical layout shift 和 operand movement，PiDRAM 则把它端到端原型化。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
