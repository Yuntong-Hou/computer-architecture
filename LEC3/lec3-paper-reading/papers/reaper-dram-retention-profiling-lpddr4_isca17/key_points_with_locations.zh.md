# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：许多 refresh-reduction 技术假设可以快速找到延长 refresh interval 后会失败的 cells，但 brute-force retention profiling 需要写模式、等待目标 refresh interval、读回检查，在线频繁 profiling 时开销过高，且 VRT 和 DPD 会让失败集合持续变化。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：REAPER 不是在目标 refresh interval/temperature 上直接 brute-force 等待，而是在 reach conditions 下运行 profiling：例如比目标 refresh interval 长 250ms，或提高温度。由于目标下会失败的 cells 在激进条件下更可靠地失败，系统可用较少 iterations 捕获高覆盖率；随后用 ECC/mitigation 处理未捕获 failures 和 false positives。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：在目标 refresh interval 上方增加 250ms profiling，REAPER 平均可达到 >99% coverage、<50% false positive rate，并比 brute-force 快 2.5x。 | Page 1-2, Abstract/Contributions; Page 8, Section 6.1.2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：更激进 reach conditions 可把 speedup 推到 >3.5x，但 false positive rate 会超过 75%。 | Page 8, Section 6.1.2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：2GB DRAM + SECDED + 1024ms/45C 示例下，99% coverage profile 的 longevity 约 2.3 days。 | Page 9, Section 6.2.2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：64Gb chips、512ms operating point 下，REAPER 平均性能提升 16.3%，DRAM power 平均降低 36.4%。 | Page 11-12, Figure 13 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：64Gb、1024ms 时 REAPER 平均性能提升 13.5%，brute-force 仅 7.5%；1280ms 时 brute-force 平均退化 -5.4%，REAPER 仍有 8.6% 平均收益。 | Page 12, Figure 13 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：与 ArchShield 结合时，REAPER 平均性能提升 12.5%，比 brute-force profiling 组合高 5.6%。 | Page 12, Section 7.3.2 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：结果依赖具体假设：45C、reach profiling 2.5x speedup、32 chips/module、100% coverage 假设和 20 个 workload mixes。 | Page 13, Section 7.3.2 caveat | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：profiling 本身仍依赖 retention failure mitigation，如 ECC、bit repair 或 remapping；单独 REAPER 不等于完整可靠性方案。 | 推断，基于 Sections 6-7 | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
