# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：Bit-Exact ECC Recovery (BEER): Determining DRAM On-Die ECC Functions by Exploiting DRAM Data Retention Characteristics

中文标题：Bit-Exact ECC Recovery（BEER）：利用 DRAM 数据保持特性确定片上 ECC 函数

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
现代 DRAM 使用 on-die ECC 来提升良率，但 ECC function 被隐藏在芯片内部。BEER 通过非侵入方式诱导 data-retention errors，并观察 ECC 在 uncorrectable patterns 下产生的 miscorrections，从而恢复完整 parity-check matrix。作者在真实 LPDDR4 chips 和大规模仿真中验证该方法，并提出 BEEP 用已知 ECC function 反推不可见的 raw bit errors。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
随着 DRAM cell 缩小，随机单 bit errors 更频繁，厂商使用 on-die ECC 在芯片内部静默纠正错误。问题是，外部系统只能看到 ECC 纠正后的结果，不能看到 syndrome、parity 或被纠正的 raw error。

作者指出，仅知道 ECC 是某种 Hamming SEC code 不够，因为同类型 code 可有许多 parity-check matrix。不同 ECC functions 会把相同 raw error pattern 转换成不同 post-correction error distribution。Figure 1 正是这一点的直观展示。

## 2. Challenges of Unknown On-Die ECCs / 未知片上 ECC 的挑战

### 原文位置
Page 3 - Page 4

### 中文翻译
on-die ECC 被厂商视为商业机密。第三方用户包括系统设计者、大规模系统供应商、测试工程师和研究者。他们需要理解 DRAM 的真实可靠性，但 on-die ECC 会掩盖物理错误位置和数量。

未知 ECC function 会影响二级 ECC 设计、测试 pattern 构造、空间错误分布分析和故障诊断。BEER 的目标是恢复完整 ECC function，使这些分析能够从 post-correction 观测回推 pre-correction 行为。

## 3. Background / 背景

### 原文位置
Page 4 - Page 5

### 中文翻译
论文介绍 data-retention errors、on-die ECC、Hamming code 和 SAT solver。data-retention errors 对 data pattern 敏感，某些 cell 状态更容易从 CHARGED 变为 DISCHARGED。ECC 在错误数量超过纠错能力时可能 miscorrect，即翻转一个本来没有错的 bit。

SAT solver 用于求解布尔约束。BEER 将“某个 unknown parity-check matrix 会导致 observed miscorrection profile”表达成 SAT problem。

## 4. BEER Methodology / BEER 方法

### 原文位置
Page 5 - Page 7

### 中文翻译
BEER 首先写入精心设计的 test patterns，并延长 refresh window 诱导 data-retention errors。通过控制 CHARGED cells 的位置，BEER 让特定 uncorrectable patterns 更可能出现。

随后，BEER 观察哪些 bit positions 出现 miscorrections。每个 miscorrection 都揭示了 syndrome 与 parity-check matrix 的关系。最后，BEER 把这些关系编码成 SAT constraints，求解唯一 parity-check matrix。

## 5. Real DRAM Experiments / 真实 DRAM 实验

### 原文位置
Page 7 - Page 8

### 中文翻译
作者在 80 颗 LPDDR4 chips 上应用 BEER。结果表明不同厂商似乎使用不同 ECC functions，而相同厂商和型号的芯片似乎使用相同 function。由于厂商保密，作者无法获得 ground truth，也不能公开最终恢复的矩阵。

实验噪声通过阈值过滤缓解；BEER 不要求每次观测都完美，只需要 miscorrection profile 足够稳定。

## 6. Simulation and Performance Evaluation / 仿真与性能评估

### 原文位置
Page 8 - Page 10

### 中文翻译
为了弥补真实芯片缺少 ground truth 的问题，作者用 EINSim 对 115,300 个代表性 SEC Hamming codes 做仿真。BEER 能正确恢复这些 code 的 ECC function，codeword length 覆盖 4 到 247 bits。

性能方面，SAT solving 是主要成本。短 code 几乎无压力，128-bit representative code 的 median runtime/memory 为 57.1 hours/6.3 GiB，247-bit code 最多约 62 hours/11.4 GiB。作者认为这是离线一次性任务，因此实际可接受。

## 7. BEEP and Use Cases / BEEP 与应用

### 原文位置
Page 10 - Page 13

### 中文翻译
BEEP 是 BEER 的具体应用：已知 ECC function 后，它可以从 observed post-correction miscorrections 推断 pre-correction raw errors 的数量和 bit-exact locations。BEEP 也使用 SAT solver 构造 test patterns，以便逐 bit 识别 error-prone cells。

仿真结果显示，对较现实的 63-bit 和 127-bit codeword，BEEP 成功率接近 100%，尤其在 error count 和 per-bit error probability 足够高时表现更好。作者还讨论 BEER 可帮助设计二级 ECC、构造 targeted test patterns、研究 spatial error distributions 和诊断 post-correction errors。

## 8. Related Work / 相关工作

### 原文位置
Page 13

### 中文翻译
相关工作包括 on-die ECC characterization、rank-level ECC reverse engineering 和 DRAM error profiling。作者强调 BEER 的不同点是：不需要访问 encoded data、syndrome、纠错事件信号或硬件修改，就能从外部接口观测恢复完整 ECC function。

## 9. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
BEER 证明第三方可以非侵入地恢复 DRAM on-die ECC function。BEEP 进一步说明，一旦知道 ECC function，就能恢复 raw error locations。该工作为带 on-die ECC 的现代 DRAM 可靠性研究和系统设计提供了重要工具。
