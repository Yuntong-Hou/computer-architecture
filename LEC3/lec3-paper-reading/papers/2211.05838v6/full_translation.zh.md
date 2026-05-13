# Full Chinese Translation

## Title

原文标题：DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips

中文标题：DRAM Bender：用于便捷测试先进 DRAM 芯片的可扩展、多用途 FPGA 基础设施

原文位置：Page 1

处理说明：本文件按“完整度优先 + 硬件工程师视角”重写，覆盖摘要、引言、背景、DRAM Bender ISA/API/hardware stack、prototype、case studies、research directions、related work 和 conclusion。参考文献列表保留英文，不逐条翻译。

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

为理解并改进 DRAM 的性能、可靠性、安全性和能效，已有研究会分析 commodity DRAM chips 的特征。但当前最先进的开源基础设施要么过时、缺乏维护、难以使用，要么不够灵活，限制了可开展的实验类型。

作者提出 DRAM Bender，一个新的 FPGA-based infrastructure，用于在 state-of-the-art DRAM chips 上开展实验研究。DRAM Bender 同时具备三项关键特性：第一，它允许用户通过 low-level interface 直接与 DRAM chip 交互，从而以任意顺序和更细时间粒度发送 DRAM commands；第二，它提供易用的 C++ 和 Python programming interfaces，使用户能快速开发不同类型实验；第三，它易于扩展，模块化设计支持已有和新兴 DRAM interfaces，也可移植到新的商用或自定义 FPGA boards。

为展示 DRAM Bender 的通用性，作者进行了三个 case studies，其中两个产生了 RowHammer 相关新观察。结果显示，DRAM Bender 支持的数据模式能在 victim row 中发现比先前常用模式更多的 bit-flips。作者还展示 DRAM Bender 已移植到五种 FPGA boards，支持 DDR4 和 DDR3，并开源。

### 硬件工程师视角

DRAM Bender 的核心价值是“实验控制权”。普通 CPU memory controller 会隐藏或禁止很多低层命令和 timing violation，因此无法探索真实 DRAM 的边界行为。DRAM Bender 让研究者能像写程序一样控制 ACT/PRE/RD/WR、timing、data pattern 和温度，这对 RowHammer、retention、PIM primitive、timing margin、vendor variation 都是基础工具。

---

## 1. Introduction / 引言

### 原文位置
Page 1-3 / Section 1

### 中文翻译

DRAM 是主存的主流技术，因为它具有低延迟和低 bit cost。但工艺缩放让 DRAM 的性能、能效、安全和可靠性持续提升变得困难。为了理解并克服这些挑战，必须在真实芯片上实验性地研究 DRAM 行为。

DRAM testing infrastructures 至少能支持两类重要研究。第一，理解 DRAM scaling trends，例如 cell capacitance、capacitive crosstalk、latency、retention、RowHammer vulnerability 如何随制程变化。第二，发现 undocumented functionality。标准 DRAM interface 中的 timing constraints 会阻止很多非标准操作，例如 bulk data copy、bitwise operations、true random number generation、physical unclonable functions 等，这些往往需要违反 timing parameters 才能发现。

普通计算系统无法自由修改或违反 DRAM timing parameters。CPU 只发 load/store，memory controller 将其翻译为合规 DRAM commands。因此，探索低层 DRAM 行为需要专门基础设施。

已有开源 FPGA 平台 SoftMC 和 LiteX RowHammer Tester 有限制。SoftMC 的 data patterns 受限，程序不同部分之间存在微秒级不确定延迟，并且依赖过时 board 和工具。LiteX RowHammer Tester 对 successive DRAM commands 至少有 10 ns 延迟，很多标准 timing 参数都无法违反；同时，每种新实验常需要写 HDL 后处理模块。

DRAM Bender 的目标是克服这些问题：非限制 ISA 充分暴露 DRAM interface；C++/Python API 降低使用门槛；模块化设计支持新 DRAM standards 和 FPGA boards。Table 1 显示，DRAM Bender 是唯一同时具备 no interface restrictions、ease of use、extensibility、DDR3/DDR4 和五个 FPGA prototype 的开源测试基础设施。

论文贡献包括：开发 DRAM Bender；提出 RowHammer bit-flips 的两个新观察；证明 off-the-shelf DDR4 可执行 in-DRAM bitwise Majority/AND/OR；展示五个 FPGA boards 原型；开源基础设施。

### 硬件工程师视角

引言里的工程教训是：验证 DRAM 的真实行为，不能只依赖 JEDEC 合规路径。很多可靠性和安全问题发生在标准抽象下面：cell coupling、sense amplifier behavior、timing margin、address mapping、temperature、data pattern。硬件工程师需要能直接驱动 DRAM 命令和观察数据，否则只能看到被 memory controller 过滤后的系统级现象。

