# Limitations and Questions

## 1. 作者明确承认的局限
- 这是一篇 1969 年概念与工程设计论文，没有现代 benchmark、能耗、面积或系统级定量评估。
- 任意 combinational/sequential logic 的 gate utilization efficiency 低于 memory/register/arithmetic 等自然迭代结构，见 Page 2-3。

## 2. 论文中隐含的局限
- fault accommodation 是有限的，不适用于所有 array 类型或 fault 类型，见 Page 2。
- Sorting Array II 灵活性差、速度慢且 clocking 要求更严格，见 Page 8-9。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- CLIM 的规则二维结构思想如何映射到现代 DRAM subarray 或 SRAM compute-in-memory？
- 哪些现代 workload 具有足够自然的迭代/局部结构，适合 CLIM 式设计？
- 早期 CLIM 的 fault accommodation 思路能否启发现代 PIM 的 yield/reliability 处理？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
