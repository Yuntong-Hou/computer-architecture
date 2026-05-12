# Limitations and Questions

## 1. 作者明确承认的局限
- 单个 PEI 被限制在一个 LLC cache block 内，简化系统集成但限制了可表达的 PIM operation 粒度，见 Page 3-4, Section 3.1。
- 软件仍需把目标代码改写为 PEIs；作者认为编译器未来可自动识别，但本文主要假设程序员手动修改，见 Page 4, Section 3.3。

## 2. 论文中隐含的局限
- PEI 与普通 load/store 之间的 atomicity 不是自动保证的，需要 pfence 等同步，见 Page 4, Section 3.2。
- 评估基于模拟 HMC/PCU 模型，真实 HMC/HBM 产品中的接口、timing 和 coherence 支持可能不同。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- single-cache-block restriction 是否会限制现代图分析/数据库中更复杂的 PIM primitives？
- PEI 的 locality monitor 能否迁移到 HBM/CXL memory expander 场景？
- 编译器如何自动识别 PEI 插入点并和 ordinary vectorization/pass ordering 协同？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
