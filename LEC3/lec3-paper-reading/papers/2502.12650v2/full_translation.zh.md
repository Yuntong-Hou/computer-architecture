# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖 Chronus 的摘要、PRAC 背景、问题分析、wave/feinting attack、Chronus 设计、评估、比较、errata 提示和硬件工程师视角。保留 Chronus、PRAC、RFM、NRH、wave attack、feinting attack、preventive refresh 等英文术语。参考文献保留英文。

## Title

原文标题：Chronus: Understanding and Securing the Cutting-Edge Industry Solutions to DRAM Read Disturbance

中文标题：Chronus：理解并加固前沿工业 DRAM 读扰动解决方案

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

随着 DRAM RowHammer/read disturbance threshold 持续降低，工业界开始采用更明确的标准化方案，如 DDR5 PRAC/RFM。已有分析表明 PRAC 可以在一定 NRH 假设下提供安全保证，但也带来显著性能和能耗开销，并存在可用性攻击风险。Chronus 进一步研究这些工业方案的内部瓶颈，并提出改进设计。

Chronus 的核心观察是：PRAC 的开销和弱点来自三个方面。第一，counter update 位于关键访问路径，增加 tRP/tRC 等 timing。第二，固定数量 preventive refresh 无法适应不同攻击强度和风险状态。第三，refresh 后的固定 delay period 会暴露可被攻击者利用的时间窗口。

Chronus 通过三项设计改善 PRAC：将 activation counters 与 data path 分离，使 counter update 与正常访问并行；动态控制 preventive refresh 数量；移除固定 delay period，降低 wave attack 和 feinting attack 的利用空间。评估显示，在现代 NRH=1K 下 Chronus 平均性能开销低于 0.1%，在未来 NRH=20 下平均性能开销约 8.3%，显著优于 PRAC variants。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

RowHammer 防护正在从厂商私有 TRR 转向更标准化的 controller-DRAM 协同机制。PRAC/RFM 是这一转向的重要代表，但第一代机制并不完美。前序 PRAC 分析已经指出，PRAC 在低 NRH 下开销极高，并可能被用于 availability attack。

Chronus 的目标不是否定 PRAC，而是分析 PRAC 为什么昂贵、为什么存在攻击窗口，并提出更适合未来低阈值 DRAM 的设计。论文名称 Chronus 暗示其核心关注 timing：计数何时更新、刷新何时执行、delay window 如何暴露规律，以及这些时间结构如何影响安全和性能。

引言中最重要的工程问题是：如果未来 NRH 继续降低到几十次甚至更低，简单“计数后固定刷新”的协议会让 DRAM 大部分时间都在防护而不是服务正常请求。行业需要更细致的时间调度和风险自适应机制。

## 2. Background: PRAC and RFM / 背景：PRAC 与 RFM

### 原文位置

Page 2 - Page 3 / Background

### 中文翻译

PRAC 在 DRAM 内部维护 activation counters，用于跟踪 rows 的激活情况。当某些计数接近阈值时，DRAM 通知 controller 进入 back-off 或 refresh management 流程。Controller 发出 RFM commands，DRAM 执行 preventive refresh，以降低 victim rows 的 disturbance。

PRAC 的优势是 DRAM 内部能看到更接近真实物理结构的信息。Controller 不需要完全理解地址重映射和 adjacency。但 PRAC 的代价是 counter update 和 RFM 都会影响命令时序。若每次 activation 后都必须在关键路径上更新计数，普通访问 latency 会增加。若频繁触发 RFM，系统吞吐会下降。

Chronus 在这个背景上提出：问题不在于“DRAM 内部计数”这个方向，而在于 PRAC 的具体时间组织方式。只要重构 counter update 和 refresh scheduling，就可能同时提高安全性和性能。

## 3. Weaknesses of Existing PRAC Variants / 现有 PRAC 变体的弱点

### 原文位置

Page 3 - Page 5 / Table 1, Figures 2-3

### 中文翻译

论文首先分析 PRAC variants 的 timing overhead。由于 counter update 与 row activation/precharge 路径耦合，tRP、tRC 等关键参数增加。对 memory-intensive workloads 来说，这类 timing 增加会直接降低可服务 activation rate，即使没有真实攻击也会带来性能损失。

第二个弱点是固定 preventive refresh 数量。不同风险状态下，实际需要刷新的 victim rows 数量并不相同。如果固定刷新太少，安全性不足；如果固定刷新太多，正常 workload 承担不必要开销。攻击者还可以构造访问节奏，让固定刷新策略效率低下。

第三个弱点是 refresh 后的 delay period。固定 delay window 会给攻击者提供可预测节奏。论文提出 wave attack 和 feinting attack，说明攻击者可以利用防护周期、延迟窗口和刷新数量组织访问，使 PRAC variants 需要更保守配置或仍产生安全/性能问题。

对硬件工程师来说，这些弱点说明安全协议的 timing determinism 本身就是攻击面。越可预测的防护节奏，越容易被 adversarial access pattern 对齐和利用。

