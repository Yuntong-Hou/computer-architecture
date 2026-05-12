# Limitations and Questions

## 1. 作者明确承认的局限
- LISA 需要修改 DRAM array/subarray 间连接和控制逻辑，虽面积开销小但仍需 DRAM 厂商采纳，见 Page 8, Section 7。
- LISA-RISC copy latency 随 copy distance/hop count 增长；Table 4 显示 1 到 63 hops 的 latency 从 148.5ns 到 644.5ns，见 Page 11。

## 2. 论文中隐含的局限
- VILLA 的收益依赖 hot-row detection/caching policy，作者承认 hit rate 可由更好策略提升，见 Page 10-11, Section 9.2。
- coherence、cache dirty blocks 和 OS/software 对 copy 的可见性仍需系统支持，见 Page 6, Section 4.3。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- LISA links 在 DDR5/HBM bank/subarray 组织中是否仍能以相似面积和 timing 成本实现？
- LISA-RISC 与 cache coherence/dirty data 结合时，端到端 OS copy 加速会下降多少？
- VILLA 的 hot-row caching policy 如果换成现代 learned/prefetch-aware policy，收益是否显著提高？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
