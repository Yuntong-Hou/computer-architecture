# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何降低真实 UPMEM PIM 系统的编程门槛。
- [ ] 我能解释作者的方法：management interface 在 host CPU 上集中保存 PIM array 的 ID、长度、类型和 PIM DRAM 地址，支持 lookup/register/free，见 Page 3。
- [ ] 我能指出核心创新：提出 SimplePIM，这是面向 real PIM systems 的 high-level programming framework，见 Page 1-2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 11` / `Table 1`
- [ ] 我能复述最重要结果：SimplePIM 的 LoC reduction 为 2.98x-5.93x；例如 histogram 从 114 行降到 21 行，K-means 从 206 行降到 68 行，见 Page 7, Table 1。
- [ ] 我知道这篇文章的局限：当前实现针对 UPMEM，虽然框架思想可迁移，但其他 PIM 架构需要重新实现 backend，见 Page 9-10, Section 6。
- [ ] 我知道这篇文章和其他工作的关系：SimplePIM 是 DaPPA 的前序/相邻工作：两者都降低 UPMEM 编程复杂度，但 DaPPA 更进一步自动管理 dataflow 和 template-based compilation。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
