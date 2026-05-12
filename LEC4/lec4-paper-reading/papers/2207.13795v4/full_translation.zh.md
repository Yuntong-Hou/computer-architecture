# Full Chinese Translation

说明：本文件已按“高完整度学习译文”标准重写。它基于本地 PDF 抽取文本和原文结构，尽量完整覆盖论文的问题定义、DRAM 背景、架构设计、处理器/控制器支持、评估方法、结果、讨论和结论；为便于学习，长段落被拆成更自然的中文段落，专业术语保留英文。参考文献列表不逐条翻译。请结合 PDF 原文核对图表和参数表。

## Title

原文标题：Sectored DRAM: A Practical Energy-Efficient and High-Performance Fine-Grained DRAM Architecture

中文标题：Sectored DRAM：实用、节能且高性能的细粒度 DRAM 架构

作者：Ataberk Olgun; F. Nisa Bostancı; Geraldo F. Oliveira; Yahya Can Tuğrul; Rahul Bera; A. Giray Yağlıkcı; Hasan Hassan; Oğuz Ergin; Onur Mutlu

原文位置：Page 1 / Title

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
传统 DRAM 系统以 cache block 粒度传输数据，并以较粗粒度激活 DRAM 内部结构。许多程序的 spatial locality 并不理想：一次 cache block 被取入 cache 后，其中只有部分 words 会被实际使用。结果是 DRAM 传输了大量无用数据，也激活了不必要的 cells，造成能耗浪费，并可能降低内存密集 workload 的性能。

Sectored DRAM 提出一种 practical fine-grained DRAM architecture。它通过 Variable Burst Length (VBL) 减少不必要的数据传输，通过 Sectored Activation (SA) 减少不必要的 DRAM activation energy，并通过处理器侧的 LSQ Lookahead 和 Sector Predictor 降低只取部分 words 所带来的 sector miss 风险。

论文在 41 个 workloads 上评估该设计。结果显示，在 memory-intensive workloads 上，Sectored DRAM 能显著降低 DRAM energy 并提升性能，同时 DRAM chip area overhead 约为 1.7%。与已有 fine-grained DRAM 方案相比，它在性能、能耗和面积之间取得更实用的折中。

### 硬件工程师视角
摘要强调的是常规内存访问中的“过度服务”问题：为了一个 word，系统搬了整个 cache block；为了少量数据，DRAM 激活了更大范围。对硬件工程师来说，这篇论文可以帮助你思考 memory granularity：接口粒度、内部激活粒度、cache 管理粒度和 workload locality 之间必须匹配，否则能耗和性能都会浪费。

---

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2 / Section 1

### 中文翻译
作者首先指出，现代处理器通常以 cache block 粒度从 DRAM 读取数据。一个 cache block 可能包含多个 words，但很多 workload 在 cache block 进入 cache 后只使用其中一部分 words。未被使用的 words 仍然消耗 DRAM bus bandwidth、I/O energy 和 cache capacity。这种现象在 spatial locality 较差的 workload 中尤其严重。

另一方面，DRAM 内部 activation 也很粗粒度。一次访问通常会激活整行或相当大范围的 cells，即使最终只需要 cache block 中几个 words。activation energy 是 DRAM energy 的重要组成部分，因此如果能只激活必要部分，就可能进一步节能。

已有 fine-grained DRAM 研究试图解决类似问题，但存在不足。有的方案只减少数据传输，不减少 activation energy；有的减少 activation 但牺牲 bandwidth；有的需要较大面积开销；有的缺少处理器侧机制来避免细粒度取数导致的 miss 增多。作者把问题拆成两个目标：Fine-grained DRAM data transfer 和 Fine-grained DRAM activation。

