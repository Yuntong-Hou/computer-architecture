# Full Chinese Translation

说明：本文件已按“高完整度学习译文”标准重写。它基于本地 PDF 抽取文本和原文结构，尽量完整覆盖论文的背景、方法、系统实现、case studies、实验结果、讨论和结论；为便于学习，长段落被拆成更自然的中文段落，专业术语保留英文。参考文献列表不逐条翻译。请结合 PDF 原文核对图表、代码片段和版式细节。

## Title

原文标题：PiDRAM: A Holistic End-to-end FPGA-based Framework for Processing-in-DRAM

中文标题：PiDRAM：面向 Processing-in-DRAM 的端到端 FPGA 框架

作者：Ataberk Olgun; Juan Gómez Luna; Konstantinos Kanellopoulos; Behzad Salami; Hasan Hassan; Oğuz Ergin; Onur Mutlu

原文位置：Page 1 / Title

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
Processing-using-Memory (PuM) 技术试图利用 memory chip 内部已有结构执行计算，从而降低数据移动开销。近年来，很多研究证明未修改的 commodity DRAM chips 中存在可用于 PuM 的内部行为，例如 RowClone 这类 in-DRAM copy/initialization，以及 D-RaNGe 这类基于 DRAM activation latency failure 的随机数生成。

然而，这些技术要进入真实系统，需要的不只是 DRAM primitive 本身。系统必须能发出非标准或特殊 DRAM command sequence，必须能控制 timing parameters，必须能让软件申请满足物理位置约束的内存，还必须处理 cache coherence 和 OS/supervisor 交互。现有模拟器、测试平台和常规处理器系统往往只能覆盖其中一部分，因此难以端到端评估 commodity DRAM based PuM 技术。

PiDRAM 提出一个 holistic end-to-end FPGA-based framework，在基于 RISC-V 的真实系统中连接未修改 DDR3 DRAM，并提供硬件和软件组件，使研究者可以实现、测试和扩展 PuM techniques。作者用 RowClone 和 D-RaNGe 两个 case studies 展示框架能力，并报告 RowClone 在 copy 和 initialization 上相对 CPU baseline 的显著吞吐提升，D-RaNGe 原型也能在真实 DRAM 上产生随机数。

### 硬件工程师视角
摘要里的关键词是 end-to-end。很多 memory research 卡在“能在芯片里做某件事”，PiDRAM 关心的是“软件如何真正调用这件事”。作为硬件工程师，这篇论文能训练你从 primitive、controller、ISA/API、OS、allocator、coherence 到应用评估的完整链路思考。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者从 PuM 的动机讲起。现代系统中大量能耗和延迟来自 processor 与 memory 之间的数据移动。PuM 试图直接利用 memory device 内部结构执行计算，避免不必要的数据传输。不同于在 memory 附近添加独立逻辑的某些 PIM 方案，commodity DRAM based PuM 更强调利用未修改 DRAM chip 内部已经存在的行为，这使它在硬件成本和部署潜力上很有吸引力。

论文指出，很多 PuM primitive 已经在研究中被提出或演示。例如 RowClone 可以在 DRAM 内部执行 bulk copy 和 bulk initialization；D-RaNGe 可以利用 DRAM cell 在降低 activation latency 时出现的 failure behavior 产生 true random numbers。这些 primitive 表明，真实 DRAM chip 不只是被动存储阵列，也可能被重新解释成可执行特定操作的物理平台。

但作者强调，已有研究通常缺乏端到端系统支持。一个 PuM primitive 要真正运行，需要 memory controller 能发出特定 DRAM commands，可能还要违反或调整 JEDEC timing；操作系统要能分配满足 subarray/bank/row 对齐条件的物理页；cache coherence 必须保证处理器缓存和 DRAM 内部修改结果一致；用户程序需要一个可用 API，而不是直接写低层 DRAM 命令。

