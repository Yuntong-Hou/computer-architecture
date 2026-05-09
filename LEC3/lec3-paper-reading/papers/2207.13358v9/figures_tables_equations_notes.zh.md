# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | DRAM rank/chip/bank/subarray organization | DRAM 层级组织和访问对象 | 理解 lock region 必备背景 | 先看 bank/subarray/row |
| Figure 2 | Page 4 | SMD bank organization | bank 被划分为 lock regions，并有 Lock Controller | SMD 核心架构图 | 重点看锁定区域与正常访问如何共存 |
| Figure 3 | Page 5 | MC handling ACT_NACK | MC 收到拒绝后等待 ARI 并重试 | forward progress 的关键 | 结合 Section 4.4 阅读 |
| Figure 4 | Page 7 | SMD-based fixed-rate refresh | DRAM 内部执行 fixed-rate refresh | 展示 refresh 如何映射到 SMD | 与 RAIDR/DSARP 背景对照 |
| Figure 5 | Page 8 | SMD variable refresh | 利用 retention-time variation 减少 refresh | 解释 SMD-VR 为何节能 | 关注 Bloom filter 和 weak rows |
| Figure 6 | Page 9 | Probabilistic RowHammer Protection | SMD-PRP 用概率标记并刷新 neighbor rows | 展示低成本 RowHammer 防护路径 | 和 PARA 对比 |
| Figure 7 | Page 10 | Deterministic RowHammer Protection | SMD-DRP 使用 counter table 检测 aggressor rows | 更强保证但面积更高 | 和 Graphene/BlockHammer 思路对比 |
| Figure 8 | Page 13 | Single-core speedup | 不同 SMD configs 的单核性能 | 第一组性能证据 | 看 SMD-Combined 与 No-Refresh |
| Figure 9 | Page 14 | Four-core weighted speedup | memory intensity 越高收益越明显 | 主要系统性能图 | 重点看 4c-high |
| Figure 10 | Page 14 | Normalized DRAM energy | SMD 降低 DRAM energy | 能耗结论核心图 | 看 SMD-VR 与 SMD-Combined |
| Figure 11 | Page 15 | DARP/DSARP/SMD 对比 | SMD 优于已有 parallelization 机制 | 证明不是只比弱 baseline | 重点读 Figure 11 附近文字 |
| Figure 18 | Page 18 | ACT_NACK divergence policies | 多 DRAM chips 维护不同步时的影响 | 暴露实际部署风险 | 重点看 worst-case slowdown |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 12-13 | Simulated system configuration | 给出 core、cache、DRAM、workload 配置 | 评估可信度基础 | 看是否符合你关心的系统 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| SMD-PRP probability constraints | Page 9 | 设定 RowHammer probabilistic protection 参数 | ACTmax、Pmark、neighbor row distance 等 | 控制 victim row refresh 概率 | 中 |
| Sensitivity formulas / thresholds | Page 15-17 | 分析 ACTmax、blast radius、Pmark 等 | 与 RowHammer threshold 相关 | 读结果图比推公式更重要 | 低-中 |
