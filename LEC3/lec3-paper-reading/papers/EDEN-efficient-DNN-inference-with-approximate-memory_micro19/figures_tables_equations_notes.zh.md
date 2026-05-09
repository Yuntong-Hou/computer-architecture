# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | DNN layer data types | IFM/OFM/weights 的数据流 | 理解 mapping 单位 | 先看 |
| Figure 2-3 | Page 3 | DRAM organization/timing | VDD/tRCD/tRAS/tRP 如何影响访问 | 连接 approximate DRAM | 对照背景 |
| Figure 4 | Page 4 | EDEN framework | retraining、characterization、mapping 三步 | 核心框架图 | 必读 |
| Figure 5-8 | Page 6-8 | error models/real DRAM validation | approximate DRAM errors 非 uniform | 支撑训练模型 | 注意真实模块来源 |
| Figure 9-10 | Page 9-10 | curricular retraining | good-fit model + curriculum 提升 BER tolerance | 核心算法结果 | 必读 |
| Figure 11-12 | Page 10-11 | fine-grained BER tolerance/mapping | layer/data type 差异大 | 支持 partition mapping | 看 weights vs IFMs |
| Figure 13 | Page 11 | CPU DRAM energy saving | 平均 21% saving | 主要系统结果 | 注意 <1% accuracy loss |
| Figure 14 | Page 12 | CPU speedup | latency-bound DNN 最高 17% | 性能收益条件 | 看 ideal tRCD=0 对照 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 2 | Page 8 | baseline network accuracies | 列出评估 DNN 基线 | 判断 accuracy loss | 查看模型范围 |
| Table 3 | Page 10-11 | tolerable BER / DRAM parameters | 每个 DNN 可用的 VDD/tRCD 配置 | mapping 依据 | 重点 |
| Table 4-6 | Page 11-12 | CPU/GPU/Eyeriss/TPU configs | 系统模拟参数 | 影响结果外推 | 需要复现时看 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 5 | fine-grained DNN-to-DRAM mapping | BER tolerance、partition BER、parameter reduction | 把数据放到能承受的最激进 DRAM partition | 是 |
| Error model formulas | Page 6-7 | 描述 bitline/wordline/locality errors | PW/PB/FB 等 | 近似真实 DRAM 错误分布 | 中 |
