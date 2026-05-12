# Full Chinese Translation

说明：本文件已按“高完整度学习译文”标准重写。它基于本地 PDF 抽取文本和原文结构，尽量完整覆盖论文的问题动机、DRAM/FPGA 背景、DRAM Bender 设计、编程接口、实验 workflow、use cases、相关工作、未来方向和结论；为便于学习，长段落被拆成更自然的中文段落，专业术语保留英文。参考文献列表不逐条翻译。请结合 PDF 原文核对图表、代码片段和实验参数。

## Title

原文标题：DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips

中文标题：DRAM Bender：用于便捷测试先进 DRAM 芯片的可扩展 FPGA 基础设施

作者：Ataberk Olgun; Hasan Hassan; A. Giray Yağlıkçı; Yahya Can Tuğrul; Lois Orosa; Haocong Luo; Minesh Patel; Oğuz Ergin; Onur Mutlu

原文位置：Page 1 / Title

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
理解现代 DRAM chips 的可靠性、安全性和潜在内部功能，必须能够在真实芯片上发出灵活的低层 DRAM command sequence。普通系统的 memory controller 不允许研究者随意控制 ACTIVATE、PRECHARGE、READ、WRITE、refresh、timing parameters 或违反标准时序，因此很难系统研究 RowHammer、retention failure、in-DRAM computation 等现象。

DRAM Bender 提出一个 extensible and versatile FPGA-based infrastructure，目标是让研究者能够容易地测试 state-of-the-art DRAM chips。它提供 nonrestrictive DRAM command interface、C++/Python programming APIs、modular FPGA design、debugging support 和可移植的 board integration。与现有平台相比，DRAM Bender 更强调三点：不限制底层 DRAM interface，易于使用，易于扩展到新 FPGA boards 和 DRAM standards。

作者用多个 use cases 展示 DRAM Bender 的能力，包括 RowHammer interleaving pattern study、RowHammer data pattern study 和 off-the-shelf DDR4 上的 in-DRAM AND/OR/Majority behavior characterization。实验说明 DRAM Bender 能发现以前平台不易观察的现象，并支持用很少 C++ 代码描述复杂 DRAM 实验。

### 硬件工程师视角
摘要里的关键词是 infrastructure。DRAM Bender 不是提出一个单独 DRAM primitive，而是提供“看见真实芯片行为”的工具。硬件工程师在做可靠性、安全或 memory feature 验证时，最缺的往往就是这种能绕过常规 controller 限制、直接控制时序和命令的实验平台。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先指出，随着 DRAM scaling 持续推进，DRAM chips 的可靠性和安全问题变得更复杂。RowHammer、retention failures、read disturbance、timing failures 以及潜在的 undocumented functionality 都需要在真实 DRAM chips 上表征。仅依赖 datasheet 或普通系统测试不足以发现底层行为，因为普通 memory controller 会强制遵守 JEDEC timing，并隐藏 DRAM command-level 细节。

研究者需要能够任意组合 DRAM commands、改变 timing parameters、控制 data patterns、监测 readback results，并且在不同 DRAM modules 和 vendors 上重复实验。现有平台各有不足。SoftMC 是重要基础设施，但在接口灵活性、易用性或可扩展性方面存在限制。LiteX RowHammer Tester 更偏特定 RowHammer 测试，也不完全满足通用 DRAM characterization 需求。

DRAM Bender 的目标是提供一个更通用的平台。它支持低层 DRAM command 编程，同时提供 C++/Python APIs，降低用户写实验的门槛。它采用 modular FPGA design，使不同 FPGA board、DDR3/DDR4 interfaces 和未来扩展更容易接入。作者强调，DRAM Bender 让用户能够以很少代码表达复杂实验，例如 12 行 C++ 写 RowHammer test，3 行 C++ 写 bulk bitwise AND/OR experiment。

论文贡献包括：提出 DRAM Bender infrastructure；设计 nonrestrictive instruction set architecture；提供 C++/Python APIs 和 program debugger；在五种 FPGA boards 上支持 DDR3/DDR4；通过 use cases 发现 RowHammer interleaving、data pattern 和 DDR4 in-DRAM computation 的新观察；并开源平台以促进 DRAM research。

