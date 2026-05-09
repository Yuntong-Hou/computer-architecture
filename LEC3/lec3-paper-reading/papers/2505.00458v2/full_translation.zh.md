# Full Chinese Translation

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
作者最后用强烈的语气指出，如果系统继续在 processor-centric paradigm 上反复投入，却期待根本不同的结果，就会持续付出性能、能耗、面积和复杂度代价。好消息是，PRAC、UPMEM、DRAM PIM prototypes 和先进封装技术已经让 memory-centric future 更接近现实。真正的问题变成：体系结构、标准、软件和产业界是否愿意推动这一转变。
