# Full Chinese Translation

## Title

原文标题：Self-Managing DRAM: A Low-Cost Framework for Enabling Autonomous and Efficient DRAM Maintenance Operations

中文标题：自管理 DRAM：支持自主且高效 DRAM 维护操作的低成本框架

原文位置：Page 1

处理说明：本文件按“完整度优先 + 硬件工程师视角”重写，覆盖 Abstract、Introduction、Background、SMD framework、maintenance mechanisms、hardware implementation、experimental methodology、results、sensitivity analysis 和 conclusion。参考文献列表保留英文，不逐条翻译。

---

## Abstract / 摘要

### 原文位置
Page 1 / Abstract

### 中文翻译

现代 DRAM 芯片要可靠运行，需要由 memory controller 管理多种 DRAM maintenance operations，例如 refresh、RowHammer protection 和 memory scrubbing。实现新的维护操作通常需要修改 DRAM interface、memory controller，甚至其他系统组件。这类修改往往只能通过新的 DRAM standard 完成，而标准制定周期很长，因此会拖慢新 DRAM 架构技术的采用。

作者提出 Self-Managing DRAM (SMD)，一种低成本 DRAM 架构，使 DRAM chip 能自主执行 in-DRAM maintenance operations。SMD 将维护操作的控制责任从 memory controller 转移到 SMD chip。为实现自主维护，SMD 对 DRAM interface 做一个简单修改：当 memory controller 访问正在维护的 DRAM region（例如 subarray 或 bank）时，SMD chip 拒绝该访问；同时，其他 region 仍可被访问。这样，SMD 可以在不进一步修改 DRAM interface、memory controller 或其他系统组件的前提下，实现新的 in-DRAM maintenance mechanisms，并让一个 region 的维护延迟与另一个 region 的数据访问延迟重叠。

评估显示，SMD 可在不增加 DDRx interface 新 pin 的情况下实现，row activation latency 只增加 0.4%，面积开销约为 45.5 mm2 DRAM chip 的 1.1%。在 20 个四核 memory-intensive workloads 上，相比基于 DDR4 的系统/DRAM 协同技术，SMD 平均加速 4.1%。SMD 还保证被拒绝的 memory accesses 能 forward progress。作者开源了 SMD 源码和数据。

### 硬件工程师视角

这篇论文的核心不是某个 refresh 或 RowHammer 算法，而是重新定义 DRAM chip 与 memory controller 的接口边界。传统 DDRx 是 controller-centric：MC 决定一切。SMD 让 DRAM 拥有有限自治权，用 ACT_NACK 向 MC 暂时拒绝访问。这类接口思想对未来 DDR/HBM/CXL memory expander 都有启发：可靠性、RowHammer、安全、scrubbing 需要更靠近 DRAM 内部状态来处理。

---

## 1. Introduction / 引言

### 原文位置
Page 1-3 / Section 1

### 中文翻译

DRAM 制造工艺缩放持续降低 bit cost，但也让 cell 更小、相邻 cell 距离更近，可靠运行更难。现代 DRAM chip 需要三类主要维护操作：DRAM refresh、RowHammer protection 和 memory scrubbing。新一代 DRAM 往往需要更激进的维护，例如缩短 refresh period、引入 targeted refresh、DDR5 RFM 和 PRAC 等 RowHammer defenses。

作者指出两个问题会阻碍有效且高效的维护机制被采用。第一，修改已有维护机制或引入新维护操作通常需要修改 DRAM interface，而这依赖 JEDEC 标准制定。DDR3 到 DDR4 间隔约 5 年，DDR4 到 DDR5 间隔约 8 年，因此标准路径很慢。第二，随着 DRAM 可靠性恶化，维护操作会更频繁、更耗时，并阻塞 memory access。例如 DDR4 periodic refresh 会让 rank 在 410 ns 内不可访问，DDR5 也会让相关 bank 暂时不可访问。

作者的目标是：1) 简化并加速新 in-DRAM maintenance operations 的实现过程；2) 让维护操作更高效。SMD 的关键思想是让 DRAM chip 自主执行维护，并只阻止访问正在维护的小区域。对于访问该区域的 ACT command，DRAM 返回 ACT_NACK；对其他区域，MC 仍可正常访问。这样，大部分 memory requests 不会被维护操作延迟。

