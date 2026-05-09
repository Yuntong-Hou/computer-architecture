# Limitations and Questions

## 1. 作者明确承认的局限
- XMem 需要程序员、autotuner 或 compiler 标注 atoms，语义表达错误会影响优化效果。（Page 3-6, Atom design）
- 它影响性能而不影响正确性，但需要 OS/ISA/hardware 支持 AAM/AST/AMU。（Page 5-7, implementation）

## 2. 论文中隐含的局限
- 两个 use cases 不能完全证明所有九类优化都能低成本受益。（推断，基于 Table 1 vs evaluated use cases）
- 与后来的 MetaSys 相比，XMem 更偏 proposal/模拟评估，真实硬件基础设施还需补充。（推断，结合 MetaSys）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
- 能否设计通用跨层接口，把程序语义传递给 cache、prefetcher、memory controller 等组件？
- Atom 应该携带哪些属性、如何 map/unmap/activate？
- XMem 如何在 cache tiling 资源不匹配时减少性能损失？
- XMem 如何帮助 OS-based DRAM page placement？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
