# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何把 cellular logic-in-memory arrays 嵌入通用计算机系统，而不是仅作为孤立 associative memory 或特殊功能单元。 | Page 1-2 / Introduction | 作者从 1970 年的微电子趋势出发：未来封装成本可能更多由 pins 而非 gates 决定，因此在 memory array 中增加逻辑可能具有经济吸引力，见 Page 1, Introduction。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 论文借鉴 IBM 360/85 cache、Atlas virtual memory 和 Wilkes slave memory，把 logic-in-memory array 嵌入 cache 层，而不是把每个 array 当作孤立功能单元，见 Page 2, Section I-II。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 基础组织是 cache-organized computer：CPU 请求先到 cache，miss 时把主存 sector 调入 cache；如果 cache sector 是 logic-in-memory array，CPU 就能对逻辑增强 sector 发出操作，见 Page 2-3, Figure 1。 | 方法章节 / Page 2 及后续对应 section | 基础组织是 cache-organized computer：CPU 请求先到 cache，miss 时把主存 sector 调入 cache；如果 cache sector 是 logic-in-memory array，CPU 就能对逻辑增强 sector 发出操作，见 Page 2-3, Figure 1。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | program control 可显式 hold/release sectors、提示 sequential data、控制 cache load 方式；bit-slice mode 则让 cache 同时装入许多 words 的同一 bit slice，以支持 mass arithmetic，见 Page 4-5。 | 方法章节后半部分 | program control 可显式 hold/release sectors、提示 sequential data、控制 cache load 方式；bit-slice mode 则让 cache 同时装入许多 words 的同一 bit slice，以支持 mass arithmetic，见 Page 4-5。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | 摘要声称 logic-in-memory computer 由于 high-speed, highly parallel sector operations，指向 orders-of-magnitude performance increase 的新方向，见 Page 1, Abstract。 | Evaluation / Results | 摘要声称 logic-in-memory computer 由于 high-speed, highly parallel sector operations，指向 orders-of-magnitude performance increase 的新方向，见 Page 1, Abstract。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | IBM 360/85 相关模拟显示 cache hit 超过 95%，总性能达到理想高速主存机器的 80%，且 cache 只有主存的几个百分点大小，见 Page 3, Section II。 | Evaluation / Results | IBM 360/85 相关模拟显示 cache hit 超过 95%，总性能达到理想高速主存机器的 80%，且 cache 只有主存的几个百分点大小，见 Page 3, Section II。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出以 logic-enhanced cache memory array 为中心的 logic-in-memory computer 组织，见 Page 1, Abstract 与 Page 3。 | Introduction / Contributions | 提出以 logic-enhanced cache memory array 为中心的 logic-in-memory computer 组织，见 Page 1, Abstract 与 Page 3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。 | Limitations / Discussion / Future Work | 论文没有实现和定量 benchmark，除引用 IBM 360/85 cache 结果外，多数性能主张是概念性推断，见 Page 3-6。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | Stone 的 sector operation 抽象和现代 SIMDRAM/PEI 的 ISA abstraction 有哪些共同点和差异？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