SMD 的硬件改动包括：使用 DDR4/DDR5 已存在的单向 pin 传递 ACT_NACK；每 bank 增加小型 Lock Controller；每个 lock region 增加 row address latch，使一个 lock region 维护时另一个 lock region 可被访问。作者估算面积开销 1.1%，row activation latency 增加 0.4%。

作者用 SMD 实现三类维护机制：DRAM refresh、RowHammer protection 和 memory scrubbing，并用 Ramulator + DRAMPower 对 62 个 single-core workloads 和 60 个 four-core workloads 进行评估。关键结果是，对高 memory intensity 的 4-core workloads，SMD-Combined 平均加速 8.9%，达到 No-Refresh oracle 平均加速的 88.3%，同时降低 DRAM energy。

### 硬件工程师视角

引言最重要的工程点是“谁知道 DRAM 内部状态，谁就更适合做维护”。MC 看不到 vendor-specific retention distribution、RowHammer vulnerable rows、on-die ECC correction 细节。把维护逻辑放到 DRAM 内，能保护 vendor 内部信息，也能避免每次引入新机制都改标准和 MC。代价是接口必须支持拒绝/重试语义，MC scheduler 必须理解 ACT_NACK 和 ARI。

---

## 2. Background / 背景

### 原文位置
Page 3-4 / Section 2

### 中文翻译

论文背景部分回顾 DRAM organization、cell access 和 timing parameters。DRAM 层级通常包括 channel、rank、chip、bank、subarray、row、column。访问某一行需要 ACT 打开 row，把 cell 数据感测到 row buffer；随后 RD/WR 访问列；最后 PRE 关闭 row 并预充电 bitlines。

DRAM maintenance 主要包括 refresh、RowHammer protection 和 scrubbing。refresh 是因为 DRAM cell 电荷会泄漏；RowHammer protection 是因为频繁激活 aggressor row 会导致附近 victim row bit flips；scrubbing 是定期读取/纠正/写回，避免可纠错错误累积成不可纠错错误。

传统系统中，这些操作主要由 MC 发命令控制。缺点是 MC 不知道 DRAM 内部所有细节，而且维护命令会占用 command bus、阻塞 bank/rank，并影响 demand requests。

### 硬件工程师视角

如果你在设计 memory controller，SMD 要求你把 DRAM bank state 扩展为“precharged/open/locked/retry-pending”等更丰富状态。它不是简单加一个 NACK wire：scheduler、timing wheel、request queue fairness、row buffer policy、rank-level divergence 都要重新考虑。

---

## 3. Self-Managing DRAM / SMD 框架

### 原文位置
Page 4-7 / Section 4, Figure 2-3

### 中文翻译

SMD 通过一个 DRAM interface 变化重新划分 DRAM chip 和 memory controller 的职责。当前 DDRx/HBMx interface 基本处在 fully master-slave 端：MC 决定 DRAM 做什么。SMD 向 request-reply 方向移动一点，让 DRAM chip 能自主执行维护操作，同时通过 ACT_NACK 与 MC 协调。

### 3.1 Overview of SMD

SMD 的核心能力是 DRAM chip 可用 single-bit ACT_NACK signal 拒绝 ACT command。ACT_NACK 告诉 MC：目标 row 所属 region 正在维护，暂时不可用。借助拒绝 ACT 的能力，维护操作可以完全在 DRAM chip 内实现。

维护操作和普通 ACT 可以在同一 bank 的不同 lock regions 中并行。为支持这一点，SMD 增加 row address latch，让两个 local row decoders 能由两个独立 row addresses 驱动。当维护操作和 ACT 同时指向同一 lock region，bank 优先执行维护操作并拒绝 ACT。

### 3.2 Region Locking Mechanism

维护操作只能在 lock region 被锁定时执行。lock region 由连续 DRAM rows 组成，作者默认一个 lock region 为 16 个 subarrays。选择 subarray 粒度是因为维护操作使用 subarray 内 local row buffer。对于 open-bitline DRAM，相邻 subarrays 共享 sense amplifiers，因此当一个 region 被维护时，SMD 也会拒绝访问相邻 subarray，以避免冲突。

