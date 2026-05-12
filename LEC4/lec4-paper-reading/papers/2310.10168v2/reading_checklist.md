# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何让程序员不用手动管理 UPMEM 的数据分布、内存分配和通信。
- [ ] 我能解释作者的方法：用户用 C/C++ 调用 DaPPA pattern APIs 描述数据转换，DaPPA 负责将 primitive 翻译并并行化到 CPU 和 DPUs，见 Page 2 与 Page 4-7。
- [ ] 我能指出核心创新：提出首个面向 UPMEM 的 data-parallel pattern-based programming framework，见 Page 2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 6` / `Table 1`
- [ ] 我能复述最重要结果：相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC，见 Page 11, Table 1。
- [ ] 我知道这篇文章的局限：评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。
- [ ] 我知道这篇文章和其他工作的关系：DaPPA 与 SimplePIM、PrIM、UPMEM 生态相关；它关注的是 PIM 编程抽象，而不是 DRAM 内部电路 primitive，与 Ambit/RowClone/SIMDRAM 属于不同层次。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
