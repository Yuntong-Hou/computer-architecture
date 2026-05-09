# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 4 | PRAC 安全分析/最大 activation | 展示 PRAC 配置下 victim 前可发生的最大激活数 | 支撑 NRH >= 20 的安全结论 | 结合 security analysis 读 |
| Figure 2 | Page 5 | 性能开销 | PRAC 在不同 NRH 下 slowdown 急剧变化 | 本文主要系统结果 | 注意现代和未来 NRH 的分界 |
| Figure 3 | Page 6 | DRAM energy overhead | RFM 和 timing overhead 带来能耗增长 | 说明问题不只是性能 | 与 Figure 2 对照 |
| Figure 4 | Page 6 | storage cost | 片内状态规模和成本估计 | 工业可行性关键 | 看 counter granularity 假设 |
| Figure 5 | Page 7 | performance attack | adversarial pattern 抢占 DRAM throughput | 揭示新攻击面 | 重点读攻击模式描述 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | PRAC/RFM timing 参数 | PRAC 增加/改变关键 DRAM timing | 性能开销的直接来源 | 结合 tRP/tRC 理解 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 安全不等式/阈值推理 | Page 3-4 | 证明 PRAC 在 NRH >= 20 下安全 | NRH 为触发 bitflip 所需激活阈值 | 最大可能扰动小于 bitflip 阈值即安全 | 是 |
