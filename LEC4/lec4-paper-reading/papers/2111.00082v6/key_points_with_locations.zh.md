# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 如何在真实系统中发出 PuM 所需的 DRAM command sequence 与 violated timing parameters。 | Page 1-2 / Introduction | 作者指出很多 PuM 技术已经能在 off-the-shelf DRAM 中通过非标准时序或模拟行为实现，但传统系统、测试平台和模拟器都难以同时支持真实芯片、可改时序、系统软件和完整应用执行，见 Page 1-2, Section 1。 | 高 | 先把问题理解为数据搬移、能耗或可编程性瓶颈，而不是单个算法优化。 |
| 2 | 目标工作负载或平台中存在可被利用的 DRAM/PIM 内部并行性或数据并行性。 | Page 1-2 / Introduction | RowClone 这类 in-DRAM copy 需要特殊内存分配、地址对齐和 coherence 处理；D-RaNGe 这类 TRNG 还依赖真实芯片的时序失败特性，见 Page 1-2。 | 高 | 这是判断论文适用范围的关键。 |
| 3 | PiDRAM 的硬件由可扩展 memory controller 和 POC 组成；POC 通过 memory-mapped interface 让软件用普通 LOAD/STORE 触发 PuM operation，见 Page 2, Page 4-6。 | 方法章节 / Page 2 及后续对应 section | PiDRAM 的硬件由可扩展 memory controller 和 POC 组成；POC 通过 memory-mapped interface 让软件用普通 LOAD/STORE 触发 PuM operation，见 Page 2, Page 4-6。 | 高 | 论文最值得回到原文精读的部分。 |
| 4 | D-RaNGe case study 通过 reduced tRCD 访问产生 activation-latency failures，再从硬件 random number buffer 读取随机数，见 Page 13-14。 | 方法章节后半部分 | D-RaNGe case study 通过 reduced tRCD 访问产生 activation-latency failures，再从硬件 random number buffer 读取随机数，见 Page 13-14。 | 高 | 很多 PIM/PuM 方案难点不在 primitive，而在系统栈接入。 |
| 5 | Bare-Metal RowClone-Copy 相对 CPU-copy 提升 317.5x-364.8x，RowClone-Initialize 提升 172.4x-182.4x，见 Page 12, Figure 9。 | Evaluation / Results | Bare-Metal RowClone-Copy 相对 CPU-copy 提升 317.5x-364.8x，RowClone-Initialize 提升 172.4x-182.4x，见 Page 12, Figure 9。 | 高 | 这是作者主张有效性的第一证据。 |
| 6 | No Flush 配置中，rcc 在 8 KiB/8 MiB 上分别提升 58.3x/118.5x，rci 分别提升 31.4x/88.7x，见 Page 12, Figure 10。 | Evaluation / Results | No Flush 配置中，rcc 在 8 KiB/8 MiB 上分别提升 58.3x/118.5x，rci 分别提升 31.4x/88.7x，见 Page 12, Figure 10。 | 中 | 用于判断收益是否只体现在单一指标。 |
| 7 | 论文显式与传统 CPU/DRAM、已有平台、已有细粒度 DRAM 或 hand-tuned implementation 对比。 | Evaluation / Related Work | 主要对比见实验图表和 related work comparison。 | 高 | 要看 baseline 是否公平、是否覆盖端到端成本。 |
| 8 | 提出 PiDRAM，这是首个面向 commodity DRAM based PuM 的 flexible end-to-end open-source framework，见 Page 2-3。 | Introduction / Contributions | 提出 PiDRAM，这是首个面向 commodity DRAM based PuM 的 flexible end-to-end open-source framework，见 Page 2-3。 | 高 | 贡献通常对应论文的 novelty claim。 |
| 9 | prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。 | Limitations / Discussion / Future Work | prototype 基于 DDR3 与 FPGA RISC-V，不能直接代表商业 CPU/DDR4/DDR5 系统性能，见 Page 7, Section 4.6 与 Page 15, Section 7。 | 高 | 后续研究或读论文时要警惕的边界。 |
| 10 | 如果 coherence 机制由硬件而不是 CLFLUSH 支持，RowClone 端到端收益会提升多少？ | 由全文内容推断 | 该问题未被论文完全解决。 | 中 | 可作为后续阅读或讨论问题。 |
