# Limitations and Questions

## 1. 作者明确承认的局限
- MEMCON 明确不检测所有可能的 data-dependent failures，只检测当前内容会触发的失效。（Page 1, Abstract）
- runtime testing 有额外读写和 latency 成本，需要写间隔足够长才有收益。（Page 4-5, Section 3.2-3.3）

## 2. 论文中隐含的局限
- 若 workload 写入频繁或内容 churn 高，PRIL 难以找到足够多长间隔，收益会下降。（推断，基于 MinWriteInterval and Pareto predictor）
- 低刷新安全性依赖测试覆盖当前内容下的失效；极低概率、温度变化或 aging 影响需要额外保护。（推断，基于 runtime testing model）

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
- 系统不知道 DRAM 内部组织时，能否仍在线检测有实际风险的 data-dependent failures？
- 只检测当前 memory content 是否足以支持降低大多数行的 refresh rate？
- runtime testing 什么时候值得做，什么时候成本超过收益？
- write intervals 的分布是否能预测测试后内容保持时间？

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。
