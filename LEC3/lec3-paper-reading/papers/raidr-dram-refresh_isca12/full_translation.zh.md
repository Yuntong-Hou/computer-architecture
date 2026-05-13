# Full Chinese Translation

## Title

原文标题：RAIDR: Retention-Aware Intelligent DRAM Refresh

中文标题：RAIDR：保持时间感知的智能 DRAM 刷新

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖 retention variation、Bloom filter bins、RAS-only refresh、评估结果、局限和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

DRAM refresh 会阻塞 bank、增加访问延迟并消耗能量。随着 DRAM density 上升，refresh overhead 会迅速增长。RAIDR 的核心观察是：绝大多数 DRAM rows 的 retention time 远高于标准 64ms，只有极少数 weak rows 需要频繁 refresh。RAIDR 将 rows 按 minimum retention time 分入不同 refresh-rate bins，并在 memory controller 中用 Bloom filters 低开销存储这些 bins，从而跳过大量不必要 refreshes。

在 32GB/8-core 系统中，RAIDR 减少 74.6% refreshes，降低 16.1% DRAM power，并提升 8.6% performance。它不需要修改 DRAM 芯片，主要依赖 retention profiling 和 controller-side metadata。Bloom filters 保证无 false negatives；false positives 只会导致多刷新，不影响正确性。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section 1, Figure 1

### 中文翻译

DRAM cell 需要定期 refresh。JEDEC 标准通常要求在 64ms 内刷新所有 rows，以覆盖最差 retention cells。但实际 retention distribution 高度偏斜：多数 cells 能保持远超 64ms。Page 1-2, Figure 1 显示，在 32GB DRAM 中少于 1000 cells 需要短于 256ms refresh interval，约 30 cells 需要短于 128ms。

统一 64ms refresh 因此很保守。随着容量增长，refresh commands 数量上升，bank 被 refresh 阻塞的时间增加，refresh energy 也增长。RAIDR 提出用 per-row retention variation 减少 refresh，而不改变 DRAM 芯片接口。

从硬件工程角度看，RAIDR 是 retention-aware refresh 的基线方案。它展示了如何利用制造后 profiling 和 controller metadata，在不改 DRAM die 的前提下获取显著系统收益。

## 2. RAIDR Mechanism / RAIDR 机制

### 原文位置
Page 3-5 / Sections 3.1-3.4, Figures 4-5

### 中文翻译

RAIDR 首先对每行做 retention profiling，确定该行的 minimum retention time。然后根据 retention time 将 rows 分入 bins，例如 64-128ms、128-256ms、256ms 以上等。运行时，memory controller 用基础 64ms refresh 计数器遍历 candidate rows，并根据 row 所属 bin 决定是否在当前周期刷新。

为了低成本存储 bin membership，RAIDR 使用 Bloom filters。Bloom filter 的关键性质是无 false negatives：如果某 row 属于短 retention bin，查询一定不会漏掉；false positives 只会把某些 strong rows 误判为 weak rows，导致多刷新，但不会造成错误。因此 Bloom filter 很适合可靠性元数据。

RAIDR 使用 RAS-only refresh 对指定 rows 进行刷新。相比 DRAM auto-refresh，controller 对刷新目标有更多控制。代价是 RAS-only refresh 会带来额外 command/bus power，但整体评估显示节省的 refresh energy 和性能收益更大。

## 3. Correctness and Robustness / 正确性与鲁棒性

### 原文位置
Page 5-6 / Section 3.5 and sensitivity discussion

### 中文翻译

RAIDR 的正确性依赖准确 retention profiling 和无 false negatives metadata。Bloom filter false positives 不影响正确性，只降低收益。温度会影响 retention time，因此系统需要在合适温度条件下 profile 或保留 guardband。

论文讨论 Bloom filter 配置、bins 数量、capacity scaling 和 retention error sensitivity。随着容量增加，metadata 规模和 false positive rate 需要重新平衡。更大 DRAM density 下，refresh overhead 更严重，因此 RAIDR 的潜在收益也更大。

后续研究指出，VRT 会使静态 retention profile 过期，这是 RAIDR 的重要限制。AVATAR、REAPER 等工作可看作对 RAIDR 假设的补充：RAIDR 说明 refresh 可减少，后续工作说明 profile 必须动态维护。

## 4. Evaluation / 实验评估

### 原文位置
Page 7-10 / Figures 6-9

### 中文翻译

作者使用 retention distribution、DRAM timing/power model 和 8-core multiprogrammed workloads，比较 auto-refresh、distributed refresh、refresh pausing/no-refresh ideal 和 RAIDR。评估 normal/extended temperature、idle power、Bloom filter size/bins 和 4Gb-64Gb scaling。

Page 8, Figure 6 显示 RAIDR 在 32GB/8-core 系统中减少 74.6% refreshes。Page 8, Figure 7 显示平均性能提升 4.1%（normal temperature）和 8.6%（extended temperature）。Page 8-9, Figure 8 显示 average energy per access 降低 8.3% normal、16.1% extended。

Page 10, Figure 9 展示 capacity scaling：在 64Gb device capacity 下，RAIDR performance 比 auto-refresh baseline 高 107.9%，access energy saving 达 49.7%。这说明随着 refresh wall 加剧，retention-aware refresh 的价值更大。

## 5. Limitations / 局限性

### 原文位置
Page 4-5 and discussion

### 中文翻译

RAIDR 依赖 retention time profiling。Data pattern、温度、老化和 VRT 都可能改变 retention behavior。若 profile 不准确，弱 row 被分到慢刷新 bin 可能导致数据错误。因此实际系统需要 guardband、ECC、online profiling 或周期性 reprofiling。

RAIDR 的 RAS-only refresh 需要 controller 支持精确 row refresh，并知道物理 row mapping。Bloom filter false positives 会降低 refresh reduction；metadata 配置需随容量和 retention distribution 调整。

## 6. Conclusion / 结论

### 原文位置
Page 10-11 / Conclusion

### 中文翻译

RAIDR 证明，DRAM refresh overhead 可以通过 retention-aware profiling 和 controller-side metadata 大幅降低。Bloom filter bins 提供低成本、可靠的 weak-row 表达方式。它是后续 refresh reduction、VRT-aware refresh 和 online profiling 论文的重要基线。

## 硬件工程师学习提炼

1. RAIDR 的关键是把可靠性信息转化成 controller metadata：retention bins + Bloom filters。
2. 重点回看 Figure 1 retention distribution、Figure 4 operation、Figure 5 Bloom filters、Figures 6-9 结果。
3. 工程上要问 profile 如何获得、何时失效、温度/VRT 如何处理、RAS-only refresh 是否可部署。
4. 与 AVATAR/REAPER/PARBOR 一起读，可形成 refresh reduction 从静态 profile 到在线 profile 的完整路线。