维护机制不能锁定已有 active row 的 region；它必须等待 MC 预充电该 row。DRAM standard 限制 row 最长 active time，因此维护操作最多等待 9x tREFI。

### 3.3 Controlling an SMD Chip

引入 ACT_NACK 后，MC 不再需要发 refresh 等维护命令，也不需要管理相关 timing parameters。MC 仍维护 bank state，仍遵守 ACT/RD/WR/PRE 等普通命令 timing。

当 MC 收到 ACT_NACK，它等待 ACT Retry Interval (ARI) 后重新发同一 ACT。等待期间，MC 可以调度同 bank 其他 lock region 或其他 bank 的访问。SMD 强制同一区域维护结束后至少等待 ARI，才允许同一区域再次维护，从而保证被拒绝请求可以在维护结束后获得服务。作者经验上选择 ARI = 62.5 ns。

TACT_NACK 是 DRAM 收到 ACT 到发送 ACT_NACK 的延迟。它包含 ACT 传播、判断 row 是否属于 locked region、ACT_NACK 返回三部分。作者假设 TACT_NACK = 5 cycles，并评估显示小 TACT_NACK 对性能影响很小，因为被拒绝的 ACT 数量占所有 ACT 的比例较低。

### 3.4 ACT_NACK Divergence Across DRAM Chips

rank 中多个 DRAM chips 通常 lock-step 工作。若不同 chip 内维护状态不同，有些 chip 对某 ACT 返回 ACT_NACK，另一些不返回，就会出现部分芯片 row 已打开、部分未打开的 divergence。作者提出三种 MC 策略：Precharge、Wait 和 Hybrid。Precharge 在发生 divergence 时关闭部分打开的 row；Wait 等待 ARI 后重试同一 ACT；Hybrid 根据 request queue 中是否有足够多访问其他 lock region 的请求来选择。

### 3.5 Forward Progress for Memory Requests

SMD 证明：如果 MC 每 ARI 重试被拒绝的请求，则该请求能 forward progress。直觉是维护操作锁定 region 的时间有限；释放锁后同一区域至少 ARI 内不会再次被维护；如果 MC 在这段窗口内重试，就不会被拒绝。

为了限制 stall time，耗时维护操作可拆成多个短操作，DRAM standard 也可规定最大维护时间。最长的 ECC scrubbing 约 350 ns，和现代 DDR4 refresh 导致的等待时间相当。

### 硬件工程师视角

SMD 的难点在边界条件：rank-level divergence、partial row open、retry fairness、request queue starvation、ACT_NACK 与 row buffer policy 的交互。硬件验证需要构造最坏模式：高 MPKI、同一 lock region hotspot、多 maintenance mechanisms 竞争、partial divergence、多 rank/channel 并发。Forward progress 证明依赖 MC 按 ARI 重试，因此 MC 不能因为调度策略长期饿死被拒绝请求。

---

## 4. SMD Maintenance Mechanisms / SMD 维护机制

### 原文位置
Page 7-10 / Section 5, Figures 4-7

### 中文翻译

### 4.1 Use Case 1: DRAM Refresh

传统 DRAM 由 MC 周期性发 REF commands。该方法有两个低效点：第一，在 refresh period 内通过 command bus 发送大量 REF 消耗能量并增加 command bus utilization；第二，REF 实际只刷新少量 rows，但可能让整个 bank/rank 不可访问。

SMD-FR 将 fixed-rate refresh 放到 DRAM 内部。SMD-FR 用 pending refresh counter、lock region counter、row address counter 跟踪刷新进度。每个 tREFI 增加 pending refresh counter。当计数大于 0 时，SMD-FR 锁定目标 region，刷新从 row address counter 指定位置开始的 RG 行。作者经验上选择 RG = 8。刷新完成后释放 region，并更新 counters。

SMD-VR 支持 variable refresh。很多 DRAM rows 实际 retention time 远大于默认 refresh period，只有少量 weak rows 需要高频 refresh。SMD-VR 用 per-bank Bloom Filter 存储 retention-weak rows 的地址。weak rows 每个 refresh period 刷新；retention-strong rows 仅每 V R_factor 个 refresh periods 刷新。作者假设 weak rows retention time 为 32 ms，strong rows 可达到 128 ms，因此 strong rows 每四个周期刷新一次。

