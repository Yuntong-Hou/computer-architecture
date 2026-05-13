# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖摘要、PRAC/RFM 背景、安全分析、timing/性能/能耗开销、与学术方案比较、可用性攻击和硬件工程师视角。保留 PRAC、RFM、NRH、RowHammer、Graphene、Hydra、PARA、availability attack 等英文术语。参考文献保留英文。

## Title

原文标题：Understanding the Security Benefits and Overheads of Emerging Industry Solutions to DRAM Read Disturbance

中文标题：理解新兴工业 DRAM 读扰动解决方案的安全收益与开销

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

DRAM read disturbance，尤其是 RowHammer，已经从器件可靠性问题演变为系统安全问题。过去工业界的 TRR 实现高度不透明，学术界多次展示其可被绕过。JEDEC 在 DDR5 中引入 Per Row Activation Counting（PRAC）和 Refresh Management（RFM）等机制，试图用标准化方式让 DRAM 与 memory controller 协同防护 RowHammer。

本文系统分析这些新兴工业方案的安全收益和开销。作者研究 PRAC/RFM 的安全条件、对 DRAM timing 的影响、benign workloads 下的性能和能耗成本、与 Graphene/Hydra/PARA 等学术方案的比较，以及攻击者是否能利用 PRAC/RFM 自身造成 memory availability attack。

论文结论是：PRAC 可以配置为安全，但依赖明确 NRH 假设。若任何位置在 20 次访问前不会产生 bit flip，即 NRH >= 20，PRAC 可提供防护。但随着未来 DRAM 阈值降低，PRAC 的性能和能耗开销急剧增加。在 NRH=20 场景下，平均性能开销可达 84.7%，最大可达 94.0%，能耗开销可达 13x 平均和 18x 最大。攻击者还可构造访问模式占用大部分 DRAM throughput，造成严重可用性下降。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

RowHammer 防护长期面临两个问题：第一，DRAM scaling 使 RowHammer threshold 持续下降；第二，工业防护机制缺乏透明、标准化语义。过去很多 DDR4 TRR 机制由厂商私有实现，平台方和研究者很难知道其计数粒度、阈值、victim selection 和边界条件。TRRespass、Blacksmith 等攻击表明，黑盒 TRR 可能被系统性绕过。

DDR5 PRAC/RFM 的出现是重要变化。它将一部分防护行为标准化：DRAM 内部进行 per-row activation counting，当计数接近风险阈值时，通过 back-off/alert 类机制通知 memory controller；控制器随后发出 RFM commands，使 DRAM 执行 refresh management。

论文的出发点是：工业标准方案不能只看“是否更安全”，还必须量化代价。PRAC 会改变正常访问路径 timing，也会在触发 RFM 时暂停普通请求。随着 NRH 降低，触发频率上升，性能和能耗开销可能失控。此外，防护机制本身也可能成为攻击者制造 denial-of-service 的工具。

## 2. Background: RowHammer, PRAC, and RFM / 背景：RowHammer、PRAC 与 RFM

### 原文位置

Page 2 - Page 3 / Background

### 中文翻译

RowHammer 由反复激活 aggressor rows 触发。NRH 表示在 victim row 发生 bit flip 前 aggressor row 可以承受的 activation 次数。NRH 越低，防护必须越频繁。

PRAC 的基本思想是在 DRAM 内部跟踪 row activations。相比 memory controller 侧计数，DRAM 内部更接近真实 physical row 和 vendor-specific mapping。RFM 则提供 controller 与 DRAM 的协同刷新路径：当 DRAM 指示需要管理刷新时，controller 发出 RFM 命令，DRAM 刷新潜在 victim rows 或执行内部防护操作。

这种分工有吸引力，因为它把物理邻近、内部 remapping 和防护细节留给 DRAM，同时让 controller 遵循标准协议。然而，它也引入新的 timing 和协议约束。DRAM 需要更新 counters，controller 需要响应 back-off，并在 RFM 期间暂停或延迟普通内存请求。

对硬件工程师来说，PRAC/RFM 的本质是把 RowHammer 防护纳入 JEDEC timing contract。它不再是纯内部黑盒，也不是纯 controller policy，而是跨芯片边界的协议设计。

## 3. Security Analysis / 安全分析

### 原文位置

Page 3 - Page 4 / Security Analysis

### 中文翻译

论文证明，在合适配置下，PRAC 可以防止 RowHammer bit flips。关键条件是：任何 DRAM location 在少于 20 次相关访问前不会发生 bit flip，即 NRH >= 20。在这个假设下，PRAC 可以通过及时触发 RFM，让 victim rows 在达到危险 disturbance 前被保护。

