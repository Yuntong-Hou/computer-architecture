# Full Chinese Translation

## Title

原文标题：MISE: Providing Performance Predictability and Improving Fairness in Shared Main Memory Systems

中文标题：MISE：在共享主存系统中提供性能可预测性并提升公平性

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖 ARSR/SRSR slowdown 模型、highest-priority sampling、MISE-QoS、MISE-Fair、评估和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

多核系统中，多个应用共享 main memory，导致性能下降和不可预测性。系统若要提供 QoS 或公平性，需要知道每个应用相对于独占运行时被主存干扰放慢了多少。MISE 提出一种 memory-interference-induced slowdown estimation 方法，用 request-service-rate 作为应用 memory performance 的代理。

MISE 估计应用独占运行时的 alone-request-service-rate（ARSR），并与 shared-request-service-rate（SRSR）比较。对于非完全 memory-bound 应用，MISE 用 stall fraction 进行修正。基于该估计，作者构建 MISE-QoS，为 application of interest 提供 soft slowdown guarantees；构建 MISE-Fair，最小化 maximum slowdown。实验显示，MISE 在 300 workloads 上平均 slowdown estimation error 为 8.1%，显著优于 STFM 的 29.8%。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section 1

### 中文翻译

共享主存系统的问题不仅是平均吞吐下降，更是单个应用性能不可预测。一个应用在独占运行时可能很快，但与 memory-intensive 应用共跑后可能被 memory queueing、bank conflicts 和 bandwidth contention 严重拖慢。OS、hypervisor 或 runtime 若无法估计 slowdown，就很难提供 SLA、优先级或公平性。

已有 memory schedulers 如 FRFCFS、ATLAS、TCM 和 STFM 尝试改善吞吐或公平性，但要么没有直接估计 slowdown，要么估计误差较大。MISE 的主张是：memory controller 应该能在线估计每个应用的 memory-induced slowdown，并用该信息指导调度。

从硬件工程视角看，MISE 是把 memory controller 从“请求排序器”升级为“性能可观测与控制单元”的代表。它不仅决定哪个 request 先服务，还向系统提供可解释的应用级性能反馈。

## 2. Slowdown Model / Slowdown 模型

### 原文位置
Page 2-5 / Sections 2-4

### 中文翻译

MISE 的核心公式是 slowdown 约等于 ARSR / SRSR。SRSR 是应用在共享环境中实际获得的 request service rate；ARSR 是该应用独占使用 memory system 时可获得的 request service rate。对于 memory-bound 应用，request service rate 与进度高度相关，因此二者比值可近似表示 slowdown。

对于非 memory-bound 应用，应用执行时间不全在等待内存。MISE 引入 stall fraction alpha，表示应用对 memory service 的敏感程度。若应用大部分时间在 compute phase，则 memory interference 对总运行时间影响较小；若应用大部分时间 stall on memory，则 ARSR/SRSR 对 slowdown 的解释力更强。

论文还讨论 bank-level parallelism 和 row-buffer interference。MISE 不显式建模所有 DRAM 内部细节，而是通过 request-service-rate 把这些影响折叠到一个可测指标中。作者观察这种近似足够准确。

## 3. Estimating ARSR / 估计独占服务率

### 原文位置
Page 4-6 / Epoch and interval mechanism

### 中文翻译

ARSR 无法直接观测，因为应用通常与其他应用共跑。MISE 的方法是周期性 highest-priority epochs：在短时间窗口内，memory controller 给某个应用最高优先级，使其请求尽可能不受其他应用干扰。在这个窗口中测得的 service rate 近似该应用独占时的 ARSR。

系统按 interval/epoch 组织采样。Page 6, Table 3 显示，5M cycles interval、10000 cycles epoch 下误差最低约 8.1%。Epoch 太短会噪声大，太长会扰动正常调度；interval 太长会跟不上 phase change，太短又增加采样开销。