现有工具存在空缺。传统 CPU 系统的 memory controller 不允许研究者自由控制 DRAM timing 和 command sequence。很多 simulator 能建模机制，但无法捕捉真实 chip variation。SoftMC 等 FPGA-based testing infrastructure 可以发低层命令，但通常不提供完整 OS、application 和 memory allocation 支持。PiDRAM 的目标就是填补这个空缺：提供一个 flexible、end-to-end、open-source framework，使研究者能在真实未修改 DRAM 芯片上评估 PuM 技术。

作者列出的贡献包括：提出 PiDRAM 框架；在 FPGA-based RISC-V system 中实现 prototype；提供 custom memory controller、PuM Operations Controller (POC)、pumolib、supervisor software 等组件；用 RowClone 展示 data movement primitive 的端到端实现；用 D-RaNGe 展示 security primitive 的端到端实现；并说明扩展到新 PuM case 或新 FPGA board 的代码修改量较小。

### 硬件工程师视角
引言对工作的实际价值很大：你可以把 PiDRAM 看成“把论文 primitive 变成系统实验”的模板。行业里新 memory feature 或 memory-side accelerator 如果没有软件可调用路径，基本无法评估真实价值。PiDRAM 把问题拆成硬件控制、内存分配、coherence 和 API 四类，这个拆法可以迁移到 CXL memory、HBM logic layer、near-memory engine 等系统。

---

## 2. Background / 背景

### 原文位置
Page 3 - Page 4 / Section 2

### 中文翻译
背景部分介绍 DRAM、RowClone、D-RaNGe 和 PuM 系统需要满足的条件。

#### 2.1 DRAM Background

原文位置：Page 3 / Section 2.1 / Figure 1

DRAM chip 由 banks、subarrays、rows、columns、sense amplifiers 和 cells 组成。一次常规访问通常通过 ACTIVATE 打开 row，把数据放入 row buffer；随后 READ 或 WRITE 指定列；最后 PRECHARGE 关闭 row。DRAM timing parameters 约束这些命令之间的时间间隔，例如 tRCD、tRAS、tRP 等。

PuM 技术常常需要在这些 timing 或 command sequence 上做文章。RowClone 依赖连续 ACTIVATE 行为；D-RaNGe 依赖降低 tRCD 后 DRAM access failure 的随机性。因此，一个能研究 PuM 的平台必须能够精确控制 DRAM command 和 timing，而普通商用 memory controller 往往不开放这些能力。

#### RowClone

原文位置：Page 3 - Page 4 / Background

RowClone 是一种在 DRAM 内部执行 bulk copy 和 bulk initialization 的机制。它要求 source row 和 destination row 满足物理位置条件，特别是同一 subarray 内的 fast parallel mode。PiDRAM 选择 RowClone 作为第一个 case study，是因为 RowClone 同时涉及硬件命令、物理地址映射、内存分配和 cache coherence，能充分暴露端到端集成难点。

#### D-RaNGe

原文位置：Page 4 / Background

D-RaNGe 利用 DRAM 在降低 activation latency 时出现的随机 failure behavior 产生 true random numbers。它需要 memory controller 用 reduced tRCD 访问特定 DRAM locations，再收集不稳定读取结果。与 RowClone 不同，D-RaNGe 的核心不是移动数据，而是利用真实芯片的物理随机性，因此更依赖真实 hardware prototype，而不能只用高层模拟替代。

### 硬件工程师视角
这部分要建立一个判断：PuM primitive 的难点往往不是“命令能否发出”这么简单，而是物理地址、timing、芯片差异、OS page allocation 和 cache state 的组合。做硬件系统时，任何一个层次假设错了，实验结果都会失真。

---

## 3. Motivation / 动机

### 原文位置
Page 4 / Section 3

### 中文翻译
作者在动机部分说明为什么需要 PiDRAM。commodity DRAM based PuM 研究面对三个典型缺口。

第一，需要真实 DRAM chip。许多 PuM 机制依赖 analog behavior、timing margin 或 undocumented internal behavior。模拟器可以帮助探索架构趋势，但无法完全反映真实 chips 的 vendor variation、process variation、temperature sensitivity 和 failure distribution。

