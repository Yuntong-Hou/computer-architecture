# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 研究问题：集成 GPU 会产生远高于 CPU 的 memory traffic，占据 memory controller request buffer，降低 controller 对 CPU requests 的可见性；已有 ATLAS/TCM/PAR-BS 等应用感知调度在 CPU-only 场景有效，但要在 CPU-GPU 场景保持全局可见性需要很大且复杂的集中式 request buffer。 | Page 1, Abstract/Introduction | 开头定义问题。 | 高 | 这是全文动机。 |
| 2 | 核心方法：第一阶段按 source/application 将同 row requests 组合成 batches，捕获 row-buffer locality；第二阶段在 batches 之间按 SJF/round-robin 等高层策略调度，处理 application-level fairness/performance；第三阶段 per-bank FIFO 只负责按顺序发 DRAM commands 并满足 timing constraints。 | Method/design sections | 方法章节给出机制。 | 高 | 这是论文主要贡献。 |
| 3 | 关键结果：SMS0.9 平均 CPU performance 比 ATLAS/TCM 分别提升 22.1%/35.7%。 | Page 8, Figure 5 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 4 | 关键结果：SMS0.9 相比 ATLAS/TCM 平均降低 GPU frame rate 18.1%/26.7%，但大多数 workload categories 仍保持 >30 FPS。 | Page 8, Figure 5 discussion | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 5 | 关键结果：GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 system performance 46.4%/17.2%/25.7%。 | Page 9, Figure 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 6 | 关键结果：GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 fairness 244.6%/47.6%/205.7%。 | Page 9, Figure 7 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 7 | 关键结果：GPUweight=1000 时，SMS0 相比 FR-FCFS/ATLAS/TCM 分别提升 1.6%/32.7%/16.4% CGWS。 | Page 10, Figure 8 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 8 | 关键结果：SMS 在不同 CPU core counts 和 memory channel counts 下持续提升 CPU performance/fairness，并通常保持可接受 GPU frame rate。 | Page 10, Figures 9-10 | 原文实验/图表支持。 | 高 | 支撑作者结论。 |
| 9 | 作者局限：SMS0.9 会降低 GPU frame rate，某些类别如 HM 可能低于 30 FPS，需要调整 p。 | Page 8, Figure 5 discussion | 作者明确说明或设计边界。 | 中 | 实现或迁移时要复核。 |
| 10 | 推断局限：SMS 评估基于 2012 年 GPU/DDR3 模型，现代 integrated GPU、HBM/LPDDR 和 QoS requirements 需重新验证。 | 推断，基于 Section 5 setup | 基于论文范围的推断。 | 中 | 后续阅读方向。 |
