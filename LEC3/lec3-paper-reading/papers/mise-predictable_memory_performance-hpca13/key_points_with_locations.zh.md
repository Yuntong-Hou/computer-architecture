# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：多程序共享主存会导致不同应用 slowdown 不可预测；已有 memory scheduler 常优化吞吐或公平性，但对单个应用相对独占运行的 slowdown 估计不准确，难以给 QoS 或 OS 提供可靠反馈。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：MISE 的核心是 slowdown ≈ ARSR/SRSR，并对非 memory-bound 应用乘入 memory stall fraction。memory controller 通过 interval/epoch 机制轮流给应用最高优先级，测量 near-alone request-service-rate，再用 lottery scheduling 分配带宽以满足 QoS 或公平性目标。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：MISE 在 300 workloads 上 average slowdown estimation error 为 8.1%，而 STFM 为 29.8%。 | Page 5-6, Table 2 and Section 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：5M cycles interval、10000 cycles epoch 下 MISE 达到最低约 8.1% error。 | Page 6, Table 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：MISE-QoS 在 3000 data points 中满足 slowdown bound 80.9%，达到 AlwaysPrioritize 可满足情况的 97.5%。 | Page 8, Table 5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：MISE-QoS 正确预测 bound 是否满足的比例为 95.7%。 | Page 1-2 and Page 8, Table 5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：bound=10^3 时，MISE-QoS 比 AlwaysPrioritize 提高 harmonic speedup 12%、weighted speedup 10%，maximum slowdown 降低 13%。 | Page 9, Figure 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：MISE 主要估计 main memory interference，其他共享资源 slowdown 留作未来工作。 | Page 12, Conclusion | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：highest-priority sampling 会改变短期调度行为，在实时或极短 phase workload 中需重新评估。 | 推断，基于 epoch/interval design | 基于范围的推断。 | 中 | 后续阅读方向。 |
