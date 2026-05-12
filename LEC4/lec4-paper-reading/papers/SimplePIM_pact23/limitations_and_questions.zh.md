# Limitations and Questions

## 1. 作者明确承认的局限
- 当前实现针对 UPMEM，虽然框架思想可迁移，但其他 PIM 架构需要重新实现 backend，见 Page 9-10, Section 6。
- 目前主要支持 map/reduce/zip；prefix sum/filter 可扩展，但 stencil、convolution、tree/irregular access 更困难，见 Page 10。

## 2. 论文中隐含的局限
- PIM-PIM communication 仍通过 host 模拟，硬件缺少直接 PIM core 通信会限制部分应用，见 Page 10。
- hand-optimized 代码若手动采用相同优化，理论上可达到或超过 SimplePIM；SimplePIM 的主要价值是替程序员自动承担这些工作，见 Page 9。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- SimplePIM 如何支持 irregular graph/tree workloads？
- 如果 UPMEM 后续硬件支持直接 DPU-DPU 通信，SimplePIM 的 collective API 如何优化？
- SimplePIM 与 DaPPA 的 pattern/Pipeline 抽象能否合并成统一 PIM 编程层？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
