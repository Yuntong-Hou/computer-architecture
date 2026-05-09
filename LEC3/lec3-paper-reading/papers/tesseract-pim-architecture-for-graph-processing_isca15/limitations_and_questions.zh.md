# Limitations and Questions

## 1. 作者明确承认的局限
- Tesseract 不支持 virtual memory，以避免 in-memory address translation 开销。（Page 4, Section 3.1）
- 512-core scaling 受 off-chip communication 和 graph distribution 影响，需优化 network/data mapping。（Page 10-11, Sections 5.5-5.7）

## 2. 论文中隐含的局限
- 程序需要使用 Tesseract API/编程模型，迁移已有 graph frameworks 有开发成本。（推断，基于 Section 3.4）
- 结果基于 HMC-era 3D-stacked memory 假设，现代 HBM/PIM 产品接口、软件栈和热约束需重新评估。（推断，基于 architecture setup）

## 3. 实验设计可能存在的问题
- 结论依赖论文中的硬件平台、workload、模拟器、芯片样本或工艺节点；迁移到现代 DDR5/HBM/CXL/GPU/PIM 系统时需复核。（推断）

## 4. 方法可能不适用的场景
- 当系统接口、软件栈、workload locality、错误模型、QoS 目标或硬件组织与论文假设明显不同时，方法收益可能变化。（推断）

## 5. 我阅读时应该追问的问题
- 为什么 graph processing 的瓶颈是 memory bandwidth 而不是 core compute？
- 3D-stacked memory/HMC 的 internal bandwidth 如何支持 memory-capacity-proportional performance？
- Tesseract core/vault/message passing 如何组织？
- 非阻塞 remote function call 如何隐藏 remote access latency 并支持 atomic updates？
- list prefetching 和 message-triggered prefetching 如何利用图算法访问模式？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：heterogeneous memory scheduling、PIM graph processing、on-die ECC-aware DRAM characterization、HBM/PIM productization。