第二，需要端到端系统。只在 FPGA 上发低层 DRAM command 可以证明某个 primitive 存在，但无法回答应用如何调用它、OS 如何分配内存、cache coherence 如何维护、异常情况如何处理。

第三，需要易扩展平台。PuM 研究快速发展，如果每个新 primitive 都要从头搭 FPGA、memory controller、software stack，研究效率会很低。PiDRAM 试图提供可复用硬件和软件组件，使新 case study 可以以较少代码扩展。

### 硬件工程师视角
这个动机非常贴近工业研发：真实硬件平台的价值不只是“跑得更像产品”，还在于能暴露模拟器看不到的问题。对未来工作来说，如果你要验证 memory subsystem 新特性，最好尽早构建能跑完整软件路径的 prototype，否则很容易高估 primitive 的实际收益。

---

## 4. PiDRAM Framework / PiDRAM 框架

### 原文位置
Page 4 - Page 8 / Section 4 / Figure 2

### 中文翻译
PiDRAM 由硬件组件和软件组件共同构成。Figure 2 是核心架构图，展示 application、pumolib、supervisor software、RISC-V core、custom memory controller、PuM Operations Controller 和 DRAM chip 之间的关系。

#### 4.1 Hardware Components

原文位置：Page 4 - Page 6 / Section 4.1

硬件部分包括 FPGA 上的 RISC-V system、custom memory controller 和 PuM Operations Controller (POC)。普通 load/store 仍由系统正常执行，但当用户程序通过 pumolib 请求 PuM operation 时，POC 会接管并向 memory controller 发出对应 DRAM command sequence。

POC 的定位很关键：它不是直接替代整个 processor，也不是要求用户写 HDL；它作为一个 memory-mapped hardware block，让软件通过寄存器或内存映射接口配置 operation 类型、source/destination 地址、长度等信息。然后 POC 生成底层 PuM command sequence。

custom memory controller 需要支持可配置 timing parameters 和特殊 command sequence。对于 RowClone，它要执行 back-to-back ACTIVATE 等操作；对于 D-RaNGe，它要用 reduced tRCD 读取目标位置并把结果放入 buffer。

#### 4.2 Software Components

原文位置：Page 5 - Page 6 / Section 4.2

软件部分包括 pumolib 和 custom supervisor software。pumolib 向用户程序提供高层 API，例如 copy_row、initialize_row 或 random number generation 相关接口。用户不需要直接关心 DRAM command sequence。

supervisor software 负责更底层的系统支持。RowClone 需要满足对齐和物理位置约束，因此 supervisor 要提供特殊 memory allocation 机制。它还要处理虚拟地址到物理地址、物理地址到 DRAM 地址的映射，并在必要时执行 cache flush 维护 coherence。

#### 4.3 Execution of a PuM Operation

原文位置：Page 6 / Section 4.3

一次 PuM operation 的执行大致包括：用户程序调用 pumolib；pumolib 发起 system call 或 memory-mapped access；supervisor 检查权限、地址和对齐；POC 获得 operation 参数；memory controller 发出 PuM command sequence；DRAM 执行操作；结果返回或留在 memory 中。

这个流程说明 PiDRAM 的核心价值不是某个单独硬件模块，而是把从应用到 DRAM cell 的完整路径打通。

#### 4.4 PuM Operation Library

原文位置：Page 6 - Page 7 / Section 4.4

pumolib 把低层 PuM primitive 封装成可由 C/C++ 程序调用的接口。这样做降低了编程门槛，也使应用开发者可以在不理解 DRAM timing 的情况下评估 PuM operation。

#### 4.5 PiDRAM’s HW & SW Components: Summary

原文位置：Page 7 / Section 4.5

作者总结 PiDRAM 的硬件和软件组件如何协作：硬件提供可控 DRAM command generation 和真实 DRAM access；软件提供 API、memory management、coherence 和 system integration。Table 2 附近还说明 PiDRAM 可以研究多类 PuM techniques，而不只是 RowClone/D-RaNGe。

