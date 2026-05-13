# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 BEER 的摘要、背景、on-die ECC 问题、方法流程、SAT formulation 思想、真实 LPDDR4 实验、BEEP、结果、局限和硬件工程师视角。保留 BEER、BEEP、on-die ECC、parity-check matrix、SAT solver、miscorrection、retention error 等术语。

## Title

原文标题：Bit-Exact ECC Recovery (BEER): Determining DRAM On-Die ECC Functions by Exploiting Data-Retention Characteristics

中文标题：Bit-Exact ECC Recovery（BEER）：利用数据保持特性确定 DRAM on-die ECC 函数

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

随着 DRAM scaling，单 bit 错误更频繁。DRAM 厂商在芯片内部加入 on-die ECC，以提高良率和可靠性。但 on-die ECC 对系统不可见，具体 ECC function 通常是商业机密。系统只能观察经过 on-die ECC 修正后的 post-correction errors，看不到真实 pre-correction physical errors。

这种黑盒性阻碍可靠性研究和系统设计。若不知道 on-die ECC 如何把原始错误转换成可见错误，研究者很难准确建模 retention failures、RowHammer errors、data-dependent failures，也难以设计外部 ECC 和 RAS 策略。

本文提出 BEER，一种非侵入式恢复 DRAM on-die ECC parity-check matrix 的方法。BEER 利用 data-retention errors 的物理不对称性，诱导 ECC-function-specific miscorrections，并将观测到的 miscorrection profiles 编码为 SAT constraints，求解完整 ECC function。作者还提出 BEEP，在已知 ECC function 后，从 observed post-correction errors 推断 bit-exact pre-correction error locations。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

On-die ECC 是现代 DRAM scaling 的重要工具。它允许厂商在芯片内部纠正部分 cell errors，从而提高制造良率和运行可靠性。对系统来说，这看似是纯收益：外部看到的错误更少。

但 on-die ECC 也带来可观测性问题。系统无法读取 syndrome、parity bits 或 ECC metadata，也不知道 codeword 组织和 parity-check matrix。某些原始错误会被纠正而不可见；某些多 bit errors 可能被错误纠正成其它 bit 的 miscorrection；外部看到的错误位置不一定等于真实物理错误位置。

BEER 的目标是在不拆芯片、不访问内部 ECC metadata、不依赖厂商文档的情况下恢复 on-die ECC function。这对硬件可靠性研究非常关键，因为只有知道 ECC function，才能把 post-correction behavior 还原到 pre-correction physical error behavior。

## 2. Background: On-Die ECC and Retention Errors / 背景：on-die ECC 与保持错误

### 原文位置

Page 2 - Page 4

### 中文翻译

ECC 通常可以用 parity-check matrix 描述。对于 single-error-correcting（SEC）Hamming code，每个 bit position 对应 syndrome。若发生单 bit error，ECC 根据 syndrome 定位并修正。若发生多 bit errors，syndrome 可能对应另一个 bit，导致 miscorrection。

DRAM data-retention errors 具有物理方向性。某些 cells 倾向于从 charged 状态泄漏到 discharged 状态，而反向错误概率不同。通过写入精心选择的 data patterns 并暂停 refresh，可以诱导特定方向和位置的 retention errors。

BEER 利用这种 asymmetry。不同 ECC functions 在面对相同 pre-correction error pattern 时，会产生不同 post-correction miscorrection profile。通过大量观测这些 profile，可以反推 parity-check matrix。

## 3. BEER Overview / BEER 方法总览

### 原文位置

Page 4 - Page 6 / BEER design

### 中文翻译

BEER 大致分三步。

第一，构造 test patterns 并诱导 retention errors。作者写入 carefully crafted patterns，例如 {1,2}-CHARGED patterns，使某些 bit positions 更容易产生可控方向的 errors。

第二，收集 miscorrection observations。当 on-die ECC 面对多 bit pre-correction errors 时，可能把错误 syndrome 解释为另一个 bit 的单 bit error，从而翻转错误 bit，产生 post-correction error。不同 ECC function 会导致不同位置的 miscorrections。

第三，把观测结果转化为 SAT problem。Parity-check matrix 的未知 entries 是待求变量；ECC syndrome/miscorrection 关系形成约束。SAT solver 搜索满足所有观测约束的 matrix。如果约束足够，解唯一，即恢复 bit-exact ECC function。

这一思路的关键是把 DRAM 物理错误和编码理论结合起来。Retention errors 提供可控扰动，miscorrections 泄露 ECC 结构，SAT solver 完成组合搜索。

## 4. SAT Formulation / SAT 公式化思想

### 原文位置

Page 6 - Page 7 / Section 4

### 中文翻译

BEER 将 ECC parity-check matrix 的每一位视为布尔变量。给定一个假设的 pre-correction error pattern，ECC syndrome 是相关 columns 的 XOR。若 syndrome 指向某个 bit position，ECC 会翻转该 bit，形成 post-correction output。

实验观测给出“在某种 pattern 下出现/未出现某些 miscorrection”的约束。BEER 将这些逻辑关系编码成 SAT clauses。SAT solver 求解后得到一个或多个 candidate matrices。若只有一个 matrix 满足所有约束，就完成 bit-exact recovery。

这种方法计算成本高，但强大。它不要求直接观察 syndrome，也不要求知道 parity bits 位置。只要 miscorrection profile 足够丰富，就能约束出隐藏 ECC function。

## 5. Real-Chip Experiments / 真实芯片实验

### 原文位置

Page 7 - Page 8

### 中文翻译

