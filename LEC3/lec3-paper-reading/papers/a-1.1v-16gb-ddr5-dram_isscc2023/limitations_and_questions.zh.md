# Limitations and Questions

## 1. 作者明确承认的局限
- 论文篇幅为 ISSCC short paper，算法与电路细节、面积/功耗开销披露有限。（全文形式，Page 1-3）
- 评估主要是芯片级统计和 malicious pattern 测试，不是系统级 workload 性能评估。（Page 1-3, Figures 28.8.1-28.8.7）

## 2. 论文中隐含的局限
- 由于机制依赖 DDR5 RFM/controller 协作，不同系统 controller 策略会影响端到端保护效果。（推断，基于 RFM algorithm）
- 论文没有公开完整 RTL/测试流程，复现实验依赖厂商内部芯片环境。（推断，基于 ISSCC silicon paper）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 1a-nm DDR5 面临的 row hammer 与 retention 挑战是什么？
- RFM、PAT、PRHT 三类机制如何协作追踪 aggressor row？
- multi-step precharge 如何提高 intrinsic row-hammer tolerance？
- core-bias modulation 如何改善高温 retention？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
