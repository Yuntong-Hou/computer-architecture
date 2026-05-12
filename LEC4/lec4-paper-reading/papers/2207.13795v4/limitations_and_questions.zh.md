# Limitations and Questions

## 1. 作者明确承认的局限
- stride streaming 等频繁 sector miss workload 可能性能下降，见 Page 11, Figure 9。
- 低/中 MPKI workload 可能不受益，作者提出动态关闭 Sectored DRAM，见 Page 14, Section 8.2。

## 2. 论文中隐含的局限
- 需要 processor/cache/memory controller 维护 sector bits、LSQ Lookahead 和 predictor，硬件复杂度不只在 DRAM 端，见 Page 7 与 Page 14。
- ECC、prefetching、更细粒度 sector 和更复杂 predictor 多数留给讨论/未来探索，见 Page 14-15, Sections 8.3-8.5。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 更强 predictor 是否能显著降低 sector miss，又不会引入过高面积和能耗？
- 真实 DDR5/HBM 系统中 sector bits 如何编码和传输最现实？
- 对混合 workload，动态开关策略如何避免频繁切换带来的抖动？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
