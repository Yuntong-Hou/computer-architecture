# Limitations and Questions

## 1. 作者明确承认的局限
- retention-time 方法只在平均 55% cells 上清晰证明 fractional behavior，且只能从高电压向低电压泄漏方向观察，见 Page 6。
- fractional value 的普通 readout 是 destructive，作者指出 Half-m/ternary storage 的 readout 与 data recovery 仍不成熟，见 Page 12, Section VI-C。

## 2. 论文中隐含的局限
- 不同 DRAM groups 偏好的 F-MAJ 配置不同，黑盒商用 DRAM 让原因难以确定，见 Page 9。
- 实验平台主要覆盖 DDR3；DDR4 只在相关工作/潜力中讨论，完整支持仍需更多验证，见 Page 12-13。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- fractional value 如果需要长期保存或可恢复读取，需要怎样的 sense amplifier 或 refresh 支持？
- FracDRAM 在 DDR4/DDR5/HBM 上的可行性与稳定性如何？
- 把 fractional states 用于 ternary computation 或密度提升时，错误模型和 ECC 如何设计？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
