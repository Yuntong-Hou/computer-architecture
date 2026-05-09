# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2-3 | PRAC/RFM 基础流程 | DRAM 计数、back-off、RFM 的协同 | 理解 Chronus 修改点 | 先看再读设计 |
| Figure 2 | Page 4 | wave/feinting attack | 固定刷新与 delay 可被攻击利用 | Chronus 安全动机 | 重点图 |
| Figure 3 | Page 5 | PRAC 最大 activation/攻击窗口 | PRAC variants 仍需保守配置 | 连接攻击和性能开销 | 对照 security text |
| Figure 4-6 | Page 10-12 | 性能/能耗结果 | Chronus 在不同 NRH 下显著优于 PRAC | 主要实验结论 | 注意 v2 修正数值 |
| Figure 7+ | Page 12-13 | 与 Graphene/Hydra/PARA 比较 | Chronus 综合表现稳定 | 放在防护谱系中理解 | 看不同 NRH 区间 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | PRAC timing 参数 | counter update 增加关键 timing | 性能问题根源 | 重点看 tRP/tRC |
| Appendix Table | Appendix B | 结果修正 | v2 修正早期 bug 后数值变化 | 引用必须用新数值 | 回 PDF 核对 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 安全阈值推理 | Page 4-6 | 分析攻击窗口内最大扰动 | NRH、refresh count、delay window | 防护必须保证窗口内累积扰动低于 NRH | 是 |
