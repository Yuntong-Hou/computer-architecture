# Limitations and Questions

## 1. 作者明确承认的局限
- PCM 技术仍处于 speculative/early prototype 状态，参数来自多篇 prototype survey。（Page 2, Section 2）
- 5.6 years lifetime 仍依赖 effective wear-leveling；更细粒度 partial bit writes 需额外 shadow buffers/comparators。（Page 9, Section 5.2）

## 2. 论文中隐含的局限
- 论文未完整解决 PCM non-volatility 带来的 persistence consistency/security 问题。（推断，基于 conclusion）
- 现代 NVM 技术与内存控制器已经演化，早期参数需谨慎迁移。（推断，基于 2009-era technology）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何把 PCM prototype 参数映射到 DDR-style timing/energy model？
- buffer width/row count 如何影响 delay、energy、write coalescing？
- partial writes 如何提升 endurance？
- PCM scaling 是否在 40nm 后比 DRAM 更有能耗优势？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
