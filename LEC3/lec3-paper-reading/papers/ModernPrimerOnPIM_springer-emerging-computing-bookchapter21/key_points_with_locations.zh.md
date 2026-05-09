# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：现代系统以 processor-centric 方式把数据搬到计算单元，而数据密集应用、能耗限制和 off-chip data movement 成本共同使这种设计越来越难扩展。 | Page 1, Abstract/Introduction | 论文开头明确给出动机。 | 高 | 这是后续方法的出发点。 |
| 2 | 核心方法：综述式组织：先论证 DRAM scaling、RowHammer/retention 等可靠性压力和 data movement 能耗，再按照 PUM/PNM 两类实现路线分层介绍代表工作，最后总结采用 PIM 的系统问题。 | Method/design or survey sections | 正文方法/综述结构支撑。 | 高 | 关注作者如何把问题切成可执行机制。 |
| 3 | 关键结果：DRAM capacity 扩展远快于 bandwidth/latency 改善，主存瓶颈恶化。 | Page 4-6, Figure 1 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 4 | 关键结果：RowHammer、retention time variation 等可靠性问题说明 memory scaling 需要更智能的 memory controller。 | Page 4-8, Figures 2-3 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 5 | 关键结果：data movement energy 可比计算高 100-1000x，强化了 PIM 的必要性。 | Page 10-12, Figures 7-8 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 6 | 关键结果：PUM 可用 RowClone/Ambit 等低成本 DRAM operation 做 bulk copy、initialization、bitwise operations。 | Page 14-18, Figures 10-12 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 7 | 关键结果：PNM 利用 3D-stacked memory logic layer 支持 Tesseract、移动端 PIM target、GPU offload、genome/time-series 等更通用处理。 | Page 18-24, Figures 15-16 and subsections 7.1-7.6 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 8 | 局限：PIM adoption 仍受 programming model、runtime scheduling、data mapping、coherence、virtual memory 等系统问题限制。 | Page 24-31, Section 8 | 作者边界或设计假设体现。 | 中 | 迁移/复现时要先检查。 |
| 9 | 追问：综述覆盖面大但不是统一实验平台，跨案例的数字不能直接横向比较。 | 推断，基于 survey nature | 基于实验范围的推断。 | 中 | 适合后续补读。 |
