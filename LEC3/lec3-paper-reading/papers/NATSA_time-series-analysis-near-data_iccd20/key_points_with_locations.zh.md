# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：Matrix profile 是 exact anytime motif/discord discovery 的代表算法，但低算术强度和大数据量让 CPU/GPU 实现受内存带宽与数据移动限制。 | Page 1, Abstract/Introduction | 论文开头明确给出动机。 | 高 | 这是后续方法的出发点。 |
| 2 | 核心方法：NATSA 将 time series 数据放在 3D-stacked HBM 中，多个 processing units 直接从 HBM 读取并计算 matrix profile 的对角线。设计包含 dot product/update、Euclidean distance、profile update 等专用单元，并通过 diagonal scheduling 分配工作。 | Method/design or survey sections | 正文方法/综述结构支撑。 | 高 | 关注作者如何把问题切成可执行机制。 |
| 3 | 关键结果：NATSA 相比 state-of-the-art multi-core baseline 最高 14.2x、平均 9.9x 性能提升。 | Page 1-2, Abstract/Introduction; Page 6, Figure 7 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 4 | 关键结果：能耗最高降低 27.2x、平均降低 19.4x。 | Page 1-2 and Page 7, Figure 9 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 5 | 关键结果：相比 64 in-order core general-purpose NDP，NATSA 性能提升 6.3x、能耗降低 10.2x。 | Page 1-2 and Page 7 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 6 | 关键结果：NATSA 比 Xeon Phi KNL 和 GTX 1050 在等效性能点有更小面积，且分别节能 11.0x 和 4.1x。 | Page 2 and Page 7, Figures 9-10 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 7 | 关键结果：HBM 能让 SCRIMP 更好扩展，但通用 core 仍无法完全利用 HBM 带宽。 | Page 3 and Page 8, Figures 3 and 11 | 原文给出定量或分类证据。 | 高 | 这些结果支撑主要结论。 |
| 8 | 局限：NATSA 专注 matrix profile/SCRIMP 类 exact anytime 算法，通用性低于 general-purpose NDP cores。 | Page 2-5, design scope | 作者边界或设计假设体现。 | 中 | 迁移/复现时要先检查。 |
| 9 | 追问：专用 accelerator 的收益依赖 HBM 带宽和足够大的 time series；小数据或不同算法可能收益较低。 | 推断，基于 Figures 7 and 11 | 基于实验范围的推断。 | 中 | 适合后续补读。 |
