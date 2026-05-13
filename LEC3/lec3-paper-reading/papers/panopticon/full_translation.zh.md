# Full Chinese Translation

## Title

原文标题：Panopticon: A Complete In-DRAM Rowhammer Mitigation

中文标题：Panopticon：完整的 in-DRAM RowHammer 缓解机制

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖 in-DRAM counter mats、threshold bit、service queue、ALERTn 机制、安全分析和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

RowHammer 防御需要跟踪大量 row activation，并在达到阈值前刷新 victim rows。已有方案往往需要 memory controller 中的大量 SRAM/CAM 状态，或者要求 controller、DRAM、OS 多方协作，部署困难。Panopticon 提出一种 complete in-DRAM RowHammer mitigation：把每行 activation counter 放入 DRAM 内部 counter mats，复用 row decoder 做 lookup，并利用 DDR4 ALERTn 信号向 controller 请求时间来执行 mitigation。

Panopticon 的目标是在 DDR4 场景下除 DRAM 芯片外尽量不修改其他硬件。它用 thin 16-bit counter mats 为每行维护 counter，用 threshold bit 替代完整阈值比较，用 service queue 记录需要服务的 aggressor rows，并在需要时刷新潜在 victim rows。论文还分析若不能通过 ALERTn 暂停 controller，攻击者可能填满 service queue，因此请求时间机制是安全性的必要条件。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Motivation, Table I

### 中文翻译

RowHammer mitigation 的难点是状态规模。现代 DRAM 有大量 rows，若 memory controller 为每行维护精确 activation counter，SRAM/CAM 开销很高。Graphene、TWiCe、BlockHammer 等方案在状态、协议或部署上存在代价。Table I 显示，Graphene 在 DDR4 每 channel 需 39.23KB CAM，每 CPU 约 156.9KB；BlockHammer/TWiCe 需求更高。

Panopticon 的核心思路是：既然 RowHammer 风险源于 DRAM row activity，就把跟踪状态放在 DRAM 内部。DRAM 本身知道 row activation，内部 row decoder 也能定位 row，因此可以用阵列式 counter mats 存储 per-row counters，避免 controller 维护大表。

从工程视角看，这是 RowHammer 防御部署路径的另一种选择：不要求系统/OS/controller 大改，而要求 DRAM vendor 在芯片内部实现完整防御。它降低跨供应商协同复杂度，但把验证和面积功耗压力转移到 DRAM 设计侧。

## 2. Counter Mats and Threshold Bit / Counter Mats 与阈值位

### 原文位置
Page 3-5 / Figures 1, 4, 5

### 中文翻译

Panopticon 在每个 bank 内增加 thin 16-bit counter mats。每条 DRAM row 对应一个 counter，用于记录 activation 次数。由于 counter mats 与 row decoder 共享地址选择逻辑，访问某 row 时可以同步定位其 counter 并 increment。

完整比较 counter value 与阈值会增加逻辑和功耗。Panopticon 使用 threshold bit 技巧：选择 counter 中某一 bit，例如 b10。当该 bit toggle 时，表示 activation 次数跨过某个 2^k 边界，系统把 row address 放入 service queue。这样避免每次 activation 做完整比较，也避免昂贵 counter reset。

如果 b10 toggle 对应每 1024 activations 入队一次，系统就能在 row activation 接近危险阈值前多次获得服务机会。16-bit counter 支持最高 65,536 activation threshold，覆盖现代较低 RowHammer threshold 场景。

## 3. Service Queue and Victim Refresh / 服务队列与 Victim Refresh

### 原文位置
Page 5 / Section V-D

### 中文翻译

当 threshold bit 触发时，aggressor row address 被放入 service queue。Panopticon 在收到 REF 或获得服务时间时，从队列取出 row address，并刷新潜在 victim rows。队列大小可以很小，论文提出 8 entries/bank。对于 DDR4 row address 18 bits，约 144 bits/bank，远小于 Graphene 等 controller-side 表。

Service queue 的安全性取决于能否及时清空。如果攻击者能让大量 aggressor rows 连续入队，而 DRAM 没有额外时间服务队列，就可能溢出或延迟 victim refresh，产生安全缺口。

## 4. ALERTn Mechanism / ALERTn 请求时间机制

### 原文位置
Page 5-6 / Figures 6-7

### 中文翻译

Panopticon 复用 DDR4 ALERTn 信号，让 DRAM 在需要执行 mitigation 时通知 memory controller 暂停发命令。ALERTn 原本用于错误/警告类信号，Panopticon 将其作为“DRAM 需要时间服务 RowHammer 队列”的通道。

论文安全分析显示，如果没有 ALERTn 或类似方式请求 controller 时间，攻击者可在较短时间内填满 service queue。因此 ALERTn 不是性能优化，而是安全边界的一部分。它保证 DRAM 内部 mitigation 有机会执行，而不是被正常/恶意访问流完全压制。

工程上，复用现有 DDR4 信号降低协议修改，但需要 controller 正确响应 ALERTn，并且系统要定义 ALERTn 被频繁触发时的性能和错误处理语义。

## 5. Security and Overhead Analysis / 安全与开销分析

### 原文位置
Page 5-7 / Analysis sections

### 中文翻译

Panopticon 主要进行 architecture/security analysis，而非完整 workload 性能评估。它比较状态开销，分析 service queue 被攻击者填满或连续触发的可行性，并讨论 counter mats 的 power/space overhead。

相比 controller-side CAM/SRAM 方案，Panopticon 状态更贴近 DRAM row，查找利用 DRAM 解码路径，避免为每 channel/CPU 维护大规模 tracking table。代价是 DRAM 芯片内部增加 counter mats、incrementer/testing logic、service queue 和 ALERTn state machine。

作者指出 counter mats 实际 power/space overhead 需要 DRAM vendor 精确评估。这是重要局限：architecture-level 状态规模小不等于产品级面积功耗一定低，DRAM die 对面积、功耗、测试和 yield 非常敏感。

## 6. Limitations / 局限性

### 原文位置
Page 6-7 / Discussion

### 中文翻译

Panopticon 需要 DRAM 内部设计改动，因此仍依赖 vendor 采用和验证。它对 DDR4 ALERTn 的复用在 DDR5/HBM/LPDDR 中需要重新适配。论文缺少完整系统 workload 的性能、能耗和 timing closure 评估。

另外，RowHammer threshold 随工艺持续下降时，counter width、service queue size 和 mitigation latency 都要重新设计。若 future attacks 能构造更复杂 multi-row pattern，victim selection 逻辑也需保证覆盖。

## 7. Conclusion / 结论

### 原文位置
Page 7 / Conclusion

### 中文翻译

Panopticon 提出一种将 RowHammer tracking 和 mitigation 放入 DRAM 内部的完整方案。通过 counter mats、threshold bit、service queue 和 ALERTn，它减少 controller-side 状态和跨层协同要求。其核心结论是：完整 RowHammer 防御不仅需要知道谁是 aggressor，还必须保证 DRAM 有时间刷新 victim rows。

## 硬件工程师学习提炼

1. Panopticon 适合用来比较 RowHammer 防御部署位置：controller-side vs in-DRAM。
2. 重点回看 Table I 状态开销、Figure 1/5 threshold bit、Figures 6-7 service queue 攻击和 ALERTn 必要性。
3. 工程关键是 DRAM 内部 counter mats 的面积/功耗/yield、ALERTn 协议语义、以及在低 RowHammer threshold 下的服务能力。
4. 与 DDR5 RFM/PRHT、Graphene/TWiCe/BlockHammer 一起读，可形成 RowHammer 防御设计谱系。
