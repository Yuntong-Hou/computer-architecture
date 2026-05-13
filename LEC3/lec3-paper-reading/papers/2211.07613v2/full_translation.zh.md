# Full Chinese Translation

## Title

原文标题：Fundamentally Understanding and Solving RowHammer

中文标题：从根本上理解并解决 RowHammer

原文位置：Page 1

处理说明：本文件按“完整度优先 + 硬件工程师视角”重写。该文是 invited overview / perspective paper，不提出新实验算法；译文按原文结构覆盖摘要、引言、2014-2020 回顾、2020 关键进展、近期 exploiting/understanding/mitigating RowHammer、未来方向和结论。参考文献列表保留英文，不逐条翻译。

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

本文概述 RowHammer vulnerability 的近期发展和未来方向。RowHammer 影响现代 DRAM chips，而 DRAM 几乎被所有计算系统用作主存。

RowHammer 是真实 DRAM chip 中反复访问某一 row 会导致物理邻近 rows 发生 bitflips 的现象。这一现象造成严重且广泛的系统安全漏洞。自 2014 年原始 RowHammer 论文以来，许多工作都证明了其影响。近期分析显示，随着 DRAM technology scaling 持续推进，RowHammer 问题正在显著恶化：较新的 DRAM chips 在 device 和 circuit levels 上本质上更易受 RowHammer 影响。更深入的分析还表明，该漏洞对许多变量敏感，包括环境条件（temperature、voltage）、process variation、stored data patterns、memory access patterns 和 memory control policies。

因此，设计完全安全且非常高效的 RowHammer protection mechanisms 很困难。DRAM 厂商尝试的防护已被证明缺乏 security guarantees。作者回顾 RowHammer 的 exploiting、understanding 和 mitigation 进展后，提出两大未来方向：第一，在 cutting-edge DRAM chips 和 field-deployed computing systems 中建立更深入的 RowHammer 理解；第二，通过 system-memory cooperation 设计极高效且完全安全的解决方案。

### 硬件工程师视角

摘要的关键信息是：RowHammer 不是单个攻击技巧，而是 DRAM scaling 的结构性后果。对硬件工程师来说，它影响 DRAM device design、memory controller policy、refresh、ECC、firmware、OS isolation、server RAS 和安全认证。任何只依赖“厂商说有 TRR”或“提高 refresh rate”的方案都不足以作为长期架构策略。

---

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Section 1

### 中文翻译

DRAM 因低延迟和低 bit cost 成为几乎所有计算系统的主存技术。现代 DRAM chips 存在 RowHammer 漏洞：反复访问一个或多个 aggressor rows 会在物理邻近 victim rows 中产生电磁/电路干扰，使 victim cells 无法正确保持数据，从而发生 bitflips。RowHammer bitflips 具有可重复性：若某次 hammer 导致某个 cell bitflip，再次执行相同行为时，该 cell 很大概率会再次 bitflip。

随着 DRAM storage density 提高，cell size 和 cell-to-cell spacing 减小，DRAM 对 RowHammer 更敏感。作者引用 Revisiting RowHammer 的结果：在 1580 个真实 DRAM chips 上，过去十年 RowHammer threshold 降低超过 10x；同样 row activations 导致的 bitflips 增加约 500x。近期研究还显示，state-of-the-art servers 上的 commodity workloads 可能已经以超过 RowHammer threshold 的速率激活某些 rows。

RowHammer 有可靠性和安全两类影响。非恶意程序也可能触发 bitflips，造成 system reliability/safety 问题。恶意程序则可以有目标地触发 bitflips，破坏 integrity、confidentiality、availability。RowHammer 打破了现代系统安全依赖的 memory isolation，因此影响非常广泛。RowHammer-like disturbance 还出现在一些 emerging NVM 技术中，因此对未来内存技术同样重要。

本文组织如下：Section 2 回顾 2020 前 RowHammer 研究；Section 3 介绍 2020 年两个关键工作 TRRespass 和 Revisiting RowHammer；Section 4 概述 exploiting、understanding/modeling、mitigating RowHammer 的近期进展；Section 5 提出未来方向。

### 硬件工程师视角