Sectored DRAM 试图同时满足这两个目标。它把一个 cache block 分成多个 sectors，每个 sector 通常对应一个 word 或若干 bytes。Variable Burst Length 让 DRAM 只传输请求的 sectors；Sectored Activation 让 DRAM 只激活包含这些 sectors 的内部 mats/部分结构。为了避免只取部分 sectors 后很快又需要同一 cache block 的其他 sectors，作者提出 LSQ Lookahead 和 Sector Predictor，提前判断哪些 sectors 应该一起取回。

作者的贡献包括：提出 VBL；提出 SA；设计处理器和 memory controller 支持，包括 sector bits、LSQ Lookahead 和 Sector Predictor；用 cycle-level simulation 和 power modeling 评估 41 个 workloads；并与 FPA、PRA、HalfDRAM 等 fine-grained DRAM architecture 比较。

### 硬件工程师视角
引言值得你提炼出一个重要工程判断：memory subsystem 不只是追求更大带宽，还要避免把带宽和能量花在无用数据上。AI、图计算、数据库、稀疏访问、pointer chasing 都可能有类似问题。未来设计 memory hierarchy 时，granularity control 会越来越重要。

---

## 2. DRAM Background / DRAM 背景

### 原文位置
Page 3 - Page 4 / Section 2

### 中文翻译
背景部分介绍 DRAM organization、data transfer burst 和 tFAW 等与 Sectored DRAM 相关的机制。

#### 2.1 DRAM Organization

原文位置：Page 3 / Section 2.1

DRAM 系统由 channels、ranks、chips、banks、subarrays、rows、columns 和 mats 构成。一个 DRAM chip 内部通常把数据分布在多个 mats 中。一次 cache block 访问会跨多个 chips 组成完整数据宽度，也会在每个 chip 内部访问相应 bytes。

Sectored DRAM 利用的关键事实是：cache block 的不同 words 在 DRAM chip 内部已经可以对应到不同位置或不同 mats。只要在 DRAM 内部和 controller 接口上增加选择能力，就可能只传输或只激活需要的 sectors。

#### 2.2 Cache Block Organization in DRAM

原文位置：Page 4 - Page 5 / Section 2.2 / Figure 2

Figure 2 解释 cache block 如何分布在 DRAM chips 和内部 mats 中。一个 64B cache block 在多个 x8 chips 上并行传输，每个 chip 提供其中一部分数据。DRAM 的 burst transfer 会在多个 cycles 中连续传输 cache block 的不同 words。

这给 VBL 提供了机会：如果 memory controller 知道只需要某些 words，就可以缩短 burst 或选择性传输，避免把完整 cache block 全部搬回。

#### 2.3 Data Transfer Bursts

原文位置：Page 4 / Section 2.3

DDR DRAM 通过 burst 传输数据。一次 READ/WRITE command 会触发固定长度 burst，传统设计默认传输完整 cache block 所需数据。固定 burst length 简化接口和控制，但在只需要部分 words 时浪费能量。

VBL 的思想是让 burst length 根据 sectors 动态变化，保留 DRAM 高带宽的同时减少无用传输。

#### 2.4 The tFAW Timing Parameter

原文位置：Page 4 / Section 2.4

tFAW 限制在一个 rolling window 内可发出的 ACTIVATE 数量，用于控制功耗和电流峰值。细粒度 activation 可能改变 activation power profile，因此 Sectored DRAM 必须考虑 tFAW 等 timing constraints，不能简单增加更多 activation。

### 硬件工程师视角
背景部分提醒你，DRAM 已经有很多内部并行和分段结构，但传统接口把它们隐藏起来。架构创新常常来自重新暴露这些隐藏结构的一小部分能力。问题是：暴露多少才够用，暴露太多又会不会破坏标准接口和验证复杂度。

---

## 3. Motivation / 动机

### 原文位置
Page 4 - Page 5 / Section 3 / Figure 3

### 中文翻译
作者用 workload behavior 和能耗 breakdown 说明为什么需要 Sectored DRAM。很多应用的 cache block utilization 不高，即取入 cache 的 block 中只有部分 words 被访问。传统 DRAM 为这些未使用 words 付出了 transfer energy 和 cache pollution。

