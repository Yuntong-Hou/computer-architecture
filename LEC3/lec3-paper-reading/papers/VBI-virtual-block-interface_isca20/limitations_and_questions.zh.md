# Limitations and Questions

## 1. 作者明确承认的局限
- VBI 是新虚拟内存框架，需要 ISA/OS/hardware/memory-controller 协同修改。（Page 3-7, design sections）
- MTL 变成关键硬件组件，需要正确处理 capacity management、sharing、copy-on-write、swap 等功能。（Page 4-7, Section 3-4）

## 2. 论文中隐含的局限
- 真实系统采用 VBI 的兼容性成本很高，尤其对现有 OS、hypervisor 和应用 ABI。（推断，基于 framework replacement）
- 安全性依赖 VB permission/CVT/VIT/MTL 实现正确性，攻击面转移到新硬件软件边界。（推断，基于 protection design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
- 能否让应用用可变大小 virtual blocks 表达语义单位？
- 能否把 physical allocation 和 address translation 交给 memory controller 侧硬件？
- VBI 如何降低 native/VM address translation overhead？
- VBI 如何更好管理 PCM-DRAM/TL-DRAM 等异构内存？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
