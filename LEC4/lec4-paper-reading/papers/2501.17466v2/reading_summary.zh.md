# 中文阅读摘要

## 1. 一句话总结
Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。

## 2. 研究背景
- 现有 PUD 多采用 bulk bit-serial execution model，用固定 two's complement 和固定 bit-precision 处理整行数据，导致大量 inconsequential bits 被无谓计算，见 Page 1-2。
- PUD 还面临 throughput-oriented execution 难隐藏低并行场景下的单操作延迟，以及高精度操作延迟随 bit-width 线性或二次增长的问题，见 Page 1-2。

## 3. 核心问题
- 如何避免对 leading zeros/ones 等无用高位执行 bit-serial PUD 计算。
- 如何在 PUD operation 内并行执行独立 in-DRAM primitives，缓解单操作延迟。
- 如何为不同 bit-precision 自动选择最合适的 data representation 和 arithmetic algorithm。

## 4. 核心贡献
- 提出 Proteus，第一个面向 bulk bitwise PUD 的 data-aware hardware runtime framework，见 Page 1-2。
- 利用 narrow values 动态降低 PUD operation bit-precision，减少 latency 和 energy，见 Page 2。
- 利用 SALP 将一个 data word 的不同 bits 分散到多个 subarrays，跨 bit 并行执行独立 primitives，见 Page 2 与 Page 4-5。
- 引入 redundant binary representation (RBR) 支持高精度运算，减少或限制 carry propagation，见 Page 2。
- 设计 Parallelism-Aware µProgram Library、Dynamic Bit-Precision Engine 和 µProgram Select Unit，见 Page 2 与 Page 5-10。

## 5. 方法概述
- Dynamic Bit-Precision Engine 在 LLC evicted cache lines 转置为 PUD vertical layout 时扫描对象，记录适合的 bit-precision，见 Page 2 与 Page 6-8。
- Parallelism-Aware µProgram Library 保存不同 bit-precision、two's complement/RBR、bit-serial/bit-parallel 算法的 µPrograms 及 cost model LUTs，见 Page 2 与 Page 8-10。
- µProgram Select Unit 在发出 PUD operation 时查询 bit-precision 和 cost LUT，选择最低延迟或最低能耗的 µProgram，见 Page 2 与 Page 8-10。
- Proteus 复用 Ambit、LISA、SALP 等基础 DRAM mechanisms，并通过控制单元和 data transposition unit 支持运行时选择，见 Page 14-15。

## 6. 实验设计
- 使用 12 个真实应用，来自 Phoenix、Polybench、Rodinia、SPEC2017；系统配置见 Page 12, Tables 2-3。
- 比较 CPU、A100 GPU、SIMDRAM-SP、SIMDRAM-DP、Proteus LT/EN with static/dynamic precision，见 Page 12-13。
- 额外分析 data mapping/representation conversion overhead、floating-point synthetic throughput、GPU tensor cores 对比和面积开销，见 Page 13-14。

## 7. 主要结果
- Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。
- SIMDRAM 加上 Dynamic Bit-Precision Engine 后达到 SIMDRAM-SP 的 6.3x performance per mm²；Proteus µProgram adaptation 又相对 SIMDRAM-DP 提升 1.6x，见 Page 12。
- Dynamic Bit-Precision Engine 使 Proteus 相比 static bit-precision 性能提升 46%，energy consumption 降低 58%，见 Page 12-13, Figures 11-12。
- Proteus 平均比 CPU/GPU/SIMDRAM 分别降低 90.3x、21x、8.1x energy consumption，见 Page 1 与 Page 13。
- 在 int8/int4 GEMM-heavy workloads 上，Proteus 相对 A100 tensor cores 提供 20x/43x performance per mm² 和 484x/767x performance per Watt，见 Page 14, Figure 14。
- 面积开销低：DRAM chip 1.6%，CPU die 0.03%，见 Page 1 与 Page 14-15。

## 8. 关键结论
这篇论文的核心结论是：Proteus 是一个 data-aware PUD runtime，它根据数据实际位宽动态选择 bit-precision、data representation 和 arithmetic µProgram，以降低 bit-serial PUD 的高延迟和高能耗。 论文的主要实验证据集中在 Proteus LT-DP 相对 CPU、GPU、SIMDRAM 平均提供 17x、7.3x、10.2x performance per mm²；Proteus EN-DP 分别为 11.2x、4.8x、6.8x，见 Page 12, Figure 11。 这些结果表明，作者提出的方法在目标场景中确实缓解了数据搬移或系统集成瓶颈，但收益依赖具体数据布局、工作负载形态和系统支持。

## 9. 局限性
- 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。
- baseline PUD substrate 不支持 floating-point，浮点评估使用 synthetic analysis 而非完整真实应用，见 Page 13-14。
- Proteus 依赖 Ambit、LISA、SALP 等底层机制，真实硬件实现需要这些机制可靠可用，见 Page 14-15。
- 动态 bit-precision 需要对象追踪、转置缓冲和元数据维护；短任务上的 runtime/metadata 开销仍需进一步验证。

## 10. 适合我重点关注的内容
- Page 1-2 的三大短板是 Proteus 的动机主线。
- Page 4-5 Figure 3 解释 bit-serial addition 中哪些 primitive 能并行。
- Page 8-10 的 µProgram Library 和 Pareto analysis 是方法选择逻辑。
- Page 12-14 Figures 11-14 是核心性能/能耗证据。

## 11. 和其他文献的关系
Proteus 建立在 SIMDRAM、Ambit、LISA、SALP 等工作上，解决的是 PuD arithmetic 的运行时自适应和高精度低延迟问题，可与 MIMDRAM 的资源粒度控制互补。