---

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 3-4 / Section 2

### 中文翻译

背景部分回顾 DRAM organization、cell access、timing parameters 和 DFI。DRAM 系统层级包括 channel、module、rank、chip、bank、subarray、row、column。访问一个 cell 需要先通过 ACT 激活 row，使 cell 与 bitline 共享电荷并由 sense amplifier 放大；随后通过 READ/WRITE 访问列；最后 PRE 关闭 wordline 并把 bitlines 预充到 VDD/2。

关键 timing parameters 包括 tRCD、tRAS、tRP 等。tRCD 是 ACT 到 RD/WR 的间隔；tRAS 是 row 必须保持 active 的时间；tRP 是 PRE 后到下一个 ACT 的时间。很多非标准实验通过缩短这些参数暴露 DRAM 边界行为。

DFI (DDR PHY Interface) 标准化 memory controller 与 PHY layer 之间的通信。MC scheduler 生成 DRAM commands，PHY 操作物理信号。DRAM Bender 需要在 FPGA 内构建可控的 controller/PHY-facing 结构，使用户能发出精确 command sequence。

### 硬件工程师视角

做 DRAM 实验时，时间分辨率至关重要。比如 tRAS/tRP 从 1.5 ns 到 15 ns 扫描能暴露 bitwise operation；interleaving parameter T 能改变 RowHammer 强度。如果平台不能保证命令间隔确定，就无法把观察结果归因到 DRAM 本身。

---

## 3. DRAM Bender Design / DRAM Bender 设计

### 原文位置
Page 4-8 / Section 3, Tables 2-4, Figures 3-4

### 中文翻译

DRAM Bender 的设计包括 ISA、hardware modules、software modules、program debugger 和多个 FPGA prototypes。

### 3.1 Instruction Set Architecture

DRAM Bender ISA 包含两类指令。第一类是 RISC-like regular instructions，操作 programmable core 的寄存器，例如 load/store scratchpad、AND/OR/XOR、ADD/SUB、branch、jump、sleep。第二类是 DRAM instructions，用于向 DRAM module under test 发送 DRAM commands。

一个 DRAM instruction 包含四个任意 DRAM commands。这样做的原因是 FPGA DRAM PHY 常会序列化每周期接收的多个 DRAM commands，并以更高频率逐个发给 DRAM；DRAM Bender 每周期处理四个命令，可让核心频率比 DRAM 最低标准频率低四倍，同时仍能生成紧密 timing。

ISA 支持 13 个 general purpose registers 和 4 个 special registers。其中 address stride registers 自动递增地址寄存器，支持复杂访问模式；wide-data register 大小等于 DRAM transfer size，例如 DDR4 8-chip module 为 512 bits，可让用户写入任意 512-bit data pattern。相比 SoftMC 只能指定重复 8-bit pattern，这极大扩展了 RowHammer data pattern 实验能力。

### 3.2 Hardware Modules

DRAM Bender hardware 包括 programmable core、modular memory controller subsystem、instruction memory、data scratchpad、readback FIFO 和 periodic operation scheduler。

programmable core 是五级 in-order pipeline：fetch、decode、三个 execute stages。decode stage 把指令解析为一个 regular µ-op 或四个 DRAM µ-ops。DRAM pipeline 每周期执行四个 DRAM µ-ops。控制流指令会 stall pipeline，但 penalty 固定为 6 cycles，因此不会引入不可预测 timing。

DRAM Interface Adapter 位于 DRAM pipeline 和物理 DRAM interface 之间。DRAM pipeline 输出 one-hot encoded command signals，例如 dram_act、dram_write；adapter 将这些简化信号翻译成复杂 PHY interface。该 adapter 与主体设计解耦，因此支持新 DRAM interface 时主要修改 adapter。

Memory Elements 包括 instruction memory、data scratchpad 和 readback FIFO。readback FIFO 缓冲从 DRAM 读回的数据，避免 host-FPGA interface 带宽与 DRAM interface 带宽不匹配导致 pipeline stalls。DRAM Bender 采用预防性机制：只在 timing-non-critical 的 regular instruction 处 stall，不在连续 DRAM command sequence 中间 stall，从而不破坏用户指定 timing。

Periodic Operation Scheduler 用于执行 DRAM 所需周期性操作，例如 refresh、ZQ calibration、periodic READ。它保存用于周期性操作的 DRAM Bender programs，并在需要时调度。

### 3.3 Software Modules

