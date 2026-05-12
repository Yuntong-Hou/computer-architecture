# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 在端子数受限、芯片不可修复、需要少数模块类型的 LSI 背景下，如何组织有用的数字电路模块。 | Page 1-2 / Introduction | 论文写在大规模集成电路兴起时期，核心问题是“芯片上应该放什么样的大而有用的网络”，见 Page 1, Section I。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 作者认为二维重复 cell 阵列能带来功能灵活、可测试、可容错、易互连等优势，是 customized arrays 的替代方案，见 Page 1-3, Section II。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | CLIM 基本形式是二维矩形 identical cells，每个 cell 包含简单 logic-and-storage circuit，并主要连接相邻 cells，见 Page 2。 | 方法章节 / Page 2 及后续对应 section | CLIM 基本形式是二维矩形 identical cells，每个 cell 包含简单 logic-and-storage circuit，并主要连接相邻 cells，见 Page 2。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | Sorting Array II 用 brick-wall pattern 和 serial comparison/row interchange 实现排序，但灵活性较差，见 Page 8。 | 方法章节后半部分 | Sorting Array II 用 brick-wall pattern 和 serial comparison/row interchange 实现排序，但灵活性较差，见 Page 8。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Sorting Array I 可作为保持 words 有序的 single-address multiword memory，也可作为 CAM、pushdown memory、queue/buffer memory 和 programmable switching array，见 Page 1 与 Page 6-8。 | Evaluation / Results | Sorting Array I 可作为保持 words 有序的 single-address multiword memory，也可作为 CAM、pushdown memory、queue/buffer memory 和 programmable switching array，见 Page 1 与 Page 6-8。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 论文指出 isolated faulty cells 有时可通过重编程或移除行/列绕过，见 Page 2 与 Page 9。 | Evaluation / Results | 论文指出 isolated faulty cells 有时可通过重编程或移除行/列绕过，见 Page 2 与 Page 9。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 系统提出 CLIM arrays 的设计特征：identical cells、local neighbor connections、cell-level storage 和 programmability，见 Page 1-2, Section II。 | Introduction / Contributions | 系统提出 CLIM arrays 的设计特征：identical cells、local neighbor connections、cell-level storage 和 programmability，见 Page 1-2, Section II。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 这是一篇 1969 年概念与工程设计论文，没有现代 benchmark、能耗、面积或系统级定量评估。 | Limitations / Discussion / Future Work | 这是一篇 1969 年概念与工程设计论文，没有现代 benchmark、能耗、面积或系统级定量评估。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | CLIM 的规则二维结构思想如何映射到现代 DRAM subarray 或 SRAM compute-in-memory？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
