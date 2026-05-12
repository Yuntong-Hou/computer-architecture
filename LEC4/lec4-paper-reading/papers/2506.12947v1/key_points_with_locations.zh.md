# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | multiple-row activation-based PuD 是否会比传统 RowHammer 更容易诱发 bitflip。 | Page 1-2 / Introduction | PuD 操作通常需要 consecutive 或 simultaneous multiple-row activation，而现代 DRAM 已知存在 RowHammer/RowPress 等 read disturbance 问题；此前没有工作研究 PuD 多行激活是否会加剧读扰动，见 Page 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 作者把用于 in-DRAM copy 的 consecutive multiple-row activation 称为 CoMRA，把用于 bitwise operations 的 simultaneous multiple-row activation 称为 SiMRA，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 使用 HCfirst 作为主要 vulnerability metric，即诱发首个 bitflip 所需 hammer cycles；越低表示越脆弱，见 Page 5, Section 4.2。 | 方法章节 / Page 2 及后续对应 section | 使用 HCfirst 作为主要 vulnerability metric，即诱发首个 bitflip 所需 hammer cycles；越低表示越脆弱，见 Page 5, Section 4.2。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | mitigation 部分将 PRAC 扩展到多行同时计数，并提出 area-optimized、performance-optimized 与 weighted counting，见 Page 13-14。 | 方法章节后半部分 | mitigation 部分将 PRAC 扩展到多行同时计数，并提出 area-optimized、performance-optimized 与 weighted counting，见 Page 13-14。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | CoMRA 与 SiMRA 分别使最低 HCfirst 相比 RowHammer 低 13.98x 和 158.58x，见 Page 2 与 Page 5/9。 | Evaluation / Results | CoMRA 与 SiMRA 分别使最低 HCfirst 相比 RowHammer 低 13.98x 和 158.58x，见 Page 2 与 Page 5/9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | double-sided CoMRA 中，99% DRAM rows 相比 RowHammer 用更少 activation counts 发生首个 bitflip，见 Page 5-6, Figure 4。 | Evaluation / Results | double-sided CoMRA 中，99% DRAM rows 相比 RowHammer 用更少 activation counts 发生首个 bitflip，见 Page 5-6, Figure 4。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 首次在 316 个真实 DDR4 chips、40 个 modules、4 个制造商上表征 PuD 多行激活导致的 read disturbance，见 Page 1-2。 | Introduction / Contributions | 首次在 316 个真实 DDR4 chips、40 个 modules、4 个制造商上表征 PuD 多行激活导致的 read disturbance，见 Page 1-2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。 | Limitations / Discussion / Future Work | 论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 未来支持 PuD 的 DRAM 标准应如何同时保证计算能力和 read disturbance isolation？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
