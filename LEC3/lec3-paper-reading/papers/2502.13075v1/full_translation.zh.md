# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述，覆盖全文主要内容。为避免未经授权的逐字全文翻译，本文采用忠实转述；关键术语和指标保留英文。

## Title
原文标题：Variable Read Disturbance: An Experimental Analysis of Temporal Variation in DRAM Read Disturbance

中文标题：可变读扰动：DRAM 读扰动时间变化的实验分析

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文提出 Variable Read Disturbance（VRD）：同一 DRAM row 的 read disturbance threshold 会随时间变化。作者在 160 颗 DDR4 和 4 颗 HBM2 芯片上反复测量 RDT，发现最低阈值可能在大量重复实验后才出现，且一次或少数几次 profile 很可能高估安全性。这一现象对 RowHammer 防护、guardband 和 ECC 都有重要影响。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言从 RowHammer 防护依赖阈值开始。大多数防护都需要知道某个安全阈值：在达到这个 activation count 前必须刷新、限速或采取保护。若阈值稳定，profile 可以在制造、启动或维护期间完成；若阈值随时间波动，系统就可能在实际运行中遇到比 profile 更弱的状态。

作者用 Figure 1 展示同一 row 的 RDT 序列：多次测量得到的阈值并不相同，最低值可能很晚才出现。这说明 RowHammer vulnerability 具有 temporal variation，而不仅是 chip-to-chip 或 row-to-row spatial variation。

## 2. Background and Definitions / 背景与定义

### 原文位置
Page 3 - Page 4

### 中文翻译
论文定义 RDT（Read Disturbance Threshold）为触发 read disturbance bitflip 所需访问/activation 数。RDT 越低，row 越脆弱。VRD 则指同一 row 在不同时间或重复测量中的 RDT 变化。

作者区分 spatial variation 与 temporal variation。前者表示不同位置 row 的差异；后者表示同一 row 的状态随时间变化。两者会叠加，使防护设计更复杂。

## 3. Methodology / 方法

### 原文位置
Page 4 - Page 6; Algorithm 1

### 中文翻译
实验方法是对同一 row 重复执行 read disturbance 测试，并记录每次触发第一个 bitflip 的 RDT。Algorithm 1 描述了重复测量过程：初始化数据 pattern，施加访问序列，检查 victim row，记录阈值，然后重复。

实验覆盖 160 颗 DDR4 和 4 颗 HBM2 芯片，来自 3 家厂商。作者改变 data pattern、tAggON、温度等参数，以观察 VRD 是否受这些条件影响。

## 4. Main Findings / 主要发现

### 原文位置
Page 6 - Page 12

### 中文翻译
第一项发现是，少量测量不足以发现最低 RDT。论文报告，在 1000 次测量范围内，单次测量只对 22.4% 的 row 命中最低 RDT。对某些 row，最低 RDT 需要数万次重复才出现；最高例子是第 94,467 次测量才观察到最低值。

第二项发现是，同一 row 的 RDT 波动幅度很大。最小 RDT 可比最大观测 RDT 小 3.5x。这意味着如果系统根据某次较高 RDT 设置阈值，实际运行中可能遇到远低于 profile 的危险状态。

第三项发现是，VRD 非常普遍。97.1% 测试 row 在所有参数组合下都表现出 VRD，其余 2.9% 至少在一个参数组合下表现出 VRD。这说明 VRD 不是少数异常样本，而是广泛存在的现象。

第四项发现是，VRD 与参数相关。data pattern、tAggON、温度和工艺/密度都会影响 RDT 分布。更先进或更高密度的芯片可能表现出更严重的变化趋势，这与 DRAM scaling 下 cell margin 缩小相一致。

## 5. Implications for Profiling and Mitigation / 对 profiling 与防护的启示

### 原文位置
Page 12 - Page 14

### 中文翻译
VRD 对 profile-based defense 构成挑战。若系统只做一次或少数几次测量，很可能错过真实最小 RDT。即使大规模 profiling，也可能因为测试时间和能耗过高而难以覆盖所有 row。

作者估算，对于 RDT=1000 的单个 row，94,467 次测量约需 9.5 秒；但若扩展到一个包含 256K row 的 bank，完整测试可能需要约 29 天。这说明制造或启动时完全 profile 所有 row 很难实际部署。

## 6. Guardband and ECC / Guardband 与 ECC

### 原文位置
Page 14 - Page 16

### 中文翻译
一个自然想法是使用 guardband，即把测得的 RDT 再降低一定比例作为防护阈值。论文分析表明，guardband 可以降低风险，但很难在安全和性能之间取得稳定平衡。10% guardband 结合 SECDED 或 Chipkill-like SSC 在某些场景可缓解问题，但不能保证所有情况安全。

更大的 guardband 会带来高性能成本。论文指出 50% guardband 可能造成约 45% 性能损失，而 10% guardband 的开销约 5.9%。因此，单纯依靠大 guardband 会让系统难以接受。

## 7. Discussion / 讨论

### 原文位置
Page 16 - Page 17

### 中文翻译
作者认为未来防护需要 online RDT profiling 和 runtime-configurable mitigation。系统应能在运行时观察或估计 vulnerability 变化，并动态调整 refresh、throttling 或 tracking 参数。

VRD 还说明，安全分析不能只依赖某个固定 NRH。对于 PRAC、Chronus、Svärd 或任何 profile-based defense，都需要考虑阈值随时间降低的可能性。

## 8. Conclusion / 结论

### 原文位置
Page 17

### 中文翻译
本文结论是：DRAM read disturbance threshold 会随时间显著变化，且这种现象广泛存在。少量 profiling 会高估安全性，完整 profiling 又成本极高。未来 DRAM 防护必须能处理 temporal variation，不能把 RDT/NRH 当作静态常数。
