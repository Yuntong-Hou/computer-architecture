# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 VRD 的摘要、背景、实验方法、主要发现、guardband/ECC 分析、对现有 RowHammer 防护的影响和硬件工程师视角。保留 Variable Read Disturbance、VRD、RDT、NRH、RowHammer、RowPress、guardband、ECC 等关键英文术语。参考文献保留英文。

## Title

原文标题：Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance

中文标题：可变读扰动：DRAM 读扰动时间变化的实验分析

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

许多 RowHammer/read disturbance 防护都依赖一个关键假设：某个 row 或某颗芯片的 read disturbance threshold 可以通过 profiling 得到，并在后续使用中保持稳定。本文通过大规模真实芯片实验挑战这一假设。作者提出 Variable Read Disturbance（VRD），即同一 DRAM row 的 read disturbance threshold 会随时间发生显著变化，而且这种变化不容易通过少量测量预测。

论文测试 160 颗 DDR4 chips 和 4 颗 HBM2 chips，覆盖三家主要 DRAM 厂商。结果显示，绝大多数 rows 都表现出 VRD。某些 row 的最低 read disturbance threshold（RDT）需要在数万次重复测量后才出现；同一 row 的最小 RDT 可能比最大观测 RDT 小 3.5x。若系统只进行一次或少量 profiling，就可能高估该 row 的安全余量。

作者进一步分析 guardband 和 ECC 是否能缓解 VRD。结论是，它们可以降低风险，但不能单独构成稳健解决方案。较大 guardband 会带来明显性能开销，ECC 则受 error distribution 和 correction capability 限制。论文最终呼吁在线 RDT profiling、runtime-configurable mitigation 和能容忍阈值不确定性的防护机制。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 3

### 中文翻译

RowHammer 防护通常围绕 NRH/RDT 这类阈值设计。若一个 aggressor row 在 N 次 activation 内不会让 victim row 出错，那么系统可以在接近 N 之前触发刷新、节流或其它防护。很多 profile-based defenses，包括 spatial variation-aware defenses，都隐含假设：测得的阈值可以代表未来行为。

本文指出，这个假设可能不成立。DRAM cells 的易扰动程度不仅随空间位置变化，也会随时间变化。一个 row 今天或此刻测得的 RDT，不一定等于稍后或重复测量中的最低 RDT。如果最低 RDT 偶尔出现，攻击者或 worst-case workload 可能恰好利用这个低谷，而系统防护参数仍基于较高 profile。

论文用 Figure 1 直观展示：单次测量只能在一部分 rows 中捕获 1000 次测量范围内的最小 RDT。很多 rows 需要大量重复测量才能观察到真正低阈值。这说明“一次测试通过”并不能证明长期安全。

对硬件工程师来说，引言的核心是：RowHammer threshold 不是一个静态常数，而更像一个随时间、环境和器件状态变化的随机变量。防护设计必须从 static guardband 转向 dynamic uncertainty management。

## 2. Background / 背景

### 原文位置

Page 2 - Page 4 / Background

### 中文翻译

Read disturbance 是 DRAM row activation 对邻近 cells 造成干扰的现象。RowHammer 关注高频 activation，RowPress 关注长 row-open time。两者都会降低 victim cell 的电荷安全余量，导致 bit flip。

RDT 表示触发 bit flip 所需的 read disturbance 次数或相关访问次数。NRH 是 RowHammer 防护中常用的安全阈值。防护机制通常假设当 activation count 接近 NRH 时必须介入。如果 NRH 估计偏高，系统可能在 bit flip 后才介入；如果估计偏低，系统虽然安全但开销高。

已有研究强调 spatial variation，即不同 rows/chips/banks 的阈值不同。本文强调 temporal variation，即同一 row 在不同时间或重复实验中的阈值也会变化。VRD 与 spatial variation 互补，共同说明 DRAM read disturbance 不是单一全局参数可以描述的现象。

## 3. Experimental Methodology / 实验方法

### 原文位置

Page 4 - Page 6 / Methodology and Algorithm 1

### 中文翻译

