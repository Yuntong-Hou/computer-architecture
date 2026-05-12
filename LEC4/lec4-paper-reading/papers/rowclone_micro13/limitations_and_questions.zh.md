# Limitations and Questions

## 1. 作者明确承认的局限
- FPM 要求 source/destination 在同一 subarray、操作整行对齐，不能部分复制，见 Page 4, Section 3.1。
- PSM 更通用但受 shared internal bus 限制，收益远低于 FPM，见 Page 5 与 Page 9。

## 2. 论文中隐含的局限
- RowClone 初始化可能导致应用随后访问 zeroed pages 时出现低 MLP cache misses，需要 RowClone-ZI 缓解，见 Page 10。
- 需要 ISA、memory controller、DRAM peripheral logic、cache coherence 和 OS allocator 的协同，见 Page 5-7。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 现代 DDR4/DDR5 是否允许 FPM 所需的背靠背 ACTIVATE，或需要 DRAM 标准新增 copy command？
- RowClone-aware allocator 在真实 OS 中会如何影响 fragmentation、NUMA 和安全隔离？
- RowClone 与 ECC/encryption/compression memory systems 结合时如何保证正确性？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