### 硬件工程师视角
引言的行业意义很直接：DRAM 可靠性和安全性已经不只是 memory vendor 内部问题，系统公司、云厂商、CPU/GPU 设计团队都需要能独立表征真实 DIMM 行为。DRAM Bender 这类平台可以帮助硬件工程师建立从 JEDEC 抽象到底层实际行为之间的桥。

---

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 3 - Page 4 / Section 2

### 中文翻译
#### 2.1 DRAM Organization

原文位置：Page 3 / Section 2.1 / Figure 1

DRAM 由 channels、ranks、banks、rows、columns、sense amplifiers 和 cells 构成。memory controller 通过 command/address/data interface 控制 DRAM。常规访问包括 ACTIVATE、READ/WRITE 和 PRECHARGE。理解这些低层命令是编写 DRAM Bender 实验的基础。

#### 2.2 Accessing a DRAM Cell

原文位置：Page 3 / Section 2.2

访问 cell 时，ACTIVATE 打开 wordline，让 cell capacitor 与 bitline 共享电荷；sense amplifier 放大结果并恢复 cell；READ/WRITE 传输列数据；PRECHARGE 关闭 row 并准备下一次访问。很多可靠性问题都与这些模拟步骤有关，例如 activation 不充分、precharge 时间不足或反复激活导致邻近行扰动。

#### 2.3 DRAM Timing Parameters

原文位置：Page 3 - Page 4 / Section 2.3

DRAM timing parameters 规定命令之间必须等待多久。违反这些 timing 可能导致错误，也可能暴露用于研究的物理现象。RowHammer 需要高频反复激活 aggressor rows；retention study 需要控制 refresh interval；in-DRAM computation 可能需要特殊 activation sequence。普通系统不允许随意调整这些参数，因此需要 FPGA-based testing infrastructure。

#### 2.4 DDR PHY Interface (DFI)

原文位置：Page 4 / Section 2.4

DFI 标准定义 memory controller 和 DDR PHY 之间的接口。DRAM Bender 通过理解并接入这一层，使 FPGA logic 能生成低层 DRAM 命令。DFI 层是连接高层实验程序和实际 DRAM pins 的关键桥梁。

#### 2.5 FPGA-based DRAM Testing Infrastructures

原文位置：Page 4 / Section 2.5

现有 FPGA-based platforms 证明了真实 DRAM testing 的价值，但也暴露出难用、命令受限、可移植性不足、扩展新接口困难等问题。DRAM Bender 的设计动机就是同时提升 flexibility、usability 和 extensibility。

#### 2.7 Motivation for DRAM Bender

原文位置：Page 4 / Section 2.7

作者总结需求：研究者需要一个平台，既能完全控制 DRAM command sequence，又不要求每次实验都写大量 HDL；既能支持最新 DRAM chips，又能移植到不同 FPGA boards；既能做 RowHammer，也能做 in-DRAM computation、retention 和其他 characterization。

### 硬件工程师视角
背景部分可以帮助你区分两个层次：JEDEC-visible behavior 和 chip-internal behavior。硬件工程中很多 bug 或安全问题恰恰发生在标准抽象没有覆盖的边界。能控制 DFI/PHY 附近接口，就能把研究从“系统观察”推进到“物理机制定位”。

---

## 3. DRAM Bender Design / DRAM Bender 设计

### 原文位置
Page 4 - Page 9 / Section 3

### 中文翻译
DRAM Bender 的设计目标是 nonrestrictive、easy-to-use 和 extensible。它让用户通过高级 API 编写实验，同时在 FPGA 内部执行低层 DRAM command sequence。

#### 3.1 Overview

原文位置：Page 4 - Page 5 / Section 3.1

系统由 host machine、FPGA board、DRAM module、DRAM Bender hardware logic 和 software API 组成。用户在 host 上编写 experiment program，程序被转换成 DRAM Bender instruction sequence，传输到 FPGA 后执行。FPGA 通过 DRAM PHY/DFI 控制 DRAM，并将 readback results 返回 host。

