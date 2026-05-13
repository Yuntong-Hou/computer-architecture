# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖论文的摘要、背景、实验平台、HBM2 RowHammer/RowPress 表征、空间差异、片内防护推断、ECC 影响、讨论和硬件工程师视角。保留 HBM2、RowHammer、RowPress、HCfirst、BER、TRR、ECC 等关键英文术语。参考文献保留英文，不逐条翻译。

## Title

原文标题：Read Disturbance in High Bandwidth Memory: A Detailed Experimental Study on HBM2 DRAM Chips

中文标题：高带宽内存中的读扰动：对 HBM2 DRAM 芯片的详细实验研究

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

High Bandwidth Memory（HBM）通过 3D-stacked DRAM、宽 I/O、多个 channel/pseudo-channel 和高带宽接口，为 GPU、FPGA、AI/HPC 加速器提供远高于传统 DDR 的带宽。过去大量 RowHammer 研究集中在 DDR3、DDR4、LPDDR 等产品上，而 HBM2 是否同样存在 read disturbance，脆弱性如何分布，以及内部防护是否可靠，公开资料非常有限。

本文对真实 HBM2 DRAM chips 进行详细实验研究。作者发现，所有测试 HBM2 chips 都可以诱发 RowHammer bit flips，且脆弱性在 chip、channel、pseudo-channel、bank 和 row 位置之间高度不均匀。论文还研究 RowPress，即通过增加 aggressor row 的打开时间 tAggON 放大 read disturbance。结果表明，较长 tAggON 可以显著降低触发第一个 bit flip 所需的 hammer count。

作者进一步发现，测试 HBM2 chips 中存在未公开的 activation-count based TRR-like mitigation，但该机制并非不可绕过。通过特定访问模式，攻击者仍可能诱导 bit flips。论文还分析 ECC word 中 bit flips 的分布，说明 HBM 系统需要联合考虑 read disturbance、on-die/internal ECC、外部 ECC 和系统级隔离。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

HBM2 被广泛用于高性能 GPU、FPGA 板卡、机器学习加速器和科学计算系统。与传统 DIMM 形态不同，HBM2 通过 silicon interposer 将多个 DRAM dies 堆叠并连接到处理器/加速器附近，提供高带宽和较低能耗/bit。由于目标市场和封装形态不同，业界容易假设 HBM 的可靠性和安全风险与普通 DDR 有较大差异。

论文指出，这种假设缺乏公开实验证据。RowHammer 的根源是 DRAM cell scaling 和 row activation 干扰，而 HBM2 仍然是 DRAM。高带宽、高并行度和复杂内部组织并不能天然消除 read disturbance。相反，HBM 通常服务于高度并行、内存密集、共享加速环境，若存在可触发 bit flips 的访问模式，影响范围可能覆盖云端 GPU、多租户 FPGA、AI 训练集群和 HPC 系统。

本文目标是填补 HBM2 read disturbance 公开实验空白。作者不仅测试是否有 bit flips，还细分分析 chip/channel/bank/row 维度的 spatial variation，研究 RowPress 对 HBM2 的影响，并黑盒推断内部 TRR-like 防护行为。

## 2. Background and Motivation / 背景与动机

### 原文位置

Page 2 - Page 3 / Sections 2.1-2.3

### 中文翻译

HBM2 由多个 DRAM dies 垂直堆叠，并通过 through-silicon vias（TSVs）和宽接口提供高带宽。一个 HBM2 stack 内包含多个 independent channels，每个 channel 又可分成 pseudo-channels。相比 DDR，HBM2 的内部并行度更高，地址映射、bank 组织和 timing 行为更复杂。

Read disturbance 指读访问或 activation 过程对非目标 DRAM cells 造成干扰。RowHammer 是典型形式：重复激活 aggressor row，导致邻近 victim row bit flips。RowPress 则强调 row-open duration：即使 activation 次数不高，只要 aggressor row 保持打开足够久，也可能增加 victim disturbance。

作者的动机有三点。第一，HBM2 是否存在 RowHammer 需要实测。第二，HBM2 的空间结构复杂，可能导致脆弱性强烈依赖 channel、pseudo-channel、bank 和 row 位置。第三，现代 HBM2 可能包含厂商私有 read disturbance mitigation，但黑盒防护的安全边界需要评估。

对硬件工程师来说，这一节的核心是：不能把 HBM 当成“更高级所以更安全”的内存。HBM 的高带宽只解决数据搬移瓶颈，不自动解决 cell-level disturbance。

## 3. Experimental Infrastructure / 实验基础设施

### 原文位置

Page 3 - Page 4 / Section 3, Figure 3

### 中文翻译

作者使用 FPGA-based HBM2 testing infrastructure，对多颗 HBM2 chips 执行可控 DRAM command/access patterns。实验对象包括两块 FPGA 板上的 6 颗 HBM2 DRAM chips。平台允许作者控制 hammer count、aggressor row、victim row、data pattern、channel、pseudo-channel、bank 和 row segment 等参数。

