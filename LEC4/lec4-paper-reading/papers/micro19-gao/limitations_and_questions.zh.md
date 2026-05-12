# Limitations and Questions

## 1. 作者明确承认的局限
- 不是所有 vendor/configuration 都支持完整 AND/OR；作者推测某些芯片会检查并丢弃过紧 command timing，但内部设计不可见，见 Page 10。
- 可靠使用需要 error table 排除坏 columns/rows，这会降低可用容量并增加软件/地址转换复杂度，见 Page 6-7 与 Page 10。

## 2. 论文中隐含的局限
- 操作对 voltage/temperature 敏感，实际产品可能需要 binning，以标定哪些模块在什么环境下可靠，见 Page 11, Section 6.3。
- ComputeDRAM 适合 massive vector/bit-serial workloads；单个标量 ADD 需要上千 cycles，不适合低并行度计算，见 Page 12, Section 7.1。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- DDR4/DDR5 是否仍保留类似可利用的 timing-violation 行为，还是控制逻辑会过滤这些命令？
- error table、binning 与温度/电压监控的系统成本是否会抵消无需改 DRAM 的优势？
- 如何把 ComputeDRAM 的不稳定 primitive 包装成可由 OS/编译器安全使用的接口？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
