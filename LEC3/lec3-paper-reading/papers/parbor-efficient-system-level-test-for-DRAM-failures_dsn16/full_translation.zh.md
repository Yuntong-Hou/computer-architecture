# Full Chinese Translation

## Title

原文标题：PARBOR: An Efficient System-Level Technique to Detect Data-Dependent Failures in DRAM

中文标题：PARBOR：高效检测 DRAM data-dependent failures 的系统级技术

> 翻译说明：本文件按原文结构做高完整度中文详译/译述，覆盖地址 scrambling、strongly coupled cells、PARBOR 递归并行算法、真实芯片结果、DC-REF 和工程启示。参考文献不逐条翻译。

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

许多 DRAM failures 依赖物理相邻 cells 的数据模式。如果系统级测试不知道哪些 system addresses 对应物理邻居，就很难构造 worst-case pattern。DRAM vendor 内部常使用 address scrambling/remapping，使系统地址相邻不等于物理 cell 相邻。PARBOR 提出一种无需知道 vendor 内部映射的系统级方法，通过故障行为推断物理 neighbor cells 在 system address space 中的位置。

PARBOR 利用 strongly coupled cells 的特性：改变一个关键邻居就可能触发 victim failure。它递归地将候选地址空间分块，并并行测试多行，显著减少测试数量。作者在 144 颗真实 DRAM chips 上展示，只需 66-90 tests 即可定位 neighbor cell locations；相比 naive exhaustive test 减少 745,654x 测试数。PARBOR 比 random-pattern test 平均多发现 21.9% failures，并支持 data-content-aware refresh（DC-REF）减少 refresh。

## 1. Introduction / 引言

### 原文位置
Page 1-2 / Motivation

### 中文翻译

DRAM data-dependent failures 由邻近 cells 的数据模式触发。例如 victim cell 的保持能力可能取决于左右邻居存储 0 还是 1。理想测试应设置物理邻居为 worst-case pattern，再观察 victim 是否失败。

系统级测试的困难是地址 scrambling。DRAM 内部为了布局、良率、性能或安全，会把 system address 映射到内部 row/column/cell 位置。系统看到的连续地址不一定是物理相邻 cells。若测试程序按系统地址构造 checkerboard pattern，内部物理邻居可能并不是预期模式，导致漏检。

naive 方法可以穷举所有可能邻居组合，但成本不可接受。论文指出，在 8K-cell row 中穷举两个邻居约需 49 days；三/四邻居会达到 1115 years/9.1M years。因此需要利用 DRAM 结构规律和 failure behavior 降低复杂度。

## 2. Coupling Model and Address Scrambling / 耦合模型与地址扰乱

### 原文位置
Page 2-4 / Figures 1-2

### 中文翻译

Figure 1 展示 address scrambling：system-level bit order 与 physical cell adjacency 不一致。Figure 2 区分 strong coupling 和 weak coupling。Strongly coupled cells 指 victim failure 对某个邻居状态高度敏感，只要该邻居取特定值就容易失败；weak coupling 则需要多个邻居组合或更复杂条件。

PARBOR 主要利用 strongly coupled cells。若一个 victim 的 failure 可以通过改变单个邻居触发，那么测试算法可通过观察 failure 是否出现来推断哪个地址块包含关键邻居。这个性质使复杂度从 O(n^2) 降低到更接近 O(n) 甚至更少。

## 3. PARBOR Algorithm / PARBOR 算法

### 原文位置
Page 4-7 / Section 5

### 中文翻译

PARBOR 首先选择 sample victim bits，并构造测试 pattern。它将候选 system address space 分成多个块，对不同块设置不同数据模式，然后并行测试多行。若某个 victim failure 出现，说明关键物理邻居可能位于某些块中。算法递归缩小候选范围，直到推断出左右邻居在 system address space 中的距离。

为了过滤 random failures，PARBOR 使用 failure distance frequency ranking。真正的物理邻居距离会在多个 victims 中反复出现，而随机错误的距离分布更分散。通过统计高频距离，算法识别最可能的 neighbor mapping。

PARBOR 的效率来自三个因素：利用 strongly coupled cells、利用 DRAM 内部组织规律、并行测试多个 rows/blocks。它不需要 vendor 公开 mapping，但利用了 DRAM organization 的 regularity。

## 4. Experimental Results / 实验结果

### 原文位置
Page 7-9 / Figure 12 and related results

### 中文翻译

作者使用 FPGA infrastructure 测试 144 颗真实 DRAM chips。PARBOR 仅需 66-90 tests 即可定位 neighbor cell locations，相比 naive exhaustive test 减少 745,654x。与优化 O(n) test 相比，也减少约 90x。

Page 8, Figure 12 显示，PARBOR 比 random-pattern test 平均多发现 21.9% failures。在每个 tested module 中，它多发现 1K 到 45K failures，总 detected failures 增加 2%-55%。这说明理解物理邻接关系对 DRAM failure testing 非常关键。

## 5. DC-REF / Data-Content-Aware Refresh

### 原文位置
Page 10-11 / Figure 16

### 中文翻译

PARBOR 可支持 DC-REF。其思想是：如果系统知道哪些 data patterns 会导致 retention/data-dependent failures，就可以根据实际数据内容决定是否需要更保守 refresh。对于没有处于 worst-case pattern 的 rows，可降低 refresh 频率。

模拟结果显示，DC-REF 可将 refreshes 减少 73%，在 32Gbit DRAM、8-core SPEC workloads 上提升性能 18%。这说明 neighbor-aware testing 不只是提高测试覆盖率，也能支持更积极的 refresh optimization。

工程上，DC-REF 需要运行时监控 row data content 或维护 pattern 风险信息，实际硬件开销和数据一致性需要进一步设计。

## 6. Limitations / 局限性

### 原文位置
Page 10 / Section 7.3

### 中文翻译

PARBOR 依赖 DRAM internal organization 的 regularity。若厂商大量 remap columns/cells，或不同区域映射差异很大，neighbor inference 覆盖率会下降。样本太小时，random failures 也可能干扰 distance ranking。

此外，不同工艺世代、3D/HBM 组织、更强 redundancy/remapping 可能改变物理邻接和耦合关系。PARBOR 的思想可迁移，但参数和假设需要重新验证。

## 7. Conclusion / 结论

### 原文位置
Page 11 / Conclusion

### 中文翻译

PARBOR 证明，即使 DRAM vendor 不公开内部地址映射，系统仍可通过 failure behavior 推断 physical neighbor cells 的 system-level 位置。了解物理邻接关系显著提高 data-dependent failure 检测能力，并可用于 refresh optimization。

## 硬件工程师学习提炼

1. PARBOR 说明 DRAM testing 不能只看系统地址 pattern，必须理解物理邻接。
2. 重点回看 Figure 1 address scrambling、Figure 2 coupling、Section 5 algorithm、Figure 12 failure detection、Figure 16 DC-REF。
3. 对工作启发是：当 vendor mapping 不透明时，可以利用故障统计反推隐藏结构，但要谨慎处理 remap 和随机错误。
4. 它与 RowHammer、retention/VRT、MEMCON 一起构成“真实 DRAM 物理行为驱动系统策略”的主线。
