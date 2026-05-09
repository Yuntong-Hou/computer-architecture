# Limitations and Questions

## 1. 作者明确承认的局限
- PCM 仍有 long latencies、high write energy、finite endurance，必须依靠架构缓解。（Page 1-3）
- multilevel PCM 区分多 resistance levels 有较高延迟/复杂度，可能限制每 cell bits。（Page 3）

## 2. 论文中隐含的局限
- 文章基于早期 PCM prototypes 和模型，商业技术参数可能随年代变化。（推断，基于 technology survey）
- 非易失主存的软件/一致性/安全模型只做展望，未完整解决。（推断，基于 conclusion）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本、工艺假设或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征、DRAM/NVM 工艺参数或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- PCM cell 如何通过 SET/RESET 相变存储信息？
- 为什么 PCM 可缩放性好但访问延迟、能耗和 endurance 差？
- row buffer design 如何缩小 PCM 与 DRAM 的性能/能耗差距？
- redundant bit-write removal、row shifting、segment swapping 如何提升寿命？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowHammer in-DRAM mitigation、DRAM data-dependent testing、phase-change memory/hybrid memory、retention-aware refresh、VRT-aware profiling。
