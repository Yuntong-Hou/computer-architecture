# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：现代 SoC 中 CPU、GPU 和专用 HWA 共享 DRAM。HWA 往往有 frame deadline，CPU 需要高吞吐；简单优先 HWA 会牺牲 CPU，简单优先 CPU 又会错过 HWA deadline。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：DASH 监控每个 HWA 的 period、deadline、remaining requests 和 progress，判断其是否 on track。若 HWA 落后，scheduler 提升其请求优先级；同时根据 CPU application memory intensity 区分受影响对象，优先保护 latency-sensitive/memory-nonintensive apps。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：DASH 比最佳先前 scheduler 提升 9.5% CPU performance，并始终满足所有 HWAs/GPUs 的 deadlines。 | Page 1, Abstract; Page 15-17, Figure 5/Table V | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：HWA-friendly scheduler 可接近 100% deadline-met ratio，但 CPU performance 比 CPU-friendly scheduler 低约 12%。 | Page 3-4, motivation | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：Figure 5 显示 DASH 在 80 workloads 上兼顾 CPU performance 与 deadline-met ratio。 | Page 15-16, Figure 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：Table V 显示 DASH 的 deadline-met ratio/frame rate 与能满足 deadline 的动态调度相当，但 CPU 性能更好。 | Page 16, Table V | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：CPU-GPU-HWA 场景中 DASH 仍能保持 frame rate，并控制 CPU slowdown。 | Page 19-21, Figure 9 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：DASH 假设 HWA 的 deadline、period 和 memory request demand 可由系统获知或估计。 | Page 6-9, design | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：真实 SoC 中不同 HWA 的 burstiness、QoS contract 和 memory controller 实现会影响策略迁移。 | 推断，基于 simulator evaluation | 基于范围的推断。 | 中 | 后续阅读方向。 |
