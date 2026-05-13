# Full Chinese Translation

> 处理说明：本文件为按新标准扩写后的高完整度中文学习译文/译述。它按原论文结构覆盖摘要、背景、机制、算法、比较、实验、结论与附录思想，保留 DSAC、TRR、RowHammer、Stochastic Replacement、Approximate Counting、Maximum Disturbance 等英文术语。参考文献列表保留英文，不逐条翻译。图表、公式的精确排版建议回 PDF 核对。

## Title

原文标题：DSAC: Low-Cost Rowhammer Mitigation Using In-DRAM Stochastic and Approximate Counting Algorithm

中文标题：DSAC：使用 DRAM 内随机与近似计数算法的低成本 RowHammer 缓解机制

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

随着 DRAM scaling 持续推进，每 bit 成本降低，但单个 DRAM cell 的电荷余量、隔离能力和抗干扰能力也随之下降。RowHammer threshold 因此不断降低，即攻击者触发 victim row bit flip 所需的 aggressor row activation 次数越来越少。由于 RowHammer 可以完全由软件访问模式触发，它不只是器件级可靠性问题，也会成为系统级安全问题。

现代 DRAM 通常采用 Target Row Refresh（TRR）思路：当某些 row 被频繁激活时，系统需要刷新其邻近 victim rows，防止 victim cells 因耦合干扰丢失数据。已有研究主要围绕“如何识别最频繁访问的 row”展开。论文指出，如果 TRR 放在 memory controller 中实现，控制器往往不知道真实 RowHammer threshold、内部 physical row mapping 和厂商私有防护细节，可能导致两类问题：刷新不足会留下安全漏洞，刷新过度会浪费带宽和能耗。

因此，本文关注 in-DRAM TRR algorithm，也就是把检测逻辑尽可能放入 DRAM 内部。Counter-based algorithms 通常比纯 probabilistic algorithms 更可控，但 DRAM die 内部面积预算极小，不可能给大量 row 配备大规模精确 counters。作者认为，现有 counter-based methods 的关键弱点是 decoy-rows：攻击者可以访问许多“诱饵行”，它们单行访问次数不超过真正 aggressor rows，却会污染 count table，把真正危险的 rows 挤出去。本文提出 DSAC，用 Stochastic Replacement 过滤 decoy-rows，并用 Approximate Counting 降低计数结构成本。实验显示，在作者设置下，DSAC 的 Maximum Disturbance 比 state-of-the-art counter-based algorithm 低 49x。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

DRAM cell 的基本结构是 capacitor 加 access transistor。由于 capacitor 中的电荷会泄漏，DRAM 必须周期性 refresh。工艺缩小以后，cell 之间距离缩短，wordline、bitline、substrate、well 等结构之间的干扰增强，访问某一 row 会更容易影响相邻 row 中 cell 的电荷状态。RowHammer 现象正是这种 activation-induced disturbance 的代表：攻击者反复激活 aggressor rows，使邻近 victim rows 在刷新前出现 bit flips。

RowHammer 的危险在于它跨越了传统硬件/软件边界。软件不需要直接访问 victim row，只要能构造高频 DRAM activation，就可能诱导硬件错误。已有攻击已经覆盖本地进程、虚拟机、浏览器、网络、移动设备等场景。对系统设计者来说，RowHammer 不是“坏 DIMM 才会发生”的随机故障，而是可以被主动塑造的 adversarial access pattern。

TRR 的核心思想是检测 frequently activated rows，然后刷新它们附近的 victim rows。论文区分了几种实现位置：memory-controller based TRR、memory-controller aided TRR、in-DRAM TRR。控制器实现的好处是逻辑灵活、可更新，但坏处是缺少 DRAM 内部信息；DRAM 内部实现更接近物理真实情况，但面积、功耗、验证和标准接口约束更强。本文选择研究后者，因为作者认为真正可扩展、低开销的 RowHammer 防护最终需要 DRAM 内部参与。

引言中另一个重要动机是：现代攻击不一定只用两个 aggressor rows。TRRespass 等研究说明，攻击者可以使用 many-sided hammering 和复杂访问序列绕过厂商 TRR。此时，简单记录“最热的几个 row”会变得脆弱，因为攻击者可以故意制造许多 decoy-rows，让有限 counter table 失去真正的高风险对象。

## 2. DRAM Background / DRAM 背景

### 原文位置

Page 2 / Background

### 中文翻译

论文回顾了 DRAM 访问流程。Memory controller 向 DRAM rank/bank 发送 ACT、READ/WRITE、PRE、REF 等命令。一个 bank 内部包含大量 rows 和 columns。访问某个 row 时，必须先用 ACT 打开该 row，把 cell 中的数据搬到 row buffer/sense amplifiers；访问结束或切换到其它 row 前，需要用 PRE 关闭当前 row。

