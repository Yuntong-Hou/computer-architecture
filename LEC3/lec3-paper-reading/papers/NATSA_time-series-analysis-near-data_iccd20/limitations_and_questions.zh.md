# Limitations and Questions

## 1. 作者明确承认的局限
- NATSA 专注 matrix profile/SCRIMP 类 exact anytime 算法，通用性低于 general-purpose NDP cores。（Page 2-5, design scope）
- 某些 scheduling 模式可能牺牲 anytime property 来换取优化机会。（Page 5, Section 4 scheduling）

## 2. 论文中隐含的局限
- 专用 accelerator 的收益依赖 HBM 带宽和足够大的 time series；小数据或不同算法可能收益较低。（推断，基于 Figures 7 and 11）
- 实际集成需要考虑 HBM 容量、主机接口、编程栈和数据预处理成本。（推断，基于 system design）

## 3. 实验设计可能存在的问题
- 结论与本文所选平台、benchmark、模型或综述范围相关；迁移到新系统时需要重新验证。（推断）

## 4. 方法可能不适用的场景
- 当 workload 行为、硬件接口、内存技术或系统软件支持与论文假设差异明显时，本文方法或结论可能不直接适用。（推断）

## 5. 我阅读时应该追问的问题
- matrix profile 的 distance matrix/profile/profile index 如何构成主要计算？
- 如何把对角线计算划分到 near-HBM processing units，同时保持 anytime property？
- 专用 NDP accelerator 相比多核 CPU、GPU 和通用 NDP core 有多大收益？
- HBM 带宽、精度和窗口大小如何影响 NATSA？

## 6. 后续可以继续阅读的方向
- 在 LEC3 论文中继续比较 PIM/NDP、RowHammer/reliability、DRAM simulator 三条主线的共同假设和评估方法。
