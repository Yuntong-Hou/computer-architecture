# Limitations and Questions

## 1. 作者明确承认的局限
- 若只使用单个 subarray/bank，bit-serial 高延迟操作仍可能使性能低于 CPU/GPU，见 Page 12。
- multiplication/division 等成本高的操作仍是瓶颈，某些 workload 即使用满 DRAM parallelism 也可能低于 CPU，见 Page 14。

## 2. 论文中隐含的局限
- 高 vectorization factor mixes 下 fairness 仍可能比部分 SIMDRAM 多 bank 配置差，需要更好的 QoS/scheduling，见 Page 13。
- 需要修改 DRAM subarray、memory controller、ISA、compiler 和 OS，落地复杂度高。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- MIMDRAM 的 compiler passes 在更复杂控制流或 pointer-heavy 应用上效果如何？
- 是否可以结合 PNM 逻辑单元加速 multiplication/division 和 reduction，从而降低 MIMDRAM 短板？
- 在真实操作系统和多租户环境中，mat/subarray 级资源调度如何保证 QoS？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