在 RowHammer 语境下，关键不是 READ 本身，而是 ACT/PRE 循环带来的 wordline toggling。每次 activation 都会使 aggressor row 的 wordline 拉高并连接 cells 与 bitlines。高频重复这一动作，会通过多种物理路径影响邻近 victim rows。随着工艺缩小，6F2 cell layout、buried wordline、saddle-fin transistor 等设计虽然提高密度，但也改变了干扰耦合路径，使 activation-induced bit-flips 更难用单一模型解释。

对硬件工程师来说，这一节的价值在于把 RowHammer 防护问题落到命令时序和物理结构上：防护逻辑不能只看 cache miss 或 load/store 数量，而要看底层 row activation count、row open time、refresh interval 和 bank/subarray 内部布局。

## 3. Activation-Induced Bit-Flip Mechanisms / 激活诱导位翻转机制

### 原文位置

Page 2 - Page 3 / Section III

### 中文翻译

作者把 activation-induced bit-flips 分成两类：Passing Gate Effect 和 RowHammer。

Passing Gate Effect 主要与 row activation time 过长有关。当 aggressor row 打开时间超过标准 minimum activation time 时，电荷泄漏、电子注入或耦合影响会增加。直观理解是，某一 row 被“打开太久”，邻近结构受到的持续扰动更强。

RowHammer 则主要与 activation frequency 有关。即使每次 row activation 都只持续最短合法时间，如果 aggressor row 被反复打开和关闭，victim rows 也会逐步积累干扰并出现 bit flip。直观理解是，某一 row 被“打开太频繁”，每次扰动不大，但重复次数足够多。

这一区分对本文方法非常重要。传统 RowHammer 防护多关注 activation count，但如果 row open time 也会影响错误风险，只看 count 不够。作者因此提出 Time-Weighted Counting，用 activation time 给 count 增量加权，试图同时覆盖“开太久”和“开太频繁”两种风险。

工程启示是：未来 DRAM 防护不应只依赖一个统一 hammer count 阈值。Memory controller 的 open-page policy、refresh policy、power-down/self-refresh 交互、QoS 调度都可能改变 row open time 和 activation rate，从而改变真实风险。

## 4. RowHammer Vulnerability in System / 系统中的 RowHammer 脆弱性

### 原文位置

Page 3 - Page 4 / Section IV

### 中文翻译

论文讨论 RowHammer 在系统中的防护位置。若 memory controller 独立实现 TRR，它需要根据外部可见地址和命令流推断危险 rows。但 DRAM 内部可能存在地址重映射、备用行修复、subarray 组织、bank group 细节和厂商私有 TRR。控制器不知道真实物理相邻关系，也不知道每一代/每一颗芯片的实际 RowHammer threshold。因此，controller-side 防护容易出现 mismatch。

如果控制器为了安全采用非常保守的阈值，就会触发更多 preventive refresh，牺牲性能和能效。如果阈值过宽松，攻击者可能在刷新前触发 bit flip。Memory-controller aided TRR 试图让控制器发出额外命令协助 DRAM，但论文指出，这也会带来 command bandwidth 开销，并可能与 DRAM 内部现有机制冲突。

论文还讨论 MR4 和 refresh interval 的问题。MR4 可以让系统根据温度等因素调整 refresh 行为，延长 refresh command interval 有助于降低功耗、释放 command bandwidth，但也会减少普通 refresh 自然消除 RowHammer 风险的机会。换言之，节能优化可能放大安全压力。

硬件工程视角下，这里应关注防护和功耗管理之间的耦合。实际产品里，低功耗模式、温度补偿 refresh、bank-level refresh、fine granularity refresh、QoS scheduler 都可能改变攻击窗口。RowHammer 防护不是一个独立小模块，而是会和内存控制器时序策略产生系统级耦合。

## 5. Time-Weighted Counting / 时间加权计数

### 原文位置

Page 4 - Page 6 / Figure 8

### 中文翻译

Time-Weighted Counting 是作者针对 Passing Gate Effect 的补充设计。传统计数方法通常把每次 activation 视为相同权重，即打开一次 row 就让该 row counter 加一。但如果 row open time 也会影响干扰强度，那么一次长时间 activation 的风险应高于一次最短时间 activation。

作者的思路是根据 activation time 调整 count 增量。activation time 越长，对应 row 的 disturbance contribution 越大，计数权重也越高。这样，防护机制不仅能识别“访问次数很多”的 aggressor row，也能识别“单次打开时间很长”的 aggressor row。

