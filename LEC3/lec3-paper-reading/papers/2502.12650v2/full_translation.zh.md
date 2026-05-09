# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述，不提供逐字长篇翻译。本文为 2025 年较新版本，附录包含结果修正说明；笔记按当前 PDF v2 记录。

## Title
原文标题：Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance

中文标题：Chronus：理解并加固前沿工业 DRAM 读扰动解决方案

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究工业界最新的 DRAM read disturbance 防护，尤其是 PRAC/RFM。作者指出 PRAC 虽然朝标准化方向前进，但仍存在性能、能耗和安全弱点。论文提出 Chronus，通过重新组织片内计数器、动态保护刷新和去除固定延迟，显著降低开销并提升对攻击访问模式的抵抗能力。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
引言说明 RowHammer threshold 继续下降，传统防护越来越难以承受。PRAC 代表工业界将 row activation tracking 放入 DRAM 的努力，但初步研究显示其成本很高，尤其在未来低 NRH 下可能使系统不可用。

作者认为，需要更深入地理解 PRAC 的设计弱点，而不是简单否定片内计数方向。Chronus 的目标是在保持工业可部署性的同时，减少关键路径开销并避免攻击者利用固定刷新节奏。

## 2. Background and PRAC Weaknesses / 背景与 PRAC 弱点

### 原文位置
Page 2 - Page 5

### 中文翻译
背景部分回顾 PRAC/RFM 工作方式。DRAM 跟踪 row activation，当风险升高时向 memory controller 发出 back-off；控制器随后发出 RFM，让 DRAM 执行 preventive refresh。

论文指出三类问题。第一，activation counter update 位于关键时序路径上，导致 tRP/tRC 等 timing 增加，即使没有攻击也影响正常访问。第二，PRAC 使用固定数量的 preventive refresh，不能根据实际风险灵活调整。第三，refresh 后存在 delay period，攻击者可以围绕这一固定窗口构造 wave attack 或 feinting attack，从而迫使系统使用更保守阈值。

## 3. Attacks on PRAC Variants / 对 PRAC 变体的攻击

### 原文位置
Page 4 - Page 6

### 中文翻译
wave attack 利用 PRAC 的刷新与延迟节奏，让 aggressor activation 分布在多个窗口中，从而尽可能接近或超过危险累积扰动。feinting attack 则通过诱导防护机制关注某些 row 或时段，掩护真正危险的访问序列。

这些攻击说明，防护机制的确定性本身会成为攻击面。如果防护总是在固定条件下执行固定数量刷新，并在固定时间后恢复，攻击者就可以学习这个节奏。

## 4. Chronus Design / Chronus 设计

### 原文位置
Page 6 - Page 9

### 中文翻译
Chronus 的第一项设计是把 counter 与 data 分离。传统 PRAC 在访问过程中更新计数，可能延长关键 timing；Chronus 让 counter update 与数据访问并行，避免把计数逻辑放在 tRP/tRC 关键路径上。

第二项设计是动态控制 preventive refresh 数量。与固定刷新次数不同，Chronus 根据当前风险状态决定需要刷新多少 victim row，从而在安全时减少无效刷新，在高风险时提供足够保护。

第三项设计是去除固定 delay period。这样攻击者无法围绕固定延迟窗口组织 wave 或 feinting pattern，也减少了 memory controller 被迫等待的时间。

## 5. Evaluation Methodology / 评估方法

### 原文位置
Page 9 - Page 10

### 中文翻译
评估使用 cycle-level/system-level 模拟，覆盖现代和未来 NRH。工作负载包括多程序 memory-intensive workloads；比较对象包括多个 PRAC variant 以及 Graphene、Hydra、PARA。指标包括性能开销、DRAM energy overhead、攻击模式下的稳健性和实现成本。

## 6. Results / 结果

### 原文位置
Page 10 - Page 13

### 中文翻译
结果显示，PRAC 变体在现代 NRH 下已有明显开销，在未来低 NRH 下开销急剧恶化。论文报告 PRAC 在现代 NRH>1K 时平均/最大性能开销约 5.8%/8.9%，能耗 10.7%/13.5%；NRH=20 时性能开销升至 78.5%/90.7%，能耗 6.6x/7.1x。

Chronus 显著改善这一情况。在 NRH=1K 时，Chronus 平均性能开销低于 0.1%，DRAM energy overhead 约 10.3%。在 NRH=20 时，Chronus 平均性能开销约 8.3%，能耗开销约 17.9%。这说明 Chronus 在极低阈值下仍能保持系统可用性。

与 Graphene、Hydra 和 PARA 相比，Chronus 的综合表现更稳定。它既避免 PARA 在低 NRH 下概率刷新过多的问题，也避免 PRAC 固定 RFM 和 delay 带来的严重阻塞。

## 7. Discussion / 讨论

### 原文位置
Page 13 - Page 15

### 中文翻译
讨论部分强调 Chronus 的意义：它不是完全重写 DRAM 系统，而是在 PRAC/RFM 思路上修改关键设计点，使工业方向更可持续。作者也讨论实现成本、与标准兼容性、以及未来低 threshold DRAM 的需求。

需要注意的是，Chronus 仍主要围绕 activation-count based RowHammer。对于 RowPress 中的 row-open time、Variable Read Disturbance 中的 temporal variation，以及复杂 on-die ECC 行为，仍需要进一步扩展分析。

## Appendix / 附录

### 原文位置
Appendix A-B

### 中文翻译
附录包含 decrementer/counter 相关实现细节、artifact 说明以及结果修正说明。论文 v2 明确给出早期结果 bug 的修正表，并说明主要结论保持不变。阅读和引用时应使用修正后的数值。

## Conclusion / 结论

### 原文位置
Page 15

### 中文翻译
Chronus 证明，PRAC 的工业方向可以通过更好的计数器组织、动态刷新和去确定性延迟得到显著改进。在未来 RowHammer threshold 继续下降的情况下，这类低开销、抗攻击的片内/控制器协同防护可能成为 DRAM 安全的关键。
