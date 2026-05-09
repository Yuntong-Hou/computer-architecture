# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：现代 DRAM scaling 促使厂商在芯片内部加入不可见、专有、未公开的 on-die ECC；这改善 yield，却让研究者无法直接观察物理 error mechanisms，导致 retention、latency、RowHammer 等实验性 characterization 结果被 ECC 扭曲。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：EIN 为候选 ECC schemes 和 pre-correction error distribution 建立统计模型；用 EINSim 对每组模型参数进行 Monte Carlo simulation，估计观测 post-correction PMF 的 likelihood；再用 MAP/grid search 找到最可能的 ECC scheme 与 pre-correction error rate。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：on-die ECC 使 observed BER 与 pre-correction BER 的关系依赖具体 ECC scheme，不能直接比较不同 devices。 | Page 1-2, Figure 1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：EIN 研究 232 个带 on-die ECC 和 82 个无 on-die ECC LPDDR4 devices。 | Page 1-2 and Page 8, Section 6 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：EIN 推断被测 on-die ECC 为 single-error correction Hamming code (n=136, k=128, d=3)。 | Page 1-2, Abstract/Contributions; Page 9-10, Figure 8/Table 2 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：pre-correction errors 的 uniform-random model 与实验概率吻合。 | Page 8, Figure 5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：EIN 可同时推断 data pattern、ECC scheme 和 pre-correction error rate，并用 Figure 9 展示 MAP model 与实验 PMF 的拟合。 | Page 10, Figure 9 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：EIN 恢复了温度与 retention error 的底层 exponential relationship；post-correction curves 在可测范围外会偏离真实趋势。 | Page 11, Figure 11 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：MAP estimation 只能在候选模型中选择最可能模型，不能证明未纳入模型的真实 ECC scheme 不存在。 | Page 7-8, Section 5.5/5.8 | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：真实厂商 ECC 可能随产品/世代变化，候选 code set 与实验条件需随设备重新校准。 | 推断，基于 Sections 4-7 | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