为了减少 temperature drift 对结果的干扰，论文监控芯片温度，并展示了 24 小时内的温度变化。温度控制很关键，因为 DRAM retention、leakage 和 disturbance vulnerability 都与温度相关。作者通过固定或记录温度条件，尽量保证不同实验之间可比较。

实验通常会写入特定 data pattern，执行 hammering 或 RowPress 访问，再读取 victim rows 检查 bit flips。主要指标包括 bit error rate（BER）、触发第一个 bit flip 所需的 hammer count（HCfirst）、不同位置的错误分布、前若干 bit flips 的 hammer count 序列，以及 ECC word 中 bit flips 的分布。

## 4. RowHammer Characterization Across Chips / 跨芯片 RowHammer 表征

### 原文位置

Page 4 - Page 5 / Figures 4-5

### 中文翻译

作者首先回答最基本问题：HBM2 是否会出现 RowHammer bit flips。实验结果显示，所有 6 颗测试 HBM2 chips 都可以诱导出 RowHammer bit flips。这一发现本身非常重要，因为它排除了“HBM2 因结构不同而天然免疫 RowHammer”的假设。

不过，不同 chips 的脆弱程度并不相同。某些 chips 的 HCfirst 更低，说明更少 activation 就能触发第一个 bit flip；某些 chips 的 BER 更高，说明在相同 hammering 条件下出现更多错误。论文用 error bars 展示不同 chips 的范围，强调 die-to-die variation 明显存在。

从产品角度看，这意味着安全阈值不能只基于少量样品或典型芯片。若某一批次、某一 vendor、某一 speed bin 或某一 stack 表现更弱，系统级防护必须覆盖最弱情况，否则 field failure 或 security exploit 会集中发生在弱器件上。

## 5. RowHammer Across Channels, Pseudo-Channels, and Banks / 跨通道、伪通道和 Bank 的变化

### 原文位置

Page 5 - Page 7 / Figures 6-10

### 中文翻译

论文进一步分析 HBM2 内部结构上的 variation。结果显示，channel 和 pseudo-channel 之间的 BER 和 HCfirst 差异明显。某些 channel 在较低 hammer count 下就出现 bit flips，而另一些 channel 更稳健。类似地，不同 banks 的脆弱性也不同。

这种空间变化可能来自物理布局、TSV/接口路径、bank/subarray 实现差异、制造偏差、局部温度、电源噪声或厂商内部 remapping。论文并不声称完全解释物理原因，而是通过系统实验揭示这些差异真实存在。

作者还观察到 bank 中不同 row 位置的规律：某些中端或末端 row 更抗扰动。类似现象在 DDR3/DDR4 中也曾出现。它可能与 subarray 边界、dummy rows、sense amplifier 位置或物理 adjacency 有关。

工程含义是：HBM 防护若只使用全局 NRH threshold，会产生保守开销或安全漏洞。更合理的设计可能需要按 channel/bank/row group 建模，但这又引入 profile 成本、存储成本和随时间变化的稳定性问题。

## 6. Behavior of the First Several Bit Flips / 前若干 bit flips 的行为

### 原文位置

Page 8 / Figures 11-12

### 中文翻译

作者不仅记录第一个 bit flip，也分析同一 victim row 中前 10 个 bit flips 的 hammer count。实验发现，在出现第一个 bit flip 以后，后续 bit flips 往往需要的额外 hammer count 更少。这说明 HCfirst 虽然是重要指标，但并不能完整描述多 bit error 风险。

对 ECC 来说，这一点尤其关键。若一个 victim row 一旦开始出错，后续 bits 更容易继续出错，那么系统可能很快从 single-bit correctable error 进入 multi-bit uncorrectable error。特别是在 HBM 中，bit flips 如何映射到 ECC words 会决定外部 ECC 能否修复。

硬件验证中应避免只测“第一个错误出现时间”。更应统计错误增长曲线、同一 ECC word 内的多 bit 聚集、跨 beat/跨 lane 分布，以及 repeated hammering 后错误是否加速。

## 7. RowPress in HBM2 / HBM2 中的 RowPress

### 原文位置

Page 9 - Page 10 / Figures 14-15

### 中文翻译

RowPress 研究 aggressor row open time 对 read disturbance 的影响。作者改变 tAggON，从极短打开时间逐步增加到微秒级甚至更长。结果显示，当 tAggON 增大时，触发第一个 bit flip 所需的 HCfirst 显著降低。论文报告 tAggON = 35.1us 时，平均 HCfirst 比 29ns 小约 222.57x。

这说明只跟踪 activation count 的防护机制是不完整的。如果某个 row 被打开很久，即使 activation 次数少，也可能对邻近 victim rows 造成强扰动。论文甚至指出，在极端条件下，单次 activation 并保持 row open 16ms 也可能诱发 bit flip。

对 memory controller 来说，这是直接相关的工程风险。Open-page policy、row buffer locality optimization、long burst behavior、QoS-induced stalls、refresh postponement、power management 等机制都可能延长 row open duration。过去控制器优化常把 row-buffer hit 当成正收益，但 RowPress 说明，过长 row-open 可能带来可靠性和安全成本。

## 8. Hidden TRR-like Mitigation / 未公开 TRR-like 防护机制

### 原文位置

