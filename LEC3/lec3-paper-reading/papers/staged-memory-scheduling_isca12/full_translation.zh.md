# Full Chinese Translation

## Title
原文标题：Staged Memory Scheduling: Achieving High Performance and Scalability in Heterogeneous Systems

中文标题：分阶段内存调度：在异构系统中实现高性能与可扩展性

> 说明：本文件基于已下载 PDF 的抽取文本生成中文学习材料。为满足学习完整度，本文件按原文章节展开为高完整度中文译述，覆盖摘要、背景、设计、实验、局限和结论，并加入硬件工程师视角；它不是版权意义上的逐字复刻全文。术语保留 memory controller、request buffer、row-buffer locality、FIFO、batch、FR-FCFS、ATLAS、TCM、CGWS 等英文。

---

## Abstract / 摘要

### 原文位置
Page 1

### 中文翻译
现代 heterogenous systems 中，CPU cores 和 GPU/accelerators 共享同一个 main memory system。GPU 产生大量 memory requests，会严重干扰 CPU requests，并使传统 memory controller 难以观察不同 CPU applications 的行为差异。已有 application-aware memory schedulers 可以改善多核 CPU 系统的性能和公平性，但它们依赖较大的集中式 request buffers 和复杂排序逻辑。在 CPU-GPU 共享内存场景下，这些结构很难扩展。

本文提出 Staged Memory Scheduling（SMS）。SMS 将 memory scheduling 分为三个阶段：batch formation、batch scheduling、DRAM command scheduling。第一阶段捕获 row-buffer locality，第二阶段执行 application-level scheduling policy，第三阶段负责底层 DRAM commands 和 timing constraints。通过这种分解，SMS 用多个简单结构替代复杂的集中式 scheduler，在 heterogeneous workloads 下提高 CPU performance、system performance 和 fairness，同时降低硬件复杂度。

### 硬件工程师视角
SMS 的工程价值在于它不是单纯提出一个新的优先级公式，而是重新划分 memory controller 的硬件职责。它展示了一个重要原则：当 controller 中某个全局 CAM/排序结构不可扩展时，应该考虑把 locality detection、QoS/fairness policy 和 timing scheduling 拆成不同 pipeline stages。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2, Figure 1

### 中文翻译
文章从 integrated CPU-GPU systems 的趋势开始。随着系统把多个 CPU cores、GPU 和其他 accelerators 集成到同一芯片或封装中，所有 agents 都会共享 off-chip DRAM bandwidth。GPU 的 memory-level parallelism 高，能够同时发出大量 memory requests；CPU applications 的 request rate 通常低得多，但 CPU latency sensitivity 更强。因此，GPU traffic 很容易填满 memory controller 的 request buffer。

Figure 1 用一个 visibility example 说明问题。在 CPU-only 场景中，request buffer 可以看到来自不同 CPU cores 的 requests，从而判断哪些 application row locality 高、哪些 latency sensitive、哪些应该被优先服务。但当 GPU requests 大量进入 buffer 时，buffer 中可能几乎全是 GPU requests，CPU requests 被挤出视野。Memory controller 因此无法正确执行 application-aware scheduling。

一种直接方案是增大 request buffer，让 controller 同时看到足够多 CPU 和 GPU requests。但这会带来面积、功耗、时序和复杂排序逻辑问题。传统 schedulers 如 FR-FCFS、ATLAS、TCM 需要在 buffer 中搜索 row hits、排序 requests、维护 per-application ranking。随着 cores、threads 和 GPU traffic 增长，这类集中式复杂结构越来越难实现。

作者的核心观察是：memory scheduler 承担了多个逻辑不同的任务，包括 row-buffer locality detection、application-level priority/fairness、DRAM timing command issue。把这些任务混在一个集中式结构里会导致复杂度爆炸。SMS 通过 staged design 将它们拆开，用更简单的 FIFO 和 batch structure 实现相似甚至更好的效果。

### 硬件工程师视角
这个问题在现代系统里更普遍：CPU、GPU、DLA、NIC、storage DMA、display engine 都可能共享 memory fabric。只做“谁排队靠前”是不够的；controller 或 NoC 必须考虑 request visibility、buffer partition、QoS policy 和 starvation control。SMS 是理解内存 QoS 硬件设计的经典入口。

---

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 2 - Page 4, Figures 2-3