#### 4.6 PiDRAM Prototype

原文位置：Page 7 - Page 8 / Section 4.6

prototype 基于 FPGA RISC-V 系统和 commodity DDR3 DRAM。作者强调使用真实未修改 DRAM chip，这使 PiDRAM 能观察真实硬件行为。另一方面，prototype 的 CPU 性能、内存频率和系统规模不能直接代表商用 server 平台，因此实验结果更适合作为机制验证和趋势分析，而不是最终产品性能预测。

### 硬件工程师视角
Section 4 可以提炼成一个系统原型设计方法：用 POC 隔离 PuM operation generation，用 library 隔离用户 API，用 supervisor 隔离物理地址和 coherence，用 custom controller 隔离 DRAM timing。这个分层值得学习，因为它让新 primitive 可以复用大部分基础设施。

---

## 5. Case Study #1: End-to-end RowClone / 案例 1：端到端 RowClone

### 原文位置
Page 8 - Page 13 / Section 5 / Figures 8-11

### 中文翻译
RowClone case study 是 PiDRAM 最重要的系统验证。RowClone 的目标是在 DRAM 内部快速复制或初始化整行数据。它理论上可以大幅减少数据移动，但要端到端可用，需要解决 memory allocation、address mapping、cache coherence 和 operation invocation。

#### 5.1 Implementation Challenges

原文位置：Page 8 / Section 5.1

RowClone 对物理位置有严格要求。fast parallel mode 通常要求 source 和 destination 位于同一 subarray。普通操作系统分配物理页时不会考虑 DRAM subarray，因此 PiDRAM 必须提供特殊分配机制。另一个挑战是 cache coherence：如果 CPU cache 中有 dirty cache block，而 RowClone 在 DRAM 内部直接复制旧数据，就会产生错误结果。

#### 5.2 Memory Allocation Mechanism

原文位置：Page 8 - Page 10 / Section 5.2 / Figure 8

PiDRAM 提供 memory allocation API，使用户能够申请满足 RowClone 对齐和位置约束的内存区域。Figure 8 展示 physical address 到 DRAM address 的映射关系。系统需要知道哪些物理地址落在同一 DRAM subarray，才能保证 RowClone operation 合法。

这部分的工程意义很大：很多 memory-side operation 在论文中看起来像“对两个地址执行 copy”，但实际上这两个地址必须映射到特定 bank/subarray/row 关系。没有 allocator 支持，primitive 很难被普通应用稳定使用。

#### 5.3 Maintaining Memory Coherence

原文位置：Page 10 - Page 11 / Section 5.3

PiDRAM 通过 cache flush 维护 coherence。执行 RowClone 前，系统需要确保相关 cache blocks 已经从 CPU cache 写回 DRAM，避免 DRAM 内部操作使用 stale data。执行后，也要避免 cache 中残留旧结果。

作者特别评估了 dirty cache block 比例对收益的影响。dirty blocks 越多，flush 开销越大，RowClone 的端到端收益越低。这说明 coherence 机制是 PuM 技术能否实际加速的重要决定因素。

#### 5.4 RowClone Implementation

原文位置：Page 11 / Section 5.4

RowClone-Copy 和 RowClone-Initialize 被实现为 pumolib API。应用调用接口后，supervisor 完成参数检查和地址处理，POC/memory controller 发出对应命令序列。RowClone-Copy 用于复制数据，RowClone-Initialize 用于快速置零或初始化。

#### 5.5 Evaluation

原文位置：Page 11 - Page 13 / Section 5.5 / Figures 9-11

作者评估 RowClone microbenchmark。Figure 9 展示 bare-metal RowClone 的吞吐提升：RowClone-Copy 相对 CPU-copy 提升 317.5x 到 364.8x，RowClone-Initialize 提升 172.4x 到 182.4x。这个结果反映纯 DRAM 内部 copy/initialize primitive 的潜力。

Figure 10 分析 No Flush RowClone，也就是不计 cache flush 开销时的系统收益。rcc 在 8 KiB 和 8 MiB 上分别提升 58.3x 和 118.5x；rci 分别提升 31.4x 和 88.7x。相比 bare-metal，收益变小，但仍然显著。

