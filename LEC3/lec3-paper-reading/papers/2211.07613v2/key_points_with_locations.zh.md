# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | RowHammer 定义 | Page 1, Abstract/Introduction | 反复访问 aggressor rows 导致 nearby victim rows bit-flips | 高 | 这是所有后续论文的基础现象 |
| 2 | RowHammer 是安全问题而非只是一种错误 | Page 1 | 可破坏 integrity/confidentiality/availability，因为它破坏 memory isolation | 高 | 体系结构可靠性问题会升级为系统安全问题 |
| 3 | 问题随 DRAM scaling 变严重 | Page 1 | threshold 十年降低超过 10x，bit-flips 增加约 500x | 高 | 解释为什么不能靠旧防御长期解决 |
| 4 | 2014 原始工作暴露 DDR3 大规模 vulnerability | Page 2, Section 2 | 超过 80% commodity DDR3 modules vulnerable | 高 | RowHammer 研究的起点 |
| 5 | 早期工业防护包括 refresh rate increase、pTRR、TRR | Page 2, Section 2.1 | 作者指出提高 refresh 有高性能/能耗开销，TRR 不公开实现 | 高 | 工业防护存在透明度和保证不足 |
| 6 | TRRespass 证明 TRR-protected DDR4 仍 vulnerable | Page 2-3, Section 3 | many-sided RowHammer 可绕过 TRR tables | 高 | 2020 后研究的重要转折 |
| 7 | U-TRR 可 reverse engineer TRR | Page 3 | 用 retention errors 作为 side channel 发现 TRR refresh 行为 | 中 | 说明 security by obscurity 不稳 |
| 8 | Revisiting RowHammer 实证证明 worsening | Page 3, Figure 1 | newer DRAM first bit-flip 更早，数量更多 | 高 | 支撑“未来更难防”的判断 |
| 9 | DDR5 RFM 有潜在不必要开销 | Page 3 | MC bank-level activation counts 可能频繁触发 RFM | 中 | 标准机制并非完美答案 |
| 10 | Future direction 1：更基础全面理解 | Page 5, Section 5.1 | aging、temperature、voltage、access patterns 仍需系统研究 | 高 | 后续实验论文的研究空间 |
| 11 | Future direction 2：高效 fully-secure solutions | Page 6, Section 5.2 | 作者主张 system-memory co-design | 高 | SMD/DSAC 等论文可放到这条线 |
| 12 | 结论：还需要大量研究 | Page 6, Conclusion | RowHammer 是 fundamental DRAM scaling problem | 高 | 不应把它视为已解决问题 |
