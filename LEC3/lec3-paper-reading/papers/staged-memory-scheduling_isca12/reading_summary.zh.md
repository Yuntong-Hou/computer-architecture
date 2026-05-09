# 中文阅读摘要

## 1. 一句话总结
SMS 把传统 memory controller 中 row-locality detection、inter-application priority 和 low-level DRAM command scheduling 拆成三阶段，用更简单硬件在 CPU-GPU 共享内存场景下提升 CPU 性能和公平性，同时控制 GPU frame rate 损失。

## 2. 研究背景
集成 GPU 会产生远高于 CPU 的 memory traffic，占据 memory controller request buffer，降低 controller 对 CPU requests 的可见性；已有 ATLAS/TCM/PAR-BS 等应用感知调度在 CPU-only 场景有效，但要在 CPU-GPU 场景保持全局可见性需要很大且复杂的集中式 request buffer。

## 3. 核心问题
- GPU 高强度 memory traffic 为什么会破坏 CPU application-aware scheduling？
- 能否用分布式小 FIFO 代替大型集中式 CAM/request buffer？
- 如何同时捕获 row-buffer locality、提高公平性、控制 GPU frame rate？
- SJF probability p 如何在 CPU 与 GPU 优先级之间调节？
- SMS 的面积/功耗复杂度相比 FR-FCFS 如何？

## 4. 核心贡献
- 指出 integrated CPU-GPU systems 中 GPU traffic 对传统 memory scheduling 的 visibility 和 complexity 挑战。
- 提出三阶段 Staged Memory Scheduler：batch formation、batch scheduling、DRAM command scheduling。
- 使用 per-source FIFO 和 per-bank FIFO 组成低复杂度结构，避免大型集中式 request buffer。
- 引入可配置 SJF probability p，让系统软件按场景偏向 CPU 或 GPU。
- 在 105 个 workload 上证明 SMS 提升 CPU/system performance 与 fairness，并减少硬件面积/漏电。

## 5. 方法概述
第一阶段按 source/application 将同 row requests 组合成 batches，捕获 row-buffer locality；第二阶段在 batches 之间按 SJF/round-robin 等高层策略调度，处理 application-level fairness/performance；第三阶段 per-bank FIFO 只负责按顺序发 DRAM commands 并满足 timing constraints。

## 6. 实验设计
模拟 16-core CPU + 1 GPU、DDR3-1600、四个 memory controllers，并比较 FR-FCFS、ATLAS、TCM、CFR-FCFS、CTCM、SMS0/SMS0.9；指标包括 CPU weighted speedup、GPU frame rate、CGWS、unfairness、面积和 leakage。

## 7. 主要结果
- SMS0.9 平均 CPU performance 比 ATLAS/TCM 分别提升 22.1%/35.7%。（Page 8, Figure 5）
- SMS0.9 相比 ATLAS/TCM 平均降低 GPU frame rate 18.1%/26.7%，但大多数 workload categories 仍保持 >30 FPS。（Page 8, Figure 5 discussion）
- GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 system performance 46.4%/17.2%/25.7%。（Page 9, Figure 7）
- GPUweight=1 时，SMS0.9 相比 FR-FCFS/ATLAS/TCM 分别提升 fairness 244.6%/47.6%/205.7%。（Page 9, Figure 7）
- GPUweight=1000 时，SMS0 相比 FR-FCFS/ATLAS/TCM 分别提升 1.6%/32.7%/16.4% CGWS。（Page 10, Figure 8）
- SMS 在不同 CPU core counts 和 memory channel counts 下持续提升 CPU performance/fairness，并通常保持可接受 GPU frame rate。（Page 10, Figures 9-10）
- 300 request buffers 系统中，SMS leakage power 比 FR-FCFS 低 66.7%，area 低 46.3%。（Page 11, Table 5）

## 8. 关键结论
SMS 的结论是：异构 CPU-GPU memory scheduling 不应靠更大的集中式 buffer 硬撑全局复杂调度；把功能分层后，硬件更简单、可扩展，并能用一个配置参数在 CPU/GPU 需求之间折中。

## 9. 局限性
作者明确或设计中直接体现的局限：
- SMS0.9 会降低 GPU frame rate，某些类别如 HM 可能低于 30 FPS，需要调整 p。（Page 8, Figure 5 discussion）
- CPU-only 场景中 SMS 相比 ATLAS/TCM 牺牲少量 performance，换取 fairness 和低复杂度。（Page 11, Section 6.6）

我基于论文范围推断的潜在问题：
- SMS 评估基于 2012 年 GPU/DDR3 模型，现代 integrated GPU、HBM/LPDDR 和 QoS requirements 需重新验证。（推断，基于 Section 5 setup）
- p 的动态选择需要系统软件或 ISA 支持，论文主要展示可调性而非完整 runtime policy。（推断，基于 Page 9 footnote and Section 6.2）

## 10. 适合我重点关注的内容
重点读 Figure 1 visibility、Figure 4 SMS organization、Equations 1-4 metrics、Figures 5-10 性能/公平性、Table 5 复杂度。

## 11. 和其他文献的关系
SMS 与 RLMC、MISE、DASH、ASM 等 memory scheduling 论文形成对比：SMS 的核心不是预测/学习，而是结构性拆分 controller 任务来降低复杂度并处理 GPU traffic。