### 4.2 Use Case 2: RowHammer Protection

RowHammer 是重复 ACT/PRE aggressor row 导致附近 victim rows bit flips。现有 DRAM 的 TRR 依赖 refresh slack time，并且已有研究证明三大厂 DDR4/LPDDR4 的 TRR 可被绕过。SMD 将 RowHammer protection 作为 DRAM 内部维护操作。

SMD-PRP 受 PARA 启发：每次 row activation 后，以概率 Pmark 将该 row 标记为 aggressor，并在 DRAM 内刷新其 neighbor rows。SMD 用 Marked Rows Table 记录每 lock region 的 marked row address 和 valid bit。SMD-PRP 不需要 MC 知道 victim rows，也不需要额外 ACT/PRE 经过 DRAM bus。

SMD-DRP 基于 Graphene。它在每 bank 维护 Counter Table，追踪一个时间窗口内最频繁激活的 N 个 rows。若某行 activation count 接近 ACTmax，SMD-DRP 刷新其 neighbor rows。作者给出计数器数量公式：N > (ACTtREFW / ACTmax) - 1。评估中 ACTmax = 512，展示即使 DRAM 对 RowHammer 非常脆弱，SMD-DRP 开销仍可接受。

### 4.3 Use Case 3: Memory Scrubbing

on-die ECC 可纠正单 bit error，但错误若长期累积，可能形成不可纠正多 bit errors。Memory scrubbing 定期读取、纠错、必要时写回，防止错误积累。

SMD-MS 在 DRAM 内部执行 scrubbing。与 rank-level ECC scrubbing 不同，in-DRAM scrubbing 可直接利用 on-die ECC，避免 MC 读出/写回所有 codewords 的带宽和能耗开销。作者还讨论了 rank-level ECC 和 in-DRAM ECC scrubbing 应结合使用：前者通常更强，后者更靠近 DRAM 内部且更高效。

### 4.4 Other Use Cases

SMD 还可支持 online DRAM error profiling、processing in/near memory、power management。对 PIM/NDP，SMD 可把 in-DRAM processing engine 视为一种 maintenance mechanism，先锁定目标 region，避免 MC 同时访问。对 power management，SMD 可实现局部 power-down，只让冷区域进入低功耗，而频繁访问区域仍可服务请求。

### 硬件工程师视角

这里最有工程价值的是统一抽象：refresh、RowHammer defense、scrubbing、online profiling、PIM 和局部 power-down 都可看成“某个 DRAM region 暂时由内部机制独占”。这给未来 memory architecture 一个通用接口：region lock + ACT_NACK + retry。对芯片团队来说，SMD 是维护操作的 substrate；对系统团队来说，关键是 MC 是否能正确处理临时不可访问和重试。

---

## 5. Hardware Implementation and Overhead / 硬件实现与开销

### 原文位置
Page 11-12 / Section 6

### 中文翻译

SMD 需要把 ACT_NACK 传给 MC。作者讨论两种方案。第一，复用 DDR4 的 alert_n pin。alert_n 原本用于告诉 MC 命令 CRC/parity error；SMD 可在访问 locked region 时也 assert alert_n。这样不需新 pin，但会让 alert_n 多语义并增加 MC 复杂度，而且 alert_n 是 open drain，置位/复位较慢。第二，引入新 pin。对于 rank-based 组织，一个 memory channel/rank 可共用一个 ACT_NACK pin。作者估计在 12-channel、4-rank DDR5 系统中需要 96 个新 pins，占 6096-pin 处理器封装约 1.6%。

DRAM chip 内部改动包括 Lock Region Bitvector (LRB) 和 per-region RA-latch。LRB 每 bank 每 lock region 一 bit，默认 16 lock regions 时只需 16 bits。作者用 CACTI 6.0 估算，LRB 每 bank 面积 32 um2，所有 LRB 占 45.5 mm2 DRAM chip 的 0.001%，访问时间 0.053 ns。RA-latch 用于让一个 lock region 维护时另一个 lock region 可被访问，所有 RA-latches 总面积约 1.1%，延迟 0.028 ns。

