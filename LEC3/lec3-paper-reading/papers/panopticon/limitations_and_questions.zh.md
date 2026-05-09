# Limitations and Questions

## 1. 作者明确承认的局限
- 若没有 ALERTn 或类似方式请求额外时间，攻击者可通过填满 service queue 破坏安全性。（Page 5-6, Figures 6-7）
- counter mats 的实际 power/space overhead 需要 DRAM vendor 精确评估。（Page 6, Section VII-C）

## 2. 论文中隐含的局限
- Panopticon 需要 DRAM 内部设计改动，仍依赖厂商采用和验证，且对 DDR5/HBM 需重新适配。（推断，基于 in-DRAM architecture）
- 论文偏设计和安全分析，缺少基于完整 workload 的性能/能耗评估。（推断，基于 evaluation scope）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何避免 Graphene/TWiCe/BlockHammer 等方案的大量 fast-memory 状态？
- DRAM 内部如何为每行维护 counter 而不拖慢普通访问？
- 不修改 DDR4 controller/protocol 时，DRAM 如何请求时间刷新 victim rows？
- service queue 是否可能被攻击者填满或连续触发？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
