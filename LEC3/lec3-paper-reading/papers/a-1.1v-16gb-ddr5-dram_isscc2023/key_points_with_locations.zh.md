# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：随着 1a-nm 及更小 DRAM 工艺缩放，cell 间耦合、row hammer 和 refresh/retention 余量持续恶化；DDR5 引入 RFM 等机制，但真实芯片还需要把 controller-side 与 in-DRAM tracking/refresh 协同设计。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：芯片把 DDR5 RFM command path 与内部 hammer tracking 结合：controller 根据 RAACNT/RAAIMT 触发 RFM；PAT 以概率方式识别 aggressor；PRHT 使用 R/H cells 记录每条 WL 的 activation count 并在超阈值时刷新邻近 rows；multi-step precharge 和 VBB modulation 分别改善 row hammer/retention circuit margin。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：综合方案将 row hammer attack failure probability 降低 93.1%，并将 retention time 提升 17%。 | Page 1, Abstract-style summary | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：multi-step precharge 将 intrinsic row-hammer tolerance 提升 37%。 | Page 2, Figure 28.8.4/28.8.5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：PRHT 在 50 个 malicious row-hammer patterns 下将 failure probability 降低 90.5%。 | Page 2, Figure 28.8.6 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：PAT logic 在 intrinsic row-hammer tolerance 降低 66% 的条件下仍通过 50 种 malicious patterns。 | Page 2, Figure 28.8.6 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：VBB temperature modulation 在 90C 下使 refresh retention time 提升 17%。 | Page 3, Figure 28.8.7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：论文篇幅为 ISSCC short paper，算法与电路细节、面积/功耗开销披露有限。 | 全文形式，Page 1-3 | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：由于机制依赖 DDR5 RFM/controller 协作，不同系统 controller 策略会影响端到端保护效果。 | 推断，基于 RFM algorithm | 基于范围的推断。 | 中 | 后续阅读方向。 |
