# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| DASH | deadline-aware high-performance scheduler | Page 1 | 面向 CPU+HWA 异构系统的内存调度器。 | 是 |
| Distributed Priority | 分散式优先级 | Page 5-7 | HWA 落后时在整个 period 中分散给予优先，而不是最后集中抢占。 | 是 |
| Deadline-met ratio | deadline 满足率 | Page 10-16 | HWA frames 在 deadline 前完成的比例。 | 是 |
| Memory-intensive application | 内存密集应用 | Page 5-8 | 对内存带宽敏感但单请求 latency sensitivity 相对低的 CPU 应用。 | 是 |
