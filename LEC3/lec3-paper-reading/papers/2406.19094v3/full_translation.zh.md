# Full Chinese Translation

## 版权与完整性说明
以下为基于 PDF 提取文本的逐节中文详译/译述。为遵守版权边界，不提供逐字长篇翻译；技术术语、指标和机制名称保留英文。

## Title
原文标题：Understanding the Security Benefits and Overheads of Emerging Industry Solutions to DRAM Read Disturbance

中文标题：理解新兴工业 DRAM 读扰动解决方案的安全收益与开销

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
本文分析 DDR5 标准中新出现的 PRAC/RFM 机制。PRAC 让 DRAM 在片内跟踪 row activation，并在需要时通知 memory controller 触发 RFM。作者从安全、性能、能耗、存储成本和攻击面角度评估该机制。结论是：PRAC 可以在特定 NRH 条件下提供安全保证，但随着 RowHammer threshold 降低，它的性能和能耗开销会急剧上升，并可能被攻击者用来制造内存可用性攻击。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
引言强调 RowHammer 防护已经从学术问题变成工业标准问题。过去厂商使用 TRR-like 机制，但实现不透明且已有绕过案例。JEDEC 的 PRAC/RFM 是更公开、标准化的方向，因此需要认真评估它是否足够安全，以及部署代价是否可接受。

作者提出一个核心矛盾：如果未来 DRAM 的 NRH 继续降低，任何防护都必须更频繁地触发。PRAC 虽然把一部分逻辑放入 DRAM 内部，但它仍需要 memory controller 停止正常请求并执行 RFM。因此低 NRH 可能把保护流量变成主要瓶颈。

## 2. Background: PRAC and RFM / 背景：PRAC 与 RFM

### 原文位置
Page 2 - Page 3

### 中文翻译
PRAC 即 Per-Row Activation Counting。DRAM 片内维护与 row activation 相关的计数或近似计数，当某些 row 接近危险阈值时，DRAM 向 memory controller 发出 back-off signal。控制器收到信号后需要暂停普通内存访问，并发出 RFM 命令。

RFM 即 Refresh Management。它让 DRAM 执行与潜在 victim row 相关的额外刷新，以避免电荷被扰动到错误状态。PRAC/RFM 的目标是比传统固定周期刷新更有针对性，但这也引入了新的 timing constraints，如 tRP/tRC 增加，以及 back-off 期间的服务中断。

## 3. Security Analysis / 安全分析

### 原文位置
Page 3 - Page 4

### 中文翻译
安全分析试图回答：PRAC 在什么条件下可以阻止 RowHammer。作者给出一个关键结论：如果 DRAM 中任何位置在被访问 20 次之前不会产生 bitflip，即 NRH 至少为 20，那么 PRAC 可以通过适当配置保证安全。

这个结论的重要性在于，它把 PRAC 的安全边界明确化。PRAC 不是靠概率侥幸工作，而是可以在特定 threshold 假设下给出形式化 reasoning。但这个假设也说明，如果未来器件的有效阈值低于该范围，或者 RowPress/VRD 等现象使实际风险偏离 activation count 模型，PRAC 需要重新评估。

## 4. Performance and Energy Evaluation / 性能与能耗评估

### 原文位置
Page 4 - Page 6

### 中文翻译
作者用 60 个四核 benign workload 评估 PRAC。对现代 NRH 设置 10000、4800 和 1000，PRAC 的平均性能开销约 9.9%，最大约 13.1%；DRAM energy overhead 平均约 18.5%，最大约 22.7%。这些结果说明，即使在相对宽松阈值下，PRAC 也会带来非忽略的系统代价。

当 NRH 降至未来更严苛的 128、64、20 时，开销急剧上升。特别是 NRH=20 时，平均性能开销约 84.7%，最大约 94.0%；能耗开销可达 13x 平均、18x 最大。此时系统大量时间花在防护相关等待和 RFM 上，正常内存服务被严重挤压。

## 5. Comparison with Prior Defenses / 与已有防护比较

### 原文位置
Page 6

### 中文翻译
论文将 PRAC 与 Graphene、Hydra 和 PARA 比较。结果不是单向的：在较低 NRH 区间，PRAC 相比 PARA 更有优势，因为 PARA 的概率刷新需要非常频繁才能保证安全；与 Graphene/Hydra 相比，PRAC 在某些低阈值下表现接近。

但在现代较高 NRH 下，一些学术方案可能以更低性能开销达到类似目标。这说明工业标准方案的价值不仅在性能，还在可部署性、标准化和片内可见性；但从系统效率角度，它仍有改进空间。

## 6. Storage and Implementation Cost / 存储与实现成本

### 原文位置
Page 6, Figure 4

### 中文翻译
PRAC 需要在 DRAM 片内维护 activation tracking 相关状态。论文估算 counter/storage cost，并将其作为工业可行性的一部分。对 DRAM 厂商来说，面积和功耗成本非常敏感，因此防护设计必须在安全性、存储开销、时序开销之间平衡。

## 7. Memory Performance Attack / 内存性能攻击

### 原文位置
Page 7

### 中文翻译
作者进一步指出，PRAC/RFM 可能成为攻击者利用的性能攻击面。攻击者可以构造访问模式频繁触发 back-off 和 RFM，使 memory controller 大量时间无法服务正常请求。论文报告 adversarial pattern 最多可占用 94% DRAM throughput，使系统性能平均下降 86.8%，最高下降 94.5%。

这个结果非常重要，因为防护机制原本用于阻止 RowHammer bitflip，但如果它能被廉价触发并造成服务降级，就会形成新的 denial-of-service 风险。

## 8. Discussion / 讨论

### 原文位置
Page 7 - Page 8

### 中文翻译
讨论部分强调未来方案需要同时满足安全、低开销和抗滥用。单纯把 activation counter 放进 DRAM 并不自动解决问题；关键在于 counter 更新是否在关键路径上、RFM 是否会阻塞正常请求、保护刷新数量是否固定、以及攻击者能否操纵触发频率。

这些观察直接引出后续 Chronus 一类方案：通过改进计数器组织、动态控制刷新数量和消除不必要 delay 来降低开销。

## 9. Conclusion / 结论

### 原文位置
Page 8

### 中文翻译
本文结论是：PRAC/RFM 是 RowHammer 防护标准化的重要进展，能够在一定 NRH 假设下提供安全保证。然而，它在性能、能耗和可用性攻击方面存在显著挑战。若 DRAM vulnerability 继续恶化，现有 PRAC 设计可能无法以可接受成本维持安全。
