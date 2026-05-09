# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | 空间变化动机 | 不同 row 脆弱性不同会造成统一防护过度保守 | 引出 Svärd | 先理解最弱 row 与强 row 的差别 |
| Figure 3-5 | Page 5-6 | chip/module 层级变化 | 不同 chip 和 module 的 BER/HCfirst 差异 | 说明 variation 不是局部噪声 | 看分布而非单点 |
| Figure 6-10 | Page 6-8 | bank/subarray/row 变化 | 同一 subarray 内也有明显差异 | 支撑 row-level profile | 这是 characterization 核心 |
| Figure 11 | Page 11-12 | Svärd 机制示意 | 如何将 profile 映射到防护 aggressive 程度 | 理解系统设计 | 对照文字看数据流 |
| Figure 12 | Page 13-15 | 性能结果 | Svärd 叠加多种防护降低开销 | 主要量化结果 | 注意不同 base defense 收益不同 |
| Figure 13 | Page 15-16 | adversarial pattern | 攻击者可集中访问弱 row | 检查安全性 | 重点看最坏情况而非平均 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 4 | 测试芯片信息 | 144 DDR4 chips, 10 designs, 3 vendors | 判断实验覆盖范围 | 先看样本规模 |
| Table 2 | Page 12 | Svärd 与防护组合 | 展示可结合的 mitigation 类型 | 说明 Svärd 通用性 | 对比各方案参数 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 未发现核心编号公式 | 全文 | 论文以实验和机制设计为主 | NRH、HCfirst、BER 是核心指标 | 关键在 profile 到防护参数的映射 | 否 |
