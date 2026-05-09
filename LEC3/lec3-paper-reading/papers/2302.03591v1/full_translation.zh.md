# Full Chinese Translation

> 说明：以下为面向学习的逐节中文详译/译述，保留关键英文术语、变量名、算法名和表格数值；参考文献不逐条翻译。

## Title

原文标题：DSAC: Low-Cost Rowhammer Mitigation Using In-DRAM Stochastic and Approximate Counting Algorithm

中文标题：DSAC：使用 DRAM 内随机与近似计数算法的低成本 RowHammer 缓解机制

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

DRAM scaling 降低了 cost per bit，但也降低了 RowHammer threshold。RowHammer 可被软件攻击利用，因此是系统级安全威胁。DRAM 已采用 Target-Row-Refresh (TRR) 来刷新可能因邻近 aggressor rows 而丢失数据的 victim rows。已有工作关注如何识别访问最频繁的 row。虽然 TRR 可在 memory controller 中实现，但 MC 缺少 RowHammer threshold 等内部信息，可能导致 TRR 过少或过多，并引入额外命令开销。因此本文关注 in-DRAM TRR algorithm。

Counter-based algorithms 通常比 probabilistic algorithms 有更高准确性和可扩展性，但现代 DRAM 对 TRR counters 数量限制极强。本文指出 decoy-rows 是 state-of-the-art counter-based algorithms 失效的根本原因。decoy-rows 的访问次数不超过真正 RowHammer rows，却可能替换 count table 中的 RowHammer rows，使 victim rows 失去 TRR 机会。本文提出 DSAC，通过 Stochastic Replacement 过滤 decoy-rows，并通过 Approximate Counting 降低面积成本。实验显示 DSAC 的 Maximum Disturbance 比 state-of-the-art counter-based algorithm 低 49x。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 2

### 中文翻译

DRAM cell 由 capacitor 和 transistor 构成，需要 refresh 保持数据。随着 DRAM cell 缩小，cell 间电磁串扰增加，导致 activation-induced bit-flips。RowHammer 作为硬件故障可被软件触发，已在服务器、移动系统、虚拟机、浏览器、网络等环境中被研究。TRR 的目标是找出频繁访问的 aggressor rows，并刷新其邻近 victim rows。

作者认为，MC-based TRR 的主要问题是缺少 DRAM 内部工艺和 RHTH 信息；MC-aided TRR 又可能因额外命令带来性能开销，甚至与 DRAM 内部算法冲突。因此需要低成本 in-DRAM TRR algorithm。

## 2. Background / 背景

### 原文位置

Page 2

### 中文翻译

论文回顾 DRAM 系统结构：memory controller 发送 commands，bank 包含 subarrays，rows 需要被 activate 后才能读写，访问其它 row 前必须 precharge。现代 DRAM 采用 6F2 cell layout、buried wordline 和 saddle-fin transistor 等结构。

## 3. Bit-Flip Mechanism / 位翻转机制

### 原文位置

Page 2 - Page 3

### 中文翻译

作者把 activation-induced bit-flips 分成两类。Passing Gate Effect 发生在 row activation time 长于标准 minimum time 时；RowHammer 发生在 activation time 是 minimum，但 row 被频繁激活时。两者都与 electrons spreading and injection 有关。直观上，Passing Gate Effect 关注“开太久”，RowHammer 关注“开太频繁”。

## 4. RowHammer Vulnerability in System / 系统中的 RowHammer 脆弱性

### 原文位置

Page 3 - Page 4

### 中文翻译

RowHammer 是可被软件触发的 hardware-fault attack，因此威胁整个系统。TRR 需要准确检测 frequently accessed rows。MC-based TRR 可能 refresh 不足或过多；MC-aided TRR 可能与 DRAM 内部算法产生 clash。MR4 允许系统增大 refresh command interval，以节省功耗和提高 command bandwidth，但这会减少普通 refresh 缓解 RowHammer 的机会，并迫使检测算法需要更多 counters。

## 5. DSAC / DSAC 算法

### 原文位置

Page 4 - Page 8

### 中文翻译

首先，Time-Weighted Counting 根据 activation time 给 row count 加权，以处理 Passing Gate Effect。activation time 越长，权重越高。

其次，作者分析 Space Saving 等 counter-based algorithms 在有限 count table 中的问题。若大量 decoy-rows 到来，它们可能替换真正 aggressor rows，使 TRR 无法及时刷新 victim rows。

DSAC 的核心是 Stochastic Replacement：当 count table 满时，新 row 不会确定性替换 min-count row，而是以某个概率替换。这个概率与 min count 相关，使访问次数较少的 decoy-row 难以替换已经积累 count 的真正 aggressor row。DSAC 还结合 Approximate Counting 记录被替换行的 count 近似信息，以降低面积成本。

## 6. Comparison with Prior TRR Algorithms / 与已有 TRR 算法比较

### 原文位置

Page 8 - Page 10

### 中文翻译

作者比较 CRA、CBT、CAT-TWO、TWiCe、Graphene、PRA、PARA、PRoHIT、MRLoc 等算法。表 III 从 deterministic/probabilistic、decoy-row filtering、system overhead、scalability for RHTH 等角度比较。作者认为多数已有算法不能有效过滤 decoy-rows，或者在 DRAM 内实现成本过高。

## 7. Evaluation / 实验评估

### 原文位置

Page 10 - Page 11

### 中文翻译

本文提出 Maximum Disturbance 作为 RowHammer protection index，即 observation period 内某个 row 未被 TRR 处理时能累积的最大 activation 数。若超过 RHTH，说明 mitigation 失败风险高。实验注入 TRRespass 和 random access patterns，并使用 double-sided uniform weight。使用 20 counters 时，DSAC 的 average disturbance 显著低于 Graphene、TWiCe、PRoHIT 等。进一步把 counters 缩小到 8-20 时，DSAC 仍保持较低 average disturbance。

面积、access energy、static power 使用 CACTI 6.0 估算。结果显示 DSAC per-rank area 约 0.01 mm2，静态功耗约 0.71 mW，低于主要 counter-based algorithms。

## 8. Conclusion / 结论

### 原文位置

Page 11 - Page 12

### 中文翻译

DRAM cell shrinkage 会加剧 Passing Gate Effect 和 RowHammer 两类 activation-induced bit-flips。MC-based TRR 可能 refresh 不足、过多或产生性能开销；MR4 虽有低功耗和高 command bandwidth 好处，却使 RowHammer mitigation 更难。本文提出 Time-Weighted Counting 和 DSAC。DSAC 的关键思想是：只有当新 row 平均出现次数超过 count table 中 min-count row 时，它才更可能替换后者，从而过滤 decoy-rows。实验显示 DSAC 的 Maximum Disturbance 比 state-of-the-art counter-based algorithm 低 49x。
