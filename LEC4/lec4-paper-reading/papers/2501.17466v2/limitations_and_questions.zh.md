# Limitations and Questions

## 1. 作者明确承认的局限
- 真实应用需要手工修改以标记 PUD-friendly loops 和 fixed-point data arrays，工具链并非完全自动，见 Page 12。
- baseline PUD substrate 不支持 floating-point，浮点评估使用 synthetic analysis 而非完整真实应用，见 Page 13-14。

## 2. 论文中隐含的局限
- Proteus 依赖 Ambit、LISA、SALP 等底层机制，真实硬件实现需要这些机制可靠可用，见 Page 14-15。
- 动态 bit-precision 需要对象追踪、转置缓冲和元数据维护；短任务上的 runtime/metadata 开销仍需进一步验证。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- Proteus 与 MIMDRAM 是否可以结合，同时解决位精度和资源粒度问题？
- 如果应用包含大量 floating-point 或不规则数据结构，Proteus 的收益还剩多少？
- 动态 bit-precision metadata 在多线程、多进程和虚拟内存环境中如何维护一致性？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
