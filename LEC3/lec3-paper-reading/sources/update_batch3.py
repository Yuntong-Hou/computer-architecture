from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def write(rel: str, text: str) -> None:
    path = ROOT / rel
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text.strip() + "\n", encoding="utf-8")


COMMON_NOTE = "已基于 PDF 提取文本完成深度中文阅读笔记；`full_translation.zh.md` 为版权友好的逐节中文详译/译述，不是逐字全文翻译。"


DATA = {
    "2505.00458v2": {
        "title": "Memory-Centric Computing: Solving Computing's Memory Problem",
        "zh": "以内存为中心的计算：解决计算系统的内存问题",
        "authors": "Onur Mutlu, Ataberk Olgun, İsmail Emir Yüksel",
        "year": "2025",
        "venue": "arXiv:2505.00458v2",
        "doi": "未找到",
        "url": "https://arxiv.org/abs/2505.00458",
        "dataset": "综述/路线图；引用 RowHammer、RowPress、VRD、SMD、Tesseract、PAPI、CENT、PUD 等研究结果",
        "topic": "Memory-centric computing / PIM / self-managing memory",
        "keywords": "memory-centric computing, processing-in-memory, self-managing DRAM, RowHammer, RowPress, VRD, PNM, PUM",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇短文从 memory scaling 和 system/application scaling 两条线论证 processor-centric paradigm 已经无法高效处理数据密集型应用，并主张通过 self-managing memory 与 processing-in-memory 逐步走向 memory-centric computing。

## 2. 研究背景
作者指出现代计算系统的大量能耗、性能瓶颈、可靠性问题、成本和芯片面积都来自 memory system。机器学习、基因组分析、图计算和数据分析等应用越来越 data-intensive，使 data movement 成为核心代价。传统系统把 memory 当作被动存储，只由 CPU/GPU/FPGA 发起访问和维护操作，这导致 cache、prefetch、out-of-order、multithreading 等复杂结构不断堆叠，却仍难以解决 memory wall。

## 3. 核心问题
- DRAM scaling 如何引发 RowHammer、RowPress、VRD、retention 等可靠性/安全问题。
- 现有 processor-centric memory maintenance 为什么难以低开销处理这些问题。
- 数据密集型应用为什么无法随处理器堆叠而高效扩展。
- PNM 和 PUM 分别如何减少 data movement 并释放 memory 内部并行性。
- memory-centric computing 的现实采用路径是什么。

## 4. 核心贡献
- 把 memory problem 分解为 device/circuit 层的 memory technology scaling 和 system/application 层的 performance/energy scaling。
- 用 RowHammer、RowPress、VRD 说明 DRAM scaling 的可靠性问题正在恶化。
- 用 SMD 说明 memory 可以更自主地执行 refresh、RowHammer mitigation、scrubbing 等维护操作。
- 用 Tesseract、PAPI、CENT 说明 PNM 对图计算和 LLM inference 的潜力。
- 用 RowClone、Ambit、SIMDRAM、COTS DRAM 多行激活实验说明 PUM 可以直接利用 memory array 的物理特性。
- 提出采用路径：先通过小接口变化和实际硬件原型逐步引入 MCC，而不是一次性替换整个体系。

## 5. 方法概述
本文不是实验型论文，而是立场/路线图式文章。作者综合近十余年 memory systems 研究，先指出 processor-centric paradigm 的局限，再分别讨论 self-managing DRAM、processing near memory、processing using memory 和 adoption framework。

## 6. 实验设计
本文本身不做新实验。它引用既有结果作为论据：RowPress 可将诱发 bitflip 所需 activation 数降低 1-2 个数量级；VRD 中同一 row vulnerability 可变化 3.5x，最坏情况需要 94,467 次测量；Tesseract 对 graph analytics 可提升 13.8x 性能并降低超过 8x 能耗；CENT 对 LLM inference 可提升 2.3x throughput、2.4x cost、5.2x tokens per dollar；COTS DRAM 中 NOT/AND/NAND/OR/NOR/Multi-RowCopy 成功率分别在高水平。

## 7. 主要结果
- RowHammer/RowPress/VRD 说明 memory scaling 问题已变成安全和可靠性瓶颈；见 Page 2, Figure 1-2。
- SMD 通过让 DRAM 在维护区域拒绝请求、其他区域继续服务，降低维护操作干扰；见 Page 3, Figure 3。
- PNM 例子 Tesseract、PAPI、CENT 说明将计算放近 memory 可以随容量/带宽扩展；见 Page 4-5, Figure 4-6。
- PUM 例子说明未修改 COTS DRAM 也可通过特殊激活执行 bulk bitwise operations 和 Multi-RowCopy；见 Page 5, Figure 7。

## 8. 关键结论
作者的核心结论是：只继续强化 processor-centric design 会带来越来越高的性能、能耗、面积和复杂度成本；memory 必须从被动存储变成能自主管理、能计算、能与系统共同优化的主动组件。

## 9. 局限性
本文是愿景和综合性论证，不是新机制的完整设计。它引用的多个 PIM/PUM/SMD 方案处于不同成熟度，软件生态、标准接口、可编程性、成本和安全隔离仍是重大挑战。

## 10. 适合我重点关注的内容
重点读 Page 1 的 problem framing，Page 2 的 RowHammer/RowPress/VRD，Page 3 的 SMD 接口，Page 4-5 的 PNM/PUM examples，以及 Page 6 的 adoption path。

## 11. 和其他文献的关系
这篇文章像 LEC3 的总纲：它把前面 RowHammer/PRAC/SMD 类工作和后面的 PIM、genome acceleration、memory reliability 工作串到 memory-centric computing 的大方向中。""",
        "key": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | 现代计算的核心瓶颈是 memory system | Page 1, Section 1 | memory 负责大量能耗、性能瓶颈、可靠性问题、成本和面积 | 高 | 这是全文的总论点 |
| 2 | processor-centric paradigm 把 memory 当作被动组件 | Page 1, Section 1 | 计算只能在 processor，memory 只响应请求 | 高 | 后续 MCC 的反面定义 |
| 3 | DRAM scaling 导致 RowHammer/RowPress/VRD 等问题恶化 | Page 2, Section 2; Figure 1-2 | RowPress、VRD 数值作为例子 | 高 | memory 需要自主管理可靠性 |
| 4 | PRAC 是向 memory-centric 方向的一小步但还不够 | Page 3, Section 2 | PRAC 把 activation counters 放入 DRAM，但仍依赖 MC | 中 | 和 PRAC/Chronus 论文直接连接 |
| 5 | SMD 通过 DRAM negative acknowledgment 支持自主维护 | Page 3, Figure 3 | SMD chip 拒绝维护区域请求，允许其他区域访问 | 高 | 这是 memory maintenance 的关键接口变化 |
| 6 | PNM 能把容量/带宽/计算能力按比例扩展 | Page 3-4, Section 3.1 | 3D-stacked memory logic layer、UPMEM、Tesseract | 高 | 解决 system/application scaling |
| 7 | Tesseract 代表 graph analytics PNM 路线 | Page 4, Figure 4 | 引用 13.8x 性能、>8x 能耗改进 | 中 | 老牌 PIM 案例，应和 Tesseract 论文一起读 |
| 8 | PAPI/CENT 说明 LLM inference 也受益于 PNM | Page 4-5, Figure 5-6 | PAPI/CENT 用 PIM units 处理 FC/attention/KV-cache 等 | 高 | 把 PIM 连接到最新 AI workload |
| 9 | PUM 利用 memory array 的模拟/电路行为执行计算 | Page 5, Section 3.2 | RowClone、Ambit、SIMDRAM、COTS DRAM 多行激活 | 高 | 这是比 PNM 更激进的路线 |
| 10 | 采用挑战主要是软件、接口和生态 | Page 6, Section 4 | 需要 programming frameworks, compilers, runtime, prototypes | 高 | 技术可行之外还要可编程和可部署 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖全文主要论证和图表。为遵守版权边界，不提供逐字长篇翻译；关键术语保留英文。

## Title
原文标题：Memory-Centric Computing: Solving Computing's Memory Problem

中文标题：以内存为中心的计算：解决计算系统的内存问题

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
作者认为 computing 正面临巨大的 memory problem。memory system 是现代系统能耗、性能瓶颈、可靠性问题、成本和硬件面积的重要来源，而且数据密集型应用会继续放大这一问题。论文讨论两类挑战：memory technology/capacity scaling，以及 system/application performance/energy scaling。作者主张 processor-centric paradigm 把 memory 视为不能计算、不能自主管理的被动组件，因此造成根本限制；转向 memory-centric computing 后，memory 可通过自主维护解决 scaling 可靠性问题，也可通过 processing-in-memory 大幅降低数据移动。

## 1. Computing's Memory Problem / 计算的内存问题

### 原文位置
Page 1

### 中文翻译
作者先定义 processor-centric computing：memory 只服务 processor 的 load/store 和 refresh 等维护请求，自己不能操纵数据，也不能决定如何维护自身。这个范式带来三类浪费：大量数据在 memory hierarchy 中移动；处理器为了掩盖 memory latency 堆叠 cache、prefetch、乱序和多线程结构；memory 内部巨大的 bit-level 和 array-level parallelism 大多闲置。

随着 ML、genome analysis、graph processing、data analytics 等应用增长，memory bottleneck 更严重。作者认为问题的根源不是某个单点优化不足，而是 memory 被排除在计算和自治决策之外。

## 2. Memory Scaling / 内存缩放

### 原文位置
Page 2 - Page 3

### 中文翻译
DRAM scaling 让 cell 更小、电荷更少、噪声更大，因而 retention、RowHammer、RowPress、VRD 等问题变得更严重。RowHammer 已被证明可由用户态程序触发并造成安全攻击；RowPress 又说明 row 保持 open 的时间也会显著放大读扰动；VRD 进一步指出同一 row 的 vulnerability 会动态变化，使安全阈值难以确定。

工业界通过 PARA、TRR、RFM、PRAC 等机制处理 RowHammer，但这些方案越来越复杂。作者认为 PRAC 虽然把计数器放入 DRAM，是朝 memory-centric co-design 的一步，但仍不够 memory-centric，因为 DRAM 还不能完全自主完成维护和优化操作。

Self-Managing DRAM（SMD）展示了一种更进一步的接口：DRAM 在执行维护的 region 上返回 negative acknowledgment，同时其他 region 可继续服务请求。这样 refresh、RowHammer mitigation、scrubbing 等可由 DRAM 内部机制自主执行，并与正常访问重叠。

## 3. System and Application Scaling / 系统和应用缩放

### 原文位置
Page 3 - Page 5

### 中文翻译
系统层的问题是计算能力和 memory capacity/bandwidth 不能高效共同扩展。许多 data-intensive workload 算术强度低，cache 作用有限。继续增加 processor 会增加成本和能耗，却仍受限于 memory bus 和 data movement。

Processing in memory（PIM）通过把计算能力放入 memory chips 或 memory structures 来减少数据移动。作者区分 processing near memory（PNM）和 processing using memory（PUM）。PNM 在 memory 附近增加传统逻辑，适合更丰富的功能；PUM 直接利用 memory array 的电路特性执行 bulk operations，能释放更底层的并行性。

PNM 例子包括 UPMEM、3D-stacked memory logic layer、Tesseract、PAPI 和 CENT。Tesseract 将 graph analytics 分布到 3D-stacked memory+logic chips 中；PAPI 和 CENT 则展示 LLM inference 中 FC/attention/KV-cache 等 memory-bound kernel 如何分配到 PIM units。

PUM 例子包括 RowClone、Ambit、SIMDRAM，以及在未修改 COTS DRAM 中通过违反标准 timing 实现多行激活。作者引用实验结果说明 COTS DRAM 可执行 NOT、NAND、NOR、AND、OR 和 Multi-RowCopy 等操作，成功率高，说明 DRAM 本身蕴含计算能力。

## 4. Enabling Adoption / 推动采用

### 原文位置
Page 6

### 中文翻译
作者承认新硬件难以采用，尤其当它要求软件改变时。MCC 的最大挑战是软件、接口和系统组件之间的契约。需要 programming frameworks、compilers、system software、runtime systems、benchmarks 和 real prototypes。

作者建议采取渐进路线：先引入简单接口变化和低风险操作，例如 SMD 的 negative acknowledgment、RowClone-like 操作，然后在这些能力上构建新的软件机制。只要出现真实 SMD chips 或 RowClone-capable chips，生态就可以逐步形成。

## 5. Overall Message / 总体结论

### 原文位置
Page 6 最后段

### 中文翻译
作者最后用强烈的语气指出，如果系统继续在 processor-centric paradigm 上反复投入，却期待根本不同的结果，就会持续付出性能、能耗、面积和复杂度代价。好消息是，PRAC、UPMEM、DRAM PIM prototypes 和先进封装技术已经让 memory-centric future 更接近现实。真正的问题变成：体系结构、标准、软件和产业界是否愿意推动这一转变。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | RowHammer vs RowPress | RowPress 用更长 open time 显著降低 ACmin | 说明 DRAM scaling 问题不只 activation count | 和 RowPress 论文联读 |
| Figure 2 | Page 2 | VRD 阈值变化 | 同一 row 的 read disturbance threshold 会变化 | 支撑 self-managing/dynamic mitigation 需求 | 和 VRD 论文联读 |
| Figure 3 | Page 3 | SMD 概览 | DRAM 能对维护区域返回 nack 并自主维护 | memory-centric maintenance 的关键接口 | 重点看 MC/DRAM 分工 |
| Figure 4 | Page 4 | Tesseract | 3D-stacked memory logic layer 执行 graph analytics | PNM 代表案例 | 与 Tesseract 论文联读 |
| Figure 5 | Page 4 | PAPI LLM inference | 不同 PIM units 处理 FC 和 attention/KV-cache | 连接 PIM 与 LLM | 看 kernel-to-PIM mapping |
| Figure 6 | Page 5 | CENT | CXL + GDDR6-PIM 协同 LLM inference | 显示可扩展 PNM 系统 | 关注 disaggregated PIM |
| Figure 7 | Page 5 | COTS DRAM PUM 成功率 | 未修改 DRAM 可执行多种 bulk operations | 支撑 PUM 可行性 | 重点看成功率与鲁棒性 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| 未发现核心表格 | 全文 | 本文以概念图和引用结果为主 | 无独立实验表 | 不是实验论文 | 重点读图和引用案例 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| 无核心公式 | 全文 | 路线图/综述文章 | 不适用 | 重点是系统设计思想 | 否 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Memory-Centric Computing (MCC) | 以内存为中心的计算 | Page 1 | 让 memory 能自主管理和/或执行计算的范式 | 是 |
| Processor-Centric Paradigm | 以处理器为中心的范式 | Page 1 | memory 被动响应 processor 请求 | 是 |
| Self-Managing DRAM (SMD) | 自管理 DRAM | Page 3 | DRAM 自主执行维护操作的接口/架构 | 是 |
| Processing in Memory (PIM) | 存内处理 | Page 3 | 将计算放入/靠近 memory | 是 |
| Processing Near Memory (PNM) | 近内存处理 | Page 3-4 | 在 memory 附近增加逻辑 | 是 |
| Processing Using Memory (PUM) | 利用内存计算 | Page 5 | 利用 memory array 电路属性直接计算 | 是 |
| RowHammer | 行锤击 | Page 2 | 反复激活 row 导致相邻 row bitflip | 是 |
| RowPress | 行压迫 | Page 2 | 长时间打开 row 诱发/放大 bitflip | 是 |
| Variable Read Disturbance (VRD) | 可变读扰动 | Page 2 | read disturbance threshold 随时间变化 | 是 |
| CXL | Compute Express Link | Page 5 | 可用于连接/解耦 PNM devices 的接口 | 中 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- MCC 采用难，主要挑战在 software、interfaces、frameworks 和 prototypes；位置：Page 6, Section 4。
- 需要渐进式采用路径，而不是一夜之间切换范式；位置：Page 6。

## 2. 论文中隐含的局限
- 本文是愿景/综述，未提出新硬件并独立评估。
- 引用的 PIM/PUM/SMD 案例成熟度不一，不能简单等同于可立即商用。

## 3. 实验设计可能存在的问题
- 没有统一实验平台比较 SMD、PNM、PUM 的成本收益。
- 引用结果来自不同论文、工艺、workload 和模拟/实测环境。

## 4. 方法可能不适用的场景
- 计算密度高、数据复用强、cache 友好的 workload 可能不需要 PIM。
- 需要严格一致性、安全隔离或复杂控制流的 workload 迁移到 memory 附近会更难。

## 5. 我阅读时应该追问的问题
- MCC 的最小可部署接口是什么？
- SMD、PRAC、Chronus 之间如何形成标准化演进？
- PIM 编程模型如何避免把复杂度转移给程序员？
- PUM 的可靠性、测试、错误恢复和安全边界如何定义？

## 6. 后续可以继续阅读的方向
- Modern Primer on PIM：系统读 PIM 分类。
- SMD/Chronus/PRAC：读 memory self-management。
- Tesseract、PAPI、CENT、UPMEM 相关论文：读 PNM 应用案例。""",
    },
    "AcceleratingGenomeAnalysis_ieeemicro20": {
        "title": "Accelerating Genome Analysis: A Primer on an Ongoing Journey",
        "zh": "加速基因组分析：一段持续旅程的入门综述",
        "authors": "Mohammed Alser, Zülal Bingöl, Damla Senol Cali, Jeremie Kim, Saugata Ghose, Can Alkan, Onur Mutlu",
        "year": "2020",
        "venue": "IEEE Micro, vol. 40, no. 5",
        "doi": "10.1109/MM.2020.3013728",
        "url": "https://doi.org/10.1109/MM.2020.3013728",
        "dataset": "综述文章；覆盖 read mapping pipeline、pre-alignment filtering、sequence alignment 加速器和相关工具",
        "topic": "Genome analysis acceleration / read mapping",
        "keywords": "read mapping, approximate string matching, indexing, pre-alignment filtering, sequence alignment, GenASM, PIM",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
这篇 IEEE Micro 综述用 read mapping 作为主线，解释 genome analysis 为什么受 approximate string matching 和 data movement 限制，并总结算法、硬件和 PIM 加速 read mapper 的主要方向与采用挑战。

## 2. 研究背景
测序机器能快速产生大量 reads，但计算系统将这些 reads 映射到 reference genome 的速度跟不上。read mapping 包含 indexing、pre-alignment filtering 和 sequence alignment，其中 ASM/DP-based alignment 通常占据大量时间。短读有低错误率但定位困难，长读更唯一但错误率高，二者都需要高效 approximate matching。

## 3. 核心问题
- read mapping 的三个阶段分别有什么瓶颈。
- 为什么 ASM/DP alignment 会成为主要计算热点。
- indexing、filtering、alignment 各有哪些加速方向。
- 为什么单点加速不足以让整个 genome analysis pipeline 跟上测序速度。
- 硬件加速 read mapper 的实际采用障碍是什么。

## 4. 核心贡献
- 用通俗结构解释 read mapping 的 indexing、pre-alignment filtering、sequence alignment 三阶段。
- 总结 q-gram、pigeonhole、base counting、sparse DP 等 filtering 方法。
- 总结 CPU/GPU/FPGA/ASIC/PIM 上的 alignment 加速方式。
- 强调 data movement 是 genome analysis 加速的关键问题。
- 讨论 GenASM 作为 bitvector-based ASM 框架如何跨多个阶段加速。
- 提出四个采用挑战：端到端加速、减少数据移动、灵活硬件、硬件友好数据格式。

## 5. 方法概述
本文是 primer/survey。它不是提出一个新系统，而是组织已有工作，解释 read mapping pipeline 中每一步的计算模式、算法选择和硬件适配方式，并指出未来设计 read mappers 的原则。

## 6. 实验设计
本文没有独立新实验。它引用现有工具和论文结果，例如 Illumina NovaSeq 6000 的测序吞吐、CPU 分析时间、GateKeeper/Shouji/SneakySnake/GRIM-Filter/GenASM/Darwin/DRAGEN 等加速器或工具的结果。

## 7. 主要结果
- read mapping 可占 genome analysis 大部分时间，单个 human genome 分析中 mapping 可消耗 23/32 CPU hours；见 Page 2。
- pre-alignment filtering 通过快速排除 dissimilar pairs 降低昂贵 alignment 次数；见 Page 3-6。
- GenASM 可对 short/long read alignment 达到 111x/116x software speedup，并降低 33x/37x power；见 Page 9。
- adoption challenges 包括端到端 pipeline、data movement、参数灵活性和 FASTQ/FASTA 格式低效；见 Page 8-9。

## 8. 关键结论
genome analysis acceleration 不能只加速一个 kernel；未来 read mapper 需要 algorithm-hardware co-design、减少跨层 data movement、支持不同 sequencing technologies，并采用更硬件友好的数据表示。

## 9. 局限性
作为综述，本文没有统一复现实验；不同引用结果来自不同平台和假设。它对后续 LRS、pangenome、graph genome 和 cloud privacy/security 的新趋势覆盖有限。

## 10. 适合我重点关注的内容
先读 Figure 1 理解 pipeline，再读 pre-alignment filtering 和 sequence alignment 两节，最后读 Page 8-9 的 adoption challenges。

## 11. 和其他文献的关系
这篇是 GenASM、NERO、PIM genome acceleration 等工作的背景入口；与 GenASM 深度论文直接相连。""",
        "key": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | read mapping 是 genome analysis pipeline 的主要瓶颈 | Page 1-2 | sequencing 速度增长快于计算分析能力 | 高 | 解释为什么需要专用加速 |
| 2 | read mapping 包含 indexing、pre-alignment filtering、sequence alignment | Page 3, Figure 1 | 图示三阶段及对应加速方向 | 高 | 全文组织框架 |
| 3 | ASM/DP alignment 准确但复杂度高 | Page 2-3 | DP 通常为 O(m²) 或 O(mn) | 高 | alignment 加速的算法根源 |
| 4 | data movement 是第一类核心挑战 | Page 2, Challenge 1; Page 8-9 | CPU-memory、accelerator、sequencer-computer 之间移动代价高 | 高 | 与 memory-centric computing 主题一致 |
| 5 | pre-alignment filtering 可大幅减少进入 alignment 的候选 | Page 4-6 | pigeonhole、base counting、q-gram、sparse DP 等 | 中 | 过滤准确性影响后续总成本 |
| 6 | GenASM 跨多个 ASM use case 加速 | Page 9 | short/long alignment 111x/116x speedup | 高 | 与下一篇 GenASM 论文衔接 |
| 7 | 单点加速会受 Amdahl 限制 | Page 8-9 challenges | 需要加速整个 read mapping 而非单阶段 | 高 | 端到端设计比局部 kernel 更重要 |
| 8 | 硬件必须支持变化的 read length 和 edit distance | Page 9 | sequencing technologies 快速变化 | 高 | 专用硬件过窄会很快过时 |
| 9 | FASTQ/FASTA 8-bit/base 表示低效 | Page 9 | DNA base 理论只需 2-3 bits | 中 | 数据格式本身也是系统瓶颈 |
| 10 | 采用挑战包括标准化接口和硬件友好格式 | Page 9 | 作者呼吁更灵活模块化架构 | 中 | 这影响真实部署 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖文章主体内容；不提供逐字长篇翻译。

## Title
原文标题：Accelerating Genome Analysis: A Primer on an Ongoing Journey

中文标题：加速基因组分析：一段持续旅程的入门综述

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
文章说明 genome analysis 的第一步通常是 read mapping，即把测序得到的 read fragments 与 reference genome 比较。由于测序技术产生数据的速度已经超过 CPU-based 分析技术，read mapping 成为 pipeline 瓶颈。作者介绍算法优化和硬件加速两个方向，并讨论硬件加速 read mapper 的采用挑战。

## 1. Motivation / 动机

### 原文位置
Page 1 - Page 2

### 中文翻译
测序设备无法一次读完整 genome，只能产生大量短片段 reads。计算系统需要把这些 reads 重新定位到 reference genome 中，以便后续 variant calling。由于 sequencing error 和个体 genetic variation，read 与 reference 并不完全相同，因此需要 approximate string matching。

read mapping 的 ASM 常用动态规划，准确但开销高。作者列出四类挑战：数据集大导致 CPU-memory data movement 高；测序机器产出 reads 的速度增长快；metagenomic sample 需要匹配大量 reference genomes；临床和疫情监控需要快速分析。

## 2. Read Mapping / 读段映射

### 原文位置
Page 2 - Page 3; Figure 1

### 中文翻译
read mapping 的目标是在允许最多 E 个 edits 的情况下，找到 reference genome 中与 read 相似的位置。常见 edits 包括 deletion、insertion 和 substitution。典型 pipeline 有三步：indexing、pre-alignment filtering、sequence alignment。

indexing 利用 seeds 快速找到潜在 mapping locations；filtering 快速检查候选 read-reference pair 是否可能相似；alignment 对剩余候选执行更精确的 DP-based ASM，并输出 alignment score、edit distance、edit 类型和位置。

## 3. Accelerating Indexing / 加速索引

### 原文位置
Page 3 - Page 4

### 中文翻译
indexing 的主要问题是 reference genome 很大，seed 查询会产生大量随机访问。加速方法包括减少 seed 数、优化 FM-index 或 hash-based index 查询、减少内存访问和数据移动。硬件加速 indexing 需要兼顾压缩表示、随机访问和并行查询。

## 4. Accelerating Pre-Alignment Filtering / 加速预比对过滤

### 原文位置
Page 4 - Page 6

### 中文翻译
pre-alignment filtering 的目标是在昂贵 alignment 前快速丢弃明显不相似的候选。常用方法包括 pigeonhole principle、base counting、q-gram filtering 和 sparse DP。硬件实现包括 GateKeeper、SHD、Shouji、GRIM-Filter、SneakySnake 等。

过滤器的关键指标是速度、功耗、false accept rate 和 false reject rate。false reject 会错误丢掉真实相似序列，因此必须避免；false accept 会把无用候选送入 alignment，增加后续成本。

## 5. Accelerating Sequence Alignment / 加速序列比对

### 原文位置
Page 6 - Page 8

### 中文翻译
sequence alignment 是最准确但最昂贵的阶段。传统 Smith-Waterman、Needleman-Wunsch、Levenshtein 等 DP 算法需要填充大量矩阵项。软件优化使用 SIMD、多线程和 GPU；硬件优化使用 FPGA、ASIC、PIM 和 specialized systolic arrays。

作者讨论 Darwin、DRAGEN、GenAx、GASAL2、ASAP 等方案，并指出许多工作只优化一个子步骤，因此端到端收益会被其他阶段限制。

## 6. Adoption Challenges / 采用挑战

### 原文位置
Page 8 - Page 9

### 中文翻译
作者总结未来 read mapper 加速面临四个挑战。第一，需要加速整个 read mapping，而不只是单个阶段。第二，需要减少数据在 CPU-memory、accelerators 和 sequencing machine 与分析计算机之间的移动。第三，硬件必须灵活支持不同 read length、edit distance threshold 和 scoring function，否则会被快速变化的测序技术淘汰。第四，需要更硬件友好的数据格式；FASTQ/FASTA 用 8 bits 表示一个 base，而 DNA base 只需 2-3 bits，格式转换本身会浪费时间。

## 7. Conclusion / 结论性观点

### 原文位置
Page 9

### 中文翻译
作者认为，当前加速努力为未来 genome analysis tools 提供了基础。真正高效的 read mapper 应该结合算法、硬件和数据格式设计，减少 data movement，并保持对新测序技术的适应性。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1a | Page 3 | read mapping 三阶段 | indexing、filtering、alignment 如何连接 | 全文框架图 | 必读 |
| Figure 1b | Page 3 | 每阶段加速方向 | indexing/filtering/alignment 各有不同方法 | 帮助整理文献谱系 | 对照后文阅读 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| 未发现核心表格 | 全文 | 文章以文字综述和 Figure 1 为主 | 无统一实验表 | 注意引用结果来自不同论文 | 不需重点 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| DP 复杂度说明 | Page 3 | 描述 alignment 复杂度 | m 为序列长度，E 为 edit threshold | DP 准确但昂贵 | 是 |
| filtering threshold 规则 | Page 4-6 | pigeonhole/q-gram/sparse DP 判断相似性 | E、q、m 等 | 快速排除不相似候选 | 中 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| Read Mapping | 读段映射 | Page 1-3 | 将 reads 定位到 reference genome | 是 |
| Approximate String Matching (ASM) | 近似字符串匹配 | Page 2 | 允许 insertion/deletion/substitution 的匹配 | 是 |
| Indexing | 索引 | Page 3 | 用 seeds 找候选位置 | 是 |
| Pre-alignment Filtering | 预比对过滤 | Page 3-6 | 在 alignment 前丢弃明显不相似候选 | 是 |
| Sequence Alignment | 序列比对 | Page 3, Page 6-8 | 精确计算 read 与 reference segment 的相似性 | 是 |
| Edit Distance | 编辑距离 | Page 2-3 | 两序列之间最少 edits 数 | 是 |
| q-gram Filtering | q-gram 过滤 | Page 5 | 用长度 q 的子串判断相似性 | 中 |
| Pigeonhole Principle | 鸽巢原理 | Page 4 | 若相似序列至多 E edits，则存在无错片段 | 中 |
| FASTQ/FASTA | 基因组数据格式 | Page 9 | 常用 reads/reference 表示格式 | 中 |
| GenASM | GenASM 加速框架 | Page 9 | bitvector-based ASM 加速框架 | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 需要端到端加速整个 read mapping，而不只是单个阶段；位置：Page 8。
- 数据移动、硬件灵活性和数据格式仍是采用障碍；位置：Page 8-9。

## 2. 论文中隐含的局限
- 本文是综述，缺少统一实验平台和公平横向复现。
- 2020 年后的 pangenome/graph reference、ultra-long reads、GPU/AI-era hardware 未完整覆盖。

## 3. 实验设计可能存在的问题
- 引用结果来自不同输入数据、硬件平台和实现，不能直接比较绝对数值。

## 4. 方法可能不适用的场景
- 对 privacy-sensitive clinical workflows，cloud/hardware offload 方案还需要数据保护机制。
- 对快速变化的 sequencing technology，固定功能 ASIC 可能过早过时。

## 5. 我阅读时应该追问的问题
- 如何定义 read mapper 的端到端吞吐指标？
- pre-alignment filter 的 false accept/false reject 如何影响 variant calling？
- GenASM 与 DRAGEN/Darwin/GenAx 的适用范围如何区分？
- 更硬件友好的 genome data format 为什么难以普及？

## 6. 后续可以继续阅读的方向
- GenASM MICRO 2020。
- GateKeeper/Shouji/SneakySnake/GRIM-Filter。
- Darwin、GenAx、DRAGEN。""",
    },
    "BEER-bit-exact-ECC-recovery_micro20": {
        "title": "Bit-Exact ECC Recovery (BEER): Determining DRAM On-Die ECC Functions by Exploiting DRAM Data Retention Characteristics",
        "zh": "Bit-Exact ECC Recovery（BEER）：利用 DRAM 数据保持特性确定片上 ECC 函数",
        "authors": "Minesh Patel, Jeremie S. Kim, Taha Shahroodi, Hasan Hassan, Onur Mutlu",
        "year": "2020",
        "venue": "MICRO 2020",
        "doi": "未找到",
        "url": "未找到",
        "dataset": "80 real LPDDR4 DRAM chips; 115,300 simulated SEC Hamming codes; EINSim",
        "topic": "DRAM on-die ECC reverse engineering / reliability profiling",
        "keywords": "BEER, BEEP, on-die ECC, parity-check matrix, SAT solver, data retention, LPDDR4",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
BEER 提出一种无需硬件侵入、无需 ECC metadata 的方法，通过精心诱导 data-retention miscorrections 并用 SAT solver 求解，恢复 DRAM on-die ECC 的完整 parity-check matrix，并进一步用 BEEP 推断原始 pre-correction error 的精确位置。

## 2. 研究背景
DRAM scaling 使单 bit 错误更常见，厂商采用 on-die ECC 提升良率。但 on-die ECC 对外不可见，且具体 ECC function 被视为商业机密。第三方系统设计者和研究者只能观察 post-correction errors，无法知道真实 physical errors 如何被 ECC 转换。这会阻碍可靠性建模、二级 ECC 设计和 DRAM error profiling。

## 3. 核心问题
- 如何在不读取 syndrome/parity、不拆芯片、不知道 ECC 实现的情况下恢复完整 on-die ECC function。
- 如何利用 data-retention error 的 pattern asymmetry 触发 ECC-function-specific miscorrections。
- SAT solver 能否在真实 code length 上实际求解 parity-check matrix。
- 知道 ECC function 后，能否恢复 pre-correction bit error count/location。

## 4. 核心贡献
- 提出 BEER，首个恢复完整 DRAM on-die ECC parity-check matrix 的非侵入式方法。
- 在 80 颗真实 LPDDR4 chips 上应用 BEER，发现不同厂商似乎使用不同 ECC functions，同型号同厂商芯片似乎使用同一 function。
- 在仿真中验证 BEER 可正确恢复 115,300 个代表性 SEC Hamming codes，codeword length 覆盖 4-247 bits。
- 评估 SAT solver 时间和内存：128-bit representative codes median 57.1 hours / 6.3 GiB，247-bit 最多 62 hours / 11.4 GiB。
- 提出 BEEP，利用已知 ECC function 从 observed post-correction errors 推断 bit-exact pre-correction error locations。
- 开源 BEER 和 EINSim 扩展工具。

## 5. 方法概述
BEER 有三步：第一，暂停 refresh 并写入 crafted test patterns，利用 data-retention errors 的 CHARGED/DISCHARGED asymmetry 控制错误位置；第二，枚举 ECC 造成 miscorrections 的 bit positions；第三，把观察到的 miscorrection profile 编码为 SAT constraints，求解唯一 parity-check matrix。

## 6. 实验设计
真实芯片实验使用 80 颗 LPDDR4 DRAM chips，来自三家主要厂商。仿真使用 EINSim 生成大量 SEC Hamming codes 验证正确性。性能评估在 10 台 24-core Intel Xeon Gold 5118 servers 上运行 BEER SAT solving。BEEP 通过 Monte Carlo simulation 分析不同 codeword length、error count、per-bit error probability 下的成功率。

## 7. 主要结果
- BEER 在真实 LPDDR4 chips 上恢复 on-die ECC functions，但因保密不能公开具体矩阵；见 Page 2-3, Page 7-8。
- 仿真中 BEER 对 115,300 个 SEC Hamming codes 正确；见 Page 2-3, Section 6。
- {1,2}-CHARGED patterns 总能唯一识别仿真中的 ECC function；见 Page 9-10, Figure 5。
- 对 128-bit 代表性 dataword，BEER median runtime/memory 为 57.1 hours / 6.3 GiB；见 Page 10, Figure 6。
- BEEP 对更现实的 63/127-bit codeword 可接近 100% success rate；见 Page 12, Figure 8-9。

## 8. 关键结论
on-die ECC 的黑盒性并非不可突破。通过利用 DRAM 物理错误特性和 ECC miscorrection 行为，第三方可以恢复足够精确的 ECC function，从而把 observed reliability 和 underlying physical errors 解耦。

## 9. 局限性
真实芯片没有 ground truth 可验证；最终 ECC functions 因保密不能公开；BEER 依赖可诱导足够 data-retention errors；SAT solving 对长 code 仍耗时；BEEP 当前主要展示 data-retention errors，对其他故障模式需扩展。

## 10. 适合我重点关注的内容
重点读 Figure 1 理解不同 ECC functions 如何改变 post-correction errors，Section 4 的 BEER SAT formulation，Figure 5-6 的正确性/性能，Figure 7-9 的 BEEP。

## 11. 和其他文献的关系
BEER 与 HARP、on-die ECC modeling、DRAM error profiling、RowHammer/retention studies 直接相关；它解决的是“有 on-die ECC 后如何看见真实错误”的基础问题。""",
        "key": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | on-die ECC 隐藏 pre-correction errors | Page 1, Introduction | ECC metadata 对系统不可见，post-correction 位置可能不匹配物理错误 | 高 | 可靠性研究的观测层被扭曲 |
| 2 | 同类型 ECC code 的不同 function 会产生不同可见错误分布 | Page 1-2, Figure 1 | 三个 SEC Hamming functions 的 post-correction 分布不同 | 高 | 知道 code 类型不够，必须知道 parity-check matrix |
| 3 | BEER 不需要硬件工具、先验知识或 syndrome/parity | Page 1-2, Contributions | 只观察 software-visible post-correction patterns | 高 | 方法的实际价值所在 |
| 4 | BEER 利用 crafted retention errors 和 miscorrections | Page 4-6, Section 4 | CHARGED patterns + SAT constraints | 高 | 物理错误特性和编码理论结合 |
| 5 | BEER 在 80 颗 LPDDR4 chips 上应用 | Page 2-3, Section 5 | 三大厂商芯片实验 | 高 | 证明不是纯理论 |
| 6 | 缺少真实 ground truth 且不能公开 ECC functions | Page 2-3, Section 2.1/5 | 厂商保密限制 | 高 | 阅读时必须注意验证限制 |
| 7 | 仿真验证覆盖 115,300 个 SEC Hamming codes | Page 2-3, Section 6 | codeword 4-247 bits | 高 | 这是正确性主证据 |
| 8 | SAT runtime 可接受但不轻量 | Page 10, Figure 6 | 128-bit median 57.1h/6.3GiB；247-bit 最多 62h/11.4GiB | 中 | 离线一次性可接受，在线不可行 |
| 9 | BEEP 利用已知 ECC function 推断 bit-exact raw errors | Page 10-12, Figure 7-9 | pre-correction locations recovered from miscorrections | 高 | BEER 的直接实用例子 |
| 10 | BEER 可扩展到其他 linear block code memory devices | Page 13, Future Work | Flash/STT-MRAM/PCM/RRAM 等可能扩展 | 中 | 思想可迁移，但需适配错误模型 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：Bit-Exact ECC Recovery (BEER): Determining DRAM On-Die ECC Functions by Exploiting DRAM Data Retention Characteristics

中文标题：Bit-Exact ECC Recovery（BEER）：利用 DRAM 数据保持特性确定片上 ECC 函数

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
现代 DRAM 使用 on-die ECC 来提升良率，但 ECC function 被隐藏在芯片内部。BEER 通过非侵入方式诱导 data-retention errors，并观察 ECC 在 uncorrectable patterns 下产生的 miscorrections，从而恢复完整 parity-check matrix。作者在真实 LPDDR4 chips 和大规模仿真中验证该方法，并提出 BEEP 用已知 ECC function 反推不可见的 raw bit errors。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 3

### 中文翻译
随着 DRAM cell 缩小，随机单 bit errors 更频繁，厂商使用 on-die ECC 在芯片内部静默纠正错误。问题是，外部系统只能看到 ECC 纠正后的结果，不能看到 syndrome、parity 或被纠正的 raw error。

作者指出，仅知道 ECC 是某种 Hamming SEC code 不够，因为同类型 code 可有许多 parity-check matrix。不同 ECC functions 会把相同 raw error pattern 转换成不同 post-correction error distribution。Figure 1 正是这一点的直观展示。

## 2. Challenges of Unknown On-Die ECCs / 未知片上 ECC 的挑战

### 原文位置
Page 3 - Page 4

### 中文翻译
on-die ECC 被厂商视为商业机密。第三方用户包括系统设计者、大规模系统供应商、测试工程师和研究者。他们需要理解 DRAM 的真实可靠性，但 on-die ECC 会掩盖物理错误位置和数量。

未知 ECC function 会影响二级 ECC 设计、测试 pattern 构造、空间错误分布分析和故障诊断。BEER 的目标是恢复完整 ECC function，使这些分析能够从 post-correction 观测回推 pre-correction 行为。

## 3. Background / 背景

### 原文位置
Page 4 - Page 5

### 中文翻译
论文介绍 data-retention errors、on-die ECC、Hamming code 和 SAT solver。data-retention errors 对 data pattern 敏感，某些 cell 状态更容易从 CHARGED 变为 DISCHARGED。ECC 在错误数量超过纠错能力时可能 miscorrect，即翻转一个本来没有错的 bit。

SAT solver 用于求解布尔约束。BEER 将“某个 unknown parity-check matrix 会导致 observed miscorrection profile”表达成 SAT problem。

## 4. BEER Methodology / BEER 方法

### 原文位置
Page 5 - Page 7

### 中文翻译
BEER 首先写入精心设计的 test patterns，并延长 refresh window 诱导 data-retention errors。通过控制 CHARGED cells 的位置，BEER 让特定 uncorrectable patterns 更可能出现。

随后，BEER 观察哪些 bit positions 出现 miscorrections。每个 miscorrection 都揭示了 syndrome 与 parity-check matrix 的关系。最后，BEER 把这些关系编码成 SAT constraints，求解唯一 parity-check matrix。

## 5. Real DRAM Experiments / 真实 DRAM 实验

### 原文位置
Page 7 - Page 8

### 中文翻译
作者在 80 颗 LPDDR4 chips 上应用 BEER。结果表明不同厂商似乎使用不同 ECC functions，而相同厂商和型号的芯片似乎使用相同 function。由于厂商保密，作者无法获得 ground truth，也不能公开最终恢复的矩阵。

实验噪声通过阈值过滤缓解；BEER 不要求每次观测都完美，只需要 miscorrection profile 足够稳定。

## 6. Simulation and Performance Evaluation / 仿真与性能评估

### 原文位置
Page 8 - Page 10

### 中文翻译
为了弥补真实芯片缺少 ground truth 的问题，作者用 EINSim 对 115,300 个代表性 SEC Hamming codes 做仿真。BEER 能正确恢复这些 code 的 ECC function，codeword length 覆盖 4 到 247 bits。

性能方面，SAT solving 是主要成本。短 code 几乎无压力，128-bit representative code 的 median runtime/memory 为 57.1 hours/6.3 GiB，247-bit code 最多约 62 hours/11.4 GiB。作者认为这是离线一次性任务，因此实际可接受。

## 7. BEEP and Use Cases / BEEP 与应用

### 原文位置
Page 10 - Page 13

### 中文翻译
BEEP 是 BEER 的具体应用：已知 ECC function 后，它可以从 observed post-correction miscorrections 推断 pre-correction raw errors 的数量和 bit-exact locations。BEEP 也使用 SAT solver 构造 test patterns，以便逐 bit 识别 error-prone cells。

仿真结果显示，对较现实的 63-bit 和 127-bit codeword，BEEP 成功率接近 100%，尤其在 error count 和 per-bit error probability 足够高时表现更好。作者还讨论 BEER 可帮助设计二级 ECC、构造 targeted test patterns、研究 spatial error distributions 和诊断 post-correction errors。

## 8. Related Work / 相关工作

### 原文位置
Page 13

### 中文翻译
相关工作包括 on-die ECC characterization、rank-level ECC reverse engineering 和 DRAM error profiling。作者强调 BEER 的不同点是：不需要访问 encoded data、syndrome、纠错事件信号或硬件修改，就能从外部接口观测恢复完整 ECC function。

## 9. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
BEER 证明第三方可以非侵入地恢复 DRAM on-die ECC function。BEEP 进一步说明，一旦知道 ECC function，就能恢复 raw error locations。该工作为带 on-die ECC 的现代 DRAM 可靠性研究和系统设计提供了重要工具。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | 不同 ECC functions 的可见错误分布 | 同类型 ECC code 不同 matrix 会产生不同 post-correction errors | 全文动机图 | 必读 |
| Figure 2 | Page 4 | on-die ECC 接口 | 系统只看到 data，不见 parity/syndrome | 解释黑盒限制 | 结合背景读 |
| Figure 5 | Page 9-10 | 匹配 miscorrection profiles 的 ECC functions 数 | {1,2}-CHARGED patterns 可唯一识别 | 正确性支撑 | 看不同 pattern 对辨识力的影响 |
| Figure 6 | Page 10 | BEER runtime/memory | SAT solving 成本随 code length 增加 | 实用性评估 | 注意离线性质 |
| Figure 7 | Page 11 | BEEP 流程 | pattern crafting、experiment、raw error inference | BEER 的应用 | 对照 BEEP 小节 |
| Figure 8-9 | Page 12 | BEEP success rate | 较长 codeword 成功率高 | 证明 BEEP 可用 | 关注 63/127-bit |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 5 | data-retention error patterns 与 syndromes | 不同 charged pattern 暴露不同 syndrome 信息 | BEER 构造约束基础 | 配合 Section 4 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Equation 4 | Page 11 | BEEP 由 syndrome 求 pre-correction codeword | H 为 parity-check matrix，c0 为错误 codeword | 已知 H 后可解 raw error locations | 是 |
| SAT constraints | Page 5-7 | 求解 unknown parity-check matrix | columns of H, miscorrection observations | 把 ECC recovery 转成 satisfiability | 是 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| On-Die ECC | 片上 ECC | Page 1 | DRAM 芯片内部不可见纠错机制 | 是 |
| BEER | Bit-Exact ECC Recovery | Page 1 | 恢复完整 on-die ECC function 的方法 | 是 |
| BEEP | Bit-Exact Error Profiling | Page 10 | 利用已知 ECC function 恢复 raw error locations | 是 |
| Parity-Check Matrix | 校验矩阵 | Page 1-2 | 定义线性 ECC function 的矩阵 | 是 |
| Miscorrection | 误纠正 | Page 2, Page 5 | ECC 在 uncorrectable pattern 下翻转非错误 bit | 是 |
| Pre-Correction Error | 纠错前错误 | Page 1 | 物理上真实发生的 raw bit error | 是 |
| Post-Correction Error | 纠错后可见错误 | Page 1 | ECC 作用后软件可观察的错误 | 是 |
| SAT Solver | 可满足性求解器 | Page 4-7 | 求解布尔约束的工具 | 是 |
| Data-Retention Error | 数据保持错误 | Page 4-5 | refresh 间隔过长导致 cell 电荷丢失 | 是 |
| SEC Hamming Code | 单错纠正 Hamming 码 | Page 1-3 | on-die ECC 可能采用的线性纠错码 | 中 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- 真实芯片无法获得 ground truth ECC functions；位置：Page 2-3。
- 由于保密关系，不能公开恢复出的最终 ECC functions；位置：Page 2-3。
- BEEP 主要展示 data-retention errors，其他错误机制留待未来；位置：Page 12。

## 2. 论文中隐含的局限
- BEER 需要能诱导足够多、可控的 uncorrectable retention errors。
- SAT solving 对更复杂 ECC 可能成本更高。

## 3. 实验设计可能存在的问题
- 真实芯片结果无法直接验证完全正确性，只能靠仿真证明方法正确。
- 厂商可能使用非线性或组合型 ECC/repair 机制，超出本文假设。

## 4. 方法可能不适用的场景
- 如果 ECC 不属于可用线性 block code 建模，BEER 需要扩展。
- 如果芯片隐藏/扰动 post-correction error visibility，BEER 观测信息不足。

## 5. 我阅读时应该追问的问题
- DDR5 on-die ECC 是否仍可用 BEER 类方法恢复？
- BEER 与 HARP 如何互补？
- 恢复 ECC function 是否可能带来攻击风险？
- 如何优化 SAT formulation 降低 runtime？

## 6. 后续可以继续阅读的方向
- HARP-memory-error-profiling_micro21。
- understanding-and-modeling-in-DRAM-ECC_dsn19。
- REAPER/retention profiling 相关工作。""",
    },
    "EDEN-efficient-DNN-inference-with-approximate-memory_micro19": {
        "title": "EDEN: Enabling Energy-Efficient, High-Performance Deep Neural Network Inference Using Approximate DRAM",
        "zh": "EDEN：使用近似 DRAM 实现高能效、高性能 DNN 推理",
        "authors": "Skanda Koppula, Lois Orosa, A. Giray Yağlıkçı, Roknoddin Azizi, Taha Shahroodi, Konstantinos Kanellopoulos, Onur Mutlu",
        "year": "2019",
        "venue": "MICRO-52",
        "doi": "10.1145/3352460.3358280",
        "url": "https://doi.org/10.1145/3352460.3358280",
        "dataset": "DNN workloads from OpenVINO/DarkNet; real DDR3/DDR4 approximate DRAM error characterization; CPU/GPU/Eyeriss/TPU simulations",
        "topic": "Approximate DRAM for DNN inference",
        "keywords": "EDEN, approximate DRAM, DNN inference, curricular retraining, voltage scaling, latency reduction, BER",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
EDEN 利用 DNN 对 bit errors 的容忍性，通过 curricular retraining、DNN error tolerance characterization 和 DNN-to-DRAM mapping，让 DRAM 在降低 voltage/latency 的近似模式下运行，同时满足用户指定的 accuracy target。

## 2. 研究背景
DNN inference 越来越 memory-intensive，DRAM energy 和 latency 会成为 CPU/GPU/accelerator 上的重要瓶颈。DRAM 厂商通常用保守 voltage/timing 保证可靠性；降低 VDD 或 tRCD/tRAS/tRP 可节能/加速，但会增加 bit error rate。DNN 具有一定 error tolerance，因此 approximate DRAM 可能适合 DNN inference。

## 3. 核心问题
- 如何在 approximate DRAM bit errors 下保持 DNN accuracy。
- 如何根据真实 DRAM error pattern 而非简单随机错误训练 DNN。
- 不同 DNN data types/layers 对 errors 的容忍度是否不同。
- 如何将不同 data types 映射到不同 approximate DRAM partitions。
- 在 CPU/GPU/DNN accelerator 上能获得多少 energy/performance benefit。

## 4. 核心贡献
- 提出 EDEN，首个面向 DNN inference 的 approximate DRAM 通用框架。
- 提出 curricular retraining，逐步增加 error rate，避免 accuracy collapse，将 BER tolerance 提升 5-10x。
- 系统表征 DNN 对 approximate DRAM errors 的容忍度，发现低精度和首/末层更敏感，pruning 影响不显著。
- 基于 8 个真实 DDR4 modules 的 reduced voltage/latency 错误分布构建 4 类 error models。
- 在 CPU/GPU/Eyeriss/TPU 上评估：在 <1% accuracy loss 下，平均 DRAM energy reduction 分别为 21%、37%、31%、32%；CPU/GPU latency-bound 网络平均 speedup 8%/2.7%。

## 5. 方法概述
EDEN 三步：第一，用 approximate DRAM error characteristics 注入训练过程，进行 curricular retraining；第二，characterize 各 layer/data type 的 maximum tolerable BER；第三，把 DNN data 映射到满足 BER 约束且 voltage/latency 降幅最大的 DRAM partition。

## 6. 实验设计
作者用 SoftMC/真实 DRAM 模块生成 reduced voltage/latency error data，并建立 error models。DNN 包括 OpenVINO 与 DarkNet 模型，如 YOLO、VGG、ResNet、SqueezeNet、DenseNet、AlexNet 等，覆盖 FP32 和 int8。系统评估包含 ZSim+Ramulator CPU、GPGPU-Sim+GPUWattch GPU、SCALE-Sim+DRAMPower Eyeriss/TPU。

## 7. 主要结果
- curricular retraining 可使 DNN tolerable BER 提升 5-10x；见 Page 8-10, Figure 9-10。
- EDEN 在 CPU 上平均节省 21% DRAM energy，same accuracy target 下仍有 16%；见 Page 11, Figure 13。
- EDEN 在 CPU latency-bound DNN 上平均 speedup 8%、最高 17%；见 Page 12, Figure 14。
- GPU 平均 energy reduction 37%，平均 speedup 2.7%；见 Page 12。
- Eyeriss/TPU 上平均 DRAM energy reduction 31%/32%；见 Page 12。

## 8. 关键结论
approximate memory 并非只适合“允许错误”的应用；通过 error-aware retraining 和 data-to-memory mapping，它也可以在严格 accuracy target 下服务 DNN inference。

## 9. 局限性
EDEN 依赖准确的 DRAM error models 和稳定环境；retraining/characterization 有成本；DNN、数据集、温度、老化、量化和 layer sensitivity 会影响可用 BER；对训练 workload、transformer/LLM 和现代 HBM/GDDR 的覆盖需要更新。

## 10. 适合我重点关注的内容
重点读 Figure 4 的框架、Section 3 curricular retraining、Section 4 error models、Figure 9-14 的 accuracy/energy/performance。

## 11. 和其他文献的关系
EDEN 连接 approximate DRAM、DNN robustness 和 memory systems，是 Voltron/Flexible-Latency DRAM 与 ML inference accelerator 之间的桥梁。""",
        "key": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | DNN 对 bit errors 有内在容忍性 | Page 1-2 | input/weight/output data types 可承受一定 errors | 高 | EDEN 的算法前提 |
| 2 | 降低 DRAM VDD/latency 可节能/加速但增加 BER | Page 1-2, Background | DRAM reliability-performance tradeoff | 高 | EDEN 的硬件前提 |
| 3 | EDEN 三步：retraining、characterization、mapping | Page 3-4, Figure 4 | 框架图和 Section 3 | 高 | 全文核心机制 |
| 4 | curricular retraining 逐步增加 error rate 避免 accuracy collapse | Page 4, Section 3.2 | progressive error injection | 高 | 与普通 retraining 的关键差异 |
| 5 | EDEN error models 来自真实 DDR4 modules | Page 6-7, Figure 5-8 | reduced voltage/latency 错误表征 | 高 | 不只是 uniform random faults |
| 6 | tolerable BER 在 layer/data type 间差异大 | Page 10-11, Figure 11-12 | weights 通常比 IFMs 更耐错，首/末层更敏感 | 高 | 支持 fine-grained mapping |
| 7 | curricular retraining 提升 BER tolerance 5-10x | Page 10, Figure 9-10 | good-fit error model + curriculum 明显右移 accuracy curve | 高 | 主要算法结果 |
| 8 | CPU 平均 DRAM energy saving 21%，speedup 8% | Page 11-12, Figure 13-14 | <1% accuracy loss | 高 | 系统收益主结果 |
| 9 | GPU/Eyeriss/TPU 也有 energy benefit | Page 12 | GPU 37%，Eyeriss 31%，TPU 32% energy reduction | 高 | 说明框架跨架构 |
| 10 | speedup 只在 latency-bound DNN 明显 | Page 12 | Eyeriss/TPU reduced tRCD 无 speedup，prefetch/dataflow 有效 | 中 | EDEN 的性能收益有条件 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：EDEN: Enabling Energy-Efficient, High-Performance Deep Neural Network Inference Using Approximate DRAM

中文标题：EDEN：使用近似 DRAM 实现高能效、高性能 DNN 推理

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
DNN inference 对能效和性能要求很高，而 DRAM energy 和 latency 常成为瓶颈。approximate DRAM 通过降低 voltage 或 latency 超出标准规格来节能/加速，但会产生更高 bit error rate。EDEN 利用 DNN 的 error tolerance，通过 retraining 和 data mapping，在满足用户 accuracy target 的同时使用 approximate DRAM。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
DNN 模型越来越大，memory footprint 和 off-chip access 增长。DRAM 可占 DNN 系统能耗的重要部分，LLC miss latency 也会阻塞推理。已有工作通过压缩、量化、PIM 或新 DRAM 结构优化 memory efficiency；EDEN 则采取正交方向：调整现有 DRAM 的运行参数，让它以更低 voltage/latency 近似运行。

EDEN 建立在两个观察上：DNN 对输入、权重和输出中的错误有容忍性；DRAM 参数可以用可靠性换性能/能耗。

## 2. Background / 背景

### 原文位置
Page 2 - Page 3

### 中文翻译
论文介绍 DNN data types：input feature maps（IFMs）、output feature maps（OFMs）和 weights。不同 layer 和 data type 的 memory access 行为、数值范围和 error sensitivity 不同。DRAM 方面，论文回顾 cell、subarray、bank、timing 参数和 voltage/latency scaling。

## 3. EDEN Framework / EDEN 框架

### 原文位置
Page 3 - Page 5; Figure 4

### 中文翻译
EDEN 包含三步。第一，boosting DNN error tolerance：用 approximate DRAM 的 error characteristics 在训练中注入错误，使 DNN 适应目标设备。第二，DNN error tolerance characterization：测量各 DNN data type 可承受的 maximum BER。第三，DNN-to-DRAM mapping：把不同数据放到不同 approximate DRAM partitions，使每部分 BER 不超过其容忍阈值，并尽量降低 voltage/latency。

curricular retraining 是第一步的关键。若一开始注入高 error rate，训练可能 accuracy collapse；EDEN 逐步增加 error rate，使模型渐进适应。对浮点 exponent bit 导致的异常值，EDEN 也提供 correction/saturation/zeroing 类机制避免训练崩溃。

## 4. Error Models / 错误模型

### 原文位置
Page 6 - Page 8

### 中文翻译
EDEN 需要 approximate DRAM 的 error model，以便在训练和离线 mapping 中模拟真实错误。作者从真实 DDR3/DDR4 模块在 reduced voltage 和 reduced latency 下的错误分布构造四类 probabilistic models，覆盖 uniform、row/bitline locality、data pattern dependence 等现象。

这些模型用于 EDEN offloading：即使目标 approximate DRAM 不在训练机器上，也能用 error model 注入近似错误进行 retraining。

## 5. DNN Characterization / DNN 表征

### 原文位置
Page 8 - Page 11

### 中文翻译
作者表征不同 DNN 在不同 BER、precision、layer 和 data type 下的 accuracy。结果显示，较低 precision 通常更敏感；first/last layers 比中间层更敏感；weights 通常比 IFMs 更能容忍错误；magnitude-based pruning 对 error resilience 影响不显著。

fine-grained characterization 能让不同 IFMs/weights 映射到不同 DRAM partitions，从而比 coarse-grained mapping 使用更激进的 voltage reduction。

## 6. System-Level Evaluation / 系统级评估

### 原文位置
Page 11 - Page 12

### 中文翻译
CPU 评估显示，在 <1% accuracy loss 下，EDEN 平均节省 21% DRAM energy；若要求与原始 accuracy 相同，仍有 16% 平均 energy saving。降低 tRCD 在 latency-bound networks 上带来平均 8%、最高 17% speedup。

GPU 评估显示，EDEN 对 YOLO/YOLO-Tiny 等 workload 平均降低 37% DRAM energy，平均 speedup 2.7%。Eyeriss 和 TPU 评估显示，降低 DDR4 voltage 分别带来 31% 和 32% 平均 DRAM energy savings；但 reduced tRCD 对这些 accelerator 没有 speedup，因为其 dataflow/prefetch 使 memory access 更可预测。

## 7. Related Work / 相关工作

### 原文位置
Page 12 - Page 13

### 中文翻译
相关工作包括 DNN approximate hardware、reduced refresh、low-voltage SRAM、approximate arithmetic、emerging memory、approximate storage 和随机 error injection。EDEN 的区别是使用真实 approximate DRAM error characterization，并将 DNN retraining 与 memory partition mapping 结合。

## 8. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
EDEN 证明 approximate DRAM 可以在 DNN inference 中带来能耗和性能收益，同时满足 accuracy target。关键是使用与真实 memory error pattern 匹配的 curricular retraining，并按 data type/layer 的 error tolerance 做映射。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 2 | DNN layer data types | IFM/OFM/weights 的数据流 | 理解 mapping 单位 | 先看 |
| Figure 2-3 | Page 3 | DRAM organization/timing | VDD/tRCD/tRAS/tRP 如何影响访问 | 连接 approximate DRAM | 对照背景 |
| Figure 4 | Page 4 | EDEN framework | retraining、characterization、mapping 三步 | 核心框架图 | 必读 |
| Figure 5-8 | Page 6-8 | error models/real DRAM validation | approximate DRAM errors 非 uniform | 支撑训练模型 | 注意真实模块来源 |
| Figure 9-10 | Page 9-10 | curricular retraining | good-fit model + curriculum 提升 BER tolerance | 核心算法结果 | 必读 |
| Figure 11-12 | Page 10-11 | fine-grained BER tolerance/mapping | layer/data type 差异大 | 支持 partition mapping | 看 weights vs IFMs |
| Figure 13 | Page 11 | CPU DRAM energy saving | 平均 21% saving | 主要系统结果 | 注意 <1% accuracy loss |
| Figure 14 | Page 12 | CPU speedup | latency-bound DNN 最高 17% | 性能收益条件 | 看 ideal tRCD=0 对照 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 2 | Page 8 | baseline network accuracies | 列出评估 DNN 基线 | 判断 accuracy loss | 查看模型范围 |
| Table 3 | Page 10-11 | tolerable BER / DRAM parameters | 每个 DNN 可用的 VDD/tRCD 配置 | mapping 依据 | 重点 |
| Table 4-6 | Page 11-12 | CPU/GPU/Eyeriss/TPU configs | 系统模拟参数 | 影响结果外推 | 需要复现时看 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 5 | fine-grained DNN-to-DRAM mapping | BER tolerance、partition BER、parameter reduction | 把数据放到能承受的最激进 DRAM partition | 是 |
| Error model formulas | Page 6-7 | 描述 bitline/wordline/locality errors | PW/PB/FB 等 | 近似真实 DRAM 错误分布 | 中 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| EDEN | EDEN 框架 | Page 1, Page 3 | 用 approximate DRAM 加速/节能 DNN inference | 是 |
| Approximate DRAM | 近似 DRAM | Page 1 | 降低 voltage/latency 换取更高 BER 的 DRAM | 是 |
| Curricular Retraining | 课程式再训练 | Page 4 | 逐步提高 error rate 的 retraining | 是 |
| Bit Error Rate (BER) | 位错误率 | Page 3-11 | approximate DRAM 错误强度指标 | 是 |
| IFM/OFM | 输入/输出特征图 | Page 2 | DNN layer 的主要数据类型 | 是 |
| DNN-to-DRAM Mapping | DNN 到 DRAM 映射 | Page 4-5 | 按 tolerance 将数据放入不同 partitions | 是 |
| VDD | 供电电压 | Page 1-3 | 降低可节省 DRAM energy | 是 |
| tRCD/tRAS/tRP | DRAM timing 参数 | Page 3 | 降低可降低 latency 但增错 | 是 |
| Accuracy Collapse | 精度崩溃 | Page 4, Page 9 | 高 error rate 训练导致 accuracy 突降 | 是 |
| Error Model | 错误模型 | Page 6-8 | 模拟真实 approximate DRAM errors 的概率模型 | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- error model 必须足够贴合真实 DRAM；poor-fit model retraining 效果差；位置：Page 10, Figure 10。
- performance speedup 主要出现在 latency-bound networks；位置：Page 12。

## 2. 论文中隐含的局限
- 需要 retraining 和 profiling，部署前成本不低。
- 环境温度、老化、data pattern 变化可能让 error model 过期。
- 2019 DNN 工作负载不覆盖现代 Transformer/LLM。

## 3. 实验设计可能存在的问题
- 部分系统结果基于模拟器和 error model，而非全系统真实 approximate DRAM 部署。
- fine-grained mapping 需要 memory controller/OS/runtime 支持，实际复杂度较高。

## 4. 方法可能不适用的场景
- 对 accuracy safety 极严、不能容忍任何偶发错误的场景。
- 对没有 retraining 权限的闭源模型或动态模型。
- 对 error distribution 快速变化的 DRAM。

## 5. 我阅读时应该追问的问题
- EDEN 能否用于 transformer/LLM KV cache 和 weights？
- on-die ECC 会如何改变 approximate DRAM errors？
- runtime 如何监测 BER drift？
- fine-grained mapping 与 page allocator 如何集成？

## 6. 后续可以继续阅读的方向
- Voltron、Flexible-Latency DRAM、DIVA-DRAM。
- ApproxANN / DNN error resilience。
- PIM for DNN inference。""",
    },
    "GenASM-approximate-string-matching-framework-for-genome-analysis_micro20": {
        "title": "GenASM: A High-Performance, Low-Power Approximate String Matching Acceleration Framework for Genome Sequence Analysis",
        "zh": "GenASM：面向基因组序列分析的高性能低功耗近似字符串匹配加速框架",
        "authors": "Damla Senol Cali, Gurpreet S. Kalsi, Zülal Bingöl, Can Firtina, Lavanya Subramanian, Jeremie S. Kim, Rachata Ausavarungnirun, Mohammed Alser, Juan Gómez-Luna, Amirali Boroumand, Anant Nori, Allison Scibisz, Sreenivas Subramoney, Can Alkan, Saugata Ghose, Onur Mutlu",
        "year": "2020",
        "venue": "MICRO 2020",
        "doi": "未找到",
        "url": "未找到",
        "dataset": "GRCh38 human genome; PacBio/ONT/Illumina reads; Edlib datasets; synthesized SystemVerilog + simulator",
        "topic": "Genome ASM acceleration / PIM / Bitap hardware",
        "keywords": "GenASM, approximate string matching, Bitap, GenASM-DC, GenASM-TB, read alignment, pre-alignment filtering, edit distance, 3D-stacked memory",
        "summary": """# 中文阅读摘要

## 1. 一句话总结
GenASM 修改 Bitap 算法以支持长读、消除 loop-carried dependencies 并增加 traceback，再与 systolic-array hardware 和 3D-stacked memory PIM co-design，形成可加速 read alignment、pre-alignment filtering 和 edit distance 的通用 ASM 框架。

## 2. 研究背景
Genome sequence analysis 的多个步骤依赖 approximate string matching。传统 DP-based ASM 准确但时间/空间复杂度高，成为 read mapping 的核心瓶颈。Bitap 使用 bitwise operations，硬件友好，但原始版本不支持长读、高效并行和 traceback。GenASM 试图把 Bitap 改造成实用的 genome ASM accelerator。

## 3. 核心问题
- 如何让 Bitap 支持 long reads 和高 edit distance。
- 如何消除 Bitap 的 loop-carried dependencies，提升单次 ASM 的内部并行度。
- 如何实现 Bitap-compatible traceback，输出 CIGAR/optimal alignment。
- 如何在硬件中平衡 compute units、SRAM 容量和 memory bandwidth。
- GenASM 是否能跨 alignment、filtering、edit distance 三种 use cases 优于软件和硬件 baselines。

## 4. 核心贡献
- 首次增强并加速 Bitap 用于 genome ASM。
- 提出 GenASM-DC，用于 bitvector generation 和 distance calculation。
- 提出 GenASM-TB，用于 Bitap-compatible traceback。
- 设计基于 systolic array、local SRAM、3D-stacked memory vault-level parallelism 的低功耗硬件。
- 对 long read alignment，GenASM 相比 12-thread Minimap2 speedup 116x，相比 GACT speedup 3.9x，power 降低 37x/2.7x。
- 对 short read alignment，相比 12-thread BWA-MEM/Minimap2 speedup 111x/158x，相比 SillaX speedup 1.9x。
- 对 pre-alignment filtering，相比 Shouji 在 100bp 上 speedup 3.7x、power 降低 1.7x，并显著降低 false accept。
- 对 edit distance，相比 Edlib speedup 22-12501x、power 降低 548-582x；相比 ASAP speedup 9.3-400x、power 降低 67x。

## 5. 方法概述
GenASM 基于改进 Bitap。算法层面支持 long reads、通过 loop unrolling 消除依赖、采用 divide-and-conquer 降低 memory footprint，并设计 traceback。硬件层面包括 GenASM-DC systolic array 和 GenASM-TB traceback engine，每个 vault 有 local DC-SRAM/TB-SRAM，32 vaults 并行提升吞吐。

## 6. 实验设计
作者综合 synthesized SystemVerilog model 和 detailed simulation-based performance modeling。比较对象包括 Minimap2、BWA-MEM、GASAL2、GACT/Darwin、SillaX/GenAx、Shouji、Edlib、ASAP。数据包括 human reference genome GRCh38、PacBio/ONT long reads、Illumina short reads、Edlib edit distance datasets。

## 7. 主要结果
- 单个 GenASM accelerator 面积 0.334 mm²、功耗 101 mW；32 vaults 总面积 10.69 mm²、总功耗 3.23 W；见 Page 10, Table 1。
- long read alignment 相比 Minimap2 12-thread speedup 116x，power 降低 37x；见 Page 10, Figure 9。
- short read alignment 相比 BWA-MEM/Minimap2 12-thread speedup 111x/158x；见 Page 10, Figure 10。
- 端到端 pipeline speedup 相对 BWA-MEM/Minimap2 为 Illumina 2.4x/1.9x、PacBio 6.5x/3.4x、ONT 4.9x/2.1x；见 Page 10, Figure 11。
- pre-alignment filtering false accept 远低于 Shouji，false reject 为 0%；见 Page 12。
- edit distance 相比 Edlib 和 ASAP 大幅加速；见 Page 12, Figure 14。

## 8. 关键结论
GenASM 的价值不只是一个更快 alignment accelerator，而是展示了 algorithm-hardware-memory co-design 如何把一个 bitvector ASM algorithm 变成跨多个 genome analysis steps 的可扩展低功耗框架。

## 9. 局限性
许多结果基于综合和模拟；部分 baseline 结果来自原论文而非重实现；pre-alignment filtering 对更长 reads 的 speedup 下降；一些潜在 use cases 只讨论未评估；复杂 scoring scheme 和 traceback 配置仍需扩展。

## 10. 适合我重点关注的内容
重点读 Bitap limitations、GenASM-DC/GenASM-TB 设计、Figure 4-8、Table 1、Figure 9-14，以及 sources of improvement。

## 11. 和其他文献的关系
GenASM 是 Accelerating Genome Analysis primer 中重点提到的系统；也与 PIM/near-memory acceleration、NERO、SneakySnake、Darwin、GenAx 等形成 genome accelerator 脉络。""",
        "key": """# Key Points with Source Locations

| 编号 | 重点内容 | 原文位置 | 支持证据 | 重要性 | 我的理解 |
|---|---|---|---|---|---|
| 1 | ASM 是 genome sequence analysis 多个步骤的瓶颈 | Page 1-2 | read mapping、WGA、MSA 都需要 ASM | 高 | GenASM 的适用范围大 |
| 2 | 原始 Bitap 硬件友好但有五个限制 | Page 3-4 | 不支持长读、依赖、traceback、memory footprint 等 | 高 | 设计动机 |
| 3 | GenASM-DC 支持 long reads 并消除依赖 | Page 5, Figure 5 | loop unrolling 和 parallel bitvectors | 高 | 性能核心 |
| 4 | GenASM-TB 提供 Bitap-compatible traceback | Page 6, Algorithm 2, Figure 6 | 利用 intermediate bitvectors 生成 alignment | 高 | 让结果可用于 read alignment |
| 5 | 硬件采用 systolic array + local SRAM | Page 7-8, Figure 7-8 | 64 PEs、DC-SRAM、TB-SRAM | 高 | 降低数据移动和带宽压力 |
| 6 | 3D-stacked memory vault-level parallelism 提供 32x 并行 | Page 8 | 每 vault 一个 accelerator | 高 | PIM/near-memory 设计关键 |
| 7 | 面积功耗很小 | Page 10, Table 1 | 单 accelerator 0.334mm²/101mW，32 vaults 3.23W | 中 | 支持能效主张 |
| 8 | alignment 对软件和硬件 baseline 都大幅提升 | Page 10-11, Figure 9-13 | long/short reads 多项 speedup/power improvement | 高 | 主要实验结果 |
| 9 | filtering accuracy 优于 Shouji | Page 12 | false accept 0.02%/0.002%，false reject 0% | 高 | 不只是快，还减少后续 alignment |
| 10 | edit distance speedup 极大 | Page 12, Figure 14 | 22-12501x vs Edlib, 9.3-400x vs ASAP | 高 | 说明 GenASM 作为通用 ASM kernel 的价值 |
| 11 | 未评估的用例包括 de novo overlap、indexing、WGA、generic text search | Page 13, Section 11 | 作者列为 future use cases | 中 | 框架潜力但需验证 |""",
        "translation": """# Full Chinese Translation

## 版权与完整性说明
以下为逐节中文详译/译述，覆盖论文主体、设计、实验和结论；不提供逐字长篇翻译。

## Title
原文标题：GenASM: A High-Performance, Low-Power Approximate String Matching Acceleration Framework for Genome Sequence Analysis

中文标题：GenASM：面向基因组序列分析的高性能低功耗近似字符串匹配加速框架

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译
Genome sequence analysis 的第一步 read mapping 需要把 reads 匹配到 reference genome 中。ASM 能处理 sequencing errors 和 genetic variations，但计算开销大。GenASM 是首个面向 genome analysis 的 ASM acceleration framework。它修改 Bitap 算法以提升并行性、降低 memory footprint，并设计硬件 accelerator。评估显示 GenASM 在 read alignment、pre-alignment filtering 和 edit distance 三个 use cases 中都显著优于软件和硬件 baselines。

## 1. Introduction / 引言

### 原文位置
Page 1 - Page 2

### 中文翻译
现代 sequencing machines 产生大量 reads，short reads 错误率低但短，long reads 更长但错误率高。read mapping 必须处理 insertion、deletion 和 substitution，因此需要 approximate string matching。传统 DP-based ASM 时间和空间复杂度高，增长速度跟不上 sequencing throughput。

GenASM 的目标是为 short/long reads 提供快速、低功耗、可复用的 ASM 框架，并能加速 genome analysis pipeline 中多个步骤。

## 2. Background / 背景

### 原文位置
Page 2 - Page 4

### 中文翻译
典型 read mapping 包含 indexing、seeding、pre-alignment filtering 和 read alignment。ASM 的目标是在允许最多 E 个 edits 的情况下找出 read 与 reference text 的相似位置。Bitap 是一种 bitvector-based ASM algorithm，使用简单 bitwise operations，因此适合硬件。

原始 Bitap 的限制包括：对 long reads 支持不足、loop-carried dependencies 限制并行、不能执行 traceback、memory footprint 随参数增大、在通用处理器上受 register/cache 限制。

## 3. GenASM Overview / GenASM 概览

### 原文位置
Page 4 - Page 5; Figure 4

### 中文翻译
GenASM 包含两个硬件/算法组件。GenASM-DC 负责执行修改后的 Bitap，生成 match/insertion/deletion/substitution bitvectors 并计算 minimum edit distance。GenASM-TB 使用这些 bitvectors 进行 traceback，输出 optimal alignment。

设计目标是让 compute resources 与 SRAM capacity/bandwidth 匹配，避免资源浪费，并利用 3D-stacked memory logic layer 的 vault-level parallelism。

## 4. GenASM-DC Algorithm / GenASM-DC 算法

### 原文位置
Page 5; Figure 5

### 中文翻译
GenASM-DC 修改 Bitap 以支持 long reads，并通过 loop unrolling 消除邻近 bitvector 的依赖，使多个 non-neighbor bitvectors 可以并行计算。它还把 text 划分为 overlapping sub-texts，以支持 text-level parallelism 和 arbitrary-length sequences。

这种 divide-and-conquer 思路降低了 memory footprint，并使硬件可以用固定大小 windows 处理长序列。

## 5. GenASM-TB Algorithm / GenASM-TB 算法

### 原文位置
Page 6; Algorithm 2; Figure 6

### 中文翻译
GenASM-TB 是 Bitap-compatible traceback algorithm。它从 GenASM-DC 保存的 intermediate bitvectors 出发，反向追踪 match、substitution、insertion 和 deletion，生成 CIGAR-like alignment。为了避免存储全部 bitvectors，GenASM-TB 也采用 divide-and-conquer 和 window overlap。

## 6. Hardware Design / 硬件设计

### 原文位置
Page 7 - Page 8; Figure 7-8

### 中文翻译
GenASM-DC 被实现为 linear cyclic systolic array，包含 64 PEs。每个 accelerator 配有 DC-SRAM 和多个 TB-SRAMs，以减少外部带宽需求。GenASM-TB 使用简单控制逻辑读取 per-PE TB-SRAM 并执行 traceback。

在 3D-stacked memory 配置中，每个 vault 放置一个 GenASM accelerator，32 vaults 可并行处理 32 个 alignments。这样把计算放在 memory logic layer，减少 reference/read 数据移动。

## 7. Evaluation Methodology / 评估方法

### 原文位置
Page 9

### 中文翻译
作者综合 SystemVerilog synthesis、memory estimation 和 cycle-accurate simulation。比较对象包括 BWA-MEM、Minimap2、GASAL2、GACT/Darwin、SillaX/GenAx、Shouji、Edlib 和 ASAP。数据集覆盖 human genome GRCh38、PacBio/ONT/Illumina reads 和 edit distance datasets。

## 8. Results / 结果

### 原文位置
Page 10 - Page 12

### 中文翻译
面积和功耗方面，单个 GenASM accelerator 面积 0.334 mm²、功耗 101 mW；32 vaults 总面积 10.69 mm²、总功耗 3.23 W。

read alignment 方面，long reads 上 GenASM 相比 Minimap2 12-thread alignment step speedup 116x，相比 BWA-MEM 12-thread speedup 648x，并大幅降低 power。short reads 上，相比 BWA-MEM/Minimap2 12-thread speedup 111x/158x。端到端 pipeline 中替换 alignment step 后，Illumina/PacBio/ONT 也获得 1.9x 到 6.5x 的 speedup。

硬件比较中，GenASM 比 Darwin 的 GACT 平均 throughput 高 3.9x、power 低 2.7x；相比 SillaX short read alignment throughput 高 1.9x。pre-alignment filtering 中，GenASM 在 100bp 数据上比 Shouji 快 3.7x、power 低 1.7x，并将 false accept rate 降到很低且 false reject 为 0。edit distance 中，GenASM 相比 Edlib 和 ASAP 也有数量级 speedup 和 power reduction。

## 9. Sources of Improvement / 改进来源

### 原文位置
Page 12 - Page 13

### 中文翻译
GenASM 的收益来自三层。算法层面，divide-and-conquer 大幅降低 GenASM-DC 执行时间，尤其是 long reads。硬件层面，systolic array 提供 64x parallelism，per-PE SRAM 降低 traceback bandwidth。技术层面，3D-stacked memory 的 vault-level parallelism 提供 32x 并行。

## 10. Other Use Cases / 其他用例

### 原文位置
Page 13

### 中文翻译
作者讨论四个未评估但潜在适用的用例：de novo assembly 的 read-to-read overlap finding、hash-table based indexing、whole genome alignment 和 generic text search。由于 GenASM 可处理 arbitrary-length sequences 并可扩展 alphabet，它也可能用于 RNA/protein sequence alignment。

## 11. Conclusion / 结论

### 原文位置
Page 13

### 中文翻译
GenASM 展示了基于修改 Bitap 的 ASM framework 如何通过算法、硬件和 memory 共同设计，在多个 genome analysis use cases 中达到高性能和低功耗。作者希望这种方法启发更多 bioinformatics 和 emerging applications 的 co-design。""",
        "figures": """# Figures, Tables, and Equations Notes

## Figures

| 图编号 | 原文位置 | 图的主题 | 图想表达什么 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Figure 1 | Page 3 | read mapping 四步 | indexing/seeding/filtering/alignment 流程 | 背景框架 | 先读 |
| Figure 2 | Page 3 | edit 类型 | deletion/substitution/insertion | ASM 基础 | 简单看 |
| Figure 3 | Page 4 | Bitap example | 原始 Bitap 如何计算 | 理解改进前算法 | 结合 Algorithm 1 |
| Figure 4 | Page 5 | GenASM overview | GenASM-DC/TB 数据流 | 核心架构图 | 必读 |
| Figure 5 | Page 5 | loop unrolling | 消除依赖实现并行 | GenASM-DC 核心 | 必读 |
| Figure 6 | Page 6 | traceback example | GenASM-TB 如何恢复 alignment | correctness 关键 | 细读 |
| Figure 7-8 | Page 7-8 | DC/TB hardware | systolic array、SRAM、TB logic | 硬件实现 | 结合 Table 1 |
| Figure 9-11 | Page 10 | software baseline results | alignment/pipeline speedups | 主要性能结果 | 必读 |
| Figure 12-13 | Page 11 | hardware baseline results | vs GACT/SillaX | 硬件对比 | 看 iso conditions |
| Figure 14 | Page 12 | edit distance | vs Edlib | 通用 ASM 价值 | 重点 |

## Tables

| 表编号 | 原文位置 | 表的主题 | 主要结论 | 为什么重要 | 阅读建议 |
|---|---|---|---|---|---|
| Table 1 | Page 10 | area/power breakdown | 单 accelerator 0.334mm²/101mW，32 vaults 3.23W | 支撑低功耗 | 必读 |

## Equations

| 公式编号 | 原文位置 | 公式作用 | 符号解释 | 直观理解 | 是否需要重点掌握 |
|---|---|---|---|---|---|
| Algorithm 1 | Page 4 | Bitap baseline | R[d], PM, k, edit distance | GenASM 改进对象 | 是 |
| Algorithm 2 | Page 6 | GenASM-TB traceback | W/O/window/bitvectors/CIGAR | 输出 alignment 的方法 | 是 |
| Complexity expression | Page 12 | 改进来源分析 | m,k,P,w,W,O | divide-and-conquer 降低 DC cycles | 中 |""",
        "terms": """# Terminology

| English Term | 中文翻译 | 出现位置 | 简明解释 | 是否核心术语 |
|---|---|---|---|---|
| GenASM | GenASM 框架 | Page 1-2 | 面向 genome ASM 的算法/硬件框架 | 是 |
| Approximate String Matching (ASM) | 近似字符串匹配 | Page 1-3 | 允许 edits 的字符串匹配 | 是 |
| Bitap | Bitap 算法 | Page 2-4 | bitvector-based ASM algorithm | 是 |
| GenASM-DC | distance calculation 单元 | Page 5 | 生成 bitvectors 并计算 edit distance | 是 |
| GenASM-TB | traceback 单元 | Page 6 | 从 bitvectors 恢复 alignment/CIGAR | 是 |
| Systolic Array | 脉动阵列 | Page 7 | 高并行硬件结构 | 是 |
| DC-SRAM/TB-SRAM | DC/TB 专用 SRAM | Page 7-8 | 存储中间 bitvectors，降低带宽 | 是 |
| CIGAR String | CIGAR 字符串 | Page 3, Page 6 | 表示 alignment edits 的格式 | 中 |
| False Accept Rate | 错误接受率 | Page 12 | dissimilar sequences 被误认为相似 | 是 |
| False Reject Rate | 错误拒绝率 | Page 12 | similar sequences 被误丢弃 | 是 |
| 3D-Stacked Memory | 3D 堆叠内存 | Page 8 | logic layer + vault parallelism | 是 |""",
        "limitations": """# Limitations and Questions

## 1. 作者明确承认的局限
- pre-alignment filtering for long reads 未评估，留给未来；位置：Page 8。
- 一些 use cases 只讨论未量化，包括 de novo overlap、indexing、WGA、generic text search；位置：Page 13。
- GenASM-TB 对更多 scoring order/configurability 的支持留给未来；位置：Page 11 footnote。

## 2. 论文中隐含的局限
- 多数系统结果基于综合和模拟，不是完整芯片实测。
- 部分 baseline 结果来自原论文，比较公平性依赖参数假设。
- PIM 部署需要 3D-stacked memory logic layer 和软件集成。

## 3. 实验设计可能存在的问题
- 端到端 pipeline speedup 只替换 alignment step，真实系统还需考虑 I/O、format conversion、scheduling。
- accuracy comparison 与 scoring function/window overlap 参数有关。

## 4. 方法可能不适用的场景
- 需要复杂 affine gap scoring 或非标准 alignment semantics 的工具可能需要扩展 TB。
- 非 DNA 大 alphabet text search 会增加 pattern bitmask/storage 成本。

## 5. 我阅读时应该追问的问题
- GenASM 如何集成到真实 Minimap2/BWA-MEM pipeline？
- candidate location 由软件 filtering 提供时，host-accelerator data movement 多大？
- 对 ultra-long reads 和高 error ONT reads，window/overlap 如何调？
- GenASM 与 newer GPU/FPGA aligners 比较是否仍领先？

## 6. 后续可以继续阅读的方向
- Accelerating Genome Analysis primer。
- Darwin、GenAx/SillaX、Shouji、SneakySnake。
- PIM/3D-stacked memory accelerators for genome analysis。""",
    },
}


