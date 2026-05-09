# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | 不同 ECC functions 的可见错误分布 | 同类型 ECC code 不同 matrix 会产生不同 post-correction errors | 全文动机图 | 必读 |
| Figure 2 | Page 4 | on-die ECC 接口 | 系统只看到 data，不见 parity/syndrome | 解释黑盒限制 | 结合背景读 |
| Figure 5 | Page 9-10 | 匹配 miscorrection profiles 的 ECC functions 数 | {1,2}-CHARGED patterns 可唯一识别 | 正确性支撑 | 看不同 pattern 对辨识力的影响 |
| Figure 6 | Page 10 | BEER runtime/memory | SAT solving 成本随 code length 增加 | 实用性评估 | 注意离线性质 |
| Figure 7 | Page 11 | BEEP 流程 | pattern crafting、experiment、raw error inference | BEER 的应用 | 对照 BEEP 小节 |
| Figure 8-9 | Page 12 | BEEP success rate | 较长 codeword 成功率高 | 证明 BEEP 可用 | 关注 63/127-bit |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 5 | data-retention error patterns 与 syndromes | 不同 charged pattern 暴露不同 syndrome 信息 | BEER 构造约束基础 | 配合 Section 4 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Equation 4 | Page 11 | BEEP 由 syndrome 求 pre-correction codeword | H 为 parity-check matrix，c0 为错误 codeword | 已知 H 后可解 raw error locations | 是 |
| SAT constraints | Page 5-7 | 求解 unknown parity-check matrix | columns of H, miscorrection observations | 把 ECC recovery 转成 satisfiability | 是 |
