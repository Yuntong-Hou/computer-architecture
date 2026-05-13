# Full Chinese Translation

## Title

原文标题：The Application Slowdown Model: Quantifying and Controlling the Impact of Inter-Application Interference at Shared Caches and Main Memory

中文标题：Application Slowdown Model：量化并控制共享 cache 与主存处跨应用干扰的影响

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，重点覆盖 slowdown 定义、cache/main-memory interference 建模、ASM-Cache/ASM-QoS、实验和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

多程序共享系统中，应用在 last-level cache 和 main memory 处相互干扰，导致性能下降且难以预测。为了公平性、QoS 和资源管理，系统需要估计每个应用相对于独占运行时被放慢了多少。本文提出 Application Slowdown Model（ASM），用于量化应用在共享 cache 和共享主存干扰下的 slowdown。

ASM 的核心思想是估计应用独占运行时的 cache access rate，并与共享运行时观察到的 access rate 比较。对于 memory interference，论文通过让目标应用短暂获得 high priority 来估计其不受内存排队影响的访问速率；对于 cache interference，论文使用 auxiliary tag store 估计应用独占 cache 时的 miss 行为。实验显示 ASM 的平均 slowdown estimation error 为 9.9%，明显优于先前 FST 模型的 29.4%。作者进一步展示 ASM 可用于 cache partitioning 和 memory bandwidth allocation，提高 fairness 并支持 slowdown guarantee。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section 1

### 中文翻译

现代多核系统中，多个应用共享 last-level cache、memory controller、DRAM banks 和 memory bandwidth。一个应用的性能不仅取决于自己的指令流，也取决于其他应用的 cache footprint、memory intensity 和请求时序。因此，OS 或 runtime 若想提供公平性或 QoS，必须知道每个应用被共享资源干扰放慢了多少。

直接测量 slowdown 很难，因为 slowdown 定义为应用共享运行时间与独占运行时间的比值，而独占运行状态通常无法在生产系统中同时获得。已有方法要么只考虑内存干扰，要么只用粗粒度指标，无法同时捕捉 cache 和 main memory 的影响。

ASM 试图解决这个测量难题。它不要求真正让应用独占运行完整程序，而是通过硬件采样和模型估计应用在独占状态下的 cache access rate。作者认为，cache access rate 是连接 cache/memory 干扰和应用进度的关键指标：如果应用在共享环境中的有效 cache access rate 下降，就代表其执行进度被拖慢。

从硬件工程视角看，ASM 是 QoS 设计的基础论文之一。很多内存调度、cache partition、bandwidth allocation 和 cloud SLA 方案都需要“可在线测量的 slowdown”。没有这个量，调度器只能优化吞吐或局部队列指标，无法判断某个应用是否被不公平地伤害。

## 2. Background and Problem Definition / 背景与问题定义

### 原文位置
Page 2-4 / Sections 2-3

### 中文翻译

论文把 slowdown 定义为 shared execution time 与 alone execution time 的比值。若一个应用独占运行需要 1 秒，共享运行需要 2 秒，则 slowdown 为 2。为了估计 slowdown，作者关注 application progress。对于许多应用，单位时间内完成的 cache accesses 可以近似反映进度，因此 slowdown 可由独占 cache access rate 与共享 cache access rate 的比值估计。

共享环境中的干扰主要来自两处。第一是 main memory interference：多个应用的 memory requests 在 memory controller queue、DRAM bank 和 bus 上排队，造成访问延迟增加。第二是 shared cache interference：其他应用驱逐目标应用的数据，使其 miss rate 增加，进而降低 access rate。

论文指出，单独建模 memory interference 不够，因为 cache interference 会改变应用产生 memory requests 的频率；单独建模 cache interference 也不够，因为 memory queueing 会改变 miss service time。ASM 因此需要同时处理两者。

## 3. Estimating Slowdown from Cache Access Rate / 用 Cache Access Rate 估计 Slowdown

### 原文位置
Page 4-6 / Section 4

### 中文翻译

ASM 的基本公式围绕两个量：CARshared 和 CARalone。CARshared 是应用在当前共享执行中观察到的 cache access rate；CARalone 是估计应用在独占执行时的 cache access rate。应用 slowdown 近似为 CARalone / CARshared。

CARshared 可以通过硬件性能计数器直接测得。难点是 CARalone。作者把 CARalone 的估计拆成两部分：先消除 memory interference 的影响，再消除 cache interference 的影响。为了估计没有 memory interference 时的行为，系统周期性地给目标应用 memory requests high priority，使其请求尽可能不受其他应用排队影响。在这个 high-priority phase 中观察到的 access rate 可用于估计 memory-interference-free progress。

为了估计没有 cache interference 时的行为，ASM 使用 auxiliary tag store。这个结构模拟应用独占使用 cache 时的 tag 状态，从而估计如果没有其他应用驱逐，它会产生多少 cache misses。通过对 shared cache miss behavior 做校正，ASM 得到更接近独占状态的 CARalone。

工程上要注意，high-priority phase 是采样机制，不是长期调度策略。它需要足够短以避免严重扰乱系统，又要足够长以获得稳定估计。Auxiliary tag store 的容量和采样方式也影响 area/power。论文后续提出 sampled auxiliary tag store 来降低开销。

## 4. Modeling Main Memory Interference / 主存干扰建模

### 原文位置
Page 5-7 / Memory interference model

### 中文翻译

