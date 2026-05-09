# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：RowHammer 已说明反复开关 row 会破坏 memory isolation；本文进一步证明 row-open time 本身也是危险因素，现有只考虑 activation count 的防御不足。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：作者扫 tAggON、temperature、single/double-sided access patterns 和 tAggOFF，测量最小 aggressor activation count ACmin；再在带 RowHammer 防御的真实系统中构造用户态 RowPress 程序，最后把 Graphene/PARA 适配为 Graphene-RP/PARA-RP 评估开销。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：RowPress 在现实条件下把 ACmin 降低 1-2 个数量级，极端 tAggON=30ms 时一次 activation 可触发 bitflip。 | Page 1-2, Figure 1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：tAggON=7.8us 时 ACmin 平均降低 13.9x；tAggON=70.2us 时平均降低 159.4x、最高 363.8x。 | Page 2, Figure 1 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：对 tAggON >= 7.8us，RowPress vulnerable cells 与 RowHammer cells 的重叠平均低于 0.013%，与 retention failures 低于 0.34%。 | Page 7-8, Figure 9 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：温度从 50C 到 80C 会显著恶化 RowPress，且行为不同于 RowHammer。 | Page 9-10, Figures 11-13 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：Graphene-RP/PARA-RP 能以较低额外开销缓解 RowPress；示例配置下最大 slowdown 分别约 4.6%/13.1%。 | Page 15-16, Table 2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：只限制 maximum row-open time 本身不足，且可能带来高达 34.1% 性能退化。 | Page 15, Section 7 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：本文聚焦 DDR4；DDR5/HBM/LPDDR 的 RowPress 行为需要结合后续实验继续确认。 | 推断，基于 tested chips scope | 基于范围的推断。 | 中 | 后续阅读方向。 |