引言说明 RowHammer 的风险正在从“安全研究者构造攻击”变成“普通 workload 也可能接近物理失效边界”。这对服务器内存、GPU/HBM、accelerator-attached memory、CXL memory expander 都有意义。未来内存控制器不能只按性能调度，还要暴露 row activation monitoring、throttling、RFM/refresh policy、AER/RAS logging 等能力。

---

## 2. A Brief Overview of RowHammer Until 2020 / 2020 年前 RowHammer 简要回顾

### 原文位置
Page 2 / Section 2

### 中文翻译

RowHammer 在 2014 年首次被公开系统性分析。原始 ISCA 2014 工作测试了真实 commodity DDR3 DRAM modules，发现超过 80% 的测试模块容易受到 RowHammer 影响。该工作证明普通 user-level programs 可以在真实 CPU-based systems 上诱发 bitflips，并指出 RowHammer 是 DRAM technology scaling problem。由于 device/circuit-level 解决方案困难且昂贵，作者主张通过 system-memory cooperation 解决 RowHammer。

2014-2019 年间，大量工作构造 RowHammer attacks，覆盖 mobile、server 等多类系统，破坏 integrity 和 confidentiality。另一些工作从 device 和 circuit levels 建模或实验分析 RowHammer 原因。原始 RowHammer 论文提出七类解决方向，后续学术和工业界提出硬件、软件、memory-controller、DRAM-level 多种机制。

### 2.1 RowHammer Mitigations in Industry

RowHammer 公开后，系统厂商和 DRAM 厂商都尝试缓解。field-deployable 的一个主要办法是提高 refresh rate，例如 Apple security release 中提到的方式。但提高 refresh rate 开销大，性能和能耗都不理想。

memory controller 厂商引入 pTRR (pseudo Target Row Refresh) 一类机制，受 PARA 启发。但 MC 不知道 DRAM 内部物理相邻关系，因此 victim row refresh 可能不完整。

DRAM 厂商引入 TRR (Target Row Refresh)，并宣称新 DDR4 chips RowHammer-free。TRR 是一个 umbrella term，泛指刷新被认为频繁访问的 target rows 的机制。但厂商没有公开实现方式或安全保证。因此到 2019-2020 年左右，真实 DDR4 是否仍可能发生 RowHammer bitflips 并不清楚。

### 硬件工程师视角

这一节说明“安全 by obscurity”不适合硬件可靠性问题。如果防护机制不公开 threat model、计数能力、threshold、victim selection、blast radius、性能开销，就无法验证是否安全。硬件团队需要可审计机制和明确保证，而不能只依赖黑盒 TRR 声明。

---

## 3. Major Developments in 2020 / 2020 年关键进展

### 原文位置
Page 2-3 / Section 3, Figure 1

### 中文翻译

2020 年两个工作改变了 RowHammer 研究格局。

### 3.1 TRRespass

TRRespass 首次证明，被宣传为 RowHammer-free 的 TRR-protected DDR4 chips 实际仍然在 field 中 vulnerable。该工作部分 reverse engineer 了现代 DRAM chips 和 MC 中的 TRR/pTRR 机制，并提出 many-sided RowHammer attack。其核心思想是 hammer 多于两个 rows，以绕过 proprietary TRR mitigations，例如让 TRR aggressor tracking table 溢出。TRRespass 在 DDR4 和 LPDDR4(X) chips 上诱发 bitflips，证明工业界方案并不安全。

后续 U-TRR 工作进一步表明，可以利用 SoftMC 和 DRAM Bender 等 FPGA DRAM testing infrastructures，以及 retention errors 作为 side channels，几乎完整 reverse engineer 某些 DRAM chip 的 TRR 机制，并据此构造专门 hammering patterns 诱发大量 bitflips。

### 3.2 Revisiting RowHammer

Revisiting RowHammer 从 device/circuit level 角度测量 RowHammer scaling properties。它测试 1580 个 DRAM chips，覆盖至少两代和多种 DRAM 类型，证明较新 DRAM chips 显著更脆弱。有些芯片只需 4800 次 double-sided hammers 就出现首次 bitflip；RowHammer threshold 从 2014 年约 139K single-sided 降到 2020 年 4.8K double-sided。若趋势继续，已有方案要么无法保护未来更脆弱芯片，要么开销过高。