作者对同一 row 反复测量 RDT。每次测量中，先写入特定 data pattern，然后对 aggressor rows 执行 hammering 或 read disturbance 操作，逐步增加 activation 数，直到 victim row 出现 bit flip。记录该次测量的 RDT 后，重复这一过程，形成同一 row 的 RDT 时间序列。

实验覆盖 160 颗 DDR4 chips 和 4 颗 HBM2 chips，来自三家主要 DRAM vendors。作者改变 data pattern、tAggON、温度、芯片密度和工艺节点等参数，观察 VRD 是否普遍存在。评估指标包括最小 RDT、最大 RDT、min/max ratio、发现最小 RDT 所需测量次数，以及 guardband/ECC 在不同不确定性下的效果。

论文特别关注“如果只测一次或少量次数，会错过多少风险”。这比简单报告平均 RDT 更贴近真实产品，因为量产测试和系统启动测试通常不可能对每个 row 做无限次 profiling。

## 4. Finding 1: RDT Varies Over Time / 发现一：RDT 随时间变化

### 原文位置

Page 5 - Page 7 / Findings and Figure 1

### 中文翻译

实验显示，同一 row 的 RDT 会在重复测量中显著变化。某些测量中，该 row 需要很多 activations 才出错；另一些测量中，它在更低 activation count 下就出错。作者称这种现象为 Variable Read Disturbance（VRD）。

一个关键结果是，单次测量只能在 22.4% rows 中得到 1000 次测量范围内的最低 RDT。换言之，对大多数 rows 来说，一次 profiling 很可能没有捕获最坏情况。

更严重的是，某些 row 的最低 RDT 出现得非常晚。论文报告最极端情况下，需要到第 94,467 次测量才观察到最低值。虽然对一个 RDT=1000 的 row 测这么多次可能只需约 9.5 秒，但对完整 bank 做同等级别 profiling 可能需要约 29 天。这说明穷尽式 profiling 在系统规模上不可行。

## 5. Finding 2: Magnitude of Variation / 发现二：变化幅度

### 原文位置

Page 6 - Page 8

### 中文翻译

VRD 不只是微小噪声。论文发现，同一 row 的最小 RDT 可比最大观测 RDT 小 3.5x。这意味着如果系统恰好在高 RDT 时完成 profiling，就可能设置过于乐观的防护阈值；当该 row 后续进入低 RDT 状态时，系统会暴露在 bit flip 风险下。

这种变化幅度对 guardband 设计很关键。若 min/max ratio 达到 3.5x，小 guardband 不能覆盖；但若为所有 rows 使用足够大的 guardband，性能和能耗开销会非常高。

工程直觉是，VRD 类似 retention time 中的 Variable Retention Time（VRT）：cell 行为可能随时间进入不同状态。对 reliability signoff 来说，必须考虑低概率但高影响的 worst-case state。

## 6. Finding 3: Prevalence Across Devices and Parameters / 发现三：跨器件和参数的普遍性

### 原文位置

Page 7 - Page 9

### 中文翻译

论文报告，97.1% 的测试 rows 在所有参数组合下表现出 VRD，其余 2.9% 至少在一个参数组合下表现出 VRD。这表明 VRD 不是个别芯片或个别厂商的异常，而是广泛存在于真实 DRAM 的现象。

作者还在 DDR4 和 HBM2 上观察到 VRD，说明它可能不仅限于传统 DIMM。不同 data pattern、tAggON 和温度会影响 RDT 和 VRD 表现，但不能消除时间变化。

对行业而言，这个结果直接挑战静态 profile-based defense。即便某个方案能准确测量 spatial variation，如果它假设 profile 长期稳定，也可能在 VRD 下失效。

## 7. Guardband Analysis / Guardband 分析

### 原文位置

Page 14 - Page 16

### 中文翻译

一种直观缓解方式是使用 guardband：将测得 RDT 乘以安全系数，使用更低阈值触发防护。例如，如果测得某 row RDT 为 X，系统可以按 0.9X、0.5X 等更保守阈值配置。

论文发现，小 guardband 能降低部分风险，但无法覆盖所有 VRD。更大 guardband 可以提高安全性，但性能成本迅速增加。作者报告 50% guardband 可能带来约 45% 性能损失。这说明简单扩大安全余量不是可扩展方案。

