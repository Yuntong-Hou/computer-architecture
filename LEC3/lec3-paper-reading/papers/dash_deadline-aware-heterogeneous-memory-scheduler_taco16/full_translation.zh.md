# Full Chinese Translation

## Title

原文标题：DASH: Deadline-Aware High-Performance Memory Scheduler for Heterogeneous Systems with Hardware Accelerators

中文标题：DASH：面向含硬件加速器异构系统的 deadline-aware 高性能内存调度器

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖动机、三条设计原则、DASH 调度机制、实验结果和硬件工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

现代 SoC 中，CPU cores、GPU 和专用 hardware accelerators（HWAs）共享 DRAM。HWA 常用于图像、视频、信号处理等 frame-based workloads，具有明确 deadline；CPU 应用则追求高吞吐和低 slowdown。传统 memory scheduler 难以同时满足 HWA deadlines 和 CPU performance：若总是优先 HWA，会伤害 CPU；若偏向 CPU，HWA 可能错过 frame deadline。

本文提出 DASH，一种 deadline-aware high-performance memory scheduler。DASH 根据每个 HWA 的 period、deadline、remaining requests 和 progress 判断其是否 on track。当 HWA 可能错过 deadline 时，DASH 分散地提高其 memory request priority，而不是等到 deadline 临近再集中抢占。同时，DASH 区分 CPU 应用的 memory intensity，优先从 memory-intensive apps 处让出带宽，保护 memory-nonintensive apps。实验显示 DASH 在 80 个 workloads 上达到 100% deadline-met ratio，并比最佳先前 scheduler 提升 9.5% CPU performance。

## 1. Introduction / 引言

### 原文位置
Page 1-3 / Section 1

### 中文翻译

异构 SoC 越来越依赖专用加速器。HWA 可用较低功耗执行特定任务，但它们通常不是独占内存系统，而是与 CPU/GPU 共享 DRAM。共享会产生 memory interference：HWA 需要在 deadline 前完成固定数量 memory requests；CPU 应用则可能因 HWA 抢占而 slowdown。

简单策略存在明显缺陷。CPU-friendly scheduler 提升 CPU 吞吐，但 HWA 可能错过 deadline。HWA-friendly scheduler 可提高 deadline-met ratio，却可能让 CPU 长期饥饿或性能下降。传统 FRFCFS 优先 row-buffer hits 和 old requests，不理解 HWA deadline，因此无法处理实时约束。

DASH 的目标是在满足 HWA/GPU deadlines 的同时最大化 CPU performance。作者强调，正确策略不是“总给 HWA 高优先级”，而是“只在 HWA 需要帮助时提高优先级，并且从对系统吞吐伤害最小的 CPU 应用那里借资源”。

从硬件工程视角看，这篇文章直接对应真实 SoC QoS 问题。视频/display/camera/ISP/NPU/DLA 等模块常有 frame deadline，CPU/GPU 又共享 LPDDR/HBM/DDR。Memory controller 必须理解 deadline、burstiness 和 application sensitivity，否则单靠固定 priority 很难稳定。

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 3-5 / Motivation, Figure 3

### 中文翻译

论文用 timeline 示例说明 HWA deadline miss 的原因。HWA 在每个 period 内需要完成一定数量 memory requests。如果前期没有获得足够服务，后期即使提高优先级也可能来不及，因为 memory bandwidth 有物理上限。相反，如果从一开始就给 HWA 过高优先级，CPU performance 会被不必要地牺牲。

作者指出，HWA 调度应是 distributed priority，而不是 last-moment panic priority。也就是说，一旦检测到 HWA progress 落后，就应在整个 period 中分散地给予优先服务，使其平滑追赶 deadline。

第二个动机是 CPU 应用并非同等敏感。Memory-intensive apps 本身频繁访问内存，给它们稍微增加延迟对整体性能的边际影响可能低于影响 memory-nonintensive apps。Memory-nonintensive apps 通常对少量 miss 延迟更敏感，因为它们大部分时间不访问内存，一旦 miss 被拖慢，可能直接影响 IPC。因此当 HWA 需要带宽时，DASH 优先压制 memory-intensive CPU apps。

