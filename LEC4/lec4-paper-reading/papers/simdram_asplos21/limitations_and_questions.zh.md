# Limitations and Questions

## 1. 作者明确承认的局限
- 当前框架只支持 integer/fixed-point operations；floating-point operations 因 mantissa alignment 和 per-bitline shift 等问题仍然困难，见 Page 11, Section 5.6。
- 不能低成本支持跨 bitline shuffle/reduction，除非增加 dedicated bit-shift/shuffle circuitry，见 Page 11。

## 2. 论文中隐含的局限
- 需要程序员手动改写或未来编译器插入 bbop instructions；自动 compiler backend 留给未来工作，见 Page 10, Section 5.2。
- 输入数据需在 DRAM 中且需要 cache flush/pinning，coherence 目前依赖程序员负责 flush，见 Page 10-11, Section 5.3。
- SIMDRAM 可能增加 RowHammer vulnerability，防护机制需另行研究，见 Page 11, Section 5.5。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- SIMDRAM 如何高效支持 floating-point、shuffle 和 cross-bitline reduction？
- 程序员手动改写 bbop 的负担多大，实际 compiler backend 能否自动完成？
- SIMDRAM 对 RowHammer、ECC、memory encryption 和 data layout security 的影响如何处理？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