Figure 11 加入 CLFLUSH 开销，并改变 dirty cache blocks 的比例。0% dirty 时 rcc/rci 仍有 14.6x/12.6x；50% dirty 时下降到 3.2x/3.9x；100% dirty 时只剩 1.9x/2.3x。这是全篇最重要的端到端警示：coherence 成本会显著削弱 PuM primitive 的理论收益。

#### 5.6 Real Workload Study

原文位置：Page 13 / Section 5.5.6

作者还讨论 RowClone 对真实 workload 的潜在影响，尤其是 memory copy 和 zero allocation。由于 full OS system call 路径在 prototype 中受限，完整 workload study 并不是论文最强部分；但作者用 microbenchmark 和 overhead breakdown 说明端到端收益如何估计。

### 硬件工程师视角
RowClone case study 是非常好的工程学习材料。它告诉你：一个 memory primitive 的产品价值不只取决于 primitive latency，而取决于 allocator 能不能满足位置约束、coherence 能不能低成本处理、应用是否真的有大块 copy/zero、OS 是否能把它放入 hot path。未来你评估 CXL.mem copy engine、HBM-side DMA 或 memory controller acceleration 时，可以直接套用这套问题。

---

## 6. Case Study #2: End-to-end D-RaNGe / 案例 2：端到端 D-RaNGe

### 原文位置
Page 13 - Page 15 / Section 6

### 中文翻译
D-RaNGe case study 展示 PiDRAM 不只适合数据移动 primitive，也能支持依赖真实 DRAM 物理行为的 security primitive。

#### 6.1 D-RaNGe Implementation

原文位置：Page 13 - Page 14 / Section 6.1

D-RaNGe 通过降低 tRCD 等 timing parameter，在 DRAM activation 尚未完全稳定时读取数据，从而产生 activation-latency failures。这些 failures 具有随机性，可被用于 true random number generation。PiDRAM 的 memory controller 需要支持 reduced-latency access，并把读取结果收集到 random number buffer 中，供软件读取。

实现中，软件通过 pumolib 请求 random numbers；POC 配置 memory controller 访问特定 DRAM rows；DRAM 产生不稳定读取结果；硬件 buffer 收集输出。与 RowClone 相比，D-RaNGe 更依赖真实 DRAM chip 的 analog behavior，因此 PiDRAM 使用真实未修改 DRAM 的能力尤其重要。

#### 6.2 Evaluation and Results

原文位置：Page 14 - Page 15 / Section 6.2

作者报告 D-RaNGe 原型可提供 8.30 Mb/s throughput，并在 220 ns 内产生 4-bit random number。论文也指出当前 D-RaNGe controller 还没有充分优化，因此 latency 未来可能进一步降低。

这个 case study 的重点不是 D-RaNGe 本身性能已经达到产品级 TRNG，而是证明 PiDRAM 可以端到端实现依赖特殊 timing 和真实 chip failure behavior 的 PuM/security primitive。

### 硬件工程师视角
D-RaNGe 对行业的启发是：DRAM 的“失败模式”也可能成为功能。硬件工程里 failure 通常被视为需要 guardband 避免的风险，但安全、PUF、TRNG、approximate computing 等方向会把受控 failure 转换成价值。关键是要能测量、建模和限制风险边界。

---

## 7. Extending PiDRAM / 扩展 PiDRAM

### 原文位置
Page 15 / Section 7

### 中文翻译
作者讨论如何扩展 PiDRAM 到新的 PuM case study 或新的 FPGA board。因为 PiDRAM 已经提供 reusable hardware/software components，集成 RowClone 和 D-RaNGe 只需要相对较少代码修改。论文报告这两个 case studies 合计只需 388 行 Verilog 和 643 行 C++。

扩展新 PuM primitive 时，研究者通常需要新增或修改 POC operation、memory controller command sequence、pumolib API 和 supervisor 支持。如果 primitive 有新的地址约束或 coherence 需求，还要扩展 allocator 和 OS 逻辑。

