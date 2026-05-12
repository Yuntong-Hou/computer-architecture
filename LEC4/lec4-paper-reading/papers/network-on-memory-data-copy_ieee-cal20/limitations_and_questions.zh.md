# Limitations and Questions

## 1. 作者明确承认的局限
- NoM 主要针对 highly-banked 3D-stacked memory；传统低 bank 数 DDR 系统的收益和实现形态不一定相同，见 Page 1-2。
- 设计需要在 DRAM bank 周围加入 routers/links/slot tables/CCU，对现有 HMC/HBM 仍是硬件修改，见 Page 2-3。

## 2. 论文中隐含的局限
- 实验 workload 较集中于 copy-intensive/mcached-style traffic；processor-intensive benchmarks 不是目标场景，见 Page 4。
- NoM 相比 RowClone 可能最多增加 9% energy，且需要软件/ISA 发出 direct data copy request 并维护 consistency，见 Page 3-4。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- NoM 在真实 HBM3/HBM4 的 bank group、pseudo-channel 和 TSV 组织上如何映射？
- direct data copy request 的 ISA/OS 接口和 memory consistency 需要什么支持？
- 当 workload 不以 copy 为主，而是混合 gather/scatter 或 reduction 时，NoM 是否能泛化为更通用 in-memory network？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
