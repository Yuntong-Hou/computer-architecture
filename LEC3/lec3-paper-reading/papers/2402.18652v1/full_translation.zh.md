# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它覆盖论文摘要、背景、真实 DDR4 芯片实验、空间变化观察、Svärd 设计、安全性、硬件复杂度、系统性能评估、相关工作和硬件工程师视角。保留 RowHammer、read disturbance、BER、HCfirst、Svärd、AQUA、BlockHammer、Hydra、PARA、RRS 等英文术语。参考文献保留英文。

## Title

原文标题：Spatial Variation-Aware Read Disturbance Defenses: Experimental Analysis of Real DRAM Chips and Implications on Future Solutions

中文标题：空间变化感知的读扰动防护：真实 DRAM 芯片实验分析及其对未来方案的启示

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

RowHammer/read disturbance 防护通常假设 DRAM 中所有 rows 使用统一最坏情况阈值 NRH。随着 DRAM scaling，最弱 rows 的阈值降低会迫使系统更频繁触发防护，从而带来更高性能和能耗开销。但真实芯片并非所有 rows 同样脆弱。本文通过 144 颗真实 DDR4 chips 的大规模实验表明，read disturbance vulnerability 存在显著 spatial variation。

作者发现，即使在同一 subarray 内，BER 可相差约 2x，HCfirst 可相差一个数量级。简单依赖 row index、bank position 或其它粗粒度空间特征并不能稳定预测脆弱性，因为 15 个 modules 中只有 4 个表现出明显相关性。基于这些观察，论文提出 Svärd，一个 spatial variation-aware defense framework。Svärd 利用 row-level 或 row-group-level profile，为不同 rows 设置不同防护 aggressiveness。

Svärd 不是替代所有 RowHammer defenses 的单一机制，而是可以叠加到 AQUA、BlockHammer、Hydra、PARA、RRS 等已有机制上。评估显示，Svärd 在 120 个 multiprogrammed memory-intensive workloads 上显著降低防护性能开销，同时在 adversarial access patterns 下仍需对弱 rows 保持保守保护。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

RowHammer 防护的根本难题是安全与开销之间的矛盾。为了保证所有 rows 不发生 bit flips，系统必须以最弱 row 的 threshold 为基准设置防护参数。随着 DRAM scaling，最弱 row 可能变得越来越弱，导致防护越来越频繁，性能和能耗开销快速上升。

然而，如果大多数 rows 实际上比最弱 row 稳健得多，为所有 rows 采用同一最坏情况参数就会过度保守。论文的核心问题是：能否利用真实芯片中的 spatial variation，让弱 rows 获得强保护，让稳健 rows 使用较低开销的保护，从而在不牺牲安全的情况下降低平均开销。

作者强调，这不是简单把某些地址范围标记为安全或危险。真实 DRAM 的空间变化可能受到制造偏差、subarray layout、local circuit variation、温度、电压和老化影响。必须通过测量 profile 了解实际芯片，而不是只依赖启发式位置规则。

## 2. Background / 背景

### 原文位置

Page 2 - Page 3 / Section 2

### 中文翻译

论文回顾 DRAM 结构、RowHammer/read disturbance 和常见防护方式。DRAM row 被 ACT 打开后，数据进入 row buffer；访问其它 row 前必须 PRE。重复 ACT/PRE 某些 aggressor rows 会对邻近 victim rows 造成 disturbance。

防护通常依赖一个阈值 NRH，即假设在 victim row 发生 bit flip 前 aggressor row 最多能被安全激活多少次。若 NRH 很低，防护机制必须更频繁地刷新或节流。已有方案包括 probabilistic refresh、counter-based tracking、access throttling、row remapping 和 metadata-based defenses。

本论文关注的不是发明一种全新 RowHammer 防护，而是研究防护参数是否应当 spatially adaptive。若不同 rows 的实际 vulnerability 差异很大，统一 NRH 会浪费性能；但若 profile 不稳定或攻击者能集中访问弱 rows，过于乐观的 adaptive defense 会带来安全漏洞。

## 3. Motivation and Goal / 动机与目标

### 原文位置

Page 3 - Page 4 / Section 3

### 中文翻译

作者的动机来自两个观察。第一，真实 DRAM chips 的 read disturbance vulnerability 并不均匀。第二，未来随着 NRH 继续降低，传统 worst-case defense 的开销会越来越难接受。因此，利用 spatial variation 可能成为降低开销的重要方向。

论文目标包括：大规模测量真实 DDR4 chips 中的 spatial variation；分析这种 variation 是否能被简单空间特征预测；设计可与已有 defenses 组合的 spatial variation-aware framework；评估该 framework 在 benign workloads 和 adversarial access patterns 下的性能与安全影响。

对硬件工程师来说，这个问题与 binning、repair、profiling、RAS telemetry 类似。行业已经接受芯片存在 variation，但 RowHammer 防护长期仍倾向使用全局阈值。Svärd 的意义是把 variation-aware 思路引入安全防护参数。

## 4. Experimental Infrastructure and Methodology / 实验基础设施与方法

### 原文位置

