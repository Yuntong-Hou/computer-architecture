# 中文阅读摘要

## 1. 一句话总结
Panopticon 将每行 activation counter 放入 DRAM 内部 counter mats，并复用 row decoder 与 DDR4 ALERTn 信号，以仅修改 DRAM 的方式实现完整 RowHammer 防御。

## 2. 研究背景
已有 RowHammer tracking/sampling/partitioning/clean-slate 方案要么需要大量 SRAM/CAM，要么依赖 memory controller、DRAM、OS 多方协作，难以部署；DDR4 仍受 multi-row RowHammer attacks 影响。

## 3. 核心问题
- 如何避免 Graphene/TWiCe/BlockHammer 等方案的大量 fast-memory 状态？
- DRAM 内部如何为每行维护 counter 而不拖慢普通访问？
- 不修改 DDR4 controller/protocol 时，DRAM 如何请求时间刷新 victim rows？
- service queue 是否可能被攻击者填满或连续触发？

## 4. 核心贡献
- 提出 complete in-DRAM RowHammer mitigation，DDR4 场景除 DRAM 外无需修改其他硬件。
- 用 thin 16-bit counter mats 为每条 row 存储 counter，并复用 DRAM row decoding logic 做 lookup。
- 用 threshold bit 替代完整阈值比较，避免昂贵 counter reset。
- 用 service queue 记录需服务的 aggressor rows，并刷新潜在 victim rows。
- 复用 DDR4 ALERTn 信号暂停 memory controller，为 mitigation 争取时间。

## 5. 方法概述
Panopticon 在 DRAM bank 内增加 counter mats、incrementer/testing logic、service queue 和 ALERTn state machine。每次 ACTIVATE 同步更新对应 row counter；threshold bit toggle 时将 row address 入队；收到 REF 或队列需要服务时刷新邻近 victim rows，必要时 assert ALERTn 让 controller 暂停发命令。

## 6. 实验设计
论文主要进行 architecture/security analysis，而非完整系统性能评估；比较状态开销，分析 service queue 被连续占用或填满的攻击可行性，讨论 counter mats power/space overhead。

## 7. 主要结果
- Graphene 在 DDR4 每 channel 需 39.23KB CAM、每 CPU 约 156.9KB；BlockHammer/TWiCe 需求更高。（Page 1-2, Table I）
- Panopticon service queue 只需 8 entries/bank；DDR4 row address 18 bits 时约 144 bits/bank，远小于 Graphene 2511 bits/bank。（Page 5, Section V-D）
- Panopticon 用 threshold bit，如 b10 toggle 时每 1024 activations 入队一次，避免比较完整 counter value。（Page 3-5, Figure 1/Figure 5）
- 安全分析显示若不能请求 controller 时间，攻击者可在较短时间内填满 service queue，因此 ALERTn 机制是必要条件。（Page 5-6, Figures 6-7）
- 16-bit counter 可支持最高 65,536 activations threshold，适合现代较低 RowHammer threshold 场景。（Page 6, Section VII-C）

## 8. 关键结论
Panopticon 的核心价值是把 RowHammer 防御状态和 victim refresh 能力都放进 DRAM 内部，减少跨供应商协议变更；但它必须拥有向 controller 请求时间的机制。

## 9. 局限性
作者明确或设计中直接体现的局限：
- 若没有 ALERTn 或类似方式请求额外时间，攻击者可通过填满 service queue 破坏安全性。（Page 5-6, Figures 6-7）
- counter mats 的实际 power/space overhead 需要 DRAM vendor 精确评估。（Page 6, Section VII-C）

我基于论文范围推断的潜在问题：
- Panopticon 需要 DRAM 内部设计改动，仍依赖厂商采用和验证，且对 DDR5/HBM 需重新适配。（推断，基于 in-DRAM architecture）
- 论文偏设计和安全分析，缺少基于完整 workload 的性能/能耗评估。（推断，基于 evaluation scope）

## 10. 适合我重点关注的内容
重点读 Table I 状态开销、Figure 1 threshold bit/service queue、Figures 4-5 counter mat/incrementer、Figures 6-7 queue attack 分析。

## 11. 和其他文献的关系
Panopticon 与 DDR5 RFM/PRHT、PRAC/Graphene/TWiCe 构成 RowHammer 防御谱系：它更强调单 DRAM vendor 可独立部署。
