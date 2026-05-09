# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | Typical DRAM-based system | MC、DRAM bank/subarray/row 基础结构 | 背景图 | 快速浏览 |
| Figure 2 | Page 2 | Modern DRAM physical cell layout | buried wordline、passing gate 等结构 | 支撑 Passing Gate Effect | 与 Section III 一起看 |
| Figure 3-4 | Page 2-3 | Physical bit-flip mechanism | data 0/1 的 electron movement 解释 | 说明两类 bit-flip 的物理直觉 | 读概念即可 |
| Figure 5 | Page 3 | TRR-induced bit-flip due to algorithm clash | MC 与 DRAM 使用相同 TRR 可能过度刷新 | 说明 MC-aided TRR 风险 | 关注 clash 概念 |
| Figure 6 | Page 4 | MR4 refresh interval | MR4 可增加 tREFI/tREFW | 说明低功耗机制和安全的矛盾 | 结合 MPA |
| Figure 8 | Page 5 | Time-Weighted Counting hardware | activation time 转为 count weight | 缓解 Passing Gate Effect | 读高层即可 |
| Figure 9-10 | Page 5 | Space Saving 与 decoy-row 问题 | decoy-rows 替换 aggressor rows | 本文问题定义核心 | 必读 |
| Figure 11 | Page 6 | DSAC flowchart | hit/miss/insertion/replacement 流程 | 核心算法图 | 必读 |
| Figure 12-14 | Page 6-7 | DSAC overview and examples | stochastic replacement 如何保留 aggressor row | 帮助理解概率替换 | 结合 Algorithm 1 |
| Figure 16 | Page 8 | 4 count table DSAC architecture | DSAC + Time-Weighted Counter 硬件结构 | 实现可行性 | 看模块组成 |
| Figure 18 | Page 10-11 | Maximum Disturbance summary | 不同算法在攻击 pattern 下的 disturbance | 主要实验图 | 看 DSAC vs Graphene |
| Figure 19 | Page 11 | 8-20 counters 下 average disturbance | counter 数减少时 DSAC 仍较稳健 | 支撑低面积结论 | 与 Table VI 一起看 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table I | Page 4 | Parameter summary | RHTH、MR4、MPA 等关键参数 | 评估配置基础 | 核对符号 |
| Table II | Page 8 | DSAC module area | 4-count-table DSAC area 估算 | 证明低成本 | 与 Table VII 一起读 |
| Table III | Page 10 | TRR algorithms comparison | 多数算法不能过滤 decoy-rows 或开销高 | 论文定位核心表 | 必读 |
| Table IV | Page 10 | Injected malicious RowHammer attacks | TRRespass/random pattern 配置 | 实验输入 | 看 attack model |
| Table V | Page 11 | Maximum Disturbance with 20 counters | DSAC disturbance 显著低 | 主要结果 | 必读 |
| Table VI | Page 11 | Average disturbance with 8-20 counters | DSAC 比 Graphene 低 133x | 低 counter 场景证据 | 必读 |
| Table VII | Page 11 | Area/access energy/static power | DSAC area/power 低于 counter-based algorithms | 实现可行性 | 必读 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Time-Weighted Counting weight | Page 5 | 根据 activation time 计算 count weight | WC、alpha、tRAS/tRASmin | row 开得越久，风险权重越大 | 中 |
| Replacement probability P(r) | Page 6, Eq. 4 / Algorithm 1 | 决定新 row 是否替换 min-count row | min cnt | decoy-row 很难替换高 count aggressor | 是 |
| Ce bound | Page 6, Eq. 5 | DSAC 最大错误/扰动界限 | b、c 等参数 | 说明 counter 数影响安全界限 | 中 |
| Adaptive TRRTH | Page 7, Eq. 6 | 根据 count table sum 调整 TRR threshold | TRRTH、MPA、tREFI | 控制何时触发 TRR | 中 |
| Appendix probability analysis | Appendix / Page 13+ extracted text | DSAC probabilistic security analysis | P(k)、P(f)、R(t) | 证明连续过滤 aggressor 的概率极低 | 中 |
