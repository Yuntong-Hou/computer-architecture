# Limitations and Questions

## 1. 作者明确承认的局限
- 本文聚焦 COSMO 的 vadvc/hdiff 两个代表 kernel，不等于完整天气模型端到端加速。（Page 1-2 and Section 2）
- FPGA 需要足够并行性与细致映射来弥补较低频率。（Page 2, Introduction）

## 2. 论文中隐含的局限
- CAPI2/POWER9/HBM FPGA 平台特定，迁移到 CXL/CCIX 或不同 FPGA 需重新调优。（推断，基于 platform setup）
- compound stencil 的边界处理、全模型通信和多节点扩展未成为本文重点。（推断，基于 kernel scope）

## 3. 实验设计可能存在的问题
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
- FPGA+HBM 能否缓解天气 prediction stencil 的 memory bandwidth bottleneck？
- 如何在 CAPI2/SNAP 框架下把 host、FPGA、HBM 和 on-chip memory hierarchy 协同起来？
- HBM ports、PE 数量、tile/window size 和 URAM/BRAM/HBM 分层如何影响性能？
- 相对 POWER9 与 DDR4-FPGA，HBM-FPGA 的性能/能耗收益多大？

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。
