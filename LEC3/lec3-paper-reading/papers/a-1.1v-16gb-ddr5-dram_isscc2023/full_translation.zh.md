# Full Chinese Translation

## Title

原文标题：A 1.1V 16Gb DDR5 DRAM with Probabilistic-Aggressor Tracking, Refresh-Management Functionality, Per-Row Hammer Tracking, a Multi-Step Precharge, and Core-Bias Modulation for Security and Reliability Enhancement

中文标题：一种 1.1V 16Gb DDR5 DRAM：面向安全与可靠性的概率 aggressor 跟踪、RFM、逐行 hammer 跟踪、多步预充电与 core-bias 调制

> 翻译说明：ISSCC 论文篇幅较短但信息密度很高。本文件按摘要、设计动机、RowHammer/retention 机制、硅片测量和工程启示进行高完整度详译/译述。图中电路细节建议回 PDF 核对。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

本文介绍一种 1.1V、16Gb DDR5 DRAM 芯片，目标是在先进工艺和高密度条件下增强安全性与可靠性。论文围绕 RowHammer 和 retention 两类关键问题提出多项机制：Probabilistic-Aggressor Tracking（PAT）用于以概率方式识别 aggressor rows；Refresh-Management Functionality（RFM）用于配合 DDR5 refresh 管理；Per-Row Hammer Tracking（PRHT）用于逐行跟踪 hammer 行为；multi-step precharge 用于提升行间隔离和 RowHammer 容忍度；core-bias modulation 通过调节 core bias 改善 retention。

硅片测量表明，这些技术显著降低 RowHammer failure probability，并提升 retention 特性。论文报告 RowHammer failure probability 降低约 93.1%，retention 改善约 17%；PRHT 和 multi-step precharge 分别提供额外可靠性收益；PAT 能在更低 intrinsic tolerance 条件下通过恶意 pattern 测试。

## 1. Motivation / 研究背景

### 原文位置
Page 1 / Introduction and motivation

### 中文翻译

随着 DRAM 单芯片容量增加、cell 尺寸缩小、wordline 间距变窄，传统可靠性裕量持续下降。DDR5 相比 DDR4 在速率、bank group、refresh 管理和系统容量上提出更高要求，同时 RowHammer 攻击也变得更实际。RowHammer 的本质是频繁激活 aggressor row 会扰动相邻 victim row 的电荷，造成 bit flip。工艺缩放后，victim row 更容易受到 coupling、leakage 和 disturbance 影响。

另一方面，retention failure 仍然是 DRAM 可靠性的基础问题。若 cell 保持电荷能力不足，在 refresh interval 内数据可能丢失。提高 refresh 频率可以改善 retention，但会增加功耗和性能开销。因此芯片需要在安全、可靠性、功耗和性能之间取得平衡。

本文的重要性在于，它不是单纯提出一个 architecture-level RowHammer 缓解算法，而是在真实 DDR5 silicon 中集成多种 circuit/architecture 协同机制。对硬件工程师来说，这类论文展示了真实产品中如何组合“检测、跟踪、刷新、预充电、电压调节”多种手段，而不是依赖单一理论方案。

## 2. Overall Design / 总体设计

### 原文位置
Page 1-2 / Chip architecture and feature overview

### 中文翻译

该芯片是 16Gb DDR5 DRAM，工作电压 1.1V。论文围绕安全与可靠性增强列出多个模块。RFM 是 DDR5 中用于 refresh management 的关键接口，使系统可以在检测到潜在 RowHammer 风险后触发额外管理动作。PAT 和 PRHT 用于识别或跟踪 aggressor 行。multi-step precharge 改变 precharge 过程，以降低相邻行扰动。core-bias modulation 调整核心阵列偏置，提高 retention margin。

这些机制可分成三类。第一类是 row activity tracking，用于判断哪些 row 被频繁激活。第二类是 mitigation action，用于对风险 row 或 victim row 做额外 refresh 或调整。第三类是 circuit-level margin enhancement，用于从物理层提高抗扰动能力。

