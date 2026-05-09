# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | counter table and service queue | 展示 threshold bit toggle 如何入队。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 4 | Page 4 | counter mat layout | 展示 open-space staggered counter mats。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 5 | Page 5 | incrementer | 展示 counter increment/test logic。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 6 | Page 5 | consecutive tREFI attack | 分析连续刷新间隔入队攻击时间。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |
| Figure 7 | Page 6 | queue fill attack | 说明 queue 需要额外时间机制。 | 支撑核心论证 | 建议回到 PDF 查看坐标/细节 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table I | Page 2 | state size comparison | Graphene/BlockHammer/TWiCe 的 per-bank/channel/CPU 状态成本。 | 支撑方法或实验理解 | 建议回到 PDF 查看细项 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Threshold bit service rate | Page 3 | counter 入队频率 | row serviced every 2^i activates | 只检测 bit toggle 即可触发服务，避免完整比较。 | 是 |