DRAM Bender 提供 C++ API 和 Python interface。Program class 用于构建 DRAM Bender programs，用户按顺序 append 指令和 labels。Platform class 执行 program、reset platform、控制 auto-refresh、取回数据。Board class 封装 FPGA board-specific interface，例如 PCIe driver。

Listing 1 展示 14 行 C++ 代码读取 DRAM row。appendACT、appendREAD、appendPRE 等函数可以指定地址寄存器、自动递增 flag 和 optional delay。optional delay 让用户轻松构造任意 timing parameters；address stride 支持任意 stride access。

program debugger 使用 Vivado Simulator 和 DRAM device model，在没有硬件 setup 的情况下分析 timing violations，并可查看 waveform。对硬件工程师，这很重要：实验脚本可以先做 timing simulation，避免在真实板上调试低层错误。

### 3.4 Prototypes

作者在五个 FPGA boards 上实现 DRAM Bender，支持 DDR4 DIMM/RDIMM/UDIMM/SODIMM 和 DDR3 SODIMM。突出原型是 Xilinx Alveo U200，配合 SODIMM-to-DIMM adapter 可测试大多数可用 DRAM modules。Table 3 给出 FPGA boards 和 DRAM standards；Table 4 给出资源占用。DRAM Bender 在 DDR4 boards 上 timing resolution 为 1.5 ns，在 DDR3 board 上为 2.5 ns。

作者还提供 controlled environment：Maxwell FT200 temperature controller、silicone rubber heaters、thermocouple，用于将 DRAM chips 保持在目标温度。这对 RowHammer 和 retention 实验非常关键。

### 硬件工程师视角

DRAM Bender 的设计展示了一个好的硬件实验平台应具备的四个属性：命令级控制、确定 timing、任意 data pattern、可移植 board/PHY adapter。实际使用时，还应关注温控、供电、模块厂商差异、address mapping、DIMM topology 和 PHY calibration，否则实验结论可能混入平台噪声。

---

## 4. Use Cases / 用例研究

### 原文位置
Page 9-12 / Section 4, Figures 7-12, Table 6

### 中文翻译

作者用三个 case studies 展示 DRAM Bender 的通用性。

### 4.1 Study #1: RowHammer Interleaving Pattern

实验研究 double-sided RowHammer 中两个 aggressor rows 的 activation/precharge 顺序对 bit-flips 的影响。作者定义 interleaving parameter T：每轮先 hammer 第一个 aggressor row T 次，再 hammer 第二个 aggressor row T 次，总 ACT commands 固定为 1M。T=1 表示高度交替；T=64K 表示更接近 cascaded pattern。

结果显示，T 越接近 1，sandwiched victim row V2 的 bit-flips 越多。在三个厂商上，T=64K 时 V2 平均 bit-flips 分别为 31.9、9.9、71.2；T=1 时分别为 314.8、50.7、604.9。HCfirst 也受影响：T=1 时三个厂商最小 HCfirst 为 99K、80K、16K；T=64K 时为 130K、108K、23K。结论是，aggressor activation interleaving pattern 显著影响 RowHammer 强度和首次 bit-flip 所需 hammer count。

### 4.2 Study #2: RowHammer Data Patterns

第二个实验研究 data pattern 对 RowHammer bit-flips 的影响。SoftMC 只能使用有限 256 个 8-bit patterns，每个 pattern 重复形成 512-bit transfer data；DRAM Bender 可以使用随机 512-bit data patterns。作者对 victim row 的 512-bit cache block 记录 bit flips，并比较 SoftMC patterns 与 DRAM Bender random patterns。

结果显示，对三个厂商的每个测试 victim row，随机 512-bit data patterns 都能发现至少一个 SoftMC patterns 未发现的额外 flipping cell。结论是，DRAM Bender 能发现先前受限 pattern 无法发现的 RowHammer-susceptible cells。

### 4.3 Study #3: In-DRAM Bitwise Operations

第三个实验展示 off-the-shelf DDR4 chips 是否能执行 in-DRAM bitwise AND/OR。作者通过 ACT -> PRE -> ACT 命令序列并违反 timing parameters，在 DRAM segment 中利用 majority function 实现 AND/OR。tRAS 和 tRP 从 1.5 ns 到 15 ns 扫描。

结果发现，在 SK Hynix DDR4 芯片上，当 (tRAS, tRP) 为 (1.5 ns, 1.5 ns)、(1.5 ns, 3.0 ns)、(3.0 ns, 1.5 ns) 时，可观察到有效 majority AND/OR 操作。没有 segment 达到 0% BER，但存在显著 heterogeneity。AND 比 OR 更可靠；35 个 segments 支持 <3% BER 的 AND；160 个 segments 支持 <5% BER 的 AND/OR；4546 个 segments 支持 <10% BER。

