# Full Chinese Translation

> 说明：以下为面向学习的逐节中文详译/译述，保留关键英文术语、API 名、指标名和数值；参考文献不逐条翻译。

## Title

原文标题：DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to Easily Test State-of-the-art DRAM Chips

中文标题：DRAM Bender：用于便捷测试先进 DRAM 芯片的可扩展、多用途 FPGA 基础设施

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

为了理解并改进 DRAM 的性能、可靠性、安全性和能效，研究者需要研究 commodity DRAM chips 的真实特征。然而现有开源基础设施要么过时、难以维护、难以使用，要么不够灵活。本文提出 DRAM Bender，一个 FPGA-based infrastructure，支持对先进 DRAM chips 做实验研究。DRAM Bender 同时提供三个能力：直接通过低层接口控制 DRAM，允许用户按任意顺序和更细粒度 timing 发送 commands；提供易用的 C++ 和 Python 编程接口；具有模块化设计，容易扩展到现有和新兴 DRAM interfaces 以及不同 FPGA boards。作者通过三个 case studies 展示其多用途性，并开源该平台。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

DRAM 是主存的主流技术，但工艺缩放使可靠性、延迟、安全性和能耗问题更加突出。理解这些问题需要测试真实芯片。真实芯片实验至少有两个用途：第一，揭示 scaling trends，例如 cell capacitance、crosstalk 对 RowHammer/retention 的影响；第二，发现 undocumented functionality，例如通过违反 timing parameters 实现 bulk copy、bitwise operations、TRNG 或 PUF。

普通计算机系统无法做这类实验，因为 CPU memory controller 会自动把 load/store 翻译成合法 DRAM commands，并严格遵守标准。已有开源平台 SoftMC 和 LiteX RowHammer Tester 又存在 data/command interface 限制、使用困难和扩展性不足。因此作者设计 DRAM Bender。

## 2. Background and Motivation / 背景与动机

### 原文位置

Page 3

### 中文翻译

论文回顾 DRAM organization、cell access、timing parameters、DFI 和 RowHammer。DRAM bank 包含 rows、bitlines、sense amplifiers；访问 row 需要 ACT、PRE、READ/WRITE 等 commands。RowHammer 是频繁激活 aggressor rows 导致附近 victim rows bit-flips 的 circuit-level phenomenon。研究这类现象必须能直接操控 command sequence 和 timing。

## 3. DRAM Bender Design / 设计

### 原文位置

Page 4 - Page 8

### 中文翻译

DRAM Bender 由 host API、instruction set、FPGA frontend/backend 和 DDR PHY interface 相关逻辑组成。用户用 C++/Python 创建 program，并通过 appendACT、appendPRE、appendREAD 等函数构造 command sequence。FPGA 收到 program 后，按用户指定的时间执行 DRAM commands。DRAM Bender 的 ISA 不强行限制 data patterns 和 command order，因此比 SoftMC/LRT 更适合探索异常 timing、RowHammer patterns 和 undocumented operations。

平台还提供 debugger、temperature control setup 和多个 FPGA prototypes。作者展示其移植到五种 FPGA boards，支持 DDR4 DIMM/SODIMM 和 DDR3 SODIMM。移植到另一 FPGA/DRAM interface 只需较小代码改动。

## 4. Use Cases / 用例研究

### 原文位置

Page 9 - Page 12

### 中文翻译

### 4.1 RowHammer: Interleaving Pattern of Activations

作者研究 double-sided RowHammer 中两个 aggressor rows 的激活交替方式。参数 T 表示连续 hammer 一个 aggressor row 多少次后切换到另一个。实验显示，T=1 的频繁交替通常比 T=64K 的 cascaded pattern 更有效。例如 sandwiched victim row 在三个厂商上 T=1 的平均 bit-flips 明显高于 T=64K。HCfirst 也随 T 改变，说明 RowHammer 防护不能只看总 activation count，还要理解 activation order。

### 4.2 RowHammer: Data Patterns

作者比较 SoftMC 支持的 8-bit data patterns 和 DRAM Bender 支持的随机 512-bit data patterns。结果显示，随机 512-bit patterns 在每个测试 victim row 上都至少发现一个 SoftMC patterns 未发现的 vulnerable cell。这说明测试基础设施的数据接口限制会影响 RowHammer characterization 的完整性。

### 4.3 In-DRAM Bitwise Operations

作者通过违反 timing parameters 的 ACT-PRE-ACT command sequence，在真实 DDR4 chips 上测试 bitwise AND/OR。结果显示，来自某一厂商的 DDR4 chips 中部分 segments 支持 majority-based AND/OR，但 bit error rate 不为 0；AND 通常比 OR 更可靠。这个结果支持 processing-using-memory 的可行性，但也说明真实芯片行为具有 heterogeneity。

## 5. New Research Directions / 新研究方向

### 原文位置

Page 12 - Page 13

### 中文翻译

DRAM Bender 可以用于 RowHammer characterization、power consumption studies、评估 RowHammer mitigations、探索 DRAM 未公开功能，以及开发 processing-in-memory / processing-near-memory prototypes。作者强调，开放、灵活、可复现的基础设施可以帮助学术界和工业界验证真实芯片行为，而不是只依赖文档或仿真。

## 6. Conclusion / 结论

### 原文位置

Page 13

### 中文翻译

DRAM Bender 是一个开源 DRAM testing infrastructure，兼具 versatile、extensible 和 easy-to-use。它提供 nonrestrictive DRAM interface 和 modular design，能发出任意顺序与任意 timing 的 DRAM commands，并已移植到五个 FPGA boards。作者希望它成为 DRAM systems research 的主流实验平台。
