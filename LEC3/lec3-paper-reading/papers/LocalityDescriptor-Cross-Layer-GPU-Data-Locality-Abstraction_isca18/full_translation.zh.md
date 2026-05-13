# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 Locality Descriptor 的问题动机、descriptor 字段、cache locality、NUMA locality、硬件协同机制、评估、局限和硬件工程师视角。保留 CTA scheduling、cache policy、prefetching、NUMA placement、INTER-THREAD、INTRA-THREAD 等术语。

## Title

原文标题：The Locality Descriptor: A Holistic Cross-Layer Abstraction to Express Data Locality in GPUs

中文标题：Locality Descriptor：在 GPU 中表达数据局部性的整体跨层抽象

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

GPU 编程模型擅长表达大规模并行性，但缺少统一方式表达数据局部性。程序员知道哪些 data structures 被哪些 thread blocks/CTAs 重用，哪些访问没有 reuse，哪些数据应靠近某个 NUMA partition，但硬件通常看不到这些语义。硬件-only 机制只能根据运行时访问推断，容易滞后或误判。

本文提出 Locality Descriptor，让软件以可移植方式描述 data structure、locality type、tile semantics、locality semantics 和 priority。硬件使用这些语义协调 CTA scheduling、cache bypass/prioritization、prefetching 和 NUMA placement。

评估显示，在 reuse-based cache locality 场景，Locality Descriptor 平均提升 26.6%；在 NUMA memory system 场景，平均提升 53.7%，最高 2.8x。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 4

### 中文翻译

GPU 应用往往有丰富局部性，但局部性不一定能被硬件自动推断。例如，某个 data tile 会被一组 CTAs 共享；某些 streaming data 没有 reuse，应 bypass cache；某些 data 与某个 GPU module 更近，应放在对应 NUMA zone。

单独 CTA scheduling 不一定带来性能。论文指出，即使调度让 working set 降低 54.5%，平均性能只提升 3.3%，因为更多 L1 inflight hits 可能让线程一起等待，cache policy 未配合时收益有限。

NUMA locality 也需要协同。只用 first-touch/page placement 对 GPU 细粒度共享不稳定。若 CTA 调度和 data placement 不一致，计算仍会跨 NUMA 访问远端 memory。

## 2. Locality Descriptor Design / Locality Descriptor 设计

### 原文位置

Page 5 - Page 7

### 中文翻译

Locality Descriptor 描述一个 data structure 的地址范围、tile 划分、与 compute tile/CTA 的关系、locality type 和 priority。它可以由程序员、compiler 或 runtime 生成。

Locality types 包括 INTER-THREAD、INTRA-THREAD、NO-REUSE 等。INTER-THREAD 表示多个 threads/CTAs 之间共享数据，应通过调度和 cache policy 保留重用。INTRA-THREAD 表示单线程内部重用。NO-REUSE 表示 streaming data，适合 bypass 或低优先级 cache。

Priority 用于处理多个 descriptors 冲突。若两个 data structures 争用 cache 或 placement resource，硬件可根据 priority 决定哪一个优先优化。

Descriptor 的关键是抽象层次。它不要求程序员指定具体 cache set 或 scheduler algorithm，而是表达可移植语义，让不同硬件实现选择策略。

## 3. Hardware Use of Descriptors / 硬件如何使用 descriptor

### 原文位置

Page 7 - Page 10

### 中文翻译

CTA scheduler 可以利用 descriptor 把共享同一 data tile 的 CTAs 调度到时间/空间上更接近的位置，提高 cache reuse 或 NUMA locality。

Cache controller 可根据 locality type 做 bypass、priority insertion、replacement priority 或 retention policy。NO-REUSE data 可避免污染 cache；INTER-THREAD data 可获得更高保留优先级。

Prefetcher 可以利用 tile semantics 提前加载即将被 CTAs 使用的数据。NUMA placement mechanism 可把 data 放到最可能访问它的 GPU module 附近，降低远端访问。

论文的核心主张是：单一硬件机制不足以利用软件局部性，descriptor 需要驱动多个机制协同。

## 4. Evaluation / 评估

### 原文位置

Page 10 - Page 13 / Section 6

### 中文翻译

作者在 GPGPU-Sim 和 NUMA GPU simulator 中评估 Rodinia、Parboil、PolybenchGPU 等 benchmarks。单芯片系统用于 cache locality，四个 GPU modules/NUMA zones 系统用于 NUMA locality。

Reuse-based cache hierarchy 场景中，Locality Descriptor 平均提升 26.6%，最高 46.6%。NUMA memory system 场景中，平均提升 53.7%，最高 2.8x。

结果说明，跨层语义接口可以显著提高硬件优化质量，尤其在硬件难以自动推断局部性时。

## 5. Discussion and Limitations / 讨论与局限

### 原文位置

Discussion / Limitations

### 中文翻译

Locality Descriptor 需要程序员、compiler 或 runtime 生成准确语义。如果 descriptor 错误，硬件会优化错误方向。高度动态、输入相关或 irregular locality 可能难以静态描述。

真实 GPU 产品中，开放 CTA scheduler、cache policy、NUMA placement 接口有工程和商业难度。Descriptor 还需要 ISA/API/runtime 支持，并与现有 memory consistency、virtual memory 和 security isolation 兼容。

## 6. 硬件工程师视角

这篇论文的价值是 cross-layer contract。硬件通常缺少程序语义，软件通常缺少硬件控制。Descriptor 是中间层：软件表达意图，硬件选择实现。

对 GPU/accelerator 设计，类似思想可用于 cache hints、memory placement hints、prefetch descriptors、DMA scheduling hints、tensor locality metadata。关键是语义必须稳定、可验证，并且错误 hint 不应破坏 correctness，只影响性能。

验证重点包括 descriptor conflict、priority、错误 descriptor fallback、context switch、multi-process isolation、NUMA remap 和 cache policy corner cases。

## 7. 不确定与需回原文核对

- Descriptor 字段定义和 ISA/API encoding 需回原文核对；
- Figures 3-5 的动机案例建议仔细看；
- 性能数据来自模拟器，真实 GPU 产品化需要额外验证。