#### 3.2 Hardware Components

原文位置：Page 5 - Page 7 / Section 3.2

DRAM Bender 包含多个硬件模块。

Instruction dispatcher/program memory 保存用户生成的 DRAM command program，并按顺序或分支逻辑执行。Data buffers 保存要写入 DRAM 的 data patterns，也接收 DRAM readback 数据。DRAM Interface Adapter 把 DRAM Bender 内部指令转换为 PHY/DFI 接口所需信号。Memory elements 包括 program memory、data memory 和状态寄存器。

Periodic Operation Scheduler 用于定期插入 refresh、ZQ calibration 等 DRAM self-maintenance operations，确保实验期间 DRAM 不因完全关闭维护操作而偏离目标，或在需要时有意识地控制这些操作。Readback FIFO 处理 DRAM read latency 和 host/FPGA 数据返回之间的速率差。

这些模块共同保证：用户可以发任意低层命令，同时平台仍然能管理数据输入输出、调试和必要维护。

#### 3.3 Programming Interface

原文位置：Page 6 - Page 8 / Section 3.3

DRAM Bender 提供 C++ 和 Python APIs。用户可以构建 Program object，向其中添加 ACT、PRE、READ、WRITE、WAIT、BRANCH、LABEL 等指令。API 支持 sequential instruction list、labels、loops 和 branch，使复杂实验可以用简短代码表达。

Program Debugger 提供检查和调试能力，帮助用户发现非法 command sequence、标签错误或数据读写问题。作者强调 usability，因为很多 DRAM researchers 不一定熟悉 HDL 或 FPGA timing closure；如果实验平台过难使用，就会限制社区采用。

#### 3.4 Extensibility

原文位置：Page 8 / Section 3.4

DRAM Bender 采用 modular hardware IP cores，使用标准接口如 AXI4、PHY/DFI 等，使它能适配不同 FPGA boards。作者展示了 DDR3 changes 和 DDR4 support，并说明移植到另一 FPGA board 只需约 230 行 Verilog 和 30 行 C++ 修改。

#### 3.5 Experiment Workflow

原文位置：Page 8 - Page 9 / Section 3.5

一次实验 workflow 通常包括：在 host 端编写 C++/Python program；编译或生成 DRAM Bender instruction list；把程序和 data patterns 传到 FPGA；FPGA 执行 command sequence；readback FIFO 收集结果；host 读取并分析输出。这个 workflow 让 DRAM characterization 变成可重复的软件实验，而不是每次修改 HDL。

### 硬件工程师视角
Section 3 最值得学习的是平台抽象设计。DRAM Bender 没有把用户暴露在裸 DFI 信号上，而是定义了足够接近 DRAM command 的 instruction API。这种抽象层选择非常重要：太高层会失去控制力，太低层会难用且难扩展。硬件工具平台设计都面临这个平衡。

---

## 4. Use Cases / 使用案例

### 原文位置
Page 9 - Page 13 / Section 4

### 中文翻译
作者用三个主要 use cases 证明 DRAM Bender 的能力。

#### 4.1 Study #1: RowHammer Interleaving Pattern

原文位置：Page 9 - Page 11 / Section 4.1 / Figures 7-11 / Table 6

RowHammer 攻击通过反复激活 aggressor rows，在邻近 victim rows 中诱发 bit flips。传统 double-sided RowHammer 关注两个 aggressor rows 夹住 victim row 的情况。DRAM Bender 进一步研究 aggressor activation 和 precharge 的 interleaving pattern 如何影响攻击效果。

实验设置中，作者定义 interleaving parameter T，扫描 T=1 到 64K，总 ACT command 数固定为 1M。测试对象包括 Micron、Hynix 和 Samsung 的 DDR4 modules。Figure 7 展示 aggressor rows 和 victim rows 的布局。