### 中文翻译
论文回顾了 DRAM request scheduling 的基本目标。FR-FCFS 优先服务 row-buffer hits，以提高 row-buffer locality 和 bandwidth utilization；application-aware schedulers 进一步考虑不同 applications 的 memory intensity 和 slowdown，试图提升 fairness 或 system throughput。ATLAS 倾向优先服务短 memory service demand 的线程，TCM 将 applications 分成 latency-sensitive 和 bandwidth-intensive clusters，进行不同策略调度。

这些方法在 CPU-only workloads 中有效，因为 controller 可以看到来自多个 CPU applications 的 requests。但 GPU traffic 会改变 request stream 的组成。GPU usually has many outstanding requests and high memory intensity，buffer 很容易被 GPU requests 占据。这样，controller 即使有 application-aware policy，也因为看不到足够 CPU requests 而无法正确决策。

Figures 2 和 3 分析了代表性 workload 的 memory intensity、row-buffer locality、bank-level parallelism 和不同 scheduling policies 的效果。GPU application 有高 request rate 和高 memory-level parallelism；CPU applications 的 MPKI 和 row-buffer behavior 差异更大。已有 schedulers 面对 GPU flood 时，要么牺牲 CPU performance，要么过度降低 GPU frame rate，要么需要复杂硬件支持。

作者由此提出一个设计目标：memory scheduler 应在 CPU-GPU shared memory system 中保持良好 CPU performance、合理 GPU frame rate、较高 system performance 和 fairness，同时硬件结构要可扩展。SMS 的 staged architecture 正是为这个目标设计。

### 硬件工程师视角
这里应避免一个常见误区：GPU 不只是“带宽需求高的 CPU core”。GPU workload 对 latency 的容忍度、parallelism、frame-rate QoS、buffer occupancy 行为都不同。做 shared memory controller 或 interconnect arbitration 时，不能用单一 priority rule 粗暴处理所有 master。

---

## 3. SMS Design Overview / SMS 设计概述

### 原文位置
Page 4 - Page 6, Figure 4, Table 1

### 中文翻译
SMS 将 memory scheduling 拆成三个阶段。

第一阶段是 batch formation。每个 source/application 有自己的 FIFO。这个阶段从对应 source 的 incoming requests 中寻找同一 row 的 requests，并把它们组合成 batch。一个 batch 代表一组可以利用 row-buffer locality 的 requests。这样，SMS 不需要在一个巨大集中式 buffer 中全局搜索 row hits，而是在每个 source 内局部形成 locality-aware batches。

第二阶段是 batch scheduling。它决定不同 batches 的服务顺序。这个阶段可以执行高层 policy，例如 shortest-job-first（SJF）、round-robin 或混合策略。论文使用 SJF probability p 作为可调参数：以概率 p 选择 shortest batch，以概率 1-p 用 round-robin。较大的 p 倾向优先短 batches，通常有利于 CPU latency-sensitive workloads；较小的 p 让 GPU batches 得到更均衡服务，通常有利于 GPU frame rate。

第三阶段是 DRAM command scheduling。被选中的 batch 进入 per-bank FIFO。低层 scheduler 只需按 FIFO 顺序发出 ACTIVATE、READ/WRITE、PRECHARGE 等 commands，并满足 DRAM timing constraints。因为 row locality 已在第一阶段处理，application priority 已在第二阶段处理，第三阶段无需复杂全局排序。

Figure 4 展示了 SMS 组织方式：per-source FIFOs、batch scheduler、per-bank FIFOs 共同构成 pipeline。Table 1 列出硬件存储开销。相比传统集中式 request buffer，SMS 的每个结构更简单，避免了大 CAM、多维排序和复杂优先级比较。

### 硬件工程师视角
SMS 的设计可以直接映射到硬件实现思维：把“难 timing closure 的全局组合逻辑”变成多个局部 FIFO 加 pipeline stage。现代高频 memory controller 或 NoC scheduler 很怕大规模 associative search。SMS 这种分阶段结构虽然可能牺牲某些全局最优机会，但通常更容易实现、验证和扩展。

---

## 4. Detailed Mechanism / 机制细节

### 原文位置
Page 5 - Page 6

