# Full Chinese Translation

说明：本文件已按“高完整度学习译文”标准重写。它基于本地 PDF 抽取文本和原文结构，尽量完整覆盖论文的问题动机、UPMEM 背景、DaPPA API、Pipeline 编程模型、动态模板编译、DPU memory 管理、非法 pipeline 处理、实验方法、性能结果、相关工作和结论；为便于学习，长段落被拆成更自然的中文段落，专业术语保留英文。参考文献列表不逐条翻译。请结合 PDF 原文核对代码片段和图表。

## Title

原文标题：DaPPA: A Data-Parallel Programming Framework for Processing-in-Memory Architectures

中文标题：DaPPA：面向 Processing-in-Memory 架构的数据并行编程框架

作者：Geraldo F. Oliveira; Alain Kohli; David Novo; Ataberk Olgun; A. Giray Yağlıkçı; Saugata Ghose; Juan Gómez-Luna; Onur Mutlu

原文位置：Page 1 / Title

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
Processing-in-Memory (PIM) architectures 通过把计算移动到 memory 附近或 memory 内部，缓解 processor-memory data movement bottleneck。UPMEM 是首个商用 general-purpose PIM system，提供大量 DRAM-integrated DPUs，可并行处理 memory-resident data。

尽管 UPMEM 提供真实硬件平台，编程仍然复杂。程序员必须手动划分输入数据、管理 CPU 与 DPUs 之间的数据传输、分配 DPU MRAM/WRAM、编写 DPU kernel、启动 DPUs、收集结果，并处理不同 DPU 之间缺乏直接通信的问题。这些细节使 PIM 编程难以普及。

DaPPA 提出一个 data-parallel programming framework，通过 map、filter、reduce、window、group 等 data-parallel pattern primitives，以及 Pipeline dataflow programming interface，让程序员用高层模式表达计算。DaPPA 使用 dynamic template-based compilation 自动生成 UPMEM host code 和 DPU code。评估显示，DaPPA 在真实 UPMEM 系统上显著减少代码量，并在多个 workloads 上达到或超过 hand-tuned baseline 的端到端性能。

### 硬件工程师视角
摘要里的核心不是“又一个编程框架”，而是 PIM 产品化的关键问题：硬件已经存在，但如果软件太难写，硬件价值就很难释放。硬件工程师读这篇时要关注抽象如何映射到真实硬件瓶颈，例如 MRAM/WRAM 容量、CPU-DPU transfer、DPU tasklets 和 lack of inter-DPU communication。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先指出，数据移动是现代系统的重要瓶颈。PIM 希望通过在 memory 附近执行计算来减少数据移动。UPMEM 是一个实际商用 PIM system，它把多个 DPU 放入 DRAM DIMM 中，每个 DPU 有自己的 instruction memory、working memory 和可访问的 MRAM。大量 DPUs 可以并行处理分布在 PIM memory 中的数据。

然而，UPMEM 编程模型复杂。程序员需要写 host-side code 和 DPU-side code。host 负责分配 DPUs、把数据从 host memory 传到 DPU MRAM、启动 DPU kernel、等待执行完成、把结果取回。DPU 端代码还要管理 MRAM 到 WRAM 的显式数据搬移，因为 DPU 直接在 WRAM 上高效计算，而 MRAM 访问更慢。程序员还要决定如何把输入数据分布到多个 DPUs，以及如何合并输出。

这些要求使开发高效 UPMEM 程序需要大量 boilerplate code 和硬件知识。已有 hand-tuned PrIM implementations 性能较好，但代码复杂、移植和维护成本高。SimplePIM 等框架降低了一些难度，但仍有进一步提升空间。DaPPA 的目标是用 data-parallel patterns 抽象常见计算，让程序员关注算法逻辑，而由框架自动处理数据划分、内存管理、代码生成和运行时调度。

作者提出五类 primary data-parallel pattern primitives：map、filter、reduce、window 和 group。它们覆盖许多 PIM-friendly workloads。作者还提出 Pipeline interface，让用户把多个 stage 串成 dataflow。DaPPA 根据 pipeline 和 pattern 信息动态生成 UPMEM code，并处理 CPU/DPU work partition、WRAM/MRAM 参数和数据传输。