工程上，这类采样设计需要解决两个问题。第一，采样本身会改变系统行为，因此必须控制 duty cycle。第二，应用 phase 变化很快时，历史 ARSR 可能过时，需要平衡稳定性和响应速度。

## 4. MISE-QoS / QoS 调度

### 原文位置
Page 7-9 / MISE-QoS, Table 5, Figure 5

### 中文翻译

MISE-QoS 面向 application of interest（AoI）提供 soft slowdown guarantee。系统给 AoI 设置 slowdown bound，memory controller 根据 MISE 估计判断当前资源分配是否足以满足 bound。如果不满足，就提高 AoI 的服务概率或优先级；如果满足，则释放部分资源给其他应用。

论文使用 lottery scheduling 分配带宽。每个应用获得一定 tickets，scheduler 按概率服务请求。MISE 估计结果用于调整 tickets，使 AoI 尽量满足 slowdown bound，同时不完全牺牲其他应用。

实验显示，在 3000 data points 中，MISE-QoS 满足 slowdown bound 80.9%，达到 AlwaysPrioritize 可满足情况的 97.5%；同时正确预测 bound 是否满足的比例为 95.7%。当 bound=10^3 时，MISE-QoS 相比 AlwaysPrioritize 提高 harmonic speedup 12%、weighted speedup 10%，maximum slowdown 降低 13%。

## 5. MISE-Fair / 公平性调度

### 原文位置
Page 9-11 / MISE-Fair, Figure 8

### 中文翻译

MISE-Fair 用 slowdown estimate 最小化 maximum slowdown。公平性的目标不是让每个应用获得同样 bandwidth，而是让最受干扰的应用不被过度放慢。基于 MISE，scheduler 可以判断谁 slowdown 最大，并把资源向它倾斜。

16-core 评估中，MISE-Fair 相对最佳先前机制 STFM 提供 7.2% 更好公平性。这个结果说明，准确 slowdown estimate 比单纯优化 memory throughput 更适合公平调度。

## 6. Evaluation / 实验评估

### 原文位置
Page 5-11 / Evaluation

### 中文翻译

作者使用 cycle-accurate DDR3 simulator 和 SPEC CPU2006 multiprogrammed workloads，评估 4/8/16-core 场景。指标包括 slowdown estimation error、QoS bound satisfaction、harmonic speedup、weighted speedup、maximum slowdown 和 fairness。

核心结果是 MISE 平均 estimation error 8.1%，STFM 为 29.8%。MISE-QoS 在接近 AlwaysPrioritize 的 bound satisfaction 下保留更好系统吞吐。MISE-Fair 在高 core count 下改善公平性。

## 7. Limitations / 局限性

### 原文位置
Page 12 / Conclusion and discussion

### 中文翻译

MISE 主要估计 main memory interference，不处理 shared cache、I/O、NUMA、accelerator 和其他共享资源带来的 slowdown。这也是 ASM 后续扩展 cache interference 的动机。

MISE 依赖 highest-priority sampling，可能影响短 phase 或 real-time workloads。实验集中在 SPEC workloads 和仿真平台，现代服务器、GPU/HBM/CXL 场景需要重新验证。

## 8. Conclusion / 结论

### 原文位置
Page 12 / Conclusion

### 中文翻译

MISE 证明，基于 request-service-rate 的简单模型可以准确估计 memory-induced slowdown，并支撑 QoS 与公平性调度。共享主存系统要实现可预测性能，必须让 memory controller 具备在线性能估计能力。

## 硬件工程师学习提炼

1. MISE 是理解 memory QoS 的入口，ASM 是它的扩展，DASH 是异构 deadline 场景的延伸。
2. 重点回看 ARSR/SRSR 定义、Table 2/3 的误差、Table 5/Figure 5 的 QoS、Figure 8 的公平性。
3. 工程上要关注 sampling 对 workload 的扰动、request tagging、per-application counters 和 scheduler policy 的验证成本。
4. 对未来 HBM/CXL/多租户平台，slowdown telemetry 可能比裸 bandwidth counter 更有价值。
