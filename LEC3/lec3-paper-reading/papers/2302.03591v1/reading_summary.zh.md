# 中文阅读摘要

## 1. 一句话总结

本文提出 DSAC，一种用于 in-DRAM RowHammer mitigation 的 stochastic and approximate counting algorithm，通过 Stochastic Replacement 过滤 decoy-rows，并用 Approximate Counting 降低面积开销，使有限 counter 条件下的 TRR detection 更稳健。

## 2. 研究背景

DRAM scaling 降低了 cost per bit，但也降低 RowHammer threshold。RowHammer 可被软件触发并造成系统级安全威胁。传统 TRR 需要识别被频繁访问的 aggressor rows 并刷新 victim rows；如果 TRR 在 memory controller 中实现，可能缺少真实 RowHammer threshold 和内部物理信息，导致 refresh 不足或过多，还会引入额外 commands 和性能开销。Page 1 Introduction 因此把重点转向 in-DRAM TRR。

## 3. 核心问题

- 在 DRAM 内部 counter 数量极其有限时，如何可靠识别 RowHammer aggressor rows。
- 为什么 state-of-the-art counter-based algorithms 会被 decoy-rows 干扰。
- 如何同时处理两类 activation-induced bit-flips：Passing Gate Effect 和 RowHammer。
- 如何用低面积、低能耗结构实现可扩展 in-DRAM TRR。

## 4. 核心贡献

- 将 activation-induced bit-flips 分为 Passing Gate Effect 和 RowHammer，并解释两者与 activation time/frequency 的关系。原文位置：Page 2-3, Section III。
- 提出 Time-Weighted Counting，用 activation time 给 row count 加不同权重以缓解 Passing Gate Effect。原文位置：Page 4-6, Figure 8。
- 指出 decoy-rows 是 counter-based algorithms 在有限 counters 下失效的根本原因。原文位置：Page 5, Figure 10。
- 提出 DSAC，用 Stochastic Replacement 让新 row 只有在平均访问次数超过当前 min-count row 后才更可能替换，从而过滤 decoy-rows。原文位置：Page 6-7, Figures 11-14。
- 提出 Maximum Disturbance 作为 RowHammer protection index。原文位置：Page 10, Section VII。
- 实验显示 DSAC 相比 Graphene 等算法有更低 disturbance 和较低 area/energy overhead。原文位置：Page 10-11, Tables V-VII。

## 5. 方法概述

DSAC 维护一个有限大小的 count table。若 incoming row 已在 table 中，则增加其 count；若 table 未满，则插入；若 table 已满，则用 stochastic replacement 判断是否替换当前最小 count row。替换概率与 min count 相关，直观上，一个偶然出现的 decoy-row 很难替换已积累较高 count 的真正 aggressor row。DSAC 同时用 approximate counting 保留被替换 row 的 count 信息，降低面积开销。

Time-Weighted Counting 则根据 row activation time 加权计数。activation time 超过标准 minimum 时，说明 Passing Gate Effect 风险上升，因此相应 row count 增量更高。

## 6. 实验设计

作者配置 baseline parameters，并比较多种 TRR algorithms：CRA、CBT、CAT-TWO、TWiCe、Graphene、PRA、PARA、PRoHIT、MRLoc、DSAC。主要指标是 Maximum Disturbance，即 observation period 内某 row 未被 TRR 处理时能累积的最大 activation 数。攻击模式包括 TRRespass 和 random access，并采用 double-sided uniform weight。面积、access energy、static power 使用 CACTI 6.0 估算。原文位置：Page 10-11。

## 7. 主要结果

- Page 1 Abstract：DSAC 的实验数据显示 Maximum Disturbance 比 state-of-the-art counter-based algorithm 低 49x。
- Page 10, Table V：使用 20 counters 时，DSAC 在 TRRespass/random 模式下的 average disturbance 为 2196/2211，显著低于 Graphene 的 19450/10822。
- Page 11, Table VI：当 counters 从 8 到 20 缩放时，DSAC average disturbance 比 Graphene 低 133x。
- Page 11, Table VII：DSAC per-rank area 约 0.01 mm2，占 CPU area 约 0.01%，access energy 9.64 pJ，static power 0.71 mW，低于主要 counter-based TRR algorithms。

## 8. 关键结论

在 DRAM 内部 counter 资源有限时，核心问题不是简单“计数不够”，而是 decoy-rows 会污染 count table、挤出真正 aggressor rows。DSAC 的 Stochastic Replacement 通过概率方式降低 decoy-row 替换成功率，使 aggressor rows 更可能留在 table 中，从而获得低成本 RowHammer mitigation。

## 9. 局限性

- 作者明确说明 DSAC 不需要外部 DRAM 操作，因此没有评估 system performance。原文位置：Page 10, Section VII。
- DSAC 是 probabilistic，安全分析依赖概率模型和攻击假设。Appendix 中给出数学分析，但实际系统仍需验证。
- 评估使用合成 attack patterns 和 CACTI 估算，不是完整真实系统/芯片原型。
- 论文英文和排版存在不清晰处，公式和参数需回原文仔细核对。

## 10. 适合我重点关注的内容

重点读 Page 2-3 的 bit-flip mechanism，Page 4 的 MR4/MPA 分析，Page 5-7 的 decoy-row 和 DSAC flow，Page 10-11 的 Maximum Disturbance 评估。若只抓一个核心，要理解 Figure 10 为什么传统 counter-based algorithms 会被 decoy-rows 击败，以及 Figure 11/Algorithm 1 如何解决。

## 11. 和其他文献的关系

DSAC 是具体 RowHammer mitigation algorithm，可放在 `Fundamentally Understanding and Solving RowHammer` 的 mitigation 方向下。它与 SMD 互补：SMD 提供部署 in-DRAM maintenance 的框架，DSAC 则是可放入 DRAM 内部的 TRR detection/counting mechanism。它也应与 Graphene、PARA、BlockHammer、Hydra 等 counter/probabilistic defenses 对比。
