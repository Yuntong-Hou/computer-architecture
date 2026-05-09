# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：RowHammer 证明电路级失效机制可以变成广泛、实用的系统安全漏洞；随着 DRAM scaling，类似问题可能继续出现。 | Page 1, Abstract/Introduction | 论文开头明确给出动机。 | 高 | 这是后续方法的出发点。 |
| 2 | 核心方法：回顾性 survey：先复述 RowHammer 机制与原始实验，再按 attacks、defenses、circuit-level studies、platforms、persistence、broader context 分类梳理后续文献。 | Method/design or survey sections | 正文方法/综述结构支撑。 | 高 | 关注作者如何把问题切成可执行机制。 |
| 3 | 关键结果：原始研究测试 129 个 2008-2014 年模块，其中 110 个表现 RowHammer errors，最早可追溯到 2010。 | Page 2, Figure 1 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 4 | 关键结果：2012-2013 年模块全部 vulnerable，说明问题随制程缩放显著出现。 | Page 2, Figure 1 discussion | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 5 | 关键结果：Google Project Zero 2015 证明用户态程序可利用 RowHammer 获取 kernel privileges。 | Page 1 and Section III-A | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 6 | 关键结果：PARA 以很低概率刷新 adjacent rows，p=0.001 或 0.005 时可提供强保证且性能开销小于 0.75%。 | Page 4, Section II-E | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 7 | 关键结果：ECC、提高 refresh rate、row remapping、access counters 等方案各有成本或覆盖限制。 | Page 4-8, Sections II-E and III-B | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 8 | 局限：提高 refresh rate 是直接短期方案，但会带来显著性能/能耗问题。 | Page 7, Section III-B | 作者边界或设计假设体现。 | 中 | 迁移/复现时要先检查。 |
| 9 | 追问：作为 retrospective，它整合已有结果，不提供统一实验复现。 | 推断，基于文章类型 | 基于实验范围的推断。 | 中 | 适合后续补读。 |
