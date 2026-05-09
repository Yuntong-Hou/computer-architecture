# 中文阅读摘要

## 1. 一句话总结
DASH 在 CPU 与 hardware accelerators 共享 DRAM 的 SoC 中，用 deadline-aware 且 application-aware 的内存调度同时满足 HWA deadlines 并提升 CPU performance。

## 2. 研究背景
现代 SoC 中 CPU、GPU 和专用 HWA 共享 DRAM。HWA 往往有 frame deadline，CPU 需要高吞吐；简单优先 HWA 会牺牲 CPU，简单优先 CPU 又会错过 HWA deadline。

## 3. 核心问题
- memory scheduler 如何判断 HWA 是否 on track 满足 deadline？
- 为什么应优先打断 memory-intensive CPU 而保护 memory-nonintensive CPU？
- 短 deadline HWA 是否需要与长 deadline HWA 不同的调度？
- DASH 相比 FRFCFS 和 dynamic threshold scheduler 性能/deadline tradeoff 如何？

## 4. 核心贡献
- 提出 Distributed Priority：HWA 不在进度轨道上时立即分散式提高优先级，而不是临近 deadline 才抢占。
- 提出 application-aware priority：当 HWA 需要优先时，优先压制 memory-intensive CPU apps。
- 针对短 deadline HWA 用 worst-case memory access time 估计保守调度。
- 在 80 个 workloads 上实现 100% deadline-met ratio，同时比最佳先前 scheduler 提升 9.5% CPU performance。

## 5. 方法概述
DASH 监控每个 HWA 的 period、deadline、remaining requests 和 progress，判断其是否 on track。若 HWA 落后，scheduler 提升其请求优先级；同时根据 CPU application memory intensity 区分受影响对象，优先保护 latency-sensitive/memory-nonintensive apps。

## 6. 实验设计
使用多核 CPU + HWA/GPU 共享 DRAM 模拟，比较 FRFCFS、CPU-friendly、HWA-friendly、FRFCFS-Dyn、FRFCFS-DynOpt 与 DASH；指标包括 CPU weighted speedup、system performance、maximum slowdown、deadline-met ratio/frame rate。

## 7. 主要结果
- DASH 比最佳先前 scheduler 提升 9.5% CPU performance，并始终满足所有 HWAs/GPUs 的 deadlines。（Page 1, Abstract; Page 15-17, Figure 5/Table V）
- HWA-friendly scheduler 可接近 100% deadline-met ratio，但 CPU performance 比 CPU-friendly scheduler 低约 12%。（Page 3-4, motivation）
- Figure 5 显示 DASH 在 80 workloads 上兼顾 CPU performance 与 deadline-met ratio。（Page 15-16, Figure 5）
- Table V 显示 DASH 的 deadline-met ratio/frame rate 与能满足 deadline 的动态调度相当，但 CPU 性能更好。（Page 16, Table V）
- CPU-GPU-HWA 场景中 DASH 仍能保持 frame rate，并控制 CPU slowdown。（Page 19-21, Figure 9）

## 8. 关键结论
异构 SoC memory scheduling 的核心不只是给 HWA 高优先级，而是精确知道何时必须优先、该从哪些 CPU 应用处借带宽，以及短 deadline 场景需要怎样保守处理。

## 9. 局限性
作者明确或设计中直接体现的局限：
- DASH 假设 HWA 的 deadline、period 和 memory request demand 可由系统获知或估计。（Page 6-9, design）
- 研究重点是 soft real-time frame deadlines；hard real-time worst-case guarantee 不是本文目标。（Page 4 and Page 8-10）

我基于论文范围推断的潜在问题：
- 真实 SoC 中不同 HWA 的 burstiness、QoS contract 和 memory controller 实现会影响策略迁移。（推断，基于 simulator evaluation）
- DASH 需要额外硬件监控和 scheduler 逻辑，复杂度高于 FRFCFS。（推断，基于 scheduler design）

## 10. 适合我重点关注的内容
重点看 Figure 3 的 timeline 动机、Section 4 的三条设计原则、Figure 5/Table V 的主要结果、Figure 9 的 CPU-GPU-HWA 场景。

## 11. 和其他文献的关系
DASH 与 ASM/MISE 都面向共享内存干扰，但 DASH 的目标是 HWA deadlines + CPU throughput，而 ASM/MISE 更关注应用 slowdown/fairness。
