# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| EDEN | EDEN 框架 | Page 1, Page 3 | 用 approximate DRAM 加速/节能 DNN inference | 是 |
| Approximate DRAM | 近似 DRAM | Page 1 | 降低 voltage/latency 换取更高 BER 的 DRAM | 是 |
| Curricular Retraining | 课程式再训练 | Page 4 | 逐步提高 error rate 的 retraining | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 3-11 | approximate DRAM 错误强度指标 | 是 |
| IFM/OFM | 输入/输出特征图 | Page 2 | DNN layer 的主要数据类型 | 是 |
| DNN-to-DRAM Mapping | DNN 到 DRAM 映射 | Page 4-5 | 按 tolerance 将数据放入不同 partitions | 是 |
| VDD | 供电电压 | Page 1-3 | 降低可节省 DRAM energy | 是 |
| tRCD/tRAS/tRP | DRAM timing 参数 | Page 3 | 降低可降低 latency 但增错 | 是 |
| Accuracy Collapse | 精度崩溃 | Page 4, Page 9 | 高 error rate 训练导致 accuracy 突降 | 是 |
| Error Model | 错误模型 | Page 6-8 | 模拟真实 approximate DRAM errors 的概率模型 | 是 |
