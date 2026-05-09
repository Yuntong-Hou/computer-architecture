# Limitations and Questions

## 1. 作者明确承认的局限
- AVATAR 依赖 ECC DIMM 和 scrubbing；没有 ECC 的系统无法按该方式安全捕获 VRT failures。（Page 6-7, Section V）
- fast refresh table 会随时间增长，长期 refresh savings 低于刚测试后的 profile。（Page 9, Figure 15）

## 2. 论文中隐含的局限
- VRT 统计模型来自有限芯片样本，未来工艺/温度/工作负载下 AVI rate 可能变化。（推断，基于 24 chips sample）
- scrubbing 周期、ECC 强度与系统空闲带宽会影响实际部署效果。（推断，基于 scrubbing design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- VRT 为什么会让传统 multirate refresh 不安全？
- Active-VRT Pool 与 Active-VRT Injection 如何刻画 VRT 行为？
- AVATAR 如何用 ECC/scrubbing 捕获新出现的 VRT failures？
- AVATAR 在可靠性、refresh savings、性能和 EDP 上收益多少？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
