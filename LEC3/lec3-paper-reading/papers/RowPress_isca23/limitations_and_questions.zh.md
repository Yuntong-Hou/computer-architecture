# Limitations and Questions

## 1. 作者明确承认的局限
- 只限制 maximum row-open time 本身不足，且可能带来高达 34.1% 性能退化。（Page 15, Section 7）
- RowPress 需要纳入 RowHammer mitigation 参数配置，否则只看 hammer count 的防御可能失效。（Page 15-16, Section 7.4）

## 2. 论文中隐含的局限
- 本文聚焦 DDR4；DDR5/HBM/LPDDR 的 RowPress 行为需要结合后续实验继续确认。（推断，基于 tested chips scope）
- 真实攻击 exploit 的完整权限提升链不在本文主线，系统风险还需与 OS/allocator/防御配置结合分析。（推断，基于 user-level bitflip demo）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
- RowPress 与 RowHammer 在物理触发条件、bitflip cell 集合、温度和访问模式敏感性上有何不同？
- 增加 aggressor row on time (tAggON) 会怎样降低 ACmin？
- 真实系统和 in-DRAM RowHammer 防御存在时，用户态程序是否仍能触发 RowPress？
- 现有 RowHammer mitigation 如何适配 RowPress？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