## 3. DASH Design Principles / DASH 设计原则

### 原文位置
Page 5-9 / Section 4

### 中文翻译

DASH 建立在三条设计原则上。

第一，deadline-aware priority。Scheduler 必须判断每个 HWA 是否 on track。它根据 HWA period、deadline、已完成 requests、remaining requests 和当前时间计算所需服务速率。如果 HWA 落后，就提高其请求优先级。

第二，distributed priority。DASH 不等到 deadline 临近才集中提高优先级，而是在 period 内尽早、分散地调整。这样可以避免临近 deadline 时长时间阻塞 CPU，也能降低 HWA deadline miss 风险。

第三，application-aware priority。当 HWA 需要优先时，DASH 不平均伤害所有 CPU 应用，而是根据 memory intensity 选择更适合被降低优先级的应用。它保护 memory-nonintensive/latency-sensitive apps，减少整体 weighted speedup 损失。

论文还讨论短 deadline HWA。对于 deadline 很短的 HWA，进度采样和动态判断可能来不及发挥作用，因此 DASH 使用 worst-case memory access time 做更保守估计，确保短周期任务不因估计误差错过 deadline。

## 4. DASH Scheduling Mechanism / 调度机制

### 原文位置
Page 8-12 / Scheduler details

### 中文翻译

DASH memory controller 需要维护每个 HWA 的状态：period、deadline、request demand、served requests、remaining requests 和 progress。Scheduler 周期性判断 HWA 是否满足预期进度。如果 remaining time 内按正常服务速率无法完成 remaining requests，HWA 被标记为需要高优先级。

当多个请求竞争 DRAM 时，DASH 在传统 FRFCFS 的 row-buffer locality 和 age 规则之外加入 HWA deadline priority 与 CPU application awareness。若 HWA on track，scheduler 不必给它额外优先级；若 HWA lagging，则其请求优先级提升。对于 CPU 请求，DASH 根据 memory intensity 调整优先级，使 memory-nonintensive apps 不被过度阻塞。

这种调度策略的本质是把 memory controller 从“局部队列优化器”提升为“系统级 deadline/QoS 仲裁器”。它仍然需要尊重 DRAM timing、bank conflicts 和 row hits，但目标函数不再只是 row-buffer hit rate 或平均延迟，而是 deadline-met ratio 与 CPU performance 的组合。

## 5. Methodology / 实验方法

### 原文位置
Page 12-15 / Evaluation setup

### 中文翻译

作者构建多核 CPU + HWA/GPU 共享 DRAM 的模拟环境。HWA workloads 包括 Sobel、TPACF、Debayer、DMR 等具有 frame deadlines 的加速器任务，也评估 CPU-GPU-HWA 场景。CPU workloads 使用多个应用组合，形成 80 个 workloads。

比较对象包括 FRFCFS、CPU-friendly scheduler、HWA-friendly scheduler、FRFCFS-Dyn、FRFCFS-DynOpt 和 DASH。评价指标包括 CPU weighted speedup、system performance、maximum slowdown、deadline-met ratio 和 frame rate。

这样的实验设计覆盖了关键 tradeoff：只看 CPU speedup 会忽略 HWA deadline；只看 deadline-met ratio 又会掩盖 CPU 被过度牺牲。DASH 必须在两个指标上同时表现好。

## 6. Main Results / 主要结果

### 原文位置
Page 15-17 / Figure 5, Table V

### 中文翻译

Figure 5 显示，在 80 个 workloads 上，DASH 能保持 100% deadline-met ratio，同时提高 CPU performance。相较最佳先前 scheduler，DASH 的 CPU performance 提升约 9.5%。Table V 进一步显示，DASH 的 deadline-met ratio/frame rate 与能满足 deadline 的动态调度相当，但 CPU 性能更好。