这些结果促使 JEDEC 重新组织 RowHammer task group，并推动 DDR5 中的 RFM (Refresh Management)。RFM 让 MC 以 bank granularity 计数 activations，当计数达到阈值时发 RFM command，给 DRAM 内部 TRR 机制额外时间刷新 victim rows。但由于 MC 只按 bank 粒度计数，即使没有 RowHammer attack，也可能频繁达到 threshold，触发不必要 RFM commands，造成性能开销。

### 硬件工程师视角

2020 年进展对硬件设计的启发是：RowHammer 防护必须针对最坏真实芯片和真实访问模式，而不是针对理想模型。bank-level activation count 太粗，row-level tracking 太贵，DRAM-internal information 不透明。未来机制必须在准确性、面积、带宽、可验证性之间做系统级折中。

---

## 4. Recent RowHammer Developments / 近期 RowHammer 发展

### 原文位置
Page 3-5 / Section 4

### 中文翻译

### 4.1 Exploiting RowHammer

2020 后出现多类新攻击。RAMBleed 证明 RowHammer bitflips 可作为 side channel 破坏 confidentiality，例如泄露 OpenSSH key。针对 neural networks 的工作证明，定向 RowHammer bitflips 能显著降低 inference accuracy，影响自动驾驶等安全关键系统；也有工作用 RowHammer side channel 恢复 neural network weights。

TRRespass 后续攻击包括 SMASH、Blacksmith 和 Half-Double。SMASH 在 JavaScript 中实现 synchronized many-sided hammering，绕过 TRR，并在 15 分钟内 compromise Firefox。Blacksmith 用 frequency-domain fuzzing 自动发现非均匀 access patterns，以不同 phase、frequency、amplitude hammer aggressor rows，在所有 40 个测试 DDR4 modules 上触发 bitflips。Half-Double 证明 hammer 远邻 row 和少量 hammer 近邻 row 结合，也可在某些 DDR4 chips 上导致 victim bitflips，揭示 RowHammer 影响可能跨越直接邻近 row。

### 4.2 Understanding RowHammer

近期研究从温度、aggressor row active time、cell physical location、wordline voltage 等方面理解 RowHammer。A Deeper Look into RowHammer 测试 248 个 DDR4 和 24 个 DDR3 chips，发现 bitflip 更可能在某个温度范围、aggressor row active 更久、特定物理区域中发生。RowHammer under Reduced Wordline Voltage 测试 272 个 DDR4 chips，发现降低 wordline voltage 可显著降低 bitflips 并提高 threshold，而不显著影响可靠运行。

这些研究说明 RowHammer 不是单变量问题。温度、电压、active time、data pattern、物理位置、访问模式和 memory controller policy 都会改变 vulnerability。

### 4.3 Mitigating RowHammer

Revisiting RowHammer 表明必须开发 fully-secure、low-overhead、scalable mitigations。Graphene 使用 Misra-Gries frequent item counting 追踪高频 rows，并刷新邻近 rows。它有效且性能开销低，但随着 threshold 降低，CAM metadata 面积会变大。

BlockHammer 使用 counting Bloom Filters 识别接近 threshold 的 rows，并 throttle 对这些 rows 的访问。它不需要 DRAM physical adjacency 等 proprietary information，可完全在 MC 中实现。BlockHammer 还提出 RowHammer Likelihood Index (RHLI)，用于识别和报告 RowHammer attacks。

SMD 采用不同路线：修改 DRAM interface，让 DRAM chip 可拒绝 ACT command，从而获得内部维护时间。RowHammer mitigation 被视为 DRAM maintenance operation，可基于 DRAM 内部 device-level information 实现。SMD-PRP 和 SMD-DRP/PRP+ 通过 fine-grained regions 在低开销下执行 in-DRAM mitigation。

RRS 和 AQUA 通过 relocation 隔离 aggressor rows。它们不需要知道 DRAM physical layout，也兼容 commodity DRAM，但 data relocation 需要经过 memory bus，增加数据搬移开销。HiRA 尝试将 refresh-based RowHammer mitigation 与访问/其他 refresh 并行，降低性能开销。Hydra 将 row activation counters 存在 DRAM 中，并用小 on-chip cache 缓存，降低 counter 硬件成本。

### 硬件工程师视角

