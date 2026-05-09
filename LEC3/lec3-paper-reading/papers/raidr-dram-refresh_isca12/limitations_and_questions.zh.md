# Limitations and Questions

## 1. 作者明确承认的局限
- RAIDR 依赖准确 retention time profiling；data pattern 和温度对 retention 的影响留待进一步分析。（Page 4, Section 3.2 footnote and Page 5, Section 3.5）
- RAS-only refresh 会带来额外 bus power，尽管评估显示节能收益超过开销。（Page 5, Section 3.4）

## 2. 论文中隐含的局限
- VRT 会使静态 retention profile 过期，需结合 AVATAR/Reaper 等运行时机制。（推断，结合后续文献）
- Bloom filter false positives 不影响正确性但会降低 refresh reduction，配置需随容量扩展。（推断，基于 Figure 9/Table 3）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何利用 retention time variation 减少 refresh 而不修改 DRAM 芯片？
- Bloom filters 为什么适合存储 retention bins？
- RAIDR 在性能、能耗、idle power 和 future density scaling 上收益如何？
- false positives、温度和 retention distribution 变化如何影响正确性？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
