# Open Questions

| 编号 | 问题 | 相关论文 | 原文位置 | 为什么重要 | 下一步建议 |
|---|---|---|---|---|---|
| 1 | 现代 DDR5/HBM 的 RowHammer/RowPress/RFM/TRR 真实防护边界是什么？ | dram-row-hammer, RowHammer-Retrospective, RowPress, panopticon, a-1.1v DDR5, 2106/2207/2211/2502/2505 arXiv papers | 各论文 RowHammer/mitigation sections | 这是 reliability-security 主线的核心未决问题。 | 汇总最新 DDR5/HBM attack 和 mitigation 论文，按 threshold、coverage、false positive、状态开销比较。 |
| 2 | on-die ECC 会如何改变未来所有 DRAM characterization 的可比性？ | understanding-and-modeling-in-DRAM-ECC, Reaper, SoftMC, HARP, MEMCON | EIN Figures 1/8/11; Reaper Sections 5-6 | 如果不建模 ECC，错误率和分布可能被系统性误读。 | 以后读任何 DRAM 实验论文时先检查设备是否有 on-die ECC 以及作者是否处理。 |
| 3 | retention profiling 如何在 VRT、DPD、温度变化和系统开销之间取得稳定折中？ | RAIDR, AVATAR, Reaper, error-mitigation, HARP | Reaper Figures 9-13; AVATAR/RAIDR evaluation | refresh reduction 的收益取决于 profile 是否长期有效。 | 比较 offline、online、ECC-assisted、guardband-based profiling 方案。 |
| 4 | PIM/NDP 真正落地的瓶颈是硬件、编程模型还是数据布局？ | ModernPrimerOnPIM, Google PIM, Tesseract, SISA, SMASH, GenASM, NERO, NATSA | 各 PIM papers architecture/evaluation sections | 多数 PIM 论文收益明显，但软件栈和部署复杂度决定实际采用。 | 按 workload 类型整理 PIM 适配条件：随机访问、低计算密度、数据布局可控性。 |
| 5 | memory scheduling 在现代 heterogeneous CPU-GPU-NPU 系统中是否仍适合传统指标？ | RLMC, MISE, ASM, SMS, DASH | SMS Equations 1-4; MISE/ASM model sections | Weighted speedup/fairness/QoS 指标可能不足以表达交互式 GPU/NPU workload。 | 补读现代 QoS、real-time GPU 和 CXL tier scheduling 论文。 |
| 6 | cross-layer metadata 接口如何既有用又不破坏抽象边界？ | VBI, X-MEM, MetaSys, LocalityDescriptor | 各论文 interface/design sections | 许多 memory 优化都需要额外语义，但跨层接口很难标准化。 | 总结每篇暴露的 metadata 类型、使用方、硬件改动和兼容性风险。 |
| 7 | PCM/NVM 早期结论在当前存储级内存和持久内存生态中还成立吗？ | pcm_isca09, pcm_ieee_micro10, memory-scaling | PCM figures/tables; Memory Scaling sections | 早期参数可能变化，但 endurance、write energy、persistence 问题仍重要。 | 查找后续 Optane/NVM/SCM 真实系统研究补齐时间线。 |
| 8 | 这些论文中的实验基础设施是否足以复现？ | Ramulator2, SoftMC, PARBOR, Panopticon, EINSim | metadata code/project fields; extraction logs | 可复现性决定后续研究能否构建在这些工作之上。 | 优先尝试 Ramulator2、SoftMC、EINSim、PARBOR 公开代码，记录可运行环境。 |