扩展新 FPGA board 时，主要工作在 board-specific memory interface、clocking、PHY 和 peripheral integration。作者强调 PiDRAM 的模块化设计降低了移植成本。

### 硬件工程师视角
这部分说明平台工程本身也是研究贡献。对硬件团队来说，可扩展 infrastructure 往往比单个 demo 更重要，因为它决定后续实验迭代速度。一个好的 prototype 应该把 board-specific、controller-specific 和 operation-specific 代码隔离开。

---

## 8. Related Work / 相关工作

### 原文位置
Page 15 - Page 16 / Section 8 / Table 4

### 中文翻译
作者把 PiDRAM 与多个方向比较，包括 Processing-in-Memory/PuM architectures、SoftMC、ComputeDRAM、DRAM simulators、FPGA-based test platforms 和 commercial PIM platforms。Table 4 是这一节的核心：它突出 PiDRAM 同时支持真实 DRAM、flexible memory controller、system software、end-to-end application execution 和 open-source extensibility。

SoftMC 能控制真实 DRAM command，但更偏 characterization/testing，不提供完整系统软件路径。ComputeDRAM 研究 off-the-shelf DRAM computation，但不是通用 end-to-end framework。模拟器便于探索大规模设计空间，但缺少真实 chip behavior。商用 PIM 平台可运行应用，但不允许研究者随意修改 DRAM timing 和内部命令。

PiDRAM 的定位因此很清楚：它不是最高性能产品平台，也不是最高保真全系统商用平台，而是面向 commodity DRAM based PuM research 的 flexible end-to-end prototyping framework。

### 硬件工程师视角
相关工作部分适合帮你建立工具谱系：simulator、testing infrastructure、prototype、product platform 各自回答不同问题。行业里经常有人用一个工具回答它不擅长的问题。PiDRAM 的价值在于把真实芯片和系统软件结合起来，但它也不能替代最终产品验证。

---

## 9. Conclusion / 结论

### 原文位置
Page 16 / Section 9

### 中文翻译
论文总结说，commodity DRAM based PuM techniques 有潜力利用现有 DRAM chip 内部结构降低数据移动开销，但缺少能够端到端评估这些技术的系统框架。PiDRAM 提供一个 FPGA-based open-source framework，包含 custom memory controller、POC、pumolib 和 supervisor software，使研究者可以在真实未修改 DRAM 上实现和评估 PuM operation。

RowClone case study 展示 PiDRAM 可以处理数据移动类 primitive 的地址对齐、memory allocation 和 coherence 问题；D-RaNGe case study 展示 PiDRAM 可以支持依赖真实 DRAM timing failure behavior 的 security primitive。实验结果说明，PiDRAM 能在真实系统路径中展示 PuM 的潜力，同时也暴露端到端开销，例如 cache flush 对 RowClone 收益的削弱。

### 最终学习提炼
对硬件工程师而言，PiDRAM 的学习价值主要在：

- 把 PuM primitive 放进完整系统栈，而不是只看 array-level 操作。
- 学会分析 memory allocation 和 DRAM address mapping 对硬件功能的约束。
- 认识 cache coherence 对 memory-side computation 的实际成本。
- 理解真实 DRAM chip characterization 与 simulator 之间的差异。
- 学习如何设计可扩展 FPGA prototype，让后续 primitive 可以复用基础设施。

在行业现状中，PiDRAM 代表的是 prototyping infrastructure 的价值。无论未来是 DDR5/LPDDR/HBM/CXL memory-side compute，真正影响产品路线的都不是单点 primitive，而是端到端可验证、可调用、可维护的系统路径。

---

## References / 参考文献

### 原文位置
Page 16 及以后 / References

### 处理说明
参考文献保留英文原文，不逐条翻译。建议重点追踪 RowClone、D-RaNGe、SoftMC、ComputeDRAM、Processing using Memory 和 FPGA DRAM testing infrastructure 相关引用。
