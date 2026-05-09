# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：大规模图处理有随机访问、低 locality、每顶点计算少等特征，传统 CPU/缓存/外部 memory bandwidth 难以扩展；仅增加 cores 或使用 HMC 外部带宽仍无法满足数百 GB/s 到 TB/s 的需求。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：每个 HMC vault 配一个简单 in-order core，只直接访问本地 DRAM partition；远端数据更新通过 message passing 把 computation 移到数据所在 vault。host 负责初始化和分配图对象到 vaults。程序通过 get/put/list_for/barrier 等 API 暴露访问模式，硬件 prefetchers 根据 hint 预取列表和消息目标数据。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：Tesseract 在无 prefetching 时相比 DDR3-OoO 平均提升 9x；LP+MTP 后平均提升 14x。 | Page 8-9, Figure 6 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：论文摘要保守总结为平均系统性能提升 10x、平均能耗降低 87%。 | Page 1-2, Abstract/Contributions | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：Tesseract 使用 HMC internal bandwidth，系统可利用 8 TB/s，总带宽远超 DDR3-OoO 102.4GB/s 和 HMC-OoO/HMC-MC 640GB/s。 | Page 8, Section 4.1/5.1 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：Tesseract 的 average memory access latency 比 DDR3-based system 低 96%。 | Page 8, Figure 7 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：即使 HMC-MC 被理想给予 PIM-level bandwidth，Tesseract 仍快 2.2x，说明 programming model 也同样关键。 | Page 9, Figure 8 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：prefetching schemes 平均覆盖 87% L1 cache misses，性能距离理想 prefetching 仅 1.8%。 | Page 10, Figure 10 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：Tesseract 不支持 virtual memory，以避免 in-memory address translation 开销。 | Page 4, Section 3.1 | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：程序需要使用 Tesseract API/编程模型，迁移已有 graph frameworks 有开发成本。 | 推断，基于 Section 3.4 | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
