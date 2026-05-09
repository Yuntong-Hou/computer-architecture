# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | retention time distribution | 说明多数 cells 不需要 64ms refresh。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 3 | Page 3 | adverse effects of refresh | 展示容量扩展下 refresh latency/power/throughput loss。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 4 | Page 4 | RAIDR operation | 展示 profiling、bins、candidate refresh decision。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 5 | Page 5 | Bloom filter implementation | 说明 bins 存储和组件。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 7 | Page 8 | performance | 展示性能提升。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 9 | Page 10 | sensitivity/scaling | 展示配置和容量扩展。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 3 | Page 10 | RAIDR configurations | 比较 2 bins/3 bins 和不同 Bloom filter overhead。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Bloom filter membership | Page 5 | retention bin membership test | k hash functions over m-bit array | false positive 只造成额外 refresh，false negative 不会发生。 | 是 |
