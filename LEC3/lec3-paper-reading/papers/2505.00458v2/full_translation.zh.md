# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。本文是路线图/观点型文章，不是单一实验论文；翻译按其论证结构展开，覆盖 memory problem、self-managing memory、PNM、PUM、采用路径和硬件工程师视角。保留 memory-centric computing、PIM、PNM、PUM、SMD、RowHammer、RowPress、VRD 等术语。

## Title

原文标题：Memory-Centric Computing: Solving Computing's Memory Problem

中文标题：以内存为中心的计算：解决计算中的内存问题

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

现代计算系统越来越受 memory system 限制。处理器核心、GPU、AI accelerators 的计算能力快速增长，但数据必须在 memory 和 compute units 之间反复移动。对于机器学习、图分析、基因组学、数据库和科学计算等 data-intensive applications，data movement 的能耗和延迟往往超过实际计算本身。

本文主张，processor-centric paradigm 已经无法充分解决 memory problem。系统需要转向 memory-centric computing：让 memory 不再只是被动存储，而是能更自主地管理自身可靠性、安全性和维护操作，并在 memory 附近或 memory 内部执行部分计算。

作者从两条线论证这一观点。第一，memory technology scaling 带来 RowHammer、RowPress、VRD、retention 等可靠性/安全问题，传统由 processor/controller 管理的方式越来越吃力。第二，system/application scaling 使数据搬移成为性能和能耗瓶颈，单纯增强 CPU/GPU 不再高效。文章讨论 self-managing DRAM、processing near memory（PNM）和 processing using memory（PUM），并提出渐进采用路径。

## 1. The Memory Problem / 内存问题

### 原文位置

Page 1 - Page 2

### 中文翻译

计算系统的传统设计把 processor 放在中心。Memory 被视为 passive storage，负责响应 load/store，而管理、调度、纠错、刷新和计算都主要由 processor 或 memory controller 发起。几十年来，系统通过 cache hierarchy、prefetching、out-of-order execution、multithreading、SIMD/GPU 并行性等方式掩盖 memory latency。

但 data-intensive applications 正在改变瓶颈位置。数据集规模增长速度超过片上 cache 容量增长，很多 workload 的 working set 位于 DRAM/HBM/SSD 中。处理器为了得到少量有效计算，必须移动大量数据，消耗能耗、带宽和芯片面积。

作者认为 memory problem 同时存在于 device/circuit 层和 system/application 层。器件层面，DRAM scaling 使 cell 更脆弱；系统层面，data movement 使性能和能耗受限。若继续仅强化 processor-centric design，系统复杂度和成本会持续增加，但收益递减。

## 2. Memory Technology Scaling Problems / 内存技术扩展问题

### 原文位置

Page 2 / Figures 1-2

### 中文翻译

DRAM scaling 降低成本和提高容量，但也导致可靠性问题恶化。RowHammer 是最典型例子：反复激活 aggressor rows 会让邻近 victim rows 出现 bit flips。RowPress 进一步说明 row-open time 也会影响 disturbance。VRD 则显示同一 row 的 read disturbance threshold 会随时间变化。

这些问题让 memory maintenance 更复杂。传统 refresh、ECC、scrubbing 和 RowHammer mitigation 由 controller 统一管理，但 controller 不一定知道 DRAM 内部物理结构、真实阈值和实时状态。随着故障模式更细粒度、更动态，单纯 processor/controller 外部管理会越来越不准确或过度保守。

本文把这些现象作为 memory-centric computing 的一个动机：memory 应该更自主地管理自身状态。不是所有维护动作都应由 processor 发起，也不是所有内部信息都应隐藏到 controller 完全不可见。

## 3. Self-Managing DRAM / 自管理 DRAM

### 原文位置

Page 3 / Figure 3

### 中文翻译

Self-Managing DRAM（SMD）是一类让 DRAM 更主动执行维护操作的思想。DRAM 可以根据内部状态自主执行 refresh、RowHammer mitigation、scrubbing、repair 或 error management。与传统方式相比，SMD 的关键是把“需要维护什么、何时维护、维护哪些区域”更多交给 memory 内部。

文章引用 SMD 框架：当 DRAM 在某个区域执行维护操作时，它可以临时拒绝对该区域的请求，同时其它区域继续服务。这种方式比全 rank 或全 bank 停顿更细粒度，减少维护对正常访问的干扰。

工程意义是，DRAM maintenance 需要从固定周期、全局命令，转向内部状态驱动、局部化和并行化。PRAC/Chronus 也可以看作这条路线的一部分：DRAM 内部计数，controller 通过标准接口协同。

## 4. Processing Near Memory / 近内存处理

### 原文位置

Page 4 - Page 5 / Figures 4-6

### 中文翻译