不同 mitigation 的硬件代价完全不同。Graphene/BlockHammer 偏 MC metadata 和计数结构；SMD 偏接口与 DRAM 自治；RRS/AQUA 偏数据搬移和 address remapping；RFM/PRAC 偏标准化和 firmware/MC 协议。设计防护时必须明确目标：是防攻击、降 bitflip、限制 DoS、支持可证明安全，还是降低普通 workload overhead。单一机制很难同时最优。

---

## 5. Future Directions / 未来方向

### 原文位置
Page 5-6 / Section 5

### 中文翻译

### 5.1 Building a Fundamental and Comprehensive Understanding of RowHammer

作者认为，尽管已有详细 characterization，RowHammer 仍有大量未知。未来至少要理解几个关键属性：DRAM aging、environmental conditions（temperature、supply voltage）、memory access patterns。现有工作已表明温度、电压和访问模式会显著影响 vulnerability，但还需要更细理解这些因素与 RowHammer 的关系。

这很重要，因为所有已有和未来防护机制都依赖对 RowHammer vulnerability 的测量，例如 threshold。若不了解 aging、temperature、voltage、pattern 的单独和组合效应，就难以构建完整防护。作者认为 SoftMC、DRAM Bender 等 FPGA-based infrastructures 对这类研究非常关键。

作者还强调，需要在真实系统和真实应用上理解 RowHammer，包括 mobile/server CPUs、GPUs、accelerators、FPGAs、HBM 和 emerging NVM。研究不仅要构造攻击，也要理解 benign workloads 是否会触发 bitflips 或触发 mitigation 开销。

### 5.2 Designing Extremely Efficient Solutions to RowHammer

随着 RowHammer 恶化，必须设计低 performance/energy/area 开销且 provably-secure 的解决方案。未来 benign workload 的 row activation rate 可能接近甚至超过 threshold，因此系统可能在无攻击时也出现 bitflips 或频繁触发防护机制，造成性能下降。

作者主张 system-memory co-design。一个 holistic solution 应能同时防止 bitflips、检测 attacks，并避免 RowHammer attacks 和 mitigations 带来的性能与 DoS 问题。例如系统可 relocate/isolate data，或 throttle/relocate/isolate threads，使非恶意应用不受攻击或防护机制影响。

作者还认为，未来机制应利用 RowHammer vulnerability 的 variation。不同 cells、chips、manufacturers、types/generations、environmental conditions 和 data patterns 的 vulnerability 都不同。目前机制通常按最脆弱芯片配置，导致 common case 过度保守。未来方案应可配置或可编程，能静态/动态适配系统和 workload。

### 硬件工程师视角

未来方向对实际硬件路线很明确：需要 telemetry、programmability、adaptivity。MC/DRAM 需要暴露 activation counters、mitigation triggers、RFM events、temperature/voltage context、error logs。Firmware/OS 需要利用这些信号做 workload-aware policy。没有可观测性和可调参数，就无法同时做到安全和低开销。

---

## 6. Conclusion / 结论

### 原文位置
Page 6 / Section 6

### 中文翻译

作者简要回顾了 RowHammer vulnerability 的历史和当前研究状态，并提出未来研究方向。尽管已有大量研究，未来仍需做更多工作，因为 RowHammer 是一个基本的 DRAM technology scaling problem，并且在新 DRAM chips 中持续恶化，而这些芯片仍将广泛部署在几乎所有计算系统中。作者希望本文讨论能为社区找到从根本上理解和高效解决 RowHammer 的路径提供帮助。

### 面向硬件工作的学习提炼

这篇文章应作为 RowHammer 方向的路线图。对硬件工程师来说，它要求我们把 RowHammer 看成跨层问题：DRAM cell physics、array organization、MC scheduling、refresh/RFM/TRR、ECC、OS isolation、workload behavior、security threat model 都有关。真正可持续的解决方案必须跨 DRAM chip、MC、firmware、OS 协作，而不是只在某一层打补丁。

---

## References / 参考文献

### 原文位置
Page 6 onward / References

参考文献列表保留英文原文，不逐条翻译。建议优先回读原始 RowHammer ISCA 2014、TRRespass、Revisiting RowHammer、BlockHammer、SMD、DRAM Bender、RFM/PRAC/Jedec whitepapers、Half-Double、Blacksmith、HiRA、Hydra。
