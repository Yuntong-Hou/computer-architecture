# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：如何在 3D-stacked memory 的多个 banks 之间直接、快速地复制数据。
- [ ] 我能解释作者的方法：NoM 给每个 bank 增加简单 circuit-switched router，包括 crossbar、single-cycle latch、local slot table/controller 和 links；bank 可通过 NoM links 或传统 bus 发送/接收数据，见 Page 2, Figure 1。
- [ ] 我能指出核心创新：提出 Network-on-Memory (NoM)，用 3D mesh links 连接 highly-banked memory 中相邻 banks，见 Page 1-2, Section 2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 4` / `未检测到核心编号表`
- [ ] 我能复述最重要结果：NoM 相比 RowClone 平均 IPC 高 75%，因为它加速 inter-bank copies 并允许多个 inter-bank copies 与其他 memory accesses 并发执行，见 Page 4, Section 3/Figure 4。
- [ ] 我知道这篇文章的局限：NoM 主要针对 highly-banked 3D-stacked memory；传统低 bank 数 DDR 系统的收益和实现形态不一定相同，见 Page 1-2。
- [ ] 我知道这篇文章和其他工作的关系：NoM 接在 RowClone/LISA 之后补齐更高层次的数据移动：RowClone 做同 subarray copy，LISA 做跨 subarray copy，NoM 做 3D-stacked memory 中跨 bank copy。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
