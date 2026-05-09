# Limitations and Questions

## 1. 作者明确承认的局限
- ASM 依赖 auxiliary tag store、高优先级 sampling phase 和硬件计数器，增加实现复杂度。（Page 4-6, Section 4-5）
- ASM 给的是 slowdown estimate 而非严格实时保证，QoS 用例也定位为 soft guarantee。（Page 11-12, Section 6.2.3）

## 2. 论文中隐含的局限
- CAR 与性能的相关性对极端 compute-bound、prefetch-heavy 或 non-cache-sensitive 应用可能减弱。（推断，基于 Figure 1 assumption）
- sampling phase 会扰动正常调度，在非常短 phase 或强实时系统中需重新评估。（推断，基于 online sampling）

## 3. 实验设计可能存在的问题
- 结论依赖论文的硬件模型、benchmark、芯片样本或系统假设；迁移到新环境需复核。（推断）

## 4. 方法可能不适用的场景
- 当硬件接口、系统假设、workload 特征或可靠性模型与论文不同，方法收益或保护能力可能明显变化。（推断）

## 5. 我阅读时应该追问的问题
- 如何在线估计应用在共享 cache 与主存干扰下的 slowdown？
- 为什么 cache access rate 能代表应用性能变化？
- 如何分别估计 cache interference 和 memory bandwidth interference？
- ASM 的估计能否直接驱动资源分配/QoS 策略？

## 6. 后续可以继续阅读的方向
- 与本批相关方向：DDR5 RowHammer 防御、共享资源 slowdown/QoS、VRT-aware refresh、异构 SoC memory scheduling、RowHammer 后续安全研究。