Figure 3 量化了 DRAM access 和 activation energy 的浪费。即使只需要一个 word，传统 DRAM 仍然传输完整 cache block，并激活更大范围内部结构。只优化 transfer 不够，因为 activation energy 仍然存在；只优化 activation 也不够，因为 I/O burst 仍然搬运无用数据。论文因此把目标设为同时支持 fine-grained transfer 和 fine-grained activation。

作者还强调，细粒度访问不能以严重性能下降为代价。如果每次只取一个 word，后续访问同一 cache block 的其他 words 时可能产生 sector misses，导致更多 DRAM accesses。Sectored DRAM 必须预测或提前发现同一 cache block 内未来会被使用的 sectors。

### 硬件工程师视角
这一节的行业意义在于能效优化的精细化。过去很多系统通过预取和大粒度传输换性能，但能耗压力越来越大后，“传多一点以防万一”的策略不总是划算。尤其在移动、边缘、数据中心内存能耗受限场景，细粒度访问和预测会变得更重要。

---

## 4. Sectored DRAM / 架构设计

### 原文位置
Page 5 - Page 7 / Section 4

### 中文翻译
Sectored DRAM 包含两个核心 DRAM-side 机制：Sectored Activation 和 Variable Burst Length。两者分别减少 activation 和 transfer 的无用能耗。

#### 4.1 Sectored Activation (SA)

原文位置：Page 5 - Page 6 / Section 4.1

SA 把 DRAM row 内部划分为 sectors，使 memory controller 可以选择只激活需要的 sectors。作者利用 DRAM row 内已有 mat structure，在每个 sector 增加必要的控制元件，例如 sector transistors 和 sector latches。这样，ACTIVATE 时不必让整行所有相关 mats 都参与，而是根据 sector bits 启用目标部分。

SA 需要把 sector information 传递给 DRAM。论文讨论通过命令或地址位携带 sector bits，使 controller 能指定要激活哪些 sectors。由于只激活部分结构，SA 可以降低 array activation power。但它也会带来少量额外电路和控制开销。

#### 4.2 Variable Burst Length (VBL)

原文位置：Page 6 / Section 4.2

VBL 让 data transfer burst 的长度根据请求 sectors 数量变化。传统 DRAM 固定 burst length 传输完整 cache block，而 VBL 只传输被选中的 sectors。对于只需要一个 word 的访问，它可以显著减少 READ/WRITE I/O energy。

VBL 的设计目标是尽量复用 DRAM I/O 已有能力，而不是完全重做接口。它需要 memory controller、DRAM chip 和 cache hierarchy 都理解 sector-level valid bits，确保部分 cache block 的数据能被正确追踪。

#### 4.3 Exposing SA and VBL to the Memory Controller

原文位置：Page 6 - Page 7 / Section 4

memory controller 必须知道一次 request 需要哪些 sectors，并把这些信息编码到 DRAM command 中。controller 还要处理 partial cache line fill、sector misses、writebacks 和 coherence。也就是说，Sectored DRAM 不是单纯 DRAM chip 内部变化，还需要 processor-side metadata 和 request scheduling 配合。

### 硬件工程师视角
SA 和 VBL 是很典型的 cross-layer hardware design。DRAM chip 端加一点选择能力，controller 端加一点 command/metadata，cache 端加 valid bits，processor 端加预测。每层改动都不算特别大，但组合起来才能产生效果。读这一节可以训练你做 architecture cost accounting：面积、时序、命令编码、controller 状态、cache metadata 都要一起算。

---

## 5. Processor and Controller Support / 处理器和控制器支持

### 原文位置
Page 7 - Page 9 / Section 5

### 中文翻译
Sectored DRAM 需要处理器和 memory controller 提供 sector-level 支持，否则细粒度取数可能导致大量 sector misses。

#### 5.1 Tracking Valid Words in the Processor