### 中文翻译
Batch formation 的关键是将相同 row 的 requests 聚合。传统 FR-FCFS 需要动态搜索整个 request buffer 中所有 row hits；SMS 则利用每个 source 的 FIFO 顺序，发现同 row requests 后形成 batch。Batch 的大小反映该 source 在该 row 上的局部性，也为 batch scheduler 提供“job size”信息。

Batch scheduler 的核心是可配置 policy。SJF 倾向短 batch，因为短 batch 更快完成，有利于降低一些 latency-sensitive applications 的等待时间；round-robin 则避免某类 source 长期被饿死。SMS 通过概率参数 p 在两者之间平衡。论文中 SMS0 表示 p=0，即纯 round-robin；SMS0.9 表示 p=0.9，即大多数情况下用 SJF，但仍保留 round-robin 成分。

DRAM command scheduling 阶段不再需要理解应用语义。它只处理 bank conflicts、timing constraints 和 command issue。由于 batch 已按 row locality 聚合，进入 per-bank FIFO 的 requests 更容易被顺序执行，减少 row-buffer 反复开关。

作者还讨论了动态调整 p 的可能性。系统可以根据 CPU/GPU performance target、frame rate requirement 或 workload phase 改变 p。如果 GPU frame rate 低于目标，就降低 p 以提高 GPU 服务机会；如果 CPU performance/fairness 更重要，就提高 p。

### 硬件工程师视角
p 参数是一个很重要的工程接口。它把硬件 policy 暴露成一个简单可调旋钮，允许 firmware、OS 或 runtime 根据 workload 调整。实际产品中，类似旋钮常见于 QoS register、priority weight、credit allocation、isochronous traffic control。设计时必须考虑谁来配置、多久调整一次、如何避免振荡。

---

## 5. Methodology / 实验方法

### 原文位置
Page 7 - Page 8, Tables 2-4, Equations 1-4

### 中文翻译
作者使用 cycle-level simulation 评估 SMS。系统配置包括 16-core CPU、integrated GPU、多个 memory controllers 和 DDR3-1600 DRAM。CPU workloads 来自 SPEC CPU2006，GPU workloads 来自图形/通用计算 benchmark。论文构造 105 个 CPU-GPU mixed workloads，覆盖不同 CPU intensity、GPU intensity 和 memory interference 组合。

评估指标包括 CPU weighted speedup、GPU frame rate / GPU speedup、combined CPU-GPU weighted speedup（CGWS）和 unfairness。CPU weighted speedup 将各 CPU application 在 shared system 下的 IPC 与 alone execution IPC 比值相加。GPU speedup 比较 shared system frame rate 与 GPU alone frame rate。CGWS 用 GPUweight 将 GPU performance 纳入系统性能：GPUweight 越大，表示用户或系统越重视 GPU frame rate。Unfairness 用最差 slowdown 衡量不同 agents 之间的性能不均衡。

论文比较多种 baseline，包括 FR-FCFS、ATLAS、TCM、CFR-FCFS、CTCM 以及 SMS0、SMS0.9 等配置。SMS0.9 偏向 CPU performance，SMS0 更保护 GPU throughput。实验还评估不同 CPU core counts、memory channel counts、buffer sizes、p values 和硬件面积/功耗。

### 硬件工程师视角
SMS 的指标设计值得学习。异构系统不能只看总吞吐，也不能只看 GPU FPS 或 CPU IPC。真实产品常常有多个服务等级：CPU interactive latency、GPU frame deadline、accelerator throughput、memory bandwidth cap、thermal/power limit。你读实验时要问：这个指标是否代表目标用户体验？是否隐藏了某类 agent 的严重 slowdown？

---

## 6. Evaluation Results / 实验结果

### 原文位置
Page 8 - Page 11, Figures 5-12, Table 5

### 中文翻译
Figure 5 是主要结果之一，展示 7 类 workload categories、共 105 workloads 上 CPU 和 GPU performance。SMS0.9 平均 CPU performance 比 ATLAS 和 TCM 分别高 22.1% 和 35.7%。这说明在 GPU traffic 很强的情况下，SMS 的 staged design 比传统 application-aware schedulers 更能保护 CPU requests 的可见性和服务质量。

但 SMS0.9 也会降低 GPU frame rate。相比 ATLAS 和 TCM，它平均降低 GPU frame rate 18.1% 和 26.7%。作者指出，大多数 workload categories 中 GPU 仍能保持超过 30 FPS，但 HM 等更高压力类别可能低于这个阈值。因此 SMS0.9 不是唯一最优配置，而是偏 CPU 的配置。

