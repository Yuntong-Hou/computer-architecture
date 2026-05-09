# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：DRAM refresh 会阻塞 bank、增加访问延迟并消耗能量；随着 DRAM density 上升，refresh latency、throughput loss 和 refresh power 占比都会快速增加，但绝大多数 cells retention time 远高于标准 64ms。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：系统先 profile 每行 retention time；memory controller 维护若干 Bloom filters 表示短 retention rows。运行时 controller 以 64ms 基础周期遍历 candidate rows，根据 period counter 和 bin membership 决定是否发 RAS-only refresh。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：32GB DRAM 中少于 1000 cells 需要短于 256ms refresh interval，约 30 cells 需要短于 128ms。 | Page 1-2, Figure 1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：RAIDR 在 32GB/8-core 系统中减少 74.6% refreshes。 | Page 1 and Page 8, Figure 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：RAIDR 平均性能提升 4.1% normal / 8.6% extended temperature。 | Page 8, Figure 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：RAIDR 平均 energy per access 降低 8.3% normal / 16.1% extended temperature。 | Page 8-9, Figure 8 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：64Gb device capacity 下，RAIDR performance 比 auto-refresh baseline 高 107.9%，access energy saving 达 49.7%。 | Page 10, Figure 9 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：RAIDR 依赖准确 retention time profiling；data pattern 和温度对 retention 的影响留待进一步分析。 | Page 4, Section 3.2 footnote and Page 5, Section 3.5 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：VRT 会使静态 retention profile 过期，需结合 AVATAR/Reaper 等运行时机制。 | 推断，结合后续文献 | 基于范围的推断。 | 中 | 后续阅读方向。 |
