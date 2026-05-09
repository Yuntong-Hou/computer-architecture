# Full Chinese Translation

> 说明：以下为面向学习的逐节中文详译/译述，保留关键英文术语、机制名、指标名和数值；参考文献不逐条翻译。

## Title

原文标题：Self-Managing DRAM: A Low-Cost Framework for Enabling Autonomous and Efficient DRAM Maintenance Operations

中文标题：自管理 DRAM：支持自主且高效 DRAM 维护操作的低成本框架

## Abstract / 摘要

### 原文位置

Page 1 / Abstract

### 中文翻译

在现代系统中，memory controller 负责管理 DRAM maintenance operations，例如 refresh、RowHammer protection 和 memory scrubbing。要实现新的维护操作，通常需要修改 DRAM interface、memory controller，甚至其它系统组件，而这些修改往往必须等待新 DRAM standard。本文提出 Self-Managing DRAM (SMD)，让维护操作的控制责任从 memory controller 转移到 DRAM chip。SMD 只做一个简单接口修改：当某个 DRAM region 正在维护时，DRAM chip 可以拒绝 memory controller 对该区域的访问，同时允许访问其它区域。这样，SMD 既能在 DRAM 内部实现新维护机制，又能把一个区域的维护延迟和另一区域的数据访问重叠起来。评估显示，SMD 具有低面积和低 latency overhead，并在 memory-intensive workloads 上提升性能、降低 DRAM energy。

## 1. Introduction / 引言

### 原文位置

Page 1 - Page 3

### 中文翻译

DRAM cell 缩小降低了 bit cost，但也加剧了可靠性、安全性和效率挑战。现代 DRAM 需要 refresh 来保持数据，需要 RowHammer protection 来防止 read disturbance，需要 scrubbing 来提前修复错误。问题在于，当前 DRAM interface 是 processor-centric 的，memory controller 指挥一切。只要维护机制发生变化，就可能需要接口和标准变化，而 JEDEC 标准周期很长。

作者认为，DRAM vendor 具有内部工艺和可靠性知识，却无法灵活地在不暴露内部细节的前提下部署新维护机制。SMD 的目标是让 DRAM 有“breathing room”：DRAM chip 可自主维护一小块 region；memory controller 如果碰巧访问该 region，就收到 ACT_NACK 并稍后重试。

## 2. Background / 背景

### 原文位置

Page 3

### 中文翻译

DRAM 由 channel、rank、chip、bank、subarray、row 和 row buffer 构成。访问一个 row 需要 ACT command 打开 row，把数据放入 row buffer；之后用 RD/WR 读写；最后用 PRE 关闭 row。维护操作通常也需要占用 bank 或 row 资源，因此会阻塞普通 memory requests。

## 3. Motivation & Goal / 动机与目标

### 原文位置

Page 3 - Page 4

### 中文翻译

DDR5 引入 Same Bank Refresh、RFM 等新机制，说明 refresh 和 RowHammer protection 仍在变化。但每次修改都带来 interface complexity。作者希望用一次通用改动支持未来多种维护操作：DRAM 内部负责决定做什么维护，MC 只需要知道某次 ACT 是否被拒绝。

## 4. Self-Managing DRAM / SMD 设计

### 原文位置

Page 4 - Page 7

### 中文翻译

SMD 把 DRAM bank 划分成多个 lock regions。每个 region 可被 maintenance mechanism 锁定。若 MC 向锁定 region 发 ACT，DRAM 返回 ACT_NACK；若访问非锁定 region，则正常执行。MC 收到 ACT_NACK 后等待 ACT Retry Interval (ARI) 再重试，从而保证 forward progress。

SMD 的硬件包括 Lock Controller、lock region 状态、额外 row address latch，以及 ACT_NACK 物理信号。作者强调 SMD 不要求 MC 知道 DRAM 内部具体在做哪种维护操作，这对 DRAM vendor 也有吸引力，因为它不必暴露 chip-generation-specific vulnerability information。

## 5. SMD-based Maintenance Mechanisms / 基于 SMD 的维护机制

### 原文位置

Page 7 - Page 12

### 中文翻译

作者展示三类实现。第一是 refresh，包括 fixed-rate refresh (SMD-FR) 和利用 retention-time variation 的 variable-rate refresh (SMD-VR)。第二是 RowHammer protection，包括 probabilistic protection (SMD-PRP) 和 deterministic counter-based protection (SMD-DRP)。第三是 memory scrubbing (SMD-MS)，把 ECC 读改写等操作放在 DRAM 内部以减少 off-chip data movement。

这些机制共同说明：SMD 不是单一算法，而是一个框架；任何可被视为“对一小块 DRAM region 的内部维护”的操作都可能映射到 SMD。

## 6. Evaluation Methodology / 实验方法

### 原文位置

Page 12 - Page 13

### 中文翻译

作者使用 Ramulator 做 cycle-accurate simulation，并用 DRAMPower 估算能耗。系统配置基于 DDR4。工作负载包括 62 个 single-core workloads 和 60 个 four-core workloads。四核 workload 按 memory intensity 分组。比较对象包括 baseline DDR4、DARP、DSARP、No-Refresh oracle、以及多种 SMD configurations。

## 7. Performance and Energy Results / 性能与能耗结果

### 原文位置

Page 13 - Page 18

### 中文翻译

实验显示，SMD 对 memory-intensive workloads 最有用。single-core 中，SMD-Combined 平均获得 5.0% speedup，并达到 No-Refresh oracle 收益的 84.7%。四核中，SMD-Combined 对 4c-medium 和 4c-high 分别获得约 5.1% 和 8.9% 平均 speedup，并在 4c-high 上达到 No-Refresh 收益的 88.3%。能耗方面，SMD-Combined 对 4c-medium 和 4c-high 分别降低 DRAM energy 约 4.8% 和 4.3%。

与 DARP/DSARP 相比，SMD 的优势来自两点：它可以在 DRAM 内部自主维护，不需要 MC 发出大量维护命令；它可以在一个 lock region 维护时访问其它 region。作者还分析了 lock region 数量、refresh period、scrubbing rate、RowHammer threshold、neighbor row distance 等参数敏感性。

## 8. Related Work / 相关工作

### 原文位置

Page 18 - Page 19

### 中文翻译

相关工作包括修改 DRAM interface、降低 refresh overhead、RowHammer / RowPress protection、memory scrubbing、subarray-level parallelism 和 CXL。SMD 的区别在于：它不针对某一个维护机制，而是用一个低成本接口扩展，使未来维护机制可在 DRAM 内部自主执行。

## 9. Conclusion / 结论

### 原文位置

Page 19

### 中文翻译

本文提出 SMD，用一次低成本接口修改支持未来 in-DRAM maintenance operations。作者实现了 refresh、RowHammer protection 和 memory scrubbing 的 SMD 版本，并展示它们在性能、能耗和鲁棒性上的收益。作者希望 SMD 促进未来 DRAM design 的创新，并推动 memory 和 processor 之间更合理的职责划分。
