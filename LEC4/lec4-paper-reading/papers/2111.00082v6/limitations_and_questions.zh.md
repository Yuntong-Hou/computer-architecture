# Limitations and Questions

## 1. 作者明确承认的局限
- prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。
- coherence 通过低效 CLFLUSH 实现，dirty cache block 比例升高时收益明显下降，见 Page 12, Figure 11。

## 2. 论文中隐含的局限
- D-RaNGe 控制器未优化，作者说明 TRNG latency 可进一步降低，见 Page 14 footnote。
- 温度、电压控制以及更多安全 primitive 的端到端研究留给未来工作，见 Page 15。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 如果 coherence 机制由硬件而不是 CLFLUSH 支持，RowClone 端到端收益会提升多少？
- PiDRAM 扩展到 DDR4/DDR5 后，时序违例和内部地址映射问题会发生什么变化？
- 真实 OS 中如何把 PuM allocation 和普通 page allocator 更自然地融合？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