结果显示，T 越接近 1，即 aggressor activations 更细粒度交错，bit flips 越多。对于 V2 行，T=64K 时三家厂商平均 bit flips 为 31.9、9.9、71.2；T=1 时分别增至 314.8、50.7、604.9。HCfirst 也受 interleaving 影响：T=1 时为 99K/80K/16K，T=64K 时为 130K/108K/23K。

这些结果说明 RowHammer effectiveness 不只取决于 hammer count，也取决于 activation/precharge 顺序。普通平台如果不能灵活控制 command interleaving，就可能错过这种现象。

#### 4.2 Study #2: RowHammer Data Patterns

原文位置：Page 11 - Page 12 / Section 4.2

第二个 study 研究 data pattern 对 RowHammer bit flips 的影响。不同 victim/aggressor data patterns 会改变 cell-to-cell coupling、sense amplifier behavior 和 disturbance sensitivity。DRAM Bender 支持用户灵活生成和写入 data patterns，因此可以系统扫描模式。

作者报告，DRAM Bender 支持的数据模式能发现更多 victim-row bit flips，说明固定少量 pattern 的测试可能低估 RowHammer 风险。

#### 4.3 Study #3: In-DRAM Bitwise Operations on DDR4

原文位置：Page 12 - Page 13 / Section 4.3 / Figure 12

第三个 study 探索 contemporary off-the-shelf DDR4 devices 是否能执行 in-DRAM Majority/AND/OR。作者通过特殊 command/timing sequence 在真实 DDR4 chips 上尝试 bitwise operations，并测量 bit error rate (BER)。

结果显示，某些 DDR4 segments 能支持 in-DRAM AND/OR，但可靠性不均匀。论文没有发现 0% BER segment；35 个 segments 在 <3% BER 下只支持 AND；最小 AND BER 为 1.9%；160 个 segments <5% BER；4546 个 segments <10% BER。

这个结果很重要：它说明真实 DDR4 中确实存在可利用的 in-DRAM computation 行为，但 BER 和 location heterogeneity 使它还不能直接当作可靠通用计算。后续研究需要选择可靠 segments、加入错误控制或把它用于 approximate workloads。

#### 4.4 Research Enabled by DRAM Bender

原文位置：Page 13 / Section 4.4

作者讨论 DRAM Bender 还能支持 retention time characterization、read disturbance、power measurement、DRAM refresh policy、in-DRAM computation、RowHammer mitigation evaluation 等研究。平台价值在于它不是为单一实验写死，而是让研究者快速构造新 command sequence。

### 硬件工程师视角
Use cases 是本文最有现实冲击力的部分。RowHammer interleaving 告诉你，安全漏洞的强弱可能取决于 controller scheduling 细节；DDR4 in-DRAM computation 告诉你，真实芯片里可能存在“标准外能力”，但可靠性远比论文 primitive 复杂。行业上这意味着 memory controller、firmware、BIOS 和 validation team 都需要更底层的测试工具。

---

## 5. Discussion and Future Work / 讨论与未来工作

### 原文位置
Page 13 - Page 14 / Sections 5-7

### 中文翻译
作者讨论 DRAM Bender 的边界和未来扩展。

#### 5.1 Characterization of RowHammer and Other Phenomena

原文位置：Page 13 / Section 5.1

DRAM Bender 可以用于系统表征 RowHammer，包括不同 vendors、temperatures、data patterns、refresh settings 和 command interleavings。它也适合研究 retention、timing failures 和 read disturbance。

#### Limitations

原文位置：Page 13 - Page 14

当前版本仍有局限。DDR5 支持、RFM command 研究和更多 FPGA board prototypes 是未来工作。功耗测量 setup 还在进行中，尚未完整发布。对于 packetized interfaces 的 3D-stacked DRAM，底层 DRAM interface 可能无法完全暴露，限制 DRAM Bender 的适用性。GUI 也是未来方向，目前平台主要面向程序化实验。

DRAM Bender 还能发特殊命令，但不等于能复现商用 memory controller 的所有调度策略。若要评估系统级影响，还需要把 characterization 结果与 full-system simulator 或真实系统测量结合。

