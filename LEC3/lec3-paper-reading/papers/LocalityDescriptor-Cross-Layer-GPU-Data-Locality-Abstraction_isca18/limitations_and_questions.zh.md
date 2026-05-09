# Limitations and Questions

## 1. 作者明确承认的局限
- 需要程序员或编译器生成 descriptor，局部性语义不准确会影响优化效果。（Page 4-6, Section 3）
- 多个 descriptor 可能冲突，因此需要 priority 机制。（Page 2 and Section 3）

## 2. 论文中隐含的局限
- 实验以模拟器为主，真实 GPU 产品中开放 CTA scheduler、cache policy 和 placement 接口的可行性需要进一步工程化。（推断，基于 Section 6 methodology）
- 高度动态或输入相关的 irregular locality 可能难以静态描述。（推断，基于 descriptor design assumptions）

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
- 如何让程序员/编译器表达数据结构、线程组和访问模式之间的局部性关系？
- 为什么单独 CTA scheduling 或单独 cache policy 不足以转化为性能收益？
- Locality Descriptor 需要包含哪些字段才能既可移植又足够驱动硬件优化？
- 在 cache locality 与 NUMA locality 两类场景下，它相对硬件-only/first-touch 等基线提升多少？

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。