## 4. Wave Attack and Feinting Attack / Wave attack 与 Feinting attack

### 原文位置

Page 4 - Page 5 / Figures 2-3

### 中文翻译

Wave attack 利用固定防护周期，把攻击访问组织成波形。攻击者在防护机制重置或 delay window 周围安排 aggressor activations，使多个 rows 接近危险状态，同时尽量减少触发有效 preventive refresh 的机会。这种攻击强调跨时间窗口累积 disturbance。

Feinting attack 则通过“佯攻”访问诱导防护机制把资源用在并非真正危险的 rows 上，再把真实攻击 rows 推向危险状态。它利用固定刷新数量和确定性选择策略，使防护资源被误导。

这两类攻击的共同点是：它们不只追求高 activation count，而是利用防护协议的时序和资源分配规则。传统只看平均 workload 或简单 hammering 的评估很难发现这些问题。

工程启示是，RowHammer 防护验证需要包含 protocol-aware attacks。攻击者会读论文和标准，会利用 back-off、delay、counter reset、refresh quota 等细节。

## 5. Chronus Design Overview / Chronus 设计总览

### 原文位置

Page 6 - Page 8 / Chronus design

### 中文翻译

Chronus 的设计围绕三项改进。

第一，counter update 与 data path 分离。Chronus 重新组织 activation counters，使计数更新可以与正常访问并行执行，而不是阻塞 tRP/tRC 等关键路径。这样，PRAC 的基本“内部计数”能力被保留，但普通访问 latency 不再承受同等开销。

第二，动态控制 preventive refresh 数量。Chronus 不采用固定刷新数，而是根据当前 risk state、计数状态或访问模式调整需要刷新的 rows 数量。这样可以在低风险时减少过度刷新，在高风险时提供足够保护。

第三，移除固定 delay period。Chronus 避免给攻击者一个可预测的刷新后窗口，从而降低 wave attack 和 feinting attack 的有效性。防护流程更连续、更自适应，不依赖容易被对齐的固定节奏。

这些设计共同目标是把 PRAC 从“固定、阻塞、可预测”的防护流程，改造成“并行、自适应、不易被节奏利用”的防护流程。

## 6. Counter/Data Path Decoupling / 计数器与数据路径解耦

### 原文位置

Page 6 - Page 7

### 中文翻译

Chronus 把 counter update 从正常访问关键路径中移开。传统 PRAC 中，activation 后需要更新 counter，这可能延长 precharge/activate cycle。Chronus 通过结构调整，使 counter update 与 DRAM data access 并行或后台执行。

这种设计对性能至关重要。Memory-intensive workloads 通常受限于 DRAM timing 和 bank-level parallelism。如果每个 activation 都增加固定 latency，性能损失会在所有 workload 中出现。把 update 并行化后，只有真正触发防护时才产生显著开销。

工程上需要关注 counter consistency 和 race conditions。若 counter update 延迟执行，必须保证攻击者不能在 update 完成前快速累积未计数 activations。Chronus 需要在并行性和安全可证明性之间保持平衡。

## 7. Dynamic Preventive Refresh / 动态保护刷新

### 原文位置

Page 7 - Page 8

### 中文翻译

固定 preventive refresh 数量的问题是缺乏上下文。某些情况下一个或少数 victim rows 需要保护，另一些情况下多个 rows 可能同时接近风险。Chronus 动态决定 preventive refresh 数量，使防护资源更贴合实际风险。

这样做有两个收益。性能上，避免低风险情况下过度刷新。安全上，在攻击模式更复杂时可以提供更多刷新，而不是被固定 quota 限制。

对硬件实现而言，动态刷新需要额外控制逻辑和状态判断。它还可能影响 JEDEC timing、refresh scheduling 和 controller policy。论文评估显示这些成本相对收益可接受，但真实产品仍需做 RTL/PPA 和验证。

## 8. Removing the Delay Period / 移除固定延迟期

### 原文位置

Page 7 - Page 8

### 中文翻译

PRAC variants 中的 delay period 原本用于给防护流程留出时间或避免连续触发。但固定 delay period 会暴露可预测窗口。攻击者可以在 delay 前后组织访问，使防护节奏被利用。

Chronus 移除固定 delay period，让防护行为不再以简单周期暴露给攻击者。这降低了 wave attack 和 feinting attack 的效果，也减少了不必要等待。

工程上，移除 delay 不代表没有任何保护间隔，而是把固定等待替换为更细粒度的状态驱动控制。控制器和 DRAM 需要更紧密地协同，确保刷新完成、计数状态更新和普通请求恢复之间没有安全漏洞。

## 9. Evaluation Methodology / 评估方法

### 原文位置

Page 9 - Page 10

### 中文翻译

论文使用与 PRAC 分析类似的模拟框架和 workload 设置，评估现代 NRH 和未来低 NRH 场景。比较对象包括多种 PRAC variants、Graphene、Hydra、PARA。指标包括 performance overhead、DRAM energy overhead、storage/implementation cost，以及 adversarial attacks 下的稳健性。