def checklist(title: str) -> str:
    return f"""# Reading Checklist

- [ ] 我能用一句话解释 `{title}` 解决的问题
- [ ] 我能指出本文的核心方法或论证主线
- [ ] 我能说清楚最重要的图或表在哪里
- [ ] 我能解释关键指标、实验对象或引用结果
- [ ] 我能区分作者明确结论和本文笔记中的推断
- [ ] 我能指出本文的主要局限
- [ ] 我知道这篇文章应和哪些 LEC3 文献联读
- [ ] 我知道哪些结论需要回到 PDF 精确复核
"""


for slug, p in DATA.items():
    base = f"papers/{slug}"
    arxiv = slug if slug[0].isdigit() else "未找到"
    pdf = f"`paper reading/sources/LEC3/{slug}.pdf`"
    write(f"{base}/metadata.md", f"""# Paper Metadata

- Title: {p['title']}
- Chinese Title: {p['zh']}
- Authors: {p['authors']}
- Year: {p['year']}
- Venue / Journal / Conference: {p['venue']}
- DOI: {p['doi']}
- arXiv ID: {arxiv}
- URL: {p['url']}
- PDF Source: {pdf}
- Code / Project Page: 未找到
- Dataset: {p['dataset']}
- Main Topic: {p['topic']}
- Keywords: {p['keywords']}
- Reading Status: 第三轮深度阅读完成
- Full Text Available: Yes
- Notes: {COMMON_NOTE}""")
    write(f"{base}/reading_summary.zh.md", p["summary"])
    write(f"{base}/key_points_with_locations.zh.md", p["key"])
    write(f"{base}/full_translation.zh.md", p["translation"])
    write(f"{base}/figures_tables_equations_notes.zh.md", p["figures"])
    write(f"{base}/terminology.zh.md", p["terms"])
    write(f"{base}/limitations_and_questions.zh.md", p["limitations"])
    write(f"{base}/reading_checklist.md", checklist(p["title"]))
    write(f"{base}/extraction_log.md", f"""# Extraction Log

- Input Type: GitHub repository PDF
- Source: {pdf}
- Access Status: 已下载并可读取
- Full Text Retrieved: Yes
- PDF Pages: 见 `metadata.md` 或 `00_INDEX.md`
- Sections Detected: Yes
- Figures Detected: Yes
- Tables Detected: Yes / 若文中无核心表则已注明
- Equations Detected: Yes / 若文中无核心公式则已注明
- Appendix Detected: 根据 PDF 文本，若未发现则未发现明显 appendix
- Supplementary Material Detected: 未确认
- OCR Used: No
- Missing Content: 图像本体未做视觉 OCR；部分图中细粒度数值需回 PDF 查看
- Parsing Problems: pdftotext 对双栏论文、作者列表、图表换行存在不稳定
- Uncertain Parts: 部分元数据 DOI/URL 若 PDF 未明确展示则标注未找到
- Need User Action: 如需逐字全文翻译或图像级表格复核，请指定重点页并确认版权授权
- Quality Check: 已覆盖全文结构、主要方法/论证、实验或引用结果、图表、术语、局限和原文位置；`full_translation.zh.md` 为逐节中文详译/译述，不是逐字全文翻译
- Batch Status: 第三轮深度阅读完成""")
