# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：是否能在 off-the-shelf DRAM cell 中稳定写入并验证 fractional value。
- [ ] 我能解释作者的方法：Frac operation 先 PRECHARGE bitline 到 Vdd/2，再 ACTIVATE target row，并在 sense amplifier 完全放大前立刻 PRECHARGE 中断，使 cell 保留介于 Vdd/2 与初始值之间的电压，见 Page 3, Figure 3。
- [ ] 我能指出核心创新：首次展示在未修改商用 DRAM 中存储 fractional values，见 Page 1-2, Introduction。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 11-12` / `DRAM group table`
- [ ] 我能复述最重要结果：Frac 使平均约 55% cells 的 retention time 随 Frac 次数单调下降，支持其电压被逐步拉向 Vdd/2 的解释，见 Page 6, Figure 6。
- [ ] 我知道这篇文章的局限：retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。
- [ ] 我知道这篇文章和其他工作的关系：FracDRAM 是 ComputeDRAM 的延伸：ComputeDRAM 利用商用 DRAM 的多行激活实现 0/1 逻辑，FracDRAM 则把中间电压状态显式作为工具，用于 majority 稳定化和 security primitive。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
