# Limitations and Questions

## 1. 作者明确承认的局限
- SMS0.9 会降低 GPU frame rate，某些类别如 HM 可能低于 30 FPS，需要调整 p。（Page 8, Figure 5 discussion）
- CPU-only 场景中 SMS 相比 ATLAS/TCM 牺牲少量 performance，换取 fairness 和低复杂度。（Page 11, Section 6.6）

## 2. 论文中隐含的局限
- SMS 评估基于 2012 年 GPU/DDR3 模型，现代 integrated GPU、HBM/LPDDR 和 QoS requirements 需重新验证。（推断，基于 Section 5 setup）
- p 的动态选择需要系统软件或 ISA 支持，论文主要展示可调性而非完整 runtime policy。（推断，基于 Page 9 footnote and Section 6.2）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、workload、模拟器、芯片样本或工艺节点；迁移到现代 DDR5/HBM/CXL/GPU/PIM 系统时需复核。（推断）

## 4. 方法可能不适用的场景
- 当系统接口、软件栈、workload locality、错误模型、QoS 目标或硬件组织与论文假设明显不同时，方法收益可能变化。（推断）

## 5. 我阅读时应该追问的问题
- GPU 高强度 memory traffic 为什么会破坏 CPU application-aware scheduling？
- 能否用分布式小 FIFO 代替大型集中式 CAM/request buffer？
- 如何同时捕获 row-buffer locality、提高公平性、控制 GPU frame rate？
- SJF probability p 如何在 CPU 与 GPU 优先级之间调节？
- SMS 的面积/功耗复杂度相比 FR-FCFS 如何？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：heterogeneous memory scheduling、PIM graph processing、on-die ECC-aware DRAM characterization、HBM/PIM productization。
