# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何让程序员不用手动管理 UPMEM 的数据分布、内存分配和通信。 | Page 1-2 / Introduction | UPMEM 是首个商用 PIM 系统，拥有大量 DPUs，但程序员必须手动划分数据、管理 CPU-DPU/DPU 内存传输、启动 kernel 和收集输出，见 Page 1, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | 这种编程模型要求开发者理解 MRAM/WRAM/IRAM、DPU tasklets 与数据搬移细节，阻碍 PIM 普及，见 Page 1-3。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | 用户用 C/C++ 调用 DaPPA pattern APIs 描述数据转换，DaPPA 负责将 primitive 翻译并并行化到 CPU 和 DPUs，见 Page 2 与 Page 4-7。 | 方法章节 / Page 2 及后续对应 section | 用户用 C/C++ 调用 DaPPA pattern APIs 描述数据转换，DaPPA 负责将 primitive 翻译并并行化到 CPU 和 DPUs，见 Page 2 与 Page 4-7。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | dynamic template-based compilation 先根据 UPMEM application skeleton 生成初始代码，再填充 offset、数据搬移、WRAM/MRAM 参数和 CPU/DPU work partition，见 Page 8-10。 | 方法章节后半部分 | dynamic template-based compilation 先根据 UPMEM application skeleton 生成初始代码，再填充 offset、数据搬移、WRAM/MRAM 参数和 CPU/DPU work partition，见 Page 8-10。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | 相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC，见 Page 11, Table 1。 | Evaluation / Results | 相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC，见 Page 11, Table 1。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | 六个 workload 上，DaPPA 平均达到 PrIM 端到端性能的 2.1x，SEL/UNI 因并行数据回传策略表现尤其好，见 Page 11, Figure 5。 | Evaluation / Results | 六个 workload 上，DaPPA 平均达到 PrIM 端到端性能的 2.1x，SEL/UNI 因并行数据回传策略表现尤其好，见 Page 11, Figure 5。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出首个面向 UPMEM 的 data-parallel pattern-based programming framework，见 Page 2。 | Introduction / Contributions | 提出首个面向 UPMEM 的 data-parallel pattern-based programming framework，见 Page 2。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | 评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。 | Limitations / Discussion / Future Work | 评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | DaPPA 是否能支持需要复杂 inter-DPU communication 的 graph/irregular workload？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
