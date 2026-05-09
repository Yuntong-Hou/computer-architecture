# Limitations and Questions

## 1. 作者明确承认的局限
- PIM accelerator 更高效但每个 target 需要专用逻辑，面积和设计复杂度高于 PIM core。（Page 2, Section 1; Page 3, Section 3.3）
- 分析基于模型和估算，实际产品集成还受热、成本、内存接口、软件栈迁移影响。（Page 3, Section 3.1 and Section 3.3）

## 2. 论文中隐含的局限
- 工作负载来自 Google 生态，结论对其他厂商应用或新型移动 SoC 需要重新验证。（推断，基于 Page 1-3 workload scope）
- PIM offload 的编程模型、调度开销和一致性问题不是本文主要展开对象。（推断，基于 Section 3 target-level evaluation）

## 3. 实验设计可能存在的问题
- 实验结论与特定模型、平台、benchmark 或 workload 选择有关；迁移到新硬件/新应用时需要复核。（推断，基于实验设置章节）

## 4. 方法可能不适用的场景
- 当系统假设无法满足、输入行为与评估 workload 差异明显，或硬件/软件接口无法提供所需支持时，该方法收益可能下降。（推断）

## 5. 我阅读时应该追问的问题
- 消费设备常见工作负载中，多少能耗来自主存与计算单元之间的数据移动？
- 哪些函数/primitive 同时占用大量能耗、以数据移动为主、又适合放到 PIM logic 执行？
- 在有限 logic-layer 面积与功耗预算下，PIM core 与 fixed-function PIM accelerator 分别是否划算？
- PIM 与已有专用硬件/压缩技术相比是否仍有额外价值？

## 6. 后续可以继续阅读的方向
- 阅读同一主题下的相邻论文，并重点比较：问题定义是否相同、硬件假设是否一致、评价指标是否可比、是否有真实系统或芯片数据。
