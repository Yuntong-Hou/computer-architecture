# Cross-Paper Synthesis

## 1. 这些文献共同关注的问题

这些论文共同围绕一个问题展开：现代系统的数据移动成本越来越高，传统 processor-centric 架构把大量时间和能耗花在 CPU/GPU 与内存之间搬运数据。LEC4 的论文从四个层次回应这个问题：DRAM 内数据移动、DRAM 内逻辑计算、PIM/NDP 编程与系统接口、以及真实商用 DRAM 行为探索。

## 2. 方法之间的关系

- `stone_logic_in_memory_1970` 提供早期思想源头：把带逻辑的 memory/cache 暴露为 sector-level operations。
- `rowclone_micro13` 是数据移动 primitive，后续 Ambit、SIMDRAM、PiDRAM、LISA 等都直接或间接依赖它。
- `lisa-dram_hpca16`、`figaro-*`、`network-on-memory-*` 继续扩展数据移动范围：subarray 内、subarray 间、bank 间分别对应不同瓶颈。
- `in-dram-bulk-and-or-*`、`ambit-*`、`1905.09822v3`、`simdram_asplos21` 形成 DRAM 内 bitwise logic 主线。
- `micro19-gao`、`micro22-gao`、`DRAM Bender`、`FCDRAM`、`SiMRA`、`PuDHammer` 关注商用 DRAM 在非标准时序、多行激活和可靠性/安全方面的真实行为。
- `SimplePIM`、`DaPPA`、`PiDRAM`、`PIM-enabled instructions` 关注如何让 PIM/PuM 被程序和系统真正使用。

## 3. 技术路线对比

- 修改 DRAM 或控制逻辑路线：RowClone、LISA、Ambit、SIMDRAM、MIMDRAM、Proteus。优点是机制清晰、性能强；缺点是需要厂商和系统栈支持。
- 使用商用 DRAM 非标准行为路线：ComputeDRAM、FracDRAM、FCDRAM、SiMRA、DRAM Bender。优点是证明门槛低；缺点是可靠性、vendor dependence 和温度/电压敏感性强。
- 近数据/逻辑层路线：TOM、PIM-enabled instructions。优点是更接近可编程计算；缺点是不能直接利用 DRAM array 内部并行性。
- 编程框架路线：SimplePIM、DaPPA、PiDRAM。优点是降低使用门槛；缺点是性能高度依赖硬件平台和 runtime 实现。

## 4. 结论是否一致

总体一致：减少数据移动能显著提升性能和能效。但各文献也共同说明，收益不是自动出现的。数据布局、cache locality、subarray/bank 位置、coherence、dirty cache lines、温度/电压、workload regularity 和编程模型都会决定最终收益。

## 5. 争议点或不确定点

- 多行激活和 out-of-spec timing 在真实 DDR4/DDR5/HBM 上能否可靠、可量产。
- ECC、memory encryption、RowHammer mitigation 与 in-DRAM computation 如何共存。
- PIM/PuM 的编译器和 runtime 能否自动完成数据布局、transposition、cache flush 和同步。
- 实验中 microbenchmark 的巨大收益能否转化为真实端到端应用收益。

## 6. 哪些论文适合先读

建议先读 `rowclone_micro13`、`ambit-bulk-bitwise-dram_micro17`、`lisa-dram_hpca16`、`simdram_asplos21`。这四篇构成 LEC4 的 DRAM 内数据移动和逻辑计算骨架。

## 7. 哪些论文适合深入读

如果关注系统落地，深入读 `pim-enabled-instructons-for-low-overhead-pim_isca15`、`2111.00082v6`、`SimplePIM_pact23`、`2310.10168v2`。如果关注真实 DRAM 行为和可靠性，深入读 `micro19-gao`、`micro22-gao`、`2211.05838v6`、`2402.18736v2`、`2506.12947v1`。

## 8. 我的学习路线建议

先建立 DRAM subarray、row buffer、ACTIVATE/PRECHARGE、sense amplifier 的基础；再学习 RowClone/LISA 的数据移动；然后学习 Ambit/SIMDRAM 的 MAJ/NOT 逻辑；最后回到系统层，比较 PEI、PiDRAM、SimplePIM、DaPPA 如何把 primitive 变成可用的软件接口。

## 9. 后续值得补充阅读的方向

- DDR5/HBM/CXL 环境下的 PIM/PuM 支持。
- PIM cache coherence、memory consistency 和 security。
- PIM compiler、DSL、runtime 和 data placement。
- RowHammer/TRR/PRAC 与 PuD/PuM interaction。
- UPMEM 等商用 PIM 平台的新一代软件栈。
