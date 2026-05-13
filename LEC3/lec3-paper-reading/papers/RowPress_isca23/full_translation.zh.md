# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 RowPress 的概念、tAggON/ACmin 实验、DDR4 大规模表征、与 RowHammer/retention 的差异、真实系统演示、防护适配和硬件工程师视角。保留 RowPress、tAggON、ACmin、RowHammer、Graphene-RP、PARA-RP 等术语。

## Title

原文标题：RowPress: Amplifying Read Disturbance in Modern DRAM Chips

中文标题：RowPress：放大现代 DRAM 芯片中的读扰动

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

RowHammer 强调 aggressor row 被频繁打开/关闭会导致 victim rows bit flips。RowPress 进一步证明，aggressor row 保持打开的时间 tAggON 本身也能显著放大 read disturbance。换言之，不只是“打开次数多”危险，“打开太久”也危险。

作者在 164 颗真实 DDR4 chips 上系统表征 RowPress。结果显示，增加 tAggON 可将触发 bit flip 所需 activation count（ACmin）降低 1-2 个数量级，在极端 tAggON=30ms 时甚至一次 activation 就能触发 bit flip。

## 1. Motivation / 动机

### 原文位置

Page 1 - Page 2 / Figure 1

### 中文翻译

现有 RowHammer 防护多围绕 activation count 设计，例如统计某 row 被激活多少次，并在接近阈值时刷新邻近 rows。RowPress 说明这种模型不完整，因为 row-open duration 也是 disturbance 的关键变量。

现实系统中，memory controller 的 open-page policy、row-buffer hit optimization、调度等待、QoS 和 power management 都可能让 row 保持打开较长时间。因此 RowPress 不是纯实验室现象，而与控制器策略直接相关。

## 2. Experimental Characterization / 实验表征

### 原文位置

Page 3 - Page 10

### 中文翻译

作者测试 164 颗 DDR4 chips/21 modules，覆盖三大厂商和多种 die revisions。实验改变 tAggON、tAggOFF、temperature、single/double-sided patterns，测量最小 aggressor activation count ACmin。

结果显示，tAggON 越长，ACmin 越低。tAggON=7.8us 时，ACmin 平均降低 13.9x；tAggON=70.2us 时，平均降低 159.4x，最高 363.8x。温度从 50C 到 80C 会进一步恶化 RowPress。

RowPress vulnerable cells 与传统 RowHammer cells 和 retention failure cells 大多不同。对 tAggON >= 7.8us，RowPress cells 与 RowHammer cells 重叠平均低于 0.013%，与 retention failures 重叠低于 0.34%。这说明 RowPress 不是简单同一弱 cell 集合的另一种触发方式。

## 3. Real-System Demonstration / 真实系统演示

### 原文位置

Page 13

### 中文翻译

论文展示在带有 in-DRAM RowHammer 防护的真实 DDR4 系统中，用户态程序可通过 RowPress 触发 bit flips，而传统 RowHammer 方式不能。这说明厂商现有防护若只关注 activation count，可能漏掉 row-open-time 维度。

用户态可利用 row-buffer behavior 和访问模式影响 tAggON。攻击可行性还依赖 OS allocator、cache behavior、physical address mapping 和 DRAM policy。

## 4. Mitigation / 防护

### 原文位置

Page 15 - Page 16 / Table 2

### 中文翻译

一种直接方案是限制 maximum row-open time。但论文指出，只限制 row-open time 本身可能导致高达 34.1% 性能退化，而且不能完全替代 RowHammer 防护。

作者将 Graphene 和 PARA 适配为 Graphene-RP/PARA-RP，使防护同时考虑 activation count 和 row-open duration。示例配置下，Graphene-RP/PARA-RP 最大 slowdown 分别约 4.6%/13.1%。

## 5. 硬件工程师视角

RowPress 对 memory controller 设计影响很直接。Open-page policy 不能只追求 row-buffer hit rate。控制器可能需要最大 row-open timer、基于 tAggON 的 weighted counting、long-open-row telemetry，或者在 scheduling 中避免 adversarial long-open patterns。

对验证，RowHammer test suite 必须加入 RowPress patterns：长 tRAS/open row、ONOFF、temperature sweep、single/double-sided、不同 data pattern。只测高频 ACT/PRE 不够。

## 6. 不确定与需回原文核对

- Figure 1、Figures 9-13、Table 2 的数值建议回 PDF；
- DDR5/HBM/LPDDR 的 RowPress 行为需结合后续论文；
- 完整 exploit chain 不是本文重点，需要结合 OS/security 研究。