动机部分也展示了 HWA-friendly scheduler 的局限：它可接近 100% deadline-met ratio，但 CPU performance 比 CPU-friendly scheduler 低约 12%。DASH 的收益来自避免不必要的 HWA 优先级，并在必须优先 HWA 时更聪明地选择被影响的 CPU 应用。

这些结果支持论文主张：deadline-aware 与 application-aware 必须结合。只知道 HWA deadline 不够，因为会过度压制 CPU；只知道 CPU memory intensity 也不够，因为会错过实时约束。

## 7. CPU-GPU-HWA Scenario / CPU-GPU-HWA 场景

### 原文位置
Page 19-21 / Figure 9

### 中文翻译

论文进一步评估 CPU、GPU 和 HWA 同时共享 memory 的场景。GPU 也可能具有 frame-rate 或 throughput 要求，并且请求流通常更 bursty。Figure 9 显示 DASH 在这种更复杂环境下仍能保持 frame rate，并控制 CPU slowdown。

这部分对真实 SoC 特别重要。实际平台中，display、camera、video codec、GPU、NPU 和 CPU 往往同时访问内存。如果 memory controller policy 只为两类 agent 设计，很容易在多 agent 场景中失效。DASH 的 progress-based priority 为扩展到多 HWA/GPU 提供了思路。

## 8. Hardware Cost and Practicality / 硬件成本与实用性

### 原文位置
Page 17-19 / Implementation discussion

### 中文翻译

DASH 需要额外硬件状态和调度逻辑，包括每个 HWA 的 deadline/period/remaining request tracking、CPU memory intensity classification、priority decision logic 等。相比 FRFCFS，复杂度更高，但这些结构主要是计数器、比较器和少量状态机，不需要大容量存储。

部署难点在于系统如何提供 HWA demand 信息。某些 HWA 的每 frame memory request 数量可静态估计；某些 workload 可能输入相关，需要 runtime profiling 或 driver 提供 metadata。短 deadline 场景还需要 worst-case memory access time 估计，这要求 conservative bound 足够准确。

从验证角度，DASH 的正确性不应依赖完美估计。若估计错误，系统可能损失性能或错过 deadline，因此产品实现需要 guardband、telemetry 和 fallback priority mode。

## 9. Limitations / 局限性

### 原文位置
Page 21-22 / Discussion and conclusion

### 中文翻译

DASH 假设系统能获得或估计 HWA 的 deadline、period 和 memory request demand。对于固定功能视频/图像加速器，这通常可行；对于高度数据相关或可变控制流的 accelerator，估计更困难。

论文主要面向 soft real-time frame deadlines，而不是严格 hard real-time formal guarantee。真实安全关键系统还需要 worst-case execution time、memory interference bound 和形式化验证。

此外，实验基于模拟平台。真实 memory controller 中还存在 power-down、refresh、thermal throttling、DRAM timing corner、QoS register interface 和 firmware policy 等因素，可能影响实际收益。

## 10. Conclusion / 结论

### 原文位置
Page 22 / Conclusion

### 中文翻译

DASH 证明，在异构 SoC 中，memory scheduler 应同时理解 HWA deadline 和 CPU application sensitivity。通过 distributed priority、application-aware interference control 和短 deadline 保守处理，DASH 能在满足 HWA/GPU deadlines 的同时提高 CPU performance。

## 硬件工程师学习提炼

1. DASH 是 SoC memory QoS 的实用模板：deadline tracking、agent progress、CPU sensitivity、DRAM locality 必须共同进入仲裁逻辑。
2. 设计 HWA 接口时，应让 driver/firmware 能向 memory controller 暴露 period、deadline 和 request demand，否则硬件调度器无法做准确决策。
3. Fixed priority 在复杂异构系统中通常不够；progress-based priority 更适合多媒体、AI、GPU 和 CPU 共享内存场景。
4. 复习优先看 Figure 3 的动机 timeline、Section 4 的三条原则、Figure 5/Table V 的主结果，以及 Figure 9 的 CPU-GPU-HWA 场景。
