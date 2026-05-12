# Limitations and Questions

## 1. 作者明确承认的局限
- TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。
- data mapping 假设 offloaded block 的访问模式具有可重复性；BFS 这类 irregular workload 可能被错误映射拖慢，见 Page 9。

## 2. 论文中隐含的局限
- 编译器分析使用保守静态估计和 PTX 工具链，真实 GPU ISA/驱动中的实现会更复杂，见 Page 3 与 Page 8。
- offloading aggressiveness 仍可改进，尤其是 offloaded block 中 ALU 指令比例较高时，见 Page 11。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- TOM 的 mapping predictor 如何适应 phase behavior 更剧烈的现代 GPU workloads？
- 在 HBM/CXL 等新内存系统中，TOM 的 offload/mapping cost model 是否仍成立？
- 是否能把 TOM 的透明 offloading 思路迁移到 UPMEM 或其他 PIM 系统？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
