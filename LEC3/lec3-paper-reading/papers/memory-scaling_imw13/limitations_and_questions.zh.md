# Limitations and Questions

## 1. 作者明确承认的局限
- 本文是 research directions/survey，不提供统一实验平台上的新定量评估。（全文形式，Page 1-5）
- emerging memory 的 endurance、write latency/power、security/privacy 仍是未解决挑战。（Page 3, Section V）

## 2. 论文中隐含的局限
- 许多代表性机制来自研究原型，其产业部署依赖 JEDEC/DRAM vendor/controller/software 协同。（推断，基于 system-DRAM co-design）
- position paper 对每个方向的细节不充分，需要回读 cited works。（推断，基于文章篇幅）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- DRAM 缩放面临哪些系统级挑战？
- system-DRAM co-design 可通过哪些机制改进 refresh、parallelism、latency、data movement？
- PCM/STT-MRAM 等 emerging memory 带来哪些机会和风险？
- 共享内存系统如何提供 predictable performance 和 QoS？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DRAM retention/VRT profiling、数据中心应用容错、PIM pointer chasing、system-DRAM co-design、shared-memory slowdown/QoS。
