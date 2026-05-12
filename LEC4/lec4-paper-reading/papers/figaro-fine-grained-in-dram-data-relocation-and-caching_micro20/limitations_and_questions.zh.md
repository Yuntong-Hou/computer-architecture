# Limitations and Questions

## 1. 作者明确承认的局限
- 需要修改 DRAM peripheral logic 和 memory controller/FTS，虽然不改 cell array，但仍需 DRAM 厂商支持，见 Page 11。
- FIGCache 效果依赖 temporal locality、row segment size、replacement policy 和 hot data identification，见 Page 11-12 Sensitivity Studies。

## 2. 论文中隐含的局限
- row segment 太大退化为整行缓存，relocation latency 和 cache underutilization 上升，见 Page 11, Section 9.2。
- RowHammer/side-channel mitigation 只是其他用例讨论，不是主要实验验证对象，见 Page 8。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- FIGARO 的 RELOC 操作在真实 DDR4/DDR5 芯片上能否以论文时序安全实现？
- FIGCache 与 Sectored DRAM 的 fine-grained access 思路能否结合？
- FIGCache 在现代多租户安全攻击和 RowHammer mitigation 中的实际收益需要怎样验证？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