这一设计并不是 DSAC 的全部，但它给后续 RowPress 类问题提供了重要方向。对内存控制器工程师而言，这意味着 row open policy 不能只用 row-buffer hit rate 来评价。一个 aggressive open-page policy 可能提高局部性命中率，却增加长期 row-open 风险。未来控制器可能需要在性能、能耗、RowHammer/RowPress 风险之间动态折中。

## 6. DSAC Algorithm / DSAC 算法

### 原文位置

Page 5 - Page 8 / Figures 10-14, Algorithm 1

### 中文翻译

DSAC 的核心问题定义是：在 count table 很小的情况下，如何避免 decoy-rows 把真正的 RowHammer aggressor rows 挤出表。许多 counter-based algorithms 在 table 未命中且 table 已满时，会替换当前最小 count entry 或执行类似确定性策略。攻击者可以利用这一点访问大量 decoy-rows，使这些 decoy-rows 轮流进入 table，破坏对真正 aggressor rows 的持续跟踪。

DSAC 的第一项关键设计是 Stochastic Replacement。当 incoming row 已经在 count table 中时，DSAC 更新该 entry 的 count。当 incoming row 不在 table 中且 table 未满时，DSAC 插入该 row。当 table 已满时，DSAC 不会确定性地用 incoming row 替换 min-count row，而是以与 min count 相关的概率执行替换。直观上，如果 table 中某个 row 已经积累较高 count，偶然出现的 decoy-row 很难把它替换掉；如果 incoming row 确实持续出现，它最终仍有机会进入 table。

这种概率替换的意义在于改变攻击者成本。确定性替换让攻击者能设计精确访问序列；随机替换让 decoy-row 的污染效果不稳定，真正高频 aggressor row 更可能长期保留在 table 中。DSAC 因此不是简单增加 counter 数量，而是提高每个 counter entry 的“抗污染能力”。

第二项关键设计是 Approximate Counting。DRAM 内部不适合放置大量宽 counter。DSAC 使用近似计数保留被替换 row 的 count 信息，并在有限面积下估计 row 热度。这类近似结构的工程取舍是：牺牲一点精确性，换取面积、能耗和可布线性的可接受性。

作者的算法流程可以理解为三层过滤：第一层按 row activation 建立候选；第二层用 stochastic replacement 抑制 decoy pollution；第三层用 approximate counting 降低硬件实现成本。对安全设计而言，关键不是平均检测率，而是在 adversarial pattern 下是否仍能限制 victim row 的最大未保护 disturbance。

## 7. Comparison with Prior TRR Algorithms / 与已有 TRR 算法比较

### 原文位置

Page 8 - Page 10 / Tables III-IV

### 中文翻译

论文把 DSAC 与 CRA、CBT、CAT-TWO、TWiCe、Graphene、PRA、PARA、PRoHIT、MRLoc 等算法比较。比较维度包括 deterministic/probabilistic、是否过滤 decoy-rows、是否需要 memory controller 参与、系统开销、是否能随 RowHammer threshold 降低而扩展。

PARA 类 probabilistic refresh 方案实现简单，但概率配置需要覆盖最坏情况，低阈值时代可能带来大量额外 refresh。Graphene 等 counter-based 方案更精确，但需要足够 counters，否则容易受到 decoy-rows 干扰。TWiCe、PRoHIT、MRLoc 等方法各有侧重，但未必同时满足 in-DRAM、低面积、抗 decoy 和可扩展。

作者强调 DSAC 的定位是低成本 in-DRAM defense。它不是在 controller 外部做大规模 tracking，也不是依赖大量 storage，而是试图在 DRAM die 内部有限逻辑预算下实现可用的 TRR detection。

工程上，这一比较提醒我们：评估 RowHammer defense 不能只看“能否检测 hot row”。还要看 storage granularity、counter width、per-bank/per-rank area、额外命令、与标准 timing 的交互、可验证性，以及攻击者是否能构造反例访问模式。

## 8. Evaluation Methodology / 实验方法

### 原文位置

Page 10 - Page 11 / Section VII

### 中文翻译

论文提出 Maximum Disturbance 作为 RowHammer protection index。它表示 observation period 内某个 row 在未被防护刷新处理前累计的最大 activation 次数。这个指标比单纯 detection rate 更贴近安全风险，因为真正危险的是 victim row 在刷新前承受了多少 disturbance。

实验采用 TRRespass 和 random access patterns，并使用 double-sided uniform weight。作者比较不同算法在相同 counter 数量下的 average disturbance 和 worst-case disturbance。面积、access energy 和 static power 使用 CACTI 6.0 估算。由于 DSAC 不需要额外 DRAM commands，作者没有重点评估 system performance slowdown。