论文贡献包括：提出首个面向 UPMEM 的 data-parallel pattern-based programming framework；设计 Pipeline dataflow interface；提出 dynamic template-based compilation；在真实 UPMEM hardware 上评估六个 workloads；展示 DaPPA 相对 hand-tuned PrIM 平均减少 94% LOC，并平均获得 2.1x 端到端性能。

### 硬件工程师视角
引言能帮你建立一个重要认识：PIM 的瓶颈不只是硬件 bandwidth，也包括 programmer productivity。行业里硬件 adoption 往往由软件门槛决定。一个架构如果要求程序员手动管理每个 memory transfer，很难大规模推广；因此硬件团队必须和编译器/runtime 抽象一起设计。

---

## 2. Background / 背景

### 原文位置
Page 2 - Page 4 / Sections 2-3

### 中文翻译
#### UPMEM-enabled System

原文位置：Page 2 - Page 3 / Figure 1

UPMEM 系统由 host CPU、常规 main memory、UPMEM PIM DIMMs 和大量 DPUs 组成。每个 DPU 与一块 MRAM 关联，还包含 WRAM 和 IRAM。MRAM 容量较大，用于存放输入/输出数据；WRAM 较小但访问更快，用于 DPU kernel 的工作集；IRAM 存放 DPU instruction。

host 与 DPUs 之间的数据传输由 UPMEM SDK 管理。程序通常先把数据从 host memory copy 到 DPU MRAM，启动 DPU kernel，DPU 从 MRAM 分块搬到 WRAM 处理，再把结果写回 MRAM，最后 host 把结果从 DPU MRAM copy 回 CPU side。

#### 3.1 The UPMEM Programming Model

原文位置：Page 3 - Page 4 / Section 3.1

UPMEM 程序包含 host code 和 DPU code。host code 使用 SDK 分配 DPUs、加载 DPU binary、拷贝数据、launch kernel、同步并取回结果。DPU code 通常由多个 tasklets 并行执行，但 tasklets 共享有限 WRAM，需要程序员手动分配 buffers 和同步。

UPMEM 缺乏 direct inter-DPU communication。如果一个 workload 需要跨 DPU 合并或 shuffle 数据，通常要通过 host 或 main memory 间接完成。这对 reduce、group、sort、join 等操作有重要影响。

#### Programming Pain Points

原文位置：Page 3 - Page 4

作者强调几个痛点：数据分区繁琐；CPU-DPU/DPU-CPU transfers 需要手写；MRAM/WRAM 搬移容易出错；DPU binary 生成与 host code 协调复杂；不同 workload 都重复大量 boilerplate；优化性能需要理解 DPU memory hierarchy 和 transfer granularity。

### 硬件工程师视角
背景部分最值得硬件工程师关注的是 memory hierarchy mismatch。UPMEM 把计算放到 memory 里，但它内部仍有 MRAM、WRAM、IRAM 和 transfer hierarchy。PIM 不是“数据在内存里就不用搬”，而是把大规模 host-memory movement 转换成更局部的 DPU memory movement。框架价值就在于管理这些新层次。

---

## 4. DaPPA Overview / DaPPA 总览

### 原文位置
Page 4 - Page 5 / Section 4

### 中文翻译
DaPPA 的设计思想是：让用户用 data-parallel patterns 描述计算，由框架生成 UPMEM 所需的 host code 和 DPU code。用户不需要显式管理 DPU allocation、数据切分、MRAM/WRAM transfer 和 kernel launch 的全部细节。

框架包含三个层次。第一是 pattern APIs，提供 map、filter、reduce、window、group 等常见数据并行算子。第二是 Pipeline interface，允许用户把多个 pattern stage 串联。第三是 dynamic template-based compilation，基于预写 skeletons 和用户定义函数生成实际 UPMEM code。

