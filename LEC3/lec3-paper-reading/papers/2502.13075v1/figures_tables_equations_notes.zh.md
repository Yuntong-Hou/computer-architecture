# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 1-2 | 同一 row 的 RDT 时间序列 | RDT 随重复测量变化，最低值可能晚出现 | 引出 VRD | 必读 |
| Figure 2-4 | Page 6-8 | RDT 分布与 min/max 差异 | 少量测量无法捕捉最低阈值 | 支撑核心发现 | 看分布尾部 |
| Figure 5-8 | Page 8-12 | 参数影响 | data pattern、tAggON、温度、工艺影响 VRD | 连接 RowPress/工艺缩放 | 关注趋势而非单点 |
| Figure 9+ | Page 14-16 | guardband/ECC 分析 | 大 guardband 成本高，小 guardband 不稳健 | 防护启示核心 | 对照性能开销 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 4-5 | 实验芯片/平台 | 160 DDR4 + 4 HBM2，3 厂商 | 判断覆盖范围 | 先看样本 |
| Appendix Tables | Appendix | 测试时间/能耗补充 | 完整 profiling 成本很高 | 支撑部署难度 | 有需要时回查 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 5 | RDT 重复测量流程 | RDT、victim row、aggressor row、pattern | 通过重复实验观察 temporal variation | 是 |
| Guardband 计算 | Page 14-16 | 根据测得 RDT 设置更低保护阈值 | guardband percentage、profiled RDT | 用性能换安全余量 | 是 |
