# Limitations and Questions

## 1. 作者明确承认的局限
- PARBOR 依赖 DRAM internal organization 的 regularity；remapped columns/cells 会降低覆盖率。（Page 10, Section 7.3 Limitation）
- sample size 太小会让 random failures 干扰 distance ranking。（Page 10, Figure 15）

## 2. 论文中隐含的局限
- 不同工艺世代、更强 redundancy/remapping 或 3D/HBM 组织可能改变 PARBOR 假设。（推断，基于 address mapping regularity）
- DC-REF 需要运行时监控 row data content 与 worst-case pattern，实际硬件开销需进一步实现验证。（推断，基于 DC-REF design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何在不知道 vendor 内部映射的情况下找到物理邻居 cell 的 system address？
- strongly coupled cells 如何将 O(n^2) 测试降到 O(n)？
- 递归并行测试如何进一步减少测试数量？
- neighbor-aware patterns 相比 random patterns 多发现多少 failures？
- PARBOR 如何支持 DC-REF 降低 refresh？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
