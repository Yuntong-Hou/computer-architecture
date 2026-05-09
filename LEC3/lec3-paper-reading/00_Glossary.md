# Global Glossary

| English Term | 中文翻译 | 出现论文 | 简明解释 | 重要程度 |
|---|---|---|---|---|
| near-memory computing | 近内存计算 | 2106.06433v2 | 把计算逻辑放到接近内存的位置，减少远距离数据搬移 | 是 |
| HBM | 高带宽内存（High Bandwidth Memory） | 2106.06433v2 | 与 FPGA 同封装的高带宽内存，提供多个 pseudo channels | 是 |
| FPGA | 现场可编程门阵列（Field-Programmable Gate Array） | 2106.06433v2 | 可重构硬件，用于实现应用专用加速器 | 是 |
| pre-alignment filtering | 预比对过滤 | 2106.06433v2, AcceleratingGenomeAnalysis_ieeemicro20 | 在完整 sequence alignment 前快速过滤不相似序列 | 是 |
| SneakySnake | SneakySnake 过滤算法 | 2106.06433v2 | 将 approximate string matching 转换为 single net routing 的高并行过滤器 | 是 |
| COSMO | COSMO 天气预测模型 | 2106.06433v2, NERO-near-memory-stencil-acceleration-for-weather_fpl20 | Consortium for Small-Scale Modeling，本文用其中 kernels 做案例 | 是 |
| stencil kernel | stencil 计算核 | 2106.06433v2 | 在网格上访问邻域数据的数值计算模式 | 是 |
| PE | 处理单元（Processing Element） | 2106.06433v2 | FPGA 中并行执行 kernel 部分工作的计算单元 | 是 |
| OCAPI | Open Coherent Accelerator Processor Interface | 2106.06433v2 | POWER9 与 FPGA 的 cache-coherent interconnect | 是 |
| CAPI2 | Coherent Accelerator Processor Interface 2 | 2106.06433v2, NERO-near-memory-stencil-acceleration-for-weather_fpl20 | 另一种 POWER-FPGA coherent interconnect | 中 |
| BRAM / URAM | 块 RAM / UltraRAM | 2106.06433v2 | FPGA 上的片上存储资源，用于缓存和构建数据流 | 是 |
| arithmetic intensity | 算术强度 | 2106.06433v2 | 每 byte 数据对应的计算量；低值通常意味着 memory-bound | 是 |
| energy efficiency | 能效 | 2106.06433v2 | 每瓦性能，本文以 Mseq/s/Watt 或 GFLOPS/Watt 表示 | 是 |
| Self-Managing DRAM (SMD) | 自管理 DRAM | 2207.13358v9, 2505.00458v2 | 让 DRAM 自主执行维护操作的框架 | 是 |
| maintenance operation | 维护操作 | 2207.13358v9 | refresh、RowHammer protection、scrubbing 等保持可靠性的操作 | 是 |
| ACT_NACK | 激活拒绝信号 | 2207.13358v9 | DRAM 拒绝对锁定区域的 ACT command 的信号 | 是 |
| lock region | 锁定区域 | 2207.13358v9 | bank 中可被维护机制临时锁定的小区域 | 是 |
| Lock Controller | 锁控制器 | 2207.13358v9 | 记录并管理 region 是否正在维护的结构 | 是 |
| ACT Retry Interval (ARI) | ACT 重试间隔 | 2207.13358v9 | MC 收到 ACT_NACK 后等待的时间 | 是 |
| DRAM refresh | DRAM 刷新 | 2207.13358v9 | 周期性恢复 DRAM cell 电荷 | 是 |
| RowHammer protection | RowHammer 防护 | 2207.13358v9 | 防止高频激活 aggressor row 导致 victim row bit-flip | 是 |
| memory scrubbing | 内存巡检/擦洗 | 2207.13358v9 | 定期读取并纠正内存错误 | 是 |
| DARP | Dynamic Access Refresh Parallelization | 2207.13358v9 | memory controller 侧的 refresh scheduling/parallelization 技术 | 中 |
| DSARP | Dynamic Subarray Access Refresh Parallelization | 2207.13358v9 | 支持 subarray-level refresh-access parallelization 的机制 | 中 |
| No-Refresh | 无刷新 oracle | 2207.13358v9 | 假想完全消除维护开销的上界 | 中 |
| SMD-FR | SMD fixed-rate refresh | 2207.13358v9 | 固定频率的 SMD refresh 实现 | 是 |
| SMD-VR | SMD variable-rate refresh | 2207.13358v9 | 基于 retention variation 的 SMD refresh | 是 |
| SMD-PRP | SMD probabilistic RowHammer protection | 2207.13358v9 | SMD 版概率 RowHammer 防护 | 是 |
| SMD-DRP | SMD deterministic RowHammer protection | 2207.13358v9 | SMD 版确定性 RowHammer 防护 | 是 |
| SMD-MS | SMD memory scrubbing | 2207.13358v9 | SMD 版内存巡检 | 是 |
| DRAM Bender | DRAM Bender 测试平台 | 2211.05838v6 | FPGA-based open source DRAM testing infrastructure | 是 |
| DRAM testing infrastructure | DRAM 测试基础设施 | 2211.05838v6 | 用于直接实验真实 DRAM chip 的平台 | 是 |
| SoftMC | SoftMC | 2211.05838v6, softMC_hpca17 | 早期 FPGA-based DRAM testing infrastructure | 是 |
| LiteX RowHammer Tester (LRT) | LiteX RowHammer Tester | 2211.05838v6 | 另一个开源 RowHammer 测试平台 | 是 |
| DFI | DDR PHY Interface | 2211.05838v6 | memory controller 与 PHY 之间的标准接口 | 中 |
| RowHammer | RowHammer 行锤击 | 2211.05838v6, 2211.07613v2, 2302.03591v1, 2310.14665v3, 2505.00458v2, RowHammer-Retrospective_ieee_tcad19 等 | 高频激活 aggressor row 导致 victim row bit-flips | 是 |
| aggressor row | 攻击行/侵扰行 | 2211.05838v6, 2211.07613v2, dram-row-hammer_isca14 | 被反复激活的 row | 是 |
| victim row | 受害行 | 2211.05838v6, 2211.07613v2, dram-row-hammer_isca14 | 发生 bit-flips 的邻近 row | 是 |
| interleaving parameter T | 交替参数 T | 2211.05838v6 | 切换 aggressor 前连续 hammer 的次数 | 是 |
| HCfirst | 首次翻转 hammer count | 2211.05838v6, 2310.14665v3, 2402.18652v1 | 出现第一个 bit-flip 前所需 ACT commands | 是 |
| data pattern | 数据模式 | 2211.05838v6 | 初始化 rows 的 bit pattern | 是 |
| in-DRAM bitwise operation | DRAM 内部位运算 | 2211.05838v6 | 通过 DRAM analog behavior 实现 AND/OR | 是 |
| BER | 位错误率（Bit Error Rate） | 2211.05838v6 | in-DRAM operation 结果错误比例 | 是 |
| ACT / PRE | 激活 / 预充电命令 | 2211.05838v6 | DRAM low-level commands | 是 |
| bit-flip | 位翻转 | 2211.07613v2 | DRAM cell 数据从 0 到 1 或 1 到 0 的错误 | 是 |
| RowHammer threshold | RowHammer 阈值 | 2211.07613v2 | 触发 bit-flip 所需的 aggressor activation 次数 | 是 |
| TRR | Target Row Refresh | 2211.07613v2, 2302.03591v1 | 工业界用于刷新 potential victim rows 的 RowHammer mitigation umbrella term | 是 |
| pTRR | pseudo Target Row Refresh | 2211.07613v2 | memory controller 侧 victim row refresh 机制 | 中 |
| TRRespass | TRRespass | 2211.07613v2 | many-sided RowHammer attack，绕过 TRR | 是 |
| Revisiting RowHammer | Revisiting RowHammer | 2211.07613v2 | 大规模真实芯片实验，证明 RowHammer worsening | 是 |
| RFM | Refresh Management | 2211.07613v2, 2406.19094v3, 2502.12650v2, a-1.1v-16gb-ddr5-dram_isscc2023 | DDR5 中辅助 in-DRAM mitigation 的命令/机制 | 是 |
| system-memory cooperation | 系统-内存协同 | 2211.07613v2 | 系统侧与 DRAM 侧共同设计 RowHammer defenses | 是 |
| security by obscurity | 依赖隐藏细节的安全 | 2211.07613v2 | TRR 不公开实现但仍被逆向/绕过 | 中 |
| DSAC | DRAM 内随机与近似计数算法 | 2302.03591v1 | 用 Stochastic Replacement + Approximate Counting 的 RowHammer mitigation | 是 |
| decoy-row | 诱饵行 | 2302.03591v1 | 访问次数不足以成为真正 RowHammer 但会污染 count table 的 row | 是 |
| Stochastic Replacement | 随机替换 | 2302.03591v1 | 以概率决定新 row 是否替换 min-count row | 是 |
| Approximate Counting | 近似计数 | 2302.03591v1 | 用低成本结构近似保留计数信息 | 是 |
| Passing Gate Effect | 传递栅效应 | 2302.03591v1 | row activation time 过长导致邻近 cell bit-flip | 是 |
| Time-Weighted Counting | 时间加权计数 | 2302.03591v1 | 根据 activation time 增加 count weight | 是 |
| RHTH | RowHammer threshold | 2302.03591v1 | 触发 RowHammer bit-flip 的 activation 阈值 | 是 |
| MR4 | Mode Register 4 | 2302.03591v1 | 控制 refresh command interval 的标准特性 | 中 |
| MPA | Maximum Possible Activations | 2302.03591v1 | 一个 refresh window 内可能发生的最大 activation 数 | 中 |
| Maximum Disturbance | 最大扰动 | 2302.03591v1 | observation period 内最大累积 activation | 是 |
| Graphene | Graphene RowHammer defense | 2302.03591v1, 2406.19094v3 | state-of-the-art counter-based mitigation baseline | 是 |
| CACTI | CACTI 6.0 | 2302.03591v1 | 用于估算 area/energy/power 的建模工具 | 中 |
| High Bandwidth Memory (HBM2) | 高带宽内存 HBM2 | 2310.14665v3 | 3D-stacked DRAM，提供高带宽接口 | 是 |
| Read Disturbance | 读扰动 | 2310.14665v3, 2402.18652v1 | 读取/激活某些 row 对邻近 row 造成电气干扰 | 是 |
| RowPress | 行压迫 | 2310.14665v3, 2505.00458v2, RowPress_isca23 | 延长 aggressor row open 时间造成更强扰动 | 是 |
| Bit Error Rate (BER) | 位错误率 | 2310.14665v3, 2402.18652v1, EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | bitflip 数相对测试位数的比例 | 是 |
| tAggON | aggressor row 开启时间 | 2310.14665v3, 2502.13075v1, RowPress_isca23 | RowPress 中 aggressor row 保持 open 的时间 | 是 |
| TRR-like Defense | 类 TRR 防护 | 2310.14665v3 | 片内跟踪高 activation row 并刷新 victim 的机制 | 是 |
| Dummy Row | 干扰/填充 row | 2310.14665v3 | 用于影响内部 tracking 的额外访问 row | 是 |
| ECC Word | ECC 码字 | 2310.14665v3 | ECC 进行错误检测/纠正的粒度 | 中 |
| Spatial Variation | 空间变化 | 2402.18652v1, 2502.13075v1 | 不同物理位置 row 的脆弱性差异 | 是 |
| Subarray | 子阵列 | 2402.18652v1 | DRAM bank 内共享局部电路的 row group | 是 |
| Svärd | 空间变化感知防护框架 | 2402.18652v1 | 根据 row vulnerability profile 调整防护强度 | 是 |
| AQUA | RowHammer 防护方案 | 2402.18652v1 | Svärd 评估中的 base mitigation | 中 |
| BlockHammer | RowHammer 防护方案 | 2402.18652v1 | 通过限制高风险访问降低攻击能力 | 中 |
| Hydra | RowHammer 防护方案 | 2402.18652v1, 2406.19094v3 | 计数/跟踪型防护 | 中 |
| PARA | Probabilistic Adjacent Row Activation | 2402.18652v1, 2406.19094v3, RowHammer-Retrospective_ieee_tcad19, dram-row-hammer_isca14, rowhammer-and-other-memory-issues_date17 | 概率刷新相邻 row 的经典方案 | 是 |
| RRS | Reactive Refresh Scheme | 2402.18652v1 | 响应式刷新防护 | 中 |
| PRAC | Per-Row Activation Counting | 2406.19094v3, 2502.12650v2 | DDR5 中片内跟踪 row activation 的机制 | 是 |
| Back-off Signal | 回退信号 | 2406.19094v3 | DRAM 通知控制器暂停普通请求并执行 RFM | 是 |
| NRH | RowHammer threshold | 2406.19094v3, 2502.12650v2 | 触发 RowHammer bitflip 所需 activation 数 | 是 |
| tRP/tRC | DRAM timing 参数 | 2406.19094v3 | precharge/row cycle 等关键时序 | 是 |
| Memory Performance Attack | 内存性能攻击 | 2406.19094v3 | 利用防护机制降低系统吞吐 | 是 |
| Chronus | Chronus 防护机制 | 2502.12650v2 | 改进 PRAC 的片内/控制器协同防护 | 是 |
| Preventive Refresh | 预防性刷新 | 2502.12650v2 | 在 bitflip 前刷新潜在 victim row | 是 |
| Wave Attack | 波形攻击 | 2502.12650v2 | 利用固定刷新/延迟窗口累积扰动的攻击 | 是 |
| Feinting Attack | 佯攻攻击 | 2502.12650v2 | 诱导防护误判或分散资源的访问模式 | 是 |
| Delay Period | 延迟期 | 2502.12650v2 | RFM 后控制器/DRAM 等待窗口 | 是 |
| Counter-Data Separation | 计数器与数据路径分离 | 2502.12650v2 | Chronus 避免计数更新阻塞关键路径的设计 | 是 |
| Variable Read Disturbance (VRD) | 可变读扰动 | 2502.13075v1, 2505.00458v2 | 同一 row 的 RDT 随时间变化 | 是 |
| Read Disturbance Threshold (RDT) | 读扰动阈值 | 2502.13075v1 | 触发 bitflip 所需 activation/access 数 | 是 |
| Temporal Variation | 时间变化 | 2502.13075v1 | 同一对象随时间的脆弱性变化 | 是 |
| Guardband | 安全裕量 | 2502.13075v1, error-mitigation-for-intermittent-dram-failures_sigmetrics14 | 在测得阈值基础上进一步保守设置 | 是 |
| SECDED | Single Error Correction, Double Error Detection | 2502.13075v1 | 常见 ECC 能力 | 中 |
| Chipkill-like SSC | 类 Chipkill 符号级纠错 | 2502.13075v1 | 更强 ECC 组织形式 | 中 |
| Online RDT Profiling | 在线 RDT 剖析 | 2502.13075v1 | 运行时更新阈值估计 | 是 |
| Memory-Centric Computing (MCC) | 以内存为中心的计算 | 2505.00458v2 | 让 memory 能自主管理和/或执行计算的范式 | 是 |
| Processor-Centric Paradigm | 以处理器为中心的范式 | 2505.00458v2 | memory 被动响应 processor 请求 | 是 |
| Processing in Memory (PIM) | 存内处理 | 2505.00458v2 | 将计算放入/靠近 memory | 是 |
| Processing Near Memory (PNM) | 近内存处理 | 2505.00458v2, ModernPrimerOnPIM_springer-emerging-computing-bookchapter21 | 在 memory 附近增加逻辑 | 是 |
| Processing Using Memory (PUM) | 利用内存计算 | 2505.00458v2, ModernPrimerOnPIM_springer-emerging-computing-bookchapter21 | 利用 memory array 电路属性直接计算 | 是 |
| CXL | Compute Express Link | 2505.00458v2 | 可用于连接/解耦 PNM devices 的接口 | 中 |
| Read Mapping | 读段映射 | AcceleratingGenomeAnalysis_ieeemicro20 | 将 reads 定位到 reference genome | 是 |
| Approximate String Matching (ASM) | 近似字符串匹配 | AcceleratingGenomeAnalysis_ieeemicro20, GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 允许 insertion/deletion/substitution 的匹配 | 是 |
| Indexing | 索引 | AcceleratingGenomeAnalysis_ieeemicro20 | 用 seeds 找候选位置 | 是 |
| Sequence Alignment | 序列比对 | AcceleratingGenomeAnalysis_ieeemicro20 | 精确计算 read 与 reference segment 的相似性 | 是 |
| Edit Distance | 编辑距离 | AcceleratingGenomeAnalysis_ieeemicro20 | 两序列之间最少 edits 数 | 是 |
| q-gram Filtering | q-gram 过滤 | AcceleratingGenomeAnalysis_ieeemicro20 | 用长度 q 的子串判断相似性 | 中 |
| Pigeonhole Principle | 鸽巢原理 | AcceleratingGenomeAnalysis_ieeemicro20 | 若相似序列至多 E edits，则存在无错片段 | 中 |
| FASTQ/FASTA | 基因组数据格式 | AcceleratingGenomeAnalysis_ieeemicro20 | 常用 reads/reference 表示格式 | 中 |
| GenASM | GenASM 加速框架 | AcceleratingGenomeAnalysis_ieeemicro20, GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | bitvector-based ASM 加速框架 | 是 |
| On-Die ECC | 片上 ECC | BEER-bit-exact-ECC-recovery_micro20, HARP-memory-error-profiling_micro21, understanding-and-modeling-in-DRAM-ECC_dsn19 | DRAM 芯片内部不可见纠错机制 | 是 |
| BEER | Bit-Exact ECC Recovery | BEER-bit-exact-ECC-recovery_micro20 | 恢复完整 on-die ECC function 的方法 | 是 |
| BEEP | Bit-Exact Error Profiling | BEER-bit-exact-ECC-recovery_micro20 | 利用已知 ECC function 恢复 raw error locations | 是 |
| Parity-Check Matrix | 校验矩阵 | BEER-bit-exact-ECC-recovery_micro20, HARP-memory-error-profiling_micro21 | 定义线性 ECC function 的矩阵 | 是 |
| Miscorrection | 误纠正 | BEER-bit-exact-ECC-recovery_micro20 | ECC 在 uncorrectable pattern 下翻转非错误 bit | 是 |
| Pre-Correction Error | 纠错前错误 | BEER-bit-exact-ECC-recovery_micro20, understanding-and-modeling-in-DRAM-ECC_dsn19 | 物理上真实发生的 raw bit error | 是 |
| Post-Correction Error | 纠错后可见错误 | BEER-bit-exact-ECC-recovery_micro20, understanding-and-modeling-in-DRAM-ECC_dsn19 | ECC 作用后软件可观察的错误 | 是 |
| SAT Solver | 可满足性求解器 | BEER-bit-exact-ECC-recovery_micro20 | 求解布尔约束的工具 | 是 |
| Data-Retention Error | 数据保持错误 | BEER-bit-exact-ECC-recovery_micro20 | refresh 间隔过长导致 cell 电荷丢失 | 是 |
| SEC Hamming Code | 单错纠正 Hamming 码 | BEER-bit-exact-ECC-recovery_micro20 | on-die ECC 可能采用的线性纠错码 | 中 |
| EDEN | EDEN 框架 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 用 approximate DRAM 加速/节能 DNN inference | 是 |
| Approximate DRAM | 近似 DRAM | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 降低 voltage/latency 换取更高 BER 的 DRAM | 是 |
| Curricular Retraining | 课程式再训练 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 逐步提高 error rate 的 retraining | 是 |
| IFM/OFM | 输入/输出特征图 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | DNN layer 的主要数据类型 | 是 |
| DNN-to-DRAM Mapping | DNN 到 DRAM 映射 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 按 tolerance 将数据放入不同 partitions | 是 |
| VDD | 供电电压 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 降低可节省 DRAM energy | 是 |
| tRCD/tRAS/tRP | DRAM timing 参数 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 降低可降低 latency 但增错 | 是 |
| Accuracy Collapse | 精度崩溃 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 高 error rate 训练导致 accuracy 突降 | 是 |
| Error Model | 错误模型 | EDEN-efficient-DNN-inference-with-approximate-memory_micro19 | 模拟真实 approximate DRAM errors 的概率模型 | 是 |
| Bitap | Bitap 算法 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | bitvector-based ASM algorithm | 是 |
| GenASM-DC | distance calculation 单元 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 生成 bitvectors 并计算 edit distance | 是 |
| GenASM-TB | traceback 单元 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 从 bitvectors 恢复 alignment/CIGAR | 是 |
| Systolic Array | 脉动阵列 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 高并行硬件结构 | 是 |
| DC-SRAM/TB-SRAM | DC/TB 专用 SRAM | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 存储中间 bitvectors，降低带宽 | 是 |
| CIGAR String | CIGAR 字符串 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | 表示 alignment edits 的格式 | 中 |
| False Accept Rate | 错误接受率 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | dissimilar sequences 被误认为相似 | 是 |
| False Reject Rate | 错误拒绝率 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | similar sequences 被误丢弃 | 是 |
| 3D-Stacked Memory | 3D 堆叠内存 | GenASM-approximate-string-matching-framework-for-genome-analysis_micro20 | logic layer + vault parallelism | 是 |
| Processing-in-Memory (PIM) | 存内/近存处理 | Google-consumer-workloads-data-movement-and-PIM_asplos18, ModernPrimerOnPIM_springer-emerging-computing-bookchapter21, tesseract-pim-archit… | 把部分计算放到 memory logic 附近，以减少主存到 CPU/GPU/accelerator 的数据搬移。 | 是 |
| PIM target | PIM 目标函数 | Google-consumer-workloads-data-movement-and-PIM_asplos18 | 能耗占比较高、以数据移动为主、适合简单近存逻辑执行的函数或 primitive。 | 是 |
| PIM core | PIM 通用核心 | Google-consumer-workloads-data-movement-and-PIM_asplos18 | 低功耗通用 embedded core，可服务多种 target。 | 是 |
| PIM accelerator | PIM 专用加速器 | Google-consumer-workloads-data-movement-and-PIM_asplos18 | 面向特定 target 的 fixed-function logic，通常收益更高但面积更大。 | 是 |
| Texture tiling | 纹理分块 | Google-consumer-workloads-data-movement-and-PIM_asplos18 | Chrome 渲染中把 bitmap 转成 tiled texture 的数据整理步骤。 | 是 |
| Direct error | 直接错误 | HARP-memory-error-profiling_micro21 | ECC word 数据部分 raw bit error 直接导致的 post-correction error。 | 是 |
| Indirect error | 间接错误 | HARP-memory-error-profiling_micro21 | on-die ECC 在不可纠正错误上发生 miscorrection 后引入的错误。 | 是 |
| Hybrid Active-Reactive Profiling (HARP) | 混合主动-反应式错误画像 | HARP-memory-error-profiling_micro21 | 先主动识别 direct errors，再运行时安全发现 indirect errors 的 profiling 算法。 | 是 |
| Locality Descriptor | 局部性描述符 | LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18 | 软件表达数据结构局部性、tile 关系和优化意图的跨层抽象。 | 是 |
| CTA scheduling | CTA 调度 | LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18 | 把共享数据的 Cooperative Thread Arrays 调度到相同/相近资源上以提高局部性。 | 是 |
| Reuse-based locality | 基于复用的局部性 | LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18 | 为了提高 cache 利用率而关注数据复用关系。 | 是 |
| NUMA locality | NUMA 局部性 | LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18 | 把数据放到使用它的线程附近，减少远端访问。 | 是 |
| INTRA-THREAD / INTER-THREAD / NO-REUSE | 线程内/线程间/无复用局部性类型 | LocalityDescriptor-Cross-Layer-GPU-Data-Locality-Abstraction_isca18 | descriptor 中驱动底层优化选择的 locality type。 | 是 |
| Data-dependent failure | 数据相关失效 | MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17, parbor-efficient-system-level-test-for-DRAM-failures_dsn16 | DRAM cell 是否失效依赖邻近 cell 中存储的数据内容。 | 是 |
| MEMCON | 基于内存内容的检测/缓解机制 | MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17 | 运行时只测试当前内容触发的失效，并据此调节 refresh。 | 是 |
| MinWriteInterval | 最小写间隔 | MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17 | 测试成本能被后续低刷新收益摊销所需的最短内容保持时间。 | 是 |
| PRIL | 概率式剩余间隔长度预测器 | MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17 | 利用 Pareto 分布性质预测页面写后还会保持多久。 | 是 |
| Aggressive refresh | 激进刷新 | MEMCON-system-level-data-dependent-DRAM-failure-detection-mitigation_micro17 | 用更短刷新间隔保护所有行，可靠但性能/能耗成本高。 | 是 |
| Metadata | 元数据 | MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv | 软件传给硬件的额外语义信息，如访问模式、bounds、reuse 等。 | 是 |
| Tagged memory | 带标签内存 | MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv | 每个地址关联 tag ID，再由 ID 指向对应 metadata。 | 是 |
| Metadata Mapping Table (MMT) | 元数据映射表 | MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv | 保存地址范围到 tag ID 的映射，通常在内存中由 OS 管理。 | 是 |
| Metadata Mapping Cache (MMC) | 元数据映射缓存 | MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv | 缓存常用 MMT 映射，减少 metadata lookup 开销。 | 是 |
| Private Metadata Table (PMT) | 私有元数据表 | MetaSys-open-source-cross-layer-metadata-management_taco22-arxiv | 靠近具体 optimization component 存储该模块需要的 metadata。 | 是 |
| RowClone | DRAM 内行复制 | ModernPrimerOnPIM_springer-emerging-computing-bookchapter21 | 用连续 ACTIVATE 等方式做低成本 bulk copy/initialization。 | 是 |
| Ambit | DRAM 内位运算机制 | ModernPrimerOnPIM_springer-emerging-computing-bookchapter21 | 利用 triple-row activation 和 sense amplifier 实现 bulk bitwise operations。 | 是 |
| Matrix profile | 矩阵轮廓 | NATSA_time-series-analysis-near-data_iccd20 | 每个 subsequence 与最相似 subsequence 的距离数组。 | 是 |
| Anytime algorithm | 可中断算法 | NATSA_time-series-analysis-near-data_iccd20 | 随时停止也能返回当前有效近似结果的算法。 | 是 |
| Diagonal scheduling | 对角线调度 | NATSA_time-series-analysis-near-data_iccd20 | 按 distance matrix 对角线划分工作，降低同步并保持算法性质。 | 是 |
| High Bandwidth Memory (HBM) | 高带宽内存 | NATSA_time-series-analysis-near-data_iccd20 | 3D-stacked memory，为 near-data accelerator 提供高带宽。 | 是 |
| Processing Unit (PU) | 处理单元 | NATSA_time-series-analysis-near-data_iccd20 | NATSA 中计算 matrix profile 的专用近存单元。 | 是 |
| Compound stencil | 复合 stencil | NERO-near-memory-stencil-acceleration-for-weather_fpl20 | 天气模型中由多种邻域访问和计算模式组合而成的 stencil kernel。 | 是 |
| HBM port | HBM 端口 | NERO-near-memory-stencil-acceleration-for-weather_fpl20 | PE 访问 HBM 带宽的并行入口。 | 是 |
| Processing Element (PE) | 处理单元 | NERO-near-memory-stencil-acceleration-for-weather_fpl20 | NERO 中执行 stencil 计算的 FPGA 单元。 | 是 |
| Interface / Implementation | 接口/实现 | Ramulator2_arxiv23 | Ramulator 2.0 中解耦组件功能与具体行为的核心抽象。 | 是 |
| Controller plugin | 控制器插件 | Ramulator2_arxiv23 | 不修改 baseline controller 即可接入统计或防御机制。 | 是 |
| DRAM specification syntax | DRAM 规格描述语法 | Ramulator2_arxiv23 | 用简洁字符串和模板函数定义组织、命令、时序和状态。 | 是 |
| Refresh Management (RFM) | 刷新管理 | Ramulator2_arxiv23 | DDR5/LPDDR5/GDDR6/HBM3 等标准中的维护命令之一。 | 是 |
| RowHammer mitigation | RowHammer 缓解机制 | Ramulator2_arxiv23 | PARA/TWiCe/Graphene/Hydra/RRS 等防御插件。 | 是 |
| Disturbance error | 扰动错误 | RowHammer-Retrospective_ieee_tcad19, rowhammer-and-other-memory-issues_date17 | 电路组件间干扰导致非目标 cell 状态改变。 | 是 |
| Memory isolation | 内存隔离 | RowHammer-Retrospective_ieee_tcad19, rowhammer-and-other-memory-issues_date17 | 访问一个地址不应影响其他地址的数据，是系统可靠性和安全的基础。 | 是 |
| Targeted refresh | 定向刷新 | RowHammer-Retrospective_ieee_tcad19 | 只刷新被认为可能受 hammering 影响的相邻行。 | 是 |
| ACmin | 最小触发 activation 数 | RowPress_isca23 | 诱发至少一个 bitflip 所需最小 aggressor activations。 | 是 |
| Graphene-RP / PARA-RP | 适配 RowPress 的 Graphene/PARA | RowPress_isca23 | 同时考虑 row-open time 和 RowHammer threshold 的防御版本。 | 是 |
| Set-centric programming | 集合中心编程 | SISA-GraphMining-on-PIM_micro21 | 把图挖掘表达为 vertex set operations 的范式。 | 是 |
| SISA | 集合中心 ISA | SISA-GraphMining-on-PIM_micro21 | 用于表达和加速 set operations 的 ISA extensions。 | 是 |
| Dense bitvector (DB) | 稠密位向量 | SISA-GraphMining-on-PIM_micro21 | 高 degree vertex sets 的表示，适合 PUM bitwise。 | 是 |
| Sparse array (SA) | 稀疏数组 | SISA-GraphMining-on-PIM_micro21 | 低 degree vertex sets 的整数列表表示，适合 PNM。 | 是 |
| Hierarchical bitmap | 层次化位图 | SMASH-sparse-matrix-software-hardware-acceleration_micro19 | 用多层位图表示哪些块含非零元素。 | 是 |
| Bitmap Management Unit (BMU) | 位图管理单元 | SMASH-sparse-matrix-software-hardware-acceleration_micro19 | 硬件扫描位图层次并返回非零块位置。 | 是 |
| CSR | 压缩稀疏行格式 | SMASH-sparse-matrix-software-hardware-acceleration_micro19 | 常见稀疏矩阵格式，但 indexing/pointer chasing 开销高。 | 是 |
| SpMV / SpMM | 稀疏矩阵向量/矩阵乘法 | SMASH-sparse-matrix-software-hardware-acceleration_micro19 | SMASH 的两个核心稀疏线性代数用例。 | 是 |
| Virtual Block (VB) | 虚拟块 | VBI-virtual-block-interface_isca20 | 全局 VBI address space 中可变大小、语义相关的连续区域。 | 是 |
| Memory Translation Layer (MTL) | 内存翻译层 | VBI-virtual-block-interface_isca20 | memory controller 侧管理 allocation 和 VBI-to-physical translation 的硬件层。 | 是 |
| Client-VB Table (CVT) | 客户端-VB 表 | VBI-virtual-block-interface_isca20 | 记录 process/client 对哪些 VBs 有访问权限。 | 是 |
| VBI address | VBI 地址 | VBI-virtual-block-interface_isca20 | 由 VB ID 和 offset 构成的系统唯一地址。 | 是 |
| Expressive Memory (XMem) | 表达式内存/富语义内存接口 | X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18 | 把程序高层语义传给系统和硬件的跨层接口。 | 是 |
| Atom | 语义原子 | X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18 | 承载数据属性、访问属性和局部性的虚拟内存区域抽象。 | 是 |
| Atom Management Unit (AMU) | Atom 管理单元 | X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18 | 维护 AAM/AST 并服务硬件语义查询。 | 是 |
| Semantic gap | 语义鸿沟 | X-MEM_Expressive-Memory-for-Rich-Cross-Layer-Abstractions_isca18 | 应用知道的高层数据语义无法被 OS/硬件看到。 | 是 |
| PAT | 概率 aggressor 跟踪 | a-1.1v-16gb-ddr5-dram_isscc2023 | 以概率方式追踪可能造成 disturbance 的 aggressor rows。 | 是 |
| PRHT | 逐行 hammer 跟踪 | a-1.1v-16gb-ddr5-dram_isscc2023 | 通过 R/H cells 记录每条 wordline activation count 并触发额外 refresh。 | 是 |
| VBB modulation | 体偏置调制 | a-1.1v-16gb-ddr5-dram_isscc2023 | 随温度调节 core bias 来改善 retention margin。 | 是 |
| Application Slowdown Model (ASM) | 应用 slowdown 模型 | application-slowdown-model_micro15 | 在线估计共享 cache/主存干扰导致应用性能下降的模型。 | 是 |
| Cache Access Rate (CAR) | cache 访问率 | application-slowdown-model_micro15 | 单位时间内 shared cache accesses，用作性能代理。 | 是 |
| Auxiliary Tag Store (ATS) | 辅助 tag 存储 | application-slowdown-model_micro15 | 用于估计应用在无 cache contention 情况下的 cache behavior。 | 是 |
| Soft slowdown guarantee | 软 slowdown 保证 | application-slowdown-model_micro15 | 尽量把目标应用 slowdown 控制在用户给定 bound 内。 | 是 |
| Variable Retention Time (VRT) | 可变保持时间 | avatar-dram-refresh_dsn15, error-mitigation-for-intermittent-dram-failures_sigmetrics14, reaper-dram-retention-profiling-lpddr4_isca17 | DRAM cell retention time 在高/低状态间随机切换的现象。 | 是 |
| Active-VRT Pool (AVP) | 活跃 VRT 池 | avatar-dram-refresh_dsn15 | 给定时间窗口内处于低 retention 状态的 VRT cells 数量。 | 是 |
| Active-VRT Injection (AVI) | 活跃 VRT 注入 | avatar-dram-refresh_dsn15 | 每个时间窗口新进入 active VRT 状态的 cells 数量。 | 是 |
| Multirate refresh | 多速率刷新 | avatar-dram-refresh_dsn15 | 弱 rows 用高频刷新、强 rows 用低频刷新以减少总 refresh。 | 是 |
| DASH | deadline-aware high-performance scheduler | dash_deadline-aware-heterogeneous-memory-scheduler_taco16 | 面向 CPU+HWA 异构系统的内存调度器。 | 是 |
| Distributed Priority | 分散式优先级 | dash_deadline-aware-heterogeneous-memory-scheduler_taco16 | HWA 落后时在整个 period 中分散给予优先，而不是最后集中抢占。 | 是 |
| Deadline-met ratio | deadline 满足率 | dash_deadline-aware-heterogeneous-memory-scheduler_taco16 | HWA frames 在 deadline 前完成的比例。 | 是 |
| Memory-intensive application | 内存密集应用 | dash_deadline-aware-heterogeneous-memory-scheduler_taco16 | 对内存带宽敏感但单请求 latency sensitivity 相对低的 CPU 应用。 | 是 |
| SECDED ECC | 单错纠正双错检测 ECC | dram-row-hammer_isca14 | 常见 ECC，但可能无法修复 RowHammer 多 bit errors。 | 是 |
| Online profiling | 在线画像/在线测试 | error-mitigation-for-intermittent-dram-failures_sigmetrics14 | 系统运行中后台检测 retention failures。 | 是 |
| VS-ECC | 可变强度 ECC | error-mitigation-for-intermittent-dram-failures_sigmetrics14 | 对更易错 cache lines 使用更强 ECC。 | 是 |
| Heterogeneous-reliability memory | 异构可靠性内存 | heterogeneous-reliability-memory-for-data-centers_dsn14 | 在同一系统中对不同应用/region 使用不同可靠性保护。 | 是 |
| Safe ratio | 安全比例 | heterogeneous-reliability-memory-for-data-centers_dsn14 | 用访问/写入模式估计错误被覆盖的可能性。 | 是 |
| Parity + Recovery (Par+R) | 奇偶检测加软件恢复 | heterogeneous-reliability-memory-for-data-centers_dsn14 | 用 parity 检测错误，再从 disk clean copy 恢复。 | 是 |
| Less-Tested DRAM | 较少测试 DRAM | heterogeneous-reliability-memory-for-data-centers_dsn14 | 减少制造测试成本但错误率更高的内存。 | 是 |
| IMPICA | in-memory pointer chasing accelerator | in-memory-pointer-chasing-accelerator_iccd16 | 部署在 3D-stacked memory logic layer 的 pointer traversal 加速器。 | 是 |
| Address-access decoupling | 地址生成-访问解耦 | in-memory-pointer-chasing-accelerator_iccd16 | 在等待 memory access 时处理其他 traversal stream 的地址生成。 | 是 |
| Region-based page table | 区域式页表 | in-memory-pointer-chasing-accelerator_iccd16 | 利用连续 virtual memory regions 简化 PIM-side address translation。 | 是 |
| Pointer chasing | 指针追踪 | in-memory-pointer-chasing-accelerator_iccd16 | 通过当前 node 中的指针访问下一个 node 的串行遍历。 | 是 |
| System-DRAM co-design | 系统-DRAM 协同设计 | memory-scaling_imw13 | 重新设计 DRAM 架构、功能和接口，让 controller/processor/software 共同利用内部结构。 | 是 |
| RAIDR | retention-aware intelligent DRAM refresh | memory-scaling_imw13, raidr-dram-refresh_isca12 | 按 retention bins 差异化刷新 rows。 | 是 |
| SALP | subarray-level parallelism | memory-scaling_imw13 | 暴露并利用 DRAM bank 内 subarray 并行性。 | 是 |
| TL-DRAM | tiered-latency DRAM | memory-scaling_imw13 | 把 long bitline 划分为 low/high-latency segments。 | 是 |
| PCM | phase-change memory | memory-scaling_imw13 | 更可缩放、非易失但写延迟/能耗/耐久性存在挑战的 emerging memory。 | 是 |
| MISE | memory-interference-induced slowdown estimation | mise-predictable_memory_performance-hpca13 | 估计主存干扰导致应用 slowdown 的模型。 | 是 |
| ARSR | alone request-service-rate | mise-predictable_memory_performance-hpca13 | 应用近似独占内存时的请求服务率。 | 是 |
| SRSR | shared request-service-rate | mise-predictable_memory_performance-hpca13 | 应用与其他应用共同运行时的请求服务率。 | 是 |
| MISE-QoS | MISE 驱动的 QoS 调度 | mise-predictable_memory_performance-hpca13 | 给 AoI 分配足够带宽满足 slowdown bound。 | 是 |
| MISE-Fair | MISE 驱动的公平性调度 | mise-predictable_memory_performance-hpca13 | 通过带宽重分配最小化 maximum slowdown。 | 是 |
| Panopticon | in-DRAM RowHammer 防御 | panopticon | 在 DRAM 内部追踪 row activations 并刷新 victim rows 的完整机制。 | 是 |
| ALERTn | DDR4 错误提示信号 | panopticon | 被 Panopticon 复用来暂停 controller 命令流。 | 是 |
| Counter mat | 计数器 mat | panopticon | 与 data mat 共同布局的薄 counter 存储阵列。 | 是 |
| Service queue | 服务队列 | panopticon | 保存达到 threshold 的 aggressor rows，等待刷新 victims。 | 是 |
| PARBOR | Parallel Recursive neighBOR testing | parbor-efficient-system-level-test-for-DRAM-failures_dsn16 | 并行递归定位物理邻居 cell 地址的系统级测试。 | 是 |
| Strongly coupled cell | 强耦合 cell | parbor-efficient-system-level-test-for-DRAM-failures_dsn16 | 只受一个邻居数据内容影响即可失败的 cell。 | 是 |
| DC-REF | data content-based refresh | parbor-efficient-system-level-test-for-DRAM-failures_dsn16 | 仅当弱 row 中出现 worst-case pattern 时高频刷新。 | 是 |
| Phase-change memory (PCM) | 相变存储器 | pcm_ieee_micro10 | 通过 chalcogenide 在 crystalline/amorphous 状态间切换存储数据。 | 是 |
| SET / RESET | 置位/复位相变写入 | pcm_ieee_micro10 | SET 结晶降低电阻，RESET 非晶化提高电阻。 | 是 |
| Redundant bit-write removal | 冗余 bit 写消除 | pcm_ieee_micro10 | 不写入与旧值相同的 bits，降低磨损和能耗。 | 是 |
| Row shifting | 行内位移 | pcm_ieee_micro10 | 周期性移动 row 内写热点以均衡 wear。 | 是 |
| Partial writes | 部分写 | pcm_isca09 | 只把 dirty cache lines/words 写入 PCM array，减少磨损。 | 是 |
| Buffer organization | 缓冲组织 | pcm_isca09 | 通过 buffer width 和 rows 调节写粒度、局部性和 coalescing。 | 是 |
| Write coalescing | 写合并 | pcm_isca09 | 多个 writes 在 buffer 中合并，减少 array writes。 | 是 |
| Endurance | 写入耐久性 | pcm_isca09 | PCM cell 可可靠写入的次数。 | 是 |
| Retention time bin | 保持时间分箱 | raidr-dram-refresh_isca12 | 按需要 refresh interval 将 rows 分组。 | 是 |
| Bloom filter | 布隆过滤器 | raidr-dram-refresh_isca12 | 低开销近似集合，用于存储短 retention rows。 | 是 |
| RAS-only refresh | 按行地址刷新 | raidr-dram-refresh_isca12 | controller 指定 row 进行 refresh，而非标准 auto-refresh。 | 是 |
| Reach profiling | 触达式/激进条件 profiling | reaper-dram-retention-profiling-lpddr4_isca17 | 在比目标更长 refresh interval 或更高温度下 profile 弱 cells。 | 是 |
| Coverage | 覆盖率 | reaper-dram-retention-profiling-lpddr4_isca17 | profile 找到目标条件下所有可能失败 cells 的比例。 | 是 |
| False positive rate | 误报率 | reaper-dram-retention-profiling-lpddr4_isca17 | profile 条件下失败但目标运行条件下不失败的 cells 比例。 | 是 |
| Uncorrectable bit error rate (UBER) | 不可纠错 bit 错误率 | reaper-dram-retention-profiling-lpddr4_isca17 | 系统级不可由 ECC 修正的错误率目标。 | 是 |
| Correctable error (CE) | 可纠错错误 | revisiting-memory-errors_dsn15 | 可由 ECC 修正的内存错误。 | 是 |
| Uncorrectable error (UCE) | 不可纠错错误 | revisiting-memory-errors_dsn15 | ECC 能检测但不能纠正，通常导致系统 crash。 | 是 |
| Page offlining | 页下线 | revisiting-memory-errors_dsn15 | 把出现错误的物理页从 OS 可分配内存中移除。 | 是 |
| Pareto distribution | 帕累托分布 | revisiting-memory-errors_dsn15 | 错误高度集中在少数服务器上的 heavy-tailed 分布。 | 是 |
| DIMM architecture | DIMM 架构 | revisiting-memory-errors_dsn15 | chips per DIMM、transfer width 等组织特征。 | 是 |
| Reinforcement learning (RL) | 强化学习 | rlmc_isca08 | agent 通过环境反馈学习最大化长期 reward 的控制策略。 | 是 |
| FR-FCFS | first-ready first-come first-serve | rlmc_isca08 | 优先 ready column commands 和较老 requests 的传统 DRAM scheduling policy。 | 是 |
| Q-value | 动作价值 | rlmc_isca08 | 估计某状态下采取某动作的长期 reward。 | 是 |
| CMAC | Cerebellar Model Articulation Controller | rlmc_isca08 | 用 coarse-grain tables/hashing 近似 Q-values 的硬件友好结构。 | 是 |
| Data bus utilization | 数据总线利用率 | rlmc_isca08 | 作为 RL reward 的主要目标，反映 sustained DRAM bandwidth。 | 是 |
| System-memory co-design | 系统-内存协同设计 | rowhammer-and-other-memory-issues_date17 | controller、DRAM、系统软件共同暴露/处理可靠性问题。 | 是 |
| DDR command | DDR 命令 | softMC_hpca17 | ACTIVATE/READ/WRITE/PRECHARGE/REFRESH 等控制 DRAM 的标准接口命令。 | 是 |
| Timing parameter | 时序参数 | softMC_hpca17 | tRCD、tRAS、tRP 等命令间最小间隔约束。 | 是 |
| Retention test | 保持时间测试 | softMC_hpca17 | 写入数据、等待指定 refresh interval、读回比较错误。 | 是 |
| RIFFA | FPGA PCIe 通信框架 | softMC_hpca17 | SoftMC host 与 FPGA 间传输 instruction/data 的接口。 | 中 |
| Staged Memory Scheduler (SMS) | 分阶段内存调度器 | staged-memory-scheduling_isca12 | 三阶段、低复杂度、应用感知 memory scheduler。 | 是 |
| Batch formation | 批形成 | staged-memory-scheduling_isca12 | 按 source 和 row locality 把 requests 组成 batch。 | 是 |
| SJF probability | 最短作业优先概率 | staged-memory-scheduling_isca12 | 调节 batch scheduler 偏向短 batch/CPU 或 GPU 的参数 p。 | 是 |
| CGWS | CPU-GPU Weighted Speedup | staged-memory-scheduling_isca12 | 综合 CPU/GPU 性能并用 GPUweight 加权的指标。 | 是 |
| DCS FIFO | DRAM command scheduler FIFO | staged-memory-scheduling_isca12 | 最后阶段 per-bank FIFO，只处理低层 DRAM timing。 | 是 |
| Tesseract | PIM 图处理加速器 | tesseract-pim-architecture-for-graph-processing_isca15 | 基于 3D-stacked memory vault cores 的 programmable graph accelerator。 | 是 |
| Vault | HMC 垂直分区 | tesseract-pim-architecture-for-graph-processing_isca15 | 含 DRAM banks、memory controller 和 Tesseract core 的 HMC slice。 | 是 |
| Remote function call | 远程函数调用 | tesseract-pim-architecture-for-graph-processing_isca15 | 通过 message passing 在数据所在 vault 执行函数。 | 是 |
| Message-triggered prefetching | 消息触发预取 | tesseract-pim-architecture-for-graph-processing_isca15 | 利用消息等待处理的 slack 预取目标数据。 | 是 |
| EIN | Error-correction INference | understanding-and-modeling-in-DRAM-ECC_dsn19 | 从 post-correction errors 推断 ECC scheme 和 pre-correction rates 的方法。 | 是 |
| EINSim | EIN 仿真器 | understanding-and-modeling-in-DRAM-ECC_dsn19 | 开源 C++ simulator，用于模拟 ECC 变换和求 likelihood。 | 是 |
| MAP estimation | 最大后验估计 | understanding-and-modeling-in-DRAM-ECC_dsn19 | 选择给定观测下最可能模型参数的统计方法。 | 是 |
