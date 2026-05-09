# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：已有 RowHammer tracking/sampling/partitioning/clean-slate 方案要么需要大量 SRAM/CAM，要么依赖 memory controller、DRAM、OS 多方协作，难以部署；DDR4 仍受 multi-row RowHammer attacks 影响。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：Panopticon 在 DRAM bank 内增加 counter mats、incrementer/testing logic、service queue 和 ALERTn state machine。每次 ACTIVATE 同步更新对应 row counter；threshold bit toggle 时将 row address 入队；收到 REF 或队列需要服务时刷新邻近 victim rows，必要时 assert ALERTn 让 controller 暂停发命令。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：Graphene 在 DDR4 每 channel 需 39.23KB CAM、每 CPU 约 156.9KB；BlockHammer/TWiCe 需求更高。 | Page 1-2, Table I | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：Panopticon service queue 只需 8 entries/bank；DDR4 row address 18 bits 时约 144 bits/bank，远小于 Graphene 2511 bits/bank。 | Page 5, Section V-D | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：Panopticon 用 threshold bit，如 b10 toggle 时每 1024 activations 入队一次，避免比较完整 counter value。 | Page 3-5, Figure 1/Figure 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：安全分析显示若不能请求 controller 时间，攻击者可在较短时间内填满 service queue，因此 ALERTn 机制是必要条件。 | Page 5-6, Figures 6-7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：16-bit counter 可支持最高 65,536 activations threshold，适合现代较低 RowHammer threshold 场景。 | Page 6, Section VII-C | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：若没有 ALERTn 或类似方式请求额外时间，攻击者可通过填满 service queue 破坏安全性。 | Page 5-6, Figures 6-7 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：Panopticon 需要 DRAM 内部设计改动，仍依赖厂商采用和验证，且对 DDR5/HBM 需重新适配。 | 推断，基于 in-DRAM architecture | 基于范围的推断。 | 中 | 后续阅读方向。 |