这个结果很重要，因为它给 PRAC 一个明确安全边界。它说明 PRAC 不是“经验上可能有用”的机制，而是可以在特定 NRH 假设下配置为安全。但它也说明安全不是无条件的。如果未来器件 NRH 低于该边界，或者 RowPress/temporal variation 等机制绕过 activation count 模型，PRAC 的安全证明需要重新审视。

安全分析还依赖 PRAC 对 row activation 的覆盖粒度、counter update 的正确性、RFM 对 victim rows 的实际保护范围，以及 controller 是否严格遵守 back-off/RFM 协议。任何实现偏差都可能削弱理论保证。

## 4. Timing and Implementation Overheads / 时序与实现开销

### 原文位置

Page 4 - Page 5 / Timing discussion

### 中文翻译

PRAC 不是零成本机制。DRAM 每次 row activation 后需要更新对应 counter 或相关 tracking state，这会影响 tRP、tRC 等关键 timing。若 counter update 位于关键路径，普通内存访问即使没有触发 RFM 也会变慢。

RFM 触发后，memory controller 需要暂停普通请求并发送 RFM commands。RFM 本身占用 command bus、bank/rank 资源和内部 refresh bandwidth。低 NRH 时，RFM 触发频率上升，系统更频繁进入保护刷新状态，正常请求排队延迟增加。

这部分对实际产品非常关键。DRAM timing parameter 的小幅增加会在高带宽系统中放大为明显性能损失。尤其是 memory-intensive workloads，tRC/tRP 增加会直接降低 row activation throughput。

## 5. Evaluation Methodology / 评估方法

### 原文位置

Page 5 / Experimental setup

### 中文翻译

作者使用 cycle-level/system-level 模拟评估 PRAC。工作负载包括 60 个 benign four-core workloads，并覆盖不同 NRH 设置：现代较高阈值如 10000、4800、1000，以及未来低阈值如 128、64、20。比较对象包括 Graphene、Hydra 和 PARA 等学术防护。

评估指标包括 system performance slowdown、DRAM energy overhead、storage cost、DRAM throughput loss，以及 adversarial workload 下的性能下降。作者关注两个维度：正常工作负载是否承担过高成本，攻击者是否能利用防护机制本身制造可用性攻击。

## 6. Benign Workload Results / 正常工作负载结果

### 原文位置

Page 5 - Page 6 / Figures 2-3

### 中文翻译

对于现代 NRH 设置，如 10000、4800 和 1000，PRAC 的平均性能开销约 9.9%，最大约 13.1%；DRAM energy overhead 平均约 18.5%，最大约 22.7%。这说明即使在当前较高 NRH 场景下，PRAC 也不是免费机制。

当 NRH 降到未来极低值 20 时，PRAC 开销急剧上升。论文报告平均性能开销约 84.7%，最大约 94.0%；能耗开销平均约 13x，最大约 18x。这接近系统不可用级别。原因是低 NRH 下 PRAC/RFM 需要非常频繁地介入，正常请求大量等待防护刷新。

这些结果传达出一个清晰工程信号：标准化防护方向正确，但若协议实现把过多工作放在关键路径或固定刷新流程中，低阈值未来会面临严重 scalability 问题。

## 7. Comparison with Graphene, Hydra, and PARA / 与 Graphene、Hydra、PARA 的比较

### 原文位置

Page 6 / Comparative evaluation

### 中文翻译

论文将 PRAC 与 Graphene、Hydra、PARA 比较。不同方案的相对优劣依赖 NRH。PARA 实现简单，但在低 NRH 下需要较高概率刷新，开销迅速上升。Graphene 和 Hydra 使用 tracking/metadata 思路，可以在某些阈值区间更高效，但也有 storage 和实现复杂度。

PRAC 的优势是工业标准化和 DRAM 内部信息可见性。它不需要 controller 完全理解物理邻近关系，且可与 DRAM 内部实现结合。但 PRAC 的劣势是 timing 和 RFM 开销在低 NRH 下非常重。

工程上，不能简单说“标准方案一定优于学术方案”。实际选择要看 NRH、workload memory intensity、DRAM timing、controller implementation、area budget、ECC/RAS 组合以及可验证性。

## 8. Storage and Energy Cost / 存储与能耗成本

### 原文位置

Page 6 / Figure 4 and energy analysis

### 中文翻译

