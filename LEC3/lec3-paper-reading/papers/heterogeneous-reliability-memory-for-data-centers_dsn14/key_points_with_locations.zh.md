# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：服务器 memory 是数据中心资本成本的重要组成部分，ECC/Chipkill/mirroring 等 one-size-fits-all 可靠性机制增加成本与延迟，但很多 data-intensive workloads 对部分 memory errors 具有天然 masking/recovery 能力。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：作者通过 controlled error injection 和 memory access monitoring 测量错误命运、safe ratio 和 recoverability；再基于错误模型和可用性目标，把不同 memory regions 映射到不同硬件可靠性技术和软件 recovery response。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：传统 error protection 可增加 memory system cost 12.5%，而某些应用无需保护也可在大量错误下达到 99.00% availability。 | Page 1, Abstract | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：三类应用的 memory error vulnerability 和 incorrect result rate 差异最高达 6 个数量级。 | Page 6, Figure 3 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：WebSearch 至少 82.1% address space 可从 disk 隐式恢复，56.3% 可显式恢复。 | Page 7, Table 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：Detect&Recover/L 可减少 server hardware cost 4.7%（范围 0.9%-8.4%），达到 99.90% availability，每百万 queries 约 12 个 incorrect results。 | Page 10, Table 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：在 2000 errors/month 下，WebSearch 和 Memcached 即使无 ECC 也可达到 99.00% single-server availability。 | Page 11, Figure 8 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 局限：使用 less reliable/no-ECC memory 的前提是数据多为 read-only/transient，且错误不会长期传播到 persistent storage。 | Page 11, Section VI-C | 设计边界或作者说明。 | 中 | 实现时需关注。 |
| 9 | 追问：业务可接受的 incorrect results per million queries 取决于应用和 SLA，不能直接推广到所有服务。 | 推断，基于 WebSearch case study | 基于范围的推断。 | 中 | 后续阅读方向。 |