DaPPA 的目标不是隐藏所有性能细节，而是在保持高层表达力的同时，生成接近 hand-tuned implementation 的代码。它尤其关注减少 lines of code、减少重复 boilerplate，并在真实 UPMEM system 上保持或提升端到端 performance。

### 硬件工程师视角
DaPPA 的总览对硬件工作有一个提醒：好的编程模型不是把硬件细节全部掩盖，而是把可机械化的细节交给 runtime/compiler，把影响性能的结构化选择暴露成 pattern。对 PIM，这些选择包括数据分区、stage 顺序、reduce/group 的合并方式和 transfer overlap。

---

## 5. Programming Interface and Implementation / 编程接口与实现

### 原文位置
Page 5 - Page 10 / Section 5

### 中文翻译
#### 5.1 Data-Parallel Pattern APIs

原文位置：Page 5 - Page 6 / Section 5.1

DaPPA 支持五类 primary patterns。

map 对每个输入元素独立应用用户函数，生成输出元素。它适合 vector add、transform、hashing、简单 feature computation 等 embarrassingly parallel tasks。

filter 根据 predicate 保留部分元素。它需要处理输出数量不固定的问题，因此框架要管理 per-DPU output sizes 和最终结果收集。

reduce 把多个元素聚合成一个或多个结果。它通常需要先在 DPU 内局部 reduce，再由 host 或后续 stage 合并全局结果。

window 处理滑动窗口或相邻元素关系，适合 stencil-like 或序列局部计算。它需要管理 partition boundary，因为窗口可能跨 DPU 数据分区。

group 根据 key 或类别组织数据，涉及更复杂的数据移动和合并。由于 UPMEM 缺乏 direct inter-DPU communication，group 类操作常常需要 host-side coordination。

#### 5.2 Pipeline Dataflow Programming Interface

原文位置：Page 6 - Page 8 / Section 5.2

Pipeline 类表示一串 stages。每个 stage 包含一个 pattern、用户定义计算和输入输出描述。用户可以通过 C++ 宏或 API 指定输入类型、输出类型、函数体和 stage 之间的数据依赖。DaPPA 根据 pipeline 顺序生成执行计划。

Pipeline interface 的好处是让多个 patterns 组合起来，而不是每个 operation 都单独启动一次完整 host-DPU transfer。理论上，stage fusion 或 pipeline-aware data movement 可以减少中间数据回传。但实际能否融合受 UPMEM memory capacity、pattern type 和 data dependency 限制。

#### 5.2.1 The Pipeline Class: Implementation

原文位置：Page 6 - Page 8 / Section 5.2.1

Pipeline class 收集每个 stage 的完整元信息，包括 pattern 类型、输入输出类型、用户函数、数据长度、buffer 信息等。DaPPA 使用这些信息生成 host-side orchestration code 和 DPU-side kernel code。

论文中的代码片段展示了如何创建 pipeline、添加 map/reduce 等 stage，并指定 INPUT、OUTPUT、REDUCE_OUT 等参数。相比手写 UPMEM 程序，用户代码更短，且不需要重复写 DPU allocation、copy、launch 和 collect boilerplate。

#### 5.3 Dynamic Template-Based Compilation

原文位置：Page 8 - Page 9 / Section 5.3

DaPPA 使用 dynamic template-based compilation。它预先准备 UPMEM application skeletons，然后根据 pipeline 元信息进行模板替换和代码变换。生成过程包括：选择合适 skeleton；插入用户函数；计算数据 partition；生成 MRAM/WRAM buffer 管理代码；生成 host-DPU transfer code；生成 kernel launch 和 result collection code；最后调用 UPMEM toolchain 编译 DPU binary。

动态模板方法的优势是实现复杂度低、可控性强，并能复用 hand-written optimized skeletons。缺点是编译有运行时开销，且框架灵活性受模板覆盖范围限制。

#### 5.3.1 Managing DPU Memory

原文位置：Page 9 - Page 10 / Section 5.3.1

DPU memory 管理是 DaPPA 实现的关键。框架需要计算 WRAM 参数，决定每个 tasklet 的 buffer 大小、MRAM offset、input/output chunk size 和中间结果位置。由于 WRAM 容量有限，很多数据必须分块从 MRAM 搬到 WRAM 处理。