PRAC 需要在 DRAM 内部维护 activation counting state。具体 storage cost 取决于 counter granularity、counter width、per-row/per-group 组织和 vendor implementation。论文将 storage cost 纳入比较，强调工业方案不仅要安全，还要满足 DRAM die 面积和成本约束。

能耗开销来自两部分：正常访问路径上 counter update 和 timing 增加，以及 RFM 触发后的额外 refresh/管理操作。低 NRH 下，后一部分会成为主导，因为系统频繁执行保护刷新。

对硬件工程师来说，能耗评估不能只看 DRAM device energy。RFM 导致的性能下降可能让处理器/加速器更长时间等待，增加系统级 energy-to-solution。HBM/GPU 场景下，这种等待会浪费昂贵计算资源。

## 9. Availability Attack / 可用性攻击

### 原文位置

Page 7 / Attack analysis

### 中文翻译

论文指出，PRAC/RFM 引入新的 attack surface。攻击者可以构造访问模式，故意频繁触发 PRAC/RFM，使 DRAM 大量时间用于防护刷新而不是服务正常请求。作者报告 adversarial pattern 最多可占用 94% DRAM throughput，使系统性能平均下降 86.8%，最高下降 94.5%。

这类攻击不一定需要触发 bit flip。攻击目标是利用防护机制本身制造 denial-of-service 或 performance degradation。安全机制如果缺少 rate limiting、fairness 和 isolation，就可能从防护变成放大器。

工程意义是：RowHammer defense 必须同时防 bit flips 和防 DoS。Memory controller 需要考虑 per-domain accounting、request throttling、tenant isolation、RFM budget、QoS policy 和异常模式检测。云场景尤其需要防止一个租户通过内存访问模式拖垮其它租户。

## 10. Discussion / 讨论

### 原文位置

Page 7 - Page 8 / Discussion and conclusion

### 中文翻译

论文认为 PRAC 是工业界迈向透明、标准化 RowHammer 防护的重要一步。它相比私有 TRR 更可分析，也为 controller-DRAM 协同提供了协议基础。但 PRAC 的当前形态仍有明显瓶颈：关键路径 timing overhead、低 NRH 下高 RFM 频率，以及可用性攻击风险。

这些发现直接推动后续改进方向：减少 counter update 对关键路径的影响，动态调整 preventive refresh 数量，避免固定 delay window 被攻击利用，并在协议层加入抗 DoS 设计。Chronus 正是沿着这条路线提出改进。

## 11. Conclusion / 结论

### 原文位置

Page 8 / Conclusion

### 中文翻译

本文系统分析 JEDEC DDR5 PRAC/RFM 的安全和开销。结论是，PRAC 可以在 NRH >= 20 的假设下配置为安全，但它在现代 NRH 下已有可观性能/能耗成本，在未来低 NRH 下成本可能达到不可接受水平。PRAC 还引入 memory availability attack 面，使攻击者可利用防护机制占用大量 DRAM throughput。

因此，工业标准方案需要继续演进。标准化和透明化是正确方向，但实现必须兼顾安全、性能、能耗、可用性和可验证性。

## 12. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文安全分析、评估和讨论的工程化解读

### 中文学习笔记

1. 对 DDR5/DDR6 controller：PRAC/RFM 是未来必须理解的协议级机制。控制器不仅要发命令，还要管理 RFM 调度、QoS 和异常触发。

2. 对性能建模：RowHammer defense overhead 必须进入 memory subsystem performance model。低 NRH 下，RFM 可能成为主导瓶颈。

3. 对安全架构：防护机制本身会被攻击者利用。需要把 availability attack 当作正式 threat model。

4. 对产品验证：验证用例应包括 benign workloads、worst-case streaming、random hammering、multi-tenant adversarial patterns 和 RFM storm。

5. 对行业：PRAC 代表工业界承认 RowHammer 需要标准化处理，但第一代协议可能只是过渡。未来方案需要更灵活的计数和刷新管理。

6. 对个人学习：这篇应和 Chronus 连读。先掌握 PRAC 的安全边界和开销来源，再看 Chronus 如何重构这些瓶颈。

## 13. 不确定与需回原文核对

- PRAC/RFM 细节基于公开 JEDEC 语义和论文模型，具体厂商实现可能不同。
- Figures 2-4 的各 NRH 数值和对比方案结果建议回 PDF 核对。
- Availability attack 的实际影响依赖系统调度、tenant isolation 和 controller policy。
- RowPress、VRD 和 temporal variation 对 PRAC 安全模型的影响需要结合其它论文继续分析。