作者特别关注 NRH=1K 和 NRH=20。前者代表现代或近期较低阈值；后者代表未来极低阈值压力测试。若一个方案在 NRH=20 下仍可接受，说明它对 scaling 更有前景。

## 10. Performance and Energy Results / 性能与能耗结果

### 原文位置

Page 10 - Page 12 / Evaluation figures

### 中文翻译

论文报告，PRAC 在现代 NRH>1K 下平均/最大性能开销约 5.8%/8.9%，能耗约 10.7%/13.5%；在 NRH=20 下性能开销约 78.5%/90.7%，能耗约 6.6x/7.1x。不同版本数值与前序 PRAC 分析略有差异，论文附录说明了 errata/bug 修正，应以当前版本为准。

Chronus 在 NRH=1K 下平均性能开销低于 0.1%，DRAM energy overhead 约 10.3%。这说明 counter/data path decoupling 成功消除了大部分普通访问路径开销。

在 NRH=20 下，Chronus 平均性能开销约 8.3%，能耗约 17.9%。相比 PRAC variants 的灾难性开销，Chronus 保持在更可接受范围。虽然 8.3% 仍不是零成本，但对未来低阈值 DRAM 来说，这已经是数量级改善。

## 11. Security and Attack Robustness / 安全性与抗攻击能力

### 原文位置

Page 10 - Page 13 / Attack evaluation

### 中文翻译

Chronus 对 wave attack 和 feinting attack 更稳健，因为它不依赖固定刷新数量和固定 delay window。动态 preventive refresh 使攻击者更难用佯攻耗尽固定刷新 quota；移除固定 delay 使攻击者更难对齐防护节奏。

与 Graphene、Hydra、PARA 相比，Chronus 在不同 NRH 区间保持较好综合表现。Graphene/Hydra 需要 controller-side tracking 和 metadata，PARA 在低 NRH 下概率刷新成本高。Chronus 的优势是保留工业 PRAC 的 DRAM 内部信息优势，同时缓解其 timing 和协议弱点。

不过，Chronus 主要针对 activation-count based read disturbance。RowPress、temporal variation、spatial variation 和 vendor-specific remapping 仍可能带来额外挑战。若 row-open time 成为主要风险变量，Chronus 还需要扩展模型。

## 12. Errata and Version Awareness / 勘误与版本意识

### 原文位置

Appendix / Errata

### 中文翻译

论文附录包含 artifact 信息和 bug 修正说明。作者指出早期结果中存在修正，当前 v2 结果应作为引用依据。阅读这类系统评估论文时，版本意识非常重要：模拟器 bug、参数设置、timing model 或 workload mix 的变化都可能影响数值。

工程上，引用 Chronus 结果时应明确版本和 commit/artifact。若用其结论指导产品或研究，需要复现实验或至少核对修正后的表格。

## 13. Conclusion / 结论

### 原文位置

Page 13 / Conclusion

### 中文翻译

Chronus 说明，PRAC/RFM 的工业方向有价值，但第一代机制的时间组织方式会导致高开销和攻击窗口。通过 counter/data path decoupling、dynamic preventive refresh 和移除 fixed delay period，Chronus 显著降低正常 workload 开销，并提升对 protocol-aware attacks 的鲁棒性。

论文的核心贡献是把 RowHammer 防护从“是否计数”推进到“如何在时间上组织计数、刷新和控制器协同”。这对未来 DDR5/DDR6、HBM 和其它高密度 DRAM 防护都有启发。

## 14. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文设计、评估和附录的工程化解读

### 中文学习笔记

1. 对 memory controller：Chronus 强调防护协议不能阻塞关键路径。设计 controller/DRAM 协同时，应优先把常态路径开销降到最低。

2. 对 DRAM architecture：counter update 可以并行化，但必须证明计数延迟不会产生安全漏洞。这是微架构和安全证明共同问题。

3. 对验证：必须加入 wave attack、feinting attack 这类 protocol-aware patterns。只测随机访问和传统 double-sided hammering 不够。

4. 对标准：未来 JEDEC 方案可能需要更灵活动态的 RFM 语义，而不是固定刷新数量和固定 delay。

5. 对行业：Chronus 是 PRAC 的自然演进方向。它说明工业标准可以从学术攻击分析中快速迭代。

6. 对个人学习：先读 PRAC 安全/开销分析，再读 Chronus。重点理解三个设计点：并行 counter update、动态 preventive refresh、去除 fixed delay。

## 15. 不确定与需回原文核对

- Page 10-13 的各方案数值需回 PDF 对照图表。
- 附录 errata 必须一起阅读，引用时应说明使用 v2 结果。
- Chronus 对 RowPress、VRD、HBM2/HBM3 的适用性还需额外验证。
- 真实 DDR5/DDR6 采用 Chronus 类机制需要标准、vendor implementation 和 controller support。
