# Limitations and Questions

## 1. 作者明确承认的局限
- Ambit 要求操作数映射到同一 subarray，并需要 RowClone 在 designated rows 间搬移，见 Page 5-8。
- bitcount 仍由 CPU 执行，会限制 bitmap/BitWeaving 等端到端加速，见 Page 11-12。

## 2. 论文中隐含的局限
- ECC 需要支持 bitwise-homomorphic 或专门处理，否则 in-DRAM computation 结果难以保护，见 Page 9。
- 真实芯片 process variation、测试和 yield 仍需厂商级验证；SPICE 只是模型证据。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- Ambit 在真实 DDR4/DDR5 芯片上的错误率与 PuDHammer 风险如何权衡？
- 能否把 bitcount、shift、加法等扩展到 DRAM 内，减少 CPU 残留瓶颈？
- 编译器/OS 如何自动完成 subarray-aware data placement？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
