# Full Chinese Translation

## 版权与完整性说明
本文基于可访问 PDF 的提取文本生成逐节中文详译/译述，覆盖论文所有主要部分。以下内容不进行逐字长篇翻译，而是按原文章节忠实转述，并保留关键英文术语。

## Title
原文标题：Spatial Variation-Aware Read Disturbance Defenses: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions

中文标题：空间变化感知的读扰动防护：真实 DRAM 芯片实验分析及其对未来方案的启示

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究 DRAM read disturbance vulnerability 的空间变化。作者在大量真实 DDR4 芯片上发现，同一芯片内部不同 row、subarray、bank 的 RowHammer 敏感性差异很大。基于这一现象，论文提出 Svärd：一种利用 row-level vulnerability profile 调整防护强度的方法。Svärd 可叠加到多种已有 RowHammer mitigation 上，在保持安全约束的同时降低性能开销。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言说明 RowHammer 防护越来越困难。随着 DRAM cell 缩小，触发 bitflip 所需 activation 数下降，系统必须更频繁地刷新或阻止潜在攻击访问。许多防护采用单一阈值：只要某个 row 的 activation count 接近 NRH，就采取刷新、限速或隔离措施。

作者指出，这种设计忽略了一个事实：不同 row 的脆弱性并不相同。若所有 row 都按最弱 row 保护，系统性能和能耗开销会增加；若按平均 row 保护，则弱 row 会暴露在攻击下。因此，空间变化既是风险，也是优化机会。

## 2. Background and Motivation / 背景与动机

### 原文位置
Page 2 - Page 4

### 中文翻译
背景部分介绍 RowHammer、read disturbance、NRH 以及常见防护机制。防护方案可以在 memory controller 中记录 activation count，也可以在 DRAM 内部实现概率刷新或 row tracking。无论机制如何，它们都需要决定什么时候触发保护。

作者用初步例子说明 spatial variation：如果某些 row 的 HCfirst 远高于最弱 row，那么对这些 row 采用同样保守的防护会浪费带宽和能量。这激励了 row-level profile 的思想。

## 3. Experimental Methodology / 实验方法

### 原文位置
Page 4 - Page 5

### 中文翻译
论文测试 144 颗 DDR4 chip，覆盖 10 种 chip design 和 3 家主要 DRAM 厂商。实验通过可控内存访问测量不同位置 row 的 bit error rate 和 HCfirst。作者关注多层空间粒度：module、chip、bank、subarray 和 row。

系统模拟部分使用多程序 memory-intensive workload，比较原始防护和加入 Svärd 后的性能。作者还构造 adversarial access pattern，以测试空间感知策略是否会被攻击者利用。

## 4. Characterization of Spatial Variation / 空间变化表征

### 原文位置
Page 5 - Page 9

### 中文翻译
表征结果显示，读扰动脆弱性在多个层级上变化。不同 chip 和 module 的总体脆弱性不同；同一 chip 内，不同 bank/subarray/row 也有显著差异。论文特别强调，同一 subarray 内部的 BER 可能相差约 2x，HCfirst 可能相差一个数量级。

作者进一步分析 row index、subarray 位置等特征是否能预测 vulnerability。结果并不理想：在 15 个被测试 module 中，只有 4 个显示出明显空间特征相关性。换句话说，空间变化存在，但它不总是呈现简单、可泛化的几何规律。

这一发现非常关键。它一方面支持利用 variation，另一方面否定了“只根据 row 位置猜测安全阈值”的简单方案。

## 5. Svärd Design / Svärd 设计

### 原文位置
Page 10 - Page 12

### 中文翻译
Svärd 的核心思想是：先获得 row-level 或 row-group-level vulnerability profile，然后根据每个 row 的脆弱性调整防护 aggressive 程度。弱 row 使用更严格阈值或更频繁刷新；强 row 则允许更宽松策略，从而减少不必要保护。

Svärd 并不替代具体防护机制，而是作为一个 spatial variation-aware layer。作者把它与 AQUA、BlockHammer、Hydra、PARA 和 RRS 结合，说明 profile 可以影响不同类型防护：计数型、概率型、限速型或刷新型。

设计上必须保证安全。即使大多数 row 较强，攻击者也可能专门访问最弱 row。因此 Svärd 不能简单降低全局防护强度，而要确保每个 row 都满足自己的安全 margin。

## 6. Evaluation / 评估

### 原文位置
Page 13 - Page 16

### 中文翻译
性能评估显示，加入 Svärd 后多种防护的性能开销下降。论文报告在 120 个 multiprogrammed memory-intensive workload 上，相对于原防护，Svärd+AQUA、Svärd+BlockHammer、Svärd+Hydra、Svärd+PARA、Svärd+RRS 分别获得 1.23x、2.65x、1.03x、1.57x、2.76x 平均性能改善。

这些收益来源于强 row 不再被最坏情况 row 拖累。尤其当原防护开销高、触发保护频繁时，空间感知策略带来的收益更明显。Hydra 的改善较小，说明某些防护本身开销结构不同，留给 Svärd 优化的空间有限。

对 adversarial pattern 的评估提醒读者：空间感知不是单纯性能优化。攻击者可以瞄准最弱 row，因此防护必须保留 per-row 安全约束。Figure 13 展示了在攻击访问下的行为差异。

## 7. Discussion / 讨论

### 原文位置
Page 16 - Page 17

### 中文翻译
讨论部分集中在 profile 的成本和稳定性。要部署 Svärd，系统需要知道 row-level vulnerability。这个 profile 可以来自制造测试、启动时测试、后台测试或运行时监测。但 RowHammer vulnerability 可能随温度、电压、老化和时间变化改变，因此 profile 需要更新或留出 guardband。

作者还强调，本文并不声称一个固定 profile 能永久保证安全。更现实的方向是让防护机制能够利用 profile，同时也能在不确定时退回保守策略。

## 8. Conclusion / 结论

### 原文位置
Page 17 - Page 18

### 中文翻译
论文结论是：真实 DRAM 芯片中的 read disturbance vulnerability 具有显著空间变化。利用这种变化可以显著降低 RowHammer mitigation 的性能开销，但前提是基于真实测量 profile，并保持对最弱 row 的安全保证。Svärd 证明了 spatial variation-aware defense 是未来低开销安全 DRAM 的可行方向。
