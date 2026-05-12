# Limitations and Questions

## 1. 作者明确承认的局限
- 论文表征的是当前 COTS DRAM 中非标准 PuD 操作的读扰动效应，未来正式支持 PuD 的 DRAM 可能有不同电路与 mitigation，见 Page 12-13。
- 作者只 sketch 部分 countermeasures，详细设计和面积/能耗评估留给未来工作，见 Page 13。

## 2. 论文中隐含的局限
- PRAC-PO 的面积开销没有完整评估；多 counter simultaneous update 可能需要大量 incrementers 和 counter access，见 Page 14。
- device-level physical causes 仍需后续研究，见 Page 2 与 Page 14-15。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- 未来支持 PuD 的 DRAM 标准应如何同时保证计算能力和 read disturbance isolation？
- 是否能设计比 PRAC-PO-WC 开销更低的 PuDHammer-specific mitigation？
- PuDHammer 的物理机制与 RowHammer/RowPress 是否相同，还是存在新的耦合路径？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
