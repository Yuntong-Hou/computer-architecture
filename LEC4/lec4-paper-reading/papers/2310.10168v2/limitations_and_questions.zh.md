# Limitations and Questions

## 1. 作者明确承认的局限
- 评估只覆盖六个 PrIM workload，尚不能代表所有 PIM 应用，见 Page 10-12。
- DaPPA 强绑定 UPMEM 架构和 SDK，迁移到其他 PIM 架构需要重新设计 backend，见 Page 12, Related Work。

## 2. 论文中隐含的局限
- CPU-DPU/DPU-CPU transfer time 仍占主要执行时间，框架不能消除 UPMEM 硬件通信瓶颈，见 Page 11, Figure 5。
- runtime compilation 虽然相对端到端时间较小，但对短任务或频繁构建 Pipeline 的场景可能不可忽略，见 Page 12。
- UPMEM 缺乏 direct inter-DPU communication，DaPPA 需要通过 host/main memory 间接组织数据，见 Page 3。

## 3. 实验设计可能存在的问题
- 需要检查 baseline 是否覆盖端到端成本、真实系统开销和 workload 多样性。对应位置：Evaluation / Results。
- 需要注意模拟器、FPGA prototype 或特定商业平台的参数是否能代表更广泛系统。对应位置：Methodology / Experimental Setup。

## 4. 方法可能不适用的场景
- 当 workload 不满足论文假设，例如空间局部性、数据布局、并行模式或硬件接口条件不匹配时，收益可能下降。
- 当系统无法修改 memory controller、allocator、runtime 或 cache/coherence 支持时，方法可能只能停留在实验平台中。

## 5. 我阅读时应该追问的问题
- DaPPA 是否能支持需要复杂 inter-DPU communication 的 graph/irregular workload？
- 对于小输入或短任务，runtime compilation 开销是否会超过收益？
- 能否把 DaPPA 的 data-parallel pattern 抽象迁移到非 UPMEM 的 PIM/near-memory 平台？

## 6. 后续可以继续阅读的方向
- 与本文同主题的前序 primitive/platform/framework 论文。
- 真实硬件复现实验、开源代码和 artifact evaluation。
- 面向 DDR5/HBM/CXL 或 UPMEM 后续版本的系统集成论文。
