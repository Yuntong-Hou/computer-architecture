# Full Chinese Translation

> 说明：以下为面向学习的逐节中文详译/译述，保留关键英文术语和论文名；参考文献不逐条翻译。

## Title

原文标题：Fundamentally Understanding and Solving RowHammer

中文标题：从根本上理解并解决 RowHammer

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

本文概述 RowHammer vulnerability 的最新进展和未来方向。RowHammer 是现代 DRAM 芯片中的一种现象：反复访问某一行会使物理邻近行发生 bit-flips。由于 DRAM 几乎用于所有系统主存，这带来严重且广泛的安全问题。近年分析表明，随着 DRAM scaling，RowHammer 在 device/circuit level 上更严重，并对温度、电压、数据模式、访问模式和 memory control policies 等变量敏感。作者回顾 RowHammer 的利用、理解和缓解进展，并主张未来需要两条路线：更深入理解问题的各个维度，以及通过 system-memory cooperation 设计极高效且 fully-secure 的解决方案。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

DRAM 因低延迟和低 bit cost 成为主存主流技术。RowHammer 是 DRAM 中由于频繁访问 aggressor rows 造成 nearby victim rows 数据保持失败的现象。这些 bit-flips 具有可重复性，因此可被攻击者用于 targeted fault injection。随着 DRAM cell 更小、cell-to-cell spacing 更近，RowHammer vulnerability 增强。作者引用近年研究说明，RowHammer threshold 已显著下降，bit-flip 数显著上升。

RowHammer 的影响不限于可靠性。恶意程序可诱导敏感数据 bit-flips，破坏 system integrity、confidentiality、availability。现代系统的安全原则依赖 memory isolation，而 RowHammer 直接破坏这一基础。

## 2. A Brief Overview of RowHammer until 2020 / 2020 年前概览

### 原文位置

Page 2

### 中文翻译

2014 年原始 RowHammer 工作展示，三大 DRAM 厂商的 DDR3 modules 中大量模块 vulnerable，且用户态程序可在真实 CPU 系统上诱导 bit-flips。随后研究者开发了多种攻击，覆盖移动端、服务器、浏览器、虚拟机等。也有研究从 device/circuit level 理解 RowHammer 原因，并提出多种硬件或软件缓解方案。

工业界采用过提高 refresh rate、pTRR、TRR 等方案。提高 refresh rate 成本高；pTRR 依赖 memory controller，可能不知道真实物理邻接关系；TRR 由 DRAM vendor 内部实现但细节不公开，因此缺乏可验证保证。

## 3. Major Developments in 2020 / 2020 年关键进展

### 原文位置

Page 2 - Page 3

### 中文翻译

TRRespass 证明，被宣称为 RowHammer-free 的 TRR-protected DDR4 chips 仍可被攻破。它使用 many-sided RowHammer attack，hammer 多个 rows 以绕过或溢出 proprietary TRR tracking structures。这说明 security by obscurity 不是可靠方案。

Revisiting RowHammer 从 device/circuit level 测试 1580 个 DRAM chips，证明 RowHammer 随新代 DRAM 更严重：first bit-flip 所需 activation count 更低，bit-flip 数更多。若趋势继续，已有防护机制要么无法工作，要么开销过高。

DDR5 引入 RFM 来支持 in-DRAM mitigation，但由于 MC 以 bank granularity 计数，可能在没有攻击时也触发 RFM commands，带来性能开销。

## 4. Recent RowHammer Developments / 近年进展

### 原文位置

Page 3 - Page 5

### 中文翻译

近年研究包括三类：利用 RowHammer 的攻击、理解和建模 RowHammer 的实验/模型、以及缓解/解决 RowHammer 的机制。攻击方面，有更多 access patterns、remote attack、cross-boundary attack 等。理解方面，研究者关注 spatial correlation、reduced wordline voltage、temperature、pattern sensitivity 等。缓解方面，出现了 BlockHammer、SMD、RRS、AQUA、HiRA、Hydra 等不同路线。

作者指出，很多机制在未来更低 RowHammer threshold 下会面临面积、性能或能耗问题。系统与内存协同可能是长期方向，因为 DRAM 内部知道物理布局和脆弱性，而系统侧知道进程、数据重要性和安全上下文。

## 5. Future Directions / 未来方向

### 原文位置

Page 5 - Page 6

### 中文翻译

第一条方向是建立更基础和全面的 RowHammer 理解。需要研究 aging、temperature、supply voltage、access patterns 对 RowHammer 的单独和组合影响。也需要在 CPUs、GPUs、accelerators、FPGAs、HBM、emerging NVM 等不同系统和内存技术中研究 RowHammer-like effects。SoftMC 和 DRAM Bender 这类 FPGA-based infrastructures 对这类研究很重要。

第二条方向是设计极高效且 fully-secure 的 solutions。随着 vulnerability worsening，benign workloads 也可能触发 threshold，因此防护不能只面向攻击，也要避免正常程序导致数据损坏或大量 mitigation overhead。作者主张 system-memory co-design：系统与 DRAM 共同设计，既防止 bit-flips，又避免 DoS 和过度开销。

## 6. Conclusion / 结论

### 原文位置

Page 6

### 中文翻译

本文简要回顾 RowHammer 研究历史和当前状态，并指出未来关键方向。作者认为，尽管已有大量研究，RowHammer 仍然远未解决，因为它是 DRAM technology scaling 的基本问题，并且会继续影响几乎所有使用 DRAM 的系统。社区需要更深入理解 RowHammer，并寻找更高效、更可靠的解决方案。
