# Full Chinese Translation

## Title

原文标题：AVATAR: A Variable-Retention-Time (VRT) Aware Refresh for DRAM Systems

中文标题：AVATAR：面向 DRAM 系统的 Variable-Retention-Time 感知刷新

> 翻译说明：本文件按论文结构做高完整度中文详译/译述，覆盖 VRT 模型、Active-VRT Pool/Injection、AVATAR 机制、可靠性和性能评估。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

DRAM refresh 是容量扩展中的关键瓶颈。Multirate refresh 通过识别 retention 弱行并只对这些行使用更快刷新频率，可以显著降低 refresh overhead。然而，Variable Retention Time（VRT）会使某些 cell 在运行时随机进入低 retention 状态，从而破坏静态 retention profile 的可靠性。本文提出 AVATAR，一种 VRT-aware refresh 机制。

AVATAR 的核心思想是用 ECC 和 scrubbing 在运行时捕获 VRT-induced retention failures。一旦 ECC 发现某一行出现 correctable retention error，系统就认为该行可能发生 VRT transition，并把它加入 fast refresh set。这样，multirate refresh 不再完全依赖离线 profile，而是通过运行时 feedback loop 动态修正。论文显示 AVATAR 可将传统 multirate refresh 的可靠性提高约 100x，同时保留 62%-72% refresh reduction；在 64Gb DRAM 上性能提升约 35%，EDP 降低约 55%。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section I

### 中文翻译

DRAM cell 需要周期性 refresh，因为电容电荷会随时间泄漏。随着 DRAM 容量增加，单位时间需要刷新的 cells 越来越多，refresh 造成的性能和能耗开销持续上升，这一趋势被称为 Refresh Wall。简单缩短 refresh interval 可以提高可靠性，但会牺牲带宽、能耗和可扩展性。

Multirate refresh 的思路是：大多数 DRAM rows retention 较强，不需要频繁刷新；只有少数 weak rows 需要 fast refresh。系统通过 retention profiling 找出 weak rows，把它们放入 fast refresh table，其余 rows 使用更慢 refresh rate。该方法理论上能显著降低 refresh overhead。

问题在于 VRT。某些 cells 的 retention time 不是固定值，而会在不同状态之间随机切换。一个 cell 在离线测试时可能表现为 strong cell，运行一段时间后进入 weak state，导致静态 profile 无法覆盖它。若系统仍使用慢刷新，就可能发生 retention error。

作者指出，如果 multirate refresh 忽略 VRT，即使配备 ECC DIMM，也可能每 6-8 个月出现一次 uncorrectable error。这个结论很关键：ECC 可以修正单次错误，但如果 VRT 导致多个错误在同一 ECC word 或 scrub 间隔内累积，系统仍可能失败。

## 2. Background: DRAM Retention and VRT / 背景：DRAM 保持时间与 VRT

### 原文位置
Page 2-4 / Sections II-III

### 中文翻译

DRAM retention time 指 cell 在不刷新情况下保持正确数据的时间。Retention failure 与 leakage、温度、工艺波动和 cell 结构有关。传统 refresh 采用统一 interval，是一种保守策略，因为它必须覆盖最弱 cells。

VRT 是 retention behavior 中更难处理的现象。VRT cell 会在高 retention 和低 retention 状态之间随机切换。其低 retention 状态可能持续有限时间，也可能在任意时刻出现。由于这种状态转换在离线 profile 期间未必发生，静态测试无法可靠识别所有未来 weak cells。

论文引入 Active-VRT Pool（AVP）和 Active-VRT Injection（AVI）来刻画运行时 VRT 行为。AVP 表示某个时间窗口中处于 active weak state 的 VRT cells 集合；AVI 表示新的 active VRT cells 进入系统的速率。Page 5, Figure 7 显示，在 2GB memory 的 15 分钟窗口内，AVP 平均约 350-500 cells。这个数量足以使静态 multirate refresh 面临可靠性风险。

从工程角度看，VRT 是典型的“离线测试无法完全覆盖运行时故障模式”。它提醒我们：memory reliability 不应只依赖出厂 profile，而需要在线监测、纠错和动态策略。

## 3. Reliability Risk of VRT-Agnostic Multirate Refresh / 忽略 VRT 的风险

### 原文位置
Page 4-6 / VRT model and reliability analysis

### 中文翻译

作者评估传统 multirate refresh 在 VRT 存在时的可靠性。静态 profile 能识别测试期间已经表现为 weak 的 rows，但不能识别未来才转入 weak state 的 VRT cells。当这些 cells 被慢刷新覆盖时，就可能产生 retention errors。

ECC DIMM 可以修正部分错误，但并不能完全解决问题。若 scrub 周期过长，或同一 ECC word 中多个 bit 在 correction 前出错，就会形成 uncorrectable error。论文估计 VRT-agnostic ECC DIMM 在 multirate refresh 下仍可能每 6-8 个月发生一次 uncorrectable error。对数据中心系统而言，这种 failure rate 不可接受。

这一分析是 AVATAR 的动机基础。它说明：问题不是 multirate refresh 本身不可行，而是静态 profile 缺少运行时反馈。只要系统能发现新出现的 VRT-induced errors，并及时提高相关 row 的 refresh rate，multirate refresh 仍可安全使用。

## 4. AVATAR Mechanism / AVATAR 机制

### 原文位置
Page 6-8 / Section V, Figure 13

### 中文翻译

