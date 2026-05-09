# Limitations and Questions

## 1. 作者明确承认的局限
- 提高 refresh rate 是直接短期方案，但会带来显著性能/能耗问题。（Page 7, Section III-B）
- PARA 虽低开销，但需要 memory controller 或 DRAM chip/interface 支持。（Page 4 and Page 8, PARA discussion）

## 2. 论文中隐含的局限
- 作为 retrospective，它整合已有结果，不提供统一实验复现。（推断，基于文章类型）
- 2019 之后 TRR bypass、RowPress、VRD 等新现象需要继续读更新文献。（推断，基于发表时间）

## 3. 实验设计可能存在的问题
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
- RowHammer 的物理机制和可重复 bit flip 特性是什么？
- 为什么用户态 hammering 能破坏 memory isolation 并触发权限提升？
- 原始 ISCA 2014 论文和后续工作提出了哪些 mitigation？
- 为什么作者主张 principled system-memory co-design 而不只是补丁式防御？

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。
