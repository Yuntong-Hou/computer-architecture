# Full Chinese Translation

## Title

原文标题：The Reach Profiler (REAPER): Enabling the Mitigation of DRAM Retention Failures via Profiling at Aggressive Conditions

中文标题：REAPER：通过激进条件下的 profiling 缓解 DRAM retention failures

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖 reach profiling、coverage/FPR/runtime、ECC profile longevity、LPDDR4 表征、系统评估和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

许多 refresh-reduction 技术假设系统能快速找到在延长 refresh interval 下会失败的 DRAM cells。但 brute-force retention profiling 需要写入模式、等待目标 refresh interval、读回检查，运行时间高；VRT 和 data-pattern dependence 还会让失败集合变化。REAPER 提出 reach profiling：在比目标运行条件更激进的 refresh interval 或温度下 profile，以更短时间覆盖目标条件下绝大多数 failing cells。

作者在 368 颗现代 LPDDR4 chips 上分析 profiling tradeoff，用 coverage、false positive rate 和 runtime 三个指标刻画设计空间。结果显示，在目标 refresh interval 上方增加 250ms profiling，REAPER 平均可达到 >99% coverage、<50% false positive rate，并比 brute-force 快 2.5x。64Gb chips、512ms operating point 下，REAPER 平均性能提升 16.3%，DRAM power 降低 36.4%。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section 1

### 中文翻译

Retention-aware refresh 的关键前提是知道哪些 cells/rows 在较长 refresh interval 下会失败。传统 brute-force profiling 在目标条件下直接测试：写 pattern，等待目标 refresh interval，读回检查。若目标 interval 很长，或者需要多 pattern、多温度、多轮测试，profiling runtime 会很高，不适合频繁在线执行。

REAPER 的核心问题是：能否在更激进条件下 profile，使目标条件下的 weak cells 更快暴露？例如目标是 512ms/某温度运行，可以在更长 refresh interval 或更高温下测试。这样更多潜在 weak cells 会失败，coverage 提高，测试迭代数减少。

从硬件工程角度看，REAPER 解决的是 RAIDR/AVATAR 类机制的关键落地问题：profile 不是免费获得的。在线 profiling 的时间、带宽、误判和寿命都必须量化。

## 2. Metrics: Coverage, FPR, Runtime / 指标：覆盖率、误报率与运行时间

### 原文位置
Page 3-5 / Profiling tradeoff definitions

### 中文翻译

Coverage 表示目标条件下会失败的 cells 中，有多少被 profiling 捕获。False positive rate（FPR）表示在激进 profiling 条件下失败、但目标条件下不会失败的 cells 比例。Runtime 表示完成 profiling 所需时间。

这三个指标存在取舍。更激进条件通常提高 coverage、降低 runtime，但会增加 false positives。False positives 不一定影响正确性，但会导致更多 rows 被保护或刷新，降低性能/能耗收益。Coverage 不足则可能留下未保护 weak cells，影响可靠性。

REAPER 的贡献之一是把 profiling 设计空间显式量化，而不是只报告某个 profile 是否有效。

## 3. Reach Profiling / Reach Profiling 方法

### 原文位置
Page 5-8 / Figures 9-10

### 中文翻译

Reach profiling 在比目标更激进的条件下执行，例如更长 refresh interval 或更高 temperature。由于 retention failures 在更严苛条件下更容易出现，目标条件下的 failing cells 大多会被覆盖。

实验显示，在目标 refresh interval 上方增加 250ms profiling，REAPER 平均可达到 >99% coverage、<50% FPR，并比 brute-force 快 2.5x。更激进 reach conditions 可把 speedup 推到 >3.5x，但 FPR 会超过 75%。因此系统需要根据可靠性目标和性能收益选择 reach point。

这对工程设计很有启发：profiling 本身也是可调 policy，而不是固定测试过程。不同产品可根据 ECC 强度、refresh savings 目标和可接受误报率选择不同 aggressive condition。

## 4. ECC and Profile Longevity / ECC 与 Profile 有效期

### 原文位置
Page 9 / Section 6.2, Table 1

### 中文翻译

REAPER 分析 ECC 的 UBER/RBER 约束如何转化为 profile longevity。Profile 并非永久有效，VRT/DPD 和运行时变化会导致新的 failures 出现。系统必须知道 profile 多久需要刷新一次，或者在 ECC 可承受范围内允许多少未捕获错误。

论文给出示例：2GB DRAM + SECDED + 1024ms/45C 下，99% coverage profile 的 longevity 约 2.3 days。这意味着在线 profiling 需要周期性执行，而不是一次性完成。

该分析对产品非常关键。若 profile lifetime 只有几天，profiling overhead 和调度机制必须可持续；若系统没有足够 ECC 或 scrubbing，relaxed-refresh 操作风险会显著上升。

## 5. System Evaluation / 系统评估

### 原文位置
Page 11-12 / Figure 13

### 中文翻译

作者在系统模拟中评估 online profiling overhead、ArchShield 结合 REAPER 的性能和 power。64Gb chips、512ms operating point 下，REAPER 平均性能提升 16.3%，DRAM power 平均降低 36.4%。64Gb、1024ms 时，REAPER 平均性能提升 13.5%，brute-force 仅 7.5%；1280ms 时 brute-force 平均退化 -5.4%，REAPER 仍有 8.6% 平均收益。

与 ArchShield 结合时，REAPER 平均性能提升 12.5%，比 brute-force profiling 组合高 5.6%。这些结果说明 profiling runtime 本身会显著影响系统收益；更快 profile 可让 relaxed refresh 的收益真正体现出来。

## 6. Limitations / 局限性

### 原文位置
Page 13 / Caveats and discussion

### 中文翻译

论文指出，结果依赖具体假设：45C、reach profiling 2.5x speedup、32 chips/module、100% coverage 假设和 20 个 workload mixes。真实 relaxed-refresh operation 需要实际芯片 characterization data，而 DRAM vendors 通常不公开这些数据。

REAPER 不是完整可靠性方案。它需要 ECC、bit repair、remapping 或其他 mitigation 处理未捕获 failures 和 false positives。DPD/VRT 会让 profile 过期，不同工艺和温度下参数需要重新校准。

## 7. Conclusion / 结论

### 原文位置
Page 13 / Conclusion

### 中文翻译

REAPER 证明，可靠 refresh reduction 不能只依赖 brute-force profiling。通过在 aggressive reach conditions 下 profile，系统可以在 coverage、false positive rate 和 runtime 之间取得更好折中，使在线 profiling 更实际。

## 硬件工程师学习提炼

1. REAPER 的核心价值是把 profiling 变成工程可调问题：coverage、FPR、runtime、profile longevity。
2. 重点回看 Figures 9-10 reach tradeoff、Table 1 tolerable RBER、Section 6.2 profile longevity、Figure 13 系统收益。
3. 产品化需要 ECC/scrub/remap 支撑，不能把 REAPER 当作单独可靠性保证。
4. 与 RAIDR、AVATAR、Error Mitigation 一起读，可建立 retention-aware refresh 的完整闭环。
