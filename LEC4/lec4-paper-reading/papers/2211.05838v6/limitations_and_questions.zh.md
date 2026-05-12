# Limitations and Questions

## 1. 作者明确承认的局限
- DDR5 支持、RFM 命令研究和更多 FPGA board 原型仍是未来工作，见 Page 13, Section 7。
- 功耗测量 setup 仍在进行中，尚未完整发布，见 Page 13, Section 7。

## 2. 论文中隐含的局限
- packetized interfaces 的 3D-stacked DRAM 可能无法完全暴露低层 DRAM interface，限制 DRAM Bender 的适用性，见 Page 13-14。
- GUI 只是未来方向，目前仍偏向程序化实验，见 Page 14。
- in-DRAM AND/OR 在 DDR4 上存在 BER，不能直接当作可靠计算机制，见 Page 12。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- DDR5 RFM 是否能真正缓解 RowHammer，DRAM Bender 扩展后能否系统验证？
- DDR4 in-DRAM AND/OR 的 BER 是否能通过数据布局、温度、电压或选择 segment 降到可用范围？
- DRAM Bender 与 PiDRAM 是否可以组合，既做底层 characterization 又做端到端应用评估？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