原文位置：Page 7 / Section 5.1

cache 需要知道一个 cache block 中哪些 sectors 当前有效。传统 cache line valid bit 只表示整条 line 是否有效；Sectored DRAM 需要 per-sector valid bits。load/store 命中某个 cache line 时，还要检查目标 sector 是否有效。如果 line 存在但 sector 无效，就发生 sector miss，需要从 DRAM 取回缺失 sector。

#### 5.2 LSQ Lookahead

原文位置：Page 7 - Page 8 / Section 5.2

LSQ Lookahead 利用 load/store queue 中已经可见的 younger memory instructions。若多个即将执行的 memory operations 访问同一 cache block 的不同 sectors，处理器可以在第一次 DRAM request 时一起请求这些 sectors。这样可以避免后续 sector misses。

LSQ Lookahead 的优点是基于真实 in-flight instructions，不完全依赖历史预测；缺点是视野受限，只能看到 reorder window/LSQ 中的未来访问。

#### 5.3 Sector Predictor

原文位置：Page 8 / Section 5.3

Sector Predictor 根据历史访问模式预测一个 cache block 中哪些 sectors 未来会被使用。它可以补足 LSQ Lookahead 的视野限制。论文评估不同 predictor 配置，例如 SP512 等，分析预测准确性、miss reduction 和硬件开销。

预测器如果过于保守，会多取 sectors，降低节能；如果过于激进地少取，会增加 sector misses，影响性能。Sectored DRAM 的系统表现很大程度取决于这个 trade-off。

#### 5.4 Memory Controller Operation

原文位置：Page 8 - Page 9 / Section 5.4

memory controller 接收 cache miss request 后，根据 LSQ Lookahead 和 Sector Predictor 得到 sector mask，再生成 SA/VBL command。它还需要处理 partial fills、writebacks 和可能的 sector merging。对于 writes，controller 要确保只写回有效/dirty sectors，避免破坏未持有的数据。

### 硬件工程师视角
这节最值得学习的是 predictor 与硬件机制的闭环：DRAM 端提供细粒度能力，但是否节能取决于处理器是否能猜中未来需要哪些 words。硬件工程中很多 feature 都有类似结构：底层提供选择性，上层负责判断选择什么。判断逻辑的准确性常常比底层 primitive 本身更影响端到端收益。

---

## 6. Evaluation Methodology / 实验方法

### 原文位置
Page 9 - Page 10 / Section 6 / Table 3

### 中文翻译
作者使用 Ramulator 进行 memory system simulation，使用 DRAMPower 和 Rambus Power Model 估计 DRAM power/energy，并结合 processor/system energy 模型评估端到端影响。

workloads 包括 41 个 SPEC2006、SPEC2017 和 DAMOV workloads。作者按 LLC MPKI 将 workload 分组，区分 memory intensity。这个分类很重要，因为 Sectored DRAM 主要针对 memory-intensive 且 spatial locality 较差的程序；低 MPKI workload 可能几乎不受益。

实验比较多种配置：baseline conventional DRAM、Basic Sectored DRAM、加入 LSQ Lookahead 的配置、加入 Sector Predictor 的配置，以及 LA128-SP512 等组合。还与已有 fine-grained DRAM architecture 如 FPA、PRA 和 HalfDRAM 比较。

评估指标包括 DRAM command power、LLC MPKI、single-core performance、multi-core weighted speedup、memory latency、DRAM energy、system energy 和 DRAM chip area overhead。

### 硬件工程师视角
评估方法值得关注，因为 Sectored DRAM 的收益对 workload locality 非常敏感。硬件工程中如果只看平均值，很容易掩盖某些 workload 变差。读实验时要按 MPKI、sector miss、predictor behavior 和 energy breakdown 分层看。

---

## 7. Evaluation Results / 实验结果

### 原文位置
Page 10 - Page 14 / Section 7 / Figures 7-12

### 中文翻译
#### 7.1 Impact on DRAM Power