AVATAR 的全称可以理解为 VRT-aware refresh。系统首先执行传统 retention profiling，找出已知 weak rows，并把它们放入 fast refresh table。运行时，AVATAR 周期性执行 memory scrubbing。Scrubbing 会读出内存内容并让 ECC 检查是否存在 correctable errors。

当 ECC 发现某行出现 correctable retention error 时，AVATAR 将该 row promotion 到 fast refresh rate。这个动作背后的假设是：该 row 中可能存在 VRT cell，已经进入低 retention 状态；如果继续慢刷新，未来可能出现更多错误。通过 promotion，系统把该 row 纳入保护集合。

AVATAR 因此形成一个反馈闭环：离线 profile 提供初始 fast-refresh set；运行时 ECC/scrubbing 捕获新出现的 VRT 活动；fast-refresh table 动态增长；refresh policy 随时间适应实际故障模式。

AVATAR 有不同配置，例如 AVATAR-1 等，反映 scrub rate、fast refresh strategy 或 table 管理策略的差异。核心取舍是可靠性与 refresh savings。更积极的 scrubbing/promotion 提高可靠性，但也会增加带宽和 refresh 开销；更保守的策略节省资源，但可能延迟捕获 VRT。

## 5. Evaluation Methodology / 实验方法

### 原文位置
Page 7-8 / Evaluation setup

### 中文翻译

作者使用来自 24 个 DRAM chips 的 VRT behavior 数据建立模型，并模拟不同密度 DRAM 系统，包括 8Gb 到 64Gb。评估对象包括传统 multirate refresh、ECC-only 或 VRT-agnostic 方案，以及 AVATAR。指标包括 time-to-failure、refresh savings、performance 和 energy-delay product（EDP）。

评价的关键在于同时看可靠性和收益。一个方案若 refresh savings 很高但 time-to-failure 只有数月，在真实系统中不可接受；反之，如果完全回到高频 uniform refresh，可靠性提高但失去容量扩展价值。AVATAR 的目标是在二者之间找到可部署点。

## 6. Reliability Results / 可靠性结果

### 原文位置
Page 8-9 / Figure 14

### 中文翻译

Figure 14 显示 AVATAR 将传统 multirate refresh 的可靠性提高约 100x，使 time-to-failure 从 months 延伸到 decades 级别。这个结果说明，运行时捕获 VRT-induced errors 是有效的：一旦某 row 暴露出 retention risk，就被加入 fast refresh set，从而降低后续多 bit failure 概率。

作者强调，AVATAR 不需要预先知道所有 VRT cells。它依赖 ECC 的 correctable error 作为信号，把潜在危险 row 动态升级。这种设计利用了 ECC 的“早期告警”能力，而不仅仅把 ECC 当作最后防线。

## 7. Refresh Savings, Performance, and EDP / 刷新节省、性能与能效

### 原文位置
Page 9-10 / Figures 15-17

### 中文翻译

Figure 15 显示 AVATAR 在时间推移后仍能保持显著 refresh savings。初期 savings 约 72%；一年后，随着更多 VRT rows 被 promotion 到 fast refresh set，savings 仍约 62.4%。这符合预期：动态保护集合会增长，因此 savings 会下降，但仍远好于 uniform fast refresh。

Figures 16-17 显示，在 64Gb DRAM 上 AVATAR-1 可带来约 35% performance improvement，并使 EDP 降低约 55%。这些收益来自 refresh overhead 降低：内存系统减少因 refresh 被阻塞的时间，应用可获得更多有效带宽和更低延迟。

对硬件工程而言，这些结果说明可靠性机制不一定只带来成本。若设计得当，可靠性 feedback loop 可以让系统避免过度保守的 uniform refresh，从而同时提升性能和能效。

## 8. Limitations / 局限性

### 原文位置
Page 10-11 / Discussion and conclusion

### 中文翻译

AVATAR 依赖 ECC DIMM 和 scrubbing。没有 ECC 的系统无法安全地用 correctable error 作为 VRT 发现信号。Scrubbing 周期也很关键：周期太长可能让多个错误在发现前累积；周期太短则增加带宽和能耗开销。

Fast refresh table 会随时间增长，因此长期 refresh savings 低于初始 profile 后的 savings。论文使用 24 chips 数据建模，但未来工艺、温度、老化和 workload 条件可能改变 AVI rate 和 AVP 分布。

此外，AVATAR 把出现 correctable retention error 的 row promotion 到 fast refresh rate，但如何管理 table 容量、如何处理误判、如何与 memory controller refresh scheduling 配合，仍需要产品级设计细化。

## 9. Conclusion / 结论

### 原文位置
Page 11 / Conclusion

### 中文翻译

AVATAR 证明 VRT 不应让系统放弃 multirate refresh。通过把 ECC/scrubbing 转化为运行时反馈机制，系统可以动态发现新出现的 weak rows，并在可靠性可接受的同时保留大部分 refresh reduction。论文对高密度 DRAM 的意义在于：面对运行时可变故障模式，静态 profile 必须与在线监测结合。

## 硬件工程师学习提炼

1. AVATAR 是可靠性闭环设计的典型案例：profile、ECC、scrub、policy table、refresh scheduler 必须一起看。
2. 重点理解 AVP/AVI，因为它们把 VRT 从“随机现象”变成可建模的系统输入。
3. 对未来工作有启发的是：HBM/DDR/CXL memory 可靠性都可能需要类似 online telemetry + adaptive mitigation。
4. 复习优先看 Figure 7/9 的 VRT 模型、Figure 13 的 AVATAR 设计，以及 Figures 14-17 的可靠性和性能结果。