Page 4 - Page 5 / Figure 2, Table 1

### 中文翻译

作者使用基于 DRAM Bender 的 DDR4 testing infrastructure，对 144 颗真实 DDR4 chips 进行实验。这些 chips 来自 15 个 modules、10 种 chip design 和 3 家主要 vendors。测试覆盖不同 temperature、bank、row address 和 data pattern。

实验流程一般包括写入特定 data pattern，对 aggressor rows 执行 hammering 或 read disturbance pattern，然后读取 victim rows 统计 bit flips。主要指标包括 BER 和 HCfirst。BER 衡量错误比例，HCfirst 衡量触发第一个 bit flip 所需 hammer count。

作者在不同空间粒度上分析结果，包括 module、chip、bank、subarray、row 和 row group。论文还关注简单空间特征是否可预测 vulnerability，例如 row 在 subarray 中的位置、bank 位置或行号模式。

这部分对工程实践很重要，因为 profile 的质量决定 adaptive defense 是否可信。若测试覆盖不足，防护参数可能对未测温度、电压、老化或 workload 条件不安全。

## 5. Spatial Variation Observations / 空间变化观察

### 原文位置

Page 5 - Page 8 / Figures 3-10

### 中文翻译

实验结果显示，真实 DDR4 chips 中的 read disturbance vulnerability 有显著空间变化。同一 subarray 内 BER 可相差约 2x，HCfirst 可相差一个数量级。这意味着某些 rows 在相同 hammering 条件下更早出错，而另一些 rows 能承受更多 activations。

作者进一步分析 row/subarray/bank/module 等层级。不同 modules 和 chip designs 的整体脆弱性不同；同一 chip 内部不同 banks 和 row ranges 也有差异。某些区域可能形成较弱 clusters，但这种模式并不总是稳定可预测。

一个关键结论是：简单空间特征不可靠。论文报告，在 15 个 modules 中，只有 4 个表现出明显 correlation。这说明不能只用“某些 row index 更危险”这类规则替代实际 profile。物理布局和制造 variation 比外部地址可见特征更复杂。

硬件工程意义是：如果未来要做 row-level adaptive defense，系统需要获得真实 profile，而不是依赖 JEDEC 地址或 controller 地址的简单映射。profile 数据本身也需要存储、保护和更新。

## 6. Svärd: Spatial Variation-Aware Defense / Svärd 设计

### 原文位置

Page 10 - Page 12 / Section 6

### 中文翻译

Svärd 是一个 spatial variation-aware framework。它利用 row-level 或 row-group-level vulnerability profile，为不同 rows 设置不同的防护 aggressiveness。弱 rows 使用更保守配置，例如更低 tracking threshold、更频繁 preventive refresh 或更强 throttling；稳健 rows 使用较宽松配置，从而降低平均开销。

Svärd 的重要定位是 wrapper，而不是单独替代所有 defense。作者将它与 AQUA、BlockHammer、Hydra、PARA 和 RRS 结合。这样可以复用已有防护机制，只改变它们对不同 rows 的参数配置。

Svärd 的基本流程可以理解为：首先通过离线或在线 profiling 得到 vulnerability map；然后把 profile 压缩成可用于 runtime 的 metadata；最后 memory controller 或防护逻辑根据访问 row 的 profile class 选择防护强度。

这种方法的关键工程问题是 metadata 存储和访问。若 profile 太细，存储成本高；若太粗，又可能丢失弱 rows 信息。metadata 还必须在攻击者不可篡改的结构中保存，并且不能让 metadata access 成为性能瓶颈。

## 7. Security Considerations / 安全性

### 原文位置

Page 12 - Page 13 / Section 6.3

### 中文翻译

Svärd 的安全性依赖一个基本原则：对每个 row，防护强度必须覆盖该 row 的实际 vulnerability。不能因为大多数 rows 稳健，就对所有 rows 降低保护。攻击者可以选择性访问最弱 rows，因此安全边界必须按 row-specific worst case 设定。

论文在 adversarial access patterns 下分析 Svärd，说明如果 profile 正确且弱 rows 被正确分类，Svärd 可以降低稳健 rows 的开销，同时保持弱 rows 的安全保护。反之，如果 profile 过期、测量不完整或攻击者能找到未正确标记的弱 rows，adaptive defense 会产生风险。

这对产品设计提出要求：profile 生命周期管理必须明确。制造测试 profile、系统启动时 profile、在线 background profiling、老化后更新、温度/电压补偿，都需要纳入安全模型。

## 8. Hardware Complexity / 硬件复杂度

### 原文位置

Page 13 / Section 6.4

### 中文翻译

Svärd 需要保存 read disturbance metadata。metadata 可以按 row、row group 或更粗粒度区域存储。更细粒度 metadata 提供更准确保护，但面积和访问开销更大；更粗粒度 metadata 成本更低，但可能因为包含少数弱 rows 而必须整体保守。

硬件实现可以放在 memory controller、on-DIMM logic、DRAM 内部或与现有 defense metadata 共享。不同位置有不同 tradeoff。Controller 侧更容易更新和验证，但可能缺少物理 row mapping；DRAM 内部更接近真实结构，但 area、power、标准接口和厂商实现约束更强。

