# Limitations and Questions

## 1. 作者明确承认的局限
- 转换为 SMASH hierarchical bitmap format 有软件预处理成本。（Page 5, Section 4.1.3）
- compression ratio 选择影响 bitmap size、扫描速度和额外零元素处理之间的权衡。（Page 5 and Figure 14）

## 2. 论文中隐含的局限
- 对动态更新频繁的 sparse matrix，格式转换和 bitmap 维护成本可能降低收益。（推断，基于 conversion process）
- BMU 与 ISA 需要 CPU/编译器/库支持，部署难度高于纯软件格式。（推断，基于 hardware-software co-design）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
- 如何在保持通用性和压缩率的同时减少 indexing 开销？
- hierarchical bitmap 如何表示任意稀疏结构？
- BMU 需要哪些 buffers/registers/ISA primitives 才能扫描 bitmap hierarchy？
- SMASH 对 SpMV/SpMM/PageRank/BC 的收益和硬件面积开销是多少？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
