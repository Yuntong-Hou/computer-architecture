# Limitations and Questions

## 1. 作者明确承认的局限
- SISA 需要算法以 set-centric 形式重写或包装，软件生态有迁移成本。（Page 4-8, design sections）
- 性能依赖 set representation、degree distribution、threshold 和负载均衡。（Page 12-14, sensitivity analysis）

## 2. 论文中隐含的局限
- PUM/PNM 硬件假设较强，真实商业内存系统中部署需要 ISA、runtime 和 memory substrate 支持。（推断，基于 PIM design）
- 对动态图、在线更新图或小图 workload 的收益可能弱于大规模静态图挖掘。（推断，基于 benchmark scope）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当软件无法表达所需语义、硬件接口不可用，或 workload 行为与评估集差异很大时，收益可能明显下降。（推断）

## 5. 我阅读时应该追问的问题
- 能否用 set-centric programming model 表达多种复杂 graph mining 算法？
- 哪些 set operations 应成为 ISA primitives？
- 高阶/低阶 vertex set 该用 bitvector 还是 sparse array？
- PUM 与 PNM 分别适合加速哪些 set representation？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：RowPress 后续防御、PIM graph mining、稀疏计算 ISA、virtual memory redesign、metadata substrate。
