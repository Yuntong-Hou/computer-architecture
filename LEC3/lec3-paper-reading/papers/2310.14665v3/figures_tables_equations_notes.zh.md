# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | HBM2 组织/读扰动背景 | 帮助读者理解 channel、pseudo-channel、bank、row 的层级 | 后续空间差异分析都依赖这个结构 | 先对照 HBM2 结构再读结果图 |
| Figure 4 | Page 4 | 各 chip 的 RowHammer bit error rate | 不同 HBM2 chip 的 BER 差异明显 | 证明 chip-to-chip variation | 结合 Figure 5 看 BER 与 HCfirst |
| Figure 5 | Page 5 | HCfirst 分布 | 不同芯片触发首个 bitflip 的 hammer count 不同 | HCfirst 是防护阈值的重要参考 | 注意它不能代表后续 bitflip 风险 |
| Figure 6-7 | Page 5-6 | channel/pseudo-channel 差异 | HBM 内部通道间脆弱性不同 | 说明统一阈值可能过粗 | 看是否存在结构性偏差 |
| Figure 8 | Page 7 | bank 内 row 位置差异 | bank 中端/末端 row 较抗扰动 | 对 spatial-aware defense 有启发 | 重点看 row segment 趋势 |
| Figure 11-12 | Page 8 | 前 10 个 bitflip 的 hammer count | 第一个 bitflip 后后续 bitflip 更容易出现 | 影响 ECC 与安全攻击评估 | 不要只看 HCfirst |
| Figure 14-15 | Page 9-10 | RowPress 与 tAggON | 延长 row-open 时间显著降低 HCfirst | 证明 RowPress 是关键风险 | 这是本文最重要图之一 |
| Figure 16 | Page 11 | TRR-like 防护推断与绕过 | HBM2 存在未公开防护，但访问模式可绕过 | 关系到工业防护可信度 | 建议回 PDF 仔细看 pattern |
| Figure 17 | Page 12 | ECC word 中 bitflip 分布 | 多 bit 错误与 ECC granularity 相关 | 连接器件错误和系统容错 | 结合系统 ECC 设计理解 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 3 | 实验平台/芯片参数 | 说明 HBM2 chip 与 FPGA board 配置 | 判断实验外推范围 | 先看样本数量和芯片类别 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 未发现核心编号公式 | 全文 | 本文以实验测量为主 | HCfirst、BER、tAggON 为关键指标 | 重点是实验定义而非数学推导 | 否 |
