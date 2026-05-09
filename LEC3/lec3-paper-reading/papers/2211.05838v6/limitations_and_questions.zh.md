# Limitations and Questions

## 1. 作者明确承认的局限

- in-DRAM AND/OR 没有观察到 0% BER segments。原文位置：Page 12, Conclusion of Study #3。
- 其它使用 DRAM Bender 的 work artifacts 仍在整理中，部分未来释放。原文位置：Page 12, Section 4.4。

## 2. 论文中隐含的局限

- 三个 case studies 的 DRAM module 样本有限，仅覆盖三个 manufacturers 的少量 DDR4 modules。
- 平台虽然易用，但仍要求 FPGA、DRAM timing、硬件 bring-up 和温控知识。
- 对 DDR5、LPDDR5、HBM 的支持需要进一步扩展，不能从 DDR4/DDR3 直接外推。

## 3. 实验设计可能存在的问题

- RowHammer 结果受 temperature、mapping、module revision 和 TRR/ECC 状态影响，跨平台复现实验需严格匹配环境。
- data pattern study 测试 24 randomly selected cache blocks/rows，覆盖范围有限。
- AND/OR study 只在某一厂商芯片上观察到有效行为，且 BER 不低。

## 4. 方法可能不适用的场景

- 没有可插拔 DRAM module 或无法接入 FPGA test board 的平台。
- 需要 JEDEC-compliant production behavior 而非 timing-violation experiments 的测试。
- 要求零错误 deterministic in-DRAM computing 的应用。

## 5. 我阅读时应该追问的问题

- DRAM Bender 的 command timing resolution 与真实 DRAM minimum timing 相比是否足够细？
- RowHammer interleaving effect 是否会改变现有 defense 的 worst-case pattern？
- random 512-bit patterns 发现更多 vulnerable cells 是否意味着过去 characterization systematically underestimates vulnerability？
- DDR4 AND/OR 的 BER 是否可通过 ECC、重复计算或 approximate computing 接受？

## 6. 后续可以继续阅读的方向

- `softMC_hpca17`：理解前代 DRAM testing infrastructure。
- `RowHammer-Retrospective` 和 `2211.07613v2`：理解 RowHammer 研究脉络。
- U-TRR / QUAC-TRNG 相关论文：看 DRAM Bender 如何支撑后续研究。