这种分层组合符合实际 DRAM 产品设计逻辑：tracker 不可能无限大，refresh 不可能无限频繁，电路 margin 也不可能无限提高。因此可靠性增强需要概率策略、局部精确跟踪和电路改良共同作用。

## 3. Probabilistic-Aggressor Tracking / 概率 Aggressor 跟踪

### 原文位置
Page 2 / PAT description and measurement

### 中文翻译

PAT 的目标是在有限硬件开销下识别可能造成 RowHammer 的 aggressor rows。逐行精确计数所有 row activation 在大容量 DRAM 中成本很高，因此概率跟踪提供折中：它不保证记录每一次 activation，但通过概率采样和筛选，使高频 aggressor 更可能被捕获。

当系统识别到疑似 aggressor 后，可以通过 RFM 或内部 refresh 管理对相关 victim rows 采取保护动作。论文报告 PAT 能通过 50 种 malicious patterns，即使 intrinsic tolerance 降低 66% 也可保持防护能力。这说明 PAT 的设计目标不是追求理论上完全精确的计数，而是让攻击者难以通过多样化 pattern 逃避跟踪。

工程上，PAT 的关键问题包括随机性来源、计数器饱和策略、false positive/false negative、与命令时序路径的耦合，以及是否会影响 ACT/PRE/REF 的 critical timing。实际实现中 tracker 需要与 bank/subarray 结构匹配，否则面积和功耗可能快速上升。

## 4. Refresh-Management Functionality / RFM 刷新管理

### 原文位置
Page 2 / RFM related description

### 中文翻译

RFM 提供一种面向 RowHammer 的 refresh management 机制，使 DRAM 可以在普通周期性 refresh 之外执行风险管理。传统 refresh 主要面向 retention；RowHammer 需要根据 activation history 对特定 rows 进行更及时的保护。RFM 因此可被看作 DDR5 时代把 row activity 与 refresh policy 连接起来的接口。

在本文设计中，RFM 与 PAT/PRHT 等 tracker 协同：tracker 发现风险，RFM 触发或组织 mitigation。论文的贡献在于展示 RFM 不只是标准中抽象的命令能力，而可以和片内检测逻辑、victim refresh 策略以及电路增强机制形成完整闭环。

对系统设计而言，RFM 的价值是给 memory controller 和 DRAM 芯片之间提供更明确的可靠性协作通道。未来服务器平台中，RowHammer 防护很可能不是单纯 MC 侧算法或 DRAM 内部黑盒，而是通过标准化命令和 telemetry 共同完成。

## 5. Per-Row Hammer Tracking / 逐行 Hammer 跟踪

### 原文位置
Page 2-3 / PRHT figures and explanation

### 中文翻译

PRHT 进一步提高跟踪粒度，试图针对每个 row 的 hammer 风险进行监控。论文提到 PRHT 使用与 wordline 相关的 R/H cells 进行 tracking。与纯概率 PAT 相比，PRHT 更接近精确 per-row awareness，能够降低遗漏高风险 row 的概率。

硅片结果显示，PRHT 使 failure probability 降低约 90.5%。这说明逐行信息对 RowHammer 防护很有价值，但也意味着硬件要付出额外存储、感测和控制逻辑。真实产品中，PRHT 可能需要在 die area、yield、测试复杂度和可靠性收益之间做取舍。

从硬件工程角度，PRHT 最值得学习的是“把可靠性状态放在阵列附近”的思路。相比在 memory controller 中维护巨大 row table，阵列本地状态可能更接近扰动源，也更容易捕获实际物理行为。但这会增加 DRAM die 内部设计和验证复杂度。

## 6. Multi-Step Precharge / 多步预充电

### 原文位置
Page 3 / Multi-step precharge discussion

### 中文翻译

multi-step precharge 调整 DRAM precharge 过程，使 bitline/wordline 相关节点以更平滑或分阶段的方式回到目标状态。其目的在于减小相邻 row 的电气扰动，提高 RowHammer tolerance。

论文报告 multi-step precharge 可使 intrinsic RowHammer tolerance 提升约 37%。这属于 circuit-level mitigation，和 tracker-based mitigation 不同：它不依赖识别某个 aggressor，而是提高整个阵列对扰动的基础承受能力。

