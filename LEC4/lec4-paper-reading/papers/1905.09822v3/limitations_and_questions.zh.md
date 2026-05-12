# Limitations and Questions

## 1. 作者明确承认的局限
- 许多操作要求源/目标行位于同一 subarray，数据布局与地址映射压力较大，见 Page 18-21, Sections 4.1-4.2。
- bitcount 等操作仍由 CPU 完成，限制了部分应用的端到端加速，见 Page 28-30, Sections 8.1-8.2。

## 2. 论文中隐含的局限
- 作者指出 ECC 成本和 process variation 下的错误处理是重要问题；近似 Ambit 仍是未来方向，见 Page 24, Section 5.5 与 Page 33, Section 9.4。
- Section 8.4 中 BitFunnel、encryption、DNA、ML 等只是讨论，没有完整定量评估，见 Page 31-32。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 真实 DDR4/DDR5 芯片中 Ambit 操作的 bit error rate 与数据位置、温度、电压如何变化？
- 如果 bitcount/shift/count 等操作不能在 DRAM 内完成，应用端到端加速会在什么场景下被吞掉？
- 操作系统和内存分配器如何稳定地把操作数放到同一 subarray，且不破坏普通程序性能？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
