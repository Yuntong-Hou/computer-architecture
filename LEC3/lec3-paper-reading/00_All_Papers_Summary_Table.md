# All Papers Summary Table

| 论文 | 研究问题 | 方法 | 数据集/实验 | 主要结论 | 贡献 | 局限 | 我应该重点读哪里 |
|---|---|---|---|---|---|---|---|
| FPGA-Based Near-Memory Acceleration of Modern Data-Intensive Applicat… |  |  |  |  |  |  |  |
| Self-Managing DRAM: A Low-Cost Framework for Enabling Autonomous and … |  |  |  |  |  |  |  |
| DRAM Bender: An Extensible and Versatile FPGA-based Infrastructure to… |  |  |  |  |  |  |  |
| Fundamentally Understanding and Solving RowHammer |  |  |  |  |  |  |  |
| DSAC: Low-Cost Rowhammer Mitigation Using In-DRAM Stochastic and Appr… |  |  |  |  |  |  |  |
| Read Disturbance in High Bandwidth Memory: A Detailed Experimental St… |  |  |  |  |  |  |  |
| Spatial Variation-Aware Read Disturbance Defenses: Experimental Analy… |  |  |  |  |  |  |  |
| Understanding the Security Benefits and Overheads of Emerging Industr… |  |  |  |  |  |  |  |
| Chronus: Understanding and Securing the Cutting-Edge Industry Solutio… |  |  |  |  |  |  |  |
| Variable Read Disturbance: An Experimental Analysis of Temporal Varia… |  |  |  |  |  |  |  |
| Memory-Centric Computing: Solving Computing's Memory Problem |  |  |  |  |  |  |  |
| Accelerating Genome Analysis: A Primer on an Ongoing Journey |  |  |  |  |  |  |  |
| Bit-Exact ECC Recovery (BEER): Determining DRAM On-Die ECC Functions … |  |  |  |  |  |  |  |
| EDEN: Enabling Energy-Efficient, High-Performance Deep Neural Network… |  |  |  |  |  |  |  |
| GenASM: A High-Performance, Low-Power Approximate String Matching Acc… |  |  |  |  |  |  |  |
| Google Workloads for Consumer Devices: Mitigating Data Movement Bottl… |  |  |  |  |  |  |  |
| HARP: Practically and Effectively Identifying Uncorrectable Errors in… |  |  |  |  |  |  |  |
| The Locality Descriptor: A Holistic Cross-Layer Abstraction to Expres… |  |  |  |  |  |  |  |
| Detecting and Mitigating Data-Dependent DRAM Failures by Exploiting C… |  |  |  |  |  |  |  |
| MetaSys: A Practical Open-Source Metadata Management System to Implem… |  |  |  |  |  |  |  |
| A Modern Primer on Processing in Memory |  |  |  |  |  |  |  |
| NATSA: A Near-Data Processing Accelerator for Time Series Analysis |  |  |  |  |  |  |  |
| NERO: A Near High-Bandwidth Memory Stencil Accelerator for Weather Pr… |  |  |  |  |  |  |  |
| Ramulator 2.0: A Modern, Modular, and Extensible DRAM Simulator |  |  |  |  |  |  |  |
| RowHammer: A Retrospective |  |  |  |  |  |  |  |
| RowPress: Amplifying Read Disturbance in Modern DRAM Chips |  |  |  |  |  |  |  |
| SISA: Set-Centric Instruction Set Architecture for Graph Mining on Pr… |  |  |  |  |  |  |  |
| SMASH: Co-designing Software Compression and Hardware-Accelerated Ind… |  |  |  |  |  |  |  |
| The Virtual Block Interface: A Flexible Alternative to the Convention… |  |  |  |  |  |  |  |
| A Case for Richer Cross-layer Abstractions: Bridging the Semantic Gap… |  |  |  |  |  |  |  |
| A 1.1V 16Gb DDR5 DRAM with Probabilistic-Aggressor Tracking, Refresh-… |  |  |  |  |  |  |  |
| The Application Slowdown Model: Quantifying and Controlling the Impac… |  |  |  |  |  |  |  |
| AVATAR: A Variable-Retention-Time (VRT) Aware Refresh for DRAM Systems |  |  |  |  |  |  |  |
| DASH: Deadline-Aware High-Performance Memory Scheduler for Heterogene… |  |  |  |  |  |  |  |
| Flipping Bits in Memory Without Accessing Them: An Experimental Study… |  |  |  |  |  |  |  |
| The Efficacy of Error Mitigation Techniques for DRAM Retention Failur… |  |  |  |  |  |  |  |
| Characterizing Application Memory Error Vulnerability to Optimize Dat… |  |  |  |  |  |  |  |
| Accelerating Pointer Chasing in 3D-Stacked Memory: Challenges, Mechan… |  |  |  |  |  |  |  |
| Memory Scaling: A Systems Architecture Perspective |  |  |  |  |  |  |  |
| MISE: Providing Performance Predictability and Improving Fairness in … |  |  |  |  |  |  |  |
| Panopticon: A Complete In-DRAM Rowhammer Mitigation |  |  |  |  |  |  |  |
| PARBOR: An Efficient System-Level Technique to Detect Data-Dependent … |  |  |  |  |  |  |  |
| Phase-Change Technology and the Future of Main Memory |  |  |  |  |  |  |  |
| Architecting Phase Change Memory as a Scalable DRAM Alternative |  |  |  |  |  |  |  |
| RAIDR: Retention-Aware Intelligent DRAM Refresh |  |  |  |  |  |  |  |
| The Reach Profiler (REAPER): Enabling the Mitigation of DRAM Retentio… |  |  |  |  |  |  |  |
| Revisiting Memory Errors in Large-Scale Production Data Centers: Anal… |  |  |  |  |  |  |  |
| Self-Optimizing Memory Controllers: A Reinforcement Learning Approach |  |  |  |  |  |  |  |
| The RowHammer Problem and Other Issues We May Face as Memory Becomes … |  |  |  |  |  |  |  |
| SoftMC: A Flexible and Practical Open-Source Infrastructure for Enabl… | 如何让研究者用真实 DRAM chips 验证 timing、retention 和 failure mechanisms | FPGA-based programmable memory controller + DDR command-level API | Retention test；recently-refreshed/accessed latency validation；24 chips/3 manufacturers | SoftMC 可复现 retention 行为，也能反驳现有 chips 上不可观察的 latency effect | 开源、易用、可控的 DRAM 实验平台 | PCIe 延迟使其不适合直接系统性能评估；现代 DDR5/HBM 需新平台 | Figure 2-4 架构/API；Figure 5 retention；Figures 7-8 latency |
| Staged Memory Scheduling: Achieving High Performance and Scalability … | CPU-GPU 共享内存中 GPU traffic 降低 CPU request visibility，传统 scheduler 难扩展 | 三阶段 memory scheduling：batch formation、batch scheduling、DRAM command scheduling | 105 CPU-GPU workloads；FR-FCFS/ATLAS/TCM/CFR-FCFS/CTCM；CPU WS、GPU FPS、CGWS、fairness | SMS0.9 提升 CPU/system performance 和 fairness；SMS0 更适合 GPU-priority 场景 | 把 locality、policy、timing 分层，降低硬件复杂度 | p 的动态策略未完整解决；DDR3-era 模型需现代系统重评估 | Figure 1 visibility；Figure 4 架构；Figures 5-8 tradeoff；Table 5 复杂度 |
| A Scalable Processing-in-Memory Accelerator for Parallel Graph Proces… | 大规模图处理随机访问强、局部性差，传统系统受外部 bandwidth 限制 | HMC vault-local PIM cores + message passing + graph-aware prefetching | PageRank/SSSP/Conductance/Vertex Cover 等；真实图 LJ/WK/IC；DDR3/HMC/Tesseract baselines | Tesseract 平均 10x/14x 级性能收益并显著降低能耗，瓶颈转向通信和分区 | 展示 PIM 需要数据布局、编程模型和预取协同 | 需要专用 API；不支持 VM；大规模下 off-chip communication 仍限制 | Figure 3 架构；Figure 4 MTP；Figure 6 性能；Figures 10-14 预取/scaling/能耗 |
| Understanding and Modeling On-Die Error Correction in Modern DRAM: An… | 不可见 on-die ECC 遮蔽真实 DRAM physical error behavior | EIN MAP inference + EINSim Monte Carlo 模拟候选 ECC schemes 和 error distributions | 232 个带 on-die ECC LPDDR4 + 82 个无 on-die ECC LPDDR4；retention errors | 推断被测 devices 使用 (136,128,3) Hamming SEC，并恢复 pre-correction error trend | 为现代 DRAM characterization 提供 ECC-aware 方法 | 只能在候选模型中选择；不能定位 bit-exact pre-correction errors | Figure 1 ECC obfuscation；Figure 4 EINSim；Figure 8/Table 2 推断；Figure 11 温度趋势 |
