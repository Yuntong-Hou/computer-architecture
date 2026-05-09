# Limitations and Questions

## 1. 作者明确承认的局限
- metadata locality 差时开销明显上升，最坏 microbenchmark 可达 27%。（Page 2, Characterization summary）
- security/protection 用例可能需要 Force stall 等保守模式，开销高于性能 hint 类用例。（Page 4-6, MetaSys modes/use cases）

## 2. 论文中隐含的局限
- 基于 RISC-V Rocket Chip 的研究原型，迁移到复杂 OoO server CPU 需要额外工程验证。（推断，基于 prototype scope）
- 新增 ISA 与 OS 支持意味着软件生态迁移成本不可忽略。（推断，基于 Section 3 interface design）

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
- 能否建立一个通用元数据系统，支持性能、安全和保护类跨层技术？
- 元数据接口、tagged memory、OS support 和硬件 lookup 会带来多少面积/性能/内存开销？
- 多个优化同时共享元数据系统是否会互相拖慢？
- 元数据访问的 locality、TLB miss 和 cache 行为如何影响系统效率？

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。
