# Full Chinese Translation

## 版权与完整性说明
本文基于已下载 PDF 的可提取文本生成逐节中文详译/译述，覆盖摘要、背景、方法、实验、结果、讨论和结论。为避免对版权论文做大段逐字翻译，以下内容采用忠实转述方式，不复制英文长段；公式、指标、数据集、模型名和专有术语保留英文。

## Title
原文标题：Read Disturbance in High Bandwidth Memory: A Detailed Experimental Study on HBM2 DRAM Chips

中文标题：高带宽内存中的读扰动：对 HBM2 DRAM 芯片的详细实验研究

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文研究 HBM2 DRAM 中的 read disturbance。作者指出，RowHammer 已经在多代 DDR DRAM 中被证实，但 HBM2 由于 3D stacked 结构、高带宽接口和较少公开可控测试平台，仍缺少细粒度实验理解。论文在真实 HBM2 芯片上测量 RowHammer 与 RowPress，发现所有被测芯片都可出现 bitflip，且脆弱性具有明显空间差异。作者进一步发现，延长 aggressor row 的开启时间 tAggON 会大幅降低触发 bitflip 所需 activation 数，并揭示 HBM2 芯片中存在未公开的 read disturbance 防护机制，但这种机制可以被特定访问模式绕过。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
引言首先说明 HBM2 的重要性：许多 GPU、FPGA 和高性能加速器系统依赖 HBM2 来提供远高于传统 DDR 的内存带宽。随着 HBM2 被用于云端、AI、HPC 和多租户平台，其可靠性和安全性不再只是器件层问题，而会影响系统隔离和服务可用性。

作者回顾 RowHammer：重复激活一个或多个 aggressor row 会干扰相邻 victim row 中的电荷，导致 bitflip。以往研究主要关注 DDR3、DDR4、LPDDR 和部分 GDDR/commodity DRAM。HBM2 的内部结构不同，包括多个 channel、pseudo-channel、bank 和 3D 堆叠，因此 DDR 上的结论不能直接外推。

论文还把 RowPress 纳入研究。RowPress 的关键不是简单增加 activation 次数，而是让 aggressor row 保持开启较长时间。这个维度对 HBM2 尤其重要，因为高性能内存控制器可能采用 open-page policy 或产生长 row-open 行为。

## 2. Background / 背景

### 原文位置
Page 2 - Page 3

### 中文翻译
背景部分介绍 HBM2 的组织结构。HBM2 通过 stacked DRAM dies 和宽 I/O 接口提供高带宽。每个 stack 被划分为多个 channel，每个 channel 又可包含 pseudo-channel 和多个 bank。这样的结构意味着 read disturbance 的空间位置不只是 row number，还包括 channel、pseudo-channel、bank 和 die/stack 相关因素。

作者还解释 RowHammer 与防护机制。现代 DRAM 往往实现 TRR-like 机制，即在芯片内部跟踪激活次数较多的 row，并刷新潜在 victim row。但这些机制通常未公开，系统软件和研究者很难知道其阈值、追踪粒度和绕过条件。

## 3. Methodology / 方法

### 原文位置
Page 3 - Page 4

### 中文翻译
实验使用 FPGA-based HBM2 平台生成精确的访问序列。作者可以控制 aggressor row、victim row、activation 数、row-open 时间 tAggON 和 dummy row 插入方式。主要测量指标包括 bitflip 数、bit error rate、HCfirst 以及不同空间位置上的分布。

为了研究 RowHammer，作者施加大量 activation 并检查 victim row 是否出现 bitflip。为了研究 RowPress，作者固定或改变 row-open 时间，并观察较长 tAggON 是否降低 HCfirst。为了推断内部防护机制，作者构造不同 hammer/dummy-row pattern，观察 bitflip 是否被抑制或重新出现。

## 4. RowHammer Characterization / RowHammer 表征

### 原文位置
Page 4 - Page 8