DaPPA 还要处理 variable-size output，例如 filter 和 group 可能产生不确定数量结果。框架通过 per-DPU metadata、prefix/sizes 和 host-side aggregation 管理这类输出。

#### 5.4 Handling Invalid Pipeline Implementations

原文位置：Page 10 / Section 5.4

某些 pipeline 组合无法高效或正确映射到 UPMEM。例如 stage 间数据依赖可能要求全局同步或跨 DPU 通信；某些 window/group 操作可能需要超出当前 partition 的数据；输出大小可能超过 buffer。DaPPA 需要检测这些 invalid implementations，并给出错误或 fallback。

作者通过这种检查避免用户写出表面合法但硬件上不可执行的 pipeline。

### 硬件工程师视角
Section 5 是把硬件约束转化成编程抽象的核心。UPMEM 的硬件限制包括 WRAM 小、MRAM 慢、DPU 间不互联、host transfer 贵。DaPPA 的每个 API 设计都在回应这些限制。对硬件工程师来说，这说明 ISA/architecture feature 最终需要对应到 compiler/runtime 的可表达模型，否则软件很难稳定利用。

---

## 6. Methodology / 实验方法

### 原文位置
Page 10 - Page 11 / Section 6

### 中文翻译
实验平台为 2-socket Intel Xeon Silver 4110，128GB DDR4-2400，以及 20 个 UPMEM PIM DIMMs，共 160GB PIM-capable memory 和 2560 DPUs。作者在真实 UPMEM hardware 上评估 DaPPA。

评估 workloads 来自 PrIM benchmark，包括 VA、SEL、UNI、RED、GEMV、HST-S 等六个 workloads。这些 workload 覆盖 vector arithmetic、selection/filter、unique/group-like operation、reduction、matrix-vector multiplication 和 histogram 等数据并行模式。

比较对象包括 hand-tuned PrIM implementations 和 SimplePIM。指标包括 source lines of code (LOC)、end-to-end execution time、DPU kernel performance 和 DaPPA runtime overhead。end-to-end time 被拆分为 CPU-DPU transfer、DPU kernel execution 和 DPU-CPU transfer，有助于判断性能瓶颈到底来自计算还是数据移动。

### 硬件工程师视角
实验方法要重点看真实硬件配置和时间分解。PIM 框架如果只报告 kernel time，很容易掩盖 host-DPU transfer 开销。DaPPA 把端到端时间拆开，是评估 PIM 编程框架是否真正有用的必要做法。

---

## 7. Evaluation / 实验结果

### 原文位置
Page 11 - Page 12 / Section 7 / Table 1 / Figures 5-6

### 中文翻译
#### 7.1 Programmability

原文位置：Page 11 / Section 7.1 / Table 1

DaPPA 显著减少代码量。相对 hand-tuned PrIM，DaPPA 平均减少 94% LOC；相对 SimplePIM 进一步减少 59% LOC。这个结果说明 data-parallel pattern 和 Pipeline interface 能有效隐藏 UPMEM boilerplate。

代码量减少不仅是美观问题。更少代码意味着更少手动 memory transfer、offset calculation 和 synchronization bug，也降低维护和迁移成本。

#### 7.2 Performance Analysis

原文位置：Page 11 - Page 12 / Section 7.2 / Figures 5-6

端到端性能方面，DaPPA 在六个 workloads 上平均达到 PrIM 的 2.1x。SEL 和 UNI 表现尤其好，原因包括 DaPPA 对数据回传策略和输出管理做了更有效的并行化。

DPU kernel-only performance 平均为 PrIM 的 1.4x，最高 3.5x。这说明 DaPPA 不只是减少代码量，有时生成的 DPU code 或 memory management 也优于 hand-tuned baseline。但并非所有 workload 都同样受益，性能取决于 pattern、数据分布、transfer 占比和 DPU-side computation intensity。