对硬件工程师而言，Svärd 的难点不是算法概念，而是 metadata plumbing：地址转换、bank/subarray mapping、ECC/repair 后 row remapping、metadata consistency、secure update 和 low-latency lookup。

## 9. Evaluation / 系统评估

### 原文位置

Page 13 - Page 15 / Figure 12

### 中文翻译

作者将 Svärd 与 AQUA、BlockHammer、Hydra、PARA 和 RRS 组合，在 120 个 multiprogrammed memory-intensive workloads 上评估性能。结果显示，Svärd 可以显著降低原防护机制的性能开销。论文报告平均性能改善分别约为 1.23x、2.65x、1.03x、1.57x 和 2.76x，具体取决于与哪种 defense 组合。

这些结果说明，当 RowHammer defense 因低 NRH 变得昂贵时，利用 spatial variation 可以恢复一部分性能。收益最大的场景通常是原机制过于保守、许多 rows 实际不需要最强保护的场景。

但评估也表明，Svärd 不是免费收益。profile storage、lookup、更新和保守保护弱 rows 都有成本。更重要的是，它依赖真实 vulnerability profile。如果 temporal variation 或老化改变了弱 rows 集合，Svärd 需要及时更新，否则安全性下降。

## 10. Adversarial Pattern Analysis / 对抗访问模式分析

### 原文位置

Page 15 - Page 16 / Figure 13

### 中文翻译

论文专门分析 adversarial access patterns。攻击者不会按平均 workload 行为访问内存，而会集中访问最弱 rows 或构造最容易触发防护开销的模式。因此，Svärd 必须保证弱 rows 仍按照 worst-case threshold 防护。

结果显示，在正确 profile 的前提下，Svärd 可以在 adversarial 模式下保持安全，同时对非弱 rows 减少过度保护。但如果 profile 简化过度或弱 rows 被错误分类，攻击者可能利用这些盲点。

工程结论是：adaptive security mechanism 不能只用 benign workloads 评价。必须用 red-team style pattern、row selection attack、profile poisoning、temperature shift 和 aging scenario 评估。

## 11. Related Work / 相关工作

### 原文位置

Page 16 - Page 17 / Section 8

### 中文翻译

论文将自己放在 RowHammer characterization、DRAM testing infrastructure、RowHammer defenses 和 variation-aware memory reliability 的研究脉络中。已有工作证明 RowHammer 广泛存在，提出 PARA、BlockHammer、Hydra、AQUA、RRS 等防护。也有工作研究 DRAM retention variation、VRT、ECC、refresh optimization。

Svärd 的独特之处是把真实芯片 read disturbance spatial variation 直接用于调整防护 aggressiveness。它不是单纯测量现象，也不是单一新 defense，而是试图连接 device characterization 和 system-level defense parameterization。

## 12. Conclusion / 结论

### 原文位置

Page 17 / Conclusion

### 中文翻译

本文通过 144 颗 DDR4 chips 的实验表明，read disturbance vulnerability 存在显著 spatial variation。同一 subarray 内的 BER 和 HCfirst 都可能大幅不同，且简单空间特征不能稳定预测脆弱性。基于这些发现，作者提出 Svärd，将 row-level profile 用于调节已有防护机制的 aggressiveness。

Svärd 说明未来 RowHammer 防护不一定只能采用全局最坏情况阈值。通过 measurement-driven、spatially adaptive 的方式，可以在保证弱 rows 安全的同时降低稳健 rows 的防护开销。

## 13. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文实验、设计和评估的工程化解读

### 中文学习笔记

1. 对内存控制器：未来 controller 可能需要支持 row-class aware defense，而不是单一全局阈值。调度器、refresh engine 和防护模块都要能读取 vulnerability class。

2. 对制造测试：RowHammer/read disturbance profile 可能成为类似 binning 或 repair data 的一部分。问题在于 profile 时间和成本是否能被量产接受。

3. 对 RAS/firmware：profile 可能需要在 BIOS/firmware 中保存和更新，并与温度、老化、ECC error telemetry 结合。

4. 对安全：adaptive defense 必须防止攻击者专打弱 rows。profile 的正确性和保守性是安全边界。

5. 对行业：这篇论文体现 memory reliability 从“统一 guardband”向“measurement-driven adaptive guardband”演进。它与 DRAM retention profiling、RAIDR、AVATAR、REAPER 的思想相通。

6. 对个人学习：重点掌握 spatial variation 的实验证据、为什么简单 row index 不够、Svärd 如何叠加到已有 defenses、adversarial pattern 下为何仍要保护弱 rows。

## 14. 不确定与需回原文核对

- Figures 3-13 的精确图形趋势和各方案数值建议回 PDF 核对。
- Svärd 的 metadata 粒度和存储成本需要结合具体实现重算。
- 本文主要基于 DDR4；外推到 HBM2、DDR5、LPDDR5 需要额外实验。
- Temporal variation、temperature 和 aging 对 profile 的影响仍需继续阅读 VRD 等后续工作。