作者认为，DDR4 中确实存在 in-DRAM bitwise operation 能力，但它不是理想数字逻辑，而是存在 BER 的模拟/电路现象。这可被 approximate computing 利用，例如把 AND 操作放在 AND BER 更低的 segments。

### 硬件工程师视角

三个 case studies 的工程意义非常强。

第一，RowHammer 不是只由 hammer count 决定，时间交错模式也很关键。这影响攻击构造，也影响 defense 评估。

第二，data pattern 覆盖不足会导致漏报 vulnerable cells。做 memory reliability/security validation 时，pattern space 不能过窄。

第三，in-DRAM bitwise operations 在真实 DDR4 上“可观察”不等于“可直接产品化”。BER heterogeneity、segment selection、温度/电压稳定性、厂商差异、ECC 交互都必须评估。

---

## 5. Research Enabled and Future Directions / 已支持研究与未来方向

### 原文位置
Page 12-13 / Sections 4.4-5

### 中文翻译

DRAM Bender 已支持多项研究，包括 read disturbance characterization、RowHammer mitigation evaluation、true random number generation、undocumented DRAM functionality、approximate DRAM、end-to-end processing-in-DRAM framework 和 HBM2 DRAM testing infrastructure。

作者提出两个未来研究方向。第一，state-of-the-art DRAM chips 上的 RowHammer characterization。DRAM Bender 可公开评估真实 DDR4 RowHammer mitigations 的安全保证，并发现潜在新 vulnerability。第二，power consumption studies。现有 DRAM power models 往往不准确，因为 datasheet guardband 会掩盖真实功耗变化，IDD/ICC values 也不覆盖峰值条件。DRAM Bender 能支持更真实的功耗测量和建模。

### 硬件工程师视角

对硬件团队，DRAM Bender 不只是学术工具，也可作为 pre-silicon/post-silicon validation 思路参考。产品团队如果无法使用 DRAM Bender，也应在内部 controller/PHY validation 环境中保留类似能力：低层命令注入、timing sweep、temperature sweep、data pattern sweep、vendor A/B/C 对比和错误日志导出。

---

## 6. Related Work / 相关工作

### 原文位置
Page 13-14 / Section 6

### 中文翻译

相关工作包括两类：一类是 DRAM testing infrastructures，例如 SoftMC、LiteX RowHammer Tester、各种 vendor/academic 平台；另一类是利用这些平台进行的 DRAM characterization、RowHammer、retention、latency、energy、PIM primitive、TRNG、PUF 等研究。作者强调 DRAM Bender 与 prior infrastructures 的区别在于同时具备无接口限制、易用性和可扩展性。

### 硬件工程师视角

相关工作说明“实验平台本身就是架构贡献”。如果一个平台降低实验门槛，它会放大后续研究产出。硬件工程团队在搭建内部验证环境时，也应把易用 API、调试器、可移植性、温控、数据处理 pipeline 当作一等目标，而不是只做一次性脚本。

---

## 7. Conclusion / 结论

### 原文位置
Page 14 / Section 8

### 中文翻译

作者开发了一个新的开源 DRAM testing infrastructure，具备多用途、可扩展、易用的特点。不同于已有开源基础设施，DRAM Bender 同时提供 nonrestrictive interface 和 extensible design。它的 API 允许用户以任意顺序、任意时间发送 DRAM commands。模块化设计使其易于集成新 DRAM interfaces 并移植到不同 FPGA boards。

作者通过三个研究展示 DRAM Bender 的通用性和易用性，并通过移植到五个支持 DDR3/DDR4 的 FPGA boards 展示可扩展性。作者希望 DRAM Bender 成为实验性 DRAM 研究的主流基础设施，并帮助开发提升 DRAM 安全、可靠性、性能和能效的新机制。

### 面向硬件工作的学习提炼

这篇论文对硬件工程师最直接的价值是方法论：真实 DRAM 不是完全由标准文档定义的数字黑盒，它有大量 analog/circuit-level 行为。若想研究 RowHammer、retention、timing margin、PIM primitive 或 vendor variation，必须有能打破标准 memory controller 限制的实验平台。DRAM Bender 提供了可复用的接口和工程结构。

---

## References / 参考文献

### 原文位置
Page 14 onward / References

参考文献列表保留英文原文，不逐条翻译。建议配套阅读 SoftMC、U-TRR、QUAC-TRNG、ComputeDRAM、RowHammer characterization、DRAM Bender GitHub repository。
