# Reading Checklist

- [ ] 我能说清楚这篇文章解决的问题：multiple-row activation-based PuD 是否会比传统 RowHammer 更容易诱发 bitflip。
- [ ] 我能解释作者的方法：使用 HCfirst 作为主要 vulnerability metric，即诱发首个 bitflip 所需 hammer cycles；越低表示越脆弱，见 Page 5, Section 4.2。
- [ ] 我能指出核心创新：首次在 316 个真实 DDR4 chips、40 个 modules、4 个制造商上表征 PuD 多行激活导致的 read disturbance，见 Page 1-2。
- [ ] 我能看懂主要实验表格和图，例如 `Figure 25` / `DRAM module table`
- [ ] 我能复述最重要结果：CoMRA 与 SiMRA 分别使最低 HCfirst 相比 RowHammer 低 13.98x 和 158.58x，见 Page 2 与 Page 5/9。
- [ ] 我知道这篇文章的局限：论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。
- [ ] 我知道这篇文章和其他工作的关系：PuDHammer 是对 SiMRA/FCDRAM/Ambit 等 PuD 能力论文的重要安全可靠性补充：前者证明 DRAM 能算，PuDHammer 提醒多行激活可能显著加剧 read disturbance。
- [ ] 我知道哪些结论有原文位置支持
- [ ] 我知道哪些问题还需要继续查证