### 中文翻译
作者首先展示 6 颗 HBM2 芯片的总体 bitflip 与 HCfirst 分布。结果说明所有芯片都可产生 RowHammer bitflip，但不同芯片间差异明显。有些芯片表现出更低 HCfirst 或更高 bit error rate，说明制造差异和芯片内部组织对扰动敏感性有影响。

随后，论文按 channel、pseudo-channel、bank 和 row 位置分析空间变化。结果显示，即使在同一颗 HBM2 chip 内，不同组件也可能表现出不同脆弱性。特别是 bank 中不同 row segment 的结果不均匀，bank 中间或末端的 row 相对更抗扰动。

作者还分析前 10 个 bitflip 的出现过程。一个重要观察是：触发第一个 bitflip 所需 hammer count 高，并不意味着后续 bitflip 也同样困难。许多 row 在第一个 bitflip 后，后续 bitflip 需要的额外 hammer 数下降。这意味着只用 HCfirst 评价安全性可能不足，因为攻击者关心的往往是多 bit 错误或特定 ECC word 中的错误组合。

## 5. RowPress Characterization / RowPress 表征

### 原文位置
Page 9 - Page 10

### 中文翻译
RowPress 实验改变 aggressor row 保持开启的时间 tAggON。结果非常显著：当 tAggON 从常规纳秒级提升到微秒级时，触发第一个 bitflip 所需 activation 数大幅下降。论文报告 tAggON=35.1us 时平均 HCfirst 比 29ns 设置小约 222.57x。

更极端地，作者发现当 row 保持 open 16ms 时，单次 activation 也可能导致 bitflip。这个结果说明 read disturbance 的根本原因不只是激活次数，还与 row 被打开期间相邻电路受到的持续电气压力有关。对系统而言，这意味着防护需要考虑 row-open duration，而不是只统计 ACT 命令。

## 6. Undocumented In-DRAM Defense / 未公开片内防护

### 原文位置
Page 10 - Page 11

### 中文翻译
通过构造不同 dummy row 和 aggressor 访问序列，作者推断某些 HBM2 芯片中存在未公开的 TRR-like 防护。该机制似乎会根据 activation count 跟踪高频访问 row，并触发针对相邻 victim 的保护刷新。

不过，这种防护并不完整。作者展示特定访问模式可以影响 tracking 行为，使真实 aggressor 不再被充分保护，从而重新诱发 bitflip。该结果与 DDR4 上 TRRespass 等工作相呼应：只要防护机制黑盒且资源有限，就可能被自适应访问序列绕过。

## 7. ECC Implications / ECC 影响

### 原文位置
Page 12, Figure 17

### 中文翻译
论文分析 bitflip 在 ECC word 中的分布。结果表明，某些扰动模式可能在同一 ECC word 中产生多个错误，或以不利方式跨 ECC word 分布。对系统设计来说，这意味着不能仅依赖“有 ECC”这一事实判断安全；需要知道 ECC granularity、correction capability、on-die ECC 与外部 ECC 的组合方式。

## 8. Discussion / 讨论

### 原文位置
Page 12 - Page 14

### 中文翻译
讨论部分强调 HBM2 读扰动对未来系统的含义。HBM 被越来越多地用于加速器和共享平台，攻击者可能不需要直接访问 DRAM 命令接口，只要能诱导特定内存访问模式，就可能增加扰动风险。RowPress 进一步扩大风险面，因为它把 memory controller policy、row buffer 行为和 read disturbance 连接起来。

作者建议未来防护需要同时考虑空间差异、row-open 时间、ECC 组织和片内防护可验证性。公开实验基础设施和数据有助于避免每篇论文都重新构建测试平台，也能让工业界和学术界比较不同防护方案。

## 9. Conclusion / 结论

### 原文位置
Page 14 - Page 15

### 中文翻译
论文结论是：HBM2 DRAM 对 read disturbance 并不免疫，RowHammer 和 RowPress 都能在真实芯片中诱发 bitflip。脆弱性具有显著空间变化，且现代芯片中的未公开防护机制不能保证安全。未来 HBM 系统需要透明、可评估且能覆盖 activation count 与 row-open time 两个维度的防护。