### 硬件工程师视角
局限部分很实用。很多实验平台能看到底层现象，却不一定代表产品环境。DRAM Bender 适合发现和表征机制；要转化为行业决策，还需要把结果映射到真实 controller policy、ECC/RAS、thermal condition 和 workload behavior。

---

## 6. Related Work / 相关工作

### 原文位置
Page 14 - Page 15 / Section 6

### 中文翻译
作者将 DRAM Bender 与 SoftMC、LiteX RowHammer Tester、DRAM simulators、RowHammer testing tools、retention characterization platforms 和 other FPGA-based infrastructures 比较。SoftMC 开创了 programmable DRAM testing 的重要方向，但 DRAM Bender 试图进一步提升 instruction flexibility、API usability 和 board extensibility。LiteX RowHammer Tester 对 RowHammer 很有用，但不如 DRAM Bender 通用。

DRAM simulators 如 Ramulator 可以快速探索架构设计，但无法替代真实 chip testing。真实 DRAM 行为受 vendor、工艺、温度、电压、老化影响，很多现象只有上板测试才能发现。DRAM Bender 因此处在 simulator 和 commercial system 之间：它牺牲了一部分真实系统复杂性，换取对 DRAM command/timing 的精细控制。

### 硬件工程师视角
相关工作可以帮你建立工具选择标准：如果目标是快速探索架构趋势，用 simulator；如果目标是验证真实芯片物理现象，用 DRAM Bender/SoftMC；如果目标是评估应用端到端影响，还需要系统平台。不要把一种工具的结论外推到所有层次。

---

## 7. Future Work / 未来工作

### 原文位置
Page 15 / Section 7

### 中文翻译
未来工作包括支持 DDR5、研究 RFM 等新命令、扩展更多 FPGA boards、完善功耗测量、支持 GUI、以及扩展到更多 DRAM standards 或 memory technologies。作者也希望 DRAM Bender 能成为开放社区基础设施，让更多研究者复现实验、比较结果并探索新 DRAM 行为。

### 硬件工程师视角
DDR5/RFM 特别值得关注。随着 RowHammer mitigation 从 TRR 演进到 RFM 等机制，能够在真实 DDR5 上构造攻击和验证防护的平台会很重要。对行业来说，这直接关系到 memory security validation。

---

## 8. Conclusion / 结论

### 原文位置
Page 15 - Page 16 / Section 8

### 中文翻译
论文总结说，研究现代 DRAM chips 的可靠性、安全性和潜在内部功能，需要一个能够自由控制低层 DRAM command sequence、易于使用且易于扩展的真实硬件平台。DRAM Bender 提供这样的 FPGA-based infrastructure。它通过 nonrestrictive ISA、C++/Python APIs、modular FPGA design 和 debugging/workflow 支持，让研究者能够快速编写并执行 DRAM experiments。

RowHammer interleaving study 表明，激活顺序显著影响 bit flips 和 HCfirst；data pattern study 显示更灵活模式能发现更多 bit flips；in-DRAM DDR4 bitwise study 表明真实 DDR4 chips 中存在近似 in-DRAM logic 行为，但 BER 和 segment heterogeneity 是重要限制。

### 最终学习提炼
对硬件工程师而言，DRAM Bender 的学习价值主要在：

- 理解真实 DRAM testing 为什么需要 command/timing-level control。
- 学会区分 characterization platform、simulator 和 end-to-end system prototype。
- 认识 RowHammer 风险与 controller scheduling、data pattern、vendor variation 的关系。
- 看到 in-DRAM computation 在真实芯片上的可靠性边界。
- 学习如何设计面向研究社区的 FPGA infrastructure 和 API 抽象。

在行业现状中，DRAM Bender 对 memory security、RAS validation、DDR5 feature evaluation 和 PuM/PIM 真实性验证都有直接意义。它提醒我们，很多“架构假设”必须回到真实芯片上被测量。

---

## References / 参考文献

### 原文位置
References

### 处理说明
参考文献保留英文原文，不逐条翻译。建议重点追踪 SoftMC、LiteX RowHammer Tester、RowHammer、TRR/RFM、retention characterization、ComputeDRAM 和 PuM characterization 相关引用。
