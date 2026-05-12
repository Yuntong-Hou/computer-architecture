# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：COTS DRAM 芯片是否能执行功能完备的布尔操作集合，而不修改芯片或接口。
- [ ] 我能解释作者的方法：NOT 的核心假设是：在 open-bitline 架构中，同时连接 sense amplifier 两端的两个 DRAM cell，可利用反相端把一个 cell 的值取反并写入另一个 cell，见 Page 2, Figure 1a 与 Page 7, Section 5.1。
- [ ] 我能指出核心创新：首次实验展示 unmodified off-the-shelf DRAM chips 能执行 NOT、NAND、NOR，以及多输入 NAND/NOR/AND/OR，见 Page 2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 19-21` / `未检测到核心表格`
- [ ] 我能复述最重要结果：COTS DRAM 可执行 NOT，平均 success rate 为 98.37%，见 Page 1-2 与 Page 8-9。
- [ ] 我知道这篇文章的局限：并非所有厂商芯片都支持所有操作：SK Hynix 支持最完整，Samsung 主要观察到 NOT，Micron 未观察到这些 bitwise operations，见 Page 14, Section 7。
- [ ] 我知道这篇文章和其他工作的关系：这篇论文延伸 Ambit/ComputeDRAM/DRAM Bender 的真实芯片 PuD 路线：从展示 AND/OR 推进到 functionally-complete Boolean logic 和多输入逻辑。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