具体维护机制还可能有额外面积。SMD-FR 只需 77.1 um2；SMD-MS 控制逻辑类似，ECC engine 假设已有；SMD-DRP 因 Counter Table/CAM 比较昂贵，在 ACTmax=512 时需要 3.2 mm2，占 7.0%。

MC 修改较小：收到 ACT_NACK 后将 bank 标为 precharged，并按 ARI 重试。MC 还需要追踪 locked regions。对于 2 ranks、16 banks、16 lock regions，每个 locked region 需要 rank/bank/lock-region bits，共约 288 bytes 存储。

### 硬件工程师视角

面积数字要分清“接口 substrate 开销”和“具体机制开销”。SMD substrate 的 1.1% 主要来自 RA-latches；LRB 很小。真正可能昂贵的是 SMD-DRP 这类具体 RowHammer tracker。产品设计时应问：是否需要 deterministic guarantee？是否可用 probabilistic/approximate counter？ACTmax 未来降低到 128 或 64 时，计数器开销会如何变化？

---

## 6. Experimental Methodology / 实验方法

### 原文位置
Page 12-13 / Section 7, Table 1

### 中文翻译

作者扩展 Ramulator 实现并评估 SMD-FR、SMD-DRP 和 SMD-MS，使用 DRAMPower 评估 DRAM energy。仿真采用 CPU-trace driven mode，traces 来自自定义 Pintool。每个 workload fast-forward 100M instructions warm-up cache，然后仿真 500M instructions；multi-core 仿真直到每个 core 至少执行 500M instructions。

系统配置包括 4 GHz、4-wide issue CPU core，1-4 cores，8 MSHRs/core，128-entry instruction window；LLC 为每 core 4 MiB，64B cache line；MC 有 64-entry read/write queue，FR-FCFS-Cap scheduler，Cap=7；DRAM 为 DDR4-3200，32 ms refresh period，4 channels，2 ranks，bank groups/banks，128K rows per bank，512-row subarray，8 KiB row size。

workloads 包括 SPEC CPU2006、SPEC CPU2017、TPC、STREAM、MediaBench 共 62 个 single-core applications。按 LLC MPKI 分为 low、medium、high。multi-programmed workloads 随机组合成 60 个 4-core workloads，每类 memory intensity 20 个。

比较对象包括 DDR4 baseline、SMD-FR、SMD-VR、SMD-FR+SMD-PRP、SMD-FR+SMD-DRP、SMD-FR+SMD-MS、SMD-Combined、DARP-Combined、DSARP-Combined 和 No-Refresh oracle。

### 硬件工程师视角

这套实验值得学习的是比较对象设计。SMD 不只和普通 DDR4 baseline 比，还和 DARP/DSARP 这类已有 memory-controller/DRAM co-design 比，并用 No-Refresh 作为上界。实际做架构评估时，必须有 baseline、强优化 baseline 和 oracle 上界，否则很难判断收益是来自机制本身还是来自弱 baseline。

---

## 7. Performance and Energy Results / 性能与能耗结果

### 原文位置
Page 13-15 / Section 8, Figures 8-11

### 中文翻译

### 7.1 Single-core Performance

Figure 8 展示 22 个 LLC MPKI 至少为 10 的 single-core workloads。SMD-FR 平均加速 4.8%，因为它允许 refresh 与其他 lock region 的访问并行，同时消除 REF commands 对 command bus 的占用。SMD-VR 平均加速 5.5%，因为它根据 retention time 对不同 rows 使用不同 refresh rates。SMD-FR+SMD-DRP 和 SMD-FR+SMD-PRP 分别平均加速 4.8% 和 4.2%，说明 RowHammer victim refresh 的延迟几乎可与其他 region 访问重叠。SMD-FR+SMD-MS 平均加速 5.0%，即使 5 分钟 scrubbing period 很激进，scrubbing 开销也很低。SMD-Combined 平均加速 5.0%，达到 No-Refresh 平均加速的 84.7%。

### 7.2 Multi-core Performance

Figure 9 展示 60 个 4-core workloads。SMD 对 memory-intensive workloads 收益最大。SMD-Combined 对 4c-medium 和 4c-high 分别平均加速 5.1% 和 8.9%，最高为 8.2% 和 10.5%。对 4c-high，SMD-Combined 达到 No-Refresh 平均加速的 88.3%，同时仍执行 refresh、RowHammer protection 和 scrubbing。