作者在 80 颗真实 LPDDR4 DRAM chips 上应用 BEER，来自三家主要 DRAM vendors。实验显示，不同厂商似乎使用不同 ECC functions；同一厂商同型号芯片似乎使用相同 function。由于 ECC functions 属于厂商机密，论文不能公开具体矩阵。

真实芯片实验没有 ground truth，因此作者不能直接证明恢复结果与厂商内部实现完全一致。为增强可信度，论文结合仿真验证、SAT 唯一解和跨芯片一致性进行论证。

工程意义是，on-die ECC 的黑盒性不是绝对屏障。即便厂商不公开 ECC function，研究者仍可通过物理错误和外部行为推断内部编码结构。

## 6. Simulation Validation / 仿真验证

### 原文位置

Page 8 - Page 10 / Figures 5-6

### 中文翻译

为验证 BEER 正确性，作者在仿真中生成 115,300 个代表性 SEC Hamming codes，codeword length 覆盖 4 到 247 bits。BEER 对这些 codes 正确恢复 parity-check matrix。

论文还分析不同 test patterns 的约束能力。结果显示，{1,2}-CHARGED patterns 能唯一识别仿真中的 ECC function。这说明精心选择 data pattern 对降低搜索空间和提高唯一性很重要。

SAT solving 成本不低。对 128-bit representative codes，BEER median runtime/memory 为 57.1 hours / 6.3 GiB；对 247-bit codes，最多约 62 hours / 11.4 GiB。虽然这不适合在线系统运行，但对离线 reverse engineering 和研究工具可接受。

## 7. BEEP: Bit-Exact Error Profiling / BEEP：精确错误画像

### 原文位置

Page 10 - Page 12 / Figures 7-9

### 中文翻译

BEER 恢复 ECC function 后，作者进一步提出 BEEP。BEEP 的目标是从 observed post-correction errors 反推出 pre-correction errors 的 bit-exact locations。也就是说，它试图回答：外部看到这个错误后，芯片内部原始错误最可能发生在哪些 bits。

BEEP 利用已知 parity-check matrix 和 ECC correction behavior，对可能的 pre-correction error patterns 进行推断。论文通过 Monte Carlo simulation 分析不同 codeword length、error count 和 per-bit error probability 下的成功率。结果显示，对于更现实的 63/127-bit codeword，BEEP 可接近 100% success rate。

这对 DRAM error profiling 很重要。若只看 post-correction errors，研究者可能误判哪个 cell/row/bitline 更脆弱。BEEP 使 on-die ECC 后的错误分析更接近真实物理错误。

## 8. Implications / 启示

### 原文位置

Page 12 - Page 13 / Discussion

### 中文翻译

BEER/ BEEP 对多个领域有影响。对 reliability characterization，它让研究者能更准确评估 retention errors、RowHammer errors 和 data-dependent failures。对 ECC co-design，它帮助系统外部 ECC 理解 on-die ECC 后错误分布。对安全研究，它说明隐藏的 ECC function 可能被逆向，不能作为唯一安全边界。

对 DRAM vendors 来说，on-die ECC 提升良率，但也会改变外部错误可见性。若系统设计者不知道内部 ECC，可能错误配置 scrubbing、page retirement 或 Chipkill。更透明的 error reporting 或标准化 metadata 可能有助于系统级 RAS。

## 9. Limitations / 局限性

### 原文位置

Page 13 / Limitations

### 中文翻译

BEER 的局限包括：真实芯片没有 ground truth 可直接验证；恢复出的 ECC functions 因保密不能公开；方法依赖可诱导足够 retention errors；SAT solving 对更长 code 仍耗时；BEEP 当前主要展示 data-retention errors，对 RowHammer、read disturb、data-dependent errors 等其它故障模式还需扩展。

此外，厂商未来可能改变 ECC design、加入 interleaving、scrambling 或更复杂 correction scheme，使 BEER 需要调整。

## 10. Conclusion / 结论

### 原文位置

Conclusion

### 中文翻译

BEER 证明，DRAM on-die ECC function 可以通过非侵入式方法恢复。它利用 retention error asymmetry 和 ECC miscorrection 行为，将隐藏 ECC 结构转化为 SAT 求解问题。BEEP 进一步利用恢复的 ECC function 推断 pre-correction error locations。

本文的核心贡献是打破 on-die ECC 黑盒，使第三方能够更准确地理解现代 DRAM 的真实错误行为。

## 11. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文方法、实验和讨论的工程化解读

### 中文学习笔记

1. 对 RAS 设计：on-die ECC 会改变错误可见性。外部 ECC 和 page retirement 不能直接把 observed error 当作 physical error。

2. 对 DRAM validation：需要区分 pre-correction 和 post-correction error。BEER/BEEP 提供了恢复真实错误分布的研究路径。

3. 对安全：隐藏 ECC function 不能作为安全假设。攻击者可能通过 side behavior 逆向内部机制。

4. 对系统建模：RowHammer/retention 实验若使用带 on-die ECC 的 DRAM，必须考虑 ECC miscorrection 和 error masking。

5. 对行业：更透明的 ECC reporting 可能有助于云服务器和高可靠系统做正确 RAS 决策，但厂商商业机密和接口成本是阻力。

6. 对个人学习：这篇适合与 HARP、on-die ECC modeling、DRAM retention profiling 一起读。核心是理解 syndrome/miscorrection 如何泄露 hidden ECC。

## 12. 不确定与需回原文核对

- Page 6-7 SAT formulation 的具体变量和 clauses 建议回 PDF 核对。
- 真实 LPDDR4 ECC matrices 未公开，结果无法由读者直接复现验证。
- BEER 对不同 ECC 类型、interleaving 和未来 DDR5/LPDDR5 的适用性需进一步研究。
