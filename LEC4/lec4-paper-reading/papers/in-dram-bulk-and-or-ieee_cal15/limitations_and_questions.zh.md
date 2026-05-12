# Limitations and Questions

## 1. 作者明确承认的局限
- 最佳情形依赖 A/B/C 与临时行位于同一 subarray；跨 subarray/bank copy 需要 RowClone-PSM 或更慢路径，见 Page 2, Section 3。
- 机制只直接覆盖 AND/OR，NOT、XOR、count 等操作不在本文实现范围内，见 Page 3-4。

## 2. 论文中隐含的局限
- 需要 DRAM 支持 triple-row activation variant、RowClone 支持和 memory controller/ISA/software 改动，见 Page 3, Sections 3.2-3.3。
- FastBit 应用结果是基于测量 OR 操作次数后的估算，不是完整硬件原型实测，见 Page 4, Section 5。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 真实芯片中 triple-row activation 在 process/temperature/voltage variation 下错误率是多少？
- 如果操作数跨 subarray 或跨 bank，性能会下降到什么程度？
- 如何将 AND/OR primitive 扩展成完整 bitwise ISA 并处理 ECC/cache coherence？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