对 4c-low，SMD 收益较小，因为非 memory-intensive workloads 本来就不太受维护操作影响，No-Refresh 上界也不高。

### 7.3 Energy Consumption

Figure 10 显示所有 SMD configurations 相比 baseline 降低 DRAM energy。原因包括：SMD 缩短执行时间，降低 background energy；消除维护命令在 DDRx bus 上传输。对 4c-medium 和 4c-high，SMD-Combined 平均降低 DRAM energy 4.8% 和 4.3%。SMD-VR 在 4c-high 上平均节能 6.9%，因为它减少不必要 refresh。

### 7.4 Comparison to DARP and DSARP

Figure 11 显示 SMD-Combined 优于 DARP-Combined 和 DSARP-Combined。对 4c-high workloads，SMD-Combined 比 DARP-Combined 和 DSARP-Combined 分别平均快 8.6% 和 4.1%。原因是 DARP 不能在维护和访问之间做真正并行；DSARP 虽可并行 refresh/access，但 MC 仍需发维护命令，占用 command bus。SMD 则由 DRAM 内部自主维护，只在冲突时产生 ACT_NACK。

### 硬件工程师视角

结果说明 SMD 的收益来自两个层面：并行化维护与访问，以及把维护命令从 DDR bus 上移走。对高带宽系统，command bus 和 timing window 也是资源，不只是 data bus bandwidth。对未来 DDR5/HBM/CXL memory，减少 controller-to-DRAM maintenance traffic 可能和减少数据搬运一样重要。

---

## 8. Design Choices and Sensitivity Analyses / 设计选择与敏感性

### 原文位置
Page 15-18 / Section 9

### 中文翻译

作者分析多个设计选择，包括是否暂停维护以优先服务 memory request、lock region 数量、refresh period、core 数量、scrubbing rate、RowHammer threshold、blast radius、SMD-PRP 与 PARA 比较，以及 ACT_NACK divergence。

SMD-PMP (Pause Maintenance Policy) 在 MC 对 locked region 发 ACT 时暂停正在进行的维护操作，让该 ACT 更早执行。对 4c-high workloads，SMD-PMP-FR 比 SMD-FR 略快，因为 ACT_NACK rate 更低。lock region 数量方面，从 2 增加到 256 会提高并行性，但超过 16 后收益递减。

这些敏感性分析表明，SMD 的设计空间不是单点固定方案。lock granularity、ARI、maintenance chunk size、priority policy、RowHammer threshold 都会影响性能、能耗和安全保证。

### 硬件工程师视角

真正产品化时，SMD 参数必须可配置。未来 DRAM 不同 die、不同温度、不同 workload、不同 RowHammer threshold，需要动态或静态调优。对 firmware/MC 来说，ARI、Cap、retry priority、locked-region tracking 可能需要暴露调试计数器，否则很难定位性能异常。

---

## 9. Conclusion / 结论

### 原文位置
Page 18 / Section 11

### 中文翻译

作者提出 SMD，一种低成本 DRAM architecture，让 DRAM chip 能自主执行 refresh、RowHammer protection、scrubbing 等 maintenance operations。SMD 通过 ACT_NACK 和 lock region 机制，只拒绝访问正在维护的小区域，并允许其他区域继续服务请求。SMD 可以降低维护操作的性能和能耗开销，并为未来 DRAM 维护机制提供更灵活的部署路径。

### 面向硬件工作的学习提炼

SMD 对硬件工程师最重要的启发是：可靠性机制不应总是放在 memory controller 或软件层。随着 RowHammer、retention、on-die ECC、scrubbing、temperature variation 变复杂，DRAM 内部知识越来越关键。未来内存系统可能需要更丰富的 request/reject/retry/metadata 接口，而不是单向命令式 DDRx 模型。

---

## References / 参考文献

### 原文位置
Page 18 onward / References

参考文献列表保留英文原文，不逐条翻译。建议配套阅读 DARP、DSARP、RAIDR、Graphene、PARA、BlockHammer、PRAC/RFM、DRAM Bender 和 Self-Managing DRAM 的开源代码。