工程上，guardband 的问题是把不确定性转化为固定开销。对高带宽、低延迟系统来说，大 guardband 会导致频繁刷新、节流或 RFM，影响吞吐和能耗。更好的方向是动态检测和局部调整，而不是全局保守。

## 8. ECC Analysis / ECC 分析

### 原文位置

Page 14 - Page 16

### 中文翻译

ECC 可以纠正一定数量 bit errors，因此看似能缓解 VRD。论文分析 SECDED、Chipkill-like SSC 等方案，指出 ECC 可以降低因少量 bit flips 造成的数据错误，但不能替代 RowHammer 防护。

原因有三。第一，VRD 可能导致更低阈值和更多 bit flips，超过 ECC 能力。第二，bit flips 在 ECC word 中的聚集程度决定修复能力，单看总错误数不够。第三，on-die ECC 可能隐藏原始错误，使系统更难感知真实 disturbance 状态。

因此，ECC 应作为 defense-in-depth 的一层，而不是唯一防护。系统仍需减少 bit flips 发生概率，并记录 corrected error telemetry，用于动态调节防护策略。

## 9. Implications for Existing Defenses / 对现有防护的影响

### 原文位置

Page 16 - Page 17 / Implications

### 中文翻译

VRD 对多类防护提出挑战。对于 Svärd 这类 spatial profile-based defense，VRD 意味着 profile 需要随时间更新；只在制造阶段或启动阶段测一次可能不够。对于 PRAC/Chronus 这类基于 NRH 配置的工业方案，VRD 意味着 NRH 不能只取某次 characterization 的结果，而要覆盖时间变化下的低谷。

对于 memory-controller tracking 方案，VRD 要求阈值和刷新策略可 runtime reconfigurable。对于 DRAM 内部 TRR，若厂商内部阈值固定，也可能在 VRD 下出现未覆盖窗口。

论文呼吁在线 RDT profiling、dynamic mitigation 和 uncertainty-aware design。未来防护可能需要结合 ECC telemetry、temperature sensors、error scrubbing、row-level counters 和 periodic re-profiling。

## 10. Conclusion / 结论

### 原文位置

Conclusion

### 中文翻译

本文提出 Variable Read Disturbance，并通过 160 颗 DDR4 和 4 颗 HBM2 chips 的实验表明，同一 DRAM row 的 read disturbance threshold 会随时间显著变化。最低 RDT 可能需要大量重复测量才能观察到，且最小值可比最大观测值低很多。

这一发现说明，RowHammer 防护不能只依赖一次或少量 profiling。未来系统需要在线测量、动态配置和能容忍阈值不确定性的防护机制。Guardband 和 ECC 有帮助，但单独使用会面临安全不足或开销过高的问题。

## 11. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文实验和 implications 的工程化解读

### 中文学习笔记

1. 对 DRAM validation：RowHammer 测试不能只跑一次 threshold sweep。需要重复测量，统计尾部分布和最晚出现的低 RDT。

2. 对 controller/firmware：防护阈值应支持 runtime update。固定 BIOS table 或一次性 vendor profile 不足以覆盖 VRD。

3. 对 RAS：corrected error telemetry 可以作为在线 profile 信号。系统应把 ECC 纠错事件与 row/bank/channel 关联起来，驱动动态防护。

4. 对标准：PRAC/Chronus 类机制需要考虑 NRH uncertainty，而不是假设一个静态标准阈值。

5. 对行业：VRD 会增加量产测试压力。完整 row-level profiling 成本极高，因此需要抽样、在线学习和保守默认策略组合。

6. 对个人学习：把 VRD 与 Svärd 对照看。Svärd 解决空间差异，VRD 说明时间差异会让静态空间 profile 失效。

## 12. 不确定与需回原文核对

- Figure 1 和 guardband/ECC 图中的具体数值建议回 PDF 核对。
- VRD 的物理根因仍需进一步研究，可能与 charge trapping、噪声、温度、电压、VRT 类行为相关。
- DDR5/LPDDR5 和长期老化场景仍需后续实验。