Page 11 / Figure 16

### 中文翻译

论文通过 black-box experiments 推断 HBM2 chips 中存在未公开的 activation-count based mitigation。作者设计不同 hammering 和 dummy row access patterns，观察 bit flip 行为如何变化。如果插入某些访问后 bit flips 被抑制，说明内部可能有机制在追踪 aggressor activations 并刷新 victim rows。

然而，这种防护并非完全可靠。特定访问模式仍可绕过它并诱发 bit flips。这与 DDR4 上许多厂商 TRR 被绕过的历史一致：黑盒防护若未公开安全模型和阈值，攻击者可以通过实验搜索绕过模式。

工程意义很强：系统设计不能只相信“DRAM vendor 已经有 TRR”。如果防护机制不透明，平台方难以证明安全边界。对于云 GPU/HPC 多租户系统，HBM read disturbance 需要纳入威胁模型，并考虑 workload isolation、memory coloring、refresh hardening 或 runtime monitoring。

## 9. ECC Word Distribution / ECC word 中的 bit flip 分布

### 原文位置

Page 12 / Figure 17

### 中文翻译

作者分析 bit flips 在 ECC words 中的分布。ECC 能否修复错误，不只取决于总 bit flips 数量，还取决于这些 bit flips 是否落在同一个 ECC word 中。如果多个 flips 聚集在一个 ECC word 内，single-error correction 可能失效；如果分散在不同 ECC words 中，修复概率更高。

HBM 系统可能包含 on-die ECC、stack 内部 ECC、外部 controller ECC 或加速器 SoC 侧 ECC。不同层级 ECC 对错误的可见性不同。On-die ECC 可能隐藏原始 cell errors，使外部系统看不到早期故障模式；但如果错误超过 on-die ECC 能力，外部系统可能只看到不可纠正错误。

对硬件工程师来说，这提示读扰动防护不能只看 raw bitflip count。必须结合 ECC granularity、scrubbing interval、retry 机制、poisoning/reporting、RAS telemetry 和 page retirement 策略评估系统风险。

## 10. Discussion and Defenses / 讨论与防护

### 原文位置

Page 12 - Page 13 / Section 8

### 中文翻译

论文讨论了 read disturbance defenses。传统方案包括增加 refresh、TRR、probabilistic adjacent row activation、访问节流、迁移高风险 pages、memory controller tracking 和更强 ECC。对 HBM2 而言，这些方案都面临高带宽场景下的额外挑战。

增加 refresh 会消耗 HBM 带宽和能耗，影响 GPU/FPGA 计算吞吐。Controller tracking 需要理解 HBM 地址映射和物理邻近关系，但这些信息可能对平台不可见。ECC 能提高容错能力，但无法消除攻击者制造不可纠正错误或静默数据破坏的风险。

作者强调，HBM2 read disturbance 需要专门研究，而不是简单套用 DDR 防护结论。HBM 的 channel/pseudo-channel/bank 组织、封装热特性和目标 workload 都会影响防护设计。

## 11. Conclusion / 结论

### 原文位置

Page 13 / Conclusion

### 中文翻译

本文系统实验表明，HBM2 DRAM chips 存在 RowHammer 和 RowPress read disturbance vulnerability。脆弱性在 chip、channel、pseudo-channel、bank 和 row 位置上显著变化。较长 aggressor row open time 会显著放大 disturbance，使单纯 activation-count based 防护不足。

论文还显示，现代 HBM2 chips 可能包含未公开 TRR-like mitigation，但该机制可被特定访问模式绕过。ECC word 分析进一步说明，read disturbance 与系统 RAS 机制紧密相关。

## 12. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文实验、讨论和结论的工程化解读

### 中文学习笔记

1. 对 GPU/HPC 平台：HBM 读扰动应进入 reliability/security signoff。不能只依赖 vendor 声称的内部防护。

2. 对 memory controller：RowPress 说明 row-open time 是一等风险变量。控制器策略应限制极端长时间 open row，或把 tAggON 纳入防护计数。

3. 对验证团队：HBM 测试矩阵应覆盖 channel、pseudo-channel、bank、row segment、data pattern、temperature、refresh mode 和 long row-open patterns。

4. 对 RAS：ECC 分析必须和扰动分布结合。需要关注同一 ECC word 内多 bit flips、scrubbing 周期、错误上报和 page retirement。

5. 对行业趋势：AI/HPC 高带宽内存系统越来越多采用 HBM。如果 read disturbance 防护不透明，云端多租户 GPU/FPGA 会面临新的隔离和可用性挑战。

6. 对个人学习：这篇论文适合和 RowPress、Svärd、PRAC/Chronus 连读。它负责证明 HBM2 也存在问题，后续论文进一步讨论空间/时间变化和标准化防护。

## 13. 不确定与需回原文核对

- Figures 4-17 中各 chip/channel/bank 的精确数值建议回 PDF 复核。
- 内部 TRR-like 机制是黑盒推断，不应当视为厂商公开规格。
- ECC word mapping 的具体实现依赖平台和厂商，本文结果不能直接外推到所有 HBM2/HBM3。
- 参考文献保留英文，未逐条翻译。