Processing Near Memory（PNM）把计算单元放在 memory 附近，例如 3D-stacked memory logic layer、HBM base die、near-memory FPGA/ASIC 或 memory-side accelerators。PNM 的目标不是让 DRAM array 自己计算，而是减少数据从 memory 到远端 processor 的移动距离，并利用 memory-side bandwidth。

文章引用 Tesseract、PAPI、CENT 等例子。Tesseract 面向 graph analytics，将计算放近 3D-stacked memory，利用图算法的大量不规则访问靠近数据执行。PAPI 和 CENT 则展示 PNM 对其它数据密集场景，尤其是 LLM inference 的潜力。CENT 被引用为可提升 throughput、cost efficiency 和 tokens per dollar 的代表。

PNM 的适用场景通常具有高 memory intensity、低算术强度、数据访问不规则或跨大量数据执行简单操作。对硬件工程师而言，PNM 的难点在于接口、编程模型、一致性、虚拟内存、cache coherence、安全隔离和热设计。

## 5. Processing Using Memory / 利用内存本体计算

### 原文位置

Page 5 / Figure 7

### 中文翻译

Processing Using Memory（PUM）更进一步，直接利用 memory array 的物理特性执行计算。典型例子包括 RowClone、Ambit、SIMDRAM 和基于 commodity DRAM 多行激活的 bulk bitwise operations。通过特殊 activation 序列，DRAM array 可以执行 copy、AND、OR、NOT、NAND、NOR 或类似 bulk operations。

PUM 的吸引力在于能在数据所在位置执行大规模位级操作，减少数据搬移。它特别适合 bulk bitwise、初始化、拷贝、bitmap、数据库 scan、图算法和某些线性代数/神经网络 primitive。

但 PUM 的工程挑战更强。它可能需要非标准 DRAM command、特殊 timing、厂商支持、错误控制和软件栈暴露。COTS DRAM 上的多行激活实验说明物理上有潜力，但要产品化，需要标准、验证和安全隔离支持。

## 6. Adoption Path / 采用路径

### 原文位置

Page 6 / Adoption discussion

### 中文翻译

作者强调 memory-centric computing 不会一次性替代现有体系。更现实的路径是渐进采用。第一步可能是 self-managing memory 和标准化 maintenance 接口，例如更透明的 RowHammer 防护和更智能 refresh。第二步是在 HBM/3D-stacked memory 逻辑层或 near-memory accelerator 中加入可编程/专用计算。第三步才是更广泛的 PUM 和 memory-native computing。

采用的关键障碍包括软件生态、编程模型、兼容性、虚拟内存、缓存一致性、安全隔离、调试、成本和标准化。任何 memory-centric design 若无法被系统软件、编译器、runtime 和应用使用，就很难产生真实价值。

文章的核心态度是务实：memory-centric computing 不是单一技术，而是一组从小接口变化到架构重构的连续谱。

## 7. Conclusion / 结论

### 原文位置

Page 6 / Conclusion

### 中文翻译

本文认为，计算系统的关键瓶颈已经越来越集中在 memory。Memory scaling 带来可靠性和安全挑战，data-intensive applications 带来数据搬移瓶颈。processor-centric paradigm 继续堆叠复杂度的收益有限。

Memory-centric computing 的方向是让 memory 成为主动组件：能自主管理维护，能在附近或内部计算，能与 processor/system 协同优化。SMD、PNM 和 PUM 是这一方向的三个重要组成。

## 8. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文路线图的工程化解读

### 中文学习笔记

1. 对架构设计：未来内存子系统不是“带宽越高越好”这么简单，而是要考虑维护、计算、可靠性、安全和可编程性。

2. 对硬件实现：HBM base die、CXL memory expander、smart DIMM、near-memory accelerator 都是 memory-centric computing 的潜在落点。

3. 对验证：self-managing memory 会增加状态机和协议复杂度。需要验证 controller 与 memory 内部维护之间的交互。

4. 对软件栈：没有编译器/runtime/API，PIM/PUM 很难被采用。硬件方案必须从一开始考虑编程模型。

5. 对行业：AI 和 HPC 的 memory bandwidth/energy pressure 会推动 HBM-PNM 和 CXL-memory-side compute。RowHammer/VRD 会推动 self-managing reliability。

6. 对个人学习：这篇适合作为 LEC3 总纲。先理解 memory problem，再把 RowHammer、防护、PIM、PUM、genome acceleration 和 reliability profiling 串起来。

## 9. 不确定与需回原文核对

- 本文是观点/综述型文章，引用结果来自不同论文和平台。
- PNM/PUM 的成熟度差异很大，不能把原型结果直接等同于产品可用性。
- 对新近 LLM/HBM3/CXL 生态的具体实现仍需补充阅读。
