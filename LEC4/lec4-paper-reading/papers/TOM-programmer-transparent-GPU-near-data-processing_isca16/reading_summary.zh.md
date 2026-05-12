# 中文阅读摘要

## 1. 一句话总结
TOM 通过编译器选择可 offload 的 memory-intensive code blocks，并用软硬件协同数据映射把 offloaded code 与数据共置，从而无需程序员修改 GPU 程序即可利用 3D-stacked memory logic layer。

## 2. 研究背景
- GPU 应用常受 off-chip memory bandwidth 限制；3D-stacked memory 的 logic layer 可以放置 SMs 并靠 TSV 获得高内部带宽，见 Page 1, Section 1。
- NDP 系统面临两个核心问题：哪些代码应在 main GPU 还是 memory stack SMs 执行，以及数据如何映射到多个 memory stacks，见 Page 1。

## 3. 核心问题
- 如何不让程序员手动标注 offloading code。
- 如何在多个 memory stacks 中放置数据，使 offloaded code 和访问数据尽量共置，同时不损害 main GPU 的带宽利用。
- 如何根据运行时资源状况控制 offloading aggressiveness，避免 memory stack SMs 成为瓶颈。

## 4. 核心贡献
- 提出 compiler-based offload candidate selection，用 memory bandwidth cost-benefit 分析选择 code blocks，见 Page 2-4, Section 3.1。
- 提出 programmer-transparent data mapping，利用 offloaded blocks 的可重复内存访问模式预测页面映射，见 Page 2 与 Page 4-6, Section 3.2。
- 提出 runtime offloading control，根据 SM 与 bandwidth utilization 动态决定候选 block 是否实际 offload，见 Page 2 与 Page 6。
- 在 10 个 memory-intensive GPGPU workloads 上评估 TOM，见 Page 8-12。
- 展示平均 30%、最高 76% 性能提升，并降低 off-chip traffic 和 energy，见 Page 2 与 Page 9-10。

## 5. 方法概述
- 编译器估计 offload 一个 block 后 TX/RX bandwidth 的变化；如果节省的 memory traffic 超过 live-in/live-out register transfer 成本，则标记为 candidate，见 Page 3, Equations 1-4。
- data mapping 机制在 learning phase 评估简单 address mapping options，预测 offloaded block 将访问的 pages，并将这些 pages 放到最接近 offloaded code 的 stack，见 Page 4-6。
- offloading control 防止过度 offload：当 memory stack SMs 的 pending requests 或资源压力过大时，候选 block 可继续在 main GPU 执行，见 Page 6 与 Page 9。
- 实现上增加 offloading metadata table、memory allocation table 和 memory map analyzer 等结构，见 Page 6-7。

## 6. 实验设计
- 使用 Rodinia、GPGPU-Sim workloads 和 CUDA SDK 中 10 个 memory-intensive GPU applications，见 Page 8-9, Table 2。
- 指标包括 IPC speedup、off-chip memory traffic、energy consumption、warp capacity sensitivity、internal/cross-stack bandwidth sensitivity 和 area，见 Page 9-12。
- baseline 是不能 offload 到 3D-stacked memories 的 GPU 系统；比较不同 NDP offloading/mapping policies，见 Page 9。

## 7. 主要结果
- TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。
- programmer-transparent data mapping 相比 baseline memory mapping 平均额外提升 10%；例如 KM 从 3% 提升到 39%，RD 从 51% 提升到 76%，见 Page 9。
- 没有 offloading control 时，系统平均变慢 3%/7%；controlled offloading 将 offloaded instructions 从 46.4% 降到 15.7%，避免 memory stack SMs 成瓶颈，见 Page 9-10。
- TOM 平均降低 off-chip memory traffic 38%、最高 99%，平均降低 energy 11%、最高 37%，见 Page 2 与 Page 10。
- 把 memory stack SM warp capacity 提高到 4x 可在保持约 29% speedup 的同时额外节省 20% memory traffic，见 Page 11, Figures 11-12。
- 即使 internal bandwidth 等于 external link bandwidth，TOM 平均仍有 28% speedup，见 Page 11, Figure 13。

## 8. 关键结论
这篇论文的核心结论是：TOM 通过编译器选择可 offload 的 memory-intensive code blocks，并用软硬件协同数据映射把 offloaded code 与数据共置，从而无需程序员修改 GPU 程序即可利用 3D-stacked memory logic layer。 论文的主要实验证据集中在 TOM 在启用 NDP-Controlled 和 tmap 后，平均性能提升 30%，最高 76%，且所有 workload 均有 speedup，见 Page 9, Figure 8。 这些结果表明，作者提出的方法在目标场景中确实缓解了数据搬移或系统集成瓶颈，但收益依赖具体数据布局、工作负载形态和系统支持。

## 9. 局限性
- TOM 主要面向 memory-intensive GPU workloads；compute-intensive code 通常不会被选为 offload candidate，见 Page 8。
- data mapping 假设 offloaded block 的访问模式具有可重复性；BFS 这类 irregular workload 可能被错误映射拖慢，见 Page 9。
- 编译器分析使用保守静态估计和 PTX 工具链，真实 GPU ISA/驱动中的实现会更复杂，见 Page 3 与 Page 8。
- offloading aggressiveness 仍可改进，尤其是 offloaded block 中 ALU 指令比例较高时，见 Page 11。

## 10. 适合我重点关注的内容
- Page 1 的两个 Challenge 是 TOM 的设计入口。
- Page 3 Equations 1-4 是 offload candidate cost model 的关键。
- Page 4-6 的 mapping learning/prediction 解释 TOM 如何做到 programmer-transparent。
- Page 9-12 Figures 8-13 是性能、traffic、energy 和敏感性核心证据。

## 11. 和其他文献的关系
TOM 属于 processing-near-memory/3D-stacked memory logic layer 路线，与 Ambit/PuD 不同：它在 memory stack logic layer 放计算单元，而不是用 DRAM cell/sense amplifier 本身计算。
