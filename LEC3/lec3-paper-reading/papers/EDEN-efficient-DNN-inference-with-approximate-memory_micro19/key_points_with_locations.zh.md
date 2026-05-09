# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | DNN 对 bit errors 有内在容忍性 | Page 1-2 | input/weight/output data types 可承受一定 errors | 高 | EDEN 的算法前提 |
| 2 | 降低 DRAM VDD/latency 可节能/加速但增加 BER | Page 1-2, Background | DRAM reliability-performance tradeoff | 高 | EDEN 的硬件前提 |
| 3 | EDEN 三步：retraining、characterization、mapping | Page 3-4, Figure 4 | 框架图和 Section 3 | 高 | 全文核心机制 |
| 4 | curricular retraining 逐步增加 error rate 避免 accuracy collapse | Page 4, Section 3.2 | progressive error injection | 高 | 与普通 retraining 的关键差异 |
| 5 | EDEN error models 来自真实 DDR4 modules | Page 6-7, Figure 5-8 | reduced voltage/latency 错误表征 | 高 | 不只是 uniform random faults |
| 6 | tolerable BER 在 layer/data type 间差异大 | Page 10-11, Figure 11-12 | weights 通常比 IFMs 更耐错，首/末层更敏感 | 高 | 支持 fine-grained mapping |
| 7 | curricular retraining 提升 BER tolerance 5-10x | Page 10, Figure 9-10 | good-fit error model + curriculum 明显右移 accuracy curve | 高 | 主要算法结果 |
| 8 | CPU 平均 DRAM energy saving 21%，speedup 8% | Page 11-12, Figure 13-14 | <1% accuracy loss | 高 | 系统收益主结果 |
| 9 | GPU/Eyeriss/TPU 也有 energy benefit | Page 12 | GPU 37%，Eyeriss 31%，TPU 32% energy reduction | 高 | 说明框架跨架构 |
| 10 | speedup 只在 latency-bound DNN 明显 | Page 12 | Eyeriss/TPU reduced tRCD 无 speedup，prefetch/dataflow 有效 | 中 | EDEN 的性能收益有条件 |