Figure 6 展示不同 p 值下 CPU/GPU tradeoff。随着 p 增大，CPU performance 通常提高，因为 SJF 更频繁服务短 CPU batches；GPU performance 则可能下降，因为 GPU batches 更容易被延后。这个结果验证了 p 是有效的 policy knob。

Figure 7 使用 GPUweight=1 评估 CPU 和 GPU 等权时的 system performance 与 fairness。SMS0.9 相比 FR-FCFS、ATLAS、TCM 分别提升 system performance 46.4%、17.2%、25.7%，并显著改善 fairness。Figure 8 使用 GPUweight=1000，代表非常重视 GPU frame rate 的场景。此时 SMS0 更合适，相比 FR-FCFS、ATLAS、TCM 仍有 CGWS 优势。

Figures 9 和 10 展示 sensitivity：随着 CPU cores 或 memory channels 变化，SMS 仍能保持 CPU performance/fairness 优势，并通常保持可接受 GPU frame rate。Figure 11 和 12 进一步分析 buffer sizes、design parameters 和 CPU-only scenario。CPU-only 场景下，SMS 相比 ATLAS/TCM 可能牺牲少量 performance，但改善 fairness 并降低复杂度。

Table 5 给出硬件面积和 leakage power 对比。在 300 request buffers 的系统中，SMS 的 leakage power 比 FR-FCFS 低 66.7%，area 低 46.3%。这支撑作者的核心论点：SMS 不只是性能更好，也更容易硬件实现。

### 硬件工程师视角
最重要的工程结论是：SMS 用结构性简化换取可扩展性。对硬件团队而言，area/leakage/timing closure/verification complexity 往往和性能一样重要。一个性能略高但需要巨大 CAM 和复杂排序的 scheduler，可能无法在高频内存控制器中落地；一个 staged FIFO design 可能更符合产品实际。

---

## 7. Related Work / 相关工作

### 原文位置
Page 11 - Page 12

### 中文翻译
论文将 SMS 与多类 memory scheduling 工作比较。FR-FCFS 代表传统 row-hit 优先策略，目标是提升 row-buffer locality。PAR-BS、ATLAS、TCM 等 application-aware schedulers 试图改善多核 CPU 系统中不同 applications 的 performance 和 fairness。还有面向 GPU 或 CPU-GPU systems 的调度方案，尝试识别 CPU/GPU request 特征并设置优先级。

SMS 的差异在于，它不只是换一个 priority function，而是改变 scheduler organization。它将 row locality、application priority 和 DRAM command timing 分阶段处理，从而降低硬件复杂度并提升异构系统中的可见性。

### 硬件工程师视角
读相关工作时建议把 SMS 与 MISE、DASH、RLMC、TCM 放在一起比较。MISE/DASH 偏建模和 QoS，RLMC 偏学习式 controller，SMS 偏硬件结构分解。不同论文给出的启发不同：有的告诉你如何决策，有的告诉你如何实现得下。

---

## 8. Conclusion / 结论

### 原文位置
Page 12

### 中文翻译
论文总结说，CPU-GPU heterogeneous systems 对 memory scheduling 提出了新的挑战：GPU traffic 会压低 CPU request visibility，传统 application-aware schedulers 需要复杂且不可扩展的集中式结构。SMS 通过三个阶段分别处理 row-buffer locality、application-level policy 和 DRAM command scheduling，在性能、公平性和硬件复杂度之间取得更好平衡。

SMS 的实验表明，分阶段设计能显著提升 CPU performance、system performance 和 fairness，同时降低 area/leakage。通过 SJF probability p，SMS 还可以在 CPU-oriented 和 GPU-oriented policy 之间切换。

### 硬件工程师复习要点
- Figure 1 是理解问题的入口：GPU traffic 降低 controller visibility。
- Figure 4 是核心设计图：batch formation、batch scheduling、DRAM command scheduling。
- p 是关键可调参数：高 p 偏 CPU，低 p 偏 GPU。
- Figures 5-8 是性能与 tradeoff 证据。
- Table 5 证明 SMS 的硬件复杂度优势。
- 工程上要记住：memory scheduling 的难点不是单个优先级公式，而是可见性、缓冲结构、QoS 目标和 timing closure 的共同约束。