原文位置：Page 10 / Section 7.1 / Figure 7

Figure 7 分析 DRAM command power。读/写一个 sector 相比读/写全部 sectors，DRAM READ/WRITE power 分别降低 70.0% 和 70.6%。这说明 VBL 对 I/O transfer energy 有很直接的效果。

只激活一个 sector 可使 DRAM array activation power 降低 66.5%，但整体 ACT power 只降低 12.7%。原因是 ACT power 不只来自 array activation，还包括外围电路和固定开销。SA 自身增加的 activation power overhead 很小，约 0.26%。

#### 7.2 Impact on Cache Misses

原文位置：Page 10 - Page 11 / Section 7.2 / Figure 8

Basic Sectored DRAM 只取请求 sector，会显著增加 LLC MPKI，平均提高 3.1x。这是细粒度访问的典型代价：第一次少取了数据，后续如果需要同一 cache block 的其他 sectors，就会产生额外 miss。

LSQ Lookahead 和 Sector Predictor 能缓解这个问题。LA128-SP512 相比 Basic Sectored DRAM 将 LLC misses 降低 52%。这说明只改变 DRAM 端不够，处理器侧预测机制是性能可接受的关键。

#### 7.3 Performance

原文位置：Page 11 - Page 12 / Section 7.3 / Figures 9-10

性能结果显示，Sectored DRAM 对高 MPKI workload 更有帮助。对于 16-core high-MPKI workloads，平均 parallel speedup 比 baseline 高 26%，平均 memory latency 降低 25%。原因是减少无用传输和部分 activation 后，memory system 能更快服务有用请求，降低排队和访问延迟。

但并非所有 workload 受益。stride streaming 等模式可能由于频繁 sector miss 导致性能下降。论文因此强调需要动态机制，在不适合时关闭 Sectored DRAM。

#### 7.4 Comparison with Prior Fine-Grained DRAM Architectures

原文位置：Page 12 - Page 13 / Section 7.4

作者与 FPA、PRA、HalfDRAM 等方案比较。Sectored DRAM 的优势在于同时支持 fine-grained transfer 和 fine-grained activation，并尽量保持较高 bandwidth 和较低 area overhead。相对 HalfDRAM，Sectored DRAM 获得 89% 的 performance benefits、12% less DRAM energy 和 34% less chip area。

#### 7.5 Energy and Area

原文位置：Page 13 - Page 14 / Sections 7.4-7.5 / Figures 11-12

DRAM energy 最高降低 33%，平均降低 20%；system energy 最高降低 23%，平均降低 14%。这说明 DRAM-side energy reduction 能够传导到系统层，但系统层收益小于 DRAM 层收益，因为 CPU、cache 和其他组件仍然消耗能量。

DRAM chip area overhead 为 1.72%。这来自 sector transistors、sector latches 和相关控制逻辑。作者认为该 overhead 相对低，体现了 Sectored DRAM 的 practical 属性。

### 硬件工程师视角
实验结果的核心不是“平均提升 26%”这一个数字，而是完整 trade-off：VBL 大幅降低 I/O power，SA 只部分降低 ACT power，Basic 会显著增加 MPKI，predictor 把 miss 拉回来，最终高 MPKI workload 性能和能耗受益。你可以把它当成一个硬件 feature 评估模板：先看 primitive energy，再看 cache/miss 副作用，再看 full-system energy。

---

## 8. Discussion / 讨论

### 原文位置
Page 14 - Page 16 / Section 8

### 中文翻译
作者讨论 Sectored DRAM 的边界和扩展。

#### 8.1 Sectored DRAM with More Memory Channels

原文位置：Page 14 / Section 8.1

更多 memory channels 会改变 bandwidth pressure 和 energy balance。Sectored DRAM 在带宽受限时更有性能收益；如果系统 bandwidth 很充裕，性能提升可能下降，但 energy reduction 仍可能有价值。

