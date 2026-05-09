# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 作者想解决的问题：GPU 编程模型擅长表达并行性，却缺少表达 reuse-based locality 与 NUMA locality 的统一接口；软件技巧不便移植，硬件-only 机制又缺少程序语义。 | Page 1, Abstract/Introduction | 论文开头明确把研究目标放在该瓶颈或可靠性挑战上。 | 高 | 这是理解全文动机的入口。 |
| 2 | 核心问题：如何让程序员/编译器表达数据结构、线程组和访问模式之间的局部性关系？；为什么单独 CTA scheduling 或单独 cache policy 不足以转化为性能收益？ | Page 1-2, Introduction | 研究问题在 introduction 中被拆解成可评估问题。 | 高 | 先抓问题，再读方法细节。 |
| 3 | 核心方法：软件通过 descriptor 标注某个数据结构的地址范围、tile 与 compute tile 对应关系、局部性类型和优先级；硬件运行时将这些语义送给 CTA scheduler、cache controller、prefetcher 和 memory placement mechanism，从而选择对应的策略。 | Method/design sections | 作者在方法章节给出机制或抽象设计。 | 高 | 这是本文与相关工作的主要差异。 |
| 4 | 关键结果：Locality Descriptor 在 reuse-based cache hierarchy 场景平均提升 26.6%，最高 46.6%。 | Page 1-2, Abstract/Introduction; Section 6 | 定量结果来自论文实验或摘要贡献段。 | 高 | 这些数字支撑作者主要结论。 |
| 5 | 关键结果：在 NUMA memory system 场景平均提升 53.7%，最高 2.8x。 | Page 1-2, Abstract/Introduction; Section 6 | 定量结果来自论文实验或摘要贡献段。 | 高 | 这些数字支撑作者主要结论。 |
| 6 | 关键结果：单独 CTA scheduling 虽可把 working set 降低 54.5%，但平均性能只提升 3.3%，因为 L1 inflight hit rate 增加导致更多线程一起等待。 | Page 3, Figures 3-4 | 定量结果来自论文实验或摘要贡献段。 | 高 | 这些数字支撑作者主要结论。 |
| 7 | 关键结果：NUMA locality 需要数据放置与 CTA scheduling 协同；简单 first-touch/page placement 对细粒度共享不稳。 | Page 3-4, Figure 5 | 定量结果来自论文实验或摘要贡献段。 | 高 | 这些数字支撑作者主要结论。 |
| 8 | 局限：需要程序员或编译器生成 descriptor，局部性语义不准确会影响优化效果。 | Page 4-6, Section 3 | 作者在机制边界或设计假设中直接体现。 | 中 | 复现或迁移时需要优先检查。 |
| 9 | 需要追问：实验以模拟器为主，真实 GPU 产品中开放 CTA scheduler、cache policy 和 placement 接口的可行性需要进一步工程化。 | 推断，基于 Section 6 methodology | 该点为基于实验范围的推断。 | 中 | 不是论文确定结论，但适合后续阅读。 |
