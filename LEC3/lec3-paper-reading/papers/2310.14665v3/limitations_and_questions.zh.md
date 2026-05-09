# Limitations and Questions

## 1. 作者明确承认的局限
- 样本为 6 颗 HBM2 chip，不能覆盖所有厂商、容量和世代；位置：Page 3 Methodology, Page 12 Discussion。
- 芯片内部防护机制是黑盒推断，作者无法直接读取厂商实现；位置：Page 10-11。

## 2. 论文中隐含的局限
- FPGA 测试环境能精确控制访问序列，但真实 GPU/HPC 系统中的调度、cache、memory controller policy 会改变可达攻击模式。
- 对 ECC 的讨论主要基于 bitflip 分布，未完整构建端到端 exploit 或系统级容错评估。

## 3. 实验设计可能存在的问题
- HBM2 样本数量较少，chip-to-chip variation 又很大，因此最坏情况可能未被捕捉。
- tAggON 极端设置对真实系统代表性需要结合具体 memory controller policy 判断。

## 4. 方法可能不适用的场景
- 对无法控制 row-open time 的系统，RowPress 攻击可行性可能低于实验平台。
- 未来 HBM3/HBM4 可能采用不同内部防护和 ECC，不能直接沿用阈值。

## 5. 我阅读时应该追问的问题
- HBM2 的 address mapping 是否会限制攻击者定位 aggressor/victim row？
- GPU cache/coalescing 是否会削弱或增强可控 hammer pattern？
- 如果外部 ECC 与 on-die ECC 同时存在，Figure 17 的安全含义如何变化？
- RowPress 是否能由正常 HPC kernel 意外触发？

## 6. 后续可以继续阅读的方向
- RowPress ISCA 2023：理解 tAggON 对 DDR4 的影响。
- Spatial Variation-Aware Defenses：把本文空间差异转化为防护策略。
- PRAC/Chronus：理解 JEDEC/industry 方案如何处理更低 NRH。
