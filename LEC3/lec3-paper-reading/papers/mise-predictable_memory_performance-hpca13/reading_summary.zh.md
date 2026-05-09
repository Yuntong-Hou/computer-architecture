# 中文阅读摘要

## 1. 一句话总结
MISE 用 request-service-rate 估计 memory-interference-induced slowdown，并基于该估计构建 MISE-QoS 和 MISE-Fair，实现更好的 QoS 保证和公平性。

## 2. 研究背景
多程序共享主存会导致不同应用 slowdown 不可预测；已有 memory scheduler 常优化吞吐或公平性，但对单个应用相对独占运行的 slowdown 估计不准确，难以给 QoS 或 OS 提供可靠反馈。

## 3. 核心问题
- 如何在线估计应用独占运行时的 request-service-rate？
- request-service-rate 为什么能作为 memory-bound 应用性能代理？
- 非 memory-bound 应用如何加入 compute phase/stall fraction 修正？
- MISE-QoS/MISE-Fair 相对 STFM/ATLAS/TCM 效果如何？

## 4. 核心贡献
- 提出 MISE，用 ARSR/SRSR 估计 slowdown。
- 通过周期性 highest-priority epochs 估计 alone-request-service-rate。
- 用 stall fraction alpha 修正 non-memory-bound applications。
- 构建 MISE-QoS，为 AoI 提供 soft slowdown guarantees。
- 构建 MISE-Fair，最小化 maximum slowdown 并优于 FRFCFS/ATLAS/TCM/STFM。

## 5. 方法概述
MISE 的核心是 slowdown ≈ ARSR/SRSR，并对非 memory-bound 应用乘入 memory stall fraction。memory controller 通过 interval/epoch 机制轮流给应用最高优先级，测量 near-alone request-service-rate，再用 lottery scheduling 分配带宽以满足 QoS 或公平性目标。

## 6. 实验设计
使用 cycle-accurate DDR3 simulator、SPEC CPU2006 组合 workload，评估 slowdown estimation error、epoch/interval sensitivity、single/multiple AoI QoS、4/8/16-core fairness 与 harmonic speedup。

## 7. 主要结果
- MISE 在 300 workloads 上 average slowdown estimation error 为 8.1%，而 STFM 为 29.8%。（Page 5-6, Table 2 and Section 6）
- 5M cycles interval、10000 cycles epoch 下 MISE 达到最低约 8.1% error。（Page 6, Table 3）
- MISE-QoS 在 3000 data points 中满足 slowdown bound 80.9%，达到 AlwaysPrioritize 可满足情况的 97.5%。（Page 8, Table 5 discussion）
- MISE-QoS 正确预测 bound 是否满足的比例为 95.7%。（Page 1-2 and Page 8, Table 5 discussion）
- bound=10^3 时，MISE-QoS 比 AlwaysPrioritize 提高 harmonic speedup 12%、weighted speedup 10%，maximum slowdown 降低 13%。（Page 9, Figure 5）
- 16-core 下 MISE-Fair 相对最佳先前机制 STFM 提供 7.2% 更好公平性。（Page 10-11, Figure 8）

## 8. 关键结论
准确、简单的 slowdown estimation 可作为共享主存 QoS/fairness 的 substrate；memory controller 不只应调度请求，还应向系统暴露可解释的应用级 slowdown 信息。

## 9. 局限性
作者明确或设计中直接体现的局限：
- MISE 主要估计 main memory interference，其他共享资源 slowdown 留作未来工作。（Page 12, Conclusion）
- MISE 不显式建模 bank-level parallelism 或 row-buffer interference，但作者观察其对准确性影响有限。（Page 4, Section 4.3）

我基于论文范围推断的潜在问题：
- highest-priority sampling 会改变短期调度行为，在实时或极短 phase workload 中需重新评估。（推断，基于 epoch/interval design）
- MISE 只在仿真 SPEC workloads 上系统评估，现代 server workloads/NUMA/HBM 需要新验证。（推断，基于 methodology）

## 10. 适合我重点关注的内容
重点读 Section 3 的 ARSR/SRSR 模型、Table 2/3 误差、Table 5/Figure 5 QoS、Figure 8/10 fairness/performance。

## 11. 和其他文献的关系
MISE 是 ASM 的前身，ASM 后续把 cache interference 纳入模型；DASH 则把共享内存调度扩展到 HWA deadline 场景。
