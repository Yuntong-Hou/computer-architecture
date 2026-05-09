# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：DRAM/NAND/PCM 等存储技术持续缩放带来更高密度和更低成本，但 cell-to-cell interference、retention、variation 等可靠性问题可能越过抽象边界，破坏 memory isolation 并成为安全漏洞。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：本文是综述和立场论文。作者复盘 ISCA 2014 RowHammer characterization、Project Zero 与后续攻击，讨论 immediate 和 long-term countermeasures，并把 RowHammer 放入更广泛的 scaled memory disturbance/retention/security 语境。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：测试 129 个 DRAM modules，110 个出现 RowHammer errors，最早可追溯到 2010 年，2012-2013 年 modules 全部 vulnerable。 | Page 1, Section II and Figure 1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：简单用户态程序能在 commodity AMD/Intel systems 上可靠诱发 RowHammer errors，违反 read 不应修改其他地址、write 只修改目标地址两个不变量。 | Page 2, Section II-A | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：RowHammer 已被用于 Project Zero kernel privilege escalation、remote server takeover、VM takeover、Android device takeover 和 browser read/write access 等攻击。 | Page 2, Section II-B | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：单纯提高 refresh rate 若要消除测试中所有 RowHammer-induced errors 需要约 7x refresh rate，代价是 power/performance/QoS。 | Page 2, Section II-C | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：PARA 在每次关闭 row 后以很低概率刷新 adjacent rows，可用 negligible performance/energy overhead 消除 RowHammer vulnerability，但需要 controller/DRAM 支持邻接信息或内部 refresh。 | Page 3, Section II-C | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 作者局限：PARA 不能立即部署，因为需要 memory controller 或 DRAM chip 修改，并需要知道物理相邻 rows。 | Page 3, Section II-C | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 9 | 推断局限：本文是 invited/survey-style 论文，很多结论依赖引用的先前实验和攻击论文，而非新实验。 | 推断，基于全文结构 | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