主存干扰来自 memory controller 中其他应用请求的排队和 DRAM 内部资源冲突。ASM 通过 high-priority interval 让目标应用暂时优先获得 memory service，近似观察其在没有其他应用 memory interference 时的 cache access rate。这个阶段不消除 cache interference，因为 cache state 仍然共享，但它显著降低 memory queueing 对进度估计的影响。

作者比较了 ASM 与之前的 FST（Fairness via Source Throttling）模型。FST 主要基于 memory stall time 估计 slowdown，但对 cache interference 和应用进度变化处理不足。实验中，ASM 的平均估计误差为 9.9%，FST 为 29.4%，说明 CAR-based 方法更准确。

从硬件实现角度，memory scheduler 必须支持按 application/core 标记请求，并在采样窗口内改变优先级。这类似 QoS class 或 request tagging。关键风险是采样带来的扰动：如果 high-priority phase 过多，系统行为本身会被改变；如果过少，估计噪声会增加。

## 5. Modeling Shared Cache Interference / 共享 Cache 干扰建模

### 原文位置
Page 7-9 / Cache interference model

### 中文翻译

共享 cache 干扰会改变应用的 miss rate。若目标应用独占 cache，它的一些 block 不会被其他应用驱逐；共享运行时这些 block 可能被替换，导致额外 misses。ASM 用 auxiliary tag store 来估计目标应用独占 cache 的 hit/miss 行为。

Auxiliary tag store 不存储数据，只维护 tag 和替换状态，因此开销小于复制完整 cache。为了进一步降低开销，论文讨论采样方式：只为部分 set 或部分访问维护辅助状态，并由此估计整体行为。

该机制的价值在于它把“如果独占 cache 会怎样”变成一个在线可估计问题。对硬件工程师来说，这与 utility-based cache partitioning、shadow tags、set dueling 等思想有相通之处，都是用小型影子结构估计不可直接观察的替代状态。

## 6. Using ASM for Resource Management / 用 ASM 做资源管理

### 原文位置
Page 9-12 / ASM-Cache and ASM-QoS

### 中文翻译

论文不仅提出模型，还展示了两个使用场景。ASM-Cache 用 slowdown estimate 指导 cache partitioning，目标是降低 unfairness。系统根据各应用 slowdown 判断谁受干扰更严重，并调整 cache allocation。实验显示 ASM-Cache 可将 unfairness 降低约 12.5%。

ASM-QoS 用于 slowdown guarantee。系统为应用设定 soft slowdown bound，然后根据 ASM 估计结果调节 memory bandwidth 或优先级，使应用 slowdown 不超过目标。相比只控制 bandwidth 或 miss rate，直接控制 slowdown 更接近用户可感知性能。

这部分对工程工作非常有用。实际 SoC/服务器的 QoS 策略常常被设计成 bandwidth cap、priority level 或 credit 机制，但业务目标往往是 latency/SLA/slowdown。ASM 提供了把低层资源控制映射到高层性能目标的方法。

## 7. Evaluation / 实验评估

### 原文位置
Page 12-16 / Evaluation

### 中文翻译

作者使用 100 个 multiprogrammed workloads，主要来自 SPEC CPU 应用，并加入 database workloads 做额外验证。评价指标包括 slowdown estimation error、fairness、performance 和 QoS target 满足情况。baseline 包括 FST 等先前模型，以及不同资源管理策略。

主要结果如下。ASM 的平均 slowdown estimation error 为 9.9%，而 FST 为 29.4%。在 database workloads 上，ASM 误差约 4%，说明模型不仅适用于 SPEC，也能处理更复杂的服务器类负载。ASM-Cache 相比 baseline 降低 unfairness 约 12.5%。ASM-QoS 能提供 soft slowdown guarantee，使系统更接近以应用体验为中心的资源管理。

实验结果支持作者的核心结论：若能准确估计应用独占进度，就可以更有效地控制共享资源干扰。需要注意的是，实验基于模拟和特定 workload 集合，真实系统中的 phase behavior、OS scheduling、I/O 和 prefetcher 可能带来额外噪声。

## 8. Limitations / 局限性

### 原文位置
Page 16-17 / Discussion

### 中文翻译

ASM 假设 cache access rate 与应用进度高度相关。对许多 CPU workloads 这成立，但对强 I/O、GPU offload、同步密集、spin-wait 或 phase 极短的程序，CAR 可能不是充分指标。High-priority sampling 也可能改变系统行为，特别是在强实时或高 tail-latency 场景中需要谨慎。

Auxiliary tag store 带来硬件开销，并需要处理多级 cache、inclusive/exclusive policy、prefetch 和 coherence interactions。论文已经讨论采样降低开销，但完整产品化还需要验证复杂度和 corner cases。

## 9. Conclusion / 结论

### 原文位置
Page 17 / Conclusion

### 中文翻译

ASM 提供了一种在线估计应用 slowdown 的方法，同时考虑共享 cache 和 main memory interference。通过估计 CARalone 与观察 CARshared，ASM 能比先前方法更准确地量化应用受干扰程度，并可直接用于 cache partitioning 和 QoS 控制。

## 硬件工程师学习提炼

1. 这篇文章是理解 memory QoS 的基础：先要能测 slowdown，才谈得上公平调度。
2. High-priority sampling 与 auxiliary tag store 是两个可复用设计模式，分别用于估计“无 memory interference”和“无 cache interference”的反事实状态。
3. 做 SoC 或服务器 QoS 时，不应只看 bandwidth utilization；应用 slowdown、tail latency 和 fairness 更接近真实目标。
4. 复习优先看 Page 4-9 的模型推导、Page 12-16 的误差结果，以及 ASM-Cache/ASM-QoS 两个使用场景。