这一实验设计的优点是直接针对 RowHammer 防护核心风险。局限是它仍偏合成模式和模型估计，不等同于真实芯片 tapeout 或完整系统验证。对产品团队来说，DSAC 还需要经过 RTL 实现、timing closure、PVT corner、soft error/FIT、DFT、firmware 配置、JEDEC 兼容性和安全红队测试。

## 9. Evaluation Results / 实验结果

### 原文位置

Page 10 - Page 11 / Tables V-VII, Figure 19

### 中文翻译

在 20 counters 配置下，DSAC 在 TRRespass/random 模式下的 average disturbance 分别约为 2196/2211，显著低于 Graphene 的 19450/10822。论文报告 DSAC 的 Maximum Disturbance 相比 state-of-the-art counter-based algorithm 低 49x。

当 counter 数量在 8 到 20 之间变化时，DSAC 仍维持较低 disturbance。论文报告 DSAC average disturbance 比 Graphene 低 133x。这说明 DSAC 的优势正来自“小表情况下的抗污染能力”，而不是依赖大规模精确计数。

面积和能耗结果显示，DSAC per-rank area 约 0.01 mm2，占 CPU area 约 0.01%；access energy 约 9.64 pJ，static power 约 0.71 mW。作者据此认为 DSAC 适合 in-DRAM deployment。

从硬件工程角度看，这些数值需要谨慎理解。CACTI 对 SRAM/array 结构估算有参考价值，但 DRAM die 内部新增逻辑的真实代价还包括版图位置、跨 bank 共享、信号线、测试、良率、时序余量和标准接口不可见性。DSAC 的方向有吸引力，但工程落地需要比论文估算更完整的 PPA 和验证闭环。

## 10. Appendix and Mathematical Intuition / 附录与数学直觉

### 原文位置

Appendix / Algorithm and probability analysis

### 中文翻译

附录部分主要给出 DSAC stochastic replacement 的概率分析。核心直觉是：如果一个新 row 只是 decoy，它出现次数有限，替换已有高 count row 的概率很低；如果它是真正 aggressor，它会持续出现，最终能够通过重复尝试进入并留在 table 中。

这种分析依赖访问模式假设和概率模型。它有助于说明 DSAC 为什么比确定性 min-count replacement 更稳健，但不等于对所有可能 adversarial sequences 的形式化证明。未来若用于安全产品，需要结合模型检查、攻击搜索和真实 workload trace 做补充验证。

## 11. Conclusion / 结论

### 原文位置

Page 11 - Page 12 / Conclusion

### 中文翻译

本文认为，随着 DRAM scaling，activation-induced bit-flips 会同时表现为 Passing Gate Effect 和 RowHammer。Memory-controller based TRR 存在信息不足和性能开销问题；MR4 等低功耗机制可能进一步增加防护难度。为此，作者提出 Time-Weighted Counting 和 DSAC。

DSAC 的关键贡献不是简单“再做一个 counter table”，而是识别出 decoy-rows 对有限 counter table 的破坏作用，并用 Stochastic Replacement 加 Approximate Counting 在低成本下提高鲁棒性。实验显示 DSAC 能显著降低 Maximum Disturbance，并具有较低面积和能耗估算。

## 12. 硬件工程师视角：对工作和行业的影响

### 原文位置

基于全文方法、实验和结论的工程化解读

### 中文学习笔记

1. 对 DRAM controller 设计：DSAC 说明 RowHammer 防护不应只在 controller 外部做粗粒度统计。若 controller 无法看到真实 physical adjacency 和内部 TRR 状态，安全边界会很弱。未来 controller 与 DRAM 之间可能需要更明确的协作接口。

2. 对 DRAM vendor：在 DRAM die 内增加小型计数逻辑是可行方向，但必须极度关注面积、功耗和良率。DSAC 的价值在于用算法降低 storage，而不是堆 counters。

3. 对验证团队：decoy-row attack pattern 应成为 RowHammer 验证的标准测试项。只测 double-sided hammering 或简单 many-sided hammering 不够。

4. 对系统安全：Maximum Disturbance 是比 detection rate 更好的安全指标。工程评审时应追问“在最坏攻击序列下 victim row 最多承受多少未处理 activation”，而不是只问“平均能检测多少 hot rows”。

5. 对个人学习：这篇论文适合作为理解 in-DRAM RowHammer mitigation 的算法入口。重点掌握 decoy-row 问题、Stochastic Replacement、Approximate Counting、Maximum Disturbance 四个概念，再与 PRAC、Chronus、Svärd 结合阅读。

## 13. 不确定与需回原文核对

- Page 5-8 的概率公式、replacement probability 和 approximate counting 细节需要回 PDF 对照符号。
- Tables V-VII 的数值建议结合原表复核。
- CACTI 面积/能耗估算不等于真实 DRAM die 成本。
- 参考文献保留英文，未逐条翻译。
