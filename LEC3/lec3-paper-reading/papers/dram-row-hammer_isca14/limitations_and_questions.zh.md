# Limitations and Questions

## 1. 作者明确承认的局限
- 提高 refresh rate 可以消除测试错误，但需要大幅增加 refresh，带来功耗/性能开销。（Page 9, Section 7.2）
- PARA 需要 memory controller 在 row close 时能以概率刷新 adjacent rows，依赖邻接关系和控制器支持。（Page 9-10, Section 7.4）

## 2. 论文中隐含的局限
- 本文主要研究 DDR3-era modules；DDR4/DDR5/HBM 的表现需要后续论文重新测量。（推断，基于 sample scope）
- 安全 exploit 只展示 bit flips，可利用性还取决于 OS memory allocation、page deduplication、ECC/TRR 等系统因素。（推断，基于 user-level demo）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 真实 commodity DRAM 是否普遍存在 disturbance errors？
- 最少需要多少 activations 才能触发 bit flips？
- user-level 程序能否在普通系统上诱发错误？
- ECC、提高 refresh rate 和 PARA 分别能否缓解 RowHammer？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
