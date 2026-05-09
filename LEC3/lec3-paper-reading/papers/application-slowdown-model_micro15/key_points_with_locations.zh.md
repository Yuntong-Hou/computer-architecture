# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：多核系统中多个应用共享 LLC 和 memory bandwidth，互相干扰导致单应用性能下降；已有机制要么只估计 cache 或 memory 的一部分影响，要么需要离线 profiling，难以在线准确控制。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：ASM 把应用性能与 shared cache access rate 联系起来。系统周期性给目标应用 memory high priority，测量不受 memory bandwidth 干扰时的 CAR；再用 auxiliary tag store 推断没有 cache contention 时的 cache accesses。最终用 CARalone/CARshared 估计 slowdown，并把该估计输入 cache/memory resource management。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：ASM 在 100 个 workloads 上平均 slowdown estimation error 为 9.9%，比最佳先前机制 FST 的 29.4% 明显更低。 | Page 1, Abstract; Page 6-8, Figure 2/4 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：使用 sampled auxiliary tag store 时，ASM error 从 9.0% 仅升至 9.9%，而 PTCA/FST 分别升至 40.4%/29.4%。 | Page 7-8, Figure 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：数据库 workloads 上，FST/PTCA/ASM sampled errors 分别为 27%/12%/4%。 | Page 8, Section 6.1.2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：ASM-Cache 在 8-core 系统上降低 unfairness 12.5%，并提升性能。 | Page 10-11, Figure 9 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：ASM-QoS 能为指定应用提供 soft slowdown guarantee，同时避免过度牺牲系统吞吐。 | Page 12, Figure 11 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：ASM 依赖 auxiliary tag store、高优先级 sampling phase 和硬件计数器，增加实现复杂度。 | Page 4-6, Section 4-5 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：CAR 与性能的相关性对极端 compute-bound、prefetch-heavy 或 non-cache-sensitive 应用可能减弱。 | 推断，基于 Figure 1 assumption | 基于范围的推断。 | 中 | 后续阅读方向。 |
