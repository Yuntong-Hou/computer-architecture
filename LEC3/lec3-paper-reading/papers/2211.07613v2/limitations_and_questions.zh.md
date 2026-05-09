# Limitations and Questions

## 1. 作者明确承认的局限

- 本文指出 RowHammer 仍未被完全理解，尤其是 aging、temperature、voltage、access patterns 的影响。原文位置：Page 5, Section 5.1。
- 作者认为现有 defenses 在未来更低 threshold 下可能面临开销或安全问题。原文位置：Page 6, Section 5.2。

## 2. 论文中隐含的局限

- 本文是 overview，不提供新实验数据。
- 对大量相关工作只能概述，机制细节、开销比较和安全证明需要回原论文。
- 未来方向依赖 system-memory co-design，但现实标准化和产业采用周期可能很长。

## 3. 实验设计可能存在的问题

本文无新实验。引用的实验来自不同论文，测试条件、DRAM types、temperature、TRR 状态、platform 都不同，不能简单横向比较所有数值。

## 4. 方法可能不适用的场景

本文不是具体方法论文，不能直接作为工程实现方案。它适合建立研究地图和问题意识。

## 5. 我阅读时应该追问的问题

- 哪些 RowHammer defenses 具有可证明安全性，哪些只是经验有效？
- DDR5 RFM/PRAC 是否真正解决 many-sided / pattern-based attacks？
- 随着 threshold 下降，正常 workload 的 activation behavior 是否会造成误触发？
- system-memory co-design 的接口应公开到什么程度？

## 6. 后续可以继续阅读的方向

- 原始 `dram-row-hammer_isca14`。
- `RowHammer-Retrospective_ieee_tcad19`。
- `DRAM Bender` 和 `SoftMC`。
- `SMD`、`DSAC`、`BlockHammer`、`Hydra`、`AQUA` 等 mitigation 论文。