Figure 5 的时间分解显示，CPU-DPU 和 DPU-CPU transfer 仍然是许多 workload 的重要开销。DaPPA 可以优化和组织这些 transfer，但不能消除 UPMEM hardware 本身的 host-DPU communication cost。

#### 7.3 DaPPA Execution Time Overheads

原文位置：Page 12 / Section 7.3

DaPPA 的 runtime compilation 和模板替换有额外开销。作者报告 skeleton substitution 约 1 ms，DPU binary compilation 约 150 ms，其他操作约 1 到 150 ms。相比 UPMEM SDK 分配 DPUs 的约 1200 ms，以及较长的端到端 workload runtime，这些开销通常较小。

但对短任务、频繁构建 pipeline 或 interactive 场景，这些开销可能不可忽略。实际系统可以通过 caching compiled binaries、复用 pipeline 或 ahead-of-time generation 缓解。

### 硬件工程师视角
实验结果对行业的启发是：编程框架有时还能提升性能，因为它可以系统性优化数据划分和 transfer，而 hand-written code 未必总是最优。硬件工程师不应把 software abstraction 默认看成性能损失；好的 abstraction 可能通过全局信息做出更好的调度。

---

## 8. Related Work / 相关工作

### 原文位置
Page 12 - Page 13 / Section 8

### 中文翻译
作者讨论 PIM architectures、UPMEM programming frameworks、data-parallel programming models、compiler/runtime systems 和 prior UPMEM benchmarks。PrIM 提供 hand-tuned UPMEM implementations，是重要 baseline。SimplePIM 降低 UPMEM 编程难度，但 DaPPA 进一步使用 data-parallel patterns 和 dynamic template-based compilation 减少代码量。

与通用 CPU/GPU data-parallel frameworks 相比，DaPPA 面向 UPMEM 的特殊 memory hierarchy 和 host-DPU transfer 机制。它必须处理 DPU MRAM/WRAM、缺乏 direct inter-DPU communication、DPU binary compilation 和 PIM DIMM 数据分布等问题。

### 硬件工程师视角
相关工作说明 PIM 软件生态还很年轻。GPU 的成功离不开 CUDA、libraries 和 compiler stack；PIM 如果要扩大应用，也需要类似抽象。DaPPA 是这条路线上的一个尝试，虽然目前强绑定 UPMEM。

---

## 9. Conclusion / 结论

### 原文位置
Page 13 / Section 9

### 中文翻译
论文总结说，UPMEM 这样的 real PIM architecture 为减少数据移动提供了硬件基础，但直接编程复杂，阻碍了 PIM adoption。DaPPA 通过 data-parallel pattern APIs、Pipeline dataflow interface 和 dynamic template-based compilation，自动生成 UPMEM host/DPU code，显著降低编程复杂度。

在真实 UPMEM system 上，DaPPA 相对 hand-tuned PrIM 平均减少 94% LOC，并在六个 workloads 上平均获得 2.1x 端到端性能。结果表明，高层编程抽象和自动代码生成可以同时提高生产率和性能。

### 最终学习提炼
对硬件工程师而言，DaPPA 的学习价值主要在：

- 理解 PIM hardware adoption 为什么依赖 programming model。
- 掌握 UPMEM 的 DPU/MRAM/WRAM/IRAM 层次和 host-DPU transfer 瓶颈。
- 学习 data-parallel patterns 如何映射到 PIM execution。
- 关注 end-to-end time，而不是只看 DPU kernel time。
- 思考硬件限制如何反向塑造 compiler/runtime abstraction。

在行业现状中，DaPPA 说明 PIM 的未来不只取决于更强 DPUs 或更高 memory bandwidth，也取决于是否能让软件开发者用可维护方式表达 PIM-friendly computation。对硬件工程师来说，最值得带走的经验是：设计新硬件时要同时设计“别人如何高效使用它”。

---

## References / 参考文献

### 原文位置
References

### 处理说明
参考文献保留英文原文，不逐条翻译。建议重点追踪 UPMEM、PrIM、SimplePIM、PIM programming models、data-parallel programming 和 code generation 相关引用。