工程含义很直接：算法级 RowHammer 防护常常受 worst-case pattern 约束，而 circuit margin enhancement 能降低上层策略压力。但 multi-step precharge 可能影响 timing、能耗或 tRP/tRAS 相关参数，因此需要评估在不同 PVT corner 和高频 DDR5 操作下的代价。

## 7. Core-Bias Modulation and Retention / Core Bias 调制与保持时间

### 原文位置
Page 3 / Core-bias modulation and retention result

### 中文翻译

core-bias modulation 通过调节 DRAM core 的偏置条件改善 retention。Retention failure 与 cell leakage、sense margin、电容电荷保持能力相关；改变 bias 可以在一定程度上降低 leakage 或改善 sensing 条件，从而延长数据保持时间。

论文报告 retention 提升约 17%。这对 DDR5 很重要，因为高密度 DRAM 的 refresh power 和 refresh interference 会持续上升。若芯片能通过 bias modulation 提高 retention margin，就可以在不简单增加 refresh 频率的情况下改善可靠性。

对硬件工程师而言，这一机制提醒我们：内存可靠性不是只有数字控制逻辑，模拟/电路层参数同样关键。bias modulation 需要关注温度、电压、老化和 workload 相关行为，也会影响生产测试与 binning。

## 8. Silicon Results / 硅片测量结果

### 原文位置
Page 3-4 / Measurement figures and conclusion

### 中文翻译

论文基于 1a-nm 16Gb DDR5 silicon 进行测量。关键结果包括：整体 RowHammer failure probability 降低约 93.1%；PRHT 单独带来约 90.5% failure probability reduction；multi-step precharge 提升 intrinsic RowHammer tolerance 约 37%；core-bias modulation 改善 retention 约 17%；PAT 在 50 种 malicious patterns 下通过测试，并在 intrinsic tolerance 降低 66% 的条件下仍表现有效。

这些结果的组合说明，真实 DDR5 产品需要多层防护。PAT/PRHT 负责发现高风险访问，RFM 负责组织刷新管理，multi-step precharge 和 bias modulation 提升底层物理裕量。单独看任何一项都可能不足以覆盖所有攻击和工艺条件，但组合后可以形成更强防线。

## 9. Limitations and Engineering Questions / 局限与工程问题

### 原文位置
Page 4 / Discussion implied by results

### 中文翻译

ISSCC 论文通常篇幅有限，因此本文没有完整展开所有系统级影响。需要进一步确认的问题包括：这些机制对标准 DDR5 timing 的具体影响；PAT/PRHT 的面积、功耗和测试成本；RFM 与 memory controller policy 的接口细节；在温度、老化、电压 droop 和不同访问 pattern 下的 worst-case 行为。

另外，论文报告的是特定 16Gb DDR5 silicon 的结果。不同工艺节点、die density、vendor architecture 和 package 条件下，数值可能不同。对产品设计来说，应把本文看作“可行技术组合”的证据，而不是直接可移植的通用参数。

## 10. Conclusion / 结论

### 原文位置
Page 4 / Conclusion

### 中文翻译

本文展示了一种面向安全与可靠性增强的 16Gb DDR5 DRAM。通过 PAT、RFM、PRHT、multi-step precharge 和 core-bias modulation 的协同，芯片在 RowHammer 防护和 retention 方面取得显著改善。论文的核心价值是证明：先进 DRAM 的可靠性问题需要在标准接口、片内跟踪、电路时序和偏置控制多个层级同时解决。

## 硬件工程师学习提炼

1. RowHammer 防护已从“系统论文问题”变成真实 DDR5 silicon feature，阅读时要把 tracking、refresh command、array circuit 放在同一张图里理解。
2. PAT 与 PRHT 分别代表低成本概率检测和高粒度本地跟踪，适合用来比较 area/power/coverage 的工程取舍。
3. multi-step precharge 与 core-bias modulation 说明 circuit-level margin 仍然是可靠性设计的基础；不能只从 architecture policy 推导可靠性。
4. 复习时优先回 PDF 看 PAT/PRHT 结构图、failure probability measurement、multi-step precharge waveform 和 retention/bias 结果。