#### 8.2 Non-Memory-Intensive Workloads

原文位置：Page 14 / Section 8.2

低/中 MPKI workloads 对 memory system 不敏感，Sectored DRAM 可能收益有限，甚至由于 sector miss 带来损失。作者提出动态开关机制，根据 workload behavior 决定是否启用 Sectored DRAM。

#### 8.3 Hardware Prefetchers

原文位置：Page 14 - Page 15 / Section 8.3

prefetching 与 Sectored DRAM 关系复杂。prefetcher 可能提前取入未来 sectors，减少 sector miss；也可能增加无用数据传输，削弱节能。作者讨论将 sector bits 与简单 prefetcher 结合的可能性。

#### 8.4 Smaller Sectors and Alternative Granularities

原文位置：Page 15 / Section 8.4

sector 粒度越小，理论上越能减少无用数据，但 metadata、prediction、command encoding 和 sector miss 风险都会增加。粒度选择必须在 energy saving、performance risk 和 hardware overhead 之间折中。

#### 8.5 DRAM Error Correcting Codes (ECC)

原文位置：Page 15 / Section 8.5

ECC 是实际系统必须考虑的问题。传统 ECC 通常围绕完整 cache line 或固定数据宽度设计；sector-level transfer 和 activation 可能需要调整 ECC granularity、校验位获取方式和 partial write 逻辑。作者把 ECC 作为重要讨论点，而不是完整解决。

#### 8.6 Sector Cache Benefits

原文位置：Page 15 - Page 16 / Section 8.6

sector-level validity 类似一种更细粒度 cache 管理方式，可能减少 cache pollution，也可能提升有效 cache capacity。但实际收益依赖 workload locality 和 predictor 行为。

### 硬件工程师视角
讨论部分非常适合你把论文和行业现实连接起来。DDR/LPDDR/HBM 标准、ECC、prefetcher、multi-channel、server workload mix 都会影响 feature 是否可部署。论文方案如果进入产品，不可能只改 DRAM chip；还要改 controller、cache metadata、RAS/ECC 和性能管理策略。

---

## 9. Conclusion / 结论

### 原文位置
Page 16 / Conclusion

### 中文翻译
论文总结说，传统 DRAM 系统以固定 cache block 粒度传输和较粗 activation 粒度服务访问，导致许多 spatial locality 较差的 workload 浪费能量和带宽。Sectored DRAM 通过 Variable Burst Length 和 Sectored Activation 同时减少不必要的数据传输和不必要的 cell activation，并通过 LSQ Lookahead 和 Sector Predictor 降低 sector miss 对性能的伤害。

评估表明，Sectored DRAM 在 memory-intensive workloads 上能降低 DRAM energy、降低 system energy 并提升性能，且 DRAM chip area overhead 较低。论文的核心结论是：细粒度 DRAM 必须同时考虑 transfer、activation 和 processor-side prediction，才能成为实用方案。

### 最终学习提炼
对硬件工程师而言，Sectored DRAM 的学习价值主要在：

- 理解 cache block 粒度和实际 word utilization 之间的错配。
- 区分 fine-grained transfer 与 fine-grained activation，两者缺一不可。
- 学会分析 partial cache line 带来的 sector miss 和 metadata 成本。
- 关注 predictor、prefetcher、ECC、multi-channel 对内存架构 feature 的影响。
- 用 energy breakdown 判断优化是否真正传导到 system energy。

在行业现状中，这篇论文与节能内存、near-data processing、HBM/DDR interface evolution 和 workload-aware memory hierarchy 都有关。它不直接做 PIM compute，但提供了另一条同样重要的路线：让普通 memory access 更接近实际需求粒度。

---

## References / 参考文献

### 原文位置
References

### 处理说明
参考文献保留英文原文，不逐条翻译。建议重点追踪 fine-grained DRAM、HalfDRAM、FPA/PRA、DRAMPower、Ramulator、spatial locality 和 sector cache 相关引用。
